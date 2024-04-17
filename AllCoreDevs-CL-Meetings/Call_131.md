
# Consensus Layer Meeting 131 [2024-4-4]
### Meeting Date/Time: Thursday 2024/4/4 at 14:00 UTC
### Meeting Duration: 60 Mins
### Moderator: Alex Stokes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1003)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=ZqxDq1aJxHc) 
### Meeting Notes: Meenakshi Singh
___


| S.NO. | AGENDA | SUMMARY |
| ----- | ------ | ------- |
| 131.1 |   Electra Upgrade and Devnet: | Ethereum Improvement Proposals (EIPs) play a crucial role in shaping these upgrades. The three EIPs approved for inclusion in Electra are: EIP 6110, EIP 7002, EIP 7549.|
| | | Additionally, developers are working on proof of concepts for EIP 7547 (inclusion lists) to potentially include it as the fourth EIP in Electra.| 
| | |Alex Stokes and Hsiao-Wei Wang are finalizing specifications for the first Electra multi-client developer test network (devnet).|
| 131.2 | Deneb Upgrade:|The discussion around the Deneb upgrade focused on two topics:  **Voluntary Exits** , **Network Outage** | 
| 131.3|Peer Data Availability Sampling (PeerDAS) | Developers are parallelizing work on PeerDAS alongside Electra preparations. PeerDAS aims to scale data availability beyond existing solutions while maintaining workload efficiency for honest nodes.|

____

## 1. Deneb

**Alex Stokes** [1:07](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=67s): And we are live Okay, great.  Cool, then. Okay, let's get started. Yeah, everyone. So this is the call 131. And yeah, I imagine we'll have a pretty packed agenda today. So let's get to it. First, let's talk about Deneb. There are a few things that we should bring up. Let's see here. Yeah. First thing is clarify voluntary exits hoppecke. Sorry, gossip topic after Capella. Just someone wants to take this over? I think Danno is at a high level, what's going on?

**Dmitrii** [2:35](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=155s): I have all on this topic, I want just to be sure that all clients understand it, on the same way that we should use Deneb topic for this and maybe change a bit broughten in this line.


**Alex Stokes** [2:55](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=175s): Okay, yeah, I mean, I think that sort of confusion here is that we're using this old domain for verifying the signatures, but the gossip topic, I believe, should be for Deneb. Does that align with  everyone's understanding? We have a thumbs up, 2 thumbs up, 3 thumbs up. Okay. So I assume everyone's doing this. And we understand. And then yeah, from there if we can clarify the language of the PR, but that works. So we're good on this. I’ll assume awesome silences is Yes. Okay. 


### Network outage with Bloxroute relay

**Alex Stokes** [3:50](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=230s): Next up, we have the common hear from Terence. So I'm sure you're all aware, but there was a bit of a network outage. Likely due to some interactions between the clients and bloxroutes, the relay? Terence, do you want to give us an overview of what exactly happened?

**Terence** [4:13](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=253s): Sure, happy to so. Yeah, so people can read my comments. I don't want to repeat. So since then, bloXroute was put their Post Mortem, Michael’s aslo has their response. And the case of the issue is that there's definitely some I would say, edgecase with how Beacon API is interpreted and used. So currently, beacon API proposed block endpoint has this option to basically say the following. If I see the similar blog, there is already gossip on the network. I will not propagate the blocks by probably I mean, I will not even send a block out as the first hop, but this is to prevent unbundling attack. So, we basically all the clients do that basically implement that. But the open question is that what do we do with a blob sidecar? Because blob sidecar doesn't have this inherits slashing condition. So I'm currently I think before that lighthouse and prysm, I can say for them, they do not broadcast the blob sidecar. If they see there's a similar block on the gossip network but because of that bloXroute block was not able to be Gossip. So since then we have updated the behavior to basically fix that. So Michael is also working with the rest of the client team to make sure their beacon API is basically kind of working for the rest of the relay as well. So yeah that's pretty much the Update.

**Alex** [5:56](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=356s): Cool thanks. And yeah I mean I don't think anyone hears from bloxroute to kind of respond but yeah ultimately I mean ideally this wouldn't happen we have like a lot of testing in place to make sure things like this don't happen but this one kind of slipped the cracks. So yeah I guess from here we'll just work with them to try to prevent things like this in the future. Okay is there anything else  for that anyone wants to talk about? Any data any stats on blobs anything like that. 

## 2. Electra
### Discuss [currently included EIPs](https://eips.ethereum.org/EIPS/eip-7600) including status of spec and any open questions

**Alex** [6:56](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=416s): Okay that's good then. Next up I want to talk about Electra. So I imagine will take up the bulk of the call . So just to like frame things you know it'd be great to go ahead and move forward on figuring out what Electra looks like even just like an initial scope. Especially so that we can aim for Devnets as soon as possible. You know even ideally within like say the next month we have things ready to go. Barnabas asked about 2537. So I was only including things for the CL and there really aren't any CL dependencies for 2537. Does that answer the question Barnabas? Okay we got a thumbs up. Right so I started with the Fork that have been included just going off of this uh EIP 7600 for the Hard Fork Meta. And yeah I think it'd be helpful just to go through each one of these in turn. Go through the status of the spec if there's any open questions we can talk about now. That'd be great but ultimately. Let's try to figure out what we need to do to get these to a place where we can Implement Devnets again say in the next month. Really as quickly as possible. So the first one is 6110 this is essentially making deposits work a lot like withdrawals today where they are sort of synchronously produced. If you deposit within a block the deposits then passed off to the CL who then processes that on the Beacon chain. Are there anything here I mean I looked yesterday it seemed actually like it was in pretty good shape is there. Anything anyone wants to talk about any open questions on this one or do we feel pretty good about it? Yeah Mikhail?


**Mikhail** [8:49](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=529s): Yeah so this EIP has a consensus spec test with a good coverage. And there is the PR to this pack which bundles 6110 and 7002 which is in progress. So yeah that's also great about 6110, I was just going to raise a bit of awareness that considering the max effective balance is in Electra as well. And considering that the max effective balance introduces the pending deposits queue. There was just thought that we could leverage on having this Queue to finalize the deposit flow before actually creating new address is helpful for preserving the invariant of EPOCH key index matching. And if this can be resolved on the spec level on the protocol level we could probably get rid of additional complexity in CL client implementations where they will would need to manage this cash per each for independently. So because the same EPOCH key can get different indexes across different works. This just one of the things that probably could be introduced. I'm going to play with it in next couple of weeks. And provide the update if it for is doing or not. We will decide later on. 

**Alex** [10:36](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=636s): Okay yeah that'd be great. If you want to open an issue or even make a PR to explore that sounds Good. Okay anything else on that otherwise we'll move to 7002. Okay let's go to 7002 then. So this is the execution layer initiated exits. And we'll get to this with MaxEB but we also want to include I suppose we're calling them partial withdrawals. Does someone here want to give an update on 7002? Again I think the spec is in a pretty good place except for the partial withdrawals bit. So it looks like the EIP would need to be updated and then also the pre deploy assembly. Lightcleint or Mikhail I think you guys have been working on this?

**Mikhail** [11:43](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=703s): Yeah, Lightclient do you want to ? Or do you want me to share the last updates?

**Lightclient** [11:49](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=709s): Yeah I think you've been working on adding partial withdrawals. So maybe you can share how that's going. 


**Mikhail** [11:54](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=714s): Yeah sure. So there is a PR into the assembly into actually the repository where the assembly code for your contract is sitting. So I just send the PR to the chat yeah in this pair basically what we have is adding the amount field the change is relatively small because the amount field is appended to the POP key data. And the stored in the storage slot where the rest of the POP Key Bytes can accommodate the amount as well. Yeah so it's relatively small PR to the code and once we finish working on it. I think it just needs review and then merge and then merge after that review. Yeah we will you know we will update the EIP that's it basically. And yeah also the corresponding change would need to be done to the engine API as well. And but it's going to be relatively small as well. 


**Alex** [13:11](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=791s): Right and for the engine API it's just changing execution payload right. There's no like additional fields that we
Need.

**Mikhail** [13:19](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=799s): Yeah. We already have the back for Electra a bootstrap with 6110 and 7002,  I mean engine API specs. So we just need to add an amount field to the exit data structure and basically rename exit to withdraw request to generalize this thing. Yeah but that's just rename thing. 


**Alex** [13:49](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=829s): Cool. Okay sounds good. Okay if there's nothing else on that one we'll move to maxEB 7251. I think Mark is on the call somewhere? 

**Mark** [14:04](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=844s): Yep can you guys hear me cool. We've been chugging away at maxEB for a while now. In terms of the spec it's been merged into Dev.  Most of the pieces are in place, obviously still minor changes and things being updated. And that will continue for a while and then there are a few outstanding questions that we still need to answer before we can really stabilize it. So first of all when a validator opts into being a compounding validator. They are then exempt  from the withdrawal suite until they hit the maxEB of 2048. And a feature that we could include are custom ceilings where validators could configure a custom ceiling up to 2048 but potentially lower if they want to still hit the withdrawal sweep. And it's I mean obviously it's a little more to implement but it depends on what the appetite is for that from the community. We did speak with Lido yesterday. And they said it was nice to have and it's certainly nice to have for solo stakers. But it's not something that at least Lido to I guess it's not Mission critical for them. So that's something to discuss and then the second bigger one is regarding consolidations of validators. So in the third breakout call we were kind of leaning towards there's basically two options for this. One is a beacon chain operation similar to BLS to execution changes. And another is to have it the execution layer initiated similarly to the new deposits in the exits or the partial withdrawals. And so in the third call we were kind of leaning towards have it being a beacon chain operation because it was lower complexity and we kind of made the assumption that all validators that shared the same withdrawal  credentials are fungible with each other. But then in the last call yesterday we had someone from Wider Community and they said that this kind of breaks their accounting both on and off chain and that it would be ideal for them if the withdrawal address had some ability to either initiate or gatekeep consolidating a validator because there's a risk that they wouldn't be able to update their contracts and time for the fork. So this kind of puts execution layer initiated  consolidations more or less back on the table and we kind of need input from the Wider Community to see if this is something they have an appetite for. So like I said Lido seems to have an appetite or or is worried that they won't have time before the Fork. And I don't  believe it breaks anything with rocket pool but I do know that they like the feature just it gives more it's just more of a beneficial thing rather than something of a break their contract. But yeah basically those two issues that we need wider input on. 

**Alex** [17:37](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1057s): Gotcha, thanks. Yeah I agreed with Potuz here in the chat just like surfacing on your first point like partial withdrawals like with 7002 seem to get at the same thing. I guess the trade-off then is yeah maybe there's more transactions you have to send. But yeah I think whatever we can do to reduce complexity is at least should be very strongly weighed. Yeah and then the other point I guess we'd want to add execution layer consolidation initiated well execution layer initiated consolidations. So yeah I mean again I would just say let's be mindful of scope creep. If we can get away without it then that's strongly preferable. Do we feel like we have a way forward to answer these two things? 

**Mark** [18:33](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1113s): The alternative that Lido was asking for was like I guess execution layer gated consolidation so it like might still be initiated but I don't know that kind of seems like not it just seems like worse ux and not significantly less complexity but yeah.

**Alex** [18:58](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1138s): Right okay. I mean I think a path forward is we can agree to do like initial Pectra Devnets without these things and just work on them in parallel and then you know they're not going to radically change. Well I don't know if it ripples into 7002 then that's could become kind of big but either way. I would at least suggest that as an option just to move ahead and then you know work on these things in parallel. Yeah is this the thing where we need another breakout call? 

**Mark** [19:38](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1178s): Probably or okay I mean yeah I'm sure we could have another one next week and and talk about it more.



**Alex** [19:45](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1185s): Yeah and it sounds like we probably want one that you know if it's in two weeks and we have time to like get more community members to be present because it sounds like that might be the path forward is just seeing how much demand there really is and then using that to weigh our decision. 

**Mark** [20:06](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1206s): Yeah that sounds like a plan especially if it takes two weeks I have a little more time rather than I guess just the next call next week. 

**Alex** [20:17](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1217s): Right I mean you know if it can happen next week that's great but it's more just like giving people time to be aware and then plan and show up.


**Mark** [20:26](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1226s): Yeah I think it's  just about scoping out the complexity of execution Layer initiated consolidations might I just anticipated might take a little more than a week but yeah.

**Alex** [20:39](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1239s): Yeah okay well thanks. Okay maxEB. We can move on to the next EIP that's been included 7549. So this is moving the committee index out of the attestation data into the attestation object again. I took a look at this specs. Yesterday they seem like they're in a pretty good place. Are there any open questions anyone here who's been working on this are aware of. I think Mikhail might have some stuff.

**Mikhail** [21:09](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1269s): Yeah so this just for the context this EIP also introduces a notion of onchain Aggregates versus network Aggregates. So it allows to back signatures and aggregation bits more tightly when we  include attestation on chain. And currently this design that is in this back has one downside. So because those Aggregates will be bigger because there are aggregation bits from many committees in one onchain aggregate. So we have to reduce the number of marks attestations and currently it is set to 8 versus 128 as we have it right now. And the problem here is that let's just consider that the situation where proposer wants to include many many Aggregates from the same Committee in the same slot which is the case according to the chain data we have. Because those Aggregates probably have just more information and just more bits. If we include several of them for the same committee. And the problem here is that say we have 10 Aggregates for the same committee and one slot cannot accommodate it with this proposal while with the status can be accommodated. Why it can't accommodate because we have 8 attestations at marks and each of those attestation can accommodate just one aggregate from the same committee. So what yeah what I'm just going to play with is to see if we can replace the commit a bit Vector with the list of committee indexes and in this case they will be possible to include to pack aggregate from multiple Aggregates from the same committee into one chain Aggregate. And basically it means that one onchain aggregate will be able to contain overlap in Aggregates from the same committee. So that's just one addition that I want to try to experiment with. 


**Alex** [23:52](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1432s):  Okay and maybe just to recap so we lowered the number of onchain attestations per block because they're now more dende right. But now this makes it harder to get even more Aggregates in the same block which makes sense.


**Mikhail** [24:09](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1449s):  Yeah and in some cases want probably want more flexibility.


**Alex** [24:19](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1459s):  Gotcha yeah Terence?

**Terence** [24:21](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1461s): In this model are you assuming there's this like aggregator that just volunteer the decide to subscribe to all the subnets and then by aggregated altra races basically on it behave versus like the current model is more like a random selection right you. Basically say today there's like 2048 committee and each committee has like 500 validators and by chances there are 16  validators I'm sorry 16 aggregators per committee. So basically those are by random live stream. So I just which model does this. Okay Potuz just answer the proposal. I see thank you. 

**Alex** [25:07](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1507s): Right yeah so the way it's written right now is there's like that's sort of an additional step from what we do today where as far as I can tell the network level stuff stays in place. But then the proposer Now can do this additional thing where they can like pack things much more tightly on chain. Because now the attestation can like span rather than just like one committee they can now span all of them.


**Terence** [25:30](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1530s): Right but this doesn't reduce the beacon attestation aggregate subnets bandwidth and traffic right which is well. I thought it does but I am run there. 

**Alex** [25:41](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1541s): Yeah I mean it would make box smaller because again the attestations are just more tightly packed which is nice. It would be like a more much more invasive change as far as I can tell to like yeah touch network. I mean theoretically we could do it but yeah would be much bigger change. Yeah Potuz?


**Potuz** [26:02](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1562s):  Yeah just on that. It does help in a few things the economics of validators that are losing attestations because they can't Fit after reorg and clients are dropping attestations because it's not just profitable for them to pack them. But I think this is going to help on that? But yeah Terence it's also helps some security. We have some security assumptions in that in the worst possible attacks to fork choice. We should be able to repack attestations from other blocks into the canonical chain. So it even helps in the theoretical properties that fork Choice has. but I think Terence is getting into something that we should be prioritising which is what Julio from Arigon on try to come up with solutions which is change the adaptation format. So that we actually lower the bandwidth on the network. I think this should be a priority for next forks. 

**Alex** [27:05](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1625s): Yeah I tend to agree but then I think that would touch subnet structure right. And so that's just like a much bigger thing. Says it's scary in the chat. Cool so it sounds like Mikhail's going to look at getting more flexibility into like the onchain packing otherwise this one seems like it's in a pretty good place. Okay again silence is compliance. Great so those are the four EIPs on the CL that have been included in Electra. Yeah next on the agenda I did want to touch on updates with respect to each team's implementation status. Well again maybe taking a step back like I guess my plan now is to get all of these four at least into some like Electra spec and the CL specs and have that out ASAP obviously. Then we'll like work on spec tests and you know hopefully ideally even by the end of the month. we have all that ready to go. So in parallel it'd be great if client teams are implementing these things. Could I get a brief status
update from each of the client teams on their implementation progress. Are there some of these that you've looked at some of these that you haven't? Anything like that?

### Client team updates on current implementation status of each included EIP


**Sean** [28:41](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1721s): I can go for
Lighthouse. Yeah I would say we've got a lot of progress on MaxEB Mark's been working on that obviously. 6110 we've had an external contributor implement this. I think what's lacking still is any changes related to like The Pub Key cache and Mikhail mentioned that he might be working on a design that would alleviate us having to make changes around this so that would actually simplify that a lot.  EIP 7002 I don't think we have any implementation progress on and is that it or am I missing already attestation change. Yeah Eton from our team has also started working on that one. 

**Alex** [29:40](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1780s): Cool thanks any other clients want to chime in?

**Stefan Bratanov** [29:53](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1793s): Yeah for Teku we have implement imped 6110. But so we we also implemented the cache but we may have to revert that depending if the specs which Mikhail discussed are going to be part of it. 7002 is in progress we have a PR for it. And the attestation changes are also being looked at maxEB we haven't done any coding but we have someone looking at it. 

**Gajinder** [30:37](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1837s): For loadstar 6110 we have mostly implemented MaxEB as well. And we might just push in other PRs that are required. So yeah we are sort of feeling confident on it.

**James He** [30:58](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1858s): For prysm we're pscing 7251 MaxEB. But the other ones were still in the early phases of assigning to each of the team members. They're being discussed but not too deep into it. 

**Alex** [31:20](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1880s): Sounds good. And I think Nimbus we're still missing if anyone is here? Okay I can follow up offline with Nimbus on that. So yeah kind of what I expected some teams have different progress in different ones and yeah hopefully that can be top of mind for everyone over the next month. So yeah Terence?

**Terence** [32:02](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1862s): Are there like a general tracking sheet for like team progress you can think of like a table where the loss of the EPIs and the calls of Client teams and we can Mark like progress like basically
milestone 1, milestone 2 blah blah yeah it looks like. 


**Alex** [32:18](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=1938s): Yeah Barnabas is already on top of it. Great. Cool yeah I think that will help people understand where their clients are at. And then again I think it'd be great to aim for devnet in like the next month month and a half. And you know if client teams can do sort of parallelize interop sort of on their own when they're ready. That'd be great. Okay. So those are the EIPs that have been included. Let's take some time to talk about about other EIPs. We might want to think about for the initial pectra devnet one that was CFI but not included is inclusion list. I would at least like to get to a point today where we agree on IL's. Well yeah. Should we focus on them or not, does anyone have any thoughts here? I'm not sure exactly what the latest status is? I know there's some complication let's say around AA account abstraction with the design.

**Mike Neider** [33:31](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2011s): Yeah I can give a kind of brief update. Right so I guess the last All Core Dev Execution call has a similar update. But so yeah if you want kind of more details check there. I think Potuz's post is the most thorough description of the relationship between 3074 specifically and inclusion list. I just sent the link in the chat. So yeah I guess this issue came up and it's around kind of this idea that um we used to have this assumption that if the transaction was valid in the pre-state of the block it would be valid in the prostate of the block unless the only condition that would change that is if there was a transaction from that address in the block. 3074 changes this because you can spend the balance of a different account. So an account that shows up in the inclusion list could be corresponding to an invalid transaction if someone else spends the balance from that account. So that's the tldr and  why 3074 in particular causes issues. We have a breakout room tomorrow show the link it's PM issue 1000. Yeah we hopefully we'll over that kind of exhaustively there. Yeah I think the general sentiment at least in the IL channel of the eth R&D Discord has been that we have a few Solutions but most people are uncomfortable with both the speed at which the spec has changed. Given these Solutions and the kind of Aesthetics of the changes being I feel like they kind of look a little less aesthetic than the original design. I think it's still going to be something we have to face down the line. I don't think the 3074 compatibility will ever go away personally. But yeah we can probably get more into the details tomorrow I'll probably cut it here. And yeah definitely bunch of other people have a lot of context too if they want to chime in. 

**Alex** [35:58](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2158s): Cool thanks. Okay so what I would like to do today is just focus us on devnet-0 which you know given IL’s or maybe a little up in the air. They'd also you know like we won't make a decision today because we're also going to need EL Buy in and like 3074 is not even CFI. So if that's an issue for but then it's on the fork like you know maybe that unblock IL’s like it seems like  there's some uncertainty there. And so I would kind of suggest just putting it to the side for
Now. Again for like our initial for our initial devnet-0 scope. I think everyone will also be plenty busy with these other 4 EIPs. And yeah we can work on ILs in parallel was 3074 CFI. yeah I thought it wasn't. I think going to be discussed next ACDE it was CFI for CFI. Great. So yeah I mean there's definitely some open questions here with respect to AA. And yeah I don't think we're going to decide today what I would then suggest is yeah essentially what I said. So basically let's focus on these other four. Again I think that'll keep client teams busy and yeah ILs can just kind of go in parallel. And yeah we'll see how they shape up. Let's see yeah so Tim put the included EIPs in the chat. So it's the fork that we've talked about today and then also 2537 which I wasn't going to touch just because I believe that's only EL scope. And so yeah none of us really need to worry about it. So cool let's then you know it'd be good to hear what people think about timelines for again this initial devnet. So you know assuming we only target these 4 EIPs. Do people have thoughts on you know when we could start seeing early Devnets like is this something that's going to take one month two months it's too early to give estimates. Anyone have any thoughts? 


**Sean** [38:32](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2312s): I feel like we don't really have enough info for estimates yet if 6110 and MaxEB could both have design changes I could change the workload of decent amount. So yeah I think we just need to focus on like getting a Devnet spec because rushing to the devnet prior to having a spec is I think a bit counter productive. It ends up with us like writing a lot of code that we can't
end up merging. 


**Alex** [39:09](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2349s): Yeah totally. Okay. Well I think that's at least my Show's top priority over like the next week or two is like getting to some electra spec that's final and then hopefully that gives us more clarity moving forward. Okay I think that's all I had for Electra. Is there anything else that we should discuss? I think it sounds like there's plenty to do and people know what to do but if there's any else let's hear it. 

**Sean** [39:51](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2391s): Oh well we didn't mention PeerDAS. Right.

## Research, spec, etc 
 ###PeerDAS

**Alex** [39:55](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2395s): Yeah I was going to go that next jump into. So I put it more in like the research / Spec side of things. Yeah so PeerDAS hopefully is also State of mind for everyone. You know at a high level we should focus on what we can hopefully call a small fork and then I think in parallel well you know if your team's working on this you know say 80% is going to Electra maybe 20% is going to PeerDAS. And yeah that's something that we can move forward in parallel as well. Are there let's see, yeah anyone here want to give an update? I know there's been some proof of concept work on implementation also the spec is, well there's a huge PR around the PeerDAS spec. I think the plan is to merge that as is and then you know any open issues from that PR we'll just move to another issue and an iterate from there. Is there uh yeah anything on PeerDAS people want to discuss?

**Sean** [41:17](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2477s): I guess I can give like a general update with Lighthouse stuff. We've made a lot of progress. Right now we're spending a fair bit of time though refactoring existing Lighthouse code to sort of
like support integrating PeerDAS more simply. So I think we're still a decent amount away from a full Lighthouse implementation but we have a lot of progress on individual Pieces.


**Alex** [41:56](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2516s): Okay awesome. Are any other client teams actively looking at PeerDAS. Yeah Potuz? 

**Potuz** [42:05](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2525s): yeah so I can't really speak for prysm because I don't know if Nishan is here. Nishan and Manu from Prysm are looking at this and they have been looking at the specification started thinking I mean brainstorming for the actual coding but something that they pointed the Nishan pointed is that even though Tech technically it's not a hard fork it's in practice. It is because it seems to be very hard to have these networking changes not affecting brutally the network if you don't ship them out of hard fork. So I wonder if this has been agreed or not because if this is going to be in a hard Fork then this decision has to be made right now.


**Alex** [42:57](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2577s): Right so I mean I think the thinking was kind of that assuming it's not like yeah like you're saying really complex networking wise like clients you know you can imagine that. I download prysm and I set a flag in terms of my like availability Mode. And that should just sort of be transparent at least that's the intention with PeerDAS. The only like necessary hard Fork would be bumping up the the blog data gas on it. Right.


**Potuz** [43:26](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2606s): I technically that's correct but the problem seems to be along the lines of like proposers not proposers are updated and they don't send the full blogs or like be PeerDAS nodes don't download The Blob. So they don't have the blob to separate completely and then non PeerDAS that blobs wouldn't be able to get the blob and this can create like head split views. 


**Alex** [43:47](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2627s): Right so what I would say to that is just like I think we keep working on you know implementations on the side. I think it'll become clear you know. If we have PerDAS Devnets say six months from
now eight months from now then like it'll be clear if this is an issue or not and then we can go from there. Yeah it's I would rather focus on shipping Electra as quickly as possible and so like I don't want to have this huge uncertainty PeerDAS off slow things down personally. I don't know if anyone else disagrees?


**Sean** [44:24](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2664s): So we had sort of talked a little bit about potentially having overlap and serving both like PeerDAS samples and participating in Blob gossip and blob validation normally. So then we could get like even on Mainnet some degree of certainty with sampling that like when you sample the blows are there but there'd be a lot of redundant upload down that we'd have for a period. So unclear if it's worth it but I thought. 


**Alex** [45:04](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2704s): Yeah but it does like greatly due risk rolling out PeerDAS which I think is important. So I know I don't like that would be my preference is to like risk as much as possible have a more gradual roll out and then once we're very confident then go ahead and do like the hard Fork to bump up the block count. Okay well there's some chat. I guess that's worth surfacing. Ansgar saying you know PeerDAS is definitely very very urgent and then yeah Potuz’s put this point next in the chat that would change prioritizations. Yeah Ansgar, do you want to say something? 


**Ansgar** [45:45](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2745s): Yeah I mean I don't I think there's not like unanimous agreement in here yet necessarily that there is the demand on the layer two side yet to already absorb the the block throughput that we have today and that basically it's going to be very urgent to scale I personally predict that that will happen of course we will see by the time we viz have to make final decisions around elector. we will have more time to see how much the demand has picked up. But ideally at least I'm operating on the assumption that it will pick up. I would personally like to see at least this be prioritised in the sense that clients spend attention and resources on this and then if it's not ready in time for Electra. I don't think Electra should wait for it because it's not necessarily strictly like has to be combined with the fork but I would personally think it would be very unfortunate if basically everyone focuses on the electra features. And only once that's done basically starts really working a lot on PeerDAS that seems like the wrong order of priorities to me.

**Alex** [46:43](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2803s): Right and this is kind of my point a second ago where I think you know if client teams can split Focus 8020 let's say I think that is a good compromise.

**Mark** [46:53](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2813s): I also have brought up something to a few people but is it possible in Electra you could consider increasing the max Blob size to something like 10 or so. And then when we are closer to the electra Fork we'll have more of an idea of how much demand there is. And then potentially you know for like while loadstar is going on maybe there's a CL only fork and we can decide at that time whether or not maybe we just further increase max blobs per block to something like 14 or 16 or if PeerDAS has made sufficient progress then maybe we could handle the CL only fork that does PeerDAS but we could make that decision later like. Right now we could plan for a small increase in capacity for Electra and then later decide on what the next increase in capacity is.

**Alex** [47:49](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2869s): Right and Ansgar you had the EIP right to suggest bumping up the Blob counts even without PeerDAS.

**Ansgar** [47:56](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2876s): Yes it's still in draft but it has a number 7500. Basically the idea would be to have it gradually increased and Electra basically like a small bump at Electra itself. And then two months later like  another bump and then two months later another bump. Exact details like in this case I was targeting 816 basically it could of course be less ambitious initially. But something like that the one complicating Factor here is just that basically we have two alternative approaches for  scaling right so basically there's still head room for like a one time pushing the existing 4844 mechanism to its limits right. So basically just really optimising propagation seeing how well the network handles things today. And then pushing to this. Of course this will require some engineering effort. And so of course once we move to PeerDAS  or other forms of data availability sampling. This will basically no longer like this. This will become redundant work. So the question is if we are optimistic on the timeline for DAS. It would basically be a waste to put engineering efforts on pushing to the limits of 4844 but if we think that say DAS PeerDAS will still need a year or so to hit mainnet. It would maybe make sense to First have one in initial step of throughput increases just by pushing for it 4844. And then a second step moving to DAS. So I feel like we just have to agree on a strategy. 


**Alex** [49:14](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2954s): Right I mean that makes sense. And then the question is like how do you actually get there? It seems a bit early to like commit one way or the other. So you know I think we see how mainnet that goes right just getting data is going to inform how urgent it is to bump up the 4844 blob count you know if PeerDAS implementation proceeds a lot more quickly than we expect then that kind of pushes us that way. So yeah I mean I guess it's just something to keep on everyone's radar and then we'll address as we go. 


**Mark** [49:43](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2983s): I mean, I think is it true though that either way the pressure for Electra is small 4844 blob increase?


**Alex** [49:54](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=2994s): Well it sounds like I mean yeah so I think it'll just depend on PeerDAS implementation right. Like if PeerDAS is ready to go and we are confident in it then like great we'll do it if we're not then like I would say you know DAS or like you know data scalings sort of a soft question mark with Electra right now. And what that would likely resolve into is bumping up the 4844 counts. Yeah I mean luckily that should just be a constant change so that's something we can easily do you know down the line. So takeaway is focus on PeerDAS. Focus on everything. But actually to the extent that you have spec capacity definitely keep eyes on  PeerDAS and yeah otherwise sounds like everyone will be head down on these other EIPs. So that was pretty much everything. I had in the agenda are there any other things we want to discuss while we're here. 

**Hsiao- Wei Wang** [51:26](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=3086s): Like does any client teams wants to test with just basic two EIPs that has been pretty close to finalized. I mean the 6110 and 7002 or like people just want to wait.

**Alex** [51:55](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=3115s): Yeah Teku says in the chat. 

**Hsiao- Wei Wang** [51:59](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=3119s): Oh yeah, so like  know if people think like two weeks is too long to wait and I can generate the test vectors just early next week. But I think it won't be a formall release yet just the
test vectors. Is that okay? 

**Alex** [52:27](https://www.youtube.com/watch?v=ZqxDq1aJxHc&t=3147s): Yeah also from Lighthouse uh yeah test are good so yeah I mean I think that's a good path forward with the spec Hsiao Wei like we can work on that into show Electra PR that has 7110 and 7002. And yeah then again something I'll be working on next week is getting these other two in a place where we can merge them all. And then yeah again my aim is by end of the month to have or even sooner to have this Devnet-0, Electra spec with test ready to go. Okay anything else otherwise we can wrap up a little bit early today. Okay seems like a know. Thanks for joining everyone and yeah I'll see you around. 


## Attendees

* Anders Holmbjerg
* Tim Beiko
* Alex Stokes
* Vasilly Shapovalov
* Danceratopz
* Justin Traglia
* Mark 
* Echo
* Pooja Ranjan
* Ignacio
* Joshua Rudolff
* Mikhail Kalinin
* Dmitrii Shmatko
* Toni Wahrstaetter
* Ben Edgington
* Fredrik
* Guillaume
* Trent
* Carl Beekhuizen
* Mehdi Aouadi
* Terence
* Lightclient
* Hsiao- Wei Wang
* Mikeneuder
* Ansgar Dietrichs
* Matt Nelson
* Sean
* Barnabas 
* George Kadianakis
* Phil NGO
* Mario Vega
* Gajinder
* MatthewKeil
* Stefan Bratanov
* Nflaig
* Pawan Dhananjay
* Maurius Van Der Wijden
* Fabio di Fabio
* Enrico Del Fante
* Preston Van
* Anton Nashatyrev
* Daniel Lehmer
* Potuz
* Francesco
* Saulius Grigaitis
* Lukasz Rozmej
* James He
* Tomasz Starczak
* Paritosh


## Next meeting:  Thursday  April 18, 2024, 14:00 UTC
_______

