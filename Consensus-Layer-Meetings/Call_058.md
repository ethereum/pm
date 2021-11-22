


# Ethereum 2.0 Implementers Call 58 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2021/02/25 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  30 mins  <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/206) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=yrDVhoTg5XU) <!-- omit in toc --> 
### Moderator:  Danny Ryan<!-- omit in toc --> 
### Notes: Avishek Kumar <!-- omit in toc --> 


-----------------------------

# Contents <!-- omit in toc --> 

- [1. Client Updates](#1-client-updates)
- [2. Upgrate1](#2-client-updates)
- [3. Pyrmont load/new testnet?](#3-Pyrmont-load-/-new-testnet-?)
- [4. Research Updates](#4-research-updates)
- [5. Spec discussion](#5-spec-discussion)

  - [Attendees](#attendees)
  - [Zoom chat](#zoom-chat)
  - [Next Meeting Date/Time](#next-meeting-datetime)

-----------------------------------------------

# 1. Client Updates

**Danny**:  Okay to switch over if you are on the chat then let me know that you can hear us that be great. Okay we are at ETH 2 call 58 this the agenda. I’ve updated it and we'll talk about upgrade HF1 the unnamed thing that hopefully we can name soon, then talk about the fate of Pyrmont and or a new test net and then go to research updates back to Carl Beekhuizen and some closing remarks.  let's go ahead and get started with client updates we start with  Prysm today

## Prysm

**Terence (Prysmatic lab)**: Thanks. Here is the updates in last two week we makes some improvement,
Biggest improvement is to performance of anti-slashing data handling. See Raul’s [blog post](https://rauljordan.com/2021/02/18/when-a-solution-is-right-in-front-of-your-eyes.html).
      -	Improvement breakthrough that we made is that would make a pretty good ipv4 
            addresses in IPv6 address
     - 	Also implemented  more on API methods so that we are almost there.
      - 	We start training for half a month . so that's very excited and other than that  we 
made some minor login stakeholder improvements

**Danny**: Great thank you. Next Teku

   ## Teku

 **Cem Ozer**: Hi  everyone this is Cem from Teku. I hope you can  hear me all right.
      -	We will be migrating logic and constants in prep for HF1. 
      -	we are testing out LevelDB along with RocKDB because we have generally memory
             issues with RocksDB
      - 	One of the Teku bootnodes ENR has changed.
      -	we have the ability to add validators without restarting and halved the time to load
            validator keys.
[Release 21.2.0](https://github.com/ConsenSys/teku/releases/tag/21.2.0) out today.


**Danny**:  Cool. next Nimbus.

## Nimbus

**Danny**:  oh no we can hear you before the call started on me and now we can't okay moving on Lighthouse

## Lighthouse

**Adrian Manning**:  Hey everyone , in the last 2 week the main point are:

   -	We have added support for queueing and processing early arriving blocks. 
   -	The slashing protection DB is now pruned.
   -	we push three release which include	blockstick of the analysis time. and we're still 
            analysing the cause of incorrect head votes (affects several clients).

 **Danny**: Thank you. Let go on to Lodestar for now

## Lodestar

 **Cayman Nava**: Hello, past few weeks:
    -	 we've been adding all the tentative hard fork 1 configuration, SSZ  types along with prototypical Phase 1 types getting everything refactor to allow for separate kinds of name spaced variables.
    -	 We have also been working on the typing multi proof support attaching that to the 
ZCC library and both of them should be landed in our next release on Monday. 


 
 # Upgrade 1

**Danny**: Move on for now. Mamy let me know if you fix audio, let's move on for now.

## [Status / Plan](https://notes.ethereum.org/@djrtwo/hf1-plan)
**Danny**:  I wrote down very high level [HF1 doc](https://notes.ethereum.org/@djrtwo/hf1-plan). 

 We are still scrambling to get a pre-release done. Pre-release we want at least all of the consensus items in place and there's still some ongoing work there. Proto has done a little bit of work on doing some fork Choice work and in Serenity so we have a little bit of feedback with them. High level items are get the consensus pre-releases there if necessary, we will make some changes based on client feedback. And then will do a full pre-release which has all of the networking and validator specs.  It is still being worked on and in tandem right now so that might not be a disjoint process. At that point things are done enough that people can work on testnets, iterate it there, if there's additional feedback on.  then from there kind of like we did on mainnet launch expects private and transients singles client testnets . likely testing just HF 1 features from Genesis and then testing forking the net partially through and that some fork epoch. Then we will begin collaborating with each other doing some private transient multi clients testnets, doing the same sequence of events  testing both the features that isolation and testing through forking mechanism through epoch.  Those we might spend one out to be public or semi-public but Pyrmont or whatever is Pyrmont will serve as our public testnet. So after we went to all those the pre  releases as necessary little mainet release that will include a fork epoch chosen for Pyrmont and main net and will be all talk about it. No big surprises in this list I just want to write down and we will iterate and expand on it and might toss that to Eth2.0 pm. Behind that my team working on  and see how much is on my team working on and see how much is on my team working on and see how much is a past feature written and test written and tested and a number of and a number of others fork epoch tests as well as fork choice test. actually I thought we will have a pre-release about today and we’re not. I apologize but we’re on it.

**Ben Edginton**:  Danny what time you said? midyear?

**Danny**: It would be June mid-year. I don't want to put an obvious date on it until we get an engineering all that side done. I want you all to make a decision based on your understanding of the work at hand.  Eth1.0 will will have one fork in April and most likely another by the end of July. So probably best if we don’t do it at the same time but it's also best if we have this process done by the time London is done in July due to difficulty bomb.

**Ben Edginton**: That sounds good and it's planning goal so that just helps, thanks.

**Danny**: Okay anything else on that I know that we are the biggest bottleneck right now and not working so we will unbox.

**Jacek Sieka**:  I think one may be an interesting point to think about  Genesis. we have to think of syncing nodes from Genesis because I think if you look at 1.0, even if clients were to release even if they supported not syncing from genesis state starting today, we still have to support all the 1.0 clients previously and not force them to upgrade. 

**Dany**:Right,  so it's a good point today and change some of the networking  assumptions.

**Jacek Sieka**: So I mean good to make HF1 is a good spot to change those assumptions. a target for no longer requiring sync from Genesis.

**Danny**: I very much agree. 

**Danny**: Maybe we should see if there's any other coordination points better are good to slip in there for example and not that there's anything to do but like if we were to rename a field in the enr something like that this would also be if you could point the good place to do it is for coordination point okay yeah I'll keep that in mind. Yeah I'll keep that in mind if something came up some of the other things going on here and if anyone has some of the things that we can talk him out or like nice to do and not necessarily the hard work but it would be nice to coordinate on.

## Naming

**Danny**: Hsiao can you give us the contacts on progress and naming and also introduce our friend Patricio.

**Hsiao-wei Wang**: Yes. So about linking the future major upgrade , two weeks ago I opened an issue to collect ideas and thanks to all the proposers and emoji givers we’ve got  like 42 proposal. Here's the [summary](https://docs.google.com/spreadsheets/d/1vhZTXcTRlFvOOFTXpeD-S52-hK3F6Huq-vp-26YeWJI/edit#gid=0) of all candidates and the primary energy signals. We can see that star naming things got the highest emojis. It's proposed by our community friend Edson Iyom and it's like over 20 positive emojis.  I assume it is liked by the Eth2 pm people. I want to welcome Patricio from the poap (proof of attendance protocol) that offers to help us with the naming thing with POAP votes. So I invite official here to give us a short intro to their solution and after that I hope we can discuss or even decide if we want to have a community election /Poap the both or go with standard things, so even if we don't use it could be useful in the future anyway also. Any question before I can go over to Patricio.

**Danny**: Thank you Hsiao. 

**Patricio Worthalter**: Hello  everyone thank you very much for your attention. I help facilitate the events in this community forum. We have been growing this community from many months now and it is growing well. We are very happy to be the bridge between development and statkers and the enthusiast communities and to make the community feel closer to their research and implementation. We do some activities. 

POAPs provide a means to vote on things like this. It’s a nice test case for decentralised, non-binding governance. Proposal to use POAP.vote to poll those running validators, via the NFT dataset of 2000 validators. Highly sybil resistant. Might not be right for the naming choice, but the facility is available if people are interested. May be useful to gain input on contentious topics.

Presentation can be listened to at [20:51](https://youtu.be/yrDVhoTg5XU?t=1251)

**Danny**: If there is a sentiment to go with the star name, it has to be alphabetically starting with A. We could vote on which “A” start to do. Does anybody has any stron feeling, let Hasio know. In the next 24 hrs, we will make a call on the name. 

**Carl BeeKhuizen**: I’d like to voice my opinion against the voting. Voting on every name is likely to be cumbersome in future, so best avoided and could be resolved on GitHub or Discord. 

**Danny**: Also sometime we need to name it quickly. 

**Carl BeeKhuizen**: exactly.

**Danny**: Patricio, kindly do some community sentiments and we can go off from there. I assume people are okay with Stars name. 

**Patricio**: Yeah,that’s the plan.

**Danny**: Thank you! Okay anything else on naming before we move on Pyrmont load/new testnet.

# 3. Pyrmont load / new testnet ?

**Danny**: Pyrmont load the number of validators on Pyrmont, I believe mainnet is catching up with it relatively quickly and if it does not have a relatively full queue from here on out for the next chunk of time as a long as the mainnet queue is full, then mainnet will exceed the  load of Pyrmont and we will lose a nice testing zone.  Both Proto and Preston brought this up on different contexts that it's probably time to either grow Pyrmont or start fresh with something new, different testnet. The problem with growing Pyrmont is yes we could toss $50,000 validators in the queue but then we have degraded quality of service for users to test things. So if we were to grow Pyrmonth, we need to do it in a little bit of a new fashion. 
As in keep the queue relatively full on a daily basis but not overly full so that users show up, have one or two-day delay to get them. This can probably be scripted up relatively easily and those keys shared amongst people but then there's just ongoing maintenance and management to ensure the teams have these keys running. The alternative and this is not mutually exclusive, we could do both start another testnet or we can run a thousand validator and start it at a higher number 200k-250k that has a little bit maybe less guarantee of quality service to keep Pyrmont going as is. So I don't feel very strongly I would like some kind of engineering input because each of these paths would have different amounts of overhead. I think that the problem is a problem. I think we do need to have a higher load test net with respect validator count than mainnet but that's about all. Does anyone have any comments?

**Preston Van Loon**: Yes,  I think we’ve grown past the point where we can grow Pyrmont. we should seriously consider a second testnet with a much larger scale so that there are nice margins for testers. I am in favor of a new testnet or an alternative. 

**Danny**: An alternative would be to do a fork but that would require a lot more coordination and higher chance of failure. 

**Preston**: If we should choose the testnet with a much larger scale where we’ve a large lead time on the mainnet. It would be nice to have many months of lead time for the validators, so that we can work on the bottlenecks before it will become an issue. Prysmatic will be happy to send deposits on a frequent basis and never exceeding the queue size 50%. So that if somebody wants to join the quality of the Pyrmont will not be too degraded, will be 12 hrs at most to get processed to queue instead of dumping all 50k at once, to keep Pyrmont going and stay ahead of mainnet.  

**Danny**: Yeah it's an another goal. If Pyrmont is not way ahead of the mainnet,  it should be at least at parity for people to see new setups. Okay I'm convinced, who wants to take the lead on seting up a new testnet? I can knock on Afri’s door to see if he has interest. He can do probably some of the work but ultimately there will be some work on client team’s hand..

**Jacek Sieka**: I mean I would just mention, Eth2 deposits are slowing down. 

**Danny**: Yeah I agree I think that though it is still likely that in the 12-24 month time horizon that we do get to pretty high pretty substantial validator counts. But yeah,  what is the queue,  3 days long now ?

**Justin Drake**: So my estimate is that Coinbase will add roughly 1 million ETH.

**Danny**:  where do you get that?

 **Justin Drake**: So basically just by looking at the amount of ETH on the custody in the cold wallet of coinbase and comparing that to have exchanged like Kraken.

**Dankrad Feist**: I think it could be very different from what you expect. Kraken does not support staking and Coinbase might.

 **Justin Drake**: Kraken does, I believe. 

**Danny**: I’d imagine exchange would by default. But haven’t gone in detail.

**Danny**: So you would say maybe there's even a higher number coming. 

**Dankrad Feist**: I think it just depends. 

**Justin Drake**: So I just checked, they do have the new token. They actually have two new tokens. One called  Eth2 and one is Eth 2.S.  Dot S is the one that's taken for standard one and both are derivative and tradable. 

**Danny**: Are you trying to say that it’d be exited?.

**Justin Drake**: Yes that would be my assumption.

**Danny**: Great count.

**Dankrad Feist**: You can basically create a two different basket. You don’t take the staking risk and you also don’t get the rewards? 

**Danny**: Yeah!

**Danny**: I’d agree that testnet is slowing down and getting ahead with 200k- 250k validator will be valuable.

**Micah** (in chat): Why do we care that the queue is slow? Explained at [40:40](https://youtu.be/yrDVhoTg5XU?t=2440)

**Danny**: I still think we should do a second testnet, but organized. 

**Proto**: For the new testnet we should get started with state filled validators that we need. We want it to be implemented in the Geth client so it would be easy for people to actually get it. 

# 4.Research Updates

**Danny**: okay let's move on Research updates I don't know you all saw there was  a stateless call and Dankrad and Vitalik talked in depth about Verkle trees, pretty cool. Not immediately relevant to our work but impacted potentially. I don't know if the videos are public but if you want to check out the video. Any other research updates.

**Mikahail Kalinin**:  Update on the merge side - There is an [updated beacon chain spec](https://hackmd.io/@n0ble/executable_beacon_chain) including the executing beacon chain proposal. Plan to migrate to the specs o the Eth2 repo by the end of the next week. If interested, please add comments and feedback. Some feedback already received has been incorporated.
One update, it became independent of the Eth1-Eth2 communication protocol. This version tries to address the confusion of Eth1-Eth2 terms in the context of merge. 
 E.g. terminology around Eth1/Eth2 - we should all be mindful of this. Eth1 -> Application layer, Eth2 - > Consensus or beacon chain layer.
Once in the specs repo, it will be executable and publish some test vectors so people will be start implementation.
Will continue to work on the application layer, reach me out for any questions.

**Danny**: Great! Any other questions for Mikhail or on the merge in general? Any other research updates?

**Vitalik**: I also have a post on [ethresear.ch](http://ethresear.ch/) around [state-expiry](https://ethresear.ch/t/resurrection-conflict-minimized-state-bounding-take-2/8739/2). Feel free to check that as well. 

**Mikhail**: Question regarding Verkle tree timeline? It will be after the merge?

**Vitalik**: I do not know, there are people in favor that it can be done before. 

**Danny**: There is still some debate on technical vetting. Probably just depend on the relative progress. We probably wouldn’t do them simultaneously.

**Dankrad Feist**: I’d agree.

**Mikhail**: Timing of any Verkle tree implementation - 3 months 6 months?

**Dankrad Feist**:  I think, from the cryptographic engineering, they can be implemented in months.But all the stuff around that needs to happen,  it is likely to be more than 12 months to get the whole stateless Verkle tree apparatus into clients, but a basic implementation could be quicker.

**Danny**: It’s very much because how clients are structured today.

**Dankrad Feist**: Yeah!

**DannY**: You can do the Verkle tree without the stateless merge?

**Dankrad Feist**: Yes. That can be done a bit sooner, if we want to do that. 

**Danny**: Any other questions on Verkle tree? We will move on.


# 5.Spec discussion

**Danny**: something that I did and I'll take this offline. I request there's this PR by Vitalik that does changes it such that when there is epoch empty transitions which is substantial DoS vector today. 

It also does  per validator leak tracking so that's something that we saw on testnets the number of times was you have a leak that is happening when you get back to that Valley point and all the sudden epoch tracking is done.

Justin's also done a bunch of work to clean that up reviewing his PR. 
I did get some review with Terrance, General thumbs up there and I got a little bit of review from Paul. He said he can dig deeper and he was not in his feature and thought complexity was not worth it.  I would encourage members from each team to take a look at features and last bit of work that we are doing  at consensu side for HF-1. 
There is PR from  Vitalik that Iam working on merge from Justin, hopefully will get that done today. 

Any other things else you want to provide on Spec updates? We’re not on the pre-release yet but we’re getting there soon. 

Okay, anything else? 

Great, thank you everyone!

 ----------------------------------------------------------------
## Attendance

- Danny
- Leo BSC
- Vitalik
- Jacek Seika
- Patricio Worthalter
- Nishant
- Dankrad Feist
- Justin Drake
- Mamy
- Cayman Nava
- Mehdi Zerouali 
- Cem Ozer
- Terence
- Hsiao-wei wang
- Carl Beekhuizen
- Aditya Asgaonkar
- Alex Stokes
- Mikhail Kalinin
- Barnabe Monnot
- Zahary
- Pooja Ranjan
- Ansgar Dietrichs
- Proto Lambda
- Ben Edginton

## Next Meeting Date/Time : March 11, 2021 at 1400 UTC.


## Zoom Chat 

From danny 

https://youtu.be/yrDVhoTg5XU

https://github.com/ethereum/eth2.0-pm/issues/206

From Terence(prysmatic labs)

https://rauljordan.com/2021/02/18/when-a-solution-is-right-in-front-of-your-eyes.html

From Mamy 

Main points are here: https://github.com/status-im/nimbus-eth2/releases/tag/v1.0.8

From danny 

https://notes.ethereum.org/@djrtwo/hf1-plan

From Hsiao-Wei Wang

summary of all candidates: https://docs.google.com/spreadsheets/d/1vhZTXcTRlFvOOFTXpeD-S52-hK3F6Huq-vp-26YeWJI/edit#gid=0

From Patricio Worthalter 

https://docs.google.com/presentation/d/1_D5EwusPvG0jcVXCcq52gthH7FRJrudHfql1G29w-Tk/edit#slide=id.g656e31850d_0_0

www.poap.vote

From Hsiao-Wei Wang 

Beacon Chain Genesis Depositor: https://poap.gallery/event/661

From Mikhail Kalinin

https://hackmd.io/@n0ble/executable_beacon_chain

From danny

https://ethresear.ch/t/resurrection-conflict-minimized-state-bounding-take-2/8739/2

From Alex Stokes 

https://github.com/ethereum/eth2.0-specs/pull/2192

https://github.com/ethereum/eth2.0-specs/pull/2212


