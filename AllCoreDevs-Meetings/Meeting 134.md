# Ethereum Core Devs Meeting #134
### Meeting Date/Time: Friday, March 18th, 2022 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [GitHub Agenda](https://github.com/ethereum/pm/issues/492)
### [Video of the meeting](https://www.youtube.com/watch?v=Lbsjw-lzMIw)
### Moderator: Tim Bieko
### Notes: Avishek Kumar
### Summary
## Decisions Made
|Action/ Decision Item | Description |
| ------------- | ----------- |
| **1**   | Need more testing infrastructure and things like running a shadow forks of gorli and running through the transition. |      
| **2**   | Mikhail will submit a PR or update the existing one for safe head |
| **3** | EIP-4895 move to CFI  |
---
 
# Merge Updates

**Tim Beiko**: Good Morning Everyone welcome to our core dev's number 134. I have a couple of things on the agenda today, I think, by far the biggest one is Kiln and kind of going through what happened and making sure we figure out next steps from here, and then we have some updates on some Shanghai proposals. So Alex has some updates on beacon chain withdrawals. There's also someone else. I'm sorry I'm blanking on their name who left a comment and wanted to discuss something about partial withdrawals and then their protocol had a bunch of updates about the EIP 4844 and then, if we still have time at the end. I had a proposal about how we can harmonise the query EIP process and the executable specs that are being worked on and so to kick us off. Yeah Pari I will put you, but maybe somebody else is in a better position but someone kind of wants to walk through high level.What happened through the kiln merge, and then we can probably hear from a few different client teams kind of specifically about  what's not on their side.

## [Kiln Updates](https://hackmd.io/@n0ble/kiln-spec) 🔥🧱 


**Pari**: Sure, I can give a high level overview, so we had to kiln test net-launched last the proof of work portion of it launched last week on Wednesday and we had the proof of stake beacon chain launched last week on Friday, the match itself happened on Tuesday, a bit earlier than expected. We had to delay the merge once by using the terminal override. terminal total difficulty overnight flag and that was unexpected, but that exercise  seemed to have worked perfectly. All the clients respected it and we noticed no weird behaviour from anyone.However, once the merge transition actually happens, a few clients have issues with block proposals and or syncing.I let the individual client teams go into detail later on, substandard networks him stable, I think there are still one or two clients that have some issues, but they they all seem to be minor and should be fixed relatively soon.

**Tim Beiko**:  Got it,thanks one thing I am curious about the status of the block explorers. I know there were some issues with the blocking spurs like shorty around the merge and being kind of where we're lagging for a while and can you just give us a quick update if you know what happened there.

**Pari**: Yeah so we run a fourth version of the beacon chain block explorer and one of the payloads exactly the execution payload was set up in instead of begin.This wasn't an issue in the previous ones, because well the base feedback as didn't wasn't too high, but apparently in this for the number of transactions, went to high and in this one, it was high, so it just overflowed. I think it's pretty much the same thing that tripped up the prysm that tripped up the explorer but it's fixed now and the explorer just takes a long time to sync, so I think we're still stuck about lagging by doing something.

**Tim Beiko**: Okay, great I apologise to everyone on the live stream, there was an obs issue and only my voice was audible so i'll recap with Pari said 30 seconds and we also have the zoom transcript which we can add to the notes for version but basically would kiln launched under proof of work last Wednesday. The proof of stake beacon chain went live last Friday. There was too much mining and the network, so we had to use a dd override feature in clients which worked well and allow the delay of the actual merge on the network, which still happens today. There were a couple issues on the merge testnet on block production and syncing and we'll dive into the specific ones from clients or after. But the network we're still finalising and it's still doing something today, and if there were some issues also with the block explore some integer overflow issues, and these have been fixed, but block explorers are still lagging importing all the data. Anyone else have just general comments on kiln before we kind of dive into the specific client issue.okay go ahead

**Micah Zoltu**:  Will we be discussing perhaps after the client issue  whether we want to do another Dev test net before the public test net given that failure or not.

**Tim Beiko**: Yes, I think, actually, We might maybe do that now like I know Marius Pari and I and others have talked about shadow for kiln  gorli next week, basically  So I think the short answer is yes yeah.

**Danny**: Yeah, I think, given that the kiln at least as we believe the specs will be is future complete and we've kind of solicited a lot of the Community to jump in on it. I would like to just kind of keep that as quote the public test net right now and continue to ask people to do full. You know application deployments and things like that I would say, certainly, we should do another test net, you know call another transition and maybe they just call it a definite and and have an invite and i'm an advocate for. You know, shadow forking Gorli and sepoila  every few days for the next few months.You know if we can automate that, in a way that kind of just shows us the latest builds continue to work and and block production is happening, and all that stuff that's going on, I think away a lot of the concerns.

**Tim Beiko**: Right and yeah I shall be more confident that this in about five minutes, but, as I understand it, right now, none of the issues we found on kiln are like spec issues. They all seem to be client implementation issues, so to me that says, like you know we don't need a different public test net, which runs like an updated version of the merge specs we need, as I understand, like clients to obviously fix the issues that they found and we obviously want to test that on devnet’s but yeah unless I think there's like a significant change to spec. It seems like we could just keep kiln as is and obviously have clients issue new releases, which will work on the network. There is a question in the chat about mev boost. I don't think it's been used yet and we reached out to the flashbots teams this week to chat with them about that. cool I guess yeah okay to dive into the client stuff a bit more offsides with the first one that comes to mind was that there was a prym guess kind of in compatibility around the encoding of values like the base sheet, I know, if anyone from prysm is on. I am here Terence. Yeah Terence wants to give us a quick overview of what would happen.

**Terence(prysmatic labs)**: Yeah, it sounds good. Thanks for having me here, such a high level summary execution layer used edn and consensus layer used to edn so when we have this custom implementation for the above so whenever we Marshall and and the Marshal specifically that field, we have to be careful to basically reverse the cycle. We missed that for the base fee per gasfield and unfortunately we didn't catch them for the previous testnet because the basic progress was quite low and there was not actually people reporting only the videos are broken so should we fix that first.

**Tim Beiko**: So we are sorry, you say something.

**Terence(prysmatic labs)**: Yeah in the chat people are saying the audio.yeah.

**Tim Beiko**: I don't know sorry yeah everything's turned on. I will just upload the zoom recording after.

**Terence(prysmatic labs)**: Okay, sounds good. Okay I am gonna keep going. Then basically the previous test net was able to catch that because the base of your guests was quite low so  yeah I was quite happy to realise this bug so use the corrective action I posted a postmortem  on Twitter. I am sure most of you all have seen it but a high level summary for that is that we will be using our testing infrastructure. So right now we are working on our differential buzzer for all the API endpoints. meaning that we will aim to be hundred percent compliant with older merges and for our end to end testing, we are also adding being the transaction generator, and so we can make sure to send all the exotic Transaction  to make sure the base fee for gas does not remain low and stuff so yeah that's the High Level summary.

**Tim Beiko**: Thanks and Marius. I understand there was no issue on the geth side. Right? It was just the Geth Prysm combination, but I guess it was working right.

**Marius Van Der Wijden (M)**: Right, yes, and like we saw this bug because the guest prysm didn't.create any blocks and we only noticed it because guest prysm is such a large majority of the network and that's where we only saw geth prysm but it's probably it was probably also on geth Besu and geth nethermind  and so it has nothing to do with geth. Piece of prsm is out of mind.

**Tim Beiko**: yeah yeah that makes sense. Okay, thanks thanks for sharing. Any questions for people on that.

**Danny**: Yeah I guess in not just the prysm CI, we need to make sure that we have sufficient transaction activity, and you know kurtosis nightly builds and some of the other testing, we have as well. Also, I will say I was looking at the base fee on Gorli and I don't believe it's always above 255. So we might consider when we do shadow fork to make sure that there's sufficient activity on there as well.

**Tim Beiko**: Yes, Marius with your transaction Fuzzer works on Gorli if you have enough.

**Marius Van Der Wijden (M)**: Sure so  unfortunately  Someone stole all of my Gorli ETH. Send it back. If you're listening to this call, and you send it back, I could test. So one thing that I wanted to talk about was that I think we left insights a bit into which clients were like missing the slots and which clients were like not proposing blocks or not testing and. I think we need to up our game there so that we can like it. See the bad client the odd one out way quicker than we then did just on Tuesday.

**Tim Beiko**: Yes, agreed, I know, there was an idea and I think it was Pari's ideas like maybe we build, like devnet which have each combination of client as like a super majority client, so that if we those issues that show up kind of the the show up in the network stops finalising and I don't know if that would catch.If that would catch the bulk of it.

**Danny**: Is that a suggestion through the nightly builds?

**Pari**: Yeah exactly so one variation of the nightly build is just to have all clients together, and the second variation is to just have a combination of every client has a super majority and we could just do this parallel in it, so if a supermajority client fails it's a lot louder whereas if  it's just a minor, it can be my friend even notice, an issue.

**Danny**: Yeah I mean if that's a tractable thing to do at this point, I would say.

**Pari**: yeah.

**Danny**: Definitely anything like that  we can do to kind of continuously get a view into things working is really good at this point.

**Terence(prysmatic labs)**: I will save for the building blocks for you can tie them proposer into like a name, so if we look at, if we look at a proposer, for example, if you see the proposal you actually says prysm, lighthouse blah blah blah, so we probably can do that for our kiln as well.

**Pari**: Yeah I will look into that one as well, and one other nice thing that Tim from a testing vouch worked on updatingEth2. So you can now process a block or an epoch as soon as it comes out and it will list out all the proposal indexes that have failed or missing attstations or syn committee participation. So we no longer have to wait for the explorer to update. The explorer will always be a bit slow, but since this tool is actively indexing you have to call it, it will be a lot faster and should be easier to debug stuff.

**Tim Beiko**: Nice, I think there were also some issues on the kiln between basically besu and teku. If that's right. That is, anyone from your team wants to give an update.

**Gary Schulte**: Yeah I can. I can say that there's a case that we weren't expecting where the terminal block was finalised and our logic to check that we were descending from a valid terminal block wasn't considering that the block itself is being finalised was the terminal block, so there were some cases where basically, we just sit there at that tdd. So we have got a PR for that and also we had some issues with backwards sync which we have a matching backwards think PR that is merging today, so we should have. 22.1.3 snapshot which is what we are going to recommend for using the kiln. But yeah that's the issue that we were having and encountered and there were a couple of reports of basically sitting a TTD, for that reason.

**Tim Beiko**: Got it, so the fact that it was basically there was nothing on the teku and right, it was just a coincidence. And then I think nethermind also had an issue with you. Is that correct?

**Marek Moraczyński**:  Yeah, some issues for some notes after the transition require restart to make it work. So after the restart they are working fine.We are still investigating it and to make sure that it was fixed, we need to experiment a bit with transitions. We found a few potential places, but still investigated. One piece of good news is that Marius ran a differential fuzzer between geth and nethermind. So fuzzer is sending random requests to execution clients and comparing heads and seems that both clients behave in the same way.

**Tim Beiko**: Awesome. And I know Erigon, as well, I think of you. You knew that Erigon would probably have some issues during the transition, but still run it. Any way you want to give a quick update on like yeah what you learn from this and where you're at right now.

**Andrew Ashikhmin**: So there was one issue in Erigon actually related to the engine as well that was fixed, but so we were incorrectly sending an invited block hash for a valid block but I think teku was incorrectly ignoring our incorrect invalid block hash and he was keeping resending the same block though we sent an invited block hash. Also because Erigon was quite late to the party, I personally would like more time so we are still refactoring our sync code and during that kiln with like quite a few issues discovered during kiln though maybe not like theoretically blocking but still I would suggest, not to rush the merge.Take  it slowly, spend more time on testing more like match transitions and things like that. I personally would like to spend more time understanding how sync works on the consensus layer side, the difference between optimistic, non optimistic sync performance, implications, think about it test because i'm worried like what we were discussing the chat really the most recently is that  What a kind of the performance implications of like consensus layer sending us when you have to sync something and then consensus sends a block and just have every block to the execution layer is it Okay, is it not Okay, maybe it is OK, but I personally would like to spend some more time thinking about it and and also testing it.

**Tim Beiko**: Yeah thanks for sharing with others. I don't find teams, I think those were all the ones that kind of had issues on kiln specifically but did I miss anyone. Okay, I guess, not. So I guess so in terms of next steps from here, obviously I think it's clear to everyone that we need more testing infrastructure and things like running a shadow forks of gorli and running through the transition. A couple more times and I think in terms of like you know rushing to merge or not, the timelines and we probably have another month or so before we need to make a call about whether we want to move the test nets or whether  we're not ready for it up, and so I feel like that the next step is probably to spend obviously, the next two weeks, and then possibly next four weeks and improving the testing infrastructure, finding these issues and you know growing confidence in our  implementations and then we can probably make a call about you know, do we feel comfortable moving this through the test nets or not and if not, then I think at that point it's like we we might have to discuss potentially pushing back difficulty bomb and  I do think we probably still have like one month basically until we have to make that call and a high level, I think that the bomb is going to start begin.

 You know, early June around mid June June and July, we would probably have like 14-15 second block times, which is high, but not manageable and late July early August, assuming like things are the same, you probably are lucky he had like 17 or more and that's supposed to be. You know much greater delays and just considering the time it takes to generally go from the Test net  to the main net.. Yeah I think we basically have like about a month, where we can kind of grow our confidence in these implementations and then have to make a call and yeah I think you know, the more iteration cycles, we get a test of Shadow forking in that period the better.

**Marius Van Der Wijden (M)**: So one like one thing that I'm thinking about is like I don't think we like, I think we uncover a lot of facts. But we don't like that we don't really notice them. We don't really recognize them so like there was this sync aggregate attestation thingy whatever were like that was like at like 60% or something and then after two weeks  someone decided to look into it and it turned out that nethermind was. Prysm was just not sending something and I think that is like that is a bigger issue like I think with what we do trigger a lot of bugs and I'm pretty sure that we trigger the prysm. The prysm base fee is encoding back at least five times already, but we work, but we never recognized it as such, so I think we should spend more time building infrastructure to recognize these bugs and I would really urge all the client teams that if they see something funny on or something interesting on all of the on a test net or whatever, then they should reach out to the clients that they think are affected and then really look into it, instead of just saying Okay, there was there was pretty funny but if I restart my client and it's a way so it's like a non issue, and I think we do that way too often.

**Danny**: I think we could probably come up with something like a key indicator, 10 or so Key indicators for a testnet's health,  Right ? And it's not just the finality,  finality is good, you know that's what you hope to see always on the main net, even if there's some sort of issue with a client here there but there's other things like no one's looking at the sync aggregate thing because no one's really running light clients, and so it doesn't really matter and just kind of falls to the wayside, but that's an indicator that something's not right, so that there's the number of blocks per epoch. It  should be 32 almost all the time. There's the number, you know there's the finality. There's the amount of the percentage of attestation that is actually making on and so I would say, most of our monitoring and most of our integration testing should be looking at a number of these things rather than just finality, which I think we rely a bit too much on the two thirds metric there, we should obviously can let a lot of air through.

**Marek Moraczyński**: I think we should also think more about test cases for high because Mario the guy is doing great work with these tests and I think we should all try to add more test cases here.

**Danny**: I mean I'm definitely of the mind that at this point, if there's one or a half resource from each team that can work on testing devops and other things that we would be in a much better place come four weeks from now.

**Tim Beiko**: Yes, agreed, and I know that I don't think she's on the call but Frederick from the EF has been trying to gather people from different teams that coordinate all of that so and yeah hopefully like we can just have more people from each team, but also kind of be a bit more proactive and sharing this stuff that's being worked on, so that everybody's aware of what everybody else is working on. Oh Fredrik is here.

**Fredrik**: Yeah exactly yeah I sent that out so I message to the client teams, this one about it. So get moving.

**Tim Beiko**: Maybe just to touch back on one thing that Andrew brought up, like syncing and  bulk sending the blocks of the execution layer. I'm curious to check generally, how people feel about that, like is that something that can realistically be changed before to merge is that something that we might want to improve shortly after.

**Danny**: So it's something that can be leveraged like the execution layer can already leverage information to do whatever he wants here.The consensus layer if it's syncing and sending you bulk blocks means that it is not the head and it literally doesn't have a good piece of information for you to decide how to like do reversing in any sophisticated methods from the head and so it's walking into way forward and that's just the case, and so you can either execute as it does that or because you know. The current time in the world, you know that the consensus layer is not quite actually at the head. You can wait until the consensus there gets to the head and then do whatever sync techniques that you like to do at that point but there's kind of a  bit of a chicken egg problem here, you can you can lock step sync with them, or you can wait until they get to the head and then do whatever things that you want and there's this sufficient information to be able to make either those decisions.

**Tim Beiko**: That makes sense.

**Danny**: To talk  about more in some of the channels and stuff if people want to discuss different designs.

**Tim Beiko**: sweet yeah I think yeah it's been discussed a bunch so  we can keep kind of their conversation there and was there anything else that people wanted to discuss about kiln or merge, just like testing specifically.

**Mikhail Kalinin**: I would like to quickly discuss safe, unsafe and finalised tags.So there is a PR opens into the execution api,s repo that just that's finalised blocked back to the  json rpc and on the last call we decided not have saved for was a bit uncertain about that, and one of the suggestions, one of the one of the things that we may do for safe block, that is to use justify  block for it as a stopgap until we get see through implemented it's like a full proposal that was made by the Dankrad & Aditya.on this using justified block is pretty cheap from CI standpoint. so it just responded with just sending these justified block to EI and it also  brings the safe block closer to the head than the finalised one and it's a truly saved block. It's not gonna be reordered. Assuming that there is the honest majority and synchronicity. Also yeah but yeah it's still not that close to the head. As we previously discussed as a could be so that's just the proposal and just curious what people think about it.

**Marius Van Der Wijden (M)**: I think that's good. I think that's, that is, the block that we should declare safe.

**Danny**: yeah I think it's nice too, because it gives the exchanges and stuff a chance to begin using this and the algorithm can improve. Dankrad are you here, can you chime in on how you feel justified being safe currently.

**Dankrad Feist**: I mean that's definitely no downside to using that for now, I think. Yeah I mean as an update on that like this it's unfortunately turned out that it is much harder than we thought to define a safe hand with lmd. So yeah. I said I'm so optimistic that we can do it, but yeah it's definitely a good idea to have this intermediate solution.

**Micah Zoltu**: I would say there's no downside, the downside is that we can't point to the latest that goes too far behind.

**Dankrad Feist**: yeah sure it's off course, but it's safe right that justified. So  in the safe hat so the framework, the justified one is definitely safe.

**Micah Zoltu**: Do it. Is there a reason we don't have a justified tag like if that's a useful thing beyond the same tag like can we imagine execution or people will.

**Danny**: I want to know to justify  it might be if we had saved justified and finalised were safe and justified or just kind of equivalent this point that does give an additional granularity of progressive confirmation, in a sense. You know not finalised, but now the assumption on this break is much higher than just save it but you're also kind of just giving users more choice which may or may not begin. So yeah I'm not opposed to exposing us to buy it, you can definitely think of use cases where it's nice.

**Micah Zoltu**: I feel like if there're use cases then exposing it seems like the right thing to do, and we can always just in the docs make it clear that hey you should probably just use safe.If you don't know what you're doing you safe, but we also offer justified and finalised or whatever, but like I feel like we can solve the problem of too many choices to be a good documentation.

**Marius Van Der Wijden (M)**: My only issue with that is once we have safe justification already ready with the safest let's save.

**Tim Beiko**: It sounds like it was followed by a storm, yeah.

**Marius Van Der Wijden (M)**: You told me I just go for a walk.

**Danny**: We got the point. The semantics of like safe versus finalised just slide is weird that safe is less safe from those two things  called unsafe that would.

**Mikhail Kalinin**: I would not say that it's less safe, it's safe on the final life and say yeah I mean finalised justify it and see all three are safe  on the different assumptions  that's how it should be better.

**Mikhail Kalinin**: yeah.

**Micah Zoltu**: I'm open to other terms for safe if people have them. I'm also fine with safe.

**Aditya Asgaonkar**: confirmed, is a good alternative but it doesn't convey the same meaning.

**Tim Beiko**: I think confirmation is very dangerous because it has the proof of work connotation, and so people might confuse that with Like literally finalised.

**Micah Zoltu**: Or the last one is a block confirmed six times.

**Tim Beiko**: yeah exactly yes, I do.

**Mikhail Kalinin**: Okay, so finalised justified safe unsafe latest safe to justify it later still unsafe.Did we want to capture this all?

**Tim Beiko**: Is there a reason to be unsafe and not just keep the latest.

**Micah Zoltu**: Fine. I think they're the value of trying to overtime rename latest unsafe helps inform new developers into the ecosystem that they should not be using this thing, especially once we have better safes something more close to head them justified and so I think getting that name change now is the best opportunity to get the name change or introducing a bunch of other terms. Maybe in three to five years we can finally deprecate the latest, but I do think there's value in making it very clear that you should not be using this unless you really know what you're doing.

**Mikhail Kalinin**: OK so. I will just probably submit a PR or update the existing one and we can proceed with that. 

**Tim Beiko**: Okay, the recap, you will be so finalised and then justified safe and that's it.

**Danny**: I guess inside of the consensus layer spec is where we probably map, we just do the safe algorithm is returning justified for now. We can update that algorithm and future.

**Mikhail Kalinin**: yeah, it will probably be sometimes difficult to explain the difference between finalised and just fired for and the users. I'm not sure if it's going to be that much useful but anyway haven't granularity is always good.

Mikhail Kalinin: So okay let's have this all also like a minor question is **what should el respond with when once it gets finalised requests before the merge?** I think the finalised and justify it and save before the merger think it should respond with error, which is, which will allow to avoid any bugs or unexpected things happen, and if you're requesting finalised before the merge got something meaningful other than error so **I think error is preferable option unless someone has any other opinion.**

**Tim Beiko**: I think that genesis block is more likely to lead to weird errors.

**Danny**: agree, I just worry that someone has some sort of setup where they're trying to switch from confirmations to finalised and then all of a sudden, they go from thinking something 10 blocks ago was equivalently finalised to nothing ever in the chain ever been finalised, and I worry about edge cases there I think error is safer.

**Micah Zoltu**: The other option would be for execution clients to have some sort of see CL like they can ask to say how far back do I want pre merge finalise to be so you can just define finalise to mean latest minus 10 or whatever.

**Tim Beiko**: You can always do that, but maybe it should be part of the spec.It seems a bit.

**Danny**: yeah they're very All core dev about us deciding if something's finalised soon, maybe use that rather than putting it inside of the client.

**Tim Beiko**: Okay, so it seems like there's no real objections against an error and it's just harmonising that behaviour across everything.

**Micah Zoltu**: Is it possible for json rpc clients to find out when the merge is going to happen or when it has happened.

**Danny**: They can ask for the difficulty or pre brand out and if that exceeds 64 bits then the merge has been that  value.

**Micah Zoltu**: I'm thinking of dapp developers who want to be merge ready and you want to deploy your APP before the merge happens and you want your APP to smoothly transition to pre merge behaviour to post merge behaviour with regards to finalise justified safe.  I am trying to think like do we have a good story to tell them or a good narrative for how they should build their Apps. What should they do, you know it should, should they be checking difficult equals zero is that the right thing, or can we give them something like an actual.Is proof of stake versus is proof of work query they can run. It may be that the difficult thing is perfectly fine. I don't know.

**Mikhail Kalinin**: They can use this error and response to finalised requests because of the merge.

**Micah Zoltu**: Oh code flow on errors.

**Mikhail Kalinin**: Yeah wonder yeah I agree, I agree that  difficulty zero would mean that the transition has just started and is in progress, I mean **the first block is in difficulty zero** and the merge is finished, it's considered as finished when this transition block is finalised.

**Micah Zoltu**: Right, so they can actually be finalised until sometime sufficiently after the merge, which is long after difficulty has switched to RANDAO.

**Tim Beiko**: Right and sometimes it takes 12 mins or something. Okay anything else on JSON RPC? 

**Micah Zoltu**: Sorry, I had myself muted and I have some closing comments. Users say a more clear way to find out when it's safe and it's a reasonable time to switch to using finalised that doesn't involve them like querying things that are erroring and then having to set up error handling that alters their code flow. Maybe we can give them a simple json rpc method or something they can query that says is now the time like is the merge fully complete or is finalised available yet or something along those lines just dapp developers don't have to put in these horrible hacks. Just to build good Apps around them.

**Danny**: There might be a good blog post too.We get some of the stuff and about these new tags and also talk about some of the ways they can use them and maybe some of the logic you can use to kind of assess what emerged and stuff.

**Tim Beiko**: Yeah and we can definitely organise calls like would application developers and and walk them through it and also just get their concerns about specific flows.

**Mikhail Kalinin**: Right, if we don't provide a disgraceful method call that will return that the merge test happened, they will have to rely on  errors before the merge and yeah absence of errors on gets finalised block as the signal that the merge has happened, I mean that's from json rpc will not be possible to get.

**Tim Beiko**: I mean you can look at the block header. You can look at the block header and that's what some stuff will be zero after the merge.

**Micah Zoltu**: During the transition so you'll know you're in the transition, but you won't know the merge is complete and that's when you don't want to switch over your strategy and your APP until after the merger is complete. So right now there's no way other than just trying things and getting errors and then like catching the air and  changing your behaviour based on getting an error there's no way for an APP developer to build something that changes behaviour once the merge is complete.

**Mikhail Kalinin**: I'll go, I'll continue the supply.

**Tim Beiko**: Are we creating a smart contract which just has the difficulty of code in it? And then people can just query that smart contract.

**Marius Van Der Wijden (M)**: So you want to know when the first block was finalised, and you can query for that yeah.

**Tim Beiko**: The first five.

**Marius Van Der Wijden (M)**: We like to implement this like a five line change. I just don't really like the notion of having a new json rpc call for like 12 minutes or that that is important for something I don't know. Maybe maybe like three weeks, and then you know, once we really want to use neat  stuff anymore.

**Micah Zoltu**: We can use it again and change the consensus engine again.

**Danny**: Yeah I'd prefer writing some. pseudo code to show how people get this from and then libraries can write a function if they want. 

# [Shanghai Planning #450](https://github.com/ethereum/pm/issues/450)

## [Beacon Chain Withdrawals for Shanghai #495](https://github.com/ethereum/pm/issues/495)


**Tim Beiko**: Okay, next up I guess yeah before we move to the next thing anything else on the merge itself or kiln or testing. Okay, next up Alex has an update about a big beacon chain withdrawals, and we also have someone else. I'm sorry I'm searching on the zoom screens but there's really too many people. We had someone from the ladle team who had a proposal for partial withdrawals as well, so maybe Alex if you want to go first kind of give an update on what you've been working on and then we can have the partial withdrawal. oh yeah, sorry about that yeah you want to give a quick update and literature.

**Stokes**: Sure yeah so last time we talked about this essentially, I think there was a lot of sort of demand for something to organise all different threads so that turned into a Meta spec. I'm just gonna share my screen quickly and we'll just run through it. It's pretty sure. I'm So sorry. Right, I see, can you guys see this.

**Tim Beiko**: Yes, we can.

**Stokes**: Okay, so yeah I'm not going to go through this in detail if you want to read it. It's here, but essentially it just has some pros of how low drawls flow will go and then weeks to specifications at a high level that consensus layer essentially schedules winning the draw should happen, and then it puts them into this queue and then the layers also in charge of. I didn't decrease the drawls into execution blocks. There's a specification for how that works, because of this layer here. There's a PR for the modifications to the engine API because then essentially again in some way to consider slayer decreases withdrawals the shock to the engine API to the execution layer. Then, what I want to talk about today is essentially two different options here , like two different eips.One of them, we discussed last time in terms of having a new transaction types to represent the withdrawal there's another option that is essentially some sort of system level operation that's far more involved, but essentially it's just saying okay, rather than have been new 2718 style transaction type we have this new type of thing called an operation and that's where the withdrawals live, and the reason we want to do that is basically to firewall off. You know, mixing withdrawals from user level transactions and there's probably some safety benefits there. But here's the catch is that one thing we would really like to have some sort of logging so when it all happens would be really nice if there's some way to just watch the execution layer and know that the withdrawal, you know, has actually occurred. The point here is that if we go with 4863 the previous tip that we talked about where it's a new transaction.Type then.you know, we can reuse all the existing sort of events infrastructure logging in a vm. That's great if we go this other route 4895 which is.  Maybe in some sense, you know cleaner or elegance we have basically basically have to recreate all of their seats infrastructure and that, basically, is a lot of work.
So I essentially want input on this call. Does anyone have any preferences on either? Have you had time to look at these eips yet with feedback?

**Danny**: Questions are actually very important.

**Stokes**: So it doesn't have to be, I think it is like a pretty nice ux. But yeah I mean there's probably other ways to figure out that your withdrawal process does have a validator and yeah it's really just a question of what kind of the facilities do we want to provide validators.

**Mikhail Kalinin**: I have one comment on that sorry.

**Tim Beiko**: Oh, I was gonna say what's the argument against having some way to like this.

**Micah Zoltu**: You know it's.

**Stokes**: Much the arguments and not having them yes.

**Tim Beiko**: Right right like  it's complex if we go I guess the system operations route.

**Stokes**: To add already so yeah I mean I can just click through so basically like to give you a sketch like it's literally just having like is that important okay sorry.

**Tim Beiko**: Connected very weird today.

**Stokes**: That's okay anyway, like basically it's just like adding a whole new field to the block and so because of that we can't necessarily directly reuse you know their receipts infrastructure that we already have. So we'd have to duplicate all of that and that's where. It starts to get quite hairy.

**Tim Beiko**: Right.

**Mikhail Kalinin**: Right inspect says that in case of withdrawal operation, it must never fail. It's like an unconditional one, so you may basically use it. These miserable operations as logs or kind of logs.

**Micah Zoltu**: Yeah I would. I definitely agree that logging is like we should either go through a system contract and no logs or we do something else with logs. I am definitely not a fan of trying to get logging in or get receipts in with the system operations stuff.

**Stokes**: Right, so does anyone..

**Martin Holst Swende**: Well, as well just wanted to say, Mikhail I think the spec does not say that it must conditionally succeed. I think originally the spec sold it so if you had that bind your East one contract recipients, which is something which would never ever accept anything and then you would never be able to withdraw because no matter how much gas you specified it. But I'm kind of like this.

**Danny**:  This version is just like a balance of it.

**Martin Holst Swende**: Right so that's kind of the both of these options are they both centred around the gas this the one where we just do it. yeah these are both push. Good, okay.

**Danny**: We did analysis of existing code, so one deployed contracts, none of them rely on code execution and we've spoken with some of the employers that had logs in there and said they don't need it.

**Martin Holst Swende**: yeah.

**Andrew Ashikhmin**: I think that the system approach is my screen and it's a very important operation, so we don't want to do it in a reliable fashion and transaction is just abusing the notion of transaction because it's not really a transaction it's just a balance of date but it's not like it's not a balance transfer. If you want some logs on the vm side things like that, that should be crafted specifically for this operation because it's. Yeah I wouldn't have used the notion of transaction for this.

**Stokes**: Yeah which is fine, but then I'd probably suggest going with this option out so we've got all the new operation thing, but then yeah just dropped the logs because I think it's going to be way too much to like have a whole new like receipts try have to aim testing etc to cover all that.

**Andrew Ashikhmin**: But then again like do we need access to this from the vm side, because if we don't like the observer ability will be there, you can observe it by looking at the header and the withdrawals as was mentioned, they cannot fail right So if you see there was joel's in in in the header, then you see all of them, but the question is whether you need this observer deleted from the vm site as an ev	m code.

**Stokes**: Right, and I think part orders came from, as we looked at the existing zero sort of each one's credentials that have been deployed, and the only real thing anyone who's doing was logging but yeah like Danny said we've talked I think to some players and it's been.

**Danny**: Logging  is really the only one doing logging and they said they hadn't actually expected code execution, but just kind of put that in there, as the best coding practice so you know they're not even necessarily expecting more.

**Martin Holst Swende**: So, as my five cents oh yeah and I'm sorry I'm not really up to speed on all the details, but I agree that for them as a transaction is abusing the console transactions, however. Block body is now  a list of uncle's it's going to be filled as Michael said after the merge and it isn't transactions. There is a lot of code out there I have just bought that is based on us and youth protocol which have the capacity to request these pieces of information from another peer if you want to add a third aspect, the block polly. I think that might be a lot of work. Alone codes and things to be rewritten, I would like to hurt his feelings if Peter has any thoughts about this, I don't have their own call, though.

**Tim Beiko**: I don't see them on the call.

**Micah Zoltu**: So the two options for where to put these two different sections of block, think, right now, are just depend on the end or take over uncle's. Previously Peter had argued pretty strongly against taking over uncles and he strongly prefers spending new things to the end and just throwing away things like accepting the cost of the extra bites.

**Andrew Ashikhmin**: Will there be a lot of withdrawals?  Can we simply put them in the header rather than the block body.

**Martin Holst Swende**: We can borrow a lot of them.

**Danny**: A fixed amount per slot and then they will be so we could decide on a number, you know it affects some of the ux here. But the exit queue is already bound to approximately four ish per slot so after you clear out maybe some large amount of withdrawals at the beginning the bound doesn't need much more than that and the consensus layer will have a bound on what how much putting in here, because there will be a maximum cost of this operation on the system and that number can be done.

**Tim Beiko**: So, it seems. Please correct me if i'm wrong here. It seems like we have rough consensus around the system level operations approach and it's like a question of how rather than like if it generally makes sense.

**Micah Zoltu**: And login.

**Tim Beiko**: Right and no login and I think so. Alex I don't know, I think the ether scan people had said they were fine with either option as well, like, I think the one thing we want to make sure if there's no login us yeah that folks who monitor this stuff are still able to to access it and expose it.

**Stokes**: All right, and if you're going block by block like the withdrawal will be there and we know that it succeeds so.

**Danny**: I think the one use case you don't really get is like I'm a validator. I turn on my node and I just want to have, I know my withdrawal index, and I want to ask if it happened or not, you know where it happened. If this is right, otherwise yeah you can scan I mean and there's sequential so you know you can do a binary search to find where your were received happened or actually yeah that you can actually know if what you received happened, very quickly, because you can look at the latest withdrawal. And if it's greater than your receipt index, and it has happened so there's three things that you can do without logs to probably handle these cases outside of the evm.

**Tim Beiko**: Okay and Ansgar you have your hands up..

**Ansgar Dietrichs**: yeah just wanted at this document potentially putting the phone call into the header like what's the size of dollars, just to address and the amount is there anything else, because then it's basically barely bigger than just putting the hash generic.

**Danny**: isn't an address. It's an amount and currently an index.

**Ansgar Dietrichs**: And what inexperienced.

**Danny**: Yeah, it's the difference when we were going with the transaction method and any sort of logging in that kind of stuff it allows you to differentiate it also would allow you to do, you know, a search like I just talked about more easily because it's not necessarily a mountain address you're not necessarily unique given partial withdrawals.

**Ansgar Dietrichs**: And, but then it still seems only to excel, they are basically the size of maybe the phone.

**Danny**: But you would have more than one per block.

**Tim Beiko**: I guess. Okay, in terms of the next step, does it make sense to move at the system level version so 4895 to consider for inclusion and have people kind of keep obviously looking into that and.figuring out the quirk around it, but just so we can make sure we're kind of all focused on the same thing.

**Stokes**: Sounds good to me, yeah.

**Tim Beiko**: I guess yeah, does anyone have an objection to that?

**Danny**: On the partial withdrawals, I just wanted to say yeah I have this tracking issue, and this is where there are three key features here one is to fully withdraw X validators, the other is to change credentials from bls credentials to which i'm working on in a right  now, I think that this is want from the from their perspective, the execution layer all of them just look like things being withdrawals being queued into the execution layer and so that makes it doesn't really matter but from the perspective of validators and features, I think it's a pretty critical feature to not put crazy pressure on validators exiting out of return. So it  has been kind of in the consensus real map.

**Tim Beiko**: Right and Artyom do you want to take maybe a minute to kind of explain what your proposal was.

**Artyom Veremeenko**: Here it's kind of obsolete now like the new push based proposals, definitely more preferable from the point of view of liquid second protocol as well yeah I just like to know that partial withdrawals are crucial for us.

**Danny**: I think, for even just for many other use cases as well they're pretty good for the experience.

**Tim Beiko**: Yeah just for the health of the beacon change you don't want people having to withdraw their like 30 or something ETH and do not just deposit it, on the other side.

**Artyom Veremeenko**: yeah and we have got a second part of our proposal, which is more related to the question of how to pass some intentions from the execution  layer to the consensus layer like when validated like to rotate its case or the first exit but it's out of the scope for this call.

**Tim Beiko**: Right this is more of a consensus layer call  discussion.

**Danny**: Yeah and I yeah I'm happy to haven't had a chance to read the proposal, but I do think that that is a very nice feature and actually protects against a couple of weird withholding attacks that we should talk about.

**Tim Beiko**: Anything else on withdrawals.

**Andrew Ashikhmin**: So sorry the maximum is 4 or 40.

**Danny**: Four is the amount of exits per slot currently, and so the number of withdrawals per slot you would probably have in that same order, it depends on the partial withdrawals scheme, but I would say, 4 to 16 or the realm of what we do here.

**Micah Zoltu**: There's no execution block as slots do those withdrawals testing for the slot and move to the next one, you have eight in the following.


**Danny**: Not currently.Okay, that would put a You know unbound costs the execution layer

**Andrew Ashikhmin**: If it's only for or even 16 maybe we can put them into the header but if you ever see that in the future it will be more than maybe to be future proof and yeah it should be better to be to be in the body.

**Tim Beiko**: Right yeah and we, I think we can take that offline as we're looking into the implementation details and anything else on withdrawals.

**Artyom Veremeenko**: I could also say that from the point of view of staking protocol there might be a slight desire to be able to distinguish partial and full withdrawals. I may have different addresses, but it seems to be too difficult to implement and not very crucial for us. Just to note right.

**Danny**: Yeah I mean with a beginner's code. All of that becomes possible. It's a matter of what exists.

## EIP-4844 updates


**Tim Beiko**: Okay yeah just give a lot, because you only have 20 minutes, and at least one big topic last. Proto you had an update on EIP 4844 never pronounced that right forget for the shard Blob transactions.

**Protolambda**: Exactly, hello friend, welcome very quick updates so since last all core devs comb we have worked on consensus specs exclusive APIs we have built a meta spec to link everything together, I think that's related to the proposal, Tim is going to share very you're trying to find structure for this first layer, yet the process. For now we'll just try and work with every spec out there, they also have exclusive api's now and we have benchmarks that are supposed to implement or node the benchmark survey reasons. I'm not sure if I have the time to look at those yet but it boils down to having to batch verify these block transactions to work around the processing time issues. So this requires some minor refactoring to take multiple transactions and verify them together and the blob spiffing a transaction can also be terrified. On all I think it's not too bad and the same applies here to the concerns there that can also batch verify blobs. We're working on testing this person and working on tooling to try and get a definite running.

**Tim Beiko**: Nice.

**Martin Holst Swende**: So you have an idea, they are. How to say someone sends me a batch of 1000 block transactions every single one of them isn't valid, but they're constructed to be as hard as possible to verify.

**Protolambda**: Well what ballpark  we're talking about.If you receive all those transactions from the same pair you can batch verify them and then, if everything is in fellas you can start scoring down the pair. If one of them is fellas and you need that one transaction to go through they have more of an Irish situation because, once you figure out that the batch is in fellas you'll have to go and bisects the thing to find the fellas. Block transactions in the end of head you want to penalise peers that are giving you this bad information in the first place, like this is probably about so you like its objective. It doesn't affect consensus like this is in a transaction point like this is the step before that. So I think we need to improve the pure scoring system in the expression that here to help you filter out things configs to govern.

**Martin Holst Swende**: Against big role plays, guess not to do peer scoring. There's no such concept.

**Protolambda**: The consensus layer has extensive your scoring really does help efforts problems like better to stations are these what are high throughput things.

**Danny**: What about that yeah there's right.

**Martin Holst Swende**: So we don't even ban parents, no big I mean node ids are free, so there's no point having peers and we do kind of have some EIP limits. But yeah we don't spend a lot of time scoring peers, we kick out here if it does something bad but note that these are free and.

**Danny**: So I guess the point is, you can get 1000 of these transactions for somebody that on the first you're going to stop processing.

**Martin Holst Swende**: I mean like up 1000 node ids and connect them to guys and send them 1000 transactions from different identities for free. Well there's some processing power, because we need to generate these transactions at some point, but then I can reuse them and they  mean that they got people that I sell them to will not remember them indefinitely, if I have enough of them, so I can just from the network with them and what i'm curious about this yeah how close it is to avoid that.

**Protolambda**: So a single batch of blob is somewhere between 50 and 70 milliseconds to verify. This batch can be fairly large.i'd say i'd like the 40 or 50 ish media seconds for like a single transaction like the bets versus a regular like single transaction is not a difference. So batching is important here where we avoid the cost overhead of adding a lot more to verify. In the end, like it is processing and we should just like to use that information that if you're getting something that's wrong to try and ignore mortal thoughts before we get to denial service.

**Martin Holst Swende**: Well, look, I mean.

**Protolambda**: No different current transactions so if current transaction are valid you also ignore them and, hopefully, like you cannot deny you cannot do as a gift mode, but just keep by keeping  these lower the smaller transactions up like it doesn't matter if you send like 1000 small transactions are like one large transaction if the verification is not does not like if the bear that sense you those it's not held accountable you do need some system to give feedback to what is being received.

**Martin Holst Swende**: Right, but the only tool that we can cross is that if someone sends me something, then I can disconnect from him. That is the only guarantee, well there's no guarantee that you can rely on scoring or to be effective.

**Danny**: Right and you're saying node ids are free, but eips aren't quite as free.

**Martin Holst Swende**: Yes and yeah so it might be possible, but that can be tricky.

**Protolambda**: It seems to work for you to like the old pair scoring system, I think it's not too difficult to emulate some of those small subsets enough to say, like if transactions fell out, which is considered a spear as bad and prioritise orders. Yeah with it, I mean and I guess they do have your scoring it's just a kick you know there's binary meaning this is binary to if a transaction is in fellas that's all because of the bear that is sending you the transaction it's very clear that there must be, I think.

**Martin Holst Swende**: Yeah and you don't really see Okay, we don't have to go too deep into this actually on this call. I'll read up on the benchmarks and specs.

**Protolambda**: The agenda was to metal spec banks, the benchmarks and these optimizations.

**Ansgar Dietrichs**: Right and when I said that I think that it's worth considering as well, but there's no necessity to have a mental support for these transactions like right at the time 10 minutes. So basically, this would not necessarily have to be a binding constraint to bring into mainnet  we could launch without support and then of course it  will be slow wrap up for using those and it's time for me at the beginning to just only because of course notes would support having that locally fed to the medical for like you, they could just run their own taking nodes that they could operate at that great and have like a separate network for that I will be it's fine if we only get that support later, of course, not ideal, but so this is not necessarily like strange to go.

**Tim Beiko**: Right Andrew you also had your hand up, and I think, to get down the road back up to you have any comments you want to make. Okay anyone else have comments and thoughts on 4844.


**Danny**: I do think that benchmarks from a number of stress tests from a number of different places are probably pretty important. You know just the consensus layer disrupting one to two megabyte blocks, you know and then passing the execution layer that there's just.  You go from 20 kilobyte blocks 90 as we are with the merge. I don't expect things to be diverse, but I do, I do think that it's not unlikely that once you get to him at one megabyte, like little things we didn't expect start to operate in different ways that we expected that was I don't think anyone is going to be intractable solvable but um I think that it's good investments on.
# Core EIPs & executable specs (link)


**Tim Beiko**: sweet anything else. Okay, last on the agenda  I had something so we discussed this, I think, on the last call it's not done with this course for the after and basically. The core EIP  process is kind of reaching its limits, with the merge, where we have a completely different process on the beacon chain and then on the main net.

 We are starting to have proposals which clearly span across both so the two things we talked about today are good examples of that  it's quite hard to reason about like what the entire spectrum something should be and and and how the different parts all work together and in parallel, there are folks working on an executable spec for the execution layer which aims to kind of overtime compliment to replace the yellow paper as a canonical spec for them. So I had a proposal that I put together about how we could harmonise all of this, and just share it in the chat at a very high level. The idea is that We would keep code, the eips as the way to describe changes provide the motivation, the rationale. 

The security considerations and also just have like a tip number that's easy to reference within the Community. I'm using these for both consensus layer and execution layer changes and but then. Over time, basically moved the implementation sections to the execution specifications, rather than having them live directly in the EIP itself. So that you know the benefits we get there is that it is like harmonising across the beacon chain and the execution layer so you can link both So if you have any EIP like we can change withdrawals. You can just say hey here's the change to the executions back to us to change the consensus specs and maybe even the API repositories and then see if there's always been something like this big concern with like that we don't have a lot of EIP editors so we want it to be easy for them to actually review the eips and one of the things that's actually quite hard for them to review is when people put links in the EIPS because there's a bunch of dead links over time it's hard to assess the quality. So, by having links out to just the different specs repo and you can have a pretty easy to enforce rule that only allows links that you know these two or three repositories and  just like in the API if it has a link elsewhere and and then, if you know the EIP author wants to add a whole bunch of links, as part of their PR to the to the specs rebuilding them, they can do that. But it's not like it's not blocked in the EIP process, and I know Greg you had some comments about this is Greg still on the call. So yeah Greg you had some comments about this i'll let you share them I also put together an East magicians link for people to discuss.

**Greg Colvin**: yeah Great a lot of this will just need to discuss as editors we've only got about seven minutes left, so I don't think we can dig very deep um there's some good ideas there, but I think it's a lot more intrusion on the EIP process and we want to see, and in some ways it's making it harder.The whole point of the executable spec is, it is a another client so in the usual process the clients, often with the help of the eip author implement the eip.  The beauty of the executable spec is that once that client is running and is on the main net and in consensus that client becomes the reference. So I actually don't expect that a core EIP could be a totally complete and accurate reference when it's done the the network itself is ground truth and so having one client that we can point to and say we intend for that to be actual reference is great. But whether we try to pull that back into the p as a diff against a particular implementation doesn't doesn't really seem to help matters I don't think that's where the bottleneck is and I don't think the issue of references is really directly related that that's a different discussion we're having I disagree on that one too.

**Tim Beiko**: Then you also have your hand up.

**Danny**: Yeah so just a quick follow up on that, and then I have a quick comment on the consensus layer it isn't a full client, it is actually. You know, implementation of course state transition logic such in very. Non optimised ways in ways that just expose what the logic should be rather than the sophistication of logic, as it will be in a client, and so it can't run on me that it also doesn't have network interfaces and yeah so in, and then we can build test vectors of it, so I just there's there's a different there's a spectrum of what you can do with it. I just wanted to say that out loud and then, but I will say I don't know if this helps our EIP editor problem. I mean it just shifts the burden to a different highly specialised group. You know, on the consensus layer there's a handful of people that have the ability to review these types of specs and provide rich dynamic feedback and sometimes. There are pieces that are open for a very long time because it's hard to take the time to to dig into it, so I it may be, is useful and getting more people to the table, but I don't know if it like solves the EIP editor problem I do think it may be solved other types of problems.

**Greg Colvin**: I think it makes it harder for editors I can't. We have to become experts and yet another thing.

**Tim Beiko**: To be here right there it's not expected that the editors would have to review the executable spec.I think  that he said, you do have different people who then review the actual spec and like they might be the same humans, but you don't impose that so you don't impose basically like a technical review of the executable spec before merging the EIP itself.

**Sam Wilson**: yeah so the EIP editors would only be responsible for ensuring that the format is correct that like the tooling says the right things, but the actual review of the content of the diff would be probably by all core devops.

**Greg Colvin**: Right, So I guess I don't see how this helps.

**Danny**: I mean there's a huge overlap to like if I would have a hard time reading a Meta spec and being like okay this sounds fine i'm not going to go with that route that actually has all the logic.

**Greg Colvin**: I just took a look at the last spec. It's entirely declarative way back in the appendix there's an algorithm and they clear the algorithm to stop the spec. It's an example, the spec is totally declarative. It's up to you how to implement it. So there's it's just not clear that this language is going to be the best way to actually say this is what I want to do yeah.
So, to ask someone with an idea to improve the protocol to say Oh, but first, you have to figure out how to say it in this specialised language that may or may not be the best way to express your idea. You know, a paragraph of English can turn into a page or two of code when the English was totally clear to anyone who knew how to write the code.

**Tim Beiko**: Yeah Martin, you hand up oh sorry go ahead.

**Sam Wilson**: I was gonna say I think that's a fair criticism I mean, I think  One of the it's kind of a trade off right like a lot of things will be easier to express without having to describe the current state, so that that's a problem that comes up in the eips a lot today is that to say how you're changing something, you first have to have to define how that something works. You know that this code diff process will improve that part of it, but you're right there are some changes that are going to be way easier to describe as English that you'll have to implement as Python if we go down this road, so.

**Greg Colvin**: Yeah, I know just enough Python to hack a script together or to read fairly simple descriptions of structures and stuff.

**Danny**: yeah and if you do take a look at the specs that's, that is, the requisite knowledge. It doesn't use anything Python IQ and it does not impose things in weird ways and it's pretty much. It doesn't even use complex Python type constructions such that you know you have for loops, you have variable assignments, and you have very simple data structures. Again I think there's i'm not trying to make a claim, one way or the other on the best.

**Greg Colvin**: Guys see the EIP process close out and then this executable spec is its own thing. I get they'll have to be some way of victory over but trying to do both in one process, I think, will only make it harder. I mean what I put in code, for instance that code is often going to be a go not Python because I might have implemented the algorithm in gaff and then I can put in code i've actually tested and translating the Code, the Python isn't that hard for the core group that's doing it, but it's hard for me. Now if we want to pull that text back into the EIP at the end of the process that's not too hard. Or if someone who knows that stuff wants to become a Co author that's fine too..

**Tim Beiko**: Yeah Martin, you are about to say something.

**Martin Holst Swende**: yeah well the nice thing is that it really needs to be a full blown you know network machine that can live a minute, but then I want to tell you i've spent quite a lot of time reviewing each and also implementing eips and the English language is great, but when you translate the English language into actual code when you that's when you find all the corner cases and things that are implicit in the English language, and when you put it into call it needs to you need to make it explicit and that's when you find the quirks and the corner cases which shows that the specification was under specified vague, so I think it's good if we. get closer to how it looks on this 2.0 side where it  is code, where the author, who put this down was actually forced to figure all these things out and and I want to actually implement it can basically be a process implementation against the reference implementation or just transpired into his language. So I think that lowers the lowest form of work needed to be done at five different  client implementers since the work of you know putting it down in the code is only done once Like translate from English to cold it's all done once by the author  or someone else, but I think it's good to move in that direction, but there's a spectrum yeah.

**Greg Colvin**: They do get implemented the translation however whoever's writing it might find it easier to read the English.

**Martin Holst Swende**: Might find it right, but I like the way it is. You know whoever implements it first does one implementation one interpretation and things yeah that's obviously must be known someone else does another interpretation implementing slight difference because it wouldn't be.

**Danny**: So I think it's nice to know.
**Greg Colvin**: I'm just saying, if I have any EIP i've completely implemented it and go or c++ and a client and then it's like well that's all very well and good, but it's not an acceptable Lee I pay until you translate it to Python and it's like but it's expressed here and go and the go works, you want me to translate it to something else that I can't actually run and test.

**Tim Beiko**: But I guess what Martin is saying is, if I understand correctly, if that's not the case for like the media EIP the median the EIP is like basically under specified in the current format yes yeah, and so this spec kind of forces you to at least fully specify it and or realise that you can't do that you need to do some more work basically yeah.

**Greg Colvin**: yeah i'm just saying that happens in the process, by the time something gets accepted, it will have been implemented and more than one client. We will have found these cases the authors generally aren't in a position to do all of that implementing and testing anyway. So the question gets more at the tail end when it's actually working how best to express that and currently slowly the eips make it into the yellow paper and the yellow paper is the canonical spec. Yeah we can change that but trying to get the authors to write economically up front it's going to be hard you're going to need an expert to work with the author to do that, and I think that's just going to be even harder to find that person. But if such a person stands up and volunteers, yes.

**Tim Beiko**: We're already five minutes over time so we can continue this on the position, so I shared the link it's  in the agenda and I pasted all your comments from the agenda. Anyone have anything else they wanted to share before we head out.

**Danny**: Yeah to echo what Greg said, you can run the full Python implementation for the consensus layer side, and I think, very importantly, the tests that you write for that implementation for that Python spec actually become the consensus tests and so when we have people build new features, they also write tests and those actually become the reference stuff. Whereas I think when we have many different clients and are learning eips we don't always capture all of the edge cases in reference to us, even though, even when we're kind of like processing applications. So it's just another component of this process that can be useful.

**Tim Beiko**: Right, thanks for that. Anything else before we wrap up. Okay, I think yeah worth noting, I think, Europeans your time will shift before the next All core dev as we are not shifting the all core dev  time so it'll be at a different local time for you, if you live somewhere where daylight savings time is a thing. Yeah thanks everyone for coming on thanks everybody who didn't drop off halfway through after divergent stuff and I'll see you all in two weeks.

**Greg Colvin**: Thank you.

 
 
------------------------------------------
## Attendees
-  Aditya Asgaonkar
-  Alex B. (Axic)
-  Danny
- Gary Schulte
- Greg Colvin
- Jamie Lokier
- Justin Florentine
- lightclient
 - Łukasz Rozmej
- Marius Van Der Wijden (M)
- Micah Zoltu
- Mikhail Kalinin
- Pari
- Protolambda
- Sam Wilson
- Stokes
- Terence(prysmaticlabs)
- Tim Beiko
- Trenton Van Epps
-  Martin Holst Swende
-  Pooja Ranjan
---------------------------------------
## Next Meeting
April 1st, 2022 @ 1400 UTC

## Zoom Chat 

00:07:33	**Aditya Asgaonkar**:	Hiya! Finally able to make ACD after daylight savings

00:09:27	**Tim Beiko**:	https://github.com/ethereum/pm/issues/492

00:12:50	**Micah Zoltu**:	@Tim, people saying only your voice is audible on livestream.

00:13:21	**Tim Beiko**:	Fixed, sorry, will recap

00:15:40	**Gary Schulte**:	devnet6

00:16:55	**lightclient**:	is mev-boost being actively used in any devnet?

00:17:04	**Danny**:	not that I know of

00:17:09	**Pari**:	nope

00:17:10	**Danny**:	they are working on  getting it on kiln

00:17:15	**lightclient**:	makes sense

00:18:03	**Trenton Van Epps**:	Terence you are our favorite guest

00:18:06	**Micah Zoltu**:	Audio still broken @Tim.

00:18:12	**Pari**:	Still getting reports that just Tim’s audio is working

00:18:14	**Danny**:	any CL-EL endian issues are jacek’s fault

00:18:24	**Mikhail Kalinin**:	lol

00:19:22	**Mikhail Kalinin**:	Endianness bomb under the foundation of CL-EL relationships

00:20:58	**Micah Zoltu**:	Even our dev testnets are dominated by geth:prysm?  😢

00:21:21	**Pari**:	Starting to be, the devnets need to reflect mainnet 🙂

00:21:23	**Justin Florentine**:	No, kiln didn’t halt when it happened

00:21:53	**lightclient**:	goerli hardfork!

00:21:58	**Danny**:	lollll

00:22:12	**Micah Zoltu**:	"Someone stole all my Goerli ETH."translation"I left all of my Goerli ETH on the sidewalk and one day I woke up and it wasn't there."

00:22:28	**Gary Schulte**:	😆

00:22:32	**lightclient**:	lmao

00:23:50	**Terence(prysmaticlabs)**:	https://prater.beaconcha.in/blocks

00:24:10	**Pari**:	https://github.com/wealdtech/ethdo

00:29:28	**Jamie Lokier**:	+1 to performance issues during bulk sync, in all ELs

00:30:07	**Jamie Lokier**:	Thanks for bringing it up, Andrew

00:30:39	**Pari**:	I think next weeks goerli shadow fork would help us do some real sync testing because we’d have the benefit of the goerli state.

00:32:53 **Mikhail Kalinin**:	I think we should also have a Mainnet shadow forking at some point soon, once clients are ready. This would be useful to see how block processing and sync performs in  production environment

00:33:33	**Micah **:	See something, say something!

00:33:45	**Sam Wilson**:	Would an option to refuse to build on a chain that doesn't contain your block help?

00:33:47	**Pari**:	Definitely, its part of the plan. We’d like to have that done before we have to make a call on merging testnets.

00:35:11	**Marius Van Der Wijden (M)**:	a long running mainnet shadow fork would also work as a great benchmark for client performance

00:36:46	**Tim Beiko**:	First time in a while there are more people than can fit in the zoom screen!

00:36:47	**Marius Van Der Wijden (M)**:	50 people on acd oO

00:37:54	**Micah Zoltu**:	#party-lounge is gonna be boppin'.

00:38:49	**Pari**:	To summarise testing plan for the next weeks: 
- Public goerli shadow fork next week
- merge-devnet-6 week after
- Mainnet shadow fork week after prev
- Nightly shadow forking with everyone as majority client

If anyone has any other ideas for things we should look at in the next month, let us know

00:39:48	**Danny**:	also make a list of indicators that are not just finalizing and get into kurtosis nightly and testnet monitoring

00:40:32	**Micah Zoltu**:	How far behind is Justified?

00:40:41	**Danny**:	lags by an epoch

00:40:48	**Danny**:	but finalized lags by two

00:41:14	**Pari**:	Got it, I’ll create an issue for other metrics we have to look out for

00:41:35	**Gary Schulte**:	Does that mean that ‘latest’ would be an alias for justified?

00:41:46	**Micah Zoltu**:	No, `unsafe`.  😢

00:44:08	**lightclient**:	haha

00:44:46	**Danny**:	safu head

00:45:18	**Marius Van Der Wijden (M)**:	I asked tim, and he said "You can walk during ACD slight_smile"

00:45:25	**Danny**:	we got your point!

00:45:49	**Danny**:	just not the finer details of your masterful oratory

00:46:09	**Danny**:	safer safes

00:46:57	**Micah Zoltu**:	finalized
justified
safe = justified
unsafe
latest = unsafe

00:47:21	**Danny**:	safe = safe_algorithm()

00:47:26	**Danny**:	def safe_alg():

00:47:34	**Danny**:	return state.justified

00:47:42	**Aditya Asgaonkar**:	When would we set unsafe different from latest? Why do we have an unsafe tag?

00:47:58	**Danny**:	they are equivalent

00:48:00	**Marius Van Der Wijden (M)**:	return genesis block

00:48:05	**Marius Van Der Wijden (M)**:	thats finalized

00:48:47	**Marius Van Der Wijden (M)**:	was just a joke^^

00:48:58	**Danny**:	ah lol

00:49:02	**Danny**:	it’s a real proposal!

00:50:23	**Marius Van Der Wijden (M)**:	difficulty =0

00:51:43	**Greg Colvin**:	Good morning.  If a legislature tried to pass a law saying “everyone should get up an hour earlier in the summer” it would never fly.  I just discovered the one clock in my house I neglected to reset was the one I was watching.

00:51:48	**Jamie Lokier**:	The mainnet merge TTD may not be known at the time dapp developers want to deploy a merge-ready contract, for comparisons against it.  TTD is sometimes changed at the last minute :-)

00:56:06	**Stokes**:	awer13 i think was the handle

00:56:35	**Tim Beiko**:	https://github.com/ethereum/pm/issues/495

00:56:41	**Tim Beiko**:	Withdrawal issue

00:58:48	**Łukasz Rozmej**:	if we want to have those flags like finalized, justified and avoid errors/more RPC, can we have a REASONABLE values for during POW?

01:00:47	**Axic**:	Is the contract contract option completely off the table now?

01:01:15	**Danny**:	there seemed to be very little appetite for it

01:02:30	**Micah Zoltu**:	My vote is push via system contracts, and no logging.

01:02:50	**Micah Zoltu**:	*system operations

01:02:59	**Danny**:	I tend to agree

01:03:05	**Marius Van Der Wijden (M)**:	Agree 👍

01:03:32	**Mikhail Kalinin**:	@Lukasz It’s really difficult to get any meaningful                                              values for in response to these flags pre-Merge

01:03:34	**Jamie Lokier**:	Perhaps a log entry could be added by the system operation “as if” a transaction executed.

01:03:36	**Marius Van Der Wijden (M)**:	Don't know what you mean with "system contracts" though

01:03:45	**Tim Beiko**:	It was a typo

01:04:03	**Mikhail Kalinin**:	I am in favour of push+operations either

01:04:05	**Micah Zoltu**:	@Marius Typo.  I meant system operations


01:04:21	**Marius Van Der Wijden (M)**:	ah okay

01:05:15	**Danny**:	take over uncles 😅

01:06:28	**Jamie Lokier**:	Adding transaction type encoding was also a change to the encoding of block bodies, and afaik it didn’t cause too many problems at the time.

01:08:58	**Stokes**:	60 bytes per withdrawal

01:09:05	**Stokes**:	as currently spec’d

01:09:52	**Axic**:	What other operations can we envision? It would be a shame having this only for withdrawals.

01:10:03	**Micah Zoltu**:	None yet.  I asked that last time.  😖

01:10:04	**Stokes**:	we could think about unifying deposits

01:10:14	**Micah Zoltu**:	But... I like the idea of keeping that option open.

01:10:27	**Axic**:	And it is slightly annoying to have yet another way where account balances can change without triggering execution.

01:10:35	**Danny**:	https://github.com/ethereum/consensus-specs/issues/2758

01:10:48	**Jamie Lokier**:	Etherscan can look at the whole history so don’t need logs to index system events.  But ELs like Geth hold only recent state and don’t have access to deep state history, just receipts/blocks. Something using Geth would have to look to the balance of the withdrawal account to infer if withdrawal took place, and could not determine when.

01:11:24	**Jamie Lokier**:	(If I understood the details correctly)

01:11:49	**Stokes**:	there are schemes we can think of using the index like danny was talking about

01:12:32	**Marius Van Der Wijden (M)**:	So 4 withdrawals per block -> 100.000 blocks to withdraw mainnet,  x5/60/24 = 347 days

01:13:00	**Marius Van Der Wijden (M)**:	probably made a mistake though

01:14:19	**Marius Van Der Wijden (M)**:	eip-1559 style withdrawals 😫

01:14:40	**Micah Zoltu**:	I like where your head's at @Marius.  😬

01:14:59	**Stokes**:	if we can avoid some kind of fee market to meter withdrawals, the better

01:15:15	**Danny**:	I do think there’s a mistake in your math

01:15:47	**Danny**:	~225*32 slots per day

01:16:08	**Danny**:	2.6M blocks per year

01:16:27	**Mikhail Kalinin**:	it should be 3.5 days with 16 withdrawals per block

01:18:33	**Micah Zoltu**:	Wouldn't you instantly ban the peer, not just descore them, if it is provably bad?

01:19:50	**Micah Zoltu**:	Can we make it more expensive to generate then verify?

01:20:00	**Micah Zoltu**:	Hmm, I see.

01:22:33	**Jamie Lokier**:	NodeIDs are free, but positive reputation of a NodeID can build up, when a peer sends good data over time.  That could reduce the likelihood of being dropped, and increase the likelihood of accepting a reconnection from that NodeID in future, so that peers are motivated to build up a positive reputation.

01:22:47	**Micah Zoltu**:	Banning IPs causes problems with getting into a situation where you have banned a whole VPN provider.

01:23:12	**Danny**:	heh

01:23:18	**Danny**:	IP diversity

01:23:31	**Jamie Lokier**:	Last time I checked about 1/3 of all incoming connections I saw were from a single IP at a Chinese ISP. I assume CGNAT of some kind.

01:23:42	**Danny**:	is it actually a node? wow

01:27:06	**Tim Beiko**:	https://notes.ethereum.org/@timbeiko/executable-eips

01:33:51	**Micah Zoltu**:	What Danny described is exactly what I do.  😬  I read the EIP and ignore the spec itself...

01:34:01	**Danny**:	lol

01:34:21	**Tim Beiko**:	Yeah, I do think this is the current status quo

01:34:57	**Micah Zoltu**:	https://www.commitstrip.com/en/2016/08/25/a-very-comprehensive-and-precise-spec/

01:34:58	**Jamie Lokier**:	There have also been times where code in an EIP cleared up an ambiguity in the English, also.

01:35:38	**Tim Beiko**:	@Jamie, I think that would still be the case, right?

01:35:42	**Jamie Lokier**:	And times where the code is wrong and should not be trusted! :-)

01:35:44	**Tim Beiko**:	But the code would be in the executable spec

01:35:55	**Tim Beiko**:	And hopefully the code is correct by the time it gets to mainnet!

01:37:24	**Sam Wilson**:	https://en.wikipedia.org/wiki/Literate_programming <- this is a concept that's very similar to the execution spec.

01:37:34	**Sam Wilson**:	Donald Knuth popularized it

01:39:03	**Danny**:	example PR of how we do this for withdrawals feature as  a PR https://github.com/ethereum/consensus-specs/pull/2836

01:39:25	**Danny**:	relevant spec — https://github.com/ethereum/consensus-specs/pull/2836/files#diff-e62664a360f87fbbd16c6f0f0d11f0e47dcc4f343dc6478b6f81c3f5acd6d8cbR1

01:40:24	**lightclient**:	also you can run and test the python impl

01:41:43	**Danny**:	yes, this is a very important part

01:42:22	**lightclient**:	the decreases the gap between impl & reference tests imo

01:42:49	****lightclient**:	CL spec has done a great job of keeping those tight

01:43:02	**Jamie Lokier**:	Fwiw, the Python code in EIP-1559 has a missing step, but implementations and the test suite got it right.



