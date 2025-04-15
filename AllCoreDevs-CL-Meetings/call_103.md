# Consensus Layer Call 103

### Meeting Date/Time: Thursday 2023/2/23 at 14:00 UTC
### Meeting Duration: 45 minutes  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/731) 
### [Audio/Video of the meeting](https://www.youtube.com/live/io7ALEfxJsE?feature=share) 
### Moderator: Danny Ryan
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
103.1  |**Testnet updates:** Devnet 7 was shut down this morning. Everything seemed fine, with 359k BLS changes processed, but not running final client versions. Plan to run one more large devnet just after the Sepolia upgrade. Overall a very good test.
103.2  |**Testnet updates:** Zhejiang testnet continues quite stable. MEV-boost happy-case seems good. All clients supporting it. Next, on MSF-2 (mainnet shadow fork), plan to test some edge cases, but Capella fork time is not yet set for that.
103.3  |**Testnet updates:** Sepolia [testnet upgrade announcement](https://blog.ethereum.org/2023/02/21/sepolia-shapella-announcement) is out, and a couple of updates coming very soon: new Geth version is available, and Lighthouse version is now announced. NB the validator set is closed on Sepolia.
103.4  |**mev-boost update and SSE subscriptions:** end-to-end MEV-Boost system is running on Zhejiang. Builder specs are merged and updated. There is a bunch of open PRs on the relay; they are running fine on Zhejiang and will be merged and released soon.
103.5  |**Beacon API discussion:** For version 1.3 of the spec, can ignore anything Deneb-related as far as getting a Capella version of the Beacon API spec out is concerned.

## Intro
**Danny**
* Okay, welcome to Consensus Layer Meeting 103. This is issue 731. In the PM repo. We'll go over Capella 4844, which maybe should be renamed Deneb on the agenda. 
* Then general open discussion if anybody has any, any points from there on Capella, DevOps folks or otherwise. Do we have any test net updates to share? 

**Barnabas Busa**
Sure. I can start with saying that we have shut down seven this morning. we did this as, the last, big, updates. everything seemed quite alright. We managed to get 359,000, yes, changes through, so everything was good. my only concern was that we were not running the final client versions yet, 
* So I would like to run one more large, dev net, just after Sepolia Fork in the beginning of March, just to make sure that everything is still right, but, everything's in okay on devnet-7

**Danny**
Cool. So before the fork, those were kind of preloaded into the pools, and then, were any messages dropped? 

**Barnabas Busa**
* So the problem was that, some clients needed some restart to update their clients after the, after the fork. So it's very hard to know that, what was actually dropped before, what has that, because, when I restarted, I was to republish those messages, so I see. 
* That's why, yeah, that's why, a new, devnet might be needed here. And, we final versions without requiring any more client updates. Overall was, a very good test, I think because we, we did catch some issues with the, deposit queues and such. So everything looked good. And then the testnet, everything looks quite stable still. 


**Pari**
* And just following up on that, on the Shan Testnet, we started testing relays and, testing MEV boost in general, we are good on the happy case. So now all clients support, MEV Boost and we're getting blocks built and proposed by all client combinations. 
* The next step is to have it running with the edge cases  on withdrawal mainnet, shadow Fork two and main Shadow Fork two was launched yesterday, but we haven't set the Capella Fork yet. We're mainly waiting for more relays to come online so that we can test circuit breaker conditions as well as some failovers, etc. But we'd pro most likely be doing this over the next week. We're still waiting for some days to come online. 

**Danny**
Fantastic. Thank you. And, we'll get into me Boost update shortly. anything else on test net before we move into, some of the hive testing progress? Okay. and there, the Tim, on the Sepolia testnet, net fork announcement went out, right? 

**Tim**
* Correct. And, two updates to the blog post that should be merged in the next few minutes. Our, geh has put out a new recommended release, so V1 point 11.2, the one in the blog post now is still fine, but they recommend switching to the new one if you can. 
* And, lighthouse, had not, put out a release when we published a blog post, but  it's been put out yesterday. So, V3.5 0.0 for Lighthouse, is the right version there. and yeah, the blog post should reflect that in the next hour or so. 

**Danny**
Great. And if you're listening to this, if you're a validator, this is a closed validator set, so Goly, will likely be the place to test your valve. Your stuff though, in infrastructure providers, Sepolia is a great place to be testing. Okay, let's move on to, Mario, let's, you've been working on some hive, MEV Boost Builder API stuff. Can you give us a update on that? 

## mev-boost update and SSE subscriptions [16.39](https://youtu.be/io7ALEfxJsE?t=999)
**Mario**
* Yes, of course. So I prepared this, this page with the results. Basically, we build a, we built a, hive builder api, a simulator. What this, contains is a builder mock, which basically simulates a working, builder api, module that, uses the execution client to relay build payloads to the, to the, to the consensus client. 
* So yeah, every time the, the consensus client, requests a builder api, a builder, payload, it simply relates the information back to the execution api. And with this, we have like a simulator and our environment where we can, crash or return, invalid ballots to the cl on demand. 
* And in this page, I, this is the result, of one simulator where basically we have a working builder up onto Capella, and then after Capella,  we start,  re we start returning invalid payloads in a way that, the blended payload looks legit legitimate, but when the, when  the payload is blind,  you can see that the state route of the  execution payload, it's incorrect. 
* So what happens here, is that, after the ambling you can, you have return and design, beacon block, but this is symbol, so it will not add, be added to the beacon chain.
* And with this, we are,  we can start simulating the scenario where, slots start getting, start getting missed. So, well, after this,  we are basically just trying to test the circuit breaker in this scenario. And you can see all the results of this test here. basically, the case for Lighthouse prism is that they start, currently, circuit breaking, the builder after nine miss slot in the current pac. And this is working correctly. As you can see, there's, a maximum of 17.1% of the slot myth in the, in this scenarios. and then we have, but we have our load star nimbles, we have these scenario that they don't stop requesting. 
* So basically under the beacon chain circumstances that the builder API starts simply causing missing slots, depending on the client combination, we this here, with the, two client types per, per simulation, and they, and then we, we have all combinations here for all the client types and, the one the ones that, filled most slots, even when the malfunction builder are the lighthouse of presents. 
* But if s are, our nimbles are included in the, in the 50% on the evaluator TSET basically the field slot, presentation, drops quite a bit. So, yeah, to summarize this will breaking, tests are working correctly for the prism, but the , other clients are, exhibiting some kind of issues. 
* And yeah, they, the test is currently where IR reproducible using, hive, I include all the steps here to reproduce it if you, if you'd like. And yeah, we can run it again, if you make any modifications to the breaking logic, we can run any, any test again that you, that you require. 


**Danny**
* Yeah, so importantly to note, we decided before bellatrix that the circuit breaking logic would be left client to client  on the parameters and how they perform that. And so, it's not specified that it is a must and it's not specified exactly how many slots. 
* So, my question to Nimbus and Los Stars, do you, you implement circuit breaking logic or is this the expected behavior? 

**Gajinder**
* We actually implement, the circuit breaking logic and we are on the conservative side. In fact, we start with, disabled builder and we only enable it when we see, some percentage of slots, properly, being proposed in the network. So, we are basically on the conservative side and I can look into the test and see what's going on over there. 

**Danny**
Okay, great. Thank you. Zahary?

**Zahary**
this is actually a gap in our implementation. We haven't implemented, the latest proposal yet. 

**Danny**
Okay, great. So, so Mario, yeah, given that the, this is not specified, you kind of will need to parameterize these tests on the expected slots per, I suppose, so you know, Nimbus I wouldn't say is failing Nimbus is doing as expected, whereas it looks like load star, you know, is, is not performing as expected. but this is awesome. Thank you Mario. Any other questions for Mario or Mario, did you have something? 

**Mario**
No, basically just what the test expects is just final session, which happens every time. I assume it's because even though we have missed slots, both clients are actually attesting to the available slots, so Right. We Are always getting final session. 

**Danny**
Okay. we might consider that being like a recovery of a percentage of slots rather than finalization. just I think that'd be a more valuable red or green, but we can talk outside this call. 

**Mario**
Of course. Thanks. 

**Danny**
Okay. Anything else on test nets or testing for Capella? There was a new release, primarily this deals with  for Dan Kun, but there was an additional test, for an Edge case found by Paul. I believe most of y'all have, integrated those tests in our passing. but just that's relevant here. Okay, great. Chris I believe has joined us from, flash bots to talk about mabu updates in relation to Capella. 

## mev-boost update and SSE subscriptions [23.30](https://youtu.be/io7ALEfxJsE?t=1410)
**Danny**
* Chris, Hello. Quick to be back. I wanted to share a quick update where we are with MEV Boost, implementation on the various cards and the testing. So we are, successfully, having the whole end-to-end system running on the session  network. The changes are implemented in MEV Boost and the in MEV boost itself, they are finalized. there's also a release out there, by the way, let me share a document in the side chat where I put together the current status across all the projects and links the pillar stack specs. 
* They are merged and updated. special shout out to Chen on the MEV boost relay. We have a bunch of open PRs that are leading one into the other and that we are running on she young and that is working. I think we are wrapping these up, today, tomorrow. And then by early next week we have a final mev boost really release. But any other mev boost relay that builds on our code base can take a look at these, PRs that are also linked in the documentation and, and get a pretty good understanding what has changed or even any other rule that wants to upgrade and  need some pointers. please take a look. I think the, this is four PRs. They are nicely separated and the last one is to automatically switch between Bellatrix and Capella. 
* That's the new functionality that we added yesterday. The builder is also updated the validation node. Also Prism, we implemented the get withdrawals API in our Prism fork because they really needs to know about the withdrawals to validate the bill submissions. It would really be nice to, remove our custom fork. We, would need this SSE event that notifies about new payloads and payload attributes. There has been a bunch of discussion about that and like a reignited interest. And  let me link the issue here. So if we could standardize this SSE subscription, and I think this is on the agenda later to the talk about that, then there would be no need for any custom PR fork and basically NCL client could be used to trigger block building and to drive the relays. 
* And last of all the types, we had a special types repository that had all the bellatrix types and there was a big push to move everything into the atest and types repositories also, thanks stream for support. these types are very well supported and then is less repositories and duplications to maintain. yeah, next up we are wrapping up all the PRs and merging the changes into the main branches. There is no big changes expected anymore and we are going to participate in the Sepolia  and Goly upgrades, running the new versions of all the software before and after and and during the merge and the upgrade. 
* Yeah, and, and special thanks to Paris CL people, James, Sarah, Alex, for, for supporting this. It turned out to be, quite involved actually more than we, initially estimated, but I think we are getting everything now wrapped up nicely. yeah, thanks all. I think that's the overall summary. Yeah. 

## beacon-apis release plan [27.31](https://youtu.be/io7ALEfxJsE?t=1651)
**Danny**
* Excellent. Thank you Chris. Very exciting to see this on the testnets. any questions for Chris? Okay, thank you again. so we had Beacon APIs up next. Paul from Teku had, a number of points. Paul, are you here? 

**Speaker 01**
* Yeah, Paul is not, here unfortunately being midnight in this location. 

**Danny**
* I understand, does anybody that's keeping an eye on Beacon APIs want to discuss some of these points? So there's, the SSE subscriptions, there's another PR open up about an endpoint for expected withdrawals at slot and there's general, generally the discussion about how to get the Capella spec release out. 
* I believe that  has kind of leaked a lot into this and d N's not as stable. So, some questions around that. 

**Ben**
* Yeah, so the substantive issue on the spec is I think he feels blocked in. So Paul has sort of, assumed responsibility for, curating the Beacon API repo. So, you know, with plenty of input from others, but, he wants to get a, a release out of, you know, a checkpoint, API for Capella. 
* But there is not yet a stable Capella release of the spec or final release of the spec. So he feels blocked on that and he is also concerned that stuff from Deni seems to be being pulled forward into the, the release. and that is also making it complicated to checkpoint a sort of, Capella Beacon API release. 
* I dunno the rights and wrongs of this, but if anybody's got insight that would be helpful. Paul is feeling, blocked on it, right? 

**Danny**
* I can definitely reach out to talk. I think generally when we have like a semi-mature version on the consensus specs, that certainly means the next fork and we simultaneously keep r&d forks in there. That doesn't mean that that means that anything that's trying to be at parody with 1.3 should respect Capella and not, doesn't have to respect r&d. 
* As for the service side events and other points here, I am not deep in them. but if we don't have much discussion point here, we'll have to take it to the issues. 

**Pawan**
* Regarding the service, SSE events, Michael has started working on a PR for Lighthouse. he also said that he'll be, making a PR to the Beacon API steps tomorrow for the SSE event, implementation that he has described in the issue linked issue basically. 

**Danny**
* Got it. Would you call, getting this SSE done a blocker on releasing a 1.3 of the Beacon APIs or can it be layered in after? I just wanna understand the dependency here. 

**Pawan**
* Not sure about that. 

**Danny**
* Okay. I'll circle back with Paul and try to keep, try to get a lot of this moving, and answer some of the unknown questions. any other discussion points on the Beacon APIs for the call today? Okay, thank you. Any other Capella discussion points for today? 

**Terence**
* Yeah, so I guess one thing to add is that, for Prism we're currently comparing block value in a way that if today use MEV boost and we'll compare the block value from your local blog and the view block and then choose the one that's the highest value. And I'm wondering if any other clients are doing that and whether, we can actually integrate this type of test case into hive. Cuz I think this is a great test. 

**Speaker 02**
 *Yeah is doing that now. And we also would like to add kind of a percentage where user could say, not only just favor, yeah local if it is better or you can actually have a, a multiplier says I want to have, I want to use the builder only if twice the value of the a local execute. But this is not yet implemented, but we do, implement the comparison now. 

**Terence**
* Yeah, that makes sense. I can imagine every client does it differently and that's okay, but yeah, sorry, I should have brought this up earlier. So I think this will be a very good, high test case, but then we can follow up offline, just to chip in. 

**Gajinder**
* Loadstar is also doing it, so you just have to enable a flag, minus minus builder dot selection and see it as max profit. So, that way basically it'll choose if the local execution client has more block value, then it'll choose that. Otherwise it'll choose the builder. so we can be tested, we can be put on high test for this. 

**Zahary**
* Nice, Right. We have an interesting implementation if, the engine API support this, we get the information from there, but if it doesn't, we actually leverage, the, our tier one code base to calculate the broke rewards ourself. 

**Danny**
* Nice. 

**Pawan**
* I think Lighthouse also supports this with the leader list now. 

**Danny**
* Okay, great. So it sounds like there's a bit of, in some, parameterizations are turning on and off, but I agree this would be a nice case, especially now that we have the, the mock builder stuff in there. 

**Mario**
* Yes, of course. so yeah, I actually found, those, those circumstances where I, when I was writing this test. So basically what what it does right now is just basically bumps up, page, the, the block award just to get the CL all to always, include  the build block. And so what I found is that basically, every single client is doing this. So yeah, I think we can definitely a add a test, to the builder api

**Danny**
Cool. Thank you. Okay, anything else on Capella? Okay, great. moving on to the Deneb. 


## Deneb [34.26](https://youtu.be/io7ALEfxJsE?t=2066)
**Danny**
* There was a new release, as I said, this had a couple, it had a, a test case for Capella, otherwise was stable. this release did include the freeing of the blobs. Thank you very much  for moving that forward as well as, the nethermind folks who analyzed and simulated that. it has some topography updates, which on the call on Tuesday it sounds like they have been integrated into C K Z G and I believe since then all of the, bindings have been released. I believe there's, some review on bindings. 
* So they, they might be in flux a bit over the next few weeks as they stabilize and get things ready for audit. but they should be usable now. couple of other minor updates like the excess data gas field to the end of the execution payload. Thank you proto for saving our trees. and otherwise should be pretty good. Any questions on that release or further comments on that release? Cool, thank you again Yassic and everyone else for that review. It was a bit of a monster. 
* It does look like there are a couple of like copy pastas and typos that will be integrated and fixed, but I don't think anything, breaking at this point. There has been one more network in PR 3242 that has did not make it in at Edelweiss. I think it was generally agreed by engineering teams that they'd prefer to have no message sent if there's no blob sidecar, rather than an empty blob sidecar in these various messages.  does mention that the crypto is totally fine in sending these messages and you can evaluate these without any issue. there were some notes that, you know, we're not gonna be putting these in the database so why send them on the, the network? we've gone back and forth on this a little bit. 
* My gut is that engineering teams generally want this in there. and I guess I'm, that's my default based off of some conversations and I'm probably gonna keep this moving forward unless, there's some strong against in this call. Okay. Any comment on this? I think, on Tuesday on the 4848 call, although it might be canceled, I'll kind of knock on doors of people that have potential opinions here and keep it moving. Any other comment here, Tim? Is the 4848 call canceled next week? 

**Tim**
* Yes, I was just typing a message. We'll canceled next week. We'll have, one, two weeks from now and obviously there's the execution layer call next week as well, which is there, so we can bring up anything urgent. 

**Danny**
* Great, thank you.  Okay, anything else on one more thing in there is,

**Terence**
* On Beacon API for blob signing. I know there's the, all the conversations or a happening in the issue itself or sorry, is a pull request. So yeah, if anyone has left many feedback comments, please yeah, add to those. Ideally I, we would like to get this merged like hopefully by early next week so that we can unblock client implementation. 

**Danny**
* Thank you Terrence. Yeah, I took a look at that yesterday. It does seem it's still active. although I can knock on Shan's door if Sean's not here. ask what needs to be done to get this over the edge. Cool, thank you Terrence. Any other Deneb comments? Discussion points? 
* Great. Any other items to discuss today? Research spec or just open discussions or comments in general? Okay. Easy. Everyone gets an hour back. thank you everyone, for keeping Capella and moving. Very exciting. Talk. Chill soon. Bye. Thank you. Thanks. 

____

### Attendees
* Danny
* Tim
* Trent
* Pooja
* Barnabas
* Terence
* Pari
* Ethdreamer
* Mikhail Kalini
* Mike Kim
* Zahary
* Pawan
* Chris Hager
* Gajinder
* Andrew
* Mario
* Shana
* Carlbeek
* Roberto
* Stokes
* Sammy
* Protolambda
* Saulius
* Marek
* James
* Dankrad
* Kevaundray
* Radek
* Fabio


