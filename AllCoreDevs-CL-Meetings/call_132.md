# Consensus Layer Call 132

### Meeting Date/Time: Thursday 2024/4/18 at 14:00 UTC
### Meeting Duration: 01:10   
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1010) 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=srOu8TqFYYM) 
### Moderator: Danny Ryan
### Notes: Metago

# Agenda

## Electra [6:10]( https://www.youtube.com/live/srOu8TqFYYM?feature=shared&t=370) 

**Alex**
Okay I'm just double checking everything's working okay it looks like the screen transition also. 

Alex your audio is quite bad right now.

There we go, okay but it's only like part of the window. 

I don't know Tim do you see what's going on and do you know how I can fix this? 

**Tim**
So sorry what do you see?

**Alex**
So it's like only recording like the upper quarter of the zoom window and not the whole.

**Tim**
Yeah so like if let me open it the so when you have like a screen there usually like a little red box that you can drag and drop to make like to make it bigger, if you like hover over. 

**Alex**
Okay this is kind of good, everyone sorry for the technical difficulties. I'm streaming and any let's go and get started yeah to restarts I think I'm going to leave it as is because I've also just had a really delicate so hey everyone this is consensus call 132. I need to find the agenda what I keep losing I promise kick things off. Okay let's go ahead and get started it's really hard to hear me.

Okay can you hear me now? Can you hear me now yeah okay is it better now? try this okay I on out okay may we'll try this is a spider can you hear me now can't any okay is this better yes I don't know why I've is shoes okay can you hear now? Is this better than it was entire quality just a lot more quiet, I don't know I'm like yelling at my computer, okay let's go ahead and get started I think this might just magically resolve this is what I can so anyway.

Okay Electra, so the first thing to call out is we have nice specs release of the initial Petra specs, very exciting. It's so quiet okay I don't know why I'm having his issues.

**Tim**
It's fine now.

**Alex**
You're the only one saying that though, everyone else is saying they can't hear anything.

**Barnabus**
Yeah it's very very quiet for me too.

**Alex**
Let me try I feel like this is going to explode if I try to it's something happens with my audio setup I don't know I don't know what's going on anyway let's go and get started. I'm assuming you guys can all hear me now and I'm praying that the stream is working, either way the first thing was Electra and so let's see here, we have the initial specs release which is very exciting, I don't have a link handy, but I can go get one in a second, but yeah so Alpha zero is out and the idea is this is an initial target for devnet zero so thanks to everyone who was involved getting that out, special shout out to Hsiao Wei and Franchesco, with help with the testing but yeah it has the four EIPs that we've included in Pectra and should be a stable target for you guys to go ahead and start implementing.

So yeah super exciting, I did want to call out there's this question of how we're doing consolidations in Max evb and it looks like what we're probably going to do is have them in be initiated from the El and right now the way they're kind of written is they're originated from the CL. 

This is fine, because most of the processing logic that the beacon chain will need is going to be the same regardless of the source, but if you drill into the specs you'll see there's not really anything written down around how a like validator could initiate them, I think the plan is generally for our initial devnets just to kind of have someone hack something together just locally to inject some operations to do this, but otherwise not worry too much about building out like an operation pool, gossip for these operations and all that because we're very likely in devnet like 123, moving to like an execution source for them just like 7002 so I just wanted to call it out if you find that part confusing it's because it's a little weird right now.

So otherwise yeah let's see the spec is out, there's test vectors and yeah so nice work everyone. 

## EIP-7549: [How to handle Deneb attestations at fork boundary]( https://github.com/ethereum/consensus-specs/issues/3664) 
Consider consolidating EL requests into unified envelope: [Add EIP: General purpose execution layer requests EIPs#8432](https://github.com/ethereum/EIPs/pull/8432) 

[11:49](https://www.youtube.com/live/srOu8TqFYYM?feature=shared&t=709) 

Next up, there's a number of questions around different EIPs, different parts of the spec, we'll just move on to the next one so there this question of how to handle deneb attestations at the Electro Fork boundary so EIP 7549, this is the one that's like changing how attestations work and we'll get in the situation where the last epoch of devnet will the decisions made in that epoch will be includable according to the spec into Electra but the way that you make the MB is not compatible with how you make them in Electra so we need some way to handle this and I wanted to bring it up just to see what everyone's thinking. There's a couple options or maybe I'll just stop there.

Does everyone understand the problem? 

Okay we got a thumbs up if you don't it'll probably become clear as we discuss, but there's a couple things we could do like one of them is just do nothing on mainnet, most people get attestations in pretty quickly and so like you know if we're at max performance then really it's just like attestations in the very last slot of deneb would have this issue and that's not ideal but it does mean that the specs can stay as they are and it simplifies everything else, because then we get into the other options where we do something to handle these attestations, probably like the most comprehensive solution is that we just keep another spot in the block for all of Electra for the sort of the deneb style attestations, we could do this it's just now there's this extra list that's kind of there for like just a few slots, so yeah it's just more code to maintain and the questions like what do we really gain for it.

Yeah there's other solutions like you could imagine clients try to broadcast both or like you wait if you know that you're at the end of deneb and like if you don't see your attestation get on chain well I mean yeah then I guess it's a question of how you do this because you could imagine trying to broadcast if you don't see it included on chain then you rebroadcast but then there's like slashing concerns, you could just wait maybe say halfway into the epoch there's like some design space here. Has anyone here looked at this and do you have any opinions on the path forward?

**Mikhail**
Just a quick note, if we use the same field of the same attestation field in the block that we need to understand that Max stations per block is going to be reduced significantly so those are the stations are not packed into more tight aggregates that we use for with this EIP since Electra then they will probably not be accommodated um there will be not enough BL capacity for that, so it probably makes sense for the last if we want to do anything with that it probably makes sense for the last slot of the epoch before Electra for epoch just to make them signed yeah just to make this you know index set it to zero so make an Electra like Electro Station instead of the station I don't know how what other implications are having this.

**Enrico**
Are you talking about the option suggested by dapplion to wait a couple of epochs before setting everything to zero? Is it this what you're talking about?

**Mikhail**
No, if yeah if we take this option, we should understand that if we don't aggregate them so we have like basically we'll have eight attestations instead of 120 per block at max so we probably won't be able to and put 64 attestations from the previous epoch

**Enrico**
Yeah that's hav yeah I haven't thought about that implication of doing that, so does it won't work at the end for other reasons right.

**Alex**
Okay so one option would be you have custom code your client to basically say within the last slot but maybe the last like half EAC like there's some parameter here basically you would set the committee index to zero and the reason you do this is because then you can independent of having the validator touch anything who makes who makes the attestation you can repackage the old format into the new format so that works. 

You know there's implications around I think some of the Dos protections for attestations, because they assume the committee index is a certain thing but might be fine.

**Mikhail**
Yeah so are we concerned that much if we just lose the last ? 

**Alex**
I think not but the question is like more about attack scenarios so like you know, let's see yeah I guess if you just ignore them, I mean yes this is like the do nothing approach and it might be fine enough so that might be the path forward right now is you know the way the specs are written it kind of assumes that this is just yeah you ignore the ones that don't make it in a time and if we do this then that might be fine and then we can kind of analyze different attack scenarios further down the line and see if we need to harden this but that sounds like a good path forward for now. Does anyone…?

**Mikhail**
Yeah because if you those attestations will be applied to the epoch anyway so which not be a be problem.

**Alex**
Right, the one concern would be if there are many like if there is an attacker who tries to delay for some reason then they wouldn't go on chain and that could impact justification, so there could be some like weird finality delay around the fork if someone is really motivated. 

**Terence**
It's also worth to keep in mind that those attacks are highly attributable in a way so like we can easily tell that who like basically who's doing that I'm not saying that should be the reason to not to do it but that that's just one point of note right?

**Alex**
Okay well it sounds like I mean especially for devnet zero, we'll just keep it as is which is basically ignore the issue.

**Sean**
Yeah so I saw the dapplion had left the comment here I don't know if this is what Enrico was referring to, but to me this looks like essentially like a slightly better version of doing nothing, because it's not like we couldn't fit any pre-Electra attestations in, we would be able to fit up to like whatever the new limit is.

**Mikhail**
The limit is quite low though so…

**Sean**
Right.

**Mikhail**
In the best case you can update like seven attestations per block consider perfect aggregation and just use just one  slot for the current documented attestation.

**Sean**
So but like isn't this just very similar to doing nothing but like slightly better?

**Enrico**
But then you have to deal with the complexity of doing this translation in the code to gain maybe very few arguments in terms of security, so it's maybe slightly better but less effective in any case so maybe nothing.

**Mikhail**
Actually if things will be good terms pation so the first Epoch of Electra will accommodate all those attestations from the last slot there will be enough capacity to do that.

**Alex**
Okay so let's do nothing for now and we'll just keep in mind that we'll probably want to look at this a little bit more closely and consider different options, but yeah this seems like a good path forward and generally just have this one on ones radar if you weren't following please go take a look um and yeah we'll revisit it later.

So the next one is a new EIP 8432, and this EIP essentially wants to think about how we are moving messages from the El to the CL so right now with 6110 we have deposits with 7002, we have these withdrawals we're likely adding this sort of consolidation message from the EL.

So we have all these things proliferating and the questions like how we want to structure this in the execution layer. So this EIP is from light client, do you want to maybe give a little overview?

**Lightclient**
Sure, basically the idea is that on the execution layer we have generally not added lots of things to our block body and kind of our block header but with with these new messages that we're trying to propagate from the El back to the CL, the sort of template has been put it put a commitment of all of those operations in the header put a list of them in the body and extend those data types.

And so what this proposal is trying to do is simplify the way that we do that so that we don't have to continually extend these data structures which at least it feels on the El side is pretty manual task of updating mini mini code sites where you're dealing with these, and put it all into a single type, so we're reusing the same machinery that we have for the transaction types, which is prepending a single type bite in front of the rlp encoding of the transaction use that as a discriminator to figure out what type of transaction you're dealing with and then parse out the transaction data from that.

It really doesn't have a lot to do with how things are processed on the CL. I think it would just be good to get thumbs up from any El teams here. It seems like it's had reasonable reception uh and then get a thumbs up from Cl's that it's okay it's okay on your side that maybe these data structures aren't mapped one to one, cause like right now on the spec for Petra on CL side these messages are individual lists with an execution payload.

So if you wanted to have things analogous across the two layers, on the CL maybe what you would have is you would have a union of requests, and you would put every individual request type. That to me doesn't it's not really important it's whatever you guys think is the best way of doing it. Yeah so I guess I can stop there any questions or thoughts if that's seems like a reasonable idea.

**Alex**
So I think we would want to try to keep the layout the same across El and Cl as much as we could and so really like I generally think this is a nice idea, the only thing is you know if we need to go change a lot of the structure of the vzer specs it's gonna kinda delay us getting to the devnet. 

**Lightclient**
I just don't want to put a lot of work into something that we already feel confident that we're going to change again like we can have the specs ready by tomorrow we just have to have people decide, and I think this is still this is much more of a CL or sorry an EL issue to resolve.

**Justin**
This is Justin here from Besu, I think that we recognize the need for this it seems sensible the implementation looks good I haven't had it open next to the code to actually take a look at the implementation overhead yet, my gut says it's fine, but I would like to have a chance to actually do that before making a stronger commitment. 

**Lightclient**
Do you guys have 6110 or 70002 implemented?

**Justin**
We do have 6110 implemented and 70002 is about half done.

**Lightclient**
Okay so I think the main diff between what is done right now and what would need to be done is you would have to go in and replace the exits or the deposits that you've added to the header and the body replace it with the requests type and then implement the request type so the rework that would be done is kind of just renaming and retyping that value in the header the reason I'm like bringing this up trying to bring this up now is that if we add 7002 if we add consolidations then we're starting to look at like bigger refactorings of, okay we've added three things to the block head or three things to the block body we got to go and delete some of those we got to put you know retool them into this single type.

So it feels like if we've only implemented 6110 it's a lot faster to fix that up than down the line.

**Justin**
Yeah fixing 6110 from our current implementation would be negligible there's no big deal there.

**Lightclient**
I don't want to put you guys on the spot like you can take a look at it offline I just want to try and get this decided by tomorrow so that we can get the specs out.

**Mark**
Yeah all right we can chime in, just give me a sec, terms of wasted work it seems like especially if we end up adopting this the long term because it saves a lot of long-term complexity it doesn't make sense to not adopt it in the near term to save, I guess part of an initial devnet ?

**Terence**
Do we need to come to consensus on what this request type are inside the payload or they are outside the payload by kind of like a kind of like a envelope format um do you guys have thoughts on which direction is better here?

**Lightclient**
It feels like it would go in the payload but it's not really something that I feel strongly about so if people think it needs to go in the envelope because you're not going to put it in the actual payload type on the CL then we can do that.

Like this the EIP allows the flexibility it doesn't prescribe that it must go in the execution payload. Okay um sounds like people will review this offline generally positive sentiment the one question that I think is pertinent to maybe ask here is are there thoughts on how you would like to deal with this from the engine API, I also want to cut this spec tomorrow or Monday and on the engine API side there's two ways that we could go about it I wrote it in the PM issue if you want to take a look, but the two ways are basically we extend the execution payload or the envelope whichever one people prefer, with each individual request type, so there would be a deposits list there would be an exits partial withdrawals list, a consolidations list.

Those are individual elements element and those individual elements have only one type of request the named request that the list is named after so then on your side you would parse that out put it into the payload put it into the block or the envelope however you need to.

That's one possibility the other possibility which is slightly simpler for the EL, but I think it's kind of negligible we had one additional list either in the envelope or in the payload called requests and those requests have you know several different request types that could live within the list, and so you would have to look at the Json field type and determine what type you're dealing with and then parse out that data based on the type field.

Is there any feelings on either way for that so that I can look at putting that into engine API.

**Mark**
Not a super strong preference but I feel like deserializing is generally easier when you know what you're expecting but yeah I guess nothing would stop it either from being an array of arrays separated by type. But I think we could do either but just in general deserializing is easiest when to type.

**Lightclient**
Okay that's one leaning slightly towards just having individual list of request types. 

**Justin**
Yeah Besu probably doesn't care I think I have a loose preference for individual request types.

**Lightclient**
Okay I think that's enough for me to go ahead get started unless someone feels strongly against that I'll get his spec out for that there or tomorrow people can review it and then let's solidify it on Monday.

## EIP-7549 update: [EIP-7549: replace committee_bits with committee_indices consensus-specs#3688](https://github.com/ethereum/consensus-specs/pull/3688 [30:56](https://www.youtube.com/live/srOu8TqFYYM?feature=shared&t=1856) 

**Alex**
Okay great if there's nothing else on that we'll move to the next item here, so there's a suggestion to rework EIP 7549, essentially to make the onchain aggregation more flexible. Mikhail this was your PR do you want to give us an overview?

**Mikhail**
Yeah thanks Alex so quick overview, what we do here is basically switching from committee bits to comme indices this allows same aggregate to have yeah in one aggregate there can be in one chain aggregate there can be several network aggregates from same committee. I noticed this is quite common situation where a blob contains several aggregates from same committee from same slot this is something constantly happening on mainnet.

This proposal is kind of like has more makes this more like more room for more aggregates from same committee so what's problem with like 7549 is it reduces max attestations from 128 to just 8, which means in theory max number of aggregates from same committee that can be accommodated by one block is eight so you can do more and if we want to more if this is something desirable we can go this path and yeah just allow basically one chain aggregate have several network aggregates from same committee for this we need to switch from committee bits to committee indices this is one of ways to do it so first question is whether it is really needed probably potentially it can help with case of bad network conditions but we there are many aggregates received from same committee and we want to accommodate them but actually eight is already pretty good number.

I don't know so first question to see is basically is this is like having this dation any cause any sort of concern do we want to do something about it do we want to make it more flexible yeah if we want then we need to decide on how we keep commit indices basically what number fights will what type we use so basically Comm index fits into one by at moment because we have 64 at Max and if we use commit index data type there is data overhead, so it is not significant, but yeah we could make it as complex in terms of data as good factor by using just one bite by using unit8 problem here is we don't have un dat in spec I don't know why we try to not introduce more un types so that's basically overview of this proposal.

**Akex**
Okay thanks I believe there is 8 defined it just might not be used but there definitely is one yeah. I guess I have couple questions like if eight if having like Max attestations at eight is issue here like could we just go to 16 or like some bigger number does that would help right?

**Mikhail**
Yeah that would help but if we go to bigger number then we should accept the fact that block size like theoretical block size theoretical increase

**Alex**
Right would go up you had really nice chart in pr looking at like this issue you brought up with having committee indexes be eight8 bytes versus tight packing of bit field we have now and what I didn't like was with u64 you get to place where at like million validators.

It seemed like size stations would like pretty much be status quo which was like attractive benefit this EIP is stations on chain would get much smaller do you am I interpreting chart correctly I guess is first question?

**Mikhail**
Yeah so you mean like so size is pretty much same as with status quo but it can accommodate for more attestations like from for more commities for more slots.

**Alex**
Okay I see so you can still have them more densely packed okay so that helps.

**Mikhail**
Yeah yeah so we could use like where in original EIP original proposal there was analysis of like different back stations basically to accommodate the same number committees if we consider ideal aggregation, so we could have Max attestatations to which means yeah basically one as station slot can accommodate for one spot worth of attestations received from Wire and here we can just basically increase number slots increasing capacity of block which also basically helpful case of yeah of network bad network conditions because you can commodate for more slots in one block.

**Alex**
Great. Fransesco had interesting question in chat like is there some way to use a smaller type for theying multiple committees so like rather than have like eight bytes per committee index, could we again somehow pack that down little more tightly?

**Francesco**
Just to clarify I mean like U let's say we want to say I don't know at most eight attestations per committee then we could just use three bits per committee and just like where thing we include is just multiplicity like how many of them there are instead of community index.

**Mikhail**
Yep but I think if we want to do something like that then we could probably use 8 which is really quite close to using bit vector with just one bit I mean like quite close in terms of data complexity, yeah but something like that is also possible but again this is if we want to accommodate for more than eight aggregates from same committee I don't know this is more question to those who want to chain and see is it like any problem.

**Alex**
Okay well so it sounds like to move this one forward everyone is not aware it sounds like something we won't decide today, might require little more analysis but otherwise yeah nice work Mikhail. 

I think that's that unless anyone has any other comments. So in that case Mikhail has another PR to update part of 7251 do you also want to give us overview of that one?

## EIP-7251 update: [Finalize deposit before applying it to a state consensus-specs#3689](https://github.com/ethereum/consensus-specs/pull/3689) 
 [39:32](https://www.youtube.com/live/srOu8TqFYYM?feature=shared&t=2372) 

**Mikhail**
Yeah so is more related to 6110 but it anyway leveraged on 7251 pending deposits, pending balance deposits here. So the original reason for having this proposal is basically 6110 removes variant pop key pop index yeah index of other respond to pop key this basically never changed so there was because before 6110 we have this large FL distance so no reward is possible Beyond this follow distance like no realwork is visible Beyond this follow distance so we kind of like having this invariant.

And 6110 breaks it so client implementations will have to make this POP key this cash Fork aware so on two different Forks the same index yeah can correspond to different pop keys this is something to handle in implementations idea was basically to have deposit que explicitly in State, to have it first finalized then apply after this deposit queue is finalized, only after this point start applying deposits start creating new validators and in this case it also means we are processing top-ups, after being finalized.

So bit of analysis here so I already mentioned implementation complexity that can be alleviated. Other things are in this PR signature check happens only when deposit is being applied, and since number of deposits are limited by activation chor number of deposits processed per ifocus limited by activation CH, we have limit natural limit on signature verifications per Epoch, which is also kind of nice because it helps to alleviate attack vector where someone just packs thousand of deposits in block, before this pr th000 signature verifications would need to be processed in this case yeah this tax is kind of like really not realistic though because of it really has high cost.

Also with this approach we can get rid of activation eligibility which means it there is no use for this field in B record so it can be repurposed in future sure if it matters, side effect is top Ops needs to be finalized before they can be processed. I don't think it's big problem probably it has some positive outcomes in case of inactivity leak, and these kind of situations so no one can pump their portion of state own with respect to total amount of state yeah so problem of this q that it will need to keep more information, more data than it is in original 7251 proposal yeah this is kind of like 176 bytes of additional data per every deposit slot.

I would say before 7251 would not be problem because all this information that is coming from deposit contract either you create new validator so you basically hold most of this information in State so state will not grow significantly but since in 7251 we have switch to compounding credentials while making the top up then probably have lot of topups doing this switch.

For topups this extra information is basically not needed so it will just waste more space in beacon state but yeah so to highlight data complexity with 100 W you yeah also mentioned deposit processing is limited by activation chor so if we have like 100 whether is 100,000 in activation chor it will mean this deposit que is quite full and will consume around 0 18 megabytes of data I don't know how big of concern it is, so that's kind of like view of this proposal and pros and cons.

**Alex**
So yeah thanks that was thorough. I haven't had chance to look at pr specifically but yeah I mean I think reasoning sound and it sounds like something we probably want to do unless yeah there are some complications with yeah either data complexity or something like that once we start it again I don't know if anyone else here has had chance to look and has any thoughts?

**Sean**
So I looked at it little bit I think it's probably worth doing or at least continuing to explore but I will say we've merged some changes into we're working on some changes in Lighthouse to make finalized firsts un unfinalized Pub Key cash difficulty like more simple so I don't want to like overweight that deciding on this I think this has like solid features otherwise though.  

**Alex**
Okay cool so yeah again I would just say everyone keep it on radar I don't think we' necessarily try to get this in for v0 but know it'll assuming if we want to put it into Petra then it'll come down line.

**Mikhail**
Cool thank you by way small note Francesco suggested and said basically activation eligibility book like to make it no use for activation visibility we can basically add just an epoch to pend in Balance deposit skew and do this finality St do process do increase balance after it gets finalized so this is doable with much less data complexity.

## Blob count increase: [Consensus-layer Call 132 #1010 (comment)](https://github.com/ethereum/consensus-specs/pull/3689) 

[47:48](https://www.youtube.com/live/srOu8TqFYYM?feature=shared&t=2868) 

**Alex**
Okay great next up we have suggestion for yet another EIP. Pari, are you on call, or maybe Tony?

**Paritosh**
Yes eight yeah, do you want to introduce it or should I give an overview?

**Alex**
As far as I know it's just suggesting we bump up Blob count as electra 

**Paritosh**
Exactly that's pretty much it that we conduct bunch of tests and simple blob increase so that focus from or any time client devs have can be focused on pure dev research rather than anything else and yet we're signaling that we offer some amount of scalability this year or some amount of blob increase based on how well testing goes and it's also tied to potentially including T EIP that also increases head.

**Alex**
Right one that would change call data cost execution cost yeah okay?

**Paritosh**
Exactly.

**Paritosh**
And when I look this EIP did not suggest specific number but more of this is just kind of signaling today and then as things unfold as we get more mainten that data we'll be more comfortable with particular number by time we get to Electra is that idea?

**Paritosh**
Exactly and that most of testing and figuring out number part can be done independent of Cent teams or not completely independent but mostly independent ofam.

**Alex**
Right okay cool I think this is really nice to have like yeah we'll see how P shapes up I think we'll chat about it towards end of call if we have time but yeah I think our base case should be bumping the ball counts up at least for Electra once we figure out how to do that safely on you have hand up.

**Ansgar**
Yeah just wanted to briefly mention I agree that I think it's good idea especially with 20 e that kind of worst case normal work size we have some room and we also had this kind of alternative EIP couple like I think two calls back, 7659 or I think that's not yet merged which would do of similar thing but with gradual increase, I think this situation is little complicated by fact that basically Electro might not in principle ship together with P already right and so basically how much we would want to increase depends of course on this and depending on how much we want to increase I think it also that influences whether we want to have gradual increase or just one time so I think it makes sense to basically have those two kind of alternative is out there so we kind of decide closer to electra which on I think it's that we just say hey some sort of lob increase will be part of Electra and just one thing to flag, if we end up going with simpler kind of that power just presented there's one time change necessary to way we do blob base fee adjustments, so in our kind of initial e we kind of bundled those, but I might pull this out it's really small adjustment but basically we would want just want to make sure that there's kind of 12.5% maximum change of blob base remains same and currently unfortunately quirk of how 544 works that if we increase number of blobs then basically that adjustment factor also increases which that's not of course not wanted so we have to like make one time change to keep that constant no matter block count so if we don't bundle this then it will be small separate DP but it's on line change just to mention it right thanks okay yeah that's good to keep in mind.

**Alex**
Cool okay thanks for that we will scale blobs with Electra one way or another I wanted to take few minutes just to do temperature check so alpha zero specs are out.

There's quite lot in there how are client team feeling implementation wise it could be that you haven't really had chance to dig in too deeply I know last time we discussed and like different teams had different amounts of progress on different subsets of EIPs does anyone have status update there do you feel good about it do you not feel good about it any thoughts like that, the context being we would like to get to Dev zero say like next month so yeah it's so there there might be quite bit to do.

yeah Sean?

**Sean**
So yeah I think in next month we can do that one thing is related to generalization of execution layer triggerable requests, if we include that in devnet zero that would be better for us because it's like right now we're implementing three different EIPs that might change this and we might be imp ing those just to target devnet whereas like then we'll use generalized format in future so just common I sort of feel like if we included that in devnet zero as supposed to just strictly what our current targets are that would be beneficial 

**Alex**
Right yeah I agree and this is what like client was proposing with combining all these different request types.

**Sean**
Right.

**Alex**
Yeah yeah I agree.

Okay cool okay, so let's see I think that's it on Electra is there anything else we want to discuss right now? 

## Research, spec, etc
[New post on issuance](https://ethresear.ch/t/reward-curve-with-tempered-issuance-eip-research-post/19171)  PeerDAS: clarify mapping node-id to attestation subnets. [54:00](https://www.youtube.com/live/srOu8TqFYYM?feature=shared&t=3240) 

Okay looks like no cool next up some different spec and research topics to discuss one thing just to shout out there was post by Anders around issuance. I think he just wanted to bring this to everyone's attention. I'm not sure if he's on call.

**Anders**
But yeah I'm here yeah.

**Alex**
Great do you want to give us little overview?

**Anders**
Yeah just 30 seconds or something I so I was back in January I was on call and highlighted an e post that written where I sort of discussed by relevant properties ofs level that we need to consider when changing reward card and now I finished new research post that Ares little bit more deliberate for change to reward curve and so I would just like to encourage resourcers to take look at it and so in this post I go into great detail concerning many tradeoffs that we must balance for example conditions for S stakers compos composition of staking set, Economic Security and discouragement attacks, and so also I will link in chat and also yesterday I put up more sort of educational post explaining foundations of minimum viable isss and so I will try to write some more educational material in this manner also directed toward community, I think it will be important as well yeah.

**Alex**
Great there is okay excellent so yeah everyone take look and we'll just keep conversation with issuance going.

[55:55]

Great so next up we can turn to Peer do there was particular request here let's see I don't know if age is on call but essentially there is question around some of details around mapping peers and their note IDs into which subnets they're on and I think this kind of touched this like Network shards refactoring that has been floating around this has implications for pios and how you would like structure yourself in network to do sampling and also distribution so yeah I don't know if anyone who's been engaging with that issue is on call and would like to bring up their questions?

**Adrian**
Oh, here we go. Hey, yeah, I can have a few words. Yeah, so there's multiple aspects; this one's part of pay part of just main it as it stands. With the destination subnets, essentially the spec as it stands has kind of a mistake from when we first did it. Mistake is probably not the password anyway, but there's an improvement where we can use the first bits of the node ID to map to the arbitration subnets, which allows us to hopefully improve discovery. 

So we’ve been trying to kind of get this in for a while, but there's now added complexities when we extend this into pd. The main reason I'm pushing for this is because there's two main reasons: one, I would like to just move ahead in lighthouse, in mainnet, just doing a simple version of this, and then we're also prototyping to have it as a foundation for pias when we, when we get down to pias, we're going to have to add another pr anyway to formalize the actual mapping. 

But if we can, I just mainly want to get all of the consensus client teams to at least have a look at it and I haven't heard of any like strong opposition, so that we can start prototyping with p and actually just put this into mainnet it's entirely back is compatible but if all the client teams agree then it just becomes more efficient. 

There is some technical challenges with P but as far as I can tell, we can if we put in minimal version now, which potentially doesn't have rotation, we can add another pr later that adds the complexities for pd, but mainly I just want to put it into Lighthouse now, get everyone to agree and then everything is efficient for mainnet and it's also we can start prototyping for PS. 

So I guess, if you haven't seen this pr before and you're a consensus client team just please have a look and if you have a stronger position just let me know before we start building it. Oh, going too deep down that b, that's about it. Thanks. 

**Alex**
Great. Thank you. Has anyone had a chance to look at this any other cl teams? Sounds like not yet, but yeah, please take a look and it sounds like this is a direction we want to go in so let's make it happen. Okay. I think otherwise that was everything on the agenda. Is there anything that anyone else would like to discuss right now? Do you have a question?

## Open discussion/Closing remarks

[59:32](https://www.youtube.com/live/srOu8TqFYYM?feature=shared&t=3572) 

**Lukasz**
So I wanted to clarify, what's the current status of inclusion list EIP because it was, we had some reservations on the EL and I'm not sure what the end result was. 

**Alex**
Yeah. This was one other thing to discuss. So I think on the last execution call, yeah, there definitely were some reservations and I think I was essentially going to see if anyone wanted to bring it up to discuss on this call. It sounds like to me there are some concerns around implementing it especially in light of account abstraction. I don't think anything's really changed there, but yeah, I mean, one like on one on one the call like to get into this EIP, I think we, I think it was CFI but also at this point we have quite a bit in P already. 

**Lukasz**
I think it was even included that's why I'm raising this if it was only CFI then I wouldn't raise this but it was even, I think included. 

**Alex**
It was never included. 
**Lukasz**
Okay. Never included. Then my confusion. Then. 

**Mike**
I would say nothing, no new advancements. The 3074 issue is going to exist no matter what, there's no silver bullet there. So yeah, writing a short doc on kind of explaining the issue, but I would say at this point there's not much confidence that we could get it fully resolved in a way that would be happy for Electra, at least that seems to be the sentiment broadly.

**Alex**
Saulius?**

**Saulius**
Yes. I have a couple of questions. So is there a solution for test vectors as the spec is progressing very fast and the published test vectors, they get outdated very soon. So maybe some client teams build the test vectors from this spec or is there a solution for this? 

**Alex**
Right. Well, there are the test vectors for the 150 alpha Zero release. Is it release or yeah, yeah. Okay. Great. Barnabas has link. So yeah, generally when we have a spec release, we also like make all the spec test vectors from the spec and then release those as well. 

**Saulius**
Okay. So, so this then the zero likely will target some spec release some exact spec release that will have test vectors released too. 

**Alex**
Yeah. The intention is Alpha zero, although if we change something with respect to this one EIP, what was the number, the one with the request refactoring that we were talking about? Let's see, let me find it. There's way too many messages in the chat. 8432. 

So that might have some implications for just how we like structure things syntactically, but otherwise the functionality is all in there and Alpha zero. I don't really see any other major changes with respect to that and then that gives everyone a clear stable target for devnet zero. 

**Saulius**
Okay. Thanks. So another question on on D working group telegram chat, we were discussing today an issue where, essentially if an available block is imported in a fork choice then the roots of that block may influence the fork choice and essentially the weight of the fora, so and I remember that there were some discussions before and that actually the reason why we don't right now, we don't import blocks that doesn't have all the blobs available. And maybe there is some person in this chat in this call that knows a bit more about security, the issues of this approach where unavailable blocks are important in imported in fork choice because on this telegram chat, there was no response from such person.

**Alex**
Okay. And so could you just state the question again, like the concern is I'm importing unavailable like I'm importing blocks into the fork choice with unavailable blobs and the question then is like what to do about that? 

**Saulius**
Yeah. So, some malicious validators may vote on these unavailable blocks and this could cause, is it clear? It's a bit tricky to explain. 

**Alex**
Well, I mean, if I'm following my understanding would be that these blocks wouldn't go into the fork choice, right? So like I don't know how, yeah, but Francesco was offering that it should’nt go to the fork choice just filter out.

**Francesco**
Sorry. Just what I was, saying in this chat was basically today, what we do is to just not import blocks that are unavailable. I think that's to that's basically fine today, but it wouldn't be fine if we move to P with the trailing fork choice. I think even today it's debatable that it's the best thing to do, but I think it's okay. And there's not much of an issue with it. 

But um, what changes when we go to P for choice is that, you can even go from. So like today, um, you can only go from um, availability being false to true, like is there available first being false and then true, when we move to P fork choice, it can go even in the other direction from true to false. And yeah, this basically creates like kind of different scenarios that are not um, you know, you cannot see today. 

I think what we should do instead is basically to not use these data available to gate the import in the fork choice, but to use it just as a filter. So when you're running, you just import a block in fork choice, but when you're running ahead, you, you don't basically go down a branch, where like basically you get to a certain point when you're looking at children, we block and you filter out the children that are unavailable. So just, yeah, just like as a simple filter directly when you're running the fork choice. Um, and yeah, there's like various reasons for that. I'm not aware of like a problem with doing this, but yeah, the question was, you know, when the decision was made for for to instead use, is it available to gate importing? 

Was there some specific attack that people were worried about or yeah, basically why it was that, why was it decided to do that and what what's the impact of that like maybe I'm missing something? 

**Alex**
Does that clarify? 

**Salius**
Yeah. 

**Alex**
Okay.

*Salius**
I mean this, this clarifies my, uh, FL the explanation, but I mean, we are looking for a person, which knows why in the current spec in deneb spec why exactly it was chosen to not import unavailable blocks or blocks that doesn't have all the blobs. So is there such person in this chat? And if not then, all that. So someone know, right? 

**Alex**
Well, with 4044 I mean, it's just like strictly safer to do it this way, right? Like you just cut off even the possibility of these questions if like you just wait until you know everything's available. 

**Saulius**
Yeah. But if we are discussing to change it in Beust, then it's likely we can do it right now in with the current blobs.

**Alex**
Maybe. I mean, if 444s working well enough, I don't see why we need to change it. 

**Saulius**
Okay. But it also should be related to the thing that we do not do any validator duties if payload is invalid. So it's, it's in some sense, it's. So if the payload is not validated yet. So it's in some sense, it's a similar problem. 

**Alex**
Yeah. I mean, I think it's the exact same reasoning. So before 4844 like yeah, like you can just say don't even consider it with respect to fork choice. So you don't attest to it, don't try to put on top of it for exactly this reason with Pier dots, if we do move to some trailing fork choice, it does get more complicated, and then yeah, I think you'd need to have like a more like a richer view, I think like Francesco was suggesting as to like what's, yeah, the words get overloaded, but I can't even think of one that's not valid or available, but basically you would have some notion that like this block is here and it's almost like pending.

Maybe that's a good word for it, it's like pending in the fork choice and then you just have to wait for more information to move forward.

**Saulius**
Anyway, if anyone knows this someone who did the security analysis of this thing and if there was an explanation to do that the way it is now in the net then yeah, please invite this person to us working group and we can proceed to discuss there. 

**alex**
Okay. Sounds good. Does anyone have anything else? I think that's all we had on the agenda for today. And if not, we can go ahead and wrap up a little bit early. I'm sure you're all very busy with texture zero, so good luck record.

# Attendees

* Tim Beiko

* Alex Stokes

* Csaba Kiraly

* Echo

* Nishant

* Mikhail Kalinin

*Nazar Hussain

* Hsiao Wei Wang

* Paritosh

* Anders Elowsson

* Carl Beekhuizen

* Saulius Grigaitis

* Lightclient

* Preston Van Loon

* Pop

* Roman

* Ben Adams

* Toni Wahrstaetter

* Roberto B

* Ben Edgington

* Enrico Del Fante

* Pooja Ranjan

* Cayman

* Dan (danceratopz)

* pk910

* Phil Ngo

* Paritosh

* Mario Vega

* Gajinder

* Marcin Sobczak

* Anton Nashatyrev

* Barnabas

* Terence

* Trent

* Mikeneuder

* Mark Mackey

* Adrian Manning

* Justin Florentine

* Ansgar Dietrichs

* James He

* Stefan Bratanov

* Caspar Schwartz-Schilling
