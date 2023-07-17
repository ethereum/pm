# Consensus Layer Call 113

### Meeting Date/Time: Thursday 2023/7/13 at 14:00 UTC
### Meeting Duration: 35:43
### [GitHub Agenda](https://github.com/ethereum/pm/issues/823) 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=fBVIGBrKaFA) 
### Moderator: Alex Stokes
### Notes: Metago



# AGENDA

**Alex**
I'll put the agenda here in the chat. I'll be moderating today. It looks like the agenda itself is pretty short so yeah I guess we'll just go ahead and dive in. 

## Deneb [0:20]( https://www.youtube.com/live/fBVIGBrKaFA?feature=share&t=20) 

### Testnet, testing, or development updates/discussion

The first thing would be updates on testnets, testing, development of different things for Deneb. So I know we have been working on devnet7 and there might have been some chatter about devnet 8. Does anyone hear feel compelled to give an update or would like to? 

**Paritosh**
Yeah I can go with the update so we've had devnet up for a while now it's mostly stable. We have almost every client combination represented there, I think Erigon here to be added but that's the biggest one that's missing. There's a issue tracker. I will share the link in a little bit, where we're tracking the different state that each client is in. We also have a bunch of open issues there, once we're figuring out the root cause and the patch we also just update the issue tracker. In the meantime anyone who's working on tooling for 4844, please feel free to test it out against this devnet blob scans been updated as well to include data from 4844. I think we have something like 9000 ish blobs at this point and this is still as of yesterday but there's like a blob spammer and there's like a whole days lots of blobs that should be indexed at some point I guess and we seem to be doing okay there. 

**Alex**
Cool that's exciting to hear. Do we want to just briefly touch on devnet 8? I think that was the one that was cited to have like the full Cancun / Deneb EIP set, but maybe we're not quite there… go ahead.

**Marius**
Quickly before we go to devnet 8 one thing I noticed on Death Note 7 was when I let my lighthouse Geth node full sync and I got really slow just when it arrived at the head, so it would be nice if all clients could check their performance right around the head. I think the issue was that if you needed to download all the blobs and verify the blobs but like the most current blocks and so it would be nice if other consensus clients could test it on devnet subject already anyway sorry devnet 8 now. 

**Paritosh**
Yeah so the link for the devnet 8 specs are there. I we will either Barnabas or I will try and make sure that it's up to date over the next days but the ideas that we wanna first have hype tests looking good and then we want to be able to run like a local testnet and then we'll spin up devnet 8 so I think there's still like a couple of phases before we're ready to coordinate that. 

**Alex**
Gotcha, that makes a lot of sense. Cool okay so sounds like maybe we want to look at performance on 7 if your client's near the head and anything else anyone wants to bring up right now for devnet 7? 

**Barnabus*
If forward syncing is still possible till next week Tuesday and after that we're gonna be outside of the period then only checkpoint sync will be available so if you want to check something with the syncing from Genesis you have like a few more days to do.

**Paritosh**
Also some client has an archive flag where you just never delete blobs I think  that's the perfect time to be testing it and if you don't want to test it let us know and we'll test it. 

**Alex**
When you said forward sync you mean with a blob expiry?

**Barnabus**
Yes.

**Alex**
Okay gotcha. Yeah I mean that's actually a good thing to see live, see how it works, once we go through that first window.

**Barnabus**
We've done it in devnet 6 I think and from that point on you have to do checkpoint sync, otherwise you're not going to be able to sync anymore, if you don't have any archive notes.

**Alex**
Okay, well so yeah client teams who are listening, take note and yeah otherwise it sounds like things are moving along so that's exciting to hear. 

### Continuation of p2p discussion [5:28]( https://www.youtube.com/live/fBVIGBrKaFA?feature=share&t=328) 

#### flood-publish changes seem to be on the critical path (disabling, just flooding to mesh, and/or staggered sending)

#### quick update from teams on strategies/timelines

Next up on the agenda we have this note about continuing the p2p discussion. I think it was the last 4844 implementers call. We essentially had this note around Gossip sub with p2p and like part of how this works so my understanding is that basically there's like a flood sub mode that kind of runs by default and there's like some concern that you know it will slow performance of things once we add the much bigger messages with the blobs. Does anyone here have anything to add? I know I think some client teams are looking into this feature, maybe if it could be enabled or disabled more granularly than it could be now, different strategies around publishing and things like that.

**Sean**
So I was hoping to catch up with Adrian from our team before this call but he's off this week. I did a little bit of digging though and I found some work that he and Akihito from our team had done around this and they had made an
implementation of like a smarter flood publishing strategy in Russell at p2p and had seen like a 30 percent improvement on like latency in publishing for like messages at around like 50 kilobytes. So it's just like a bit of like the scale context.

**Alex**
Cool yeah. As I understand this isn't a blocker for 4844 but definitely something that we'd like to ship at some point sooner rather than later so yeah sounds like we can maybe just wait, see if there is anything to add. Any other clients thinking about this, sort of looked into this issue?

**Pop**
 Actually we have a list of improvement that we want to do with gossip sub protocol but we are discussing that the first thing that we can do right now is to disable the publish we because actually we can still enable the first publish and change how it works but that requires the sharing right it is quite the patch but so we can just disable it right now like because it is the fastest thing that we can do and we can improve the first publish protocol later. 

**Alex**
Okay, sounds good. Sounds like there might be it on the subject the p2p topic so we'll just keep moving through the agenda. 

## E-Star Upgrade [8:48]( https://www.youtube.com/live/fBVIGBrKaFA?feature=share&t=528) 
### [Consensus Layer Call 113 #823 (comment)]( https://github.com/ethereum/pm/issues/823#issuecomment-1622820859) 
### [EIP discussion thread open -- comment with EIPs and will be listed for discussion for coming weeks/months – [E-star EIPs for discussion consensus-specs#3449](https://github.com/ethereum/consensus-specs/issues/3449) 

Next up is this E-Star Upgrade name.  Let's see, there's this comment here so yeah we are here, we have enough visibility in the next hard fork that you know we can start to think of a name. The El Fork will be called Prague following our scheme and following our CL scheme we would like to pick a star in this universe and or maybe not even in this universe but some star, and the name should start with an E. So I'm just looking at the comments, it looks like there's an eth magician's post here. People like Electra. It says Danny like Eniff, Danny's not here though so I'm not sure how strongly feels about that I'm assuming this has ever been not suggested, alright there's a couple different posts here so yeah I don't know if  anyone wants to like chime in their opinion but we're not going to spend much time on this, at least synchronously. 

I'm seeing a bunch of Electras in the chat, uniform, uniform Electras, and we can call it Electra, thank you again. So anyway I suppose if you really want to chime in, I'll put these posts here where there's been some other discussion although it seems like people really like Elektra and yeah maybe we'll just go ahead and assume that and if we all say it, everyone else will have to say it as well. Cool, thanks everyone.

EIP, I'm looking at this next agenda item comment. All right I don't know why we're talking about this well okay, interesting, has anyone thought about EIP's they like to get in for this next fork then this is on the agenda I think Danny probably added this he linked to 7002 so I think that oh sorry there's a few more down here so 7002 execution layer triggerable exits 6110, which is I think
this is moving the deposits, like reworking how the deposits work, there's 7251 the max effective balance proposal, I don't know if Mike is on the call but that's something he's been working on and, okay I think Danny put this on here he just wanted people to be aware of this and if there's anything else that you would like to start to get into the discussion, especially with respect to like the CL or any like cross layer features that would also involve the CL go ahead and add them to this issue. 

I'll drop the link in the chat. There we go. Vertical and VLS yeah those would be nice, so there's some there's some chatter in the chat around some other ones but I'll just let that be for now. Point being, start thinking about it, you know, presumably we're shipping Dencun very soon, you know, the next couple months and we will get to decide or at the end at that point we'll get to think about what comes next. So that's for that, and next up, we'll just move to General more like research spec topics. 

## Research, spec, etc [12:30]( https://www.youtube.com/live/fBVIGBrKaFA?feature=share&t=750) 

### [web3signer standardization Consensus-layer Call 113 #823 (comment)]( https://github.com/ethereum/pm/issues/823#issuecomment-1631261567) 

One is here, I think from Matt, who wants to talk about web3 signer standardization uh uh so I think basically there is a web like there is a standard for this API and maybe let's see is Matt on the call?

**Matt**
Yeah. 

**Alex**
Do you want to give us an overview of this? 

**Matt**
Yeah sure. So the goal here is to basically standardize a remote signing API similar to the you know the rest of the APIs that we have in the specifications, the reason being is that there's you know traction around remote signing and integration with clients and all these other things that we're working on, we want to make sure that it's pretty easy to you know integrate essentially remote siding into the consensus layer clients so the goal of us of this is to take what we already have in web3 signer basically clean it up a little bit and then put it out for kind of a comment and feedback period and then whatever we decide as a community, we will basically standardize back into web3 signer and then of course going forward, we can you know maintain that against new forks new functionality and we'll be working out of that kind of standards repo as opposed to just setting a standard within the product itself.

So yeah, basically the goal of this was just to bring attention to it, we're going to work to open up a repository in the Ethereum GitHub for these remote signing APIs, and when that's done, we definitely want a little bit of feedback in comments to make sure that we have a pretty reasonable view of the API and then, it's you know again it's intended to be long-lived and we'll continue to update it through hard forks and through spec changes so that when clients go to integrate remote signing they don't have to go through a lot of headaches with web3 signer they can go straight to the standard. So that's pretty much it. 

**Alex**
Cool things yeah. I mean that makes a lot of sense. This seems like an API that is, you know, has a good amount of adoption so the general strategy of, you know, making it a little more polished and kind of more formally supportive, I also think it makes a lot of sense, so yeah, thanks for the notice. If anyone's listening and you rely on this, take note, and yeah come back when there's an update on the API okay.

### [Add upper epoch churn limit consensus-specs#3448]( https://github.com/ethereum/consensus-specs/pull/3448) [15:08]( https://www.youtube.com/live/fBVIGBrKaFA?feature=share&t=908) 

So next thing on the agenda, there's an issue from dapplion, actually this is a PR, so let's see, is dapplion here? I'll just let you take over otherwise I can give a little summary.

**dapplion**
Yes I'm here.

**Alex**
Okay. 

**dapplion**
So yeah the background of these proposals is that as you know different items of the roadmap most namely ssf are much higher to deliver if we have a big State of a large count of indexes so we have different proposals starting around to deal with it if we don't deal with it we need different crypto and other stuff there is good proposals around this anyway so the point of this proposal is we could very easily for the nip potentially limit the churn. 

It's questionable if we if it's positive for Ethereum and it's positive to have such a big account of indexes, so we could limit the churn and then buy us some time to deal for the electro fork for a more proper solution like limit increase in max effect in balance or having some in protocol consolation. So this would just cap the max churn so that we don't find ourselves with a 2 million ballet account in about nine to ten months. Yeah. 

**Alex**
I mean it's not you know it's not a wild option. I do have to wonder like if we were to do this, you know it does kind of like marginally affect small stickers more, just because like essentially you're capped, like now everyone slows down in terms of like exiting, and it seems like if you have more validators then that's more less of an issue for you, but yeah on the other hand we don't want the set to be two million evaluators like you said so, yeah I don't know if anyone else has had a chance to look. This is something we could do, I don't have like a much longer opinion on it at the moment.

**dapplion**
So I'm aware the discussion is for Electra but these could be considered for an app otherwise I don't think it has that much of a use case.

**Alex**
Yeah it seems like it's we don't want to be changing the Deneb schedule this late in the game and I do kind of agree that it might not matter as much if we can't do it that quickly.

**dapplion**
So I would say technically this is a very simple change, probably just a couple lines on every single client. I think it's most  about getting it right in terms of security and political implications. 

**Alex**
Those are important concerns. How does you have your hand up very much are you talking Potuz? Can anyone hear him?

**dapplion**
I hear something very very…

**Alex**
Yeah it's like really tiny okay yeah try that one more time.

**Potuz**
Yeah now it should work. 

**Alex**
Alright.

**Potuz**
The issue that I find is that since this involves a political discussion and it's very very unrealistically that's ever going to happen that we're going to get into consensus on this by Deneb, and since this seems like a very simple change that we could actually put in a just purely consensus hard fork that we can just ship quickly, I'd suggest looking into other alternatives and if we don't find anything, we can just ship this. I would prefer personally to use a different pr from dapplion. I would prefer that we actually compromise ourselves to quickly ship the reuse of indices, after or with this, we could just think about this Max EB increase, because that would certainly allow us to like reduce the number of validators quickly, and I think that's a cure more than just as Danny put it, as a band-aid.

**Alex**
Yeah I tend to agree. I mean this is like something we can do and it's almost like you know if we found ourselves overnight in a terrible situation of too many validators, then yeah, we could like think about this. You know it doesn't seem so urgent, we need to do it in the next like you know a couple months, and then on a longer time scale we have other options to think about as well so it's more just probably a process of considering all the different trade-offs of these different options and picking them when we like the best. It doesn't feel like we should be thinking about changing the Deneb schedule, like no like if anything we should just be like shipping it up like in the next couple of months.

**dapplion**
So I don't think it's realistic. The thing that will ship so fast that hope I'm proven it wrong.

**Potuz**
What I do think is that we need to lose the fear of having consensus layer only forks so that we can actually deal with these issues. 

**Alex**
I don't know if there's like fear, it's just like even if we do a CL only fork it's just so much overhead like even for just the CL devs on the call right, so, you know, it's just not something to really take lightly, but certainly if we got to like an issue if everyone was convinced that like the network is going to be in a really bad place soon, then we could have a CL only fork soon. It doesn't seem like we're quite there yet or anywhere near it really. 

**dapplion**
I guess just to test the waters now we're here is there any strong opposition from anyone on the idea of copying the churn?

**Alex**
The only thing I would say is if we're doing something in parallel like for example max effective balance where we know we're going to also be touching the size of the set then you know we don't necessarily need to be doing other things and that would just probably come down to the timing of these various features right?

**mark (ethDreamer)**
Correct me if I'm wrong I mean but we've brought up these other issues of max effective balance and reusing validator indices but neither of those are specced out to the degree that we would need to implement them quickly correct so like this is really just I mean this could be done real quite simply, this is almost like difficulty bomb pushing back level of trivial, but yeah I just I would just say this seems like a much easier thing to do, to buy us time for those other things because I don't think they're specked out.

**dapplion**
Yeah and I want to point out if say the same goes to the 2 million and then we find ways to shrink it that is some dead buckets that will have to pay forever until we get to a point where consensus clients can deal with state in a very significant way than they do today, because as I'm aware of every single client needs to have a full state loaded in memory to do anything basically, so the dead weight in the state has a cost.

**Alex**
Mikhail?

**Mikhail**
I personally don't think that reusing indices will help us that much here as if the activation queue will remain full as it is today, so we'll see these two million validators as dapplion has mentioned quite soon. I don't see how their, we're using…

**Potuz**
…reusing indices is used with the increase of, is tied with the increase of mass effective balance so this two together reduce drastically the number of validators.

**Mikhail**
Okay but yeah, sure but before that time before we have this max effective balance increase, we can get to this number quickly assuming that the que will  be full. I mean like we will not deliver max effective balance before these two million while there's in the set before we see them in this, in the weather set, that's the point so it is like a kind of a countermeasure, so I mean like and if we have these two million validators and while it would mean that in terms of attestation and attestation aggregation the load will increase three times or yeah three times at least. I don't know how this is sufficient, how this, how bad it is in terms of aggregation, but from what I've heard that the aggregation is almost at its capacity today, and if we drop mobile layers on the network it's you know, it can get really worse.

And I don't believe that we will have a hard work to deliver this feature only even if it is a CL hard fork, it requires software upgrade so it requires coordination of node operators and all this stuff and all the related things.

**Alex**
Yeah I think unless it was like very obvious like almost an emergency then you know the temptation would be too high to like slip some other stuff in and then suddenly we just have another you know regularly sized hard fork but yeah I mean I did again this is like you know card to keep on the table I don't know if we need to make it. I mean it feels like we don't need to make a decision right now and certainly I don't think we need to think about putting it in Deneb so we'll just continue the conversation as things evolve. Obviously if we come back in two weeks and like the state is twice as big that's a different conversation. 

**Mikhail**
Yes so, and assuming that the activation queue will be full all the time which is not unrealistic assumption I guess and if we don't do something about whether sat, the speed of growth of whether it's that so we will get this 2 million whether it's in nine months, and yeah if clients are fine with that, I mean like in coping with this load then that's probably fine really, and nothing to care about, but if not then I think we should pay more attention to thinking on whether to do this or any other countermeasures really quick. 
**Alex**
Dapplion, you were saying?

**dapplion**
Yeah so I see with this pr, we have to choose a value and choosing that value comes with an opinion that can be controversial, but I think it's important to accept that before the beacon chain started, we chose a base reward and that's a very opinionated decision that clearly motivates the market into staking more or less. So if we took that opinion decision at the time, I don't see why we can do that again, especially as the landscape has changed dramatically from when the beacon chain was designed and today. So yeah I wanna motivate or at least disperse the fears that this is not such a controversial thing that we have done in the past, and we could do that again to adjust to market conditions.

**Alex**
Wait sorry, maybe I misheard you but something are you trying to link like the reward schedule to this change with the the tournament?

**dapplion**
Yes, if we chose a base reward that produced a widely different API than we have today we may not see the queue as full so that's a direct incentive for it, that's causing these big states.

**Alex**
Sure yeah. I mean so again touching that knob you're now touching like our security spend which is just something we want to like very carefully think about, which like you know zooming out some this is like all of these different proposals kind of touch on like either very like core security or economic concerns or like otherwise very political concerns which is why they're just they can get kind of hairy quickly.

**dapplion**
True. My point is on the design phase, when the base rewards fee was chosen, if we had if we could look into the future and see the colors that we can chain I'm not sure that that value was picked like I don't know if anyone anticipated that there would be such a demand for speaking, so acknowledging this reality just we are not going to change anything which is going to slow the inbound, it doesn't look like such a dramatic change. 

**Alex**
Right. There is a curve that's like responsive to demand right so like this there was some decision made. It's not that it's like flat right? 

**Dankrad**
I mean I would say I agree that the reward course was the most thing to adjust if we want, if we want to change the amount of eth. 

**mark (ethDreamer)**
I don't think he was necessarily saying that we change the reward curve I think he was just saying that it was a sort of political decision to begin with and that this is a much less dramatic decision this is simply limiting the rate of incoming validators, it's not saying you can't stake or anything it's just the  growth is quite high well.

**Dankrad**
But effectively it does change basically it means that you're giving preferences to those who have already staked. true over those who want to studying so it is also an economic decision so the fairer way to adjust it is to adjust the reward curve to get into New Balance rather than giving preference to those who have already staked. 

**Angsgar**
Yeah I just wanted to briefly say on this topic that there have been some thoughts in the past to just basically completely changed the way we do we dislocate validator rewards to more explicitly kind of target specific participation sizes and then a month of each stake everything kind of just shifting the reward curve might be a good kind of just pragmatic first step in that direction before we make the kind of bigger, more and more kind of deeper deep rooted change, but even before then maybe I would say one thing that would be very just useful to do in the very short term would be to just start communicating that the way we pay out rewards for staking might just change in the future so no one should basically no one should make a decision about staking and the eth, relying on that basically the payment schedule will still be in place here from now, five years from now, I think business is preparing the community for that this might change in the future would be very valuable to do in the short term already.

**Alex**
Yeah, I mean that makes sense and like you know one way we do that is like having these conversations on these calls so if people are listening then they can start to understand that maybe something will change. 

So that being said I think we might be done with that topic unless there's any final comments, otherwise I'll open this up, are there any final remarks or things not on the agenda anyone wants to discuss, otherwise we can go ahead and wrap up a little bit earlier today. Okay, sounds like no. I'll go ahead and call it. Thanks everyone for attending and uh we'll go ahead and close. 

Everyone thanks the host and meeting ends. 
 
## Attendees

* Alex Stokes
* Rubens
* Saulius Grigaitis
* Sean
* Spencer
* Stefan Bratanov
* Terence
* Trent
* Paritosh
* Pop
* Mario Vega
* Marekm
* Roberto Bayardo
* Carlbeek
* Mark (ethDreamer)
* Barnabus Busa
* Gajinder
* Pooja Ranjan
* Potuz
* Ahmad Bitar
* Alexey
* Andrew Ashikhmin
* Anna Thieser
* Ansgar Dietrichs
* Matt Nelson
* Alexey
* James He
* Nazar
* Dan (danceratopz)
* Preston Van Loon
* Dankrad Feist
* Lightclient
* Phil Ngo
* Dhruv Bodani
* Nico Flaig
* Mike Kim
* Ben Edgington




