# Ethereum 2.0 Implementers Call 63 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2021/05/06 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  44 mins  <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/217) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=qhcMxBh0GEc) <!-- omit in toc --> 
### Moderator:  Danny Ryan<!-- omit in toc --> 
### Notes: Avishek Kumar <!-- omit in toc --> 

-----------------------------

# Contents <!-- omit in toc --> 

- [1. Client Updates](#1-client-updates)
- [2. Incident discussion (if anything)](#2-Incident-discussion-(if-anything))
- [3. Altair](#3-Altair)
- [4. Research Updates](#4-research-updates)
- [5. Spec discussion](#5-spec-discussion)
- [6. Open Discussion/Closing Remarks](#6-Open-Discussion/Closing-Remarks)


  - [Attendees](#attendees)
  - [Zoom chat](#zoom-chat)
  - [Next Meeting Date/Time](#next-meeting-datetime)

-----------------------------------------------

**Danny**: Okay great. This is ETH 2 or consensus layer proof of stakes implementers call number 63. The agenda is issue 217. Nothing crazy today
client updates I put a point in the agenda for discussion in the incident if we have anything else to discuss. I think we have discussed this a ton offline. There are a lot of public updates and discussions around it but if anybody hasn't had a place there Altair,  general engineering progress, spec in testing, planning. We are going to research updates,spec discussion and any closing remarks. Just a reminder, we can talk about some merch stuff here but there's super
active discussion going on in the Rayonism chat and there are still merge specific calls on the opposite week of this. So we would not  go too deep but you know if there's interesting stuff to discuss we can touch on it.

# 1. Client Updates

**Danny**: Okay, we will just go ahead and get started then on client updates. If you can give us definitely a picture of where you stand on  some of the merge progress and more importantly for this call where you stand on altair that would be great.

## Lodestar

**Danny**:  Starting with Lodestar.

**Cayman Nava**: Hey, so far as Altair. I am still working on it. We have added the new gossip
and req/resp methods. We have also been working on the light client side specifically now we are able to generate,sync objects and consume them and generate to consume state proofs. I think the big open item for all the Altair like  being able to run a test net locally or anything is just updating the validator interactions. Other than just generally, we have been adding more metrics to leadstar. It is really helpful and updating our microfauna dashboard and that's it for us.

**Danny**: Great and in terms of the validator interactions, it's primarily additive as long as you have the data structures correct and I guess a block producer could do the same role. Just not be  paying attention to those sync committees and similarly someone could just not pay attention to their security. So you might even be able to stand up a testament today but great progress.

## Lighthouse

**Danny**:  Let's move on to the lighthouse.

**Paul Hauner**: Hello paul here. So when it comes to altair

we have our consensus changes awaiting review.
We are adding some caching to our beacon chain for sync committee so we can get the fast verification of that down patch. We have got the network protocols under review.

When it comes to Rayonism:

 We are just passing the merged test sectors today.
 Generally we are aiming towards the 1.4.0 release. It is probably going gonna be the next few weeks but it rolls in a bunch of features that we've been working on including beta window support. Big reduction memory footprint doppelganger service.
We are reducing our outbound F1 calls and it will also have the altair structure definitions and the mechanics to choose between the two forks that's also going to be included in that  big release. So it's coming in a few weeks 

We are also planning to share some validated performance status.It is not  comparing clients but you can compare a group of validators just to the global average for some span of time. I am  just trying to  get the broader staking community to be a little bit more aware of the details of how their annotation rewards go. So they can come back to their clients with more info and Michael also has a PR open on spec repo for last balance carryover that validates performance. I will release it on sites like reddit or twitter or something at some point soon just a little spreadsheet.
That's it for me.

**Danny**: Yeah cool. We can talk about Michael's issue in the Altair section.Thank you.

## Nimbus

**Danny**: Nimbus

 **Mamy Ratsimbazafy**: Hi

so last monday we released1.2.2.It includes more efficient queuing which kind of reduces power consumption.
We also have a stabler and a more stable rest api we had issues with. I think it was the rocket pool that made large queries and sometimes instructed the beacon node for a long time.
We also fixed some b2b timer issues that caused us to give scoring penalties to peers that were actually good.

 On the research side:

We didn't make much progress on Altair in april. It was deprioritized so that we could advance on rayonism but this would be a priority starting from May.
We have also merged some PR that we had pending for over a month.
Regarding improved slash in protection performance so that we knew that everyone updated to our v2 of the session database to prevent issues if they have to roll back.

On the social media side and documentation:

 We have improved our nimbus guide in a lot of areas.
Following feedback from especially rocket pool users.
We have a blog post called if Eth2 is green which made headlines on twitter especially and was well received also on a lot of discord and that was with graph plus numbers.
A rocket pool running 10 validators for 10 hours on a raspberry pi that was powered by an external phone battery.

**Danny**: Nice great work thank you.

## Prysm

**Danny**: Prysm 

**Terence**: Hey guys Terence here

We finally merged the optimized slasher implementation and that will go into a release in about a week and a half.  
Now we're working on optimization of the sync committee like Paul said also working on networking and the validator to connect interactions.
We participate in the merge of the testnet.
Unfortunately we had some consensus error and that was confirmed using the merge spread test.
Product put out yesterday so thank you for that, so we failed at the execution payloads transactions and we are looking into the hashtag implementation of that.
I have also started working on implementing shardings Spec.
I will also be asking questions about protocol.

That is it from us thank you.

**Danny**: Great, yeah I am in retrospect, it was crazy that we tried to do that devnet without
consensus vectors.I am surprised at one of those it did. Great thank you.

## Teku

**Meredith Baxter**:  Hey guys 

so we are pretty much caught up with the latest alpha spec release with respect to altair.
Reference tests are passing except for a few altair state upgrade test cases that we need to debug.
All the sync committee related validator duties have been implemented.
We integrated the altair state upgrade logic so that we can transition across fort boundaries.
We added logic to update the enr fork id field at fork boundaries.
We have sync committee subnet subscription updates wired through to update the new in our sync nets field.This isn't in an official release but we went ahead and implemented the v2 of the get metadata rpc request which adds a new sync nets field.
We are continuing to migrate Jim Mcdonald's proposed sync committee api’s to the standard spec and implementing those within tekku as we go.
We also had a community contribution for a custom rest endpoint to query peer gossips course and that's it for me.

**Danny**: Great thank you. 

# 2. Incident discussion (if anything)

**Danny**: Next up two weekends ago, we had the incident 70% of block proposals went offline. I don't know if there's anything discussed here. Okay  if you're listening in  prism  has a great
incident report and a number of others have been discussing this and you can probably
easily find a lot of that thank you and thank you for everyone that worked their off through the
weekend.

# 3. Altair

## Engineering progress

**Danny**:  So we got general engineering progress and it seems like things move forward not too much of an issue. I did want to have another pre-release out now-ish. I actually had eye surgery one week ago and was a little more optimistic about how much I was going to be able to read and do computer work in the past week. But many people from my team have stepped up there's a lot of PRs out for kind of not a final release but a wave of kind of cleanups and testing
primarily. 

## spec and testing

**Danny**: A lot of testing to be added so we are aiming to get a lot of that review done today and try to get spec pre-release out tomorrow. There is this item that Michael proposed before he put this out. we were essentially dropping an epoch's worth of attestation participation which as
Michael pointed out as others agree.This would probably not look and feel good from the perspective of validators losing rewards on that one epoch. So there are  the simple mitigation might be just to give a plus a tiny bit of reward but the slightly more complicated but not very complicated method which Michael proposed is to translate the current epoch out to state pending stations into flags at that epoch crossing. The one major not major but the primary downside to this is just more testing needs to happen on that fork boundary but looking at his proposed changes. I don't personally think it's extremely complicated. I think we could get a reasonable amount of test factors in there without too much issue but while we enhance the testing the next couple days on that PR. I would suggest if you haven't taken a look in your client team to take a look at whether anybody has any thoughts and opinions on that or should we take this a sync into that issue .

**Vitalik**:  All right so this would only be a basic effect like attestations created in the last pre-4 key box that get included in the first post for epoch right?

**Danny**: Well no it is pending attestations in state.

**Vitalik**: So if nothing gets done then like there will just be one e-box that gets incentivized 

**Danny**: There will be one e-book. It will look like essentially empty participation and a minor reward drop in potential. Intuitively it doesn't seem worth the effort to even try solving that problem right because that's like one e-book. That was my gut Michael does have a PR up that
reuses the functionality of  prosthetization in a modular way, so that it is primarily just for using functionality. It does introduce consensus complexity and a lot of potential for error at that fork boundary which is like this single instance but open for discussion. I don't feel super strongly about one radio. I  mean  from the first form like financial analysis. It is probably a very small amount of money. One way or the other and so but a reasonable amount of dev time so that is kind of a funny way to look at it. But there is also it's definitely probably more correct in the sense to just
do differentiation.

**Dankrad Feist**: Yeah I mean it is just like one one epoch rewards are like so tiny from another perspective. I  would also tend towards saying it's not worth introducing any complexity for this.

**Mehdi Zerual**: I think Michael's the main consent.

**Paul Hauner**: There is also I guess some complexity in breaking you know the variant that
you know if you get your intestation included in blocks in the chain then you get rewarded and that these participation metrics stay the same. So you know I guess there is a complexity that lives there too. If we choose not to address it in the spec

**Dankrad Feist**: So what complexity is that you are saying like there's a complexity because there are no rewards like but even if they wear like one pock where nobody participated because there are no rewards for it that wouldn't do very much right?

**Paul Hauner**: Yeah i'm not saying that the financial difference is a lot but it's just just a thing where the system doesn't. It just has this epoch where you include your attestations and you don't get rewarded. 

**Dankrad Feist**: Just don't tell me where that introduces complexity. I don't see that it changes as an invariant.

**Paul Hauner**: Yeah that's right users expect 

**Danny**: It could potentially introduce complexity in third-party tooling that is making some
sort of assumption based off of that I would imagine block explorer.

**Dankrad Feist**: Well I don't feel like that's true because there can be epochs with no rewards.

**Vitalik**:  That never really wasn't any variance because there was always the possibility that network latency would just temporarily increase the four minutes.

**Danny**: Okay right I mean it's very like you actually get your things on change but doctor you can imagine and I am not  just pointing down there.

**Dankrad Feist**: I cannot imagine just cannot imagine a tool where this introduces complexity that's what I am saying.

**Danny**: I could imagine a block explorer that uses on-chain attestations to cap to display granular rewards and that gets out of sync with what was actually given. Because what is given is very bulk and so but that's  not necessary.

**Dankrad Feist**: But I mean that explorers would have to use so my assumption is that there's something broken just in the way we compute rewards. But I mean there that explorer has to do
something to like uh over the fork boundary anyway.

**Medhi Zerouali**: I think one of Michael's point, sorry one of Michael's point I think was
that a lot of validators will actually be watching this quite closely. That particular epoch quite closely and monitoring their rewards and noticing that they're not actually getting any might trigger a whole heap of users complaining on our discord channels and probably.

 **Dankrad Feist**: But I mean are we serious? I mean we're talking about one epoch
that is like cents how much do you get in one epoch.

**Danny**: But the doctor there clearly demonstrated psychology that the others care a lot if they have one epoch of red.

**Dankrad Feist**: Yes I agree but they are much much worse things. I think the issue there's
like there's a midge here that is blown into an elephant. No I agree but there are like 1 000 times worse problems with that.

**Danny**: We haven't seen I agree maybe maybe a hundred thousand maybe. 

**Dankrad Feist**: No, no no I mean like with rewards being with rewards being erratic. We have like 1 000 times worse problems than just like one.

**Micah Zoltu**:  I think the issue is more  that if someone sees something happen that's unexpected. They trigger a retrospective they  trigger a dev time they start investigating and if they're not prepared  for this to happen, They may devote you know hundreds of hours of engineering effort to try to figure out why they miss the Spoc and it turns out. Just because it's a little bug that was never bothered to be fixed. They didn't know about um it can be that I think that's real the real issue is had nothing to do with the money has to do with the when you see something go wrong you research.

**Dankrad Feist**: Right and you believe that time will exceed the time that we will spend on fixing.

**Micah Zoltu**: That's the right question to ask.

**Danny**: I think this really is that seems a question of complexity and there are four or five teams here that are going to implement that complexity. Ultimately I would like to hear more input from the various teams. It seems like the lighthouse team is keen on adding.

**Paul Hauner**: I am not sure that any of the lighthouse castles down the hill for fyi. But we still stand by what we say, I think.

**Danny**: This is a one-off writer. It is not going to be useful for future forks. This is just a purely solution for this one right. Yeah my gut feel is I would rather not do the work but no stronger opinion on it.

**Jacek Sieka**:  Yeah I think there is no strong opinion from us either. I mean we will have to maintain the boundary code between the two fourths for a while. Anyway thinking, so the first time we will be able to remove any of this complexity would be the next work potentially but.. 

**Danny**: I think the big risk is not the complexity being sitting in the code but the testing that we have  to ensure we don't accidentally get a consensus split through this like one-off complexity there.

**Jacek Sieka**: Isn't that kind of issue the same true. I mean one behavior or the other it's a behavior.

**Danny**: The current behavior is extremely simple. It wipes an array and replaces it with a different array. This is like a translation function taking the state of a current array and then
mapping it into like a parallel state in the other array.

**Jacek Sieka**: Yeah but we still need to we still need tom atch the pre and post balances before and after the fork right? That is the number that we are checking actually when we are doing the testing. 

**Danny**: Yes you need the state, you need the pre and post state to match like everyone to agree on it. But the pre and post state the way you get from this one to the other is extremely
simple versus a slightly more complex mapping. But we seem to be talking about each other a little bit

**Jacek Sieka**: Yeah whatever.

**Danny**: Okay if you haven't taken a look at the open PR please take a look at the PR. It represents additional complexity to solve. This minor issue would certainly require a bit more testing to make sure that we can get that for transition correct. Let's can every team please take a look at it. It is a simple PR. We just need to make calling. Okay has anyone stood up an Altair testament with the current specification locally or even any sort of like ci that stands
up a testament.

## Planning

**Ben Edginton**:  I believe from slack messages that Adrian got something kind of running with teku. yesterday or last night my time but that is all I know.
**Jacek Sieka**:  Yeah, we spin up little test nets in our Altair PR but they are tiny really they just run a few epochs to finalize the national concerns down.

**Terence**: Yeah same here. We have our end to end test which is similar like the test net
but we only run for a few epochs. That's not nothing fancy there. Yeah same for us.

**Danny**: Okay so I think we need to make a few more decisions to look at these lasso cleanups through. We will discuss again in two weeks on plan any other Altair items.

**Ben Edginton**:  Yeah, just a little concerned  about timing if we are  punting two more weeks before we make a decision. It just that June is definitely kind of outright. If we are going to run a six week or so test net at that stage then we are sort of into mid-july and we have got things going on the eth1 network and so on time starts slipping away. I mean should we start planning a date because there's always a latency between sort of planning a test note and getting everything ready and prepared for that. And so if we don't decide for until everyone's ready then we've got this sort of latent period .

**Danny**: Right I think the one another compounding factor is that we don't  have
like five open pr's on this the spec repo. So we could think if we put a test net target date.   We also have to put a spec freeze target date which we probably should so if we are looking at a calendar. Let's at least do the theoretical could do spec freeze the 14th first test net last week of May 1st week of June. I am just gauging what people think about that last week of May. Is this for an altea test now right?

**Danny**: Yeah so I think the sequence would  probably be we have these two public test sets that we can fork. But we should probably do a multi-client short lived test set before then would be my guess.

**Vitalik**: Given that we still like occasionally finding small things, maybe spec freeze on the 21st instead of 14s would be a little bit safer.

**Danny**: Yeah probably more realistic.

**Paul Hauner**: I would need to chat to the team the broader team in order to commit to
anything. But I would really be leaning towards the later rather than sooner right it's in like the next month instead of like this one.

**Danny**: So like second week of first second week of june is short-lived multi-client test that's
moving towards the end of june on working the actual test nets and doing a hard fork in july or august.

**Paul Hauner**: Yeah I think so um I would have to check
with everyone else before I could come in.

**Danny**: yeah actually on the fuzzing effort and fuzzing infrastructure when what's the status in that i know yes.

**Mehdi Zerouali**: No good, so yeah we are spending a lot of time patching youth chufas and basically incorporating the latest changes of various clients that we have in there so that's actually taken a lot more time than I anticipated. But that timeline will probably work for us. I am expecting us to have  both the differential fuzzing and the coverage guided fuzzing up  by you know june early June so hopefully we can get a decent amount of fuzzing cycles in before we or around the time we will be forking the test nets.

**Danny**: Okay so I am based off of that spec freeze in two weeks forking one of the public test sets by the end of june and the other one shortly after and coordinating the actual main
Altair fork depending on kind of in conjunction with london to be staggered at least some amount. I guess the nice part is that our validators could update both of their nodes at the same
time to deal with Altair and London rather than having to do one and then do the other. Okay so I think that does put us at a reasonable sketch of a timeline that we can commit to and in the two-week time. We will have the frozen spec and can get an engineering update and harden that a bit more.

**Ben Edginton**: Cool thanks. For considering that I think it helps just to have some idea of  what a plan might look like even if it's, you know, somewhat vague absolutely.

# 4. Research Updates


**Danny**: Okay um anything else on Altair moving on any research updates for today.

**Vitalik**: I started working on an annotated spec for the old town.

**Danny**: Okay, anything else people want to share today on the research side. 

# 5. Spec discussion

**Danny**: Okay specs can you let us know what the state of that testing release was.

**Proto Lambda**: Sure so right now we have a lot of new features in the left branch like in respect to testing both Altair and the merge. We don't have a release out just yet but so yesterday I made two different pre-releases or pre-releases of the pre-release really that
enable all the client implementers to move to go ahead and test the merge and try the latest Altair changes and then I expect like end of this week or maybe like start next week it will cut an
official release.

**Danny**: Thanks create any other just back related items
**Proto Lambda**: One more thing, so I'm currently writing a proposal for the new way. I would like to handle configuration within the clients and so I am working on updating the specs to separate
constants configuration and presets and the idea here really is to try and separate the things that are really intended for test builds and these kind of more static configuration things and separate them from the more dynamic things that we change with almost every testnet like the
fork versions. Forward planning like the timing of these works and a few of these common configuration variables that we would want to change in testnets

**Danny**: Kind of like a configuration preset versus a chain instantiation right so minimal versus when we do the fork. What's the time stamp that genesis is not going to say

**Proto Lambda**: Right so the idea here is that it's much it's less scary to try and change the configuration for different test nets and you can rely on the runtime capability of clients for different local tests and test nets and then settle on like a few set presets that change more of the configuration for testing purposes but which won't have to go beyond those presets. You want to support them in binary so we can have compiled time configuration for a lot of things.

**Danny**: Right which I think a lot of clients do and this just kind of makes it cleaner in this operation.

**Jacek Sieka**: I mean speaking of which do we even want to maintain the minimal configurations anymore I feel that they were kind of a hacks because we didn't know very much about performance back then and now. 

**Danny**: We do they are used extensively on python spec testing. It is very important for our CI just because we can't wait the time to run the mainnet configuration testing and I do think it's good to be able to have different configurations up there.

**Proto Lambda**: Right so I think we should maintain the minimal preset that really just defines it. So we have mainnet we have minimal. These things only change during compile time and then we do specify like which things are like part of a preset so clients can opt to define additional presets but we don't require clients to define more than these two spec presets and we just try and isolate the parts of the configuration that we do want to configure as a user.

**Danny**: All right keep an eye out for your proposal. All right anything else spec related or
anything at all. I want to bring up and chat about today.

**Jacek Sieka**: Yeah coming back to those constants I think as a general rule we find it easier to reason about compile time stuff from a security point of view. It is always easier to size things if we can analyze it statically but yeah that's right as well.

**Proto Lambda**: So for the shape of the of the beacon state and many of the other types these constants are very important to know in compile time to both optimize for them it also just reason about the security and then there are these other types of applications that you'll see with the light client hard fork a lot more where we want to do miracle proofs over the state and so I think it's important that this  shape of the state is very consistent.  So yeah we'll make and try and be on the conservative side of these types of configuration variables and make them compile time.

**Jacek Sieka**: perfect and we're on the same page

**Danny**: Great anything else today.

# 6. Open Discussion/Closing Remarks

**Leo BSC**: Yes any craving yep.  Yeah so used to quick maintenance quickly mentioned that we have set up a group for working on the standardization of the style metrics. So I would take this opportunity to thank. The client teams help us on this effort and we are starting to make some progress into selecting a subset of metrics that is already implemented on our clients and trying to standardize those. So that we can track many things across clients and another thing that I want to mention is that together with the at staker community we are starting an effort in order to track plan diversity and version progress over time in a frequent basis yeah so that's it thank you.

**Danny**: Got it thank youWhere is this working group gathering is that is there some sort of chat or is it on the discord 

**Leo BSC**: Yes so we have a discord group for both efforts, one for each.

**Danny**: okay anything else today before we close.  Excellent, okay that tentative Altair timeline is the goal. Let's work towards it. I will talk to you all very soon appreciate everyone joining and for all the updates and conversation take care thanks.


------------------------------------------------------------------------------
## Attendance

- Danny
- Leo BSC
- Vitalik
- Jacek Seika
- Lakshman Sankar
- Meredith Baxter
- Dankrad Feist
- Justin Drake
- Mamy Ratsimbazafy
- Cayman Nava
- Mehdi Zerouali 
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

## Next Meeting Date/Time : May 20, 2021 at 1400 UTC.


## Zoom Chat 

From Mehdi Zerouali to Everyone
The PR in question FYI https://github.com/ethereum/eth2.0-specs/pull/2373

