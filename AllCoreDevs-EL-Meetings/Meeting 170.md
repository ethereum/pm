# Execution Layer Meeting 170
### Meeting Date/Time: September 14, 2023, 14:00-15:30 UTC
### Meeting Duration: 1:20
#### Moderator: Tim
###  [GitHub Agenda]( https://github.com/ethereum/pm/issues/857)

### [Audio Video of the Meeting](https://www.youtube.com/watch?v=aobFWu7NANc)

# Agenda

## Introduction

**Tim**
And we are live. Welcome everyone to ACD 170. So today I will cover obviously the updates on the devnets, then there's two final spec, actually two final editions that we have to discuss so the Max Epoch Churn limit and then the blob base fee opcode and then we had some questions around devnet nine and if we have time after this, the reth team has never sort of formally introduced their clients on all core dev, so we can give them some time to do this. 

## Dencun Updates

### devnet-8 updates

Yeah so I guess, to get started, does anyone want to give an update on devnet 8 and how things have been going in the past week? 

Yeah I can try. Barnabas is still on his way to the office so I think he has a better idea of what happened last week but we had a few updates, I think both to Prism and to Besu, the Nethermind team was trying out a couple of new things. I think they didn't speak a bit more about that later on. I think that's largely it. We should be finalizing, I do see some nodes are off, so I guess we'll be looking into why they are off afterwards. I think that's all on the devnet 8 side, but otherwise we've been testing a lot of MEV workflows. We have the mock builder, that's more or less up and running and we've been trying out Lighthouse as well as Lodestar on kurtosis. And if any other CLs are ready then please just DM me which image or branch and I can start trying out all the MEV workflows there.

**Tim**
Nice thanks yeah any other client team want to add more color to that? 

**Marcin**
Yeah so in on Nethermind nodes, we are running the branch with block pool implementation and as far everything looks fine so we are like we are testing it on one node for a few days and in few hours it's running on all Nethermind nodes and everything looks fine as far.

**Tim**
Nice. Any other client team want to share updates?

**Terence**
Rather than a update, I have some like quite interesting data point to briefly mention. This is very very early but we haven't got much investigation but we're seeing blobs cycle that's arrived approximately 500 milliseconds later than the blob and Lighthouse also reported they're seeing similar behavior so I'm not sure whether this is we can type this behavior particularly single cloud implementation or this is just a general P2P behavior but something definitely worth investigating moving forward because like we likely will see a fairly high reward rate if today there is additional 500 millisecond delay, given the four second cutoff but yeah that's just something to look into.

**Danny**
Sorry you're seeing the aggregate of both of the things like once I get both a 500 millisecond delay are you saying you're getting a block normally and then blobs are delayed on average?

**Terence**
So yes so there are kind of the same because we so in our implementation we wait until we have both before we process for choice and we're seeing blobs on average 500 milliseconds later, so blocks usually arrive within the first like 15 millisecond, and then blobs are arriving 500 milliseconds around there.

**Danny**
Yeah I guess I ask about the difference because you would expect a race condition between the two normally like they're roughly the same size right? Like 100 kilobytes or something, and so the fact that it's taking longer for this other message to propagate, is like very interesting and maybe that's because of the additional verification in the Hop times or something like that but I would suspect that it might be something more akin to like a certain client isn't forwarding until they get the block or something like that which is causing latency, so I just very interesting I I'd love to follow along.

**Terence**
Right so I think my preliminary analysis is that the Gab payload takes longer to return if there's a blobs bundle involved, so the kpl load takes about three times a stone. This is my preliminary investigation where this is leading, but yeah, I can I can give more updates later.

**Danny**
Yeah cool cool great that we're seeing stuff. 

**Tim**
Any other client teams have updates they want to share?

**Pari**
There's one more thing I wanted to add. Marius has started 4788 related fuzzing on the devnet 8 as well.

**Danny**
Got it.

**Tim**
And I guess on the El side so Nethermind mentioned you're rolling out the blob transaction pool across all the nodes on the devnet. Now, yeah from the other client teams I'm curious about like the status of implementation on the transaction pool because I know that was probably the last big open thing here a few weeks ago. Yes I'm curious do you ever does every team have something to deal with the blob transactions and how confident are you that its production ready?

**Andrew**
It’s still work in progress so we've checked in one like once we are but there will be like maybe one or more yards to improve our global transaction tool.

**Tim**
Okay.

**Andrew**
So we are hoping to test that on devnet9.

**Tim**
Okay.

**Peter**
Okay, the blob pool itself has been ready for quite a while and we are quite confident that it works okay. The only thing that is missing in gas code is the specialized feature for block transactions. Currently block transactions are announced the same way as every other transaction and they are retrieved without throttling or without any other productive mechanism, so that's the thing.

**Tim**
Thanks. On the Besu side? 

**Fabio**
Yes for Besu, in the next release there is the new layereth transaction pool enabled by default. These new implementation doesn't have yet any specific feature for blob transaction. The overall concept is that instead of being limited by number of transactions, is limited by size. So in this way even having more big transaction means less transaction in the pool but should not create problem with the memory. The idea is to continue to tune it in order to have specific configuration or specific transaction type so and for blobs there will be less blob for senders and also strict limit for blobs but at the moment blob transaction are treated the same as other and yes we still need to see how to find unit.

**Tim**
Got it thanks. So these are questions, about the question in the chat about ELs accepting blob transactions before the fork in the transaction pool, because does anyone see a strong reason to do that? 

**Fabio**
By default the best who doesn't accept this before the fork.

**Tim**
Why does the hive test demand it?

**EF Berlin**
There's just a hive test testing the interplay of the four Choice V2 four Choice V3 and it's trying to make sure there are blobs in the first block after so if it just seems most ELs activate their transactions type, the new transaction types whenever the fork is activated, so you can't propagate transactions of that new type until the fork is active. I was, I wasn't sure if anybody was wanting to start  supporting the transaction type before the fork. If there was any use case outside of just this test.

**Danny**
It doesn't seem of immense value if there's additional complexity to do so.

**EF Berlin**
I mean yeah it's not really much more complex it's just, I mean it depends exactly what we do, but it could be a little weird if, as soon as we push out the mainnet release candidates and people upgrade for blob transaction just sit in the pool for a while you know days or weeks that would be weird.

**Tim**
Yeah it seems easier to just change the hive test to have an empty block yeah absolute fork or something?

**EF Berlin**
Yeah we'll we'll talk about it offline thanks.

**Mario**
Yeah we can make sure that it doesn't happen. I mean it's really easy to Simply modify the hive test.

**Tim**
Nice um sweet anything else on devnet 8th or recent client updates that people want to share?

### Potential Additions 
#### [EIP-7516: BLOBBASEFEE opcode](https://eips.ethereum.org/EIPS/eip-7514) [CL specs PR](https://github.com/ethereum/consensus-specs/pull/3499/commits/cc3ced59653c39fb05a46ff33735144623ccdb1e)  

[14:27]( https://www.youtube.com/live/aobFWu7NANc?si=5IX5br-2vE9eDxMy&t=867) 

Okay so um next up then there's two potential spec changes you have to discuss. Yeah let's let's do that I just wanted to cover devnet nine after we discussed these spec changes so that we can then debate if any of those spec changes make it in should they be part of devnet nine or not. So the first one yeah the first of the spec changes is a CL change. So there's now an EIP for it,  7514 which Dapplion presented on last week's call about adding Max Epoch churn limit to the validator queue, which would lower the rate at which validators can join and sort of limit or push back the time when we'd have 50 percent and then you know more than that of ease being staked, yeah so we discussed this on last week's call, we're hoping to make a decision today given it's already quite late in the fork planning, so yeah curious to hear from CL folks. What do you think?

**Danny**
Just a quick note I believe that the current favorite proposal is asymmetric meaning this is only to the activation side of the queue, and doesn't change how exits happen, and there's an open PR, it's had review, I believe Hsioawei has been adding some tests and that like in the event that people want to do it, it's very simple from a testing and release process.

**Tim**
Dankrad?

**Dankrad**
I mean I'm in favor of doing this. I think there is a chance that the queue will stop being full at some point end of this year start of next year or something but I think it's a big gamble to bet on this. We're not sure what's gonna happen and I have a fear that that we might get into like a very like into a situation where we could have to make very drastic moves on staking and so if we can agree to do this churn limit stage change then it would be for you be much more comfortable for us to make like more measureth yeah transitions during the course of the next year or the year after rather than having to rush things.

**Tim**
Got it thanks yeah how do you CL client teams feel about this?

**Age**
From the lighthouse side I think we all are keen to see this but the asymmetric version

**Sean**
Yeah so I I was like a little resistant on the last call but I after looking into it further I think yeah one the asymmetric version is nicer and two, the actual like impact on wait times I don't think will be as extreme as like I was maybe initially thinking because the rate of new deposits is like currently lower than churn so I think that the huge spike that we had after withdrawals isn't actually the norm but yeah I still agree that it'd be good to have this  upper epoch churn limit to limit like the worst case scenario.

**Tim**
Got it thanks uh Enrico?

**Enrico**
Yeah, we want to report we did an internal survey and generally the Google Deco team is in favor of adding this limit and yeah also we were looking at the last version and seeing looks simple to implement it was just a comment from from Ben giving maybe there might be other alternatives to include in Deneb maybe having another consensus only for work to include it since maybe we are not super in rush but it's just a comment and generally speaking we are in favor of having this even in Deneb.

**Tim**
Got it thanks. Any other CL team? 

**Danny**
I suspect we can count Lodestar as fourth.

**Tim**
Okay yeah I see a plus one from Lodestar. Yeah I don't know if anyone from Prism has thoughts?

**Terence**
I don't have much thoughts I mean I trust all the CL teams on this but my Sly input is just like um with an app with blob the gossip maybe get worse, so it seems like to me it made sense to account for that extra factor which that we don't have today.

**Tim**
Got it and anyone from Nimbus on? Okay it doesn't seem like it um so okay so it seems like there's pretty broad support to have this uh pretty broad support to have it in Deneb and then there's a couple comments in the chat about the actual limit which I don't think we've chosen so the EIP proposes a couple different limits to be considereth yeah so that's probably assuming we're going forward with this then that's probably something we want to flesh out now. Ansgar so you have your hand up?

**Ansgar**
So just stay on that point I personally would really like to see like a limit more like eight, I think kind of the default one that was of course was 12 but there was different ones kind of like in comparison and for me eight looked like the best compromise it doesn't limit the duper of the queue too much for users but it also still ends up giving us a significant kind of extra breathing room to just have more time to figure out all these questions first.

With 12 we still basically it's the cube roommates will we still have a relative rapid size Pro growth so I don't know if if unless people think it is too aggressive I think that would be a really nice to have.

**Tim**
Thanks Danny?

**Danny**
Yeah I echo Ansgar’s sentiment.

**Tim**
Okay I guess does anyone want to make the case for another number than eight? It is a power of two as well, has that going for it. Okay so in that case I guess we're adding EIP 7514 to Deneb. We'll set the constant to eight and we can update the EIP and remove sort of the extra tables to make it clear what the impact is. Yeah does that make sense to everyone any objections or pushbacks? 

**Danny**
And just a note I would suspect we can do a release on Monday I don't think we can confidently get it out tomorrow with the testing that we want.

**Tim**
Got it yeah and then let's do the blog basically and then we'll discuss how all of this fits with the devnet9 as well but okay yeah let's consider this for sorry let's have this be included for Deneb and okay so we had another proposal this time on the El which was to add a base fee to retrieve the blob gas price so Arbitrum mentioned this and then Carl put together a quick EIP to formalize it but the idea here would be that similarly to how we can query the execution layer base fee or I don't know gas price basically, we could also allow query of The blob base fee and this makes it easier for l2s to generate transactions and whatnot that are dependent on this.

Okay sorry before we go that Mikhail has a a final question on the churn EIP on the validator side so do we consider the asymmetric version of the EIP or the symmetric version which seems I think we all said asymmetric, but I just want to 

**Danny**
Yeah make sure the question of the outside was asymmetric that's the pr
that we've been under review and we're working on testing on, in terms of the security from a accountability standpoint with respect to finality, there's only an improvement in that, and the Improvement in which activity period in either of these proposals and we don't see any downside from a security standpoint and having it asymmetric.

Obviously if they're dissenting voices on that we'd love to hear them immediately but right now that's our understanding of the security argument and that's our understanding of kind of doesn't create any sort of degenerative incentives either.

**Tim**
Okay anyone want to push back against asymmetric? Okay so we'll go that route and yeah we'll make sure to update the EIP to make that clear as well.

### [EIP-7516: BLOBBASEFEE opcode][(https://eips.ethereum.org/EIPS/eip-7516) [25:18]( https://www.youtube.com/live/aobFWu7NANc?si=hH20_V4qgBE_XH6S&t=1518) 

Okay blck to the base fee, so yeah we have the CIP called put together it exposes the blob base fee in the evm so it's very similar to EIP 3198 will expose it's just the basically op code and yes this would make it easier for L2s to interact. Oh lee, you're the one that proposed that?

**Lee**
That's correct yeah so I didn't write the EIP tea clear thanks Carl for that but I initially suggested the Blob gas price or blob base fee op code.

**Tim**
Yeah do you want to maybe just yeah talk like a minute for like why is this useful for Arbitrum and other L2s?

**Lee**
Yeah absolutely so L2s need to charge users for the price of code for the price of posting the user's transactions to L1 or specifically Roll-Ups too I suppose. And because how l2s generally work is there's a sequencer which accepts users transactions or if there isn't a sequencer there's some sort of aggregator model there's some entity that accepts users transactions over the RPC posts them to layer one and it has to charge the users a fee to pay for the cost to post those
transactions to layer one.

And in arbitrum this is a trustless model where the arbitrary system automatically sets the automatically sets the price of this L1 data and it does that by looking at how much batch posting cost and what the current base fee was at the time of batch posting that's in the system today but in EIP 4844, without the blog base fee opcode it's no longer visible to the evm what the cost close of hosting the blob was or what the current cost of plots is, so this EIP aims to address this by simply exposing that information it's already needed in that the evm or the El already needs to know this value tube charge for the blobs so exposing it to the evm shouldn't be much additional complexity there.

**Tim**
Got it, thanks. Yeah so we have as well yeah person from optimism I'd be curious yet to hear this is also helpful for optimism and yeah I don't know if you have a mic it's okay so there's a comment the blob base feature is not to require oh, do you want to just yeah go for it.

**Protolambda**
Yes I got well so it's not strictly speaking necessary for an L2 where you can do the fee accounting in the layer two in the layer 2 should be able to access any state any data from L 1, already now it is nice to have like I think it's a good improvement and since we already have the base fee information I don't see why we should not have the blob base fee.

**Danny**
To be clear you mean accessing through Merkel proofs into layer 1 headers? 

**Protolambda**
Yeah exactly yes so for example layer 1 information that the there to exposes from the layer one is also already basically passed along from layer one into Layer Two and layers don't use the difficulty of blobs for this like this is entirely true just a function of some data that the layer 2 node sees and then converts into the layer two block.

**Danny**
Got it.

**Lee**
Yeah historically Arbitrum has not parsed layer one block headers. I think definitely applying that as a work around would make sense and I think we figureth out how that could be done for the blob-based fee in particular um it's particularly helpful for this workaround that the previous blocks header contains all of the information needed to figure out the block base of the next block which would because the parent blocks hash is exposed to the evm but I think that this would be still a very useful option to have both in terms of I'm not sure on other else whose architectures and I'm not sure how many of them have looked at this particular part of EIP 4844 or how applicable this workaround would be to them,

And also if you want to make an L2 immutable it you can't be parsing the L1 block header with no way to upgrade it because there's a risk of the L1 block header format changing in the future.

**Tim**
Right that's a good point um yeah there's a comment by Terrence but there's any ZKA teams that have feedback on this side if there's anyone from a ZK robot team on the call another chance to speak up? Okay um so okay so clearly this is like oh Ansgar yeah?

**Ansgar**
 I mean obviously not from ZK team I just wanted to briefly mention that while the FPS is kind of a proposed to just have the op code that just pushes that one value onto the stack I think part of the reason maybe if I remember correctly by the EIP like right before it not initially include an awkward like this was just that we weren't but like that people wasn't weren't quite sure how best to expose this just because I think instead of just always having individual bits and pieces of Header information or context event context information over at some point we would want to have some sort of more structureth way where you can basically go through some sort of pre-compile so you can completely stop always having to you know go through the head and that that would so that we have a longer restricted in updating the header structure and all these kind of things I mean this is Aboriginal disgrace basically ideally you don't want to go through your header if this is enough of a nice to have that we want to have it in Lincoln of course that's not feasible because then we need a simple way to do it

In that case I would personally still prefer at least to have the op code be basically forward compatible with multiple P Dimensions so we just basically take one value from the stack and then just that's just the P Dimension basically so at zero it returns the normal base speed, one returns the database fee that now we have two op codes that both which have the normal basically but I guess that doesn't really matter and so then at least it's forward compatible I think that might be nice compromises you know a trivial change up to the EIP but yeah if we don't add it to dencun I think we would should instead start like a conversation soon for the next book after or maybe we should still do that how to expose and kind of had that information in a more structureth way inside the evm.

**Tim**
Right thanks Carl?

**Carlbeek**
yeah I mean I think it's very nice to be able to expose more of these things from the header but I also don't think it's quite as simple as Asgar's make it out to be the like just trivially looking up header items is relatively constant but if you want to start adding more fee dimensions uh particularly if we're starting to look at the L2 things like grouper costs or whatever then I think it starts becoming very complicated as to what the gas schedule looks like for all of this so I think like if we do want to do that having this like perfectly future-proof thing, I think that looks like a very complicated research problem that will take much longer and would potentially push out this solution for a while.

**Tim**
Got it Lee and then Andrew.

**Lee**
Yeah I wanted to just briefly mention that well I definitely think something like an OP code that exposes different parts of the evm context could be very useful I don't think it could be quite as general as reading different parts of the header there are some parts of the header which should not be exposed to the evm because that would break the mining process and also the blob gas price isn't a field in the header, it's computed from two different fields in the header, so I think exposing the even context would definitely make sense I'm not sure about the just exposing generalized header fields also I think it would make more sense for this to be in the op code instead of a pre-compiled if we're talking about generally exposing the generally exposing  different parts of the evm because for instance base fee block number those things I don't think you want to pay the overhead of calling fruit and pile for blob-based feed I'm not concerned about overhead 4 but if this is just a general EVM context getting thing then keeping it as not code would probably make the most sense.

**Tim**
Got it thanks. Andrew? You're on mute Andrew. 

**Andrew**
Oh sorry uh yeah I think we should do it because it's basically consistent with the base heat uh it simplifies live for abitrum and probably other l twos it's an easy change so it doesn't introduce any inconsistencies if we decide later to do some something clever about exposing the header we will just we'll have to do it for base fee and blob base here and so on so like adding blob-based fee does not complicate that future refactor.

**Tim**
Got it thanks. Yeah and I guess this is probably a good a good transition like to hear from some of the El teams, like do any El teams think this is not worth including or are opposed to this? Or I guess have any other comments uh yeah so get yeah Geth already implemented it I think it took Marius 10 whole minutes to implement it as we were on a call together.
Okay Nethermind is in support. Carl you wanna?

**Carlbeek**
Other yeah just on the last comments thing I see I had a collision with the opcode number whatever, so it's it will change to exactly what get has right now so it gets basically done it okay and what's one minor change.

**Tim**
So what's the op code number that we will use?

**Carlbeek**
I had zero x49 just goes next to the blob base fee yes because I was using evm.codes and that's an account for blob hash which already has rx49 so then it'll be zero x4a.

**Tim**
Okay so 0x4a would be the right one okay and we already have a PR for testing, great yeah. Okay so last call any objections to including this?

Okay so yeah let's add this one on the execution layer side so we'll update the EIP to reflect the new uh op code address and I believe that's the only change we need to do to this EIP. Okay so with all of that out of the way, devnet-9.

## devnet-9
### [Update EIP-4788: post audit tweaks EIPs#7672]( https://github.com/ethereum/EIPs/pull/7672) [37:20]( https://www.youtube.com/live/aobFWu7NANc?si=rUqMQTQ2LIogmIwh&t=2240) 

So we had a plan to launch devnet-9, no we should not add more things EF Berlin yeah we had a plan to launch devnet-9 in, I believe, five days. So does anyone on track for that?

Okay so Barnabas is saying we're still on track for that, which is great. I assume we should include those two changes in devnet-9, does anyone disagree with that? 

Okay so we include both EIPs do any client teams think it's not possible to get that done within a week?

**Pari**
I would say as with the previous devnet Cycles we're gonna first have to have the client releases then make sure the high PR is merged, have it in Hive do the local testing and get it on the devnet so I don't think devnet nine Tuesday which is essentially four days from now it's realistic, just probably should move it by another week.

**Tim**
Got it and I guess is it realistic for teams to say a week from now like on
next week CL call having implemented those things, and passing tests given they're both quite small? And then assuming we get there that on the CL call we can make sure to iron out like the final timelines for devnet-9 we also have the testing call next Monday so if people run into issues in the next couple days or there's something that's more complicated than it seems we can we can discuss it there, but let's maybe aim for like implementations that are passing tests next Thursday, and then yeah on the CL call, sanity check the launch date for devnet-9 and hopefully yeah those are not all plus ones on the  vacation but plus one's on getting that done by next week.

Okay so and then so for devnet nine one more thing we've been doing these 4788 audits uh in the past few weeks. We've got three audits, I believe two out of the three are complete. The third one is finishing this week so they've revealed some small tweaks to the 4788 contract we were planning to go over all the audits reports on the next ACDE so two weeks from now. So there was a question as to should we have the like should we have those audit post audit changes part of devnet-9 or do we want to wait potentially another two weeks until all the audits are finished and we've had time to review the changes and and the reports yeah how do other people feel about that?

**EF Berlin**
I don't know if there's that much that will be necessary to review so maybe an optimistic case we just plan on moving forward?

**Tim**
Okay I guess.

**Danny**
Yeah I'd be fine sharing the audits in a summary of changes in ACDE and if it is an issue to deal with it rather than assuming we need to get on a call to share.

**Tim**
Yeah so I guess given we have at least two of them done and I think the next one the other one is finishing tomorrow, if I got that right, can we discuss that on the CL call next week and if there's any more change that comes from this week's audit, we'll have them included there, and even though we may not have all the final reports and everything we can at least walk through the like yeah the pr which people can already start reviewing, and then on the next CL calls or a yeah agree to merge the pr and to the changes?

**EF Berlin**
Yeah that's fine. Our calls are converging but yeah well yeah we're getting close to shipping distance so I tried to save weeks or we can I mean I can also mention 

**Tim**
Yeah yeah do you want to go over it yeah yeah the output of the first two and how that's changed, I'll post the pr in the chat here.

**EF Berlin**
Yeah  I mean I'm hopeful that there are no other changes beyond what was found in the first two because generally the audits have been pretty good there hasn't really been anything you know specifically found, there were three things that were sort of nice to have improvements, the first main thing this was like the thing that we wanted to fix the most was that there was a edge case on the get method of the system contract where if I passed in the timestamp of zero just all zeroes, it would actually return zero as the beacon route and it's not really useful for anyone, I don't think that there's really anything that could have happened if this was live, because you can't create then a proof against a beacon route of all zeros, but it was a kind of a weird edge case on the correctness of the pre-compile. 

It was designed intended that you would the contract would revert in case it asks for a time stamp that didn't have an associated Beacon route so that was the main thing that we really wanted to address and so now in addition to the other checks that exist in the uh EIP to make sure that the timestamp passed in is actually associated with the result. 

We make sure that the timestamp that's passed in is non-zero so that was the big thing the two other changes were very optional, honestly just like slight improvements but OnStar had had taken a look at this a little while ago and he thought that the history buffer length the ring buffer length was not the optimal size if the slot time were to change and so he proposed that we modified the buffer length to be a prime number roughly around the number of Beacon routes that we wanted to store so we wanted to start 8192, turns out that 8191 is a prime number and what that gives us is that no matter what slot time we change it to the buffer will always be 100 % full, so we won't incur any additional storage overhead of kind of dormant storage slots, if the slot time changes.

So this was kind of a you know nice like small change that was beneficial and then the last one was really just more for aesthetic preferences, the original contract was written to use the call data copy op code or sorry the call data load op code two or three times I think, and we just modify the logic slightly to use call data load only once, just in case in the future if call data happened to change in price there's really yeah it was just aesthetics it really didn't need to load it from call data multiple times.

Once it was on the stack we kind of just duplicated and then swapped as necessary so those are the three things that we sort of found that we want to change based on the audits, nothing else has really been found and yeah optimistic that after this next audit nothing else we found so I mean honestly the main reason that we haven't merged that PR to the EIP itself is that we're trying to just finish mining an address to deploy the contract too.

So yeah once we find that we'll update it and yeah merge it.

**Tim**
Yeah thanks for sharing it. Danno?

**Danno**
Can we get the explanation of the Prime modulus into the EIP? I think that's really useful, but I think we will lose track of it if we only have it in this call, also there might be issues that it might be unreliable when we're transitioning between block change times because it's going to fill the buffer in a different order so that might be worth calling out as a security consideration not worth stopping but I think it should be called out.

**Tim**
Thank you any other comments thoughts?

**Andrew**
I think there was a comment from Mario's is that the buffer size or something was wrong in the pr something like that, oh sorry for Mario Vega, I think I was looking at hive tests so yeah and download this course there was some comments.

**Mario**
Yeah on the white code I think the modulu modulus value was incorrect and I've not I don't know if that's already addressed.

**EF Berlin**
Yeah it's updated and actually maybe it's not updated on the EIP, it's updated on the pr to the byte code but I yeah I don't know if I pushed that onto the EIP.

**Tim**
Yeah and I guess the other option is we can also push to merge all these changes now and so it's kind of finalizing the EIP even though we haven't had all the full audit reports but it might make it easier to set up tests and whatnot, would people rather do that or are we fine waiting until next week and and having the reports out and the I guess confidence that nothing came out the next like in this this last day of audit?
Or maybe another way to phrase this is anyone blocked if we don't if we don't merge this before next Thursday?

**Danny**
Yeah I mean these are generally like transparent changes to the actual clients, like the interfaces don't change, so I don't see how it's going to cause complexity one way or the other.

**Tim**
Okay and Marius when you say you would like to re-audit it, do you mean having new audits run on this latest version or?

**Marius**
Sorry it's a bit loud here I would I would just like to run like the audit that I like myself did on it again on these new versions but I held off on that because I wasn't sure if the improvements would make it through or if the changes would make it through and so oh that's my plus

**Danny**
Does anyone dissent against the changes as they currently stand and that any other changes would be like additive or in relation to further found bugs because you could I think given the state of where we're at like you could confidently audit that also the audit reports coming out tomorrow so you confidently audit the pr, especially after that audit report comes out. 

**Tim**
The reports won't come out tomorrow, sorry. The audit will be done, they'll probably send us an informal message to say you know looks good or here are some issues but the report probably won't but yeah.

**Danny**
I see. 

**Tim**
But yeah, does anyone oppose merging as this changes, okay. So let's maybe okay let's merge these in well we'll discuss it again next week just at the very least to send it to check that nothing else has changed um and yeah it'll make something a bit cleaner for people to review yeah in the in the coming week. Anything else on 4788?

**Andrew**
Yeah well I wanted to bring another thing is like there is the subtle if you start with an empty system address that currently like but 

**Tim**
We lost did you just drop off the call?

 yeah I can't hear me oh sorry is it better now yeah you're back yeah 

**Andrew**
Okay so basically like you would expect you know the system transaction to touch the system address and then delete it at the end if it's empty but it doesn't happen in yet and no does it happen in Azure though because there is disability that the sub balance does not touch the address of the transferreth value is zero so effectively when it was effectively what it means is that the system address is not touched and left empty after a system transaction which is and so if we just agree that okay so there's there is this work some somewhat unexpected I just wanted to ask to agree while we keep things as they are currently implemented in geth or change anything about it, and the these are there are just cases in the execution spec tests that actually are rendereth with this behavior that the system address nmt system address is not cleareth at the end of the system transaction, so it would be fine that's this weird quirky behavior that's why not or we change it. 

**Tim**
Okay I see there's a couple of raised hands already so Marek?

**Marek**
Okay my opinion is that we should remove this account from the state just by readings all the EIPs however it's important to have that it's not minute issue and we analyze here only the edge case that is possible in hive test, but if we agree that we should remove this account from the state it would mean that some clients would stop passing the test only because of this empty edge case.

However the client won't pass the test if they implement for 788 as a direct right to the state without system transactions so they do not touch system account, so what else we have, an EIP 4747 that said that we removed all empty accounts on mainnet and clients are free to remove empty account handling edge cases from the code base. So the thing is that we end up in the funny situation where there are two valid results of these tests, unfortunately this edge case is bundled together with two other with other cases that all clients really really want to pass and test so my proposition is to move this edge case scenario outside of other 4788 and got contesting and just keep it as a separate test and I'm not sure maybe it sounds weird but clients will be free to pass it or not depending if they want to rely on this system account assumptions 

**Tim**
Okay anyone else have thoughts or 

**EF Berlin**
Makes sense to me.

**Tim**
Okay so just to make sure we're all clear you mind just summarizing quickly what the path forward is?

**Marek**
So I guess we should remove this empty account handling from hive test and maybe keep it as a separate test yeah and it will be up to the client if um it is weird but it will be up to the client to pass or not this test, so they can rely on assumption that there is no empty accounts on mainnet and they don't need to touch and remove this account, does it makes sense for lightclient as well? 

**Andrew**
Well I would like us to agree on the same behavior because we actually, it's kind of this, one of those corner cases that better if we do if all clients we had the same because then we'll have worry less about Pro protocol failures yeah I I would prefer to formalize it and agree on a single approach 

**Marek**
So what version you would like to see? Removal or keeping in the state well it's probably the easiest version well well, for me is that to keep things as is to keep this weird Tech work that exists in a gas and then Aragon and not remove empty system address.

**marek**
Yeah but it would mean that it's so in theory by reading all all the EIPs like uh 158 and 161 we should remove this so well maybe we separate this test it will be I haven't I don't know a bit easier to arrive.

**Andrew**
Exactly when an address is touched, transfer so well okay kind of color I see it because uh it was like it was never specified and the touching of addresses was never formally specified in the yellow paper, so I guess we could follow what would follow geth and treat geth behavior as the standard.

Yeah or maybe I don't know does the new does EOS specify whether an address is touched or not like exactly that like the executions back does it specify exactly when address is attached? For

**Danno**
The reference test is normative whether or not it's in the yellow paper so that's when I do evm stuff and basically that's the approach I've been taking is that the tests that have been in place for years are normative, as far as system accounts the rules not deleting system accounts is about specifically not deleting the right MD
address um that's what's written into the yellow paper so that's the one exception that resulted from the Shanghai attacks.

**Tim**
So given there's like some uncertainty here is it worth maybe taking it offline and bringing it up on Monday's testing call after people had like a couple days to look into it more? Okay perfect let's see that's yeah so I'll make a note and I ping the Els teams as well so um yeah let's discuss this on Monday. Okay so I think yeah this was the last uh devent-9 open question so we'll sort that one out on Monday, September 18, 2023

But aside from that basically we've agreed we'll add the max epoch churn, we'll add the blog base fee we'll also add the changes that have currently been proposed by the audits for the 4788 contract. Is there anything else people feel should go in devnet-9 specs assuming we'd want devnet-9 to be the last one before we move to actual testnets, so is there anything else we should be testing there? yeah Mario?

**Mario**
So yeah probably the trusted setup update would be a good idea to have it in the devnet 9 the mainnet across the setup.

**Tim**
Using this so loading the mainnet file and using that?

**Mario**
Yeah but this also comes with the update of almost all tests I think so it's a pretty high modification to all of the tests, it's easy to do but I was just wondering if it's ready for us to use.

**Carlbeek**
So long and short of that is gonna need another say a week and a half to get that ready making some changes of those two file formats and that kind of thing.

**Tim**
Okay so then I would not block devnet-9 on it agreed will we want I guess we could have like a super short-lived devnet if we just want to run through this on before going on like Holesky or Goerli, but yeah that would be the last thing I guess that's out of scope for devnet-9.

Anything else? Okay so yeah let's hopefully sort out this issue with the touch addresses on Monday and then by Thursday hopefully teams all have  everything implemented for devnet-9 and on the CL call we can discuss when we  actually want to have this thing go live, does that make sense to everyone?
Okay, sweet so that was I think everything from the spec side, last thing we have today is the Reths team wanted to take time to actually introduce their clients so they've been working on it for a while and slowly becoming part of the the stack so yeah George just take it away.

## Reth Overview
Hello good morning let me share my screen. All right this should be visible all right sweet so thank you for coming to my TED Talk and thank you for the introduction uh we're going to talk about reth which is a new execution layer that we've been building at Paradigm for the last maybe almost a year now, year and a month or a few weeks, the repository is here, the blogs are here, we have a book a chat room you can find me here, and I will get into a few details about the client today, and feel free to interrupt me.

So what have we done, firstly we have an execution layer that Apache Mighty license in Rust the reason for the license was to make it maximally permissive for third parties to be able to consume it, without having to think about the license, review the node as the first use case but what I'm really excited about is the usage as an SDK in infra, so we pay a lot of attention to our abstractions to our tests or documentation, such that people can use components of the node without having to have the full thing, and we've already seen nice results for that, which I can go on in a bit. It has very good performance we test on beefy Hardware so caveating that this might not always work for everyone.

But on the hardware we tested on latitude and third-part discovery reduced it with sync in 50 hours which is really impressive okay and that is in archive mode, full node syncs slightly faster due to less data written, but overall the rough is the ball is like around that.

I have two IPS here that people should feel free to play with they're running Alpha 8 uh it's been up for two weeks alfayette is running on the same machine and it's keeping up with the tip, without any issues so we want people to hit this box, and ideally identify new resource leakages or issues that we haven't identified so far we take an open source first approach a lot of culture around mentoring onboarding people and so on so far we have over 150 contributors with only eight of us being Paradigm funded, me included, um and we have some encouraging numbers also on the library usage.

Just to give you a quick architectural sketch and I acknowledge that this should be a lot deeper but uh just to take this from a high level, on the sinking mode we employ Aragon's technique of the pipeline or stage sync which means that first you download all the headers, then all the bodies then you recover all the  senders then you execute, then you generate the state route blah blah
and this causes a nice thing because it allows you to separate workloads from each other and by separating the workload from each other you can heavily optimize because each workload is very specific so some stages are going
to be CPU bound others are going to be i o bound and you can very carefully optimize each one without stepping on other people's toes.

We employ a new mechanism that we call the blockchain tree for staying up to sync so the pipeline or the stage sync is used only for the historical sync. You should almost think of it as like a database batch read, a batch historical backfill, where the benefits of loading over big ranges of blocks are valuable was for the live sync we employ an in-memory data structure which basically tracks the last n blocks configurable uh it creates a tree of all the possible states that you can be in depending on the messages received from the engine API um and then anytime we receive the fork updated, we can only realize a branch of that tree or Flash into disk and everything else gets discarded. 

In the database we employ the flat database design also an Aragon innovation using the fast incremental State Route algorithm that they also came up with and we use mdbx via rust because we like consistency we like having multiple readers on the database and we have historically really liked its performance which is also driven somewhat by the usage of Mema I haven't run personal benchmarks on this but the node also performs well on ZFS. Currently we employ that is decompression in some of our tables but some people have run rest nodes with ZFS and zsdd or lc4 I forget enabled, and they had an archive node as low as 1.2 terabytes. Big asterisk on this number I haven't replicated it but I've heard it from more than one person. revenue is the engine at the core of ref it's a VM developed by a dragon who some people here might know we use that evm in Foundry as well.

It's I think the fastest if like I think evm1 might be faster in some benchmark or most benchmarks but it's general very easy to consume as a library it's basically hook on in various steps so it allowed us to build a lot of nice things on top of it. For Json RPC no we support both geth debug trace including the JavaScript Tracer by embedding a JavaScript runtime um whenever a user provides them a tracer and we also support parities, original Trace module which is obviously very useful for map searching, for data analytics and so on.

What one thing that we've done which I think was very useful is that we run the engine API and the blockchain tree in a separate thread from the main system which means that if somebody hits their PC very hard it does not cause research contention with the consensus critical functionality, which is nice. We take a very defensive depth approach to our releases docs and testing or I guess in our testing and I'm not going to go uh through all of this right now but we have a lot of docs we have a whole book for node operators we have rust docs inside the code base, in fact we have lints in the code which do not let you merge publicly exposed code without documentation and we have a good map of the repository here for anybody that wants to follow.

We run Hive on a nightly basis. It runs on CI, we get reports about it, we fix them and yeah we're overall excited to also be included soon in the Upstream Hive testing Suite. Another thing that is very interesting is that we developed an RPC load testing tool which we've been using to evaluate RPC providers, third body RPC providers but we also use it for equality checking as a differential fazer effectively between two rpcs, so while we were testing our tracing implementations for example, we were running the trace we're running flood with the equality mode on, for an Aragon a geth and a reth node and would like see where was there a diff and we didn't slowly find the bugs so very very feedback loop-driven approach with automated dueling for testing and so on.

So far so good in terms of performance benchmarks. This is the box that was mentioning so it's a big beefy box it costs order of 250 bucks a month, which is quite a lot, it the sync what we found out is that the sync really depends on the disk and I know that most people in this room are experts like we didn't know about this and so we were very surprised to see a very big  variance in syncing time depending on the disk um and a matter of fact there is a great gist on GitHub with a bunch of disks that you can use for sending nodes not just reth nodes any kind of node and overall pretty exciting to see like more people kind of publishing their numbers and overall getting a better understanding of what is the optimal like disk setup for a good ethereum node.

Again something that people know here is that the AVM is single threaded so less cores more clock speed is good for performance however we're starting to iterate on some parallel VM work and we're excited to see if that's gonna change in the future. Ram requirements it's eight gigs but we hope to go lower because it's all configurable and basically it's a bunch of in-memory caches that we can tune down, it already has synced on ethereum on arm uh after coordinating with the founder of the project so there is promise also in like lower end devices.

This is like a meme I like to use from around we might have here basically we're not production ready we are eight Alphas in. We've been running nodes for weeks without issues but I cannot in good faith recommend somebody to put a hundred thousand dollars or whatever it is uh today in software that is a few months old without an audit, if there is interest in helping with another please reach out.

If you want to run a node also please reach out I know people are running it in production we don't provide any reliability or warranty for it I don't know that we will ever will but we hope to be production ready by the end of the year. Cancun which is the big question for here basically you can see the  establish here 4844 we basically have it all done in the evm we're merging the pr today mem copy is done t-store is done self-destruct we just had an open VR The Blob base fee we just had the APR um for it actually like a few minutes ago 4788 it was very nice to actually see that it was not requireth to make evm changes for it and I think it's almost done and for 4844 the main thing that we're missing is a non-disc implementation of The Blob pool but we
have an in-memory implementation of it which means that we can move on hopefully to the devnet testing.

High level cultural point from like our team we try to be good vibes and collaborative and I think this is kind of like the cornerstone of the vibe. We have been attending all core devs, I haven't been because it's 7 A.M on a Thursday but sometimes I think most of the team is present because they're in Europe. We are happy to be part of any calls discords like sending us stuff to prototype we want to hope that we are able to prototype quickly one thing that was part of the core not like motivation of building the clients. We're happy to give feedback on future EIPs or to be asked for feedback.

And just to say it like we don't have like any political agenda here like to push for any like crazy changes if there is anything that is very numbers driven and we can provide a good objective uh in case for it we're happy to do the research or do like push for it if it makes sense, but I don't think you know you would expect me to say oh there's a paradigm private funded company and like we would push this like that's not that's not the vibe here. So just wanted to comment to that and somebody has asked us about if we would do ACL we're not planning to I am open to creating a single binary for like combining the nodes together, as an experiment but I don't know that this is like a great practice you know just because you could doesn't mean you should.

So TBD there but again open to experimentation we're like clean slate oh there's a big slide um so uh next stop devnet9 uh we hope to be ready for it, Holesky as well, very excited for that to kind of like Get out of your of our channel in the next steps, or roadmap items, we have snapshots um snapshots are kind of Aragon style flat files that are used for accessing historical data, unfortunately due to the way that we set up the sync which is also similar to Oregon we're not compatible to the geth, nethermind snapsync. 

We want to be part of some kind of snapshot thing that lets us be collaborative and also see data in the network not just be Victorian glitch which is it's not clear how we get there so if there is questions or discussion we can have on that please reach out and the third one is production readiness so the hope is basically where feature complete with cancun and snapshots and end of the year two three months of more polish audience refactors having our coverage and sharing 100 on hive all of that and we hope to have mainnet production testers soon and ideally you know we can enter 2024 and be like reth is 1.0, use it let's go.

There's a lot of like research that we want to do in particular more performance things I'm a big fan of IO Innovations in databases whether it is I O urine in the kernel or direct i o if you have experience with that please help us um on Parallel VM we have designs we have read all the blog STM papers we have read the Aptos to move the like polygon implementations like we know how to do it I think but I think there's like low level issues that prevent you from like going too fast so we're also happy to discuss about these.

And yeah please talk to us about any future ethereum changes uh we're happy to experiment discuss provide critical  feedback say this is a great idea I'll say this is a bad idea but always good vibe and collaborative. I think that's it happy to take any questions.

**Tim**
Thank you um there was one question earlier around snap but it got answereth both in the chat and through your presentation uh there's a question by Justin what's uh what do you use for the underlying key Value Store?

**Georgios** we use a libm dbx uh we do the library that was used in cell gorm ergon and this is a c like this is a C library but we have a five to it over rust and the bindings were written by artem, who was the previous rust node developer. We are we have abstracted the database to be behind an interface and we already have been experimenting with alternative databases. The main thinking here is that we want to not be kind of like logged in to a certain B for example we don't allow the usage of mema in mdbx because even though it gives performance in some cases, the data sets are big and when the memory when the data set is bigger than the memory it ends up hurting performance actually so in general like we wanted to be able to experiment so mdbx is the first database.

I know somebody has been experimenting with the postgres backend without it necessarily being a good idea but we have a clean interface for implementing new ones so you know we started with that one because that was the easiest one uh to use the best for performance but we're open to new ones you know if you could give me a Cassandra DB like integration that gives us good performance I would be also open to it.

What's the use for the underlying restore um I'm not sure I understand the question.

**Tim**
I think that yeah that was the question you just answered. okay yeah okay yeah.

**Georgios**
There's like two details also on that which are interesting I think we do that mdbx or in general like these types of databases they have uh transactions which means that you to write many things to the database you don't need to multi-thread and like just spawn a bunch of go threads which I think is how it was done in level DB, you're able to open transaction roll up in memory a bunch of like database changes just flush them and we have architected in a way that only happens across blocks so by leveraging the acid of that database you're ensuring that your DB is always in a consistent State and this is very powerful because you never control c and end up in a Corrupted State which is a lot of like node devops issues.

**Tim**
Is there are any more questions comments either raise your hands or put it in a chat?

Okay yeah uh well yeah thanks for sharing this and yeah great work on reth.

**Georgios**
Yeah of course thank you um snapsync is very top of mind I'm saying right double questions on this, I don't know honestly I don't know I thought about like adding pre images in the things being gossiped I heard that there is like image pre images being ghosted in the vertical trees yeah I'm not sure ibfs back and when when I owe and bandwidth stop being an issue uh we do have we had a first look at verkle trees um I have a doc I don't honestly I haven't read it in weeks so I don't have a good answer there. 

I know like like one person or team is like responsible for doing Explorations and uh yeah we have a thread, the Dual Merkle tree component seems like very scary, and a lot of Maintenance overhead, so no strong opinion but just saying it feels meaty.

**Tim**
I see. Any final questions okay well yeah thanks uh Georgios and I think we also have a rest tag in the r d Discord if people want to tag you there for any questions. Sweet, that's everything we had on the agenda anything else people wanted to cover before we wrap up? Okay if not, well thanks everyone, talk to you all on the Monday testing call. 

Everyone says thanks. 
## Attendees

* Tim Bieko 

* Paritosh (EF Berlin) 

* Danno Ferrin

* Terence

* Lee

* Protolambda

* Roman Krasiuk

* Andrew Ashikhmin

* La Donna Higgins

* Peter Szilagyi

* Hsiao Wei Wang

* Carlbeek

* Danny

* Ken Ng

* Potuz

* Lion dapplion

* Joshua Rudolf

* Kasey

* Pooja Ranjan

* Marek

* Alex Stokes

* Mehdi Aouadi

* Draganrakita

* Maintainer

* Marcin Sobczak

* Enrico Del Fante

* Adrian Manning

* Yaroslav Kukharuk

* Tanishq Jasoria

* Rai Sur

* Mikhail Kalinin

* Frethrik

* Daniel Lehrner

* Ignacio

* Phil ngo

* Sean


