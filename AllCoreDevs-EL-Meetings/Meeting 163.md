# Execution Layer Meeting #163
### Meeting Date/Time: June 8, 2023, 14:00-15:30 UTC
### Meeting Duration: 1 hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/786)
### [Video of the meeting](https://youtu.be/LqaR-kdnOoU)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 163.1 |**Cancun Progress:** We began the call with dankrad making the case for changing the 4844 blob target & limit from 2/4 to 3/6. To justify this, tests have been run on testnet + mainnet sending large blocks and analyzing the impact on the network
| 163.2 |**Cancun Progress:** Early in the call, we reached consensus to move forward with this change. That said, the proposition later faced some opposition from the Geth team, which had concerns about the impact of the change on network stability. There was a lot of back and forth, but the crux of the debate is around how conservative we should be when introducing blobs to the network.
| 163.3 |**4844 blob limit** Blobs are already a significant increase in gossiped data that will be introduced all at once. OTOH, providing L2 users with cheaper transaction fees is extremely important, and we can only increase blobs during hard forks, which are infrequent. After some more back and forth between @vdWijden and  @dankrad at the end of the call, we agreed to keep the 3/6 target/limit combo for the next devnet and continue discussions around whether this is the right value for mainnet!
| 163.4 |**devnet-6**  On that note, @BarnabasBusa gave an update on the state of 4844 devnets: a first version of devnet-6 was launched this week with Lodestar, Teku, Nethermind and EthereumJS. With this blob count change, and other clients being ready to join soon, we'll do a full restart next week!
| 163.5 |**devnet-6** We discussed the last open PRs around JSON RPC on the call and agreed to keep those out of scope for devnet 6, but include full RPC support in devnet 7! [Tracker](https://notes.ethereum.org/@bbusa/dencun-devnet-6)
| 163.6 |**EIP-4788 design** We discussed a proposed change to EIP-4788, which exposes the Beacon block root in the EVM. The proposal was to limit the number of block roots stored on the EL to cap state growth. This would require more disk writes from EL clients, but everyone agreed with the change!
| 163.7 |**Cancun scope planning** Cancun had EIPs 1153 (Transient Storage), 4844 (ProtoDanksharding) and 6780 (SELFDESTRUCT removal). On the last ACDE, we finalized the list of EIP candidates: EIP-1153: Transient storage opcodes, EIP-4788: Beacon block root in the EVM, EIP-4844: Shard Blob Transactions, EIP-5656: MCOPY - Memory copying instruction, EIP-6780: SELFDESTRUCT only in same transaction   
| 163.8 | **Engine API: employ one method one structure approach for V3 execution-apis#418** agreed to a proposed change to the Engine API versioning scheme, which would remove old ExecutionPayload versions and add a timestamp check to ensure V3 payloads are only sent after the next fork activates
| 163.9 | **Open questions** @tbenr had some questions about the validator specs. Specifically, he was wondering whether nodes should process all blobs on the network prior to sending attestations or not -- Not having to do so could provide some UX benefits if a CL is swapped out on a synced EL (e.g. when changing CL client). That said, this does go against the implied semantics of the spec. @dannyryan will put up a PR to clarify & we'll discuss further on the ACDC call next week.
| 163.10 | **Holesky Testnet Launch Coordination Call #0 #803** @BarnabasBusa announced a first coordination call around the launch of a new testnet: Holesky  aims to run more validators than are currently on mainnet, to allow us to stress test Beacon chain-related changes. Rough ETA for the launch is Merge Day (Sept 15) - if you're into testnets, you should show up!


## Intro
**Tim Beiko**
* Okay, we should be live. so welcome everyone to ACDE #163. have a, basically a lot of Cancun stuff on the agenda today and then some well Engine API decisions also probably follow, within that. And then if we have time we can even talk about the validator spec. so I guess, to start off, is Dankard here? Yes, Dankard is just joining amazingly. okay. So I guess thinking us off, Dankard you wanted to propose a change to the blob limit, for EIP-4844. Do you want to take a minute to walk us through? well, you know obviously why you wanna do that but mostly sort of the tests you've been doing, that you think justified the change? 

## 4844 blob limit [4:14](https://youtu.be/LqaR-kdnOoU?t=254)
**Dankrad Feist**
* Yeah, so I mean, I'm not gonna repeat everything because I represent, I presented that already on last week. So if you want to have the extended version, then I recommend listening to that recording. so the summary is, we ran some tests on main net where we, created blocks, of large sizes. So we, we simulated a sustained load, and that we, we tried that between 128 kilobytes and one megabyte. and so we did, 26 kilobytes for 512 and 768 kilobytes, in between. And, so in all those tests, the network looked stable. 
* Like we didn't see like, lots of validators going offline or anything like that, or like at the stations being massively delayed. So none of these happened. what did happen on one of the one megabyte tests, is that one of the blocks got, reorged, so that block was late, was after the four second deadline just passed like by just hundreds of milliseconds, so very close. And so, majority of validators in the test with. And so the next, proposal reorged it, didn't happen on any of the other tests. 
* And, as a comment, like even under normal conditions, we sometimes see, blob up to like 3.5 seconds into the spot sometimes. And, so like we probably did cause this, but probably, not by delaying the blob by four seconds, but probably our delay was only added up to like a proposal that was already pretty slow. so I would attribute that to the very aggressive four second deadline and reorging rather than to our tests like nothing else went wrong other than that block being laid and so my recommendation based on these tests is that, we should consider raising the, the limits to six blocks rather than, four and, the target to three, because, yeah, we don't see any problems, with these loads 768 kilo kilobytes. 
* Yeah, please have a look at the data and see, if you can agree with that. also as a comment from last week, I think, so the, the tests were sustained loads, so we created 10 blocks in a row with these capacities, so we didn't just send a single block. yeah. Got It. yep. 
* And maybe final comment, if anyone has looked at these tests and finds something that they would really like to see, we are, we still have all the infrastructure up to do these tests. so ideally if there are any more tests we should do I don't think we need more, but if anyone thinks we do, then we should do this soon because it costs a lot to run these notes and we probably want to sunset them in the next few days otherwise. 

**Tim Beiko**
* Awesome, thanks. anyone have comments or thoughts on this? And I guess, oh yeah, please. Yeah, go ahead. 

**Stokes**
* Oh, I was just gonna say, it seems pretty reasonable. maybe it's worth doing the experiment one more time, although they're kind of expensive, but if no one has any reason not to, then yeah, I think consider Any specific experience. 

**Dankrad Feist**
* You mean seven and 68 kilobytes because that's what we are attempting, or what would you like to see? We did two of these, by the way, two at 768 kilobytes and 281 megabytes of sustained 10 block, right? 

**Stokes**
* Yeah. Maybe we're more just at like the, yeah, the numbers going again, just try different day, different network conditions, see what happens. 

**Mikhail Kalinin**
* You wanted to suggest to increase these, numbers right from the beginning or after, I don't know, a month of evaluation on the mainnet.

**Dankrad Feist**
* I would suggest doing it from the beginning, like changing it each time is, at least according to the current setup is the hard fork. So that's a lot of coordination and takes a lot of our time here. so I think it's reasonable to just do this from the beginning and like we are doing the blocks, which should actually, be a lot more gentle than the experiments I've done. if what we're claiming on stimulating is true, so I would suggest doing this from the beginning. 

**Tim Beiko**
* Does anyone think we shouldn't do this? Or as has issues with this? Gary has a question about like, yeah, what's the max, we've pushed the network, did we reach 1.52 megabyte blocks?

**Dankrad Feist**
* So it's hard to create sustained blobs of that size, because you just are not gonna get all your transactions in and you're competing with other people who want to, put in transactions. So one, one megabyte was okay, although, even there we didn't, all get into all the blocks that we wanted to. we did, in that process create some blocks that were significantly larger. I think largest was 1.7 megabyte. but yeah, I'm, I, first, I don't, I don't think we will see instability. I don't have any indication on mainnet that it does work, create instability. and second, I, yeah, I can, it's, it is difficult. I don't think we are gonna learn that much because we're gonna see very erratic loads in practice 

**Tim Beiko**
* Okay.I guess, does anyone disagree with this change? Oh, Ansgar,

**Ansgar Dietrichs**
* Well, I don't disagree per se, and, and I don't think this is a high chance, but I wanted to least very briefly also do temperature check around pushing the two all the way to four eight. so like up to one megabytes maximum assume most people would be, would be uncomfortable with that or because, we do have the, block decoupling chunking to give us some extra robustness. so  I don't know, I would still think it's worth considering, but if people of course feel uncomfortable, we might like 326 also we got compromise. 

**Tim Beiko**
* I think, Dapplion has a question around what's the added disc requirements going from, you know, two to three to four targets, Right. 

**Dankrad Feist**
* I don't know the numbers out of my head, but I mean it's an easy computation in this case, right? Yeah. One block this 128 kilobytes over the Retention period. 

**Tim Beiko**
* Yep. okay, so, okay, so Ben is saying two per slot is 33 gigabytes over 18 days. so three would be like around 50 ish and four would be 66 I guess and then, you know, up to potentially, well, yeah, I guess that's the average results you're gonna get, but probably a bit more even, you can go past the target, I guess. Yeah. Any I have A question. 

**Stokes**
* Yes. Is it too late to do 236 on DevNet? Six? I mean, basically I think we should just roll this out as soon as possible and see what happens. 

**Tim Beiko**
* Yes. I think if we decide this, we should decide it, you know, if not now, then on the call Monday so that it's, it's part of devnet six. Yeah. 

**Stokes**
* It seems like its worth doing. Cause Sorry, go ahead. No, go ahead. 

**Barnabas Busa**
* So we started off at devnet six yesterday and we had made some progress on it, but there's still quite some, that have not joined yet. So this is more of a pre devnet six launch. We gonna be relaunching it with most clients, hopefully in the coming week. So if we want to make some kinda modification though, it's entirely feasible. 

**Tim Beiko**
* Okay, so there's a question as well as like, testing this in the transaction pool. so basically, yeah, are there any issues potentially before the block building funnel? I don't know if there's any thoughts on that or if that's something we can maybe try on DevNet six, 

**Stokes**
* If not Most, is kind of an north talking question, right? Yeah. But separately, yeah, we should probably expand then post and make sure nothing falls over. 

**Tim Beiko**
* Yeah. Okay. So I think we can probably move forward to have this at least on DevNet six, and test it out there. We can also do tests  for the main pool. and then, yeah, once we have that running, we can reevaluate if we want to, keep it like that, potentially move it to 48 or even lower it back down to 24. but yeah. Any objections to oh, moving it to three six for Six, Ansgar. 

**Ansgar Dietrichs**
* Yeah, I was just gonna say, as long as there's any chance quiet, I would rather have it started quite, and we can always lower it back down because I think we get just better insights, right? Because there's nothing that would be a problem with three six that won't show up with four eight, but the other way around it might. So if we, at least if we want to consider it at all for four, for four, I think it would be better to start with the larger limit. 

**Tim Beiko**
* Does anyone think we should consider four eight aside apart that Ansgar? 

**Stokes**
* How much data do we have from the experiments non granted? at four eight? 

**Dankrad Feist**
* Yeah, we have, we have two series of that. as I said, nothing major happened to the network, it's just that one of the blocks was delayed. So one, once, once block was offered. 

**Stokes**
* Right? Okay. I feel like I heard chatter about DevNet seven, so we could do three six and then that looks good. Bump it up. We could also go the other way. 

**Tim Beiko**
* Yeah, I think I'd also go that route. there's a question by Lucas, around increasing the attestation time, which yes, seems like a whole different can of worms. 

**Dankrad Feist**
* I don't know if anyone, I Think that would be a topic for ACD, but I, yes, I think that's a good idea. Yeah. 

**Tim Beiko**
* Okay. So we can discuss that next week, or Danny, I see coming off back of mute, I was Having technical difficulties right when was suggesting four eight, so I kind of missed that. 

**Danny**
* My gut was that we didn't have data indicating that that was a good idea and that on test nets we're not going to get that data because it doesn't look like main net. so I'm, is there an argument that I missed? I apologize. 

**Ansgar Dietrichs**
* Argument was just that we do, we will do the block de coupling so we get some extra and,  and chunking. So we'll get some extra robustness, with that. And even without that extra robustness, we already only had very minor issues, at that size. 
* So it seems whether it's considering for mainnet and if we want to at least consider it, it seems better to start the test net on the upper side to see any potential issues come up there. And then we can always lower it for later tested rather than the other way around.But if the strong offense is three six, then I think it's also fine to do that instead. 

**Danny**
* Yeah, I guess I'm not sure that I would detest that data and then be convinced that we're good on main that cuz it's just extremely different technology. but we can take the step towards three six and keep talking. 

**Tim Beiko**
* Yeah, okay. Yeah. Okay.I think three six probably makes sense, to start. So, let's do that. Ansgar says he can open the PR for it. So on the EL side, so if someone can do the corresponding PR on the CL specs, we can move the count to three six and have this part of DevNet six. Does that make sense everyone? 

**Danny**
* And when is DevNet six just so I can time, if we are doing this release like ASAP or if I can do this release the end of the next week? 

**Tim Beiko**
* So devnet six already had started but will be relaunched next week. 

**Danny**
* Okay, so this is a get this out tomorrow with desktop factors and things, rather than wait till the couple of other things we're working on. Thank you. 

**Tim Beiko**
* Yes, that's and yeah, I guess next thing on the agenda was DevNet six, Barnabas, I know you've been tracking down all the PRS, this week. do you wanna give a quick update on, where we are both from a spec perspective and like you mentioned, earlier, basically the first release or, or live test of the devnet six? 

## devnet-6 [20:07](https://youtu.be/LqaR-kdnOoU?t=1207)
**Barnabas Busa**
* Sure. So basically our consensus spec has been, released and we have all agreed, we're going to do, if we are going to change this, to three and six, I think this will require another release maybe, I dunno if there's any changes in the consensus spec for that. And then for execution EIP, we also have, most of the, or all the PRs, merged and for engine API there's one more open, 628. 
* And other than that everything has is merged. we currently have , the devnet six running with Loadstar and Teku on the CL side and we have  Nethermind, and Besu is not working just yet, but they're already part of it and is also not working just yet, but they are also part of it. So hoping to the lighthouse also by the end of today, without any validator just to see if, they can join the network and sync it up. And then hopefully next week we're gonna be able to onboard a few more client themes with the relaunch. 

**Tim Beiko**
* Nice. and I guess, okay, so you mentioned this, execution API PR, this is about adding fields to the receipts for transactions. So I'm curious, the block is the blocker there? Yeah, I, or I guess what is the blocker there to get this merge? I see Lightclient in Roberto, we're going back and forth on it, but and this is, 

**Barnabas Busa**
* I'd be curious about the opinion of, the depths on this one. 

**Gajinder**
* So I think on this, PR for execution, APIs add data, gas user and data, gas price, that's what we are running off, right? 
* Yeah. So this PR is, I mean it's not contentious and it was sort of mostly available and Roberto asked to include an extra field. So this basically include these fields in the RPC, and basically does not affect DevNet or the consensus, right? But also I think, I mean it's non-contentious so we can just approve it. There are some edits regarding some typos. I think we can just include them and try to merge this PR. 

**Tim Beiko**
* And I see there's a comment by lightclient around, there's more RPC changes for cancuns, so we wanted to merge all of them together. Is that still the case? Oh, I don't know if you have a mic 

**Lightclient**
* Hey, yeah, I think this is like, this is mostly it. I'm not sure how we need, if there needs to be changes for the RPC to submit blob transactions and we, I don't know, I'm not sure if there's anything else that needs to be changed. probably something for like the actual transaction objects to note to their blob transactions as well. 

**Tim Beiko**
* Okay. So are you saying that even if we merge this, there's some other change that will need to be done in order to expose the blob transactions via JSON RPC? Is that right? Or to Right. 

**Lightclient**
* We add that we have the blob transactions defined. Okay. Or, like eth get block. I see. And we don't have them defined, I mean we kind of accept them for sendage transaction because we just get R L P. So I'm not sure if that anything needs should be done if I want to submit a log transaction to the transaction pool. But I think that there are still some things around like the actual transaction object that needs to be specified. 

**Tim Beiko**
* Got it. So in that case, does it, I don't Really think this is blocking the definite though. Yeah. Right. So does it make sense to like whether or not we merged this have as like a target get for definite seven, the one after this to have full JSON RPC support for broad transactions? 
* I have one thumbs up, two thumbs up. Okay.So let's, I mean, you know, we can or cannot merge this, but I think, yeah, let's not have the full RPC support and scope for DevNet six and let's try to target that for DevNet seven. 

**Barnabas*
* I have one more, thing to mention that we would like every client to include a trusted stop file flag in their implementation where we could possibly override the override of, txt or G file for, for debit. This should happen. yes. Okay. This, this should happen during, runtime and not during compilation time. Okay. Any client have a problem or objection with that? The top of the Oh,

## Cancun scope planning [27:06](https://youtu.be/LqaR-kdnOoU?t=1626)
**Tim Beiko**
* Okay. See the, yeah, the section. Okay, nice. Okay, anything else on DevNet-6?. Okay, perfect. And yeah, so we have a call, Monday as well about 48488 so we can discuss, any specifics with the client implementations and whatnot. there. okay. So next up, the rest of Cancun. 
* Alex, you had a question around the spec for 4788. so you can do this first and I think after that it probably makes sense to hear from clients one last time about, whether there's anything else we want to include alongside the currently included EIPs so that, we can start, basically finalizing the scope of implementation for Cancun.  but yeah, Alex, do you wanna talk about, the issues around, 4788? 

**Stokes**
* Sure. So EIP  4788, this is essentially a cross layer EIP so what it's doing is taking the parent beacon block route from the CL and the CL sent that over with each execution payload, the execution layer, then basically writes that into the execution state in a place that everyone can look up. And so now we have access to this inside the EVM, which is really good for a lot of different applications. 
* Yeah, so the question here is what exactly does this look like? the way the EIP is written now is there's a beacon pile that kind of exposes this part of the state. And the question then is like, what is the interface to the, to this pre-con pile essentially? we've had a little back and forth about this and we talked about this some on the, the alcohol last week, but essentially where things have gotten to now is that, it's written by the root and then basically what's behind the root is, the timestamp, from the header. So the idea is like if I want to use this thing, I can call the precon pile with the root, and if the root was valid, I'll get back to the timestamp.
* I can then use the timestamp if I want any VM to like prove the slot and do all sorts of things from there. the thing is the way this works, is that there's no easy way now to limit how many rights there are before it was written by say the, the timestamp and the header. So you could do like some ring buffer thing based on time. it's what that means is written. Now the EIP has like undo big growth and did the calculation is something like 80 megabytes per year assuming to block every slot. 
* So you know, it's not nothing. and generally it'd be good just to like bound this where we could. So the question then is how do we do that? A really natural way is just to flip how this thing is indexed. So rather than do, you know, the key is the route and the values, the timestamp is you just flip it and then have some like, you know, say modular some period of time for the timestamp and then that thing is founded. So this works. The one thing that's a little weird is that if we really want to like stick to this in variant that the EL does not know any CL information, then what the EL gets is every 12 seconds, every seconds per slot, you just get another route. 
* And then, you know, the thing you would naturally do is just write every last second or every second since you last wrote, you would write the route again. And what this means is that basically there's like 12 rights of which 11 will like never be used. 

**Danny**
* 11 in the move be zeros, right? Because it doesn't know that they're what happened in the middle. 

**Stokes**
* Well you do because nothing changed. 

**Danny**
* Well that's the Design decision I suppose. It doesn't. 

**Stokes**
* Well but this, yeah. And so here's the other thing is that like anyone reading this will just probably optimize it and be like, hey, like there's only one right every 12 seconds. That's just what I'm going to do. you could, well, okay, actually Danny, the reason you wouldn't do that is cause you won't call her to probably be able to like give any timestamp. 
* So the idea is like for this timestamp kind of which slot are you in and here's the route. 

**Danny**
* Well you could also argue that callers know when blocks happen and you can just call. So yeah. Yeah, I mean the semantics are a bit weird. If you have something that you can call on like module 11, but I don't see something, I don't see anything wrong with those semantics. 

**Stokes**
* Yeah. So yeah, any questions? it would be best to bound the state growth. So then yeah, I guess we just go ahead and make the swap and then that's that from there I'd really like to all agree on trickiness in Cancun. 

**Tim Beiko**
* Okay. And yeah, just to separate those two things. So first any objections of just bounding the size of growth, given the depth of history that we want. 

**Danny**
* And given that we'd have the 12 x multiplier on timestamp, is there, what's the size of the ring buffer? 

**Stokes**
* Well, we could still target about a day. So that's what I was thinking just to mirror the period on the CL cuz we have a similar construction there, and we can figure it out. So that's the same amount of data basically That's like 230 megabytes. Hmm. 

**Danny**
* Oh no, that's not, I mean bounded two 30 megabytes is better than unbounded 80 megabytes a year in my opinion. Not that Better. 

**Stokes**
* It's still, , yeah, I don't know. Hi. 

**Danny**
* Yeah, and that number is, I'm doing 225 megabytes

**Stokes**
* Okay. Yeah. let's see. I mean we can make the window shorter. 

**Danny**
* So anyways, it's 30, it's two 30 kilobytes. I apologize. That's much better. I, yeah, yeah, that's fun. 

**Stokes**
* Either way the numbers can be tuned. So it's like a small bounded amount of space and like I've talked to different sticking pools, they're okay with any of these different designs in terms of and like, as long as it's not like you have to get your transaction in the same block that the route is. 

**Tim Beiko**
* You know, I think they're, they're okay with, you know, some amount of look, look behind And I think it's probably much easier to start it off bounded even if we eventually wanted it to grow unbounded for whatever reason. But if we do the other way around, we will never be able to bound it because someone will be relying on the first beacon route that was ever posted for something. 

**Stokes**
* Yeah, yeah, exactly. 

**Tim Beiko**
* So just not have, yeah, like whether it's a day, whether it's like an hour, whether it's a week, I think that will lead to like different design and like applications and we should probably nudge towards that. yeah, Yeah. 

**Danny**
* I'm like, I don't love the, like rights for every second, it doesn't really matter. I have, as I'm thinking about it now, like it is nice cuz you could upgrade the slot time and the execution layer would never have to know which is a nice property. so maybe that that makes it worth it and of itself. but I'm pretty fine with this. 

**Tim Beiko**
* If dubs are Any objections, I guess anyone think we should not do this? Okay. 

**Marius**
* I also don't like the, the extra rides. Oh, I think we should like the, the caller knows the timestamp so they should just give it to us. 

**Danny**
* Yeah, but if you don't know seconds per slot on the execution there, I think you do need to sweep the interim. 

**Stokes**
* Right. But you could just say the timestamp and the header is the value and then like you're suggesting the rest of 'em are just zeros and then it's same thing. 

**Danny**
* Yeah, yeah. I mean you either need to do that with a, with a map or with a ring buffer. If you do with the map you have the unbounded growth and you do the ring buffer, you have to write either zeros or the route to the interim times slot time seconds. 

**Danno Ferrin**
* Daniel, not objection to the the idea but just some design questions. Why put the pre-compile at the high  and nod at the next pre-compiled position? 

**Stokes**
* It can go wherever. 

**Danny**
* So the pre-com compile and the state for the pre compile are, are in separate places right here, right? Like the pre compile is actually in below the list slots at least Last time. 

**Stokes**
* It's not right now, but it could be. Oh, okay. yeah, like it's, I think it's a little weird to have them be separate, right? Because you could still call the state separately. So I think it makes sense to have the pre compile be like an interface around the state at that address from there. 
* I just copied this from EIP  I forget, but essentially there was an earlier EIP that suggested moving block hashes from the execution layer, to like a similar method where you'd have them in the state. And I think the idea is just this is a state of pre-compile so like toss it they at the top of the address space rather than at the bottom. 

**Danno Ferrin**
* But, But from an implementation it doesn't care. It calls it and gets a value and now we have to check two separate ranges for pre-compiles. So from implementation would be easier just to group them together. And I don't think that the, the stateful distinction is terribly useful to an implementation cuz it's gonna be going to some method that's gonna do something completely unrelated to EVM operation execution. 

**Stokes**
* Yep. Sure. 

**Danny**
* Yeah. My gut is to not have it in the high ranges if this is a stateful pre-compiled, just accept that we have stateful pre compiles and put them with the rest is been my intuition. 

**Marius**
* Yeah, totally. especially because we have, already like tests for it and all the, all the pre- compiles have have one way at least like the first 1024 and we also have those set, on basically every test net. And so yeah, there's a bunch of things that can go wrong if the precompile doesn't have any money. So just having them in the normal pre-compile range can make sure that they have, they're always funded. 

**Stokes**
* Yep. That's easy to do and I can definitely do that Okay. 

**Tim Beiko**
* Any other comments or thoughts? Okay. so I guess, yeah, last thing for Cancun, I'd be curious to hear from client teams, Of like the EIP we've been discussing in the past few weeks. is there anything that folks think should go, in Cancun? So, I can post the link in the agenda or in the chat, sorry, right here. but basically, we have already 1153, 4844 and 6780, so the transcation storage blob transactions and self-destruct removal. and then we had a bunch of CFID EIPs, so, 2735, the BLS pre-compiled 4788, which we just talked about. and then a couple, opcos, so m copy pay and then the revamped call instructions, which we discussed last time. yeah, I see, is this Marek from Nethermind is also, yes. Okay. Yeah, so, some support in Nethermind for 4788. 
* Yeah, I don't know if any client team wants to just share their thoughts about yeah, what they'd like to include. If not, I mean, does anyone not want to include 4788? Okay, this is the last chance. okay, so let's include 4788 final chance if anyone has an objection. And then of the rest of the basically four other EIPs. So, BLS m-copy pay and the revamp call instructions. Is there anything else that people would like to include? 

**Andrew Ashikhmin**
* Well, Aragon would like to include, the pay op code. 

**Tim Beiko**
* Okay. So there's a comment for pay, a comment for m copy in the chat that came at the same time. okay. So may I guess, yeah, let's start with pay. Does anyone feel strongly for against the pay op code? Marius and Charles are saying they'd like to keep the scope. I, yeah, go ahead. 

**Marius**
* Yes. I feel strongly against the pay op code because, it introduces a new way how, Basically how accounts can be touched, which is always, kind of complicated. I also don't really see the point in having the, the pay op code, when we have the, call op code already. I know, yeah, I know that there are some security issues with the call op code. but yeah, it's, I don't know, it doesn't strike me as very, much needed right now. and so it's not really a priority for me, so I don't think we should rush it into a yeah. 

**Tim Beiko**
* Andrew, I don't know if you wanna make the case for the pay op code or 

**Andrew Ashikhmin**
* No, I think, well, there is no con consensus then it's okay to skip it out. 

**Tim Beiko**
* Okay. I guess the next one, so, light client, you mentioned mcopy and, Charles, I see you have your hand up, I assume it's about this as well. Do you wanna either of you want to do a quick pitch for m copy? 

**Charles C**
* Yeah, I wanted to talk about mcopy and pay. I, well let me address pay first. I think it's, pretty important to first of all, I work on Viper. I think it's pretty important to or get into the EVM I understand that there's concerns about, you know, implementation complexity, but it is important to be able to have a way to transfer Ether without transferring you know execution context. there's a lot really, like, I don't know I have to go through the list, but you know, I think like 30 to 50% of, you know, these high profile hacks are related to actually transferring Ether.and people are always switching instead of eth. And we have a lot of, you know, words in the EVM that are kind of like a result of having to, you know, deal with this gas stipend for a call. People are always trying to like, figure out how to transfer either. And then you have to do these, either explicitly check for reentry C or, you know, will try with a limited gas stipend in order to prevent, you know, these kinds of weird things with computation being transferred to, to not yourself. So that's, that's the case for pay. 
* I understand if it, you know, doesn't make it into this hard fork, but I think that it should be really strongly considered maybe for the next one. and then the case for m copy,is in my view pretty straightforward too. it's Pretty straightforward to implement. 
* It doesn't have too much, well, as far as I know, any interaction with the other EIPs, that are considered Cancun and it would help compile, generate like much better code really. So improving on code size and gas and if anybody's interested, I can, you know, kind of prototype to, some things to see really how much better, code size would be and gas with mcopy as opposed to the current state of things where we have to, you know, issue, you know, a bunch, a lot of and EIPs, which is in my opinion, kind of wasteful, especially when we have call data copy and code copy. And the semantics of it are pretty clear to everybody too, I think. So yeah I think that's the case. 

**Tim Beiko**
* Got it. Thanks. Andrew? 

**Andrew Ashikhmin**
* Yeah, I have a question about, pay op code versus the, proposed code two op code. Does, code two also suffer from the re problem that, Besu? 

**Charles C**
* As far as I know, call two doesn't really change anything except, gas observability and it removes the output buffer. So yes, it still transfers execution context, the colleague, which is the fundamental problem with transferring Ether using any call up code. 

**Andrew Ashikhmin**
* Understood. 

**Tim Beiko**
* Okay. 

**Charles C**
* Somebody asked in the chat. Yeah, if there's the transfer property of self desconstruct, self destruct transfers, all Ether, pay allows you to send some amount of Ether and it's also a lot less wasteful in terms of gas and I suppose touching state because you don't have to create an destroyed contract. 

**Tim Beiko**
* Okay. So, I think, yeah, given like, the points Marius raised, it probably makes sense to not include pay for now. and I know, yeah,I guess I'm curious to hear on the mcopy side, from client teams, yet seems to have internal disagreement about whether to include it. Nethermind seems to be leaning towards not including more in the fork. so I don't know. Yeah. Do any of the team feel strongly in favor against including mcopy? 

**Lightclient**
* I really don't see the argument for not including mcopy. It's extremely simple and it makes the functionality we already have with the identity contract. Is it a game changing feature for Ethereum? It's not, but it's a relatively simple thing. And if we once have any chance of doing a lot of the changes that we're trying to do in the future, then we need to be able to like do more that just like need one thing that we wanna do in the fork. And so I don't think mcopy is a adding that much to the service area. 

**Tim Beiko**
* And I think There's a couple comments in the chat about, so Besu has a PR for mcopy, but then maybe, yeah, maybe, it makes more sense to be bundled with EOF and then Marus is asking if anyone looked at memory expansion attack with mcopy. Charles, I don't know if you have an answer to this. 

**Marius**
* It's not, it's not. And we had, I think we had, issues with the identity pre-compile. 

**Lightclient**
* That's, that's what I'm saying. These are like separate things then. Like if we have a problem with the identity pre compiled, then we need to sort that out. 

**Charles C**
* No, I think the issues, one of the issues with the identity pre- compile having to do with having to, you know, transfer execution context to the identity of pre-compile and transferring call frames and stuff. so I think in copy is actually simpler than the identity copy here. 

**Danno Ferrin**
* This yeah, it's definitely a simpler, The memory expansion attacks on mcopy is the same surface as mstore and mstore eight. It's all about where the highest bit of the right ends in the copy. So it doesn't truly open up any new novel surfaces is just the same well trodden surfaces from my perspective. 

**Charles C**
* Yeah, exactly. And also called it a mcopy and code copy, have the same surface for rights. maybe not reads, but for reads, the surface is the same as mload and and identity copy, sorry, the end of any file and because it's priced the same as other, copy operations still. 

**Marius**
* Yeah,that's basically what I was asking. If someone has already looked at it and you guys seem very confident that it's not an issue, There is a, there is a cost, which is memory expansion cost, right? 

**Tomasz**
* But there is no quad cost on the length of copied in the proposed solution. So if you, if you copy a lot of words, then you have just linear increase of the cost, which opens potentially attack if you cannot load to memory just that particular copy, even if you copy in the same place. 
* So we don't have memory expansion cost at all because you're not expanding memory, but you're actually expanding a lot to temporary memory needed for EVM, right? Or you're doing that word by word? 

**Charles C**
* No, You're not. the spec is written. It says okay, that, memory expansion works as if you copied to a temporary buffer. But all real memory copy implementations, just, branch to see if that there's overlap and if the overlap is a certain way,then it copies backwards instead of forward. So there's no actual temporary buffer happening. 

**Tomasz**
* Okay. Yeah. So the paragraph first, practically doing word by word copy. Okay, thanks. Sorry. 

**Charles C**
* No, it's a reasonable concern I Guess. 

**Tim Beiko**
* Yeah, I maybe, so on Geth, and Besu seem somewhat split on this too much. you said that you'd rather not have new things in okay. You're neutral now. I don't know Argon .

**Danno Ferrin**
* So It can wait for EOF if there's not, if there's a fairly laid ad and with the, with the pushback, I just don't think it's worth pushing it through. 

**Tim Beiko**
* Okay. I guess, does anyone still strongly feel we should include it? And maybe one option is, if the concern is mostly around the scope of the fork, does it make sense to leave that as like the one CFI thing, implement everything else and see, you know, how we're feeling in a couple weeks, in terms of implementation or if we wanted to do this, should we make the decision now so that we can start setting up, both testing and like implementations to support the entire scope? 

**Danno Ferrin**
* We only test, but I think the block pre-compiles are more important than these tests. So it need to be prioritized in order from the testing team. 

**Tim Beiko**
* You mean the beacon root pre- compiles? 

**Danno Ferrin**
* Yeah, the beacon root pre-compiles, yeah. 

**Tim Beiko**
* Yeah, Oh, okay. So that, I think people are like at best neutral around, the EIP for the fork. and I guess two options is one, we just push it back to the next fork. And another option is maybe we, leave it as the only CFI things and we see how implementation goes with everything else and whatever we want to add it in a few weeks. 

**Lightclient**
* Yeah, I feel like if we can't do in copy in this work, then we have no chance of doing EOF ever. Like the surface of EOF is quite a bit bigger, I think, than what we're facing right now in terms of using things. So I would prefer that we try to do mcopy now and try just to understand like, is the surface too big? 
* Like we can always remove it later on if we're like, look, this is just people feel uncomfortable with this testing surface. Cause that's been the biggest thing that I've heard so far, is that the test, the increase its testing surface makes people uncomfortable. And I would rather go down the path and figure out what happens in a couple months if we try and implement it, put it in the forks, do the test, and if people still feel that way in a couple months, and then if they do, then we just remove it. 

**Tim Beiko**
* But if we don't do it, then we're never going to. Tomasz do you still have your hand up for the previous time or do you wanna add as you have? 

**Tomasz**
* No Lower my answer. I, I wrote in the, in the chat that, I agree with the reasoning of light client that this seems to be, simple reasonable change in line with many of ours, like moving away from pre-compile, going towards COF. 
* So for that reason at perfectly makes sense as an mcopy. And the only reason why I was saying potentially no is if the teams feel like we don't want to add more things to test, more things to, to cross test. so it's more of a scope of the fork question rather than the EIP itself. 

**Lightclient**
* Right. Yeah, I mean, I totally get that and I am the same boat around these things, but I think that we need to test ourselves a little bit if we're still thinking about having EOF on the roadmap. Because if we can't, like, again, like this, I don't think we're gonna be able to do EOF the surface area for EOF is quite a bit larger in the EVM than what we're facing right now. 
* And to me it's like if we go down this path and we think the surface area was too big, we had to take out in mcopy the last minute, that's a pretty good sign that we're probably not going to be able to do EOF and maybe we should like just make that decision, 

**Tim Beiko**
* I guess. Yeah, so, based on Lucas's comment, I'd be curious to hear, just like from the testing teams, I don't know Mario, if you're on, and yeah. Do you, , I see. Okay. Mario Vega, like, yeah. Do you think mcopy significantly like slows down testing efforts or is it reasonably simple to write test for? 

**Mario Vega**
* I think we can definitely paralyze at the moment. the problem might be that we also have, high testing for example, for 4484, so that might, so if anyone wants to jump in to test and mcopy, the state tests, I mean, it's definitely welcome too. 
* So I don't see there's, I mean, Marius had some comments that the scope might be too broad, but I don't think I totally agree. in my opinion it should be doable. but yeah, any, and if anyone wants to jump into to implement those tests, those, the state tests for mcopy, that would be very nice. 

**Tim Beiko**
* And the state tests are the one using the new Python execution test, right? 

**Mario Vega**
* Exactly,. So we, let to do is we have to implement the state test for, 47 8 8. And we already have, test for 4844 and we have to translate the 1153 tests, the Python. So that's the, the remaining to do in, in terms of.In terms of status for execution layer? I think we can do and mcopy, but yeah, if anyone wants jump in also to help with this, that's obviously gonna help a lot. 

**Charles C**
* Sean, I think Paul from the Epsilon team was, designing, the tests and we're starting to write them up, but I, just pinged him to see, what the progress of that is. 

**Tim Beiko**
* Okay. So I guess Based on all of this, does it make sense to add mcopy in and then in the next call or the one after, if we see that like, you know, testing is like bottlenecked by it and or client implementations feel like it's, I don't know too much to add, we can always remove it. So like we can prioritize basically implementing, 4788 and all the other, EIP that are already included add this one as well. And then you know,if it is a relatively small change, we keep it in, but if we find some, yeah, significant cause of delay, then we should consider pulling it out. And also by doing that close the door to anything else being included in Cancun. 

**Mario Vega**
* Yeah, sounds good to me. I mean, we can give it right, just to see how yeah. How much of a remaining test test we have to implement and then we can give an update in, two weeks and see if it's, it was too much in there. Yeah, we can still remove Sounds good. 

**Tim Beiko**
* Any objections or final thoughts? Okay. So, we will add mcopy in, alongside 4788. If in a couple weeks we feel like mcopy is like significantly slowing down things either from an implementation or testing perspective, we'll just kick it out. and we also will not add anything else, to the fork. 
* So this means the fork will effectively have, 1153, 4844, 6780. so the transit storage block transactions, self, the truck removal. And then today we've added 4788, the beacon block route, and then mcopy. And then the three other things that were CFID, are just not included in this fork. yeah. Does that make sense to people? okay. 
* What else do we have on the agenda? okay, next up, yeah, Mikhail you had this change to the engine API we discussed, I don't know if it was last week or three weeks ago on ACDC about, having a single structure, a single method, sorry, for the V3 engine API calls. You wanna give some context on that? 

## Engine API: employ one method one structure approach for V3 execution-apis#418 [1:02:15](https://youtu.be/LqaR-kdnOoU?t=3735)
**Mikhail** 
* Yeah, thanks real quick, update from that. So we decided to move with, one method of one structure approach since week three since Cancun. So this is the PRs, it has a couple of allegations that the clients has to do. please everyone take a look. Any objections to how they inspect out, surprise them as, I'm target aiming to merge this early next week. 
* And after this gets merged, we can outline the engine APIs back for Cancun, which I guess will include a couple of, probably a couple of other things. One of them is deprecation of exchange transition configuration that people were waiting for, but one time, another is probably, the, builder override flag, which were, discussion. so that's it. So please take a look at this PR those who are interested. Lucas? 

**Lukasz**
* Yeah, I have a question. Would it be reasonable to, I know it'll be a breaking change to also apply to v2, to like, not allow V wonder? I know it's a breaking change, but it shouldn't break anything. We already passed the fourth, everyone is using v2, so question here. 

**Mikhail** 
* Yeah, I wouldn't, by default I would not change this bag that is, literature is finalized. So, the main goal for this change is, that it prevents us from, agrow and complexity of support in all versions that we had before. and I think that for we too, we can, remain it. We can just leave it as easy. 

**Lukasz**
* Okay. It'll slightly simplify our code base because we had this generic, way of doing that and now we will be specific, but, yeah, it's fine. And I think Nethermind already has this implemented as your proposal right now, so yeah, that's how we have it. 

**Tim Beiko**
* Cool. Any other thoughts, comments? Okay. okay, so, and then last thing we had on the agenda, this is more of a CL thing, but, basically Dan wanted to chat about, honest validator behavior for data availability, and duty production. do you wanna give some quick context there, Rico? 

**Enrico**
* Yeah, sure. so I was bringing this up, because I have this, I remembered this conversation, around with probably discord with any other guys, and the implication of that could have some engineering implication, which do, do one way or the other. 
* But point is that should we, start, validating a testing and producing blocks, before we actually have downloaded, all the blobs up to the, very end of the availability, window. Or we could start, doing duties once we reach the head and downloaded everything. Because from the spec, at least, things I remember before we could, consider everything valid only until, we have the entire, data downloaded and valid. You may write here. 

**Danny**
* Yeah. So based on past conversations and based on how the spec is written right now, you would be short circuiting, short circuiting the validity condition, if you started a testing before, and is not the intended behavior. 
* So I believe that that's how the honest behavior would read based off of the is date available function. but if that's not clear, I think we should, Right? 

**Enrico**
* So actually, so the, the UEX will be, slightly, affected here. if you have, if you want for instance, switch, CL and you just, just remain with the same EL it is already in sync, then you wipe out of the base, which means that you can check point sync quickly, reach the ahead, and then wait the full bit to be downloaded and the client should start behaving like, we should download all the as quick as possible while it's not just, an historical sync that currently is, is kind of low priority download, but now we should start changing internally, how the client behaves there because we want to reach the availability, boundary as quick as possible, Right? 

**Danny**
* So I mean, you could imagine some like local UX affordance where you could just dump that data and, and import it directly if there was actually like a, if this UX you thought was like really high priority. but I do think that if we don't do that DA check and kind of just when you're initially syncing, then we kind of like begin to break the, the honest behavior, not radically so, but, we're putting a chip in it in a way that I think could not prove. 

**Enrico**
* Right. Okay. So it's an item that we actually have to work on because Yeah. 

**Danny**
* What's the amount of data on the current window? 

**Enrico**
* Gigabytes don't have the number at the moment, but, we'll, it's, yeah, 23 gigabytes, I don't know. It's calculated on four blobs. 

**Danny**
* Yeah. Is that 36 or 24? 24

**Enrico**
* So yeah, will take some time and yeah, it's kind of, yeah, could be filled felt by, by the users for sure. 

**Mikhail**
* How, yeah, I mean, if people wanna think about the, For this data I was just wondering how much time it'll take for this data because there is the EL client, which is syncing as well. so it probably won't be, terribly Yeah, yeah. 

**Enrico**
* I'm focusing particularly if you already have an EL that is up and running, if you, if you have to sync both of them, definitely there, you still have to sync, the EL 2, probably they will, the EL will take more time, but there will be contentions on the bandwidth for sure. So yeah, everything will be, is lower. 

**Tim Beiko**
* Okay. I'm not a hundred percent sure what the right next step is here, Yeah, let's pick it up on like, cause this is our call. 

**Danny**
* Yeah, if there's, you know, this is a UX that we care about, then there might be some like, standards around dumping and porting data and stuff. but I'm happy to pick it up there when we have more people with context. 

**Enrico**
* Well, the, the action point here is maybe make things definitely, clearer in, in the validator honest validator. Just drop a line, let's says clearly. Okay. 

**Danny**
* Honest is, at least for my understanding, maybe other, Yeah, I can put up a PR to that. Just, I think it's implicitly clearer with the, the definition of the function, but a note that just says, you know, note thus you must backfill, Yeah, I guess you consider it, consider valid until all valid blobs have been downloaded. 

**Enrico**
* What do you mean by all in this case? Could be related to the blobs that are, you're validating at the moment for the, the for for that blob by all here is intended by old blobs for, for the entire developability window. 

**Danny**
* Yeah, and I'll do a pass on it just to make sure language is clear, you know, based off of a handful of iterations that might be as you weigh out, not so clear. but I'm happy to do that. 

**Enrico**
* Yeah, thanks. 

**Tim Beiko**
* Okay. okay, so Marius wanted to talk more about the blob number. we can do that, but right before, I guess, Barnabas, you wanted to, give a shout out to the new testnet call next Thursday, so we can do that. And then if anyone who doesn't want to chat about blobs, wants to leave, they can drop off and we can use the rest of the call to go into more blob conversation. yeah. Barnabas? 

**Barnabas**
* Yes. we will have our first, Testnet call, next week on Thursday at, 1230 UTC time. And, we will like to see, client, everyone, at least one person from each client team to show up, to this. We would also like, some operators to also show up to this meeting. 

**Tim Beiko**
* Sounds good. is there a, oh, I guess on the call you're gonna decide when Genesis would happen for the network? 

**Barnabas**
* Yes, we expect it to happen on Merge day. 

**Tim Beiko**
* Okay. On, okay. So the, and, and so I assume this means for the purposes of, Dan Kun, we, we should still consider Gordy and Sapolia  as like the main test nets and you know, if like there's a world where, Dancun has already happened when this goes live, maybe not, but if this is gonna go live in September, we shouldn't count on it as like a testnet for this fork, correct? 

**Barnabas**
* Well I assume Dancun will, if if doesn't happen before September, then we can also use this testnet to test also, Right? 

**Parithosh**
* Yeah, I would actually say that we should definitely use this one cuz the idea is that this testnet, this is bigger than Gordy and bigger than me mainnet. So it would be the first opportunity for us to test like how we perform with a large number of validators. 

**Tim Beiko**
* Got it. In that case, and I unfortunately, I don't think I can make the call because it's 4:30 AM I think my time. but I would potentially push to start it one or two months before September 15th. so that we're, like if, yeah, if we're ready to fork a first testnet or second testnet, in the summer, then having, this one ready would be good. 

**Barnabas**
* We would probably need, I don't think we would have the time to be honest to launch. Got it. Okay. Multiple months before the September deadline because we would need, like proper client releases and, we would need quite some organization for this because we plan to run our values set, significantly larger. And for that we, like client teams will probably need, dedicated infrastructure, from it. So this is gonna be a significant, deployment And Got it. Require Quite some planning. So this is why it would be very good if we could have someone from short in this, call next week. Cause we're gonna discuss the details there. 

**Tim Beiko**
* Okay. Sounds good. Any, any commenting you have thoughts or comments you wanna share now? Okay. so if anyone wants to not talk about blobs more, this is your chance to drop. otherwise, Marius, you had some comments saying the Geth team felt uncomfortable with, the 36 change. 

**Marius**
* Yes. Sorry. I, I joined five minutes late, so I missed the, the discussion at the beginning of the call. well, apparently this decision was made, yes. So  I have prepared a statement. No, I have not prepared a statement but the thing is we, during these tests, we've seen that with, one megabyte blocks, we start to lose adaptations quite quickly. and what this suggests to me is, and these  blocks are possible right now, what that suggests to me is that we already have two big of a gas limit. 
* And it could already be the case that if someone would, would send these big blocks for an extended period of time, then a lot of nodes would not have enough time to add a test to them. And thus we will lose a lot of attestations. 

**Dankrad**
* Now There's no indication though that, this is like, so yes, we lose attestations, but why do we lose them? It is only due to the reason that, these blocks are late, like that they arrive past the four second, slot time, and blocks arriving very close to that already happens.
* Like, I mean, look at, look at those graphs and see that even outside our tests, you see those late blocks, not quite as late, but like very close to that. Can you see drops and at stations? 

**Marius**
* Yes. 

**Dankrad**
* So I think the argument here is not that this is too,  this is like, there's no sustained effect on the network. Like all those notes are well able to catch up with the network. They just see that particular booklet. So I think, the case is actually just that our four second deadline is too aggressive and not that this is too much load for the network. 

**Marius**
* Yeah. But we like, we have that, four second deadline for a reason. Right. 

**Dankrad**
* Well, we can change it. 

**Danny**
* I mean, I would actually suggest that Well, but we do not have, we, that's a, that's not something we do tomorrow. That's not something we have a lot dated on. 

**Dankrad**
* That's not something That, but whatever It is, like, I mean, I wanna push back against the, the claim that this is net stability of the network. Okay. But it is one particular very aggressive deadline that we have. 

**Danny**
* But So I think the strongest argument here is that when you increase the target of large data payloads, which you do with blobs, so you would regularly get that you decrease the cost to push that over a threshold with call data. 

**Marius**
* Yes, Totally. That's exactly my point. like we can do this right now and the only thing that is prohibiting us from creating these big blob is cost. And with, 4844 we make this attack way cheaper. And, we all, like, we have to all be like clear about this, like this, this is the case and we are fine with it. and I'm also fine with decreasing the cost for this attack because I don't still think this, attack is kind of, extremely costly and cannot be sustained for very long. 
* But I think in the, we just have to be clear about this. We're making this this attack more possible than it is right now. And with increased blob count, we make it even, even easier to do. And, so my suggestion, would be to start slow with, 24, which is already kind of high in most cases. And, then we can, if we see that this works, reliably on mainnet for a long time, we can, we can increase it. 

**Dankrad**
* Yeah, I think this is, Yeah, I mean I think that's, it's too conservative, like in my opinion, even three six, I mean I'm pushing for that because I, I've seen that this worked reliably, but I know that there's a lot of demand out there. There are so many teams right now building on those blobs and really wanting those, and we are already very late at delivering these. 
* Like it's, it's just like we, we are always making the most conservative decisions and like, it's like 

**Marius**
* So There's no reason, there's no reason that indicates what you're saying that is completely wrong. 

**Dankrad**
* So There's no reason, there's no reason that indicates what you're saying that is completely wrong.  Like, I would like, I I think that's ridiculous. Like we haven't seen like a late at station doesn't mean that you're pushed off the network a late at station just means that you miss a little bit of your report and, and you're still attached to the chain, you're still finalizing the chain and so on And that the block has a higher chance of being reorged. 
* Yeah, that's true. But I mean, I would suspect that in this case where this happened, because we have seen like a 1.7 megabyte blob that was included, no problems. So there's, there's a high chance that this proposal already had other problems going on. Like they probably only published there may, maybe they were actually like gaming me v and published their block two seconds late already. And in this particular instance it went wrong. So I dunno, Ansgar, you've had your hand up for a while. 

**Ansgar**
* Yeah, I would say just in terms of, process here, I think Mars' concerns are somewhat warranted, at least sounds to me like, but given that we invaded this quite a bit earlier and there was, I mean again, even some people in favor of white, I think I'd personally be in like be against walking this spec now because some people have already left the call and we can always change the spec, at some of the future calls before we actually have the fork. 
* It seems like a same default for the, for the testnet at least. And I think if this is a concern, then I think we should just in general study potential ways to address this, the potential change of the first second window. Also, I think a potential call data cost increase, a small one or Cancun might be something you would want to consider. but I think working the earlier decision back now would just not be the proper process here. 

**Tim Beiko**
* Well, I guess so on the process, but like I think, you know, we're still in the main call time and I think pretty much all the 4844 people are still here, but, the thing I'd want to avoid is like if we drop, is like doing, having clients do useless work of like implementing the change and then reverting it in two weeks. 

**Dankrad**
* I mean the changes that's changing a constant, right? 

**Tim Beiko**
* Right. So I mean if that's, if that's the case, yeah, I'd probably lean towards, we keep 36 for the devnet, but I do see Marius argument where like the devnet is not gonna tell us about the potential concerns we'd see on main net right? Then I don't think we're gonna resolve that in the next like five minutes, but we can discuss it on the call Monday potentially. 

**Marius**
* So I'm not against, having the devnet with, 26 if, we don't take this as an indication, for minute because it's, it's useless. Like it's, it's just like, it's, it's just different, for minute. 

**Dankrad**
* I mean my contact claim is if you're making this argument, you should make the argument that actually like we should limit current blobs much more than we should limit blobs. Like I find this very strange that we're making always these decisions and we are always much, much more conservative on whatever new we are introducing compared to all the existing stuff that's already like pretty doable. 

**Marius**
* Yeah, yeah. 

**Dankrad**
* Like, I'm sorry, like, I like why I mean the same force why you're not stop coming with the same force out here and saying we should limit blocks to 700 kilowatts because, then I will take you more seriously. But this one I feel like it's just, it doesn't make sense to me. 

**Marius**
* That's nice of you. If you, if you take me more seriously then, I've been saying  for a really long time that 30 million gas is, is too much and it's a lot. 

**Dankrad**
* Sure. But I mean clearly like the Ethereum like community as a whole has not considered that like to be, what's the direction they want to take. So I kinda feel like that's, that's now it seems now it's not fair argument that not, not now it seems not fair that suddenly all core dev override the ethere community on this in the case of blobs. Clearly I'm not like if This is the case then maybe we should we should add the voting to the network on blobs the same way it works on gas now and let the community decide what they're comfortable with,

**Tim Beiko**
 * But then you delay for it for, 4844 by six months. so yeah, I think like, so I clearly we're not gonna resolve this now. I do think like it's probably worth going ahead with the 26 on the DevNet. and then maybe using the call, the 4844 call on Monday to focus on specifically what we would want to see to convince ourselves that like this is safe for main net. If there's anything missing, I don't know, Marius, if you can be there on Monday or someone from Geth can be there. but yeah, I think it probably makes sense to have like a longer discussion about that there. 
 * Okay. yeah Lucas, I'm not sure how serious of a suggestion that was, but we currently  vote on the gas limit, which is basically the same thing. Right. okay. Anything else before we wrap up? Okay, well thanks everyone. so we decide, okay, we're keeping 36 for the DevNet. 
 * We'll see whether we want to make this, the main net constants and we can discuss on the 4844 call Monday, what potential issues, there are with making 26, yeah. moving 26 to maintenance. Sweet. Anything else? Okay, well thanks everyone. Talk to you all, on Monday. 

**Marius**
* Thanks. Thanks. Thanks. 

-------------------------------------
### Attendees
* Tim Beiko
* Danny Ryan
* Pooja Ranjan
* Mikhail Kalinin
* Marius
* Wesley
* Barnabas
* Saulius
* Danno
* Lightclient
* Pari
* Ethan
* Mario
* Tomasz
* Oleg 
* Kasey
* Marek
* Crypdough
* Fabio Di
* Terence
* Andrew
* Roman
* Marcin 
* Pop
* Guilaume
* Protolambda
* Carlbeek
* Mike
* Gajinder
* Stefan
* Hsiao-Wei
* Josh
* Phil Ngo
* Alexey
* Holger Drewes
* Dankrad
* Guillaume
* Proto
* Holder Drewes
* Stokes
* Peter Szilagyi
* Sean
* Micah Zoltu
* Jiri Peinlich
* Marius Van Der Wijden
* Potuz
* Evan Van Ness
* Moody
* Tynes
* Alex Beregszaszi
* Marek Moraczyński
* Justin Florentine
* Ben Edgington
* Lion Dapplion
* Mrabino1
* Barnabas Busa
* Łukasz Rozmej
* Péter Szilágyi
* Danno Ferrin
* Andrew Ashikhmin
* Hdrewes
* Crypdough.eth
* Ameziane Hamlat
* Liam Horne
* Georgios Konstantopoulos
* Mehdi Aouadi
* Bob Summerwill
* Jesse Pollak
* Stefan Bratanov
* Sara Reynolds
* Caspar Schwarz-Schilling
* Ahmad Bitar
* Marcin Sobczak
* Kasey Kirkham
* Sean Anderson
* Saulius Grigaitis
* Ruben
* George Kadianakis
* Dankrad Feist
* Andrei Maiboroda
* Gcolvin
* Ansgar Dietrichs
* Jared Wasinger
* Diego López León
* Daniel Celeda
* Trent
* Mario Vega
* Kamil Chodoła
* Ziogaschr
* Kevaundray
* Antonio Sanso
* Oleg Jakushkin
* Leo
* Nishant Das
* Pote
* Sam
* Tomasz K. Stanczak
* Matt Nelson
* Gary Schulte
* Rory Arredondo

-------------------------------------

## Next Meeting
June 22, 2023, 14:00-15:30 UTC


