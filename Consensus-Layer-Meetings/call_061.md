# Ethereum 2.0 Implementers Call 61 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2021/04/08 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  30 mins  <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/212) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=XLB5HEWdZUE&list=RDCMUCNOfzGXD_C9YMYmnefmPH0g&start_radio=1&t=5) <!-- omit in toc --> 
### Moderator:  Danny Ryan<!-- omit in toc --> 
### Notes: Avishek Kumar <!-- omit in toc --> 

-----------------------------
# Contents <!-- omit in toc --> 
- [1. Client Updates](#1-client-updates)
- [2. Altair](#2-Altair)
- [3. Metrics names](#3-Metrics names)
- [4. Research Updates](#4-research-updates)
- [5. Spec discussion](#5-spec-discussion)
- [6. Open Discussion/Closing Remarks](#6-Open Discussion/Closing Remarks)
- [Attendees](#attendees)
- [Zoom chat](#zoom-chat)
- [Next Meeting Date/Time](#next-meeting-datetime)
-----------------------------------------------
# 1. Client Updates

**Danny**: cool ! welcome call 61. We will discuss Altair a bit, Paritosh and Leo are going to talk about some metrics naming that might be useful, talk about research updates. You're probably aware there's a number of other things going on specifically the Rayonism calls. There's also a fortnightly merge specific call so although we can certainly answer a couple questions here if you want to dig in any of that. I think it would be best to use the appropriate channels and the appropriate calls to dig deep into that. I think the focus here will likely be on Altair for the time being. On the client update, I would love to hear just general progress on altair specifically. Just kind of the feel on where we are at engineering. Are there any huge blockers any skeletons in the closet ? As we have been kind of modularizing components and stuff. So help us understand that so that it. Let's start with client updates and we can go with prysm.

## Prysm

**Terence (Prysmatic lab)**:Yeah hey guys Terence here from Prysmatic labs, so let's chat about Altair first. So from  Altair front it's a little bit slower but we are making progress, so the latest progress is that we implemented altair beaconstate with the replacement and the 
additional fields. We are doing some testing around the estate to make sure that's implemented correctly and I am almost done with the process on sync committee and
so the next in my to do list  is to work on the accounting reform so that's us for our tier. We are pretty confident that once we have the foundation for the hard working logic done then the rest can move pretty quickly and in terms of the merge. We released a demo for prysm and catalyst so I hope that people have tried that and on the current work front. We did some optimization for the slasher db schema for a more efficient storage. We started working on subjectivity sync. So people can pass the state or url slash block route to the COI  and the notice it from there and we also fix a few parts on the pier store in front so yeah that's it. Thank You

**Danny**: Nice Terance, let's do Teku

## Teku

**Ben**: Hey everybody it is I this week. Yeah so the last little while has been
pretty much all about altair. Progress is good. So we have updated the Alpha.3 reference tests and almost everything is passing. As I understand it, there are a couple of sanity checks which are failing. So there is some insanity going on somewhere and we are failing to decode the SSZ in one of the fork choice tests which is weird because we pass all the other SSZ tests. So I just need to investigate what is going on there but otherwise I think
we are in pretty good shape on altair. Other than that we have been making optimizations for the workload on Parata mostly improvements to peer scoring. Updating the latest
BLS library and doing a bit more batch verification of signatures in attestations and that is
pretty much it except to say like everybody else we are hiring.

**Danny**: Thank you I have a question, I request when you all do figure out the SSZ decoding issue. If that is in fact some sort of corner case that we are not covering in the SSZ test. Let us know so we can get a test specific for that in the right place rather than kind of
implicit in the poor choices.

**Ben**: Yeah for sure.

**Danny**: okay Lodestar

## Lodestar

**Lodestar**: Hey everybody, so real quick. We cut a new release 0.19 on tuesday. It is pretty chunky and we are now supporting the latest LTS Node of version 14. We added queuing to our gossip validation engine and we also have threaded BLS verification now, so all these things are kind of combined and much more stable than Node running. As far as Altair goes, we have done a lot of the preliminary work for Altair just ensuring that we have support for different data structures. Updating the database we also have a Naive implementation of the alpha 3 state transition and it's passing spec tests. So I think the upcoming things are making something that's more that matches our fast state transition implementation. Also implementing the various network updates which we have not yet tackled. 

**Danny**: Wait, did you all integrate the fork choice test yet?

**Loadstar**: Oh! we have not. We will add that to our list.

**Danny**: Cool and the other clients as we go. If  you can let me know if you will integrate those. Cool great thank you. Let's move on to Lighthouse

## Lighthouse

**LightHouse**: We are also passing the Alpha consensus tests. Danny what was that I missed, what you said just then

**Danny**:  fork choice test and the test vectors and so i'm just curious especially because Teku ran into some decoding issues. I am curious if there are integrated ones yet?

**LightHouse**: No, so we haven't done it. The 4 choice ones are just the consensus, one so far it's all by that.I am passing those. We are also working on alternate networking with 2.8. We have our doppelganger implementation in for review that's the protection against running multiple dc's. We have been doing a lot with the memory allocated still we have got kind of
3-6 times memory savings. They are kind of in review and we are still squeezing a bit more out of it.We are working on a UI development, so it's in working on screenshots now and designs and it should be starting coding at the end of the month. We are also working on preparing for the merge test net and Rayonism hackathon, that's it from us.

**Danny**: Great  and Nimbus.

## Nimbus

**Mamy**: Hi so regarding the Altair  hard fork  for now we have the low impact and preparatory changes merged. Still evaluating the modularization of the code base for example the beacon state. The main thing that we need to solve it. Currently we assume that we have a kind of one fork at a time design but when we replay all states around the transition we need to be able to handle it properly. Otherwise we improved the performance of Nimbus. so we had some bottleneck real related to planning and we also added attestations batching and this improved performance on pruning to be able to handle. The increased load on the pyramid and hopefully a Prater as well. Regarding Prater we also added a Prater page to our Nimbus book and we also merged a long-standing feature request fallback if one provider so that you can point to Geth and also insurer in case your gif instance fails. So you don't have any issue with producing blocks. Otherwise we also finished our http server work because in name we didn't have any HTTP secure server that was working with or stacking and so this means that in the future you won't need to add the insecure option to have metrics. This also means that the rest API is almost finished, it's just pending review and you won't need to use a JSON-RPC which was used as a stop gap and lastly on the devops front. We will be migrating or flipped away from AWS to save on costs for now. We are migrating only one node but it's possible that in the coming weeks we migrate some more and we have some downtime in between.

**Danny**: Got it. I have a question for those that have done the dopple ganger protection especially after the Prater launch with Nimbus. Did you all decide, is there a workaround for Genesis that you have integrated or is that just still a case where people are offline for a couple of epochs.

**Mamy**: Given that it happens once every 6 months we didn't work on the workaround yet.

**Danny**: Got it. Paul did you all do anything with that?

**Paul**: I think our plan is to just not enable it at Genesis

**Danny**: Right like a flag 

**Paul**: yeah that's right.

**Danny**: Cool okay thank you. I know everyone's kind of working on different ways to  modularize the codebase and handle these. These fork data structures and worklogic
Is there any particular blockers or issues people run into that want advice or information sharing here? Ask away. 

# 2. Altair

**Danny**: Yeah cool reach out to each other moving on to Altair.

## Alpha.3

**Danny**: As you all saw Alpha 3 was launched. I actually was,I realized, I did something embarrassing but then the prototype is not too embarrassing but I realized I started at Alpha.1 instead of alpha.0 and actually confused myself. When I was releasing Alpha.3 and I was like wait we haven't done 4 of these. So anyway I had a little off by one error in my head but that is out. That is really close to honing in on a final version. 

## Planning

**Danny**: I think there are a couple of cleanups, there is some additional testing being done but nothing substantive that is in dev currently and the plan would be to get people to kind of get thumbs up from engineering teams that  implementations are done. Also obviously any feedback that you might have, so we can hone in on finalizing that. We are at kind of the beginning of april. We had discussed releasing two mainnets in June. That's beginning to be maybe not aggressive but the optimistic timeline. I think we should definitely shoot for june july. But I have a feeling based off where people are at that. We are not quite ready to talk about timelines. Does anybody have strong feelings about the earliest timelines currently that they want to share?

**Mamy**: We need to like two months is lead time for audits. So that's a hard constraint.

**Danny**: Okay if you are looking to do audits, I would schedule them right now because  the way that my understanding of the current auditing industry is that people are incredibly busy and getting timelines even within the next three months might not be realistic.

**Mamy**: Yeah I can understand that.

**Danny**: Any other comments on Altair planning. I figure in the next couple weeks. We will have a much better visibility in this. Okay, so let's keep digging in and communicating quite
a bit as things are ironed out so that we can begin to set some target dates.

# 3. Metrics names

**Danny**:  Okay Leo and Pari have been discussing some standardization of some core prometheus metrics that might help in various ways. Pari, Leo do I want to talk about that.

**Leo BSC**: Yes so the idea is to try to standardize some of the metrics and the plan is to 
start just with a few of them. Say about a dozen of them. We have prepared a document that I just shared the link on the chat in which we have two sets. One of them we call the minimal set. It's about a dozen metrics that we think are interesting to look in particular in the context of the proctor test set and so we provide the list of the metric the description the reasoning
and we look at four of the five clients. I think at least for the first batch of metrics all of them already implemented them. The problem is that they just have different names and we are not 100 sure that this is what it really is. So the idea is to really start with just these few ones and standardize it into a way so that we can monitor it and make dashboards and really see easily what is going on. So what it would be really great if  you know the different plant teams can either choose or select one person that can help us with this process. We promise to take as least as time as possible from you guys. We know that you are very busy but yeah if  we could try to set some calls  in which we can discuss. For example which of these metrics are the most relevant and if the numbers that we sorry the metrics that we
got here are correct or not and discussing that would be great. So yeah we will try to set up
a meeting within the next few weeks to disclose these metrics. It would be great if the client
teams can select one person that can join this meeting and let us know which person is that. Pari, do you want to add something else?

**Pari**: No that is, thank you all.

**Leo BSC**: Right for one and you have questions ?

**Danny**: one thing I want to reiterate is that  for client ease of client fluidity. I think we did a good job with the validator interchange database but one thing that I think is locking people in and hearing even more is their monitoring setups. People do a lot of work to get things set up and monitored properly and then don't want to do that again. This could potentially enable
some better fluidity there. Leo and Perry what were the particular use cases that are driving
this effort on your end. Is it primarily monitoring? I mean obviously it's monitoring but um
yeah what are y'all attempting to do here?

**Leo BSC**: yeah so, I think yeah that's what we discussed with Perry, Several use cases in the context of the prater or not. I think Perry has very clear use cases. Do you wanna mention those Pari?

**Pari**: Yeah sure, So it pretty much started with the prater setup. I wanted to create a bunch of dashboards to monitor how the testnet was going but quickly then into an extensive amount of having to look at three or four different documentations to figure out the exact metric names. So I looked at what pain points were there and what metrics were relevant for me to know that stuff is working perfectly fine. I just sort of spoke with Leo and discussed them if  he was also on the same page and then we listed them down.

**Mamy**: Regarding monitoring I have seen that the Eth2.0 api repo has a v1 release, so I assume that it can be targeted as a standard or some common monitoring across clients.

**Leo BSC**: which link is that I mean.

**Mamy**: I am adding it to the chat.

**Danny**: The apis are different from these monitoring metrics right; they're fairly independent.

** **: There actually exists a metrics document which tried to standardize this
like back maybe a year ago so that would also be….maybe that yeah growing old but some of these metrics are good.

**Lighthouse**: on the lighthouse side. We have also been quite interested in standardizing metrics to enable client fluidity.one of the approaches that we have looked at taking ease. There are a bunch of community members. I guess that has made some pretty cool dashboards. I forget their names now but there's some quite popular ones. Typically they work with prysm, so the approach we have been taking is trying to get these dashboards and then use that set of metrics to indicate that. People you know want to use it and then try and focus on those first so that's kind of the route. We have been taking on someone on that full time but they got distracted but I think they will get back to that full time so the lighthouse is keen to standardize that.

**Pari**: would it be possible for you to put us in touch with this person so we could at least get the information about the dashboard and then correlate that with what we already have in a matrix with a minimum metric set?

**Lighthouse**: Yeah sure so something I found with metrics is that it varies a lot depending on what you want to do so. If you are sitting there and you have got like you know two main net validators, There's a certain amount of things you want to do. If you are trying to monitor the health and network. There's the things you want to do and if you are someone like me. There's a whole other set of things you want to do so. Yeah it is just one thing that I have found but I think there's the lighthouse that has a ux channel people share some of those in there. I think cmonkey82 is someone that's made a good one. I can also see joel dock has tried to convert it over to lighthouse but perhaps the prysm discord just reaching out there and seeing what people are using is a good idea.

**Leo BSC**: Right so we noticed that actually most of the clients already have a number of metrics that are already common to all of them. So I think the best way to start is to know to decide this common intersection between all the clients or at least most of the clients and start from that point. So I think in the document we added a small table where you can have
another contact person for each client. So if you can go ahead and philip, then we can
contact this person and try to set a common call and so we can all discuss what are the most common or like what are the metrics that make sense uh to most of the clients.

**lighthouse**: Yeah we have probably a thousand or something. So there's  quite a few but can't help out.

**Danny**: Are there any other comments or questions on the before we move on?

# 4. Research Updates

**Danny**: All right thank you Pari and Leo. There's any research updates you'd like to share today?

**Aditya**: I am happy to share that the new full choice spec is ready this has been in the works or a few months so pretty excited to share that. It's pr2292 on the spec repo. Please do check it out and leave comments and feedback and If there's something specific you want to talk about you can ping me or Danny.  The summary of changes for this pr is that the block restructure is changed. The way that latest messages are  accounted for has changed
during ghost execution and the happy news here is that there's no change to the network structures. So latest messages votes remain the same the way latest messages are structured remain the same and overall this has good security and good performance
and yeah we had a few setbacks in the research that was the cause for the delay but
it seems like this is a really good fix that we have arrived at.

**Mamy**:  Does that new fork choice imply that. We need to have two for choice implementation or can we use it to replace the world chain from Genesis?

**Aditya**: I think it should work so basically as long as that specific attack has not happened. The both folk choices are going to give the same result. As far as we know nothing like that happens since Genesis so that fork should be good.

**Dankrad**: I mean also it doesn't matter once it's finalized right. So only if we had a non-finalized chain that would matter in any way.

**Danny**: yeah both are rooted in finality and so you could imagine it in causing
a minor reorg in that stretch after finality if you switched it but that's fun.

**Dankrad**: right exactly but like once you have switched and you have finality. There is no need to remember the old fork rule.

**Danny**: Yeah exactly. It's written as such it is an change to the the phase zero to kind of
the base fork choice. 

**Dankrad**: Like I guess we can make it so that it can only get activated on finality or something like that and then you at least should never have to use both sport choice rules at once.

**Danny**: Yeah but even then in 99.99% of cases, if you just switch the fork choice, it's going to give you the same exact answer as the old one.

**Dankrad**: Right yeah I guess true you can just make it a rule that everyone implements the new fork choice at a certain time of the day and then that should also work here.

**Aditya**: right it would also probably be fine if some of the nodes have upgraded to the new one and some of them are operating on the old one but obviously that's um yeah might get tricky.

** **: Yes if we said that we were all going to change at some point in the day then that would mean that we at some point the clients need to have both of them right.

**Aditya**: Right that's exactly what I thought of Mamy's questions. I think yeah to make the transition there would have to be those two implementations living in the client at the same time. At least until we are done with the transition.

**Danny**:  Not even  worth that complexity because of anything you like. If there were
this type of attack, you might have a disagreement for some short amount of time but even justification and finalities still. It's not like you're removing things from your choice so things can still move on.

**Dankrad**: Right you are just adding. So I guess like we can probably easily show that there's no safety issue with having both at the same time right  and then I guess yeah Mamy is right like we can just make it an upgrade.

** **: Just get all the clients to release in the same week or something it sounds like it would be reasonable.

**Danny**: That's what I would argue yes but we can just think about a little bit more but that's my understanding. If we can it's safe to roll it out like that and something that we are looking for. Specifically as you look at it is just kind of like sanity check that engineering complexity and that of. This change is not massive that it can generally kind of use some of your same structures and algorithms in slightly modified way which we believe in this case
anything else on fork choice before we move on.

** **: just to be clear it's not for Altair, right

**Danny**: we are not currently planning on releasing it out in Altair. Again it is a modification of the phase 0 rule and so once we do have it inspect and we are considering it for merge we can have the conversation. we can re-up this conversation maybe offline about how we want to coordinate this. Okay other research updates.

**Mikhail**:  Yeah I was just going to give some updates on the merge. First of all we are changing the terminology a bit. So we now speak execution layer instead of application layer execution engine, execution payload execution block and so forth there is a corresponding PR in the stack repository and once this PR will be merged I am about to make a couple of
cleanups more in a separate PR. Then it will make sense to start working on making this back executable which has been already started by cellway. Thanks a lot for that. So, yeah also there is a spec for ryanism which is focused on the former proof-of-work clients and how to turn them into the execution engine and yep it's like I am almost complete so need to do some fixes in that yeah so that's probably it for the merge. Also we have a merge implementation call next week. If you want to discuss some particular technical detail regarding the merge just reach me out. I will add it to the agenda that's all for me.

**Danny**: Great and can somebody drop that Rayonism spec into the chat i think it's a really good document especially to get people up to speed on execution inside 


**Mikhail**: yeah i'll just drop it

**Danny**: thanks. Okay anything else on the research side?

# 5. Spec discussion

**Danny**: Great, spec discussion especially on Altair anything that's come up that
people want to discuss questions about?

# 6. Open Discussion/Closing Remarks

**Danny**: Great and any items in general people like to bring up on this call?

**Proto**: so besides the merge call next week we'll also do more regular calls for Rayonism. So if you're interested in staying in the loop you can attend these kinds of office hour calls. These are optional and you can hop in and out on the discord and yeah you're welcome to to help with the early merge work.

**Danny**: Great yeah less formal more just kind of catching up asking questions. okay and anything else people have to share or discuss today. Awesome again sorry about all the technical difficulties earlier we'll get this up on YouTube soon. Thanks for being with me. I have a good one. Talk to you all very soon. bye everybody.

----------------------------------------------------------------
## Attendance

- Danny
- Leo BSC
- Vitalik
- Jacek Seika
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
- Ben Edgington

## Next Meeting Date/Time : April 22, 2021 at 1400 UTC.


## Zoom Chat 
From Parithosh Jayanthi to Everyone: 03:21 PM
https://docs.google.com/spreadsheets/d/1OrToYWl-XeIfTItBM6iqEsWjynmXu0ctyOj-83qzBVM/edit?usp=sharing
From Mamy Ratsimbazafy to Everyone: 03:26 PM
Btw, eth2.0-API was tagged v1 last week.
so it can be target as a standard for monitoring?
https://github.com/ethereum/eth2.0-APIs/releases/tag/v1
From Cayman Nava to Everyone: 03:26 PM
https://github.com/ethereum/eth2.0-metrics
From Mamy Ratsimbazafy to Everyone: 03:26 PM
ah right: https://github.com/ethereum/eth2.0-metrics/blob/master/metrics.md
From Hsiao-Wei Wang to Everyone: 03:30 PM
https://github.com/ethereum/eth2.0-specs/pull/2292
From Mikhail Kalinin to Everyone: 03:37 PM
https://notes.ethereum.org/@n0ble/rayonism-the-merge-spec
New merge terminology: https://github.com/ethereum/eth2.0-specs/pull/2319