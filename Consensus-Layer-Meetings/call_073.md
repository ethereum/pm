# Consensus Layer Call #73 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2021/09/23 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  1 hour  <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/237) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=Pes_OaMJeDc) <!-- omit in toc --> 
### Moderator:  Danny Ryan<!-- omit in toc --> 
### Notes: Avishek Kumar <!-- omit in toc --> 


-----------------------------

# Contents <!-- omit in toc --> 

- [1. Altair](#1-Altair)
- [2. Client Updates](#2-Client-Updates)
- [3. Merge discussion](#3-Merge-discussion)
- [4. Research Updates](#4-research-updates)
- [5. Open Discussion/Closing Remarks](#5-Open-Discussion/Closing-Remarks)


  - [Attendees](#attendees)
  - [Zoom chat](#zoom-chat)
  - [Next Meeting Date/Time](#next-meeting-datetime)

-----------------------------------------------
#1. Altair

**Danny***: All right, the stream should be transitioned. Here is the agenda, major goal is to
make decisions on Altair as much as possible. Thank you.

## sync committee performance

**Danny**:  Members of the research team and members of client teams working through data analysis and bug fixing around sync committee performance. Proto has quite the graph on that issue, if you want to look and the fact that all of the software that all of the nodes that we run look blue. At the end of that graph is a good sign and as far as I know our sync committee troubles have been fixed. Does anybody have any other comments on the sync committee investigation? Any outstanding issues? Any important things they learned fixing those issues? Okay so..

**Jacek Sieka**: I can just briefly mention the problem that we had, yes it was kind of funny so we have this anti-DoS protection and lipb2p which adds some extra filtering because when people subscribe to gossip. Technically you could send lots and lots and lots of subscriptions and fill up our subscription table and like make numbers, use lots of memory so we had a special filter there and we kind of forgot to add the sync topics in there so it was kind of sad   as far as bugs go.

**Danny**: Oh! I guess one question is, do we have sufficient monitoring in place? Now I know we have sufficient debug tools. But I will be aware of issues because I felt like this issue kind of set for a while without anybody maybe being aware.I am not sure if that's the truth.

**Jacek Sieka**: I mean we were kind of aware but we are looking in the wrong places so, we are looking into that filter as well to make it louder.

**Danny**: cool, any other comments on the investigation issues found where we stand with respect to this feature.  We are generally good.I know that nimbus had. I think there were a
number of patches, not just Nimbus. We don't have to go over all of them but just anything else we want to discuss here? 

## Upgrade epoch selection

**Danny**: Okay, so last call two weeks ago we had a number of things we wanted to get. One additional testing on Pyrmont which  Pari carried out. Some I believe we had a release of additional test factors in that and we wanted to fix the Altair. The sync committee performance which came down to the wire. We wanted to talk about a fork date today. A fork date would imply client releases. Mainnet ready client releases no later than two weeks prior, maybe 16 days prior, so that we can do a blog post 14 days prior at the minimum to get people ready for an upgrade. Tentatively we talked about doing releases at the end of september that's the end of next week. Maybe doing a blog post a few days later and
doing an upgrade mid october. Maybe october 18 20th something in that range. Where do we stand on that? Do we feel like we have the same amount of confidence? are we ready to do this? Do we have new information and need to make a different decision?

**Ben Edginton**: Speaking of teku ready to go but would prefer to see 3 to 4 weeks lead time just because the big operators will take longer to upgrade. I expect there will be more due diligence around it. I want to make sure everyone's got time.

**Danny**: So 3 to 4 weeks from releases plus blog post to mainnet date. Right ? Okay, so releases but you all are still on the we can release kind of pre-october and then a 3 to 4 week lead time from that.

**Ben Edginton**: Yeah I believe that's doable yep for us yep.

**Danny**: Got it,  anyone against such a release timeline especially on that you know release by end of september. Okay so let's uh let's pick a date. My calendar I think kicks me out every four weeks at the exam at the same exact time and I have to relogin. I think it's literally during this call because it's happened another time. I am trying to log back into my calendar. I apologize.

**Micah Zoltu**:  Set a calendar reminder to log into your calendar tomorrow.

**Danny**: This is ridiculous. I was literally logged in I think eight minutes ago. Okay I am back in. We are back in and I can see it. Okay so we have the end of next week that thursday. Friday is september 30th September and october 1st so we could target our releases for the end of next week and a blog post that monday october 4th. Three weeks out from that is the 25th plus a few days to get into the middle of the week is the 27th,28th. Do we prefer it? Do we have preferences on Wednesday or Thursday for a fork day? someone's gotta have a preference.

**Paul Hauner**: Middle of the week sounds good today. It's further from the weekend. 

**Danny**:Wednesday. Great and if we do Thursday it'll be almost Friday for you. What was that Terence?

**Terence**: No, I was going to say a wednesday

**Danny**: Okay,  wednesday 27th. We can pick a precise fork. Epoch using Adrian's sweet tool right after the call and make a PR to configurations. Does that sound good? Is this the target? What was that, I missed Micah. I am sorry. Okay so say it out or get out loud again
end of next week client releases, mainnet releases. A blog post by the EFand anyone else
that wants to join in on october 4th to discuss dates upgrades and client releases that then three and a half weeks from that point is october 27th which over the next day we will select an epoch on that date. Anyone against what I just said?  Okay, let's do it. Any other Altair discussions or comments before we move on?

# 2. Client Updates
 
**Danny**: Great, let's go through some client updates 

## Teku

**Danny**: We can start with Teku.

**Ben Edginton**: Right design, let's start with introductions so we had a couple of new joiners, Reggio's been around for a few weeks and is in Australia and not here.Enrico joined
last week and is in europe and is here . so welcome Enrico on the client side. We fixed an issue that came up prior to the network. We first saw it there in there was a rare edge case where Teku would fail to produce blocks.It's some kind of weird race condition where we would see an attestation first in a block and then later receive it via gossip and then there was some other sort of weird conditions and when it all coincided. We have failed to produce a block later. It was rare on prata and we have not seen it on may net or had it reported but nonetheless. It's fixed in 21.9 which is the most recent release there and other minor things. We have upgraded to Blst 0.3.5 which came out last week. We now have support for building on JDK 17 which is a newly released long-term support version of java and we're working on merge support in a dedicated branch and various other minor bug fixes and bits and pieces as usual. That's all I have got.

**Ben Edginton**: That sounds like a painful bug to debug. Adrian is astonishingly good at debugging.

**Danny**: Excellent, Prism

## Prism

**Terence**: Yeah hey guys so on a tear front,  we're just chugging along. We have merged everything into the canonical development branch. so that's done so right now just a few minor budget fixes with the RPC endpoint and then a few optimizations here and there so far is looking pretty good on our end and then we are also gearing for the v2 reduce which will be at the end of next week. They are reduced from 10 slashers.We also reorganize package structures to be more draw-like. Also align all the matrix namings all the system, standardization and all the good stuff  and like tech who were also working on the merge spec support on a dedicated branch and yep that's it from us.

**Danny**: okay thank you terence nimbus

## Nimbus

**Mamy**: Hi, so we've been working on passing all the new tests uh also the one from
Blst as well or last week was focused on making sure that pratya worked so we had issues 
regarding sync committee messages and also a low number of peers that we are debugging or have debugged. We want to do a release next week well so the timing is good to fix everything and make sure that main release is rock solid for prater and Altair

**Danny**: great thank you Lodestar
 
## Lodestar

**Danny**: Is anyone from let's start here Loadstar progress continues. they have a mainnet validator that I think is doing quite well these days and continued on light clients and getting Altair refined next up lighthouse

## Lighthouse

**Paul Hauner**: Hello paul here so this week we merged two big pr's into our unstable branch, so they were weak subjectivity sync or checkpoint sync. So we can now with a trusted api endpoint. We can now sync from scratch to head in lessthan a minute which is pretty cool. We have been playing with that and having fun. We also emerged batch bls verification and attestation signatures so that sees about a 40 to 50 percent drop in cpu load average on our prada nodes so that improvement is significant when it knows it is subscribed to all subnets. Still noticeable on other nodes but much less so we're likely pushing a release candidate of version 1.6.0 next week and that'll include those fixes. Michael did some analysis on client distribution across validators by fingerprinting attestation packing characteristics and got some attention on twitter was pretty cool. We're working on our implementation of  the merge, getting ready for more testnets very soon and Adrian Manning has been working on reducing the p2p bandwidth. He seems to have over 50 reductions at this point but we're still monitoring to see if it comes with validated performance costs. That's it from our end.

**Danny**: On the lib p2p bandwidth. Do you have a tldr on that?

**Paul Hauner**: I haven't been paying attention. I think he is trying to reduce gossip duplicates by reducing his mesh size or something like that and not super clear on it.

**Danny**: Got it. Thank you paul. Grandine

## Grandine

**Saulius Grigaitis**: This is Saulius from Grandine team so we are still focusing on the multiple runtimes, refactoring and regarding the Altair we can sink the chain now and we still need some work on the validator side and I think maybe in a couple of next weeks we will be back on the broader.

**Danny**: Got it. Thank you

# 3. Merge discussion 

**Danny**: Okay, Moving on to the merge discussion. We are working very diligently. Meguile myself and many others on refining initial interop specs for the merge. We expect a release tomorrow on the consensus side which would be kind of a stable target for initial interop in the start of october. Additionally you know on the on the
execution layer side . We would have that EIPIP stabilized and also there is a minimal version of the execution api of the engine api. Here that's being put through the ringer and we expect to stabilize again in about 24 hours for release so that we can all have a common target moving into October. That's the main merge update on my end. anything else, Mikhail or others.

**Mikhail Kalinin**: Ah!  Thanks Danny for the update. I don't have anything to add here. I was just going to say something like you already did.

**Danny**: Mikhail, what are you going to do? Put all the links kind of in a single place as something like a meta spec for initial.

**Mikhail Kalinin**: Oh yeah right right. Yeah I have started to work on this document. It shouldn't be that long. I mean just spec versions and fill in the gaps that we have in this pack like what to do with the random field on the execution client side. So because we don't have any eip for that yet but.It is already specified in the consensus specification. So cool that should be finished tomorrow within the spec release I guess.

**Danny**: Great and if you all haven't taken a look. I mean primarily what we're dealing with is upgraded types and this communication protocol from the consensus side, so order of magnitude simpler than Altair. I would suppose especially now that clients have kind of a standard fork. Mechanic path in the code base so take a look any questions about the merge or comments or discussion points.

**Paul Hauner**: I am keen to get my hands on an execution node that has the api implemented. Yeah if anyone has that kingdom key to play with it.

**Danny**: I am not sure who is farthest along. Hopefully that would be something relatively soon pro and others were thinking about actually mocking an execution engine or mocking the consensus side for testing of the api proto. Do you want to talk about that a bit?

**Proto Lambda**: Right so what we learned from rainism is that once you have many clients talking  to each other you have this quadratic integration issue which can really suit you. It can delay things and so instead I would like teams to focus on sharing more tooling and trying to share testing and this one of these things that we can share is a mock version of the beacon node. A mock version of the engine mod that conform to the specification are lighter run and you can test against and once we can have all consensus clients work against the mock exclusion engine and our exclusion engines.Mock work against the mock consensus clients then we have a much better chance of interrupt.

**Paul Hauner**: Yeah I totally agree.I had a lot of trouble last time trying to get matches
because the serialization formats between the consensus clients and execution clients are quite different. Just in the way that we know serialize byte string hex strings and stuff like that. so it'd be super useful. I think I published some test sections last time. I will do the same once I can get it up but yeah a mock thing would be really handy Ii was going to produce one on our end because we are going to need it for unit testing as well in CI so we don't have to spin up a whole other execution chain.

**Jacek Sieka**: I mean on that note one thing that I have been taking mental notes for and and some real notes as well is that the execution api is kind of this private ish api between the big like the consensus client and the execution client. They shouldn't really be exposed to user applications like normal user applications and that means that it kind of could live in a separate space in the execution client now for many many reasons. we choose rest to talk between. You know VC and BN also for encoding purposes. It would make a lot of sense if we continue to use rest between consensus and execution but like before making that PR. Is there anybody that's going to like loudly scream and inject right now or is there something worth considering? I think it would be a big simplification for the future. If we want to kind of focus on just one kind of encoding and one kind of api style Tommy.

**Danny**: The primary pushback is the execution layer already has a json rpc interface.It's suggested to be exposed on a different port for some sort of separation but at the end of the
day. It's a compromise in one way or the other in terms of formats required because the user api on the json rpc is not going to go anywhere. This has been debated a bunch I am I just
wanted to provide that for context I am not going to throw my hand in the ring too much

**Paul Hauner**: My understanding is that we used an rpc because this type of communication is not suitable to rest. We need it because we can't really load balance.The execution node because we need to stay in sync so eventually. We are going to have a protocol where the execution note is going to be. I actually don't know that block that you
were that you refer to and then we have to push blocks to and we have to  create this very much rpc style sync method between the two that was my understanding is why rpc was chosen.
**Jacek Sieka**: I think they are fairly similar in that aspect. I mean if you read the two specs there is very little actual difference between them.The reason why I am mentioning it even is like one of the heaviest arguments in favor for rest when we were choosing it back then was actually like experienced from ethereum one. If you look back to that discussion when we were choosing rest. It's actually like the current execution client developers that were one of the fiercest advocates of it.

**Danny**: Right but one of the primary reasons was  it's a user api that might have needed load balancing and all sorts of other. 	Nice things that are going to fall out of a restful api whereas this doesn't have the same requirement. I think is what Paul's arguing because
It's more of a one-to-one relationship. But again I am not gonna go too deep in here. I know it's kind of gone back and forth a couple of times and ended up setting on json rpc for simplicity because that is already just embedded in execution layer clients.

**Mikhail Kalinin**: One more argument here is that rest is tightly coupled with http protocol while the json rpc could be implemented on top of any communication protocol like tcp websocket. Yeah I guess the rest will be done in websocket as well but I don't think that rest suits us well here because rest is good in accessing and updating some resources while this communication protocol is more like updating the states and syncing the states between two clients. so it's not always that each request and response corresponds to some logical resource.

**Danny**: From a practical standpoint of just getting this api ready to be used tomorrow for
people to build and then initially do some interop at the beginning of October I think there's probably zero chance it's going to change but if there is a compelling argument and you want to continue to have the conversation and try to change it after that's probably the path I will sleep on it. Cool anything else merge related. Yeah with the release tomorrow there
will be  at least kind of a minimal set of consensus vectors available on the consensus side. So keep your eyes peeled any research updates other than merge.

# 4. Research updates

**Leo(BSC)**: Yeah on our website I wanted to mention that our paper on the ethereum network crawler has been accepted for publication in the IE international conference on blockchain computing and applications that should be held in Estonia in November. I will add the link in the chat and also regarding the crawler  just a couple of days ago there was another  client distribution analysis that came out done by Michael. I guess many of you have already seen it. It's a completely different method that is derived from block proposal data and the distribution that came out it was astonishingly similar to the distribution that we
showed in that. We demonstrated with our crawler several months ago. So I think this kind of validates a little bit the data that we have got and shown over the last few months.I am gonna add the link to twitter so you can take a look at it. And yeah on the other paper that was accepted. Concerning the entering plans. Resource utilization is going to be presented next week at the conference on blockchain research and applications for innovative networks and services I am adding the link to the program in case somebody is interested to
take a look. I think the registration is free. Yeah so that's  research updates on my site.

**Danny**: Thank you.

**Mamy**: Regarding crawlers, there is one that underestimates Nimbus or always connects to Nimbus nodes. I don't remember the team that yes right,  so there is one thing that there is a difference like some clients allow crawlers to connect and then eject them while numbers don't allow them to connect at all for example and there are different behaviors between clients that makes statistics a bit tricky sometimes.

**Danny**: Right and I think Cerium is actually maybe having a very large Nimbus pure store and dumping it  and so they are seeing like actually what you see from that is like biases and how Nimbus connects to and doesn't connect to clients over time. I believe  that was my understanding of it when I spoke with them, and I am actually surprised how close the Michael Sproul validator metrics were compared to the crawler. Metrics we have seen I expected some more asymmetries between size of validator allocation and the nodes in the network Paul

**Paul Hauner**: I was just gonna say that I was talking to the esteriam person as well and they were using it. They were dumped in Nimbus' peer story. I think they had like 40 percent of the network was Nimbus or something like this. Yeah I think I mean trying to crawl is very hard and people need to really consider thinking very hard about it when they do it. Not just dump peer stalls and cat peers.

**Danny**: Agreed. Okay anything else.

# 5. Spec discussion/Open Discussion/Closing Remarks

**Danny**: Any open discussion, closing remarks, anything else people want to discuss today. I am going to suggest that we do not have our meeting two weeks from now because the number of us will be in person working on merge interrupt and Altair will be kind of progressing along. I would say we only  do a call or some sort of formal gathering in the event that we are having, some sort of issue or hiccup with the Altair progression at that point and then we would regroup again on the 21st of october which would still be before the Altair upgrade for any kind of final or emergency discussions then cool.
 
**Jacek Sieka**: I would have one question actually to client teams. I mean we are still seeing a little bit of missed attestations and so on. I was curious about the latest investigations too. I mean orphan blocks were one thing so when those things were fixed but if there's any news on that front maybe releases that address potential issues and cure incoming attestation queueing things like this.

**Terence**: Yeah so on the prism front we have a bunch of optimizations that improve that
and it was released in the previous release but those were actually part of the feature flight set. So basically in order to use this optimization feature the user needs to enable the flag just so the user knows what they're doing so now with enough testing for our v2 release those flags will be flagged. Those flags will be flagged or into the default state so most of the
other transactions will be enabled so we should definitely see some improvement there from our end.

**Danny**: Yeah so specifically what we saw and some uh analysis left by Barnabay was that there are these like zero. Zeroth epoch, zero slot blocks that are late and kind of hap increasingly so that cause issues with voting on that epoch boundary cusp and that from what we can tell is primarily the drop that we've seen over the past handful of months and using graffiti analysis. It was did generally happen when prison validators were voting were proposing at that epoch boundary and what terence was alluding to was they have quite a few optimizations for that epoch boundary, one of which is just not waiting just in time to do it and kind of when you're at the prior to that boundary and you know kind of what to build on. You can optimistically just do that epoch transition, get the shuffling in place and stuff.

**Pau Hauner**: l think I know Micah was looking into  it as well. I think he found some cases where clients weren't packing, attestations to blocks as well as they could. I think he's reached out to those teams and they are aware and doing stuff about it. 

**Danny**: Yeah the nice thing is we have a required upgrade in late october where any of these optimizations have been kind of filtering out. Will all be enabled at that point so that you know our  data point as to whether what we've been putting in place on packing and putting the place on these zero slot optimizations. Epoc transition optimizations are actually going to fix what we think they're going to fix. Anything else on that?

**Jacek Sieka**: All right, cool,  thanks.

**Danny**:  Other discussion points. Okay cool, thank you, We will  regroup in the chats to figure out a fork epoch and get that up in the configs. Good work everyone and releases at the end of next week talk to you all soon. Thanks all bye



 ----------------------------------------------------------------
## Attendance

- Danny
- Leo BSC
- Vitalik
- Grandine
- Paul Hauner
- Jacek Sieka
- Mamy
- Adrian Sutton
- Lion dappLion
- Patricio Worthalter
- Carl Beekhuizen
-  Lightclient
- Nishant
- Dankrad Feist
- Justin Drake
- Cayman Nava
- Mehdi Zerouali 
- Cem Ozer
- Terence
- Hsiao-wei wang
- Aditya Asgaonkar
- Alex Stokes
- Mikhail Kalinin
- Barnabe Monnot
- Zahary
- Pooja Ranjan
- Ansgar Dietrichs
- Proto Lambda
- Ben Edginton
- Leo BSC

## Next Meeting Date/Time : October 21, 2021 at 1400 UTC.


## Zoom Chat 

From Micah Zoltu to Everyone: 03:10 PM

What time of day is the target epoch going to be?

From protolambda to Everyone: 03:11 PM

https://slots.symphonious.net/
Click upgrade-scheduler tab

From danny to Everyone: 03:19 PM

https://github.com/ethereum/execution-apis/pull/74

From Leo (BSC) to Everyone: 03:29 PM

http://intelligenttech.org/BCCA2021/ https://twitter.com/sproulM_/status/1440512518242197516
https://brains.dnac.org/program-2/

