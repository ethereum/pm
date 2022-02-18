# Consensus Layer Call #80 Notes
### Meeting Date/Time: Thursday 2022/1/27 at 14:00 GMT
### Meeting Duration: 1.5 hour
### [Github Agenda](https://github.com/ethereum/pm/issues/458)
### [Audio/Video of the Recording](https://youtu.be/Bi2qZ2epaPM)
### Moderator: Danny
### Notes: Alen (Santhosh)

## Decisions Made / Action items
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
|80.1 | The difficulty is hard to estimate,  to expect it to start going, to be noticeable on the network, around June, and to be completely unusable around mid-July 32 block. - Tim.| [36.50](https://youtu.be/Py1_Bw0frO0?t=292)|
|80.2 | The announcement for the difficult to bomb pushback will be communicated in the first week of May for a fork a month later.| [42.10](https://youtu.be/Bi2qZ2epaPM?t=2641)|
|80.3 | The timeline for the bomb release is to think about just being aware that it's there and that there are a lot of intermediate steps, and if we see that we're not actually tracking to something where it's realistic that they hit it, then we can kind of make that call and have that conversation earlier. And I believe that does a better job of setting expectations than waiting until the last minute.| [50.10](https://youtu.be/Bi2qZ2epaPM?t=3087)|

## Intro
**Danny**
* Okay, stream should be transferred over. If you're in the chat on YouTube, let us know agenda in the chat. First, half of the call, we will talk about Kinsugi merge things.Second half the call general consensus layer things.If anything comes up,  there is a pending release with the last little bits being worked on, so we can talk about that, then there's been a number of, cool testing things, DevOps things we can talk about, and then leave some time to talk about our, next steps. The release that is coming is based off of the discussions two weeks ago in the discord about some of the semantic issues with how the engine API works and how execution layer clients generally work. And has been talked about on the last two calls, so shouldn't be surprises here, but it is coming. It is a breaking change and we'll, need to engineer it, I believe on the Marius knocked it out in a couple of hours. So at least on the execution layer side, it is not a deep change. 
It might be a little bit,  more to deal with on the consensus layer side. I'm not 100% sure generally happy to open up discussion on these two or on these items. It's really this, PR 165 which is listed by, Tim here. The authentication PR 162 is also coming. It's kind, of in the final little discussion points, ironing out points, I believe. and then the optimistic sync spec, which a lot of you guys have been working with, has, been merged. There's a tiny little semantic change to get in to match the adjustments in the engine API, but that if you've been following it, has, been shaped up really for the past few weeks, but finally will be released. 
* Anything on these items again?  we've discussed them a couple of times.  I'm sure there might be some feedback once you'll start doing some engineering. 

**Paul Hauner**
* I wanted to mention something about optimistic sync. 

**Danny**
* Yeah. 

**Paul Hauner**
* So,  there's one that the API needs a little bit of thinking about. I shared a link on the merge channel earlier,  this week, about it. The problem broadly is that we need to figure out what we want to do with optimistic blocks, whether we want to serve them over the Http API or not. Broadly, there's kind of two ways and we could probably settle in between somewhere. One way is to never send them out over the API, which means the API only returns information about fully verified things and  the other one is to continue to return information about optimistic.The reason we would want to continue to return optimistic information on the API is so that validator clients can continue to follow an optimistic chain. They can keep up, they can know their duties, but not sign messages about the chain, but just know their duties and keep subscribing to subnets and things like that. So that's kind of the reason why that it would be useful to serve optimistic information over the API. Hopefully someone I don't have to chat here on my phone, but hopefully someone can link to that docnt I shared in the merge discord channel earlier. So, just need some thought about that. 
* Yeah, if you get a chance, just make me bring it up here or raise, it in that merged discord channel. 

**Mikhail Kalinin**
* Yeah. I have a question with what Paul, have just mentioned. Do we need to serve optimistic blocks to validate our clients? To allow for validate our client to get assignments?  duty assistant. 

**Paul Hauner**
* Yeah, I guess you might argue that it needs to serve out head blocks and,  the events API endpointside. Events endpoint,  are not necessarily blocks, but just more information about the head, about the shuffling of optimistic blocks, things like that. 

**Mikhail Kalinin**
* Because I was thinking a little bit about this change,  and,  from my perspective, like this assignment, look ahead., is one of the main things why we want to do this. And if, what we like,  we will just share a minimal optimistic information that is required to satisfy this look, ahead, then it should be fine. But, do we need to account for anything else? Do we need to consider anything, any other reasons for sharing this optimistic information? 
* Yeah.Also it's probably valuable,  for debugging purposes. It's also. 

**Paul Hauner**
* Yeah, I'd be really keen to hear anyone that's using the APIs and will say, if you serve any optimistic information, then you're going to break our thing or kind of looking for broad feedback there. 

**Mikhail Kalinin**
* Yeah.Because previously our general line of thoughts with respect to the API was as follows. So we're, sinking and all optimistic blocks. We assume, that they are not yet fully processed, so which is not for them.And, I think it's reasonable and we don't want to change, the direction, but also allowing, for making look ahead, it, would be reasonable to share the information that required for this look ahead. That's for me. Yeah. This is all that I just wanted to share. 

**Paul Hauner**
* Yeah.Thanks. That link I was talking,  about before has a link to a Lighthouse issue number 2946. That's where I've kind of started to sketch out. I've enrated all of the API endpoints and enlisted how they could change so that we only shared the minimal amount of optimistic info in order to keep the value of the clients work. It has a couple of little open questions, but that's an issue when you want to compare all these things. 

**Danny**
* Right?Yeah.I mean, I see the simplicity of just adding a flag, but also, I think we want to make sure one of the big things is probably that end users don't make bad decisions by being served such data. Bad decisions as in assng things are canonical or getting mixed up the wires there., I could imagine if we do serve it, there's probably some work to be done on consumer.So like, if you, are a block Explorer, you certainly have to decide,  what are you actually serving here? Whereas, if we don't serve the data from the API, it is much clearer you just continue to follow the blocks as they become canonical and fully verified. 
* It is weird to not have the data available at all. It's kind of funny to have this relatively critical process going on and not to have some insight. So certainly in the debugging purposes, I see the argument. I did share a link. Paul, would love some more feedback and put there. Anything else on this, one today it looked like,  Perry had some testing updates and so Perry, you can get us started, I guess, give us an update on Shadow forking and then we can talk about, we'll talk about Testnet stuff in next steps, let us know how Shadowforking is going, and then if anybody else has testing updates, we can talk about them. 

**Pari**
* Sounds good. So,  just to give everyone a brief update, sometime last week Marius Raphael and I were able to, Shadow for Girly. That means we've essentially merged Girly while not touching the canonical chain. So it's just a fork that we're running ourselves because it's a fork.  we still receive all the transactions and inherit the state from Girly. As long as the state doesn't deviate too much, we just continue getting all the transactions.We'd as that,  this is great for sync testing, especially under load, and if we want to do nonfinality tests with actual States, then this is the place we'd like to do it. That being said, it's still a real open question as to what all we want to test. So I just created a small docnt, to try and write down everything. If, people have ideas, please comment or make changes and we'll figure out how to get the test in action. I,  think that's about it for Shadow for me.And also we need to decide how often we want to do that because we now have an easy way to go through the Merch transition with State really easily. 

**Danny**
* Yeah, that was going to be my question as well. So it's relatively easy to push a button or even schedule at this point. 

**Pari**
* Yes. And also Girly has a really nice feature that difficulty just, increases to every block, so it's very easy to time out.

**Danny**
* Right?Cool. Yeah, it seems like we certainly should be doing this weekly for the foreseeable future with updated builds just to as kind of a continuous live integration environment. There's also work to do similar things around the transition, within hive so that,  could serve some Sandy check building as well. But I think it's pretty valuable. Have we considered doing,  it to mainnet? 

**Pari**
* Not yet, but we wanted to first maybe standardize or automate some of the tests and then apply on main. 
* Net.The main reason we,  don't want to do it on mainnet right now is it's a lot more difficult to figure out when the transition will happen and also to sync up and it will take like a day.

**Tim Beiko**
* Why is it difficult? Is it just because the rate of the difficulty increase? 

**Pari**
* Yeah, because it would depend on the hash rate at a certain time. It's very easy to estimate it. 

**Tim Beiko**
* I think once we have Cordi more automated, it makes sense to actually get practice runs of estimating, total terminal, total difficulties on mainnet and seeing when they actually hit.Because once we have to actually do it for real, it would be nice to, have tried to estimate the data a couple of times and see how close we got to our predictions of when it would hit.So I don't think it's the most urgent thing, but I think it's worth kind of going through that inconvenience a few times before,  we actually fork payment.

**Pari**
* Makes sense. 

**Mikhail Kalinin**
* Yeah. Also, the question with respect, to the main net shadow fork is with the deposit contract. Will we have,  to emulate it or what are we supposed to do with the deposit contract on the main app? 

**Danny**
* So you don't actually have to make any deposits because you can just start with a Genesis state with validators.You can,  use like an ERC 20 variant of the deposit contract to gate deposits if you want to actually test that functionality, which is probably not the most important thing that we're testing. 

**Mikhail Kalinin**
* Oh, yeah. So we don't want to start another big chain to launch it, like from the main net. We just want to launch it like a side chain with,  like independence from the mainnet and then. 

**Pari**
* Yeah, just to give you an idea of how that works, currently I just changed the fork version so all the deposits on the main contract would just be deemed as Invalid on my chain, and all of the deposits with my fault will be deemed Invalid on the other chain.Of course, we wouldn't do this on main because then you're wasting a lot of gas.But for girly, it doesn't really matter. 

**Danny**
* Are you actually making the deposits on Gorley? 

**Pari**
* I've just made one so far. If I'm not on. 

**Danny**
* Okay, but when you're just pre populating the Genesis with validators. 

**Pari**
* Yeah, mainly. Exactly. 

**Mikhail Kalinin**
* We can make some deposits after the transition, on the shadow main. Net, but if it makes any sense. 

**Danny**
* Yeah. Well, again, there's an,  ERC 20 mod of the deposit contract that if we want to do that type of thing on mainnet. It will still cost us gas, but it won't cost us 32 ETS.Other testing related items that we'd like to discuss today. 

**Pari**
* Yes,I wanted to talk a bit about if it's beneficial to have a non finalizing testnet for now. It seemed, like we were able to trigger quite a few bugs on Kinsugi and it might make sense, especially with sync testing, if we have a non finalizing testnet. Also, for tooling, I think it's relatively unclear to a lot of people as to when to show updates, what is, deemed as optimistic how to deal with stuff. So, I'm just not sure if it's too early for a testnet like that. 

**Danny**
* I would say,  given the breaking changes that people are going to have to work on over the next week or so that,  I would target these more exceptional cases to be after we get that done just so that we don't have,especially if we want to get other people using them. Things are going,  to change and so builds are going to change and I'd rather have them, target more production builds.  yeah, it's probably worth even on like something of a continuous basis, like building a chain with exceptional scenarios and watching it run. 

**Pari**
* Sounds good. Besides,  that I guess the other test question is,  can sue be successful? Do we want to do this after each Denver during each Denver, what's, the, plan? 

**Danny**
* We're at the  as soon as possible part of the phase where we need to get this release out,immediately.And we need,  to get engineering done changes to, the semantics as soon as possible, and then start probably a couple of Sandy check builds before doing standing up a testnet. Not that we want to stand up for a long time. My estimation,  is that certainly we're not going to be doing that next week, but if we are in a good place to thinking about doing it in two weeks,that would be great.And if it's three weeks, we don't want to go more than three weeks probably if possible,but there's certainly kind of an unknown stretch in the middle between getting these updates done in clients.As soon as any clients are ready, I think we want to do some Sandy check builds and start just like standing,  up a testnet that we drop real quick or don't promise to keep running for a long time.. 

**Pari**
* That sounds good to me. And,  the last question I had was regarding permanent.Has everyone already exited the validators? Is anything happening there. 

**Terence**
* For the prison, site. We're still running notes there just for testing purpose. We, want to see how performance our notice, so we're still using it, but I'm not aware of any other teams are using it. 

**Danny**
* Yeah, it's officially whatever that may mean. Deprecated as in the client teams here are not promising that it has any stability and that it's good for end users, but some people may still be messing with it. 

**Paul Hauner**
* Sigma Primer in the middle of exiting our validators by in the middle, I mean probably maybe 10% through. We've submitted all the exit. I'm just waiting for the queue.So once they're all gone, then we're shutting off our service. 

**Mamy**
* Members is using permanent for the insecure, test where we created fork, malicious one of, the chain. And we are testing if people are using, checkpoint sync on, that what's happening. 

**Pari**
* Sounds good. Thank you. 

**Danny**
* Anything related to testing people want to talk about? I know there's various, simulation efforts in progress. I know there are continued hive efforts in progress and all of it will have to integrate updated builds in the next week or so.

**Marius**
* I started,  writing some test, vectors for the new changes.I don't know if you already talked about the new spec changes. I joined a bit late, but I have some test vectors, so it should be easy for everyone to use that.I'm also going to build a version of Gas that can sync with a new spec currently with a new spec cannot sync,but can just execute the blocks. 

**Danny**
* Great. 

**Tim Beiko**
* One more thing. Just for people to be aware, we talked on Al Cordez last week about basically what do we want to do about testnets after the merge? Because we have a bunch of execution layer tests today and which ones we want to transition over.I think roughly the consensus was that we want to keep one testnet with somewhat open validator, set, one testnet with somewhat closed, validator set.And we probably want to also,transition Robson, but eventually kind of, sunset it.So on the execution side, we'd probably transition Gordy, not transition ring can be transition Robson's with the intention of deprecating over time and then transition Sepolia, which is the new test net with the intention of, it being a replacement for time.So, no need to decide anything right now, but I think it's worth it to align obviously with the consensus teams on that to make sure that every test net that we're targeting to keep has a long term consensus fair test, that's associated with it. 

**Danny**
* So a few things. The prouder evolution of Goreli.I think we're in reasonable shape and that could be a very stable testnet.The other type of test net you said,like no gating, like no very stable backbone, from us and others. 

**Tim Beiko**
* Yes. I'm not actually sure how freighter works. Most of the validators are just run by like known entities, but anyone can join. 

**Danny**
* Is that right? Something like 80% is us, so it generally is stable unless there's some sort of bug or something. 

**Tim Beiko**
* I'm not expert here.If there is value in a test net, which has like a Flakier validator.That should probably do that, but I can also see if that's just, like, way too unstable and provides absolutely no value. 

**Micah Zoltu**
* Michael, so the goal with having one of the test sets be validated by real people is that it allows DAPs who want to Harden their applications against finality failures and things like that and give them a place to do that. That is a long term test time.They don't have to spin up their own and try to simulate their own finality failures. Because if we have regular people validating on test tens in particular, as we know,they will just disappear randomly, and then they'll have to leak out. And then eventually we'll get finality again, and then new people will join, they'll leak out, we'll get finality again. And so it comes and goes. And so it's a great place to pardon your apps against. 

**Danny**
* Yeah, I understood. I think we need to think about what, like, if we do that, how many validators are run by a more professional group, if any?, and I,  guess what the requirements of various teams, or maybe the DevOps team would be here.

**Micah Zoltu**
* Am I correct? My understanding that if we have an unreliable set of validators,  we'll still get blocks, we'll block production, just there'll be some missing ones here and there, and we just won't get finality until people leak out.And then eventually. But we will always eventually get finality, right? 

**Danny**
* Yes. So, all that premise is true. So I guess,  how do you kick it off?Because if you have any amount of professional or client team run validators quickly over the course of a few leaks and people coming and going,they'll just become a very dominant portion of the set.And probably then you have a stable testnet until somebody ds a ton of validators on. 

**Micah Zoltu**
* So you're saying we built things too?  well, and we will always trend towards stability, no matter how hard we try. 

**Danny**
* Unless we just don't go on it at all. 

**Micah Zoltu**
* Even though we still might end up with stability because we just might stand up with some dude on the Internet who just decides, I want to own this right. 

**Adrian Sutton**
* Eventually, it seems like it might be better off to just have us run a bunch of alligators on the unstable test net, but deliberately turn them off regularly, and we can deliberately cause non Fidelity, and we can deliberately cause chaos in that testNet for anything else. It's actually really hard to know what people are going to do, and if it's just valid, it's going off fine. You tend to get non finality, but not chaos.And so it doesn't test anything because you get a very stable chain. There's still a single chain, and life just goes on. Whereas the problems are when you get bug, which is the only time you'll really get nonfinality on mainnet, most likely. And once you get that, start to get an explosion of Forks like we saw in Kintsugi. And that's when you start to get trouble. 

**Danny**
* Yeah, I guess so. There's a few things there every other week.Turning off half of the validators is potentially valuable to those that want to test in a finalized environment.But,  if the issue often is when you have an explosion of Forks, we could also think about how to,  induce such an explosion of Forks rather than hoping for a bug that gives us an explosion of Forks. 

**Adrian Sutton**
* Yeah. Just kind of a chaos monkey in there. And nodes that deliberately every other week make new Forks from 100 blocks back. 

**Danny**
* Yeah. Every other week, turn off 40% of validators, make 10% validators chaos monkeys, and have the 50% run normally. ,and then the next week turn everyone back on normally. 

**Adrian Sutton**
* Yeah, I think that's the way you're going to get an actual chaos testnet.I think if you just leave it to the public, then there's a very good chance you just get a dead test that everyone wanders off because it's not interesting anymore. Or you do get enough people running it stable and it kind of does centralize on them and stabilizes. 

**Danny**
* Yeah, I think I agree. 

**Arnetheduck**
* The alternative here is actually to launch little insecure us every now and then.It's kind of a fun process to,  get that launched because it like it uncovered a few unexpected effects of turning, off, say, half the validators.Now I was running it with you can, for example, not run with the validators.That doesn't work.You can easily,  like if we have the validators known to group of people that can easily generate.Like.Spin offs that basically bleed out everybody else. So that's one way of doing it. And, doing so also stresses Forks because you can then generate Forks at will and so on. 

**Danny**
* Right. But insecure is going to test, like, only a subset of what we might want to test.Right. Because if there is a continued public test net, then those that are synced are going to continue to follow said public test net.. 

**Arnetheduck**
* Yeah, for sure. But that could become a weekly process, like a new chaos.Then you have like, a stable testnet, say whatever it is.And then you,.Generate like, a chaos test every week, which is broken in control from the product. 

**Danny**
* Right. We certainly want to have a stable testnet. Not that we point people to for testing standard things. And then I think we want to,  maybe get a little bit more clever about if we're going to create an unstable environment, how to do so in a stable way. 

**Tim Beiko**
* Yeah, that makes sense.And I think also in practice, in the short run, it's going to be two stable test set. So, for example, if we fork both Robson and Sepolia. We're, going to need to be concerned for those with the expectation that we shut one of them down in,  however many months after the merch. So short term we'd need three with the gold, two drop to two after a couple of months. 

**Danny**
* Yeah.And so we essentially have the ability to make,  a proof of authority. Testnet that by using the ERC 20 variant of the deposit contract where you  just can gate it and you give these tokens to whoever we want to run validators. So you have the Pratter, which  you know, we keep very stable and people can join and we make sure is  open. And then if we want, something that's more like Gorely, we can use this other gating mechanism as Well, it's just a tool in our pocket. 

**Tim Beiko**
* Sounds good. I noted a couple of these ideas we discussed in the issue on GitHub, so we can the conversation there. 

**Danny**
* For the result. Sorry for the release that's coming. There's one thing that I wanted to mention.I think that we need to get the slight semantic changes into the Optimistic sync spec.Does anybody want to take that in the next, 24 hours, take it as and do it. 

**Paul Hauner**
* Update the Optimistic Sync API for the new execution API. 

**Danny**
* Yeah,. 

**Paul Hauner**
* I can get on that. Thank you. 

**Danny**
* Great. So I think another  thing we want to talk about is next steps. We talked about a little bit involving clearly Kintsugi as it, stands today will be deprecated due to the breaking changes in the engine API. And the intention is to stand up another long standing version of that. Maybe  Kinsugi v.Two on the order of two,  three weeks.The,  difficulty bomb is looming and there's  plenty of things to do between now and then. Tim, do you have any discussion points based off of some of the planning you've been thinking about? 

**Tim Beiko**
* Sure.Difficulty is,  hard to estimate, but roughly we can expect it to start going, start being noticeable on the network, around June, and for the network to be completely unusable around mid July. 

**Danny**
* Not completely defined, completely unusable. 

**Tim Beiko**
* 32Nd box. And that means that we. 

**Danny**
* Because it literally becomes completely unusable. 

**Tim Beiko**
* Probably  two weeks later. Yeah, exactly.So it's like you go from 30 seconds to probably 1 minute block within two weeks., there is like an economic cost of like, once the network is at half the capacity, it's like half the economic activity can't happen. Fees double or probably more than double. So it's a pretty terrible spot to be in a 32nd box. So I think that means if we're not going to,  push back the difficulty bomb again, we probably want to aim for the transition to happen on mainnet in June, ideally like the first half of June at the latest back of the envelope looking from that, what do we need to do to actually get there? I think roughly we would want to be in a spot where we're announcing client releases for public testnets, like existing public test nets around mid March, which then gives us a couple of months for people to upgrade their nodes for those to fork for us, to make sure that there's no issues and then to pick a TTD on mainnet and then put out a release with main net.  roughly I think if we're in a spot for early March, so call it like a month from now because January is basically over, client code is basically done. That would be like ideal to hit this target. There's probably some wiggle room we can have from there, but there's not like months of wiggle room.So I think  like we were talking about in the chat earlier, if we able to have Kintsugi v2. Two by Denver, which is like mid February, I think we're in a good spot. Obviously this all asss the latest changes to the spec are kind of the biggest changes we still have to implement. We'll probably find some small bugs here and there, but it seems we don't find like a fundamental issue, or something that requires significant rearchitecting of how things are basically getting to give you two with mostly final specs, in the next couple of weeks after that, a couple of weeks after that, getting the final changes done and then starting to look at going on existing  test sets, we would be in a really good spot. 

**Danny**
* Feedback, reactions. Any discussion points on that? 

**Mikhail Kalinin**
* I have a comment on that. This is pretty tight schedule and, it's not about clients are not ready, in April or this kind of thing. But what worries me here, if we take this schedule, if, there is something appears not probably a fundamental issue, but some issue that we will need to test with more care on the test.Net, have like two more weeks of testimony, it might be the case,  that we will have to delay the merge for of course a reasonable thing.And,if we have this tight schedule, we, are risking to be between two fires.So we have to release and we don't have the time to properly do all the steps with respect to some unexpected stuff. So that's what worries me with this. 

**Tim Beiko**
* Yeah, I think if we aim for this, we have the wiggle room definitely for one issue like that happening, call it like a minor issue where we need to do a fixing clients, but let me release test out for a couple of weeks, maybe, two.But if that happens three times, I think we basically have to push the bomb again. So that's roughly that we don't have one logistical question on this. 

**Vub**
* What time between the merge fork and the terminal block. Are people expecting to happen?

**Tim Beiko**
* My thoughts on that was when we actually fork the testnets, we should probably leave a reasonable amount of time.Call it like, say, four weeks from the EF blog post.But then when we for mainnet, the reason for that is it is kind of a significant upgrade. Right.Like, everybody's running one client now they run two.So, like, give a couple of weeks for people to do that. Ideally, they've already done it on Kinsugi, but don't want to break out that. But then when we actually do main net, I would make the delay much shorter because of the difficulty of predicting the actual makeup difficulty and the fact that, you would think hash rate would, drop near the merge because people are going to try to sell their GPUs already. Right. So I think we can. 
* When we put out the test net release, we can say, hey, there's four weeks before the test nets. And by the way, when the maintenance,  release is going to come out, it's going to be on a much shorter cycle. So keep an eye on this. 

**Vub**
* I think that's reasonable.I guess the other thing we could consider is if there turned out to be lots of problems, then the merge fork itself is like an opportunity to shut down the difficulty bomb. And that would buy us a couple of weeks time. 

**Tim Beiko**
* Yeah, that's a good idea. And it's like, during the same release, we could, push back the difficulty for like a month or something. Yeah. 

**Danny**
* Part of Italy's question was also,  the time between the beacon chain fork and the difficulty bomb. So if you're calling it maybe client releases, then plus ten days to that initial fork. So that's really ten days to get things configured and then plus a week to the difficulty bomb.I mean, sorry to the transition difficulty. So something on the order of slightly more than two weeks, I'd say full process.That's aggressive. But if we set the expectation,  maybe not. 

**Tim Beiko**
* Yeah, we definitely need to set the, expectation once we have the testnet releases out and even maybe before, like, once we announced it. 

**Danny**
* Yeah.If we're in difficulty bomb zone,  and the difficulty is also changing because mining makeup is changing.It's trying to estimate beyond two weeks, it might become very difficult. 

**Tim Beiko**, 
* Right.Okay. So, if we decide to just push back difficult to bomb, what is the procedure? How much time do we need in advance to, like, to announce this and set expectations maybe. 

**Danny**
* First week of May for a fork that's a month later. 

**Tim Beiko**
* Yeah, I think that as we basically do what Vitalik just said. I think there's two worlds. Right. One is where,  we just need an extra couple of weeks and we do this, like, combined difficulty bomb pushback and merge fork. 

**Danny**
* There's a world where we need the extra two weeks doesn't actually buy you the extra two weeks because you just gave people client releases. 

**Tim Beiko**
* Right.So you could do you're saying? 

**Vub**
* I think the idea is that it's okay that if we end up giving people, we can wait all the way up until the block time goes to like 23 seconds or whatever to give people client releases. 

**Danny**
* Because that means when it reaches 30 seconds. 

**Tim Beiko**
* Right. Exactly.Because you can simultaneously diffuse and set the difficulty the thing two weeks from there. 

**Danny**
* Okay. I think that's the strategy, but we have to be like, I guess pretty confident. 

**Vub**
* Yeah, right. This is definitely all already in a kind of contingency planning territory. 

**Tim Beiko**
* Yeah.But that's like we need an extra two week territory. I think if it's like we need an extra two months territory, then basically you have a separate hard fork which just pushes back the difficulty bomb, which we can implement pretty quickly. It happened once in a matter of weeks when we literally forgot about the difficulty bomb. So it's not, like, hard technically to do. I think the right time to have this conversation is if we do get to March and we feel like we're not close to being confident to have a fork for public test nets, then it's worth having, the conversation around. Like, why aren't we confident? And do we think that this is a week's things or a month things and we can kind of decide from there? Sorry.Go on, Danny.Please. 

**Adrian Sutton**
* It's making me really, nervous that we've got essentially an arbitrary date. Our scope is fixed., like any product manager walks into an engineering team and says, hey, guys, I'd like to develop a fixed amount of software and a fixed amount of time. What do you think?It's not a conversation that goes well for, them, and that's kind of what we're doing to ourselves now. 

**Danny**
* I mean, it certainly is because the reality situation. 

**Adrian Sutton**
* But, yeah, like, I get it. But to me. I'd almost want to start from the asstion that we'll push back the difficulty bomb because we want to get the most right. We want to make sure that we are actually confident in it rather than we've got this date and we're kind of going to on the side of shipping. I'd rather on the side of delaying and be confident. 

**Danny**
* I kind of take the counter to that and that we have to try to err on the side of shipping because, we will take as much time as a lot plus some amount of time, no matter what that time is selected as. 

**Adrian Sutton**
* Yeah, I can agree with that. But when I look at the state of things, I'm not sure we have an entirely complete, optimistic sync implementation at all. Right now to the point where you can have the CL running and, we're just starting syncing tests of things. We're still working a lot of details. There's still a lot changing.I know we've got kind of another month before we're talking about being done, but, man, it feels like a lot is up in the air and that there's an awful lot of engineering work before we can get into starting to test and starting to decide if we're confident that it really works.I might be wrong in that I can be quite pessimistic about these kinds of things.But.It,  really is worrying me that we're putting the difficulty bond too much over our heads. that's just my worry. 

**Danny**
* No, I certainly hear you. I'm kind of in the position of the one hand, we've worked, on this for a long time, and a lot,  of the unknowns are uncovered.  and a lot,  of the core is in place. But you're right, there's plenty of engineering to, do, and there is a lot of testing to do.And so my personal is to attempt to get it done, but to be very willing to make reasonable decisions along the way.If we drop two weeks here, two weeks there, another week there, then certainly the timeline is too aggressive, but I'm,  tossing it out entirely at this point, I think, will slow things down more substantially than if we attempt to hit it. 

**Adrian Sutton**
* I certainly don't mind having relatively aggressive timelines for Kintsugi v2 and saying we want to have optimistic, fully working in all clients and this should be a reliable test that users can do all kinds of crazy stuff on with rethinking Els behind our back and that kind of thing and have it all work. Certainly happy to keep pushing for that. That means we can hit a merge before the difficulty bomb goes off, then. Great.I think,  we just need to be really, careful in setting expectations when we're talking dates like this. Now that we're starting to have these conversations, people think the merge is slipping.If we have to push back the difficulty bomb and beating the difficulty bomb is not something that I'm prepared to commit to right now in terms of what I see in the way software is ready. 

**Danny**
* Yes, understood. I mean, to anyone listening, it's more important to do the merge right than to do the merge by a particular date. 

**Tim Beiko**
* Right.And I agree with that. And I just think we need to be mindful of like, the bomb is there and we need to think about, like, if we do choose to delay it, ideally we make that call kind of early and explain why. And I think that helps kind of set expectations better than if we're like mid May and people know the bomb is in June and then decide to delay it. Obviously, if we find a major issue mid May, we would delay it.I think just being aware that it's there and that there are a bunch of intermediate steps, and if we see we're not actually tracking to something where it's realistic that they hit it, then we can kind of make that call and have that conversation earlier. And I think that sets expectations better than leaving it to the last minute. 

**Adrian Sutton**
* Definitely very helpful to have this timeline. Thank you for pointing out we need to be ready by March to beat it. Basically, that's key information. 

**Danny**
* Indeed. I see the difficulty bomb and the stretch of things we have to do between now and then in that reality,  it allows us to create some milestones and checkpoints that, are on the more aggressive side, and I think,  that we should at least utilize those as milestones and checkpoints to kind of check in along the, way for the next few months.

**Adrian Sutton**
* Yeah, let's be really strict on those milestones in terms of saying whether we're done or not, because I don't know, in the original plan for Kintsugi, we wanted optimistic sync done and we launched without it, which I think was great, but I think we need to acknowledge we didn't hit that milestone either.So when we set these, let's be really clear about what's in them and whether we've actually achieved it and to what level of confidence. 

**Danny**
* Tim, on some of the things we've sketched out in terms,  of hitting those test nets and stuff, maybe you and I can spend some time actually attaching some of the technical things along with what we want to see with them,along with some of the testing that we want to see as well so that we can hold ourselves to that. 

**Tim Beiko**
* Yeah, that's reasonable. 

**Danny**
* Yeah. To physics comment frustration stemming from poor communication., I agree. I think it's quite a difficult process to communicate about because there are so many different moving pieces and teams and there's not a, dictator on high saying, this is the timeline, this is the ship date, and it's kind of more of an amalgamation of,  many moving pieces.  I apologize for the poor communication.I think we can certainly do better, but it's also a product of the process itself.Okay, anything else on next steps? Timelines, difficulty bomb?Anything else related to Kintsugi, the merge or,  cross El CL? Anything? 

**Saulius Grigaitis**
* Basically, the question is, does everyone agree that the polling, approaches for API is good? Because for some calls and for some situations it seems that it would be great at least to have an option to have a blocking call and to get the response immediately if it's available. So is there any ideas, on that because the engine API looks more like most of the call seems they do not return, that sometimes it's very usable and sometimes it's actually possible to return that result.. 

**Danny**
* I'm not sure exactly. I understood the question. which endpoint in particular are we talking about with respect to polling. 

**Saulius Grigaitis**
* So basically, if I add payload it is quick to actually validate it.  then I would like to get the response immediately that it's valid. Basically, I'm okay to wait like 200 milliseconds or whatever it takes to validate it. 

**Danny**
* That is generally the case if execution layer has the data available, especially if it's adding onto what the execution layer sees, it's canonical chain, it will immediately return. 

**Saulius Grigaitis**
* Okay, so maybe I misunderstood. So basically,  my understanding was that it's not clear whether the call takes a lot of time or not.Then basically the general idea is that the response is non blocking and let's say returns syncing or whatever.Maybe I just misunderstand the specification. You are saying that if I insert the payload and the payload is something that the execution engine cannot, immediately calculate it. Basically, do the transition and say is it valid or not? Then it immediately returns that. Is it correct?Is it valuable? 

**Mikhail Kalinin**
* Let me give a comment on that. There are two general cases. There is the payload from the economical chain. If you submit a payload from the canonical chain and El doesn't have a parent state or doesn't have a parent block, whatever, it must return syncing.If it does have the parent state, it must execute it, and respond with valid or Invalid. If this payload is not from the canonical chain.There are options that are and these options depends, on the client implementation. For instance, some clients maintain several States so they, can execute this payload immediately and respond with valid if they have a state. Other clients does maintain only one state which is the canonical one of the most recent block and they will just respond with accept it. 
* And once this payload or its descendant is signified by the folks choice update as the head of the canonical chain, then the client must run the execution and the current spec says that it's up to a client implementation to decide whether this call will be synchronous and the client will spend some time to execute a few blocks., if it has these blocks and respond with valid or Invalid status, or the client decides to go to the network to pull more information or it's like 100 block worth of execution. And in this case client responds with syncing and goes executing these payloads and verifying this payload in a Chronos fashion. So these are the change that are coming with this new release. 

**Saulius Grigaitis**
* Okay, basically, if correctly implemented that execution layer, then if execution layer client can do this quickly, then it actually does that correct? 

**Danny**
* Right, and quickly it's up to client implementation because it's very difficult to specify it correctly. So this kind of quality of service stuff in particular, if Argon is really fast in execution and there is a rework, which has three, blocks to execute, and their gunmate does it in like sub 100 milliseconds. Why not to do it, to execute them all and respond with valid. So that's why there is a room in this back left floor, this kind of,. 

**Saulius Grigaitis**
* Okay,  if I get a response that it's syncing or whatever, basically not calculating it immediately, is there like some guide?How often should we pull for the result? 

**Danny**
* The idea is that you pull the idea.I suppose you could, you could just sit there and wait. But actually execution layer syncing processes often,  rely on continued information about the head. And so the idea is that you would then insert a descendant,  and you might see syncing, syncing, syncing until you insert one descendant where the syncing process is complete and you might see valid or Invalid, and that can validate or invalidate that branch that you were unsure of in the meantime. This is, the kind of the interplay between the engine API and the optimistic sync spec.  the optimistic sync spec is in the consensus layer specs if you, want to check it out.So it's not intended that you pull on the same call if you get syncing. 

**Mikhail Kalinin**
* Yeah, actually you may fall by using the pictures updated so you will get the status faster than the next payload received from the network. But yeah, it also depends on the implementation. But this implementation is client implementation, so you want to fine tune this stuff.So you might probably want to, call. 

**Saulius Grigaitis**, 
* Yeah, but let's say I just get so this is the station where I get and then, I insert the payload of that block and, then let's say execution layer says, okay, there is no immediate response and processing or doing whatever. And then I need to test, on a safe head and I need to ask again execution layer in order to check, is the new payload valid or not? Or should I wait again for a while and ask again? 

**Mikhail Kalinin**
* The default behavior will be not asking again, but just waiting for the next block, submit it and get either still syncing if it's syncing or, get valid if the sync is done. 

**Saulius Grigaitis**
* Yeah, but then I missed the possibility to vote, on, a new sale header. 

**Mikhail Kalinin**
* Yes. If you as that this stuff will help to recover, to, get this information that this thing has finished faster.It's difficult to say right now because we haven't seen any helpline implementing this new logic. 

**Danny**
* To be clear, the standard path is essentially you're just kind of inserting and lockstep. Like once El is synced and the consensus layer synced you add to the head and it says valid or Invalid very quickly.The notion of El having to go into some sort of sync mode is at the very least in the normal case on some sort of reorg, or potentially like a total reconfiguration of the underlying El software or some of these more exceptional scenarios. Not in the case where you are kind of inserting just into the head, but there are these potential reorg scenarios where  if you more aggressively want to get the answer and the information polling could be maybe a reasonable strategy on the sub slot interval to try to get updated information.  if I were working on this API, that would be a potential optimization to consider after I got the core in place. I don't think it's critical for the initial because again in some very exceptional  scenarios you might for a slot have kind of a blurry vision as to what is valid and maybe not a test, but not in a way that would  greatly affect a validator in normal case in my estimation. 

**Saulius Grigaitis**
* Okay, so I'll  just maybe see how I would expect this to work.Let's from reading validator in the first 2nd, then what I, would do, I would open Spinna call, to the API, that waits until the end of the first 4 seconds and, I either get response, from the execution layer during that period, that the payload is validated so I can update the same on that. Either I time out, then I test on the, previous whatever it is, or another option is insert the payload and then, if I do not get a response immediately thinking, then I need to call, often because I want to, Bolt on a safe head as soon as, possible on the new safe, head as soon as possible. So then I have this not so nice every 100 milliseconds or whatever until the end of the first ticket.So, this looks like this from my perspective because at the current proposal there is no, very clear or this is not, optional for execution layer clients to behave slightly differently,then there is a bit, of uncertainty what is actually happening on the execution layer. So, that's why there, maybe it makes sense. 

**Danny**
* I mean there's certainly uncertainty because there's any  of reasons why the execution layer can't immediately respond to something. 

**Saulius Grigaitis**
* Yeah, but I understand that  they cannot responded quickly, but then I'm left with the station where I even don't know should I call it and, hope that they had the update until the deadline of, when I need a test or I just should go up because,this is at least from what I hear.This is slightly, unclear. 

**Danny**
* It is unclear as to how  quickly the execution layer might be able to fix itself,  in an issue because in the two extremes it might be doing a one block reorg or it might be doing a full sync from Genesis and that is not  the granularity of the difference between those two is not specified in the call.Again, polling doesn't do any damage.So if you're trying to highly optimize these scenarios for attestation inclusion, I mean, it's a viable strategy, but I don't think it's going to buy you much in almost most cases. Sure.  

**Saulius Grigaitis**
* If I can take some time. So if I understand correctly, even the latest changes,they do not address the attacks that keeps bouncing attack, which makes you have a two running, or at least, two running Forks in parallel.And it seems this problem is still not solved. Right. It's possible to kill the execution layer by just keep reorging it, which takes a lot of time Or is there a solution for that? 

**Danny**
* If a fork choice balance can be done in perpetuity at a deep depth, I think that it could short circuit some execution layer clients, depending on the depth and depending on the frequency. 

**Saulius Grigaitis**
* If I understand correctly, the depth is like,  for guests,. 

**Danny**
* And, a mining cartel could do the same thing to Gas today as well. 

**Marius**
* Okay, so, there's a small difference. Like, we have 128 reocc depth that we can do super easily. So this, like, we maintain 128 blocks in the state for the last 128 blocks in memory, and we do maintain the state for the last, roughly, 90,000 blocks on disk.So we have those try notes on the disk, but if we were to reorg, so we can handle reorc up to 90,000 blocks,  but that takes a longer time.These 128 blocks,. 

**Saulius Grigaitis**
* Are instantly reopened, but let's say 200, blocks on the main net. What is the reward time for that? 

**Marius**
* I'm not sure, but it's a couple of seconds, so it's not bad. 
 
**Saulius Grigaitis**
* Again, it's going to depend on the institution layer, but I claim that such an attack can be done by any consensus mechanism. If there is some sort of cartel or certain threshold met, you could do that with proof of work mining at 200 block depth, but you need to have sufficient,  crypto economic weight to conduct such an attack..Okay. 

**Danny**
* Any other merge related items? 2 minutes left. Okay, we don't need to do a deep round of client updates, but if anyone has some items they want to share, please take this time to do so.. 

**Paul Hauner**
* I don't have much to talk about in terms of client updates, what's going on, but not much to talk about. But I did have a question from Michael. He's interested about the status of proposal boost., he's particularly interested in who is running it on Prada. And if we're waiting on anyone to finish implementation, please. 

**Terence**, 
* Yeah, so Prism here. So we have finished the implementation.I believe it, Was merged as of last night. We just need to cut a release, so just let us know when you like to see it.Predator test net. 

**Danny**
* Yeah., I think it's probably good to move in that direction right Paul? 

**Paul Hauner**
* Yeah, I think all of our nodes are running it I'm not sure exactly but Michael's been running it on some nodes I think Techie has been running it as well. I think he is keen to see it, running on more nodes so that we can see the actual effect of it. So yeah, I think you would be keen to see prison running it on product whenever they're ready. 

**Terence**
* Got,  it yeah, we will prioritize that.

**Adrian Sutton**
* TECO has been running it on all our proper notes for a while now. 

**Lion dapplion**
* Soda has merch but not running the notes yet. 

**Danny**
* Great. Any client updates or any discussion points in general for today? Okay. We're putting the final touches attempting to put the final touches on this release. There is a couple of things standing in the authentication that needs to be merged and those optimistic sync slight return call., status updates that need to happen., but that will land very soon.Then we can, work on consr YouTube.Okay.Thank you.Talk to you all soon. Take care. 

**Mikhail Kalinin**
* Thanks everyone. 
* Thanks for watching. 



## Attendees
- Trenton Van Epps
- danny
- Enrico Del Fante
- Pooja Ranjan
- Paul Hauner
- lightclient
- Saulius Grigaitis
- Tim Beiko
- Marius Van Der Wijden
- Ben Edgington
- carlbeek
- terence(prysmaticlabs)
- Mikhail Kalinin
- Marek Moraczynski
- Cayman Nava
- Rafael (skylenet)
- protolambda
- Adrian Sutton
- James H
- Hsiao-Wei Wang
- stokes
- Lion dapplion
- Péter Szilágyi
- Dankrad Feist
- pari
- Jose 's iPhone
- Raul Jordan Prysmatic
- Leonardo Bautista
- zahary
- Nishant
- arnetheduck



