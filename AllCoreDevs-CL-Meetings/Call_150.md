# Consensus Layer Call 150

### Meeting Date/Time: Thursday 2025/2/6 at 14:00 UTC
### Meeting Duration: 1.5 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1265) 
### [Audio/Video of the meeting](https://youtu.be/JhDgD366DKg) 
### Moderator: Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
150.1  |**Pectra Devnet 6** Pectra Devnet 6 launched on Wednesday, February 5. So far, the devnet is running smoothly with no major issues. There is a minor issue regarding an incorrect API response in the Lighthouse client that developers said is an easy fix. EF Developer Operations Engineer Parithosh Jayanthi said MEV workflows are being tested on the devnet and so far, there are no bugs to report. Paul Harris, a blockchain protocol engineer at Consensys, commented on the meeting agenda final CL specifications are needed for cutting an updated release for Beacon API references. Stokes said that he could follow up on the status of CL specifications.
150.2  |**Pectra Devnet 6** Mario Vega from the EF Testing team said that he is working on additional testing for EIP 7702, set EOA account code. Related to additional testing, Geth developer “Lightclient” highlighted a pending pull request for the EIP that requires review and feedback from other client teams.
150.3  |**Fork Scheduling** Then, developers discussed potential dates and times to activate Pectra on public testnets. Beiko commented on the meeting agenda three candidate timelines for upgrading Ethereum testnets and mainnet. The first requires client testnet releases by February 10 and would result in a hopeful mainnet activation by March 27. The second requires client testnet releases by February 13 and would result in a hopeful mainnet activation by April 8. Finally, the third requires client testnet releases by February 17 and would result in a hopeful mainnet activation by April 8. (The number of days between the Holesky and Sepolia upgrades for the third option is shortened such that the mainnet activation is the same for both the second and third candidate timelines.)
150.4  |**Fork Scheduling** Client teams expressed preferences for the second option and were supportive of the suggestion by Derek Lee, Senior Product Manager at Offchain Labs, to incorporate a 30-day buffer period between the last testnet upgrade and mainnet upgrade. EF Security Researcher Fredrik Svantes wrote in the chat, “+30 days is definitely good from a security pov. I strongly support it.”
150.5  |**Fork Scheduling** Beiko confirmed that client teams should have their releases for both the Holesky and Sepolia upgrades by February 13. He said the Ethereum Foundation could publish a blog post featuring these releases the next day on February 14 to notify the ecosystem about the scheduled testnet upgrade. He added that client teams should refrain from including any official mainnet upgrade configurations in the testnet releases until the time of the last testnet fork. Assuming all testnet forks happen smoothly, developers said they will decide on an official mainnet upgrade date and time on March 6.
150.6  |**PeerDAS** Jayanthi said that testing for PeerDAS has been happening mostly locally on clients and Kurtosis. These tests have been running smoothly so he said that he is trying to launch a multi-client PeerDAS devnet today. “I’m close, but it might happen a few hours after this call and I’ll post information on the PeerDAS testing channel but essentially, it’s exactly what we have on Kurtosis so it should be fine,” said Jayanthi. Once the devnet launches, developers will assess changes to PeerDAS specifications and implement fixes for another PeerDAS devnet thereafter.
150.7  |**PeerDAS** Lighthouse developer Sean Anderson raised two design questions about PeerDAS. He floated the idea of moving the responsibility of building KZG proofs for blobs to the transaction sender, as opposed to the validator, i.e. the block builder. This could help alleviate computation bottlenecks in validators and scale the number of blobs that can be processed on the network. Secondly, Anderson raised the idea of blob parameter only (BPO) forks. For more context on BPO forks, refer to prior call notes on ACDC #149.
150.8  |**PeerDAS** Stokes recalled that the concern about requiring transaction senders to compute blob proofs was introducing complexity into the EL. However, he said the idea should be researched further, and “if it helps scaling, I say we do it.” EF Researcher Francesco D’Amato noted that the idea was also discussed during last year’s Devcon conference and notes from that discussion have been recorded here. Generally, developers were agreeable to the idea.
150.9  |**PeerDAS** On the topic of BPO forks, Stokes said that in theory, the PeerDAS upgrade should support an 8x increase in blob capacity. However, if it does not and developers require a more gradual increase to blob capacity post-PeerDAS, he said this should be when developers revisit the idea of BPO forks. For now, Stokes encouraged developers to keep working on finalizing PeerDAS specifications and implementations on devnets.
150.10  |**Validator Hardware and Bandwidth Requirements** EF Applied Researcher Kevaundray Wedderburn requested feedback on the impact of the max blobs flag to validator hardware and bandwidth requirements. He noted that with the flag, developers would not need to constrain the network to the bandwidth of local block builders. Nethermind developer Ahmad Bitar said he was supportive of the idea but stressed that a long-term solution for preserving the participation of “home stakers”, independent and non-professional entities and individuals, in block building was needed, which is why he has proposed the inclusion of enshrined proposer builder separation (ePBS) in Fusaka, the upgrade after Pectra. EF Researcher Ansgar Dietrichs countered Bitar’s point saying that there are “more minimally invasive change than ePBS” to help preserve local block building on Ethereum and that ePBS seemed “too complex” in his view for Fusaka.
150.11  |**Validator Hardware and Bandwidth Requirements** On the topic of the max blobs flag, Prysm developer Terence Tsao said that the flag may impact how blob purchasers, primarily Layer-2 rollups (L2s), predict and calculate blob costs. Dietrichs said that he could bring up the topic of the flag on the next dedicated Rollcall meeting with L2 teams.
150.12  |**Pectra Retrospective** Stokes recommended that client teams start reviewing the EIPs that have been proposed for inclusion in Fusaka. He also recommended a review of the Pectra retrospectives thread on Ethereum Magicians. One of the takeaways from this thread that Stokes highlighted was the desire for developers to be “more disciplined” in fork scoping by trying to plan out the scope of forks farther in advance. EF Protocol Support Team Member “Nixo” noted in the Zoom chat that this sentiment runs contrary to how developers felt before Pectra when they decided to delay Verkle. Stokes surfaced the idea for developers to freeze the scope of Fusaka to PeerDAS and EOF and leave all other proposed EIPs for discussion in the context of the next fork after Fusaka, Glamsterdam.
150.13  |**Pectra Retrospective** Svantes said the EF will host a hackathon for Pectra geared towards security researchers and identifying bugs in client implementations. The hackathon bounty will award up to $2m to participants depending on the bugs found. The EF will share more details about this program once client releases for testnet upgrades have been published. Svanted said that client teams should prepare a one-pager highlighting the Pectra code changes in their client that security researchers participating in the hackathon can use to identify bugs. Svantes also encouraged teams to help spread the word about the hackathon once the program begins.
150.14  |**Pectra Retrospective** Beiko reminded Pectra EIP authors to update the status of their EIPs to “Last Call”. He also highlighted that Vega is working on a proposal to formally define new and stricter testing requirements for EIPs moving forward.


**Stokes**
* Great. Thanks. Okay, everyone today we have consensus layer call 150. Let me grab the agenda here. I'll put it in the chat. So it's issue 1265 on the PM repo And yeah let's go ahead and get in to it. There's a number of things today around Pectra and some other fun stuff. So to start with Petra we have Devnet 6 that is launched. And yeah, the Devnet looks like it's gotten much better than Devnet five, which is good to see anyone here like to say any more about the status of the Devnet or any updates? Are there any issues we should discuss now Or you put a link here in the chat yeah, that looks good 

**Parithosh**
* Yeah. Maybe just, note on one thing that's still, partially missing on the devnet. So we do have some map blocks being produced by the blocks route relay. we're still in the process of setting up the flash blocks relay ourselves. there were a couple of changes in there that took a bit longer to integrate into our Ansible stack. but we should have some information, probably after the call or early tomorrow. and that should close up the map testing issue cycle as well 

**Stokes**
* Okay, great. And we did exercise at least the client pathways with the mock builder. I think I saw a message to that effect. Yeah, exactly. 

**Parithosh**
* So we've already tested with the mock builder and it was fine. And we also tested it locally on kurtosis. And we didn't notice any bugs in itself. but there was a request to make sure that there's execution requests in the map produced, blocks as well. And that's one thing we should definitely check, and we haven't yet 

**Stokes**
* Okay, cool Then other than that, any client issues that we should be aware of, or do we want to call them Devnet six? generally Devnet six as success. Okay. Perry says nothing worth discussing, which is good to hear I think there are, like, a few small things just to flag it on the discord. I saw that lighthouse didn't conform to an API, I think which I think is a pretty easy fix, but just something to be aware of. And what else? So there was also a question here about the beacon API's. And let's see I think this was from Paul. Can we get a more final spec so that we can update the beacon API references. Is Paul on the call here 

**Paul**
* Yeah. So just in terms of that, just need to have the effectively the release version so that all the references can be to the actual Electra release rather than alphas or betas. At some point, if we're getting close to releasing, it'd be good to actually have a release sort of spec 

**Stokes**
* Yeah. Was this blocking anything 

**Paul**
* We just can't cut the release until we have that. Ideally for the beacon API. 

**Stokes**
* Right. Okay yeah. Well, I mean, generally, I think how we do it is once we feel like the beta series is good to go, then we would cut, the actual spec for Petra, which it sounds like we're very close to. I don't know if we're quite ready, but we will be soon. so, yeah, I can reach out and or follow up on the beacon API's. once we're closer to that So cool. anything else on Pectra on the CL side there? I did want to flag, the 7702 poll on the CL side because it came up at other places this week but yeah, all things before we move to that 

**Mario**
* I've been working on some tests on the east side. It's a little bit hard to pin down exactly what behavior we want to see, but I'm going to try to keep, the the expected behavior to like some logical stuff that, that is not including, a transaction that would make the block invalid and such stuff. But, but, yeah, we're working on it. I'm going to be running some tests, on hive this this week. If I find anything, I will try to ping the clients with information. Yeah 

**Stokes**
* All right. these tests are for 7702 are another IP. 

**Mario**
* Yeah, exactly. For seven, seven two. yeah. And I say the issues that, I mean, this these tests are it's tricky to pin down exactly the behavior that we expect from the clients because there's nowhere in the, in the specification that says, okay, you have to reject this, this, this type for transactions. Once they, they, you have another transaction that is not type or, or whatever that that kind of logic is never is not specified anywhere. And I think that's fine. but I think we can try to still make some tests.
* Even with the, without this, this specification, if it's not possible, I'm gonna I'm gonna see if I can find issues anyway, it just means that we might not be able to merge, tests to to east, for example, but, but, yeah, I'm gonna try it out to see. See what the what the outcome is. Yeah 

**Stokes**
* Okay. Thanks. And, yeah, from my understanding, it sounds like all clients will want some special rules for 7702, around handling these transactions in the mempool. Right now, it sounds like there's partial support. it would be good to hear from different clients that are on the call, how much they're ready for this. But as far as I know, that was kind of the last, big open question for Pectra My client says here in the chat, Geth pending PR So, like, client, would would this PR basically block a extra release, say, like a testnet release for Geth 

**Lightclient**
* I think we're a little split on whether it would. Personally, I would really prefer to have this on our testnet release. I think it's not great to make the release and then continue iterating on some pretty core pieces of Petra, and then make a main net release that really hasn't had time to sit on the test nuts a lot. Like, we're we're closing in on merging this PR so it should be around next week. I think that the times that were proposed kind of makes sense to us. But yeah, my preference is definitely to have this in before we release 

**Stokes**
* Yeah, that makes sense. 

**Mario**
* I would encourage other Ells to go into this PR because it has some test cases in it, and I don't. I'm not saying that these test cases should apply to the rest of the clients, but it's important to at least think about it. And it's fine if you don't end up with the same logic. But just to think about it, it would be nice to have some feedback. Also, please go into the R&D, R&D discord into the testing, and just chime in with your testing scenarios that you would like to see test tested in your in your clients. Yeah 

**Stokes**
* Cool. And it does tee us up for the next agenda item here, which is testnet fork timing. So there are at least two comments here to address. Tim has some candidates here. Let me just grab a link to this comment so everyone can look at it And essentially they're kind of all downstream of when we can get client testnet releases out. So there's a suggestion if we can do this by February 10th, which I believe is next Monday. then slots for Levski and Sepolia and then a plus 30 day minute slot and then suggestions for February 13th releases February 17th releases the plus 30 day maintenance slot here came from another comment by Lee Derek, and I guess I'll grab a link as well just so people have it handy. That's here.
* So yeah, the request was essentially saying like, hey, you know, l2's even applications. there's been some comments around this as well from, say, Lido and different staking pools. essentially people using the L1 want some time, some lead time between when we have, you know, our testnet progression and mainnet. And the request was to basically say, okay, 30 days from the last testnet fork is when we would set the mainnet fork at the earliest. So that's the context for Tim. Suggestions here. And there's I guess two questions here. First is like, do we feel like this 30 day buffer is good? Like maybe, you know, we could pipeline things a bit to have like a shorter amount of time in between testnet and mainnet? if not, then we have the 30 days here and then otherwise. The big question, I think for people today is when they feel comfortable getting client releases out.
* And there are a number of comments on the issue yeah. It might be hard to summarize them all, but it looks like generally either option one or option two in this comment that Tim has. So that would be releases by the 10th or February 13th. It does sound like many people feel February 10th would be a bit aggressive. does anyone want to chime in for their client 

**Sean**
* So for lighthouse, I think it would be tough for us to get a release out by the 10th. So we were suggesting that 13th, we have like that one API fix, and we have another performance fix that we want to get in on the Testnets 

**Stokes**
* Okay then if we go for the 13th. Yeah. There's some other comments in the chat here around the 13th. So yeah. Is anyone not okay with the 13th to have testnet releases And so to be clear, February 13th let me just double check my calendar I believe that's next ACDE. So yeah one week from now. And yeah that would mean having to palleschi. And Sepolia works for Petra 

**Tim**
* The 13th. Yeah. And just to be clear, the minute slots I put there is like a placeholder. But I wouldn't expect us to put this in the release. It was just to show if we wait 30 days, you know. What's the earliest decent maintenance slot? but. So then our next Alcor devs, we would announce all the client releases, and then hopefully by the end of that day, if not early on the Friday, we'll have the blog post out with everyone's releases 

**Stokes**
* Great. Yeah, sounds good to me. And generally people are okay with 13th, so let's do that So one week, be ready by next acdeThen Derek here, is touching on the other comments here with the 30 day buffer. How do people feel about this? there was another comment by Frederic that from a security perspective, this is a pretty good yeah. Anyone want to try to shorten this or, do we feel like that's a good amount of time And maybe just to make this concrete going off the timelines here, releases next Thursday would mean, minute slots, say, on April 8th. So that'd be extra minute Does anyone want to try to be more aggressive with the timeline, or do we feel good about that 
* So Paul has a comment here that's dependent on the test night. So this is all assuming that the test nets go out. And obviously if there's an issue we'll have to reorient. But in the optimistic case we would do the test nets. They work great. And then we'd move on to midnight 30 days later Tim says on March 6th, we pick the slot right? 

**Tim**
* So assuming with the schedule, like we fork Sepolia on March the 5th, it goes well then Alcor devs is the next day. On the sixth we can agree on the slot. Assuming everything goes well, we can use what I have here already. and that would give people like 31 day or whatever to yeah, to update 

**Stokes**
* Yeah, that sounds good. One question is, if that's enough time to assess the sepolia because it'd only be like one day. 

**Tim**
* Is there something about this fork that will uniquely take time to find out on Sepolia that we wouldn't have seen on Holeski 

**Stokes**
* One thing we could imagine is just testing all of the different features, and there's a number of them right. Sure. How much we want to do, like aggressive red teaming on sepolio right at the fork boundary 

**Tim**
* Yeah. I think we should probably test this on Hoski in the week before, but like And yeah, 7702. But my sense is if we wait for everyone to be ready to support 7702, we're only going to fork next year. and that's been effectively out. You know, we've had the devnet since devcon that people can use. So I suspect not everything. We'll have 7702 support on the day of the fork, but it's still better to fork earlier rather than later. 

**Stokes**
* Yeah I agree. So yeah, I mean let's do that. Let's say, what was that the fifth. And then yeah, we have the call the next day and can make a call there if we feel, yeah, palleschi is kind of weird or we feel something comes up in the meantime that would want us to wait a little bit to watch the polio. We can do that. But it sounds like we should tentatively plan for, calling that Then And yeah, Frederick says, yeah, we could always adjust it if we need to 

**Stokes**
* We're so close to Petra. Very exciting Great. Okay, so client releases, in a week and for test nets and. Yeah, then we'll keep moving along Any other points on Petra? We should discuss right now Then we will move on. So the next set of items are around Pareto's scaling the blobs. I think there have been some pretty exciting developments with deep nets there. would anyone be able to give an update on Devnet for. I think that's one that launched recently or did launch. I couldn't make the breakout this week 

**Parithosh**
* Yeah, I can give an update on that. so we've been doing, devnet for testing, mostly locally and on kurtosis, and we've had a few runs running over multiple days, and it's been quite good, and stable. And we decided yesterday to then launch the public devnet. So devnet for I've been trying to get that up and running today, and I'm close, but it might happen again a few hours after this call or so, and I'll post information on the PeerDAS testing channel. But essentially it's it's exactly what we have on kurtosis. So it should be fine 

**Stokes**
* And there were plans to then move to Devnet five assuming that Devnet four is good. any blockers there that we should surface right now 

**Parithosh**
* I think the main change is validator custody. And we're still figuring out what are the changes we want to plan for in Devnet five. But I think we're still discussing what changes would exist there 

**Stokes**
* Okay, great. Well, I'm glad to see progress. And yeah, we'll be waiting to see how Devnet four goes. Anything else then on PeerDAS for the moment 

**Sean**
* Yeah. So Jimmy asked me to bring up a couple of things. one was the idea of shifting proof building responsibilities to the transaction sender Jimmy, from Jimmy's point of view, is important for this so that we could scale the number of blobs in pure. Does past 16. the transaction sender would build kzg proofs, and sell proofs. Oh, right. Now, I think kcg proofs are built by transaction sender, but sell proofs are built by CLS. and there's a computation bottleneck here and if the transaction sender is computing cell proofs, we can shave off the proof computation time during block proposal so yeah, wanted to raise that and then also wanted to discuss the idea of blob parameter only forks because that's another thing that would allow us to, I guess, start with a lower blob, count on peer to us and increase it without having to wait for the next hard fork 

**Stokes**
* Yeah. We had discussed, this proof point at Devcon and I think. Yeah. Okay, so there's some notes here from Francesco and yeah, I think there were a few options here. The current situation is downstream of the fact that we didn't want to move this computation into the L, but especially if it is helpful given all of the block timings, then that's something we can explore for sure okay. Yeah. And Francesco, when you say they agreed with it, then you mean moving the cell proofs basically into the EL 

**Francesco**
* Yeah. I mean, at least whoever was in the breakout room at Devcon, I did not. No one raised any objection to that at the time. And then we also talked about it again in the distributed block building call and same thing No one had any objection to that 

**Stokes**
* Yeah. I mean, and again, I think the only real argument was just the separation of concerns between EL and CL because it brings a lot of cryptography into the EL that the CL kind of could handle on its own but yeah, as long as no one feels strongly about that point and this helps, especially scaling, I say we do it I think where I am on this is just waiting to see how the deep nets go with pure dos. And yeah, if we get to a place where we want to start with a lower count, then what's theoretically possible, then something like BPO, I think would make a lot of sense, essentially essentially pure dos with like a smaller number and then just, you know, best case, we do commit to say like, you know, every few months we bump up the ball count by this amount.
* And then, yeah, have this sort of like on rails upgrade pipeline up until whatever we're comfortable with for the PeerDas Max We have had a little time since this BPO idea was introduced. Anyone else have has anyone else had any more thoughts about this Do we generally feel good with the idea I'll ask a question. Do we have a target at a time for blobs? Yeah, I think the specifics will kind of depend on how the nets go So paradox itself, because it gives us a sort of theoretical, upper bound. And what I would like is just to hurt us with that number 
* If for some reason we don't feel comfortable with that, then, yeah, we'll need to find a different option. And BPO is like a good tool if we need to do something that scales 
* Dustin, I don't really follow your comment here Maybe you're applying to Paul 

**Dustin**
* No, sorry. I'll clarify that. The thing with the scaling is at least my understanding, and this is one been one of the tensions for going back, I guess, a while with the with the proposer still has to send enough out. Who or whoever sends the block out. Somebody has to send all of the I mean, whether they be a sufficient number of columns or blobs, it that still has to happen. And currently pure DOS is set at a factor of two. So you need half the columns to reconstruct everything. 64 of the 128, which means that this it's the factor of eight, still doesn't really, that can help in certain cases, but it doesn't account for, like, somebody needs to have the bandwidth. Yeah Okay 

**Stokes**
* Yeah. And I guess that was another big vertical here was essentially the, the question of local block building. And I think there's a number of solutions there around how we'd still be able to scale the blobs while preserving some amount of local building. There was this idea of like having some flag in the clients that as a local node, you could set the maximum that you want. In the event that, you know pure DOS and the protocol scales past what you have available for your local bandwidth So there are diverging opinions on that in the past, but something else to keep on our radar as we move into pure dos R&D Okay anything else on pure Dos? Otherwise, I think we keep training on the nets and hopefully that gives us more information to keep moving forward The next on the agenda.
* So that was pure dos. And then yeah we had a number of things around research spec different things to call out. The first one should be pretty brief. Just an announcement around hardware and bandwidth requirements. So Kevin and others have been working on this EIP, which I would imagine is an informational IP. I'll grab this link here, but essentially it just, puts down in text recommendations for node requirements and yeah. Kev, was there anything to add here? I think mainly the call out was just to take another look at this, PR 

**Kevaundray**
* Yeah. I wanted to just, see what people were saying about the Max blobs flag that we had in the previous act in, because, yeah, once we have max blobs flag, then we wouldn't need to sort of constrain the network to the bandwidth of local block builders who are home staking 

**Stokes**
* Okay, so does anyone here oppose this idea moving forward with the max blob swap 

**Paul**
* I think I put something on the PR just because I'd previously suggested something similar. so basically for local block building and, it got met with a bit of resistance, but I'm not against the idea generally 

**Stokes**
* Ahmed

**Ahmed**
* Yeah, I'm also not against that idea in general. I'm just like against any trend that, that has been surfacing a little bit lately about, disregarding, solar stickers and doing local block building or, not prioritizing local block building because it's dying out. Anyways, I do believe that, having a resilient network requires that local block building falling back to local block building is always available, regardless of whatever mechanism. And, if we if this is something that is planned for, for, for spectra, then, then then then that, that maybe is fine. but if it is something that is planned for a more aggressive push on blobs, for, for for Osaka, for example.
* Then I would say that we need a more permanent solution to this problem, something that would still allow solo Stakers and home stakers to, participate in local block building if they had, if they ever have to without compromising on their, fees that that they receive from, from from block potential blobs that they can post on, on on the, on the, on this and this is. Yeah. the, the this is why one of the things that I have also done in this call, I think you were getting at it later on is I proposed DPS for, for Sakai. I understand that, it's not a small thing to do or, that it's easy to do. fork. It's a very complex, but it could be. It is a solution to a lot of problems. And it also have a lot of advantages, that other, research and, and incidents have shown us, before. I wouldn't want to waste more time of everyone's time on this, so I'll stop here. 

**Stokes**
* Okay. Thanks 

**Stokes**
* Ansgar, you had your hand up. Although it just went away. 

**Ansgar**
* Yeah, just. I mean, I just want to say I think they are more minimally invasive changes we could make to also retain local block building capabilities. I put one a sketch of one idea in the chat I mean, I think EIPs in general seems great. I'm not convinced we should have it, considered,  necessarily, just because it seems like too complex. But, yeah, I don't think that a good argument for it would would be specifically the local building, because I think they are much lighter weight solutions for that 

**Stokes**
* Terence had a question around the Max blobs flag. Have we brought this up in a roll call? it might affect L2 in some subtle way. Yeah Has has this come up? Does anyone know in roll call we have another roll call next week so we can bring it up there and then report back Nice. Yeah. I think running it by L2 is there would be nice. Terence, was there something specific you had in mind? 

**Terence**
* No, it's just today the blob pricing is determined. Right. You know exactly what the target Max is. So as a layer two, I can look at the man pool. I can have some predictive, algorithm. I can predict the next few slots of the block price. Then I can kind of, batch post, optimally. Right. But with this, it's like, I probably do not know who are the validators that's constraining blobs. That's proposing the next epoch Because of that, the blob pricing may slightly vary in in some way. I'm not sure this is like a blocker blocker, but it will be nice to let the consumer of the blobs know that. And I think layer two are the biggest consumers so far 

**Stokes**
* Yeah, for sure. And I guess this is in like in the average case it wouldn't really affect l uh L2 right 

**Kevaundray**
* Because most of the blocks that are being built are not by local block builders. 

**Terence**
* Yeah, for sure, but you can imagine today we have a finality incident, right. And say today we're missing more than three slots per epoch. Then things will change. And I'm saying that the layer two should know this. Basically Yeah. 

**Kevaundray**
* Right. Okay. I see 

**Ahmad**
* Hey, quick question, you guys. so I brought up before about, like open references or guides, or really just like, data pools, statistic pools, whatever you want to call it in terms of people being able to, to reference the guidance, for something like the, the block flag, I mean, excuse me, the blob flag, the max blob flag that we're discussing. Is there something like that? Like, for example, I know that my bandwidth is only supports like 24, 25mbps down or so and whatever. Let's say maybe 25 up. this is what would make sense for me to, set my max blob size to be rather than it just seems like right now we're like, okay, perhaps this flag will be helpful in us limiting. But then there's the question of how much knowledge and experience and, and, info that people have in terms of how to properly set that flag 

**Kevaundray**
* Right. I agree with this. I think we need something like that in general. essentially, what is the maximum amount we can go to for the protocol based on these assumptions? so I think we'd need that sort of Anyways 

**Stokes**
* Right. I think he was asking like, if we essentially, how would I know? As I say, solo staker, how to set this flag. So the thing is, blobs are fixed size. So it should be a pretty straightforward calculation. And you know, clients can put out guidance if you know how much bandwidth you have locally to dedicate to getting blobs out, then it should map really directly into some concrete number that would be your max. Then the idea is just as you go to boot up your client, you put in that number and then you should be good to go 

**Ahmad**
* Cool,sounds good 

**Kevaundray**
* I'm wondering if I haven't heard from Aragon on this. is there anyone from Aragon that can say something 

**Stokes**
* Here. Just looking for their feedback on Yeah, just for the max blobs or for. Okay Is anyone from Aragon on the call? I don't see anyone Okay, we'll have to reach out some other way. Kev but, yeah, it would be good to get their input And. Right, like, I'm, I was referencing. So we did have a PR merge to set PFI for Fujisaka for EIP 7732, which is the EIP for EPBS I'll just grab a link here in case anyone wants it. It's 9291 on the IPS repo. And yeah, I don't really want to get into like scoping today. we should focus on before we open that thread in earnest. but yeah, so it is PFI and. Yeah, um I guess just. Yeah, that's a heads up And otherwise, we do have some time. So I did want to bring up at least the conversation of these petravic retrospectives. Tim started a thread on Ethereum magicians and has been collecting input. There have been a number of really interesting responses, so I would encourage everyone to go read through this thread.
* And there have been a number of client dev responses, at various points here, I don't think we have everyone, but since we do have some time today, if there's any sort of, early takeaways or points around Petra and how that might inform how we move forward with Hardfork planning and implementation R&D, all of the above now would be a good time to get into that I think a big takeaway that a number of people had was just in terms of scoping, being more, disciplined around how we actually do this. So, you know, one thing you could imagine is that we basically. Oh, yeah. So like one concrete idea that I kind of like would basically be saying by you know, fork n, the scope of N plus one is already set.
* And then what that means is we don't have to like, mix in the concerns of determining a hard fork while we're also building the current hard fork, which this is one thing we kind of did with Petra. And it's, seems to lead to distractions so that's some feedback I've seen from many people, actually.
* And I think it's something we should really consider. I will flag Tim's comment here. It would be nice if we could get all the retros by next week. So if you're a client team and you're listening, if you could please add your thoughts and I'll again, I'll direct you to this theory Magicians thread to get some more information there. But essentially, once we have all these, it'd be nice to kind of like go through some summary. I would even suggest taking like one specific acid and dedicating and adjust to that. And yeah, then the idea would be to like pull out, concrete suggestions for how to improve acid moving forward so that we can, yeah, keep things smooth and improve the protocol Any other Petra retrospective points that anyone would like to get into at the moment 

**Tim**
* Maybe. Yeah. Like, one as people, send their retros  if we are going to seriously consider, like, you know finalizing the scope of one fork as we start, or as we ship it and as we ship the previous one. Sorry. And then open the door for, for, the next fork. In practice, this means the scope for Lusaka would be, like, frozen. And so I think it would be good for client teams to start reflecting on what that implies. my sense when I talk with people about this is everyone agrees in the abstract that, yes, this would be great. And then two minutes after they propose an EIP that they obviously want in the fork because it's important. and so this is kind of the issue we always run into where, it's yeah, like if we want to make this commitment, you know, right now there's two things in Lusaka and this means everything else would go to the next fork And we should, you know, we're shipping Petra in the next, basically month or two. So we should, um. Yeah, finalize that 

**Stokes**
* Right. So, you know, yeah, to play it out, it would be like essentially going with the CFI that we have. Right, or sorry, CFI Lusaka that we have right now. Then anything around other IPS would go into Amsterdam. And the idea would be like, we can turn on Lusaka. And then in parallel, perhaps even in some like slightly different forhave the conversations around, which actually IPS go into Amsterdam The question 

**Luaksz**
* One comment from me as a core dev is that it's sometimes hard to judge those EIP, especially on their maturity of aspects, etc. because sometimes we, include something or consider something, but then it then changes a few times more later and, that's something good to try to having to come up with some assessment of, of specs, finality of EIPs. And I know you always have last minute changes sometimes, but it might be helpful to like to, to have this longer, plan forward. So that's something to consider 

**Stokes**
* Right. Yeah. I mean, it does seem to be a pretty strict improvement. And yeah, the idea would be to, like, have fork scoping discussions for the next fork after the current fork. obviously, as we like, get into the R&D process, things change. But the idea would be to limit the scope of what we're talking about with respect to like these sorts of changes to just a small set and then not also have to bring in the conversation, oh, what if we did, you know, this new EIP that we have dev nets for on the side, should that come into this fork. And yeah, the the whole point is just to be more focused. And I have high conviction that more focus will make us move faster Yeah. Trent has another comment. And forcing basically yours or co spec and limitations. Yeah that would definitely help. A big one is testing.
* So we should be very strict about no EIPs possibly or even PFI without test, but definitely CFI Or any other preliminary thoughts If not, then right. any client teams who haven't put together a retrospective, please try to do so by next week. We'll keep moving there and otherwise.
* In the meantime, if you have a few moments, take a look at the magician's thread. There's a lot of good content there Cool. Let me grab the agenda over here. What else do we have? Okay. Yeah. Fredrik wanted to announce, Petra bug bounty hackathon. Fredrik, would you like to say some words about that? Yeah. So usually for the hard forks, we add A2X multiplier, to the bug bounty program in order to get more people to basically review the, the code specific to the the hard 

**Fredrik**
* In hopes that we will find issues before they go live. This time we're doing a bug bounty competition instead, with a $2 million with a pool of up to $2 million, depending on the findings And, we will be launching this after the, client releases are ready. So I guess sometime after the 13th, most likely Basically, what we would like, like our ask, is that client teams create this type of one pager type of document, which is describing where the various security researchers should look for changes specific to Petra in their client. this is basically just to make things a bit faster for the security researchers so they can quickly drill down on the code that's in scope of the competition because, non Petra code will be out of scope. So please try to find some time to do that. because it will mean that security researcher will have a easier time potentially finding issues with their clients.
* And on top of that, it would also be good if the if any dependencies that are being used by clients or the protocol, could do the same. So, if any dependencies being used have implemented changes specific to Pectra, then please do the same.
* And, I think the easiest way to distribute this is probably through the, R&D discord. And you can send me a private message if you want. I'm, Fredrik on there, and then I'll make sure that this is all compiled for the for the competition itself Thanks 

**Stokes**
* Great and when you say, I guess. Yeah. One question would be like, where could I go to follow the developments here just to get more information? Would there be like a ethereum.org blog post announcing this after client releases? 

**Fredrik**
* Yeah. Yeah, exactly. Yeah, we'll do that on the blog. we'll update the bounty ethereum.org, website to point to this competition as well. And we will make some, some tweets as well. So we'll try to get get the word out as much as possible. And of course, that's also something worth mentioning now that you say it. when we do run the competition, obviously if the, the clients were able to help push the word out, that would also be appreciated because we want as many people as possible to to see that the competition is ongoing and partake in the in the competition to find flaws before Pectra hits may not 

**Stokes**
* Yeah. Makes sense. Thank you Cool. So I think that was all we had on the agenda for the day. And let me just see if there are any more comments, but I think that's about it 
* Otherwise. Yeah. Okay. Anything else you would like to bring up Yeah. Have you ever get, get blobs question 

**Kevaundray**
* Yeah. So we've added get blobs and I've been getting mixed, answers about sort of how effective it is. Does anyone sort of have any ideas? because it ranges from the proposer or local block builder no longer needs to send out the blobs to. Maybe they need to send out half so yeah, I wanted to get some thoughts on get blobs. Oh yeah 

**Potuz**
* It's currently very effective. the time that you need to wait for Da availability for Da now on on blobs is almost zero. it would be much better, though, if the blocks would be sent earlier than the blobs so that we have even avoid bandwidth waste. But as of now, that feature has been reducing the amount of time that you need to wait for, for proving that the data was available to essentially zero on my local node here 

**Kevaundray**
* Oh, so that means that the. Yeah. So the only bandwidth needed is from the block itself. And is it worst case now it's like one megabyte. 

**Potuz**
* In the worst case for the block. So blocks are in average now 115 K bytes. I do not know what the worst case is though. 

**Kevaundray**
* Okay, I see okay. Yeah, that's super helpful I guess then what is the what is the limit on? Because obviously we can't just scale to like a million blobs. Like, what is the now bounding the limit on the number of blobs then if it's not the block, if it's not the blobs the mempool, it's a mempool. 

**Potuz**
* And this is dependent on else on how they implement it. So currently it seems that all blobs fit in all mempools and and your local node will have all of the blobs, because they are being published and published publicly but definitely this doesn't scale. So. Right okay, I see, yeah, but we don't have to like, I mean, why like it's very clearly easily possible for rollups to just like, send their blobs directly to block builders or something like, we can still keep the mempool for censorship resistance, but does it does every blob transaction have to go through the mempool? No, that's fine. But then the thing is that then they get blob feature that Kev is asking about will not be helpful for anyone right 

**Kevaundray**
* Oh I see, well, I guess if they send it to block builders, are we talking about via some MeV beast based strategy? because bandwidth, I guess, is no longer an issue in that case, either 

**Stokes**
* Well, it could still be on download, right? So imagine we have like a thousand blobs and maybe you're constrained on download 

**Kevaundray**
* Yeah, I think I computed the download. Uh I don't have the numbers up, but yeah 

**Stokes**
* I do have something to say Kev. Okay 

**Stokes**
* I did want to service Ansgar's comment here. At least the question around. Yeah, having clients send out the block before the blobs, because, yeah, like we're saying, this get blobs thing doesn't actually really help without this. and I think different 

**Stokes**
* Clients either do blobs before block or maybe some do block before blobs. But it would be nice to standardize this 

**Stokes**
* Do clients have a sense of how much of it would be to switch to blob before blobs I think the builder and the relay sort of like dominate here, so I don't think it's an issue for clients. I mean, we can, but I think whatever we do is going to be mostly relevant for the network Just because most blocks go through relays. 

**Kevaundray**
* But I think for the average case, average case size of a block, it's okay. Like the upload speed, needed is like 3.2. It's just the worst case is, not great. From what I competed assuming you need to get the block out and you need to send the block out to eight peers and two seconds. 
 
**Enrico**
* I just want to say that. Yeah, Teko is already sending, blocks before blobs when it's time to publish. And the essentially, we are doing, like. So we send a block and we start blobs sending out, as soon as we get the confirmation that we have successfully sent the block over at least one peer, this is the current default behavior Right 

**Stokes**
* There's a comment. Lodestar publishes the blobs before the block. Was there a reason for doing it this way, or would you be interested in doing it the other way 

**Enrico**
* I guess the blob before block is more on the relay side behavior. Well, this is more on the, solo sticker, local building behavior side of things 

**Stokes**
* Right. Which kind of suggests you might want some way to have the relay customize versus a local builder 

**Enrico**
* Yeah, maybe it makes sense to have maybe options that say it depends on who are you and which part of the network you're playing with Having one strategy and the or the other one could be, a good option to have on all clients 

**Stokes**
* Any other comments or questions If not, we can go ahead and wrap the call And everyone is very busy with Pectra And yeah, if there's nothing else, then client releases, please have those ready by, a week from now. So next ACDE and yeah, we will get Pectra to minute I think, Tim, you might have had a PSA here. Please move all your EIPs to last call 

**Tim**
* Yes, so this way we can finalize the specs, but. 

**Stokes**
* Any EIP authors? please go do that as part of the EIP process. Move the status to last call. And. Yeah. Otherwise I think that's it for the day. Thank you



---- 


### Attendees
* Stokes
* Tim
* Arnetheduck
* Marek
* Lance
* Micah
* Paul Hauner
* Ben Edgington
* Loin Dapplion
* Terence
* Enrico Del Fante
* Pooja Ranjan
* Hsiao-Wei Wang
* Saulius Grigaitis 
* Roberto B
* Olegjakushkin
* Chris Hager
* Stokes
* Dankrad Feist
* Caspar Schwarz
* Seananderson
* Andrew
* Crypdough.eth
* Zahary
* Matt Nelson
* George Avsetsin
* James HE
* Marius
* Ansgar Dietrichs
* Lightclient
* Stefan Bratanov
* Afri 
* Ahmad Bitar
* Lightclient
* Nishant
* Gabi
* Pari
* Jimmy Chen
* Gajinder
* Ruben
* Mikhail
* Zahary
* Daniel Lehrner
* Andrew
* Daniel Lehrner
* Fredrik
* Kasey Kirkham
* Protolambda
* Cayman Nava
* Stefan Bratanov
* Ziad Ghali
* Barnabas Busa
* Potuz
* Trent
* Jesse Pollak


**Next meeting**
* [Thursday 2025/2/20 at 14:00 UTC](https://github.com/ethereum/pm/issues/1280)
