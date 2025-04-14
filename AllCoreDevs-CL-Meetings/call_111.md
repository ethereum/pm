# Consensus Layer Meeting 111 [2023-06-15]
### Meeting Date/Time: Thursday 2023/6/15 at 14:00 UTC
### Meeting Duration: 1.5 hours
### Moderator: Alex Stokes
### [GitHub Agenda] ( https://github.com/ethereum/pm/issues/809 )
## [Audio Video of the Meeting] ( https://www.youtube.com/watch?v=ybgQuRcz9sg )
### Next Meeting Date/Time: June 29, 2023

# Agenda
   # Error issue #809 
   ## Exchanging the engine API for Cancun
   ### Merging into Deneb release
   #### Max effective balance change.

Stokes: This is consensus layer call 111. I'll drop the agenda in the chat. It's error issue #809. Danny can't make it so I'll be moderating and yeah we can go ahead and get started. So first up oh yeah, I think first call deneb and then we'll touch on some more research forward-looking issues. So, to get started with Deneb, I think essentially we just want to understand what things are finally going into the stack the spec release soon. So, I guess we'll just go to the agenda there's this issue for EIP-6988. I think Mikhail’s been driving this let's see.

Mikhail: Yeah, okay so about 6988. So the problem to this EIP is about preventing a slashed whatever is elected. As a proposer which is basically, prevents us from having a lot of empty slots in case of mass slashing and the one of the problems that we have encountered during work on the CAE was that basically this EIP changed the brakes the invariant of the proposer shuffling for an Epoch. So, it can change throughout the Epoch and that's apparently a problem for your clients and for probably some other toolin and some other balances so I've made it PR which suggests the change proposed by that plan. It basically stores the proposer shuffling in state.  The footprint is not that big and it seems like pretty damn not that big in terms of flag conditioner complexity to keep it stored in this state. So there is the update proposer Shuffling which basically accepts the state and I'm going to use the sharpen for the next Epoch and then we read the Proposal this is from from this vector and that's the change and yeah it's called every Epoch processing this function is called Reaper processing what's not that nice about the introducing of this function is that if we are bootstrapping from from Genesis for instance. We have to call this function before our state becomes usable well and before we are going to process any further slots and propose any blocks. Otherwise it will just not you know have the proper shaft in it but I don't think it's a big issue. So the question main question here is whether considering this additional complexity whether we want to include this change into deneb. So you know if anyone took a look at this PR. It will be great if we can discuss it now so let's do it now or I would keep it for a couple of days more to take a look in those this PR and make a final decision on that EIP whether it goes in the number not.

Sokes: So, we do have a precedent of having some initialization function for the Genesis state. So yeah, I agree with you I don't think that's a big problem. Iit says in the description it only increases the extra state that we have to track by to introducing device. So not too wild there I know there's been some like back and forth on this you know trying to achieve the aim of this the slash unit variant so yeah it's good to see this here personally it feels a little bit late to me to add something that is kind of this big because it is kind of like a change to the mental model of the protocol and in the process I don't know if anyone else is taking a look.

Mikhail: Yeah I'll take that I'll take that.

Stokes: No, so maybe we have the pr open you know and for another few days and I don't know if anyone feel strongly they should voice support or not support and we'll go from there. I do. I would imagine it's a bit too late to decide this on the next CL call but if that's the next time we get to discuss it that might be the next time.

Mikhail: Yeah probably we can briefly mention it on the next yeah CL call if it makes sense. I don't know.

LionDapplion: So, I think here it will make sense to do a study like we did for removing the SELFDESTRUCT to understand the implications of breaking the dependent route which may not be that bad but I think that's the main question we have to answer here but definitely it feels tight for deneb.

Mikhail: Yeah so definitely if we want to explore breaking this depend to route thing yeah I would say that this is too late for deneb also.

Stokes:  Waystar can you explain a bit what you mean by breaking the dependent route?

LionDapplion: So, this doesn't show up in the spec but in the beacon api’s all the duties included dependent route and the idea is if the dependent route of that specific Epoch is not changing because there is a reorder deeper than a number of slots you are good and the duties should be the same. So I know a few clients at least I think loads then we can rely on that. We can get around that and just pull but it will be good because that's exposed who else may be using that dependent route because we don't know.

Stokes: Right so I thought really why we have the EIP for this is to basically maintain this invariant that the shuffling’s wouldn't change. So it seems then that you'd still have that guarantee for the dependent route right.

LionDapplion: Well my point is if no one is using a dependent route maybe we can just break it.

Stokes: Oh you just mean like get rid of it entirely yeah well but okay sure. But my point then is that it sounds like this change doesn't have any bearing on that or am I not following?

LionDapplion: So the EIP-6988 is a reaction to the simpler one that just adds an extra condition in the compute proposal if we don't mind breaking the embedding again that's that's a much simpler change.

Stokes: I see okay so you're saying we could not do this just make you know the few lines change in the other PR and then loses guarantee. Okay yep yeah, when I was talking about changing the mental model I think the like having shufflings because we're talking about that they would change possibly every slot right so that to me seems  even more chaotic than what we have today. So I think we should not go in that direction.

Mikhail: I know maybe this invariant also used by some other tool in I don't know and yeah you can have some implications but as for me not having proposer shuffling swords in the state is and more clear more clean select clear solution and like breaking the invariance if it possible it is possible.

LionDapplion: Another point is if you have to process old blocks you need to retreat the shuffling so yeah having having to press the block the block after that specific slot that's the cost but I don't know I will look into it

 Mikhail: You would have a state anyway so it's not gonna be a problem.

Stokes: Okay so I think we should stay focused on essentially what's going to go into like the you know final TM the net release and so it sounds like there's still a few design questions we have some more sort of research we want to do around this particular feature which suggests to me that we table it for now does that sound good.

Mikhail: Makes sense to me.

Stokes:Okay next up, on the agenda there is another issue, this one for exchanging the engine API for Cancun. I think also Mikhail, l opened this one and yeah anything Michael we should know. I think I went the other day and added stuff for #4788 which we'll get to later in the call and generally it looks good when I look at it.

Mikhail: Yeah it's just basically and  so this spec consists of The Blob extension spec that everyone is familiar with and also with the parent beacon block route which is for the other EIP and the other and and last one change that is in this PR in the proposed Cancun specification. For now it's not probably the last one deprecation of exchange transition configuration. I would just like to quickly to briefly  go through it so I think that this pack first of all. I think that this pack is just not enough  I'm in terms of tooling to deprecate this gracefully. So basically it's the spec says that  first execution layer clients must not surface any error messages to the user if this matter is not called if we remove this requirement I mean like if we remove this error message then we can break the dependency between CL and EL. So, we remove this on the outside and then consistently clients can remove this method entirely.  So what actually how I see the procedure the procedure of removal of this thing is that EL clients remove it right away as soon as possible.  And then we, I mean like remove the error message of the methods methods should still exist because otherwise because since the clients will surface error because of this method will be responded. So yield clients removed the error message  we wait for Cancun or yeah we we wait for every EL Client  to remove this message and then process the clients also releases this software without this method being called. And then after it Cancun everyone can just remove it at any point in time. So we will use Cancun as the point of coordination for software upgrades. Yeah this is the the way of how to do it gracefully. So, maybe we can just you know cut it, cut the court and you know remove it right away but then we will users will see some x issues by seeing by potentially seeing error messages one client stops supporting it yeah the other one will complain. Yeah so there are two potential ways to do this. I would prefer the first one which is the graceful one but maybe there are some other opinions on that.

Stokes: Yeah I mean this graceful approach sounds better and was that what you have in this PR or something else.

Mikhail: Now it's not it's not described in the PR because this spirit is into this pack and so I say that this back is not here. So probably we should just try this on the call and say and ask EL clients you know to start removing this error message if they're okay with that. How does it sound?

Stokes:Yeah it sounds good to me. I got a plus one in the chat so yeah  let's make a note to bring this up on the call next week but otherwise yeah sounds good I know this is something we're going to do for a while so makes sense to go ahead and do it.

Mikhail: Great.

Stokes: Okay that was pretty straightforward.  okay so there's a list of EIP’s here.  that we essentially well that are on the you know the slave for going into Deneb. And let's see  we'll just take them in turn so the first one is #7044. This refers to  essentially changing how we process voluntary exits so that they once made are sort of valid forever. And this was essentially ux Improvement because before they expired and that was not so nice for people especially in like custodial staking services yeah so it looks like it's been merged into the specs already. And I think it's on here just to call it out. I don't think we really need to rehash it but I guess it's worth calling out. The next one is #7045. So this one wants to change how we process attestations and I know that this was around the confirmation rule that some of the Fortress people I've been working on  does anyone here want to give an overview of this. The PR itself basically just says that you have I believe the current and also previous Epoch.  To include an attestation on chain whereas before it was just when  when epoch's worth of slots so there's a basis like slots for Epoch rolling window. And now it's basically extended back out to  sort of rounding down so to speak to both epochs. If that makes sense. So I don't know if there are any of the conformational people on the call?

Mikhail: I can try to give an overview on that. It's not only about the confirmation rule it's also about some other properties in the protocol that we want to maintain under some edge cases. So, essentially this PR removes the constraint and gives us the guarantee that attestations that has been produced in the previous epoch will be includable until the end of the current debug. Which is important for the confirmation Rule and for some other things as I already mentioned. This PR also fixes the incentives part because previously there was the same constraint on the number of slots equal to nber of slots in the Epoch for the Target. As far as I remember, to give the rewards for that. So now  well  proposal will be rewarded for attestation if it even comes from the beginning of the previous Epoch while the epoch has been proposed in the end of the guarantee epoch so yeah this part is also fixed and yeah I would be pretty much in favour of PCIP to be of this change to be deneb. As I think it is straightforward  there is also the other the P2P part as well so I'm attestations will be propagate it yeah so the propagation also changed the from from the slots equal to the number of slots in epoch to the previous Epoch in the guarantee epoch and all these issues produced in the in these two are free to be propagated.

Stokes: Okay thanks for the overview. Yeah, I mean I don't really see anything blocking inclusion so has anyone looked at this in terms of implementation that'd probably be the only reason we wouldn't have had with it if there was some issue. So, does anyone like to implementing this? I'll assume no if no one speaks up.

Arnetheduck: Okay  I have a quick question: does this affect the aggregation subscription in P2P at all like which subject you're supposed to be subscribed to for how long?

Mikhail: I don't think so.

Stokes: Yeah, I think this is mainly a state transition change.

Arnetheduck: No it's peer-to-peer change as well and it extends the time that somebody is allowed to send. The attestations on a particular Subnet in peer-to-peer.

Stokes: Right but I don't think it changes anything about the aggregation structure.

åMikhail: And that that's actually a good question and the question is that  in the current   like before this change  how does the aggregation Works in terms of subscription whether aggregators stay for the longer time to expect some attestations from the past or not because the stack is not it does not seem to say anything about this Edge case I mean like even with a 32 slots as it is today.

Arnetheduck: Yeah, I think that might be a gap actually. I think we're kind of unsubscribe early.

Mikhail: Yeah.

Arnetheduck: And then the wrong aggregators will be listening to these  attestations and they won't aggregate them anyways they'll be lost anyway so I think that's merits at least thinking about.

Mikhail: Yeah so I mean like it does not break  that much this change in terms of aggregation and  I think that there is a probabilistic this probabilistic function I mean like whether there is the right aggregator. So there is still a probability that somebody subscribed to the right subnet. I mean like the current subnet can aggregate those or or not. Maybe maybe I'm wrong.

Arnetheduck: Well that's the thing that   nowadays, we will only be subscribing to one aggregate substitute subnet per validator anymore and yeah to be honest I don't know I'm I'm raising the question because I have no idea but but it feels like the kind of thing that would in practice possibly break this or not break it it would just render it points to be propagating these attestations unless the the aggregation pipeline is  in tune with this change. 

Mikhail: Yeah so again it doesn't seem to break anything but yeah it's probably probably the problem that we're discussing now already exists in some for some all the destinations.

Stokes: Okay well so it sounds like we should do a little digging to look into this a bit further. And I suppose we'll discuss this on the next call. I don't think even if we needed to change the subscription logic that it would you know make this twice as complex or anything so I would lean towards  considering it included. But yeah  definitely something we should take a look at. Okay so we'll make a note about that  the next one up for discussion is #4788. So I opened a PR for this basically there was like a feature for this. And now it's been  in this PR migrated into Deneb formally. There is some feedback from some of you so thank you for that on the PR. And yeah this one's pretty straightforward change discussing this for a while. I think it's pretty much ready to go. There is some feedback here that I can get to but it won't be super substantial.  in terms of the spec or implementation.So yeah, I suppose any final thoughts otherwise we'll get this ready in version for the  to never release. I guess it is worth calling out that  there was also an engine API change for this  in the PR that we discussed earlier from Mikhail. 

Mikhail: One thing that I commented out in the PR and that from the first glance  I can look a bit odd is that we are duplicating the parent. We can block routes on the CL side. So the other way around would be not introducing this into the  execution payload on CL side because we have the parent route in the outer structure in the beacon box structure. And the advantages CL passes this data into El and El but El includes this parent beacon block route and to the execution payload into the actual execution block. But yeah there was a comment about it and So I think it's fine to keep it there   considering that the complexity the data complexity isn't really really cool here. So I'm just emphasising that because probably somebody else may take a look at that. And have some they have similar thoughts on that.

Sokes: Right yeah thanks for bringing that up so you know you could say very strictly that we're duplicating some data in the block with this extra parent routes and while that's true.  the reason it's there is because we essentially want to have this sort of symmetry, almost that like whatever we have in the execution payload in the block is what is passed to the EL and the EL needs us there  definitely. So I think it's easier to reason about if we just put it there   that Mikhail pointed out we could save 32 bytes but yeah. I don't know if anyone here has a strong opinion either way and perhaps if you do you can take it to the PR. Unless you want to talk about it now. Regard it seems okay in the chat. Thank you. Okay so those are the PR’s here on the agenda I think the intention is to essentially get them merged into a Deneb release in like the next week or two. And  you know that would sort of be our final Deneb spec from the CL side so very exciting to see. And yeah, everyone here please take a look at everything we've discussed if there's any final comments, especially beyond what we've discussed on the call so far let them be known. So, with that being said  the next item here is discussing the Blob counts. Perhaps this was mainly just a note to call this out that  you know. I think expect the EIP says that we essentially have a target of two blobs and a Max set before.  There's been some conversation between different  you know researchers and devs about bumping that up to say  Target three blobs Max of six blobs. And yeah I'm basically I think the cloud here is just to say that people on this call and others are looking at all the data that we can and thinking about you know potential rectifications. Please just keep doing that and  you know join the conversation to the extent that you're able to do so. And  there's a note here we're trying to make an informed minute decision in the next two weeks so yeah if you have thoughts or feelings about this you should bring them upstairs. I would imagine this will be a topic on the next  execution call but  yeah this is just a reminder that it's happening at least it's a topic to happen you know a discussion point that it may happen so don't  don't let it evolve your plate so to speak.

Dankrad Feist: Yeah and I also wanted to mention for those who went on the Monday court that  I did more tests at 768 kilobytes and I'm going to share the dashboards in my chat for anyone who's interested in looking at these as a summary. We didn't see any  yeah problematic behaviour any instabilities. We did have some problems with our own nodes sinking as far as I know. So the blocks we created some of them while we hit the average were more like 1.5 megabytes and zero megabytes. Alternating which is actually a stronger stress test but yeah what's our our endpoints the best was a problem there.

Stokes: Okay great and yeah thanks thank God for filling the charge on those experiments it seems like from what we've seen there isn't any immediate issue with the bigger Blob size. So that's a strong argument to make them bigger.  okay great there's some data in the chats. Arnetheduck is asking how into the process can we make this decision. Yeah I mean I would say the sooner the better like I don't think we want to be like two weeks out from the fork and being like Oh you know let's change this. Just because it'll grip one does I think a bunch of things.

Arnetheduck:  I'll mention one thing which is only weakly related but it kind of came out of looking at at graphs around this and and what's been happening over the past six months is that we've gone from practically no reorgs at all to you know a few per hour and we can kind of we haven't like there's no great answer to why this is happening there's a couple of theories. It looks a little bit like it's growing with the number of validators. It definitely became worse after  the complexity increasing Capella.

Dankrad Feist: Well what about the late block records? Wouldn't that be a strong reason why we're seeing this.

Arnetheduck: Because. 

Dankrad Feist: Before that if even if you get your block and as late as 11 seconds your probe is still going to be on the Chain whereas now like we walk those blocks so maybe it's not that surprising. That this has gone up as two clients have introduced that.

Arnetheduck: Yeah it's possible, let's say. But if you look at the graph it's kind of growing so that could be explained by you know more people starting to use newer versions of the clients.  But it kind of looks very similar to the validators that are growing.  Like I don't want to draw any conclusions here really I'm just highlighting it like when looking at experiments. This is like an interesting thing that has changed over the past few weeks  sorry months. And it definitely became worse with a capella like on the spot where we switch to Capella. It's markedly higher on average. And why am I mentioning it right now because  well we're packing more and more stuff into the first four seconds before we're supposed to send attestations. And like my gut feeling is that it might actually be an excellent time to rebalance the timing of sending the attestation and the aggregate. And I just wanted to sort of fill out the call whether anybody like strongly opposed to say. I'm just going to pull some numbers out of my nose there but like let's send the block at six seconds and all right sorry let's end the attestation at six seconds and send the aggregate appropriately in the middle between that and the next block instead of at four seconds. Has anybody explored this and found strong reasons not to do it? Or to do it ? I'd be kind of curious because that would help certainly help reorgs. 

Dankrad Feist: So I I'm strong in favor of of this and I also have the same feeling that this is an exactly one of our big problems we put one more the first third of the slot I think the interesting question would be if people have data on when attestations are arriving in the seconds  third and when aggregations are arriving yeah if anyone has that data that'd be very interesting well.

Arnetheduck: We have histograms  and tell us when all the stations come 

Dankrad Feist: Can you share that?

Arnetheduck: Yeah I can share it in the consensus Dev Channel later. The general trend is that  or well so there are two things in respect. There is a rule that allows us to send attestations  as soon as we've observed the block.  clients are generally not doing this; there's like a large concentration of attestations coming in shortly after the four second mark. And then like it spread out but it's fairly like there's a file is a large number of the attestations coming in the second after after the four second marks so like as a client Dev if we're pushing the timing back. I would still look into something like I would strongly suggest that people implement this feature where. We send the attestation a little bit earlier to spread out the traffic that would help. And I am going to post the exact numbers in the consensus tab Channel but I just got feeling based they're pretty good.

Stokes: I'm sorry what do you mean it's pretty good just the ones that you gave as actual numbers. 

Arnetheduck: No as in we're supposed to send the attestation at the four second mark and like by five seconds most of them most are the ones that you know we're going to be sent have been sent and result

Stokes: Okay right.

Arnetheduck: But again like this is  just me looking at the graph. I'd have to I'm going to pull it out in a slightly different format to give better numbers. 

Stokes: Sure yeah yeah I mean data would be helpful I mean I also agree I think this is something worth strong investigation. And I don't know I would my concern with deploying this in deneb is just delaying the fork. This is like a somewhat involved change that being said I do think it's like pretty important. So yeah I mean it sounds like we should probably spend some resources looking into this ASAP. I don't know if anyone has any thoughts on the Dev and its relation to this change but it sounds like we probably just want some more data first. 

Mikeneuder: I just wanted to bring up a.

Sean: Yeah go ahead Mike.

Mikeneuder: Sure yeah just from the relay perspective. Some of the issues around relay stability were around that four second deadline. And in particular getting all the relay checks done in time to hit that four second deadline like if a validator sends a signed header to the relay at T equals two then the relay really only has two seconds to get the blog post in time. So yeah, I think with bigger blocks that timeline is going to get even tighter for relays. So success seconds might help in terms of stability there too so just thought that was worth bringing up.

Arnetheduck:  for relays how much of that is like trying to, you know, post the block as late as possible to make more profit versus starting to work on time. 

Mikeneuder: Well the relay can't start the work until the validator sense of assigned header right. So I guess the validator could play like some timing games. There's a paper from Casper and the rig group about this. Let me get the link for it. It's called time is money. I think the takeaway is generally validators aren't playing these timing games yeah I'll post a link in the chat but the relay still has like some amount of latency that it has to do like for example simulating the block takes like on the order of like two to three hundred milliseconds and then like receiving all the bytes might take like another 200 milliseconds. So the latency starts to add up quickly especially if someone calls get payload later in the block. But yeah like the Relay can do stuff like oh will reject any get header requests past three seconds but if they have a if they have a valid header that they sign the relay is kind of like obliged to try and get the block published even if the signed header isn't received until like T equals 3.5 or something like that you know. 

Arnetheduck: Cool thanks Mikeneuder.

Mikeneuder: I think Terence's raising his hands. 

Terence: Yeah I just want to call out about prison also has the release that's coming either today or early on Monday that we do find like an issue where that if today there's the late block and then the substitute for the subsequent slot after the late block that presume will  delay  have some additional vacancy blob production and therefore it may cause issues with the relayer. And that's why if you're a present validator you may see more reorg or not real or you do a Blob proposed block will have a higher chance of getting New York but the fix is coming. So hopefully, that you improve things a little bit from the prism side.

Stokes: Okay that's exciting yeah so zooming out a bit like I think this is actually really important that we look into  changing these sub seconds or sorry these these so the slot second timings. So yeah let's keep this thread going and we'll see again I won't speak to when exactly it's included. But  I do think it's very important for us to to dig in here yeah Potuz, how does you have your hand up we can't hear you you're muted. if you're speaking, Can't unmute, I'm sorry um. Maybe try to get it working and just speak up when you can figure that out. Yeah I'm not sure there's some messages in the chat but I'm not sure what oh I can I don't know if I can maybe 10 do you know if you have the ability to mute people. 

Tim Beiko: Let me check I cannot. I'm getting that you are the only one I don't know what that means, I mean why couldn't he I mean people have been talking.

Stokes: Yeah but I think Danny's the host technically he's just not here .


Tim Beiko: Well Danny just shot a bad POTUS. I'll see if I'll give you trick is it

Stokes: Yeah wait wait okay he's back very incredibly, now.  Yeah I don't know I can chat with you. I'm not sure who the actual host is.  yeah okay sorry if you want to  send the message in the chat we can try to go about it that way but otherwise I will keep moving things along. 

Potus: Oh wait you I can probably be unmuted now.

Stokes: Yeah we can hear you.

Potus: Oh good so I just want to mention this thing on the on the on the sub segments that it's not so driven and it's not so clear that you can actually take out time from the first part of the slot. Because aggregation becomes a problem and becomes an actual problem  we have a very large valuator set that is getting larger and aggregating is taking over two seconds on a normal computer especially if you're subscribed to old subnets.  the highest I've been monitoring this because we changed in prison the way we are aggregating and aggregated at the stations and on a normal nuke like mine it would take up to four seconds to aggregate all unaggregated attestations if you are subscribed to all subnets. So that means that you cannot really realistically be a good aggregator.  If you are hosting more than 30- 32 keys on a nuke. So what happens is that very large validators can run on very faster software the hardware. But I think for small home stakers you are not going to get good aggregation if you reduce the middle part of the slot. So that leads us to like shifting everyone and taking only  seconds from the last part of the slot. And the last part of the slot I think is it is safer to take some time out of it. But the problem is now with the reorder feature that  we place a bet before the end of the slot on whether we are going to reorg or not and I'm afraid that we're going to see a lot of split views if we make this last part very smaller. So I think that it's going to take a long time to actually get these numbers correct and getting good experimentation that actually vouches for how long we can increase the first part. 

Dankrad Feist:  so what I don't understand is why is the relevant number all subnets. Why isn't it? 

Potus: Because if you so the amount of attestations that you need to aggregate is going to depend on how many subnets your subscribed for sure and if you run more than 30 validators you are going to be subscribed anyways to all sub names so by so if you're running on  on on a on a home computer you can't really realistically run more than the two or three.

Dankrad Feist: It wouldn't be, you wouldn't be in aggregated or something so.

Potus: Well but you are an aggregator quite often and you get all this. I mean you are going to get all of this  many more attestations and aggregated attestations that you are going to need to aggregate. So by subscribing to all subnets you're gonna be getting a lot or more of unaggregated attestations.

Dankrad Feist: Right but you cannot do all that work in parallel right like presumably if you're if you are running tens or hundreds of validators you know don't just have once you to run.

Potuz: Yeah the bottleneck is even we are parallelizing it and the Bottleneck is is in is in this in the BLST library and it doesn't matter like I see Terrence asking whether or not clients are aggregating  all at once or on us they come I Benchmark this and it doesn't matter it doesn't make much difference Lighthouse Aggregates as they come and pressing just that grades them all at prescribed times because the the number of additions that you make is exactly the same it doesn't really change anything so so I I truly don't think that we can't really subtract time from the middle part of the slot we can measure it and we can try to Benchmark it. But I would clearly see a degradation if we subtract parts from the middle part of the slot. And I think measuring the split views that will come from subtracting part from this larger the last part of the slot is the pain so I think that we should keep our minds open that if we are forced to increase the first the first four seconds then we may need to increase the slots.

Dankrad Feist: I I didn't understand why you can't parallelize it sorry that doesn't make sense.

Potuz: No we can parallelize it we are parallelizing and anyways we're getting a lot of we are getting four seconds marks so the the typical aggregation for my computer is about 200 milliseconds but then from time to time when there's a missed block for example on you need to aggregate more then you you get up to two seconds and I'm subscribed.

Dankrad Feist: Well I do need to aggregate more when there's a message.

Potus: Well because you get a lot of attestations that weren't included before that you if there's a missed slot you you have the aggregate the the attention from the previous slot then you need to aggregate with the applications from this Cloud to include more attestations and my computer takes up to two seconds.

Dankrad Feist: That's that I don't understand because the previous ones you could already have done in the previous slot.

Potus: No but you still need to aggregate with the current one so so you run there's always. Later the statements as well.

Dankrad Feist: Sure but these are you can just add right you've already aggregated the one.

Potus: Well the algorithm to add is not so simple it's simple to add when you only have one bit but then you need to start aggregating aggregates and it's not trivial.

Dankrad Feist: No you don't, I don't understand.

Potuz: Yes you do okay so I like algorithms.

Dankrad Feist: I had like 200 aggregated signatures now I received 10 more that were late. 

Potus: So yeah but then the problem is that you're receiving 10 more that had like 10. Two of them are with intersection with the 100 that you had before and you cannot and you've had like a group of like seven or ten years. 

Dankrad Feist: Okay why do you have to aggregate the Aggregates I didn't know where to?

Potuz:  Because you want to have a better block.

Dankrad Feist: Yeah okay.

Arnetheduck:  foreign compared to numbers at least that sounds a bit more like your numbers seem on the high end of things.

Potuz: Yeah so I'm giving you the worst cases so my computer takes very little on the on the on the app. So the biggest chunk is in aggregating the one beat once.  because we take them all at eight seconds and we aggregate them all at 10. And  I'm sorry we take them all at four seconds. I have eight and that one takes on my three validators is taking about like 25 milliseconds normally but it gets to two seconds on by location. 

Arnetheduck: So I'm looking at some numbers here actually   and specifically. I'm looking at   the delay from the start of the slot when the stations and Aggregates arrive and this was basically the number that was asked for before and just eyeballing it like it's in the 97 Range that both attestations and aggregates are in two seconds after when they're.

Potuz: Well but this is a different issue. So I'm talking about different things. So in order for us to submit the aggregate at eight seconds. What we're doing is start aggregating before so that their aggregate is already ready at eight seconds. So at eight seconds is our deadline to submit the aggregate so if so what we're doing now is before eight seconds and this is suggestible by the user we aggregate them all. And you need that before to have enough time so that by eight seconds you can actually send an aggregate because at eight seconds we're gonna send whatever the node has. Because that's the deadline so all right I mean it's always going to be early.

Dankrad Feist: I still I still feel like you're misrepresenting the issue because if like valid nodes with two validators can manage in that time then I feel like that's fine that's great because those are just going to get their aggregations in and we don't need the others we don't need everyone to aggregate we just need someone to aggregate right and so you know people who run more validators. Actually I need larger machines to run them then that's not the end of the world in my opinion. 

Potuz: Well I do think that this is centralising Force if we're like going to have like people that are able to be homestakers can only stake like one or two validators for four seconds.

Damkrad Fest: You were talking about not not like you were talking about someone who subscribes to all validators all right yeah.

Potuz: That's correct but this is the way that we need to when we submit our clients with default values we are typically looking at the work situation which is a validator that runs at least 30 keys and there's many of this and those are going to be subscribed to all subnets and this is what needs to be our default. so our timing is going to be this regardless of whether you're homesick or not. 

Dankrad Feist: I think it's okay to require someone who is running 30 validators which is like  what's like a few million in capital. I think they can afford a machine with a few more CPUs to make this fast enough.

Casper: Something to note here though is that aggregation is not incentivized and so we rely on aggregation but we don't actually incentivize it only. Implicit incentive is that you aggregate your own View.

Arnetheduck: I mean there's another point which is that when you're running 30 validators you're not aggregating 30  subnets you're aggregating much viewers there's 16 aggregators for every subnet. So your child.

Dankrad Feist: Yeah we're really talking about the node that's running a thousand planets or something that would actually need to aggregate.

Arnetheduck: Yeah my point is that like with 16 like the number is fixed the number of aggregators are  subnet. 

Potuz: That the blocks are full if you have like many more Aggregates that are worse Aggregates like what a validator with only two subnets would have. Then You're gonna fill the blocks with less attestations.

Dankrad Feist: Why would a node with two supplements have worse aggregates?

Potuz: Because they see less attestations. note the subscribers they get less peers

Dankrad Feist: Yeah, but aggregations are for subnets.

Potuz: Yeah but smaller nodes see many less peers and many less unaggregated attestations than larger nodes that are getting much more peers.

Dankrad Feist: Is that true?

Potuz: My node is a much worse aggregate aggregator than any that the node in the in our in our prison like  kubernetes.

Dankrad Feist: I don't understand why would if I'm subscribed to subnet 1 why would make subscribing to subnet 2 as well make me see more attestation from subnet 1.

Potuz: No it's it's it's   it's also it's also dependent on the number of fears that you have if you're a homestaker like myself on a bandwidth of a home that I am restricting that my number of peers to be I don't remember it was 30 or 50 now by default then I see many many less attestations that someone running with 200 peers on a cluster those.

Arnetheduck: That's not how the protocol works. 

Dankrad Feist: So yeah.

Arnetheduck: The number of peers is completely irrelevant. The only thing that's relevant is the concepts of mesh and that one is kept that let's say 8-12 depending on if you look at average or Max so you can be subscribed to eight periods and see the exact same traffic that if you're subscribed to 200 peers doesn't really matter and your your aggregate  when you're creating a block is Created from listening to the aggregate Channel not from listening to the attestation Channel typically. So the aggregators are doing that work for your basic calendar 16 of them right so.

Potuz: No no but I'm talking about the aggregating the one feature stations which is when you are an aggregator not when you're aggregating aggregates the largest chunk for us is aggregating one bit attestations. 

Arnetheduck:  yeah and the risk of you being one of those guys it's pretty small that's that's the 16 aggregators that exist per subnet and you're never subscribed to all the subnets and again this is not a function of how many peers you're connected to that is completely irrelevant. So I think this deserves some more investigation and I think we should take it offline. And we can go through  the flow but like   it certainly merits investigation like in-depth investigation of all these issues if we're going to change these timings.

Potuz: And I'll post it. Maybe you're in the channels these benchmarks that we have because we changed these algorithms because of these numbers that we were seeing both in my clusters and clusters and common computers. And we were seeing like very large times for aggregations.

Arnetheduck: Well yeah yeah I'm just saying, like your peer count is not relevant that's not how the protocol works. But changing the timings   the other thing I wanted to say actually was that we don't have to put all the time from the   you know the point where we do the attestation or the point that we do the aggregate we can we can play around with that a little bit like it doesn't have to be evenly divided or now it's evenly divided and we want to divide it in a different way but like it doesn't have to be you know  six.

Dankrad Feist: I mean it's all right it would even be proper whatever plasma to make this flexible right to not have a 100 fear division between other stations and aggregation.

Arnetheduck: Yeah flexible, I don't know because that feels like something that somebody could exploit but like it could be two n six or it could be three and three and whatever. 

Stokes: Right right

Dankrad Feist: So I mean even the ones even the one second is increased on the first third I think would be huge because ice   and my observations there are already under normal networking conditions slots like 3.5 seconds in  like it's not rare to see that. So like if you add one more second that's actually that's gonna have a huge benefit to the network already.

Stokes: Yeah I think we can all agree it would make sense to have more breeding room  on the front end and so the question now is just one of those numbers what should they actually be there's a lot of data people have been referencing. We should  I think moving this to the consists or some async channel is a great idea obviously there's like this is important and we should keep looking into it. But yeah we need a lot more investigation before we can just say oh let's make this six seconds let's make this two seconds or however it ends up   yeah. So let's  keep the conversation going. But we'll take it offline from here so next up  we do have an agenda item to discuss this proposal  Mike do you  want to talk about  the max effective balance change.

Mikeneuder: Yeah sure and actually this kind of flows really nicely from the previous discussion because the goal of the proposal I'll link it in the chat is to reduce the validator set which hopefully would help with aggregations kind of. Not only reducing the validator set as currently but also slowing down the rate of growth for the new incoming validators. So I'll just give a kind of a high level overview of The Proposal. We have a few docs that I'll link that kind of outline the pros and cons and then maybe we can just open up to discussion and as far as some of the design decisions go. So yeah the kind of tldr of The Proposal is increasing the max effective balance so this doesn't change the 32 ETH minimum  balance to become a validator but it allows validators to go above that we've kind of proposed   2048 -EIP. As a potential upper bound we don't want to make it Infinity   as far as how big a validator can get but yeah  going up to 2048 we think could be like a reasonable choice. Some of the benefits we outlined from the roadmap perspective we talk about how kind of slowing the growth of the validator set will be important for single slot finality dapline brought up the point that   intentionally being blocked on the current validator set size though that is like a little more of an under debate thing. We also talk about the benefits for the current consensus and P2P layers so that's kind of what we were just discussing as far as aggregation is taking a really long time. There's a post from Aditya on unnecessary stress on the P2P Network. I'll link that here so he wrote that before I published the or before we published the mods proposal. But yeah just kind of talking about some of the numbers of on the P2P layer of of how many messages are being passed around and and all these you know the kind of unnecessary bloat from all of  the the validators and then we also talk about some of the benefits for the validators from the solo Staker perspective it gives this kind of like Auto compounding benefit which people seem really interested in. The kind of key takeaway here is that with the current 32 8th Max The Sweep just takes all your rewards and withdraws them so any solo Staker just like would have to redeploy that Capital somewhere else to earn any any yield on it versus if we increase the max effective balance. They immediately start like compounding that eth so they're earning rewards on more than just the 32ETH that they kind of initially deployed. We also talk about the potential benefit for larger node operators who wouldn't have to run as many validators. This is kind of like you know a big part of the consolidation would depend on the larger validators actually doing the consolidation. There's some a risk associated with it because the slashing conditions would result in potentially higher slashing if they accidentally double a test or they double propose. So there's some risk associated with it. But in general you know for large validators like coinbase operates something like 70000 validators that 328th cap kind of artificially inflates that number for them and they've you know various staking operators have expressed interest in reducing the number of validators that they run . Or consolidating the validators into higher stake but   fewer of them. So yeah I guess that's kind of the high level overview a few of the big questions I think are the design trade-off of the UX versus the complexity of the spec change so in The Proposal we list   we link to kind of a minimal view spec PR. Let me get the link for that   and it's super tiny. It's 58 lines added 21 lines removed so you know this shows kind of the goal here was to show how small the spec change could be. But this has some. I guess some UX inefficiencies in terms of if someone wants to get the auto compounding   you know effect they have to actually withdraw and deploy with the new withdrawal credential with this direct 02 prefix instead of the 001 prefix. There's also this idea that like yeah I guess staking pools wouldn't be able to migrate or to consolidate without pulling their their validators out and redeploying them with like a 2048 validator so they'd have to like to deploy 12048 validator they'd have to exit 6432 each validators and then deploy a single 2048 one. So you know I think it's worth discussing  a bigger potential change to the spec that makes the UX better and more more desirable for people. And then I guess the other big question that's come up and and dogcraft has mentioned this a number of times is how do we actually get the consolidation to happen like if we make the change it's only worthwhile if it actually results in a meaningful difference in the validator set size. And you know if the ux is so bad and there's kind of no incentive for them to do it. The big stakers might not do it you know there might be some social capital that they gain by doing something that, like quote unquote looks, is healthy for your network and improves the overall P2P layer. But yeah it's not totally clear that they would take advantage of the consolidation and and make it worthwhile. So I guess those are the big questions in my mind   happy to open up the discussion here and you know also take questions in the Discord Channel later. If that's useful but that's kind of the high level.

Stokes: Thanks I have a question  just on your last point there is the auto compounding not enough of an incentive to sort of migrate to this regime.

Mikeneuder: Well so for for big stickers they can kind of take advantage of compounding by just they have the automatic withdrawal sweep right and then they can just deploy so for coinbase they're running like 60000 nodes that gives them enough to deploy like nine new validators every day just through the withdrawal sweep. So they don't have to really the auto compounding doesn't benefit them as much as it benefits the little guys. There could be a case to be made like the because the withdrawal sweep takes a long time. Like it's, you know 40 days or whatever that capital is effectively dead while it's waiting to get out and so the auto compounding might help them. But yeah I think other than that it's not obvious that it's strictly financially better for them to consolidate right oh yeah sorry sorry the activation sure yeah that that's the thanks opponents that's the 40-day thing that I was meaning to reference.

EthDreamer: Yeah especially since the for Sole stakers or small stakers like one of the bigger benefits was was auto compounding   yeah I'm with I'm with you on like improvements to user experience make make it easier for sole stakers so at least it's currently proposed and brought up but   that max effective balance being 2048 is so high you  a small stake we would almost never experiment to control it would have to like manually withdraw the whole thing at this point to have it withdrawal. So I definitely do think that UX needs to be improved in order for like small stakes to take advantage of this. And then Another Point   I noticed in like deposit processing or apply deposit. Like basically people can top up their if they opt into being a compounding Value. Let's say they can top up their value with the deposits and there is like a limit that you can only talk about by 32 piece. But that's it seems to be a limit per deposit and so it seems like they could. I mean they don't have to really wait the activation, they just wait the 16 - 24 hour deposit queue.

Mikeneuder: Yeah so this is actually something we tried to cover in the spec   because you're right if they are able to kind of get around the activation queues and then all of the kind of churn invariants are broken. The way we got around that is just to say like if you top up past 32ETH that's just like you can't top up past 32 ETH basically. So yeah, that that's kind of like a Brute Force way of doing it. But yeah this did come up then and it should be covered.

EthDreamer: Is’nt it will have a limit per deposit? Like you could submit a deposit within two weeks, wait for that to process and then submit another deposit for 32 years.

Mikeneuder: So basically how it works is if we see that the deposit changes the effective balance to be greater than 32 ETH then we the like effective balance of that validator then we just say okay the effective balance is only 32 ETH. So even if the deposit is processed like that.

Potuz: So how do you eliminate this thing? You're going to have a validator you need to keep track of how far how much part of this balance in this validator was added in this way or was started correctly this is like are you sure about this?

Mikeneuder: No it's just a mechanism to stop them from topping up past 32 ETH. You know we don't care.

Potuz:  How do we get track of this? So what how how is this mechanism? So u dont allow?

Lion Dapplion: So the logic is if these public is known and effective balance is already a 52 we ignore,  the value of the posited so it's effectively burned.

Mikeneuder: Right, oh so.

Potuz: Oh so you're you're declaring that deposit to be to being not to be an invalid deposit 

Mikeneuder: Yeah.

Potuz: That's that's something the contract is already deployed that sounds like something that is going to lead to a lot of people being burnt

EthDreamer: that's kind of true yeah 

Mikeneuder: Yeah we talked about this you know I think why would someone top up past 32 ETH like people can burn Ethan a lot of ways why would they top up past 32ETH. If we tell them explicitly that ETH is going to be burnt like I agree that it would be something we'd have to call out. But I also don't think that that would be a normal pattern.

EthDreamer: At the very least you'd have to like in the tooling that are like in the front ends that deal with popping up a balance you know. Tell them that it's going to burn it.

Mikeneuder: For sure yeah.

EthDreamer: Because a lot of people aren't going to know ,this a lot of people didn't know that there was a reorg for the POS activation change like if people don't know these things about the protocol.

Mikeneuder:  Yeah I mean we could also maybe think about ways that the spec like we tried to make this special super minimal and maybe there's a way that we can make deposits part of the like churn limit. And say okay this is what we have the invariant of like one over two to the it's like 1 over 65000 per Epoch can't change or whatever so just so.

Dankrad Feist: I mean this sounds extremely drastic like I mean I think there's this no go and it's too many this has actually happened a lot of time that people accidentally above 30 degrees. So like I mean that I think there's no way we're gonna do this. It was so drastic for a small mistake. But I also don't understand why. why do you want to stop people from topping up?

EthDreamer: Just getting the activation queue.

Potuz: Yeah the problem is if you get a lot of deposits like this then you get a big change in the validator set quickly but I think we can just churn this and that's it.

EthDreamer: That or like, especially something that would help.

Dankrad Feist: Right then yeah then deposits just need to replace the activation you just need to be replaced by the positive.

Potuz: Right and I think we can do this at the same time that we get rid of all of this if one voting because anyways we're thinking on churning those. So we can just mix these two things at the same time. 

EthDreamer: And then terms of user experience I mean I know this is historically at the president  and my dad a lot of complexity but another a complete other route is is it possible to add a beacon transaction to combine validators. 

Stokes: So, I think the proposal right now is trying to keep things as simple as possible and adding new types of operations would definitely be more complexity EthDreamer: Right.

Mikeneuder: Yeah I think that's kind of the trade-off we keep circling around here is like spec change complexity versus UX but you know I think it's worth kind of exploring many different Avenues and seeing what makes the most sense. 

Potuz:  And I think if everyone more or less agreed about like getting rid of one voting and there's already a spec towards that. So as long as we move towards putting the churn on the deposit queue instead of the activation queue I think we can just mix these two PR’s into one.

EthDreamer: That's a good idea

Mikeneuder: Yeah that's helpful. I haven't been kind of keeping up with the each one voting thing so I'll have to do a little research there but that sounds promising to me. 

Lion Dapplion: I mean the latest spec doesn't have a queue but it can be brought back.

Potuz: That was just a matter of terminology right. Because you still have the churn so the issue of the queue being on the states are not in the states I think is minor here.

EthDreamer: And  the other is it also like pretty heavily planned or leaned into that we're going to enable execution layer which initiated withdrawals. 

Mikeneuder: Yes yesterday, I think it seems like yes that will happen.  I'm still not totally clear on the relationship between that and this  though. 

EthDreamer: Oh it's just that if we also combine that with this it would drastically improved UX.

Mikeneuder: Yeah how do the execution layer withdrawals impact the churn but maybe that's a question for offline but it's not that sure.

EthDreamer: It's just it's just the fact that if you're a small sticker you basically you basically never withdraw and if you have one validator you have to generate 2048 EIP off of that one even if it's compounded it will take. So you need another way of initiating withdrawal.

Mikeneuder: You're right but I was just asking if you do an execution layer triggered withdrawal like do they have to go through the withdrawal queue too that seems okay it would have to yeah.

Lion Dapplion: I think the point is that yeah 

Stokes: The proposal is for exits and it would just move into the execute like it does today.

Lion Dapplion: Okay the the point here is,  if we can do parcel withdrawals triggered from execution then we could get rid of parser withdrawals automatic personality throws and.

Stokes: You're saying you would do that to add this back into the proposal now that Max is talking about.

EthDreamer:  Well I would. I was actually talking about partial withdrawals. 

Lion Dapplion: Yeah so the point is like today if you are a solo sticker you have one moderator you need to at least capture some value to pay for expenses and what not. If we disable parts of withdrawal signs that you have automatic compounding with the feature that Mike is presenting there has to be some way for you to extract  a value fractional value of your validator without having to exit the full thing.

EthDreamer: Right

Mikeneuder: So execution layer initiated partial withdrawals not full exits.

EthDreamer: Basically right although we would presumably need both.

Mikeneuder: Right.

Dankrad Feist: I mean that would be cool then we could get rid of needing an extra address right. We could just switch all validators to this functionality and everyone just withdraws whenever they want. right so that seems a lot cleaner than the current proposal.

Potuz:  One yeah, one problem I see with this is that you need to bound the amount that you can actually withdraw on a partial withdrawal otherwise you're gonna get a large change in effective balance in one slot which might be a problem.

Mikeneuder: But wouldn't the partial withdrawal have to go so the Proposal is written to to rate limit the activation and the withdrawal queue based on state rather than number of validators so if the execution layer partial withdrawal goes through the normal withdrawal queue then that rate limiting should be fine, right. Like we just have to make sure that the rate limiting is correct. That's the well yeah no yeah never mind.

EthDreamer: Yeah but it ends up like as currently written the the queue is there is no limit for partial withdrawals only full withdrawals because that actually affects the value or set but when you actually have right.

Potuz: So the proposal is only to trigger exits not to trigger withdrawals.

EthDreamer: Right but if we do enable partial withdrawals this way like you don't it now you can withdraw even more than 32 ETH and still not technically exit your validator so you would draw on a validator's word without going to the execute so yeah.

Mikeneuder: Yeah sounds like some more details to work out but this is potentially promising. I guess the one thing about this is it would change the default Behaviour. So like, Yeah, part part of our design goal for the first spec was like if people don't want to change anything then we wanted to leave that there so that's why we left the 001 credential alone but if we change everyone like to compounding with these execution layer triggered partial withdrawals then a lot of like workflows would have to be updated. I don't know if that's like a big enough reason to not do it but it's a consideration.

Stokes: Okay well thanks for bringing this up Mike and hopefully that was helpful feedback thanks everyone for the conversation. Is there anywhere Mike you'd want to drive further feedback like I guess just to the research post. 

Mikeneuder: Yeah each research post or I think Danny suggested, that Discord the POS consensus Channel could be  a good place. So yeah, I think I should be pretty easy to get in touch with but would be happy to hear more feedback so thanks everyone.

Stokes: Okay great  are there any closing or final comments for this call otherwise  we'll go ahead and wrap up.  

Paritosh: I wanted to bring up an update on the test net call we had just before this.

Stokes: Yeah please.

Paritosh: Yeah so we had the Hosekey first hoskey test net call  about an hour ago and we're gonna have the next one again on June 29th with a couple of asks I can link the summary over here. But one of the big questions that was still open is the current ideas to start with about a million and a half validators so that we have significantly more than mainnet and we don't have to rush to immediately make deposits keep ahead. We're just not sure if all clients think that they'd be ready for such a big value data set, a Genesis or such a big Genesis State. So just looking to hear some thoughts on that.

Lion Dapplion: Will we ever reach that in a minute what percentage of total each Supply stake will represent.

Paritosh: I mean we're at six hundred thousand now with the queue of about a hundred thousand so we're already at 700,000 in a couple of months so we double what we have right now we're also open to starting with a smaller number like a million but that won't give us as big a difference.

Stokes: So has anyone on this call like tried I just stayed that big I would say if we can get away with the million and a half may as well.

Lion Dapplion: But I mean I don't have is 40 million each staked. So 30% of Supply minute that will be pretty crazy

Stokes: I don't know I think if you talk to some of these liquid-staking people like  they want all these sticks so so 

Lion Dapplion: all I don't think the numbers are completely taken to be contained and no one can do anything.

Paritosh: I think when we started prata, if someone had said 15 of all it was going to be State we would also thought it was crazy but we're already here.

Lion Dapplion: Yeah I'm not opposed like seeing the difficulties I would rather start with a big one so we can optimize the clients and get done with it.  

Sean: Okay yeah I also support the nine and a half size.

Potuz:  I have a suggestion as well. I'm not sure how hard is it to do. But one of the things that we're seeing on mainnet is that we now have some validators that are exit. And even if we start with a large number of deposits we may increase even the evaluator slides by just adding validators that are already exited on Genesis. So that we start with a we don't need to have like a large number of validators sending attestations but the slice itself is still large. 

Lion Dapplion: That's a great point.

Paritosh: Yeah we can also take that into account Thanks. Yeah besides that we're looking for Client teams involvement to run at least majority of the validators. There's a Hoshkey planning dock that's been shared on the chat already that States what the requirements would be. Like what you can expect to get away in terms of machines it is a bit of an investment in terms of money so if so we're looking for commitments like solid commitments from client teams by the 29th. And if not possible then we're gonna look at node operators to help us get to the one and a half million or one million or whatever number we decide on. So, please talk to your infrastructure teams and so on and try and get back to us before the next curve.

Stokes: I'm sorry you said that was the 29th of June.

Paritosh: Yeah I think that's it on the Hoshkeyi topic thanks.

Stokes: Yeah thanks for bringing it up. It's very exciting to see progress there. Okay anything else otherwise we'll wrap up a few minutes early. Okay I'll call it thanks everyone.

Thanks Alex bye. 

Stoke: Thanks everyone.


#Attendees

Alex Stokes
Marius
Terence
Ansgar Diatrichs
Arnetheduck
Ben Edginton
Pooja Ranjan
Roberto B
Barnabas Busa
Lion Dapplion
Ahmad Bitar
Justin Florentine
Phil Ngo
Sean
Dankrad Fiest
Paritosh
Mario Vega
Tim Bieko
Mikeneuder
Hslao Wel Wang
Lightclient
Caspar Schwarz -Schilling
Zahary
Matt Nelson
Nico Flaig
EthDreamer
Fabio Di Fabio
Matthew Keil
Maintainer.Eth
Enrico Del Fante
Anna Thiesar
Potuz
Guillaume
Saulius Grigaitis
