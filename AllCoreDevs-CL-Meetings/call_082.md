# Consensus Layer Call #82 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2022/02/24 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration: 1.5 hour  <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/484) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=fqPk576t5iw) <!-- omit in toc --> 
### Moderator:  Danny Ryan<!-- omit in toc --> 
### Notes: Avishek Kumar <!-- omit in toc --> 


-----------------------------

# Contents <!-- omit in toc --> 
- [1.Kiln office hours](#1-Kiln-office-hours)
- [2.Other client updates (if any)](#2-Other-client-updates-(if-any))
- [3. Research, spec, etc](#3-Research,-spec,-etc)
- [4. Open Discussion/Closing Remarks](#4-Open-Discussion/Closing-Remarks)

- [Attendees](#attendees)
- [Zoom chat](#zoom-chat)
- [Next Meeting Date/Time](#next-meeting-datetime)

-----------------------------------------------

**Danny***: Okay. Here is the agenda. If you are on youtube and you can hear us, let us know. Great, we will go ahead and get started with Kiln office hours as we have done past many meetings.Pari can you get us started with Testnet topics and then Mikhail you could tell us about  Klin  v2 and we can have open discussion from there?

# 1. [Kiln](https://hackmd.io/@n0ble/kiln-spec) office hours

## merge-devnet-4 updates

**Pari**: Sure, so merge testnet was launched  last week. We should have all client  teams participating now. I think  Besu is still doing some internal testing but they  should be done relatively  soon. We are  seeing something like a 99.7% participation rate. I think that’s even just  surrounding error from the beacon chain part or probably as high as it goes. Marius raised to find however that were only seeing 80% Sync aggregate participation and it is relatively stable at that number so it could be that some clients are not partaking not sure why maybe some Client  can look into  their notes and let us know if we need to change some configuration or if there was an issue.

**Danny**:  Yeah it definitely is so stable, it sounds like a particular setting. Yeah there we could probably very easily see that.

**Pari**: Yeah we just need to dig into that issue. I think that’s about it from the  testnet update. I would like to  know if you want to talk about  the Kiln v2 first or if you want to talk about Kiln public testnet readiness. Which order do we want to go on?

**Danny**: Public Kiln would be the iteration of the devs that turns to test.

## Kiln public testnet readiness

 **Pari**: Yeah, so  in chat if all the clients can just type in, if you guys feel you are ready or need some more time in general. I am thinking about launching the testnet at the beginning of next week, maybe Tuesday if that works for everyone.

**Danny**: we got at least one not ready in the chat. 

**Pari**: Just to clarify this would be Klin v1 not Klin V2. So you need to have Kiln v1 spec informative which should be the same as merge devnet-4.

**Danny**: Just the plan there is to make it a more public thing, but to still do a Klin v2 test net. or to migrate over to v2. 

**Pari**: I was thinking that we Just do a migration later once everyone’s ready so that we don't have to rush it but we still have a newer test now that people can start deploying things to remember your persistent one . 

**Mikhail** : And the newer one is the Kiln v1 . Right?

**Pari**: Exactly , but yeah there are two ways of doing this: either we get ready with Kiln v2 and then we launch a public testnet directly with Kiln v2 or we launch with Kiln v1 and upgrade it to Kiln v2.

## Kiln v2 spec

**Danny**: Mikhail can you go ahead and talk about Kiln v2 and anything that sure is coming out of that might make that difficult or not.

**Mikhail**: Yeah, so trying to understand well whether they upgraded like, it is gonna be smooth or not,okay for Kiln v2 we have two things in general. Like the major thing, first one is authentication and the other one is this new exchange endpoint, other than that we have renamed RANDOM to PREVRANDAO and there are a couple of related PRs to engine API and consensus spec. So there are some basic renaming of  the field from RANDOM to  PREVRANDAO to reflect these changes in EIP.

**Danny**: So that’s one of them because that makes it into the engine API, so that actual upgrading would have to be handled with care and handled on both sides of the client combo whereas most other things could be  handled probably  transparently.

**Mikhail**: Right, so yeah authentication , as we decided to keep the authentication port  for a while so it should be smoother than this. new Kiln functionality is also not a requirement for general use cases of engine API. So it is just on top of that it can be enabled at any point of time when you will find support. Clients start to support it widely.

**Unknown speaker**: Yeah, but this renaming is probably the one thing that is not backward compatible.

**Danny** : so If we were to move forward and just want to be on safe side getting renaming done before we move forward midnight remove some of the other headaches we might have in future,  But it looks in the chat that we have lots of readies and what  I interpreted as  not ready was maybe Just an exclamation point of excitement . 

**Marius**: Yes, super excited. I already like that we also started implementing v2 and should be good with it. Oh so we tested JWT that was fun and I added a new method but I still need to test it.

## Potential Kiln launch date

**Danny**: Right, when people say they are ready, does that mean they are ready with authentication? What is the state of authentication?

**Enrico Del Fante**:  Teku is ready for v2 including authentication and we also deal with backward compatibility in just an option by command line so transitioning between v1 and v2 will be simply restarted with the different option there and yeah, let’s foothill. Thank you.

**Terence**: For Prysm we have authentication implemented, but we need to test it still, so yeah .

**Gajinder**: Lodestar is ready. JW testing well  our authentication is working in CI with Geth. Basically our CI has a test run for working well.

**Marek**: Yep one of our team members tested  out authentication  with lodestar and it is working fine however we need to do some changes in authentication port and websocket support. 

**Danny**: I see a bit  of a range on the authentication being ready but very close. Is there a tangible difference in doing Monday versus Wednesday? Any opinion here or we are all just ready. Let’s do Monday okay? 

**Mikhail**: well this rename will be ready by. Basically what should be done  is just rename the structure that is used for Engine API communication on both sides. I guess in a consensus layer name, maybe it’s not gonna be backward compatible for the communication between clients. 

**Danny**: You can technically name that whatever you want. Yeah, it is that renaming of random to prevrandoa done on the engine API. 	

**Paul Hauner**: we haven’t done the remaining at last.

**Enrico Del Fante**: Yeah we need it and we actually internally work with always the latest name but we change runtime only the APIs 	naming to be backward compatible. We need to behave the old way. So we are all interested in API for instance, we expose a prevalent always but in the engine API. We use random for v1.

**Terence**: Yeah we haven’t done the renaming yet, but you should not take too long to do that.

**Danny**: All right, so we are probably in the mix on the name. The name will break the things on the engine API. If we do this Tuesday or wednesday. Can we all be conformant on that rename?

**Paul Hauner**: We are fine with the Lighthouse. We will probably stop supporting Kintsugi because we don't really  have the ability to swap the API name based on testnets. 

**Danny** : which I think is okay.

**Marius**: So sorry we are renaming part of the engine API. Right? Is this in v2?

**Danny**: This is in aPR that  was noted and in v2 as of yesterday, I believed Mikhail.

**Mikhail**: Yep it is in v2,  it is the changes that have. So it seems , It is also included in the latest release of engine API, so it’s now in the release before that it was like  a standalone PR on top of the release. So anyways, it is in the spec and it is very tiny.

**Marius**: Yes, I thought a Pari said we wanted to target , we want to target v1 for the merge for  denvent-4 going to be V2 . 

**Danny**: V2   other than his name change can be kind of done overtime because of the way that the API port has the old one. So this is the only thing that would make v1 and v2s not be able to talk to each other so I would suggest that everyone just change the name now because otherwise, we are gonna have a headache. The name change at this point is headache. But that API or that EIP around random had the name changed . so it was best to probably ripple it everywhere. Okay so I think Tuesday with name change rather than Monday with uncertainty around name change or wednesday if that’s what people need. 

**Pari**: I think that should work. On Monday I can just reach out to everyone and maybe just collect some information. So we know if we are ready by Tuesday in the worst case, we delete wednesday. I will try and get confit out on Monday as well so in case anyone is doing a last minute release , they can just include the config into make it easier to run clients.And beside that does anyone else want to run, validators,  genesis validators. If you do then please reach out otherwise we just follow the same principle as previous time. I just keep some validator keys aside for testing but basically the validator load would be handled by the EF.

**Danny**: sounds good. So Pari in your estimation, what are the changes that this upgrade to v2,this is what we stand up and tell you via blog posts and otherwise for people to come test and Join that’s the intention here.

**Pari**: Yeah , I guess we repeat everything we have done for Kintsugi,i in terms of outreach, so we get all the tooling updates, all the joining documents and ask people to redeploy their contracts and test on Kiln. 

**Danny**: Got it. 

**Marius**: I guess what would be really nice would be to have a longer period of proof of work before the actual merge. 

**Pari**: Yes , I was not just setting the difficulty like a hundred times more than what we have done so far, so rather than it being an evening, It will probably take a few days.

**Marius** : That’s  great and we can always spin up the old mining rig?

**Pari**: Exactly, you can spin up more mining rigs if you feel like it is too high.

**Danny**: Great, very exciting. Andrew?

**Andrew**: Yes, so I would like to clarify , so we all agree that we do the v2 renaming right in the test.

**Danny**: Yes

**Andrew**: and okay that was my first question, that's fine. The second question , what about the ports because I am very confused about which port should be authenticated and which port should not be authenticated. Can we clarify that we are on the ports?

**Danny**: Yeah Mikhail what’s the latest on that and I will pull up the PR to take a look as well. I believe there are two ports and one is auth and one is not auth. 

**Mikhail**: Yeah so basically yeah let me check. So 8850 right , unauthenticated one. great yeah and then our authentication we have this 8551 right so that’s probably like I don't know how it is implementedby your clients, but I think it is a reasonable fork number as they are specified in the spec. so we'll just have this authentication for it and Yeah, then we will just decide which one to remove. Yeah, it would make sense. Yeah to remove the one, yes
.

**Andrew**: It is not what Geth has implemented right? Or Marius, could you confirm what the plan is?

**Marius**: So what we have implemented is auth on  8550 respectively 8551 for WS for web sockets  and a well the other one you can choose where you want to put it but we also want to make the like .We want to make both configurable so you can run multiple nodes on your machine and that is not implemented yet.

 **Mikhail**: Do you have enough indicated work right now  supporting you?

**Marius**: No, we have the engine so still we have no unauthenticated version of engine API so you only have the authenticate you want.

**Danny**: Okay because the spec martin wrote I believe has unauth on 8550 and auth on 8551 obviously those are configurable you can move around but to allow for backwards compatibility in the transition, but that is not the case in Geth.

**Marius**: In the implementation, no.

**Paul Hauner**: can you still hit eth_ end points on the authenticated endpoint port?

**Marius**: I am not sure. I don't know if I have to look it up, but we provide the unauthenticated eth_ endpoints on the  north indicated port. 

**Paul Hauner**: like these the end point for getting blocks, so if we presently assume that we can get the engine and eth end point on the same port if we need to spread those across auth and unauth ports might be a bit more work around probably a bit more work for the user as well in terms of specifying different end points.

**Marius**: Yeah, I am not sure we might also provide the end point on the authenticated button, like I have to look at the code.

**Paul Hauner**: Yeah once again I think it makes sense for real clients to follow the spec and use numbers from the spec.

**Danny**: whereas these good defaults for sure. I mean overreading everything. Yeah. Okay so Andrew that the spec is in one state Geth is in a slightly different state but  a configurable state that's where we stand. 

**Andrew**: Okay so we will probably for the test network probably just maybe enable one non authenticated port which will be a 8550 and then we will like add authentication later.

**Danny**: Yeah I think that’s the reasonable path.

**Mikhail**: Yeah by the way is any CL client yet not supporting authentication?

**Paul Hauner**: what was question sorry who is not supporting 

**Mikhail**: Yeah who is not supporting from  CL clients

**Paul Hauner**: We are not supporting auth yet..

**Danny**: Maybe as we approach the weekend we throw a table for readiness for Pari to gather the information.

**Mikhail**: We have a milestone. We might want to add v2. 

**Danny**: These milestones can be useful. 

**Danny**: Okay Pari thankyou for coordinating the upcoming testnet.Are there anything else related to the testnet discussion as we prepare this week. Okay! Mikhail is there anything else on v2 or anything else you would like to just discuss with respect to spec? 

## Beacon API

**Mikhail**: I am not related to Kiln about the beacon API or what  we will raise later. I mean check it just wanted to check the state of this optimistic flag status.

**Danny**: Paul, do you have an update on that one?

**Paul**:  I need to fix some CI failures on my end. I think Teku handles many issues and they are going to go ahead with it, and there seem to be no objections from others, so will probably become the standard.
**Danny**: Got it.

**Arnetheduck**: I just have a minor point about the v2 versus v1. We check the current client and we are actually stick on not allowing fields in there.

**Paul Hauner**:  so v2 will be slightly more user friendly to support. I mean it is all motivated.

**Arnetheduck**: Yeah it kind of raises the question whether we should be ignoring what we considered to be an important security  flag and if it is not in the important security flag and why it is there right? I mean semantically we are changing the meaning of the message.

**Danny**: Should we talk about it on the [PR](https://github.com/ethereum/beacon-APIs/pull/190)

**Arnetheduck**: Yeah I am fine with it.

**Danny**: Mikhail There is also an open PR to better define the eth_ endpoints to be served over the engine API.

**Mikhail**: Yeah that 	is not gonna impact that does not require an engine. There is a small clarification on this exchange about transition configuration stuff.

## Kurtosis

**Danny**: Let's move on to a testing discussion, Kurtosis, a team which presented it to all core devs on friday about the simulation automation framework that they have been working on want to help with testing merge. they are gonna have a breakout tomorrow at 1400 UTC so at the same time as this call but on friday and they are gonna to help people better understand what the tool does and how you might think about using it for testing your client , maybe doing some CI integration that kind of stuff. Team you can check it out. Any other testing item people want to discuss today. 	

## Shadow forking Goerli

**Danny**: Are we planning on Shadow forking Goerli with Kiln v2 once that kind of get ready.

**Pari**: Yeah that’s a plan we probably make it a bit semi public and people can use that for sync testing if they want. If anyone has ideas for automated tests to run while shadow forking Goerli please contact Mario or me.

**Danny**: Okay great. Another thing related to testing people want to discuss the call. Okay any other related to merge people want to discuss in the call.

# 2.Other client updates

## Nimbus

**Arnetheduck**: there is one update I would quickly share about Nimbus, so we managed to implement both client and server for light client sync. It takes the trust relationship out of the REST API.

**Danny**: How do you trustlessy bootstrap the light client committee?

**Arnetheduck**: I am not sure about the details now.

# 3. Research, spec, etc

## Benchmark.

**Leonardo Bautista**: I have plans to re-assess client benchmarks on Merge testnets, and will be contacting teams in respect of this.


## Withdrawal

**Danny**: EF research team is actively discussing different withdrawal designs. E.g. push vs. pull. It was determined that pull is the only viable method on the execution layer for 0x00 withdrawal credentials, but 0x01 credentials might support either. I am  making two sample PRs, one for each case. [Some technical discussion ensues…].

## Safe head block

**Danny**: okay Safe head block

**Aditya**: I am going to share my screen if that helps.

**Dankrad Feist**: Okay if you want, yeah of course.

Please refer detail presentation note for  [“safe-head” confirmation](https://notes.ethereum.org/@adiasg/safe-head) rule

**Danny**: So point being is there is an engineering question around if this algorithm can be officially implemented using the data that’s already in protoarray light? 

**Aditya**: Yep that’s it.

**Danny**: Are those questions written down somewhere in this document?

**Aditya**: yeah  this should be covering the questions but I will also make it explicit. I will edit it to ask the question more clearly. 

**Danny**: Okay cool. I would share the document and then maybe contact one or two client team directly with the question and see if it can be attractively solved and formulate how to solve it from there, is that reasonable.

**Aditya**: Yeah, that makes sense.	 

## Other

**Danny**: Anything else to discuss

**Proto**: Team made a demo of “blob transactions” (data availability) at EthDenver. Preparing an EIP, and it will also involve consensus layer work.

 **Danny**: there is a document on the work that you can share that is not in a very good shareable speed state.

**Proto**: During or at the end stick at that of the act on, we had prepared a document outline the changes of the specs of the execution layer prototype associated. I will share that in the chat,

**Danny**: Yeah,  I think we are good. Pari we can shut down those paramount nodes. Well actually it would be interesting to see if there are any weird load things that emerged but not super critical. Okay and final reminder Kurtosis testing breakout room tomorrow at 1400 UTC okay thankyou.	

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
- Leonardo Bautista
- Arnetheduck

## Next Meeting Date/Time : March 10, 2022 at 1400 UTC.


## Zoom Chat 

- From danny to Everyone 02:02 PM

https://github.com/ethereum/pm/issues/484

- From danny to Everyone 02:23 PM

https://notes.ethereum.org/@timbeiko/kiln-milestones

- From pari to Everyone 02:25 PM

Current versions used in merge-devnet-4 can be found here: https://notes.ethereum.org/D5xK4XrmTb6MKGudf_hcrg
Would be great if client teams can update it if/when there are new versions
We use that doc as the source of truth for other setup docs

- From Marius Van Der Wijden (M) to Everyone 02:34 PM

All namespaces (eth etc) are available on the authenticated port
cc Paul

- From Dankrad Feist to Everyone 02:40 PM

Next Adias and I would like to discuss the safe head rule: https://notes.ethereum.org/@adiasg/safe-head

- From Micah Zoltu to Everyone 02:42 PM

We still expose the head to execution layer, just via unsafe_head.

- From danny to Everyone 02:43 PM

yes
safe takeover latest is the idea
and a new keyword is added — unsafe

- From pari to Everyone 03:05 PM

EF would exit and shut down our Pyrmont nodes soon, please yell if we shouldn’t


