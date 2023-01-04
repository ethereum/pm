# Consensus Layer Call #81 Notes
### Meeting Date/Time: Thursday 2022/02/10 at 14:00 UTC
### Meeting Duration: 40 minutes
### [Agenda](https://github.com/ethereum/pm/issues/475#issue-1129437213)
### [Recording](https://youtu.be/DtwTZWZrZMY)
### Moderator: danny
### Notes: George Hervey

***Summaries and highlights were curated and slightly modified from [Quick Notes](https://hackmd.io/@benjaminion/S1YGF9Gk9) by Ben Edgington.***

## Kiln office hours

**Danny:** 
People of youTube, please let me know if you can hear us.

This is Consensus Layer Call 81. We have issue 475 in the PM repo shared there. The first portion will be at Kiln, aka the current Merge Sprint. and then we'll go into any other updates and research questions that we want to On my end, I do have Carl Shaway and Vitalik, so multiple people might come out of this audio.

**Vitalik Buterin:** 
Gm.

### Auth and exchange additions to kiln

***Summary***

- ***Kiln v1 is out. Two known issues to be put into Kiln v2:***
- ***[ethereum/execution-apis#167](https://github.com/ethereum/execution-apis/pull/167) - authentication for engine api (note, it’s now on a new port)***
- ***[ethereum/execution-apis#172](https://github.com/ethereum/execution-apis/pull/172) - add engine_exchangeTransitionConfigurationV1***

**Danny:**
Great. let's go ahead and get started. Kiln, I, think most of you, probably all of you, have seen the Kiln V1 thank you Mikhail for putting that together. there are two issues that we've been discussing over the past couple of weeks that were known to come into a Kiln V2.

You can think of these as kind of extensions and additive. You might get some warnings if you don't use the Exchange transition configuration. But that would probably be just at the beginning before the merge happened and you'd still be able to merge. And the authentication API written by Martin has been written in a way that authentication is on a new Port.

So if you're not ready to speak authentication, you can use the old Port, although we should move in that direction as soon as possible. So these V 2 extensions which will be added to a quote official V Two very soon, they won't interrupt, they just add a little bit of that you need to work on. Those issues are linked in the, those PR are linked in the issue. Are there any questions, comments or discussion on these points?

Cool. Yeah, nothing really unknown there. We've been talking about these for a month or more.

### Kiln milestones!

***Summary***

- ***New [tracker doc](https://notes.ethereum.org/@timbeiko/kiln-milestones). Similar process to previous devnets. Be sure to run optimistic sync across client combos.***
- ***Once sufficient milestones have been passed we’ll make a persistent version and release it to the public. It will be the last testnet before we fork the existing Eth1 testnets.***

**Danny:** 
Okay, next, up, we're going to talk about some kiln milestones. Tim has put this together. Tim, you want to take it over?

**Tim Beiko:** 
Yes, if I can find a new button. I just shared this on the agenda. I can share my screen as well. Make it here. So these are basically pretty similar to the stuff we've had for Kintsugi, and I'm still building on the same format. High level, just a tracker for execution and consensus error teams.

Milestone zero is implementing- starting implementation milestone one is implementing Kiln V And then we'll probably change this to Kiln V2 sometime in the next week. Maybe we can add a separate milestone for V2 actually.

Yeah, I think it's probably cleaner to just add the second milestone. then basically if you can try to interrupt, whatever clients on kind of an ad hoc basis. M 2. M 3. Like you said, we'll be starting some devnets builds.

I guess the one thing we want to make sure that we get right in these definite builds, Additionally to everything else is running, optimistic sync on CL clients. that was one of the things people commented on about the Kintsugi milestones where we were kind of done but hadn't actually gotten optimistic fully nailed down yet. So we want to make sure we get that. And then similarly, the last time after we've run a couple of devnets that things are working as expected, we'll set up kind of a persistent version of Kiln. I, still have configure here, so I need to fix that as well.

We'll set up a persistent version of Kiln and then, once it's up and it's stable, we'll release it to the public and basically advertise Kiln as the last kind of place, to test things before we actually run through the merge on existing test nets. If everything goes as expected. and then the last part is just like previously saying we'll focus the first half of the core devs and their calls on this, stuff.

**Danny:**
Sweet. Thanks, Tim. Any, questions?

Yeah, I think it goes without saying in parallel, to the kind of production engineering effort that is highlighted by this lots and lots of ongoing testing. So, we'll likely do regular Shadow forking to kind of more continuously test the builds. There's a lot of work coming out in hive, and some other simulation frameworks, and maybe, some new consensus vectors along the way.

### Testing updates

***Summary***

- ***[Lightclient] has merged a PR to mergemock to support Kiln***
- ***Pari mentioned [the Kurtosis tool](https://notes.ethereum.org/@ExXcnR0-SJGthjz1dwkA1A/H11OzhRAK) for running private test infrastructure. Can be used to test locally before joining any devnets.***

**Danny:**
Actually, I just kind of mentioned testing. Let's do that right now. Does anybody, have any testing updates or anything to share in that domain?

**Lightclient:**
I just merged the PR to merge box and it adds support for Kiln, so if anybody is interested in using that should be available on Master. If you have any problems, feel free to message me about it.

**Danny:**
Thanks. Like that.

**Pari:**
I shared a message on this card about Kurtosis. It's this tool you can use to spin up local multi client test nets. If anyone, wants to try that out, for example with your feature Branch versus stable from other clients, do let me know. I've shared documentation and happy to help out with that.

**Danny:**
Is Kurtosis using Kintsugi builds or is there going to be much work to swap it over?

**Pari:**
So you just specify it as a flag so you can just change that on the fly.

**Danny:**
Great.

**Pari:**
And at least the idea is to have that tested locally before you decide to join any devnets. That being said, I probably start working on a devnet tomorrow. Most likely with all the changes the devnet won't work, but if it does, then I'll let people know about it.

### Kiln client / experimental build status

***Summary***

- ***Consensus clients:***
    - ***Teku has a Kiln engine API implementation (but no authentication yet). Switch between Kintsugi and Kiln via a CLI flag, `-Xee-version kiln`***
    - ***Prysm has the implementation and passes tests, but no auth yet.***
    - ***Lodestar running against Nethermind and Geth. No auth yet.***
    - ***Nimbus, no authentication, but passing tests on local testnet.***
    - ***Lighthouse and Grandine implementations are in progress.***
- ***Execution clients:***
    - ***Versions of Geth and Nethermind are running against Lodestar.***

**Danny:**
Great. That can lead us into the next component. I know Kiln has been up for a relatively short time, but it's also not the deepest of change. For Pari's sake and for initial interops sake, where do people stand? Are there any Kiln V1 implementations on CL or EL?

**Adrian Sutton:**
Techu has a Kiln engine API implementation. We don't have authentication yet. we haven't done much testing on it, but we could be able to match that up with an EL that has it and actually check it works well.

**Terence:**
Prism, has, the implementation. We've just passed the vector test. I passed the, link of our test result there, and we still need, to do the authentication.

**Danny:**
Cool.

**Dapplion:**
Load Star. I'm going, to merge now implementation, and we are running in CL against Geth and Nethermind successfully. No authentication, though.

**Paul Hauner:**
yeah, a lot of assets still progressing with the Spec implementation.

**Dustin Brody:**
So if you're running in Nimbus. Nimbus likewise doesn't have authentication. There's a, branch which is passing tests thus far, but it's been, essentially local tests or local test net, type things.

**Saulius Grigaitis:**
We're working on that.

**Danny:**
Got it. And on the execution layer Dapplion you mentioned, you all are building against Geth and Nethermind. Or Geth and Nethermind , at least Spec compliant. I know there's a lot of productionizing to happen beyond Spec, compliance.

**Dapplion:**
Sorry, could you repeat?

**Danny:**
Pretty much, you're saying that Geth and Nethermind are Kiln compliant?

**Dapplion:**
Yeah, we're running. So this work has been done by a gender, but we are running some commit of some branch.

**Danny:**
Got it. Okay, so we're in the realm of being able to do some initial interop.

**Dapplion:**
I think so.

**Danny:**
Sounds good.

**Adrian Sutton:**
One thing I should have noted is there is a flag for techy, to switch from Kintsugi to Kiln mode will support both in the testing channel. Tbenner posted it just recently.

## Other client updates (if any)

**Summary:**

- **[PR #190](https://github.com/ethereum/beacon-APIs/pull/190) on API repos on how to respond to requests during optimistic sync - to be wrapped up soon.**
- **Question raised of execution payload deduplication.**
- **Merge community call for app developers, infrastructure providers, etc. is happening tomorrow (11 February 2022)**

**Danny:**
Thanks. Okay. Great. well, those are the primary items that we had in here. The additional stuff coming in V2 , which are these extensions. Kiln milestones. Thanks for giving the, update on your Kiln status and any testing discussions. Are there other merge, Kiln or other related items for discussion today?

**Paul Hauner:**
I have a PR open to the Beacon APIs repo. It's number 190 . It's, to add an execution optimistic flag to responses to indicate when we're returning information about optimistic data. It's, pretty tricky to figure out what we, want to do in terms of the API. If you go to that issue, you see, I've written some history about why we chose to do that.

I think it's getting pretty close, to the, point where we need to decide on how to standardize this API. So I intend to go forward with 190 unless we're going to get some opposition from people. It seems there's not a whole lot at this stage, but I just kind of, want to call last rounds on that one before we commit to it.

**Danny:**
Thanks, Paul. Yeah. Put your eyes on this thing. I agree. Waiting, beyond Monday doesn't make much sense. I think people have given their input.

**Dustin Brody:**
I don't know if this is better discussed in the issue or not, but I'll just say last I saw, it was just the same when there was an open question of changing the idea of an optional field or a little bit of chaos that might be, caused by changing the presence or absence of a field in return?

**Danny:**
Yeah, there's two conversations. One is the use of this additional Bool and the other is how do you upgrade if and how do you upgrade the spec versioning or the endpoint versioning. Paul, what's the state of that?

**Paul Hauner:**
I'm not sure, that there's a clear decision on whether we need to bump the tags or not on the version things or not. But either way, I think we need to go ahead with this change to the API. If anyone feels strongly either way about adding that field, they should jump into that issue and start. But that PR start commenting about it. It seems there's a precedence for adding things to that, like adding values there without bumping the version, so it's tempting to move ahead with that, get some opinions.

**Adrian Sutton:**
I very much like not to have to bump the version on everything. I think we've shown we can add metadata in the past, because otherwise we just wind up breaking every client. We got a change of a number in the URL. There's a slightly more complex one where that field wound up in the body for one of the requests and we currently I think the PR bumps that to be too. Personally, I prefer to leave that as V1 because it's still just an additional field. I'm not strong on it, though.

**Danny:**
Please take questions to 190. And yeah, I agree we should wrap this one up pretty soon. Other merge related items today?

**Mikhail Kalinin:**
I'd like to raise the question of execution payloads and duplication. So here is the PR for the context, the execution payload will be in current design, they will be stored on both EL and CL side and there is an idea to just float execution payloads from CL and request them from EL ad hoc. This PR is just one of the approaches to do this and it's been unattended for a while. and that current like default option is not included in the scope of the merge and not implemented at the merge and not implement this functionality unless there is the other opinions and somebody thinks that it will be critical for to have it at the merge. Also in addition, that if we want to introduce this kind of change after the merge, we don't need to do hard fork for that. So it may be implemented out of the hard fork timeline, which is good. And this problem of duplicated data will start to annoy us sometime after some period after the merge. So that's two things to consider.

**Danny:**
Right. The consensus layer is expected not to prune, at least to a depth of, I believe, four months. So what this looks like in practice is four months of duplicated execution payloads, or Eth1 blocks. It's essentially the size of what is on that network today. Four months of it.

You get additional storage on a local, node. did we run the numbers? I can't remember where the numbers are. It's probably not horrible, but then if you start looking into things like any of 4488 or any of these items where you're adding to the core block's size without doing any sort of sophisticated sharding, you get that multiplier on what that four months looks like. So it's probably something that's very nice to do in terms of timing. I would put it not super critical on the merge, but probably pretty important to get in, and Kyle, do you have an estimate on four months of execution payloads without 4488?

**Mikhail Kalinin:**
It's like to 80GB or some kind of it?

**Danny:**
I see.

**Mikhail Kalinin:**
If we take into, account the average size that is like average size of blocks that are on the main net currently.

**Terence:**
Are other clients, implementing indexing using the payload hash, whether it's to look up the payload itself or is to look up the beach and block that contains the payload? Because, I saw there's some discussion on Discord, but I wasn't sure whether there's some concrete conclusions that came up with it.

**Paul Hauner:**
The Lighthouse. We're trying to avoid creating an index for it. If it's pre - finalization, it's kind of lost for us at the moment. If it's after finalization as in unfinalized, then we, can just search the proto array for it, which is not one, but it's still, fast enough. Generally.

**Dustin Brody:**
This is a potential point of concern for Nimbus, because Nimbus is switching to depending more on slot numbers than hashes, as Paul was alluding to for pre finalization.

**Terence:**
Specifically, but I guess my concern is more on the API side. So consensus client will not serve this type of payload, so this will be outsourced to the execution layer client.

**Danny:**
Well, the idea is that there's network protocols where you would be expected to serve it, but if you had deduplicated it, you'd need to be able to dynamically get it from your execution layer to serve those requests on that four month balance. And so there's probably two ways. One is to do this hash look up where I just give the execution layer a bunch of hashes to retrieve them. Or you could do a more like by range request, and there was a bit of debate, probably six or eight weeks ago on that, and the hash look up is currently what's in that PR, but you could probably make, an argument to be doing the by range request as well. But again, that's an implication, not, really for the execution layer I guess you need to be able to get those payload hashes for requests, but it's more of an implication on the execution layer, I'd say.

**Terence:**
Got it.

**Danny:**
Okay. I'm not super eager to try to release this in Kiln. I think that this is something, we should have discussion with the execution layer on. I know, Mikhail, and you had done some initial discussion with geth, especially on those hash lookups, but it might be worth opening that up once more before we push this PR one way or the other.

**Mikhail Kalinin:**
Right. And I would say that if, like still clients think that it's critical. Just comment on this PR, write this question in Chat and Discord so we can proceed with that. Otherwise, as I said, the default option is just leave it there, as it is now.

**Tim Beiko:**
Yeah, I'm not sure how many EL client does or, I guess if all EL clients will watch this. So maybe we're just having an explicit opinion on Discord.

**Mikhail Kalinin:**
I think this is critical for CL more than for EL, like having this feature and yeah, definitely adverse engage EL clients, into discussion, when we will be finding, the right way of doing of implementing and design and functionality.

**Danny:**
Suppose the question of criticalness is a software implication for the CL, but it's also just what are the full node requirements? Because if you don't add this, it is plus 60 to 80 or so gigabytes of requirement, which kind of impacts the unification of CL and EL.

Okay, please chime in there and we will continue, the conversation. Anything else on this one before we move on?

**Mikhail Kalinin:**
Nothing from my side.

**Danny:**
Okay. Other merge and kiln related items for today?

**Paul Hauner:**
I did just want to raise that something we're looking at now is trying to collect the fee recipient from all existing phase Zero validators before the merge. Kind of putting interactive prompts, and warnings and stuff around the VC and trying to keep track of people who haven't provided their fee recipient. I just want to kind of raise it because it's going to be something that faces all clients. It's probably going to require updating to all of the become a validator guides. Yeah, it's going to be a bit of a weird, thing where we have to collect one piece of information, extra information from all the validators. So I just wanted to kind of mention that to bring it to implementers minds. And also it's something that people who are doing kind of education and documentation are going to have to deal with, as well.

**Terence:**
This is a great question. Do you know if there's any documentation around that already? Because I saw Tech Tool has implemented this already. So I wonder if we should have some sort, of standard alignment across this.

**Paul Hauner:**
Yeah, I don't know of any documentation about it. I wasn't aware that Tech had already done it. We became nice if we, could make it uniform.

**Danny:**
So there's two things here. One is where are you providing this information? Is it per valid or on the VC? Is there a backup on the BN, like that kind of stuff? And then the other is because we're going to need to gather the information, how does the client go about getting that from the user? And both of those need to be answered in the same way. I believe the answers to the former or there's beginning to be conformance on maybe be in fallback, but the VC by default drives on a per validator basis. Is that the case?

**Paul Hauner:**
Yeah, we're kind of like the graffiti in a lot of ways. It's a similar deal where it's like the value of the client. You can supply one that applies to all of them. You can go and edit a file where you can manually specify it for each validator. And there's also an option to read it from a flag from a file so you can change it programmatically. And if none of that works in the VC, then the BN can have a backup one to deal with it. Not sure we necessarily need, to standardize all of that just because it leaves room for innovation. But yeah, the other one about figuring out how and when to collect it. And yeah, it's something we could, probably standardize on. I think what we might influence to the time being is you can just edit we had this validated definitions file, so you can just edit this YAML file and add a key for all your validators if you want. And also the really super easy way is, that you can have a prompt when you start your VC. You get a prompt if you don't have a fee recipient for any validator and you need to fill it in to continue, it will have a flag to bypass that for, people who are dealing with automated setups.

I briefly talked to Mikhail. He said that it's been raised once before.

**Danny:**
Got it, and I was going to just say I was muted in talking to myself for a second. The trend, we should add that to kind of our outreach list. I think in general we should do around to make sure that we get in touch with all the ecosystem participants that maintain guides, and there's probably a handful of things we want to nudge them on. and this is one of them.

**Trenton Van Epps:**
Sound good.

**Danny:**
Anything else on that? Okay. Other items for today on the merge?

**Tim Beiko:**
Oh, sorry. One quick shout out. There is a merge community call tomorrow, basically the same time as this call. So, we're going to get application developers, infrastructure providers and whatnot to come and ask their questions. It's always helpful if they have full of client devs show up when there's more technical questions, or if you just want, to show your clients to people, the ecosystem. So there's an issue on the, PM repo, but it basically starts at the same time as this call tomorrow.

**Danny:**
Cool. You all should get a couple of clients, to raise their hand saying that they'll deploy their client end to end on kiln, full interfaces and everything.

**Tim Beiko:**
You mean applications, right?

**Danny:**
Yeah. Sorry. Application developers.

**Tim Beiko:**
Yes, that's it all. And if people here have ideas of applications that are tracing heavy, I think that's one thing that we haven't been able to like. I don't have a great candidate off the top of my mind. So if people have ideas of something that's like, tracing heavy, that we could deploy on Kiln to make sure all of that works is expected, that would be really valuable.

**Danny:**
Who are the big tracers? I know exchanges always say so. I would assume maybe the...

**Tim Beiko:**
Block explorers. I've asked them. A lot of them are pretty busy right now, so they haven't said they won't do it, but they haven't committed. The exchanges and block explorers are the two that I had off the top of my head.

**Danny:**
Got it. Thanks Tim. Other merge items?

Cool. Thank you to some of our devs that joined. Sweet. Moving on. are there any other client related updates that people would like to share today? No. Okay. Excellent.

## Research, spec, etc

***Summary:***

- ***Eth1 Shanghai fork - working on a feature set for consensus-side counterpart:***
    - ***EIP for withdrawals on exec layer is in progress, need to mirror this on the consensus layer.***
    - ***Jacek’s clean up of historical roots could be added.***
    - ***Discussion of Vitalik’s block data transactions proposals***
    - ***Dank Sharding educational workshop might happen next week. In planning.***

**Danny:**
Easy research spec R&D, items. I know there's a lot of stuff floating around on some, dank sharding, data availability sampling and various things. Any updates or comments here?

I guess we'll say in preparation for what is on the execution layer called Shanghai, we should be honing in on a feature set for that associated fork. Execution layer EIP for withdrawals is in progress to complement the work in progress, PRs on the consensus layer to put them together for withdrawals for executive validators and partial withdrawals for proposers, assuming that that goes to Shanghai. we'll get those specs there now in the consensus layer.

I think the other additional item we've been talking about is Jacek's cleanup of historic roots, and I'm not sure if there's anything else other than maybe kind of these fork choice updates like that being a very concrete place in which if they had not been upgraded, they become upgraded. Are there other things that I'm missing for the discussion for that, future fork?

**Tim Beiko:**
The one thing I think this is unlikely, but Vitalik had these two proposals, for block data transactions, I think the more complex one might have some work on the beacon chain. Right.

**Vitalik Buterin:**
Yeah.

**Tim Beiko:**
I think it's more likely we do the simpler one, but if we were to do more so.

**Vitalik Buterin:**
The discussion on this side has been increasingly going in the direction of the more complex one. The argument is that even though the total implementation complexity of the complex one is higher. The simple one puts all of the effort, on the execution clients and the total. And the more complex one was a bit less effort on execution clients and more on beacon clients. And execution clients are already expected to be very overworked for Shanghai.

**Tim Beiko:**
Oh, I like that, actually.

**Danny:**
And that more complex one does get to something that looks much more like a final sharding proposal. And the complexity, on the consensus side ends up being primarily the updating of data structures and the management of data. Not a lot of what I call consensus, complexity.

**Vitalik Buterin:**
Right. It's like the consensus complexity is not very high in the consensus side, not very high in the execution side. By far the highest complexity of that EIP is on the block creation side, actually, because of how, it introduces these transactions where the transaction has a piece that goes on one side and a piece that goes on the other, side. But in some ways, if we're willing to make some sacrifices, that kind of complexity is fairly manageable. Basically, we only really need one implementation that can make these blocks. And if we, have one good one, Then as long as everyone can do the verification, It would still be fine.

**Danny:**
So just a heads up. EthDenver comes up next week and there's a crew that is attempting to prototype a version of this end to end. So hopefully have some more insight through that exploration.

But, yeah, that's definitely the other item that's being explored and potentially in what might be called Shanghai or subsequent upgrade. we had discussed in another channel to do a dank sharding educational workshop for the consensus layer, and I guess anyone that wants to join, we tentatively discuss early this coming, week. I'm going to circle back with Dankrad, who's on this call, actually, and some others to see if we want to target a date for this coming week. I think it'd be valuable to get in before the EthDenver sprint, but we'll, let you know very soon.

Cool. Other things? Other items? Things to discuss?

## Open Discussion/Closing Remarks

**Danny:**
Okay. The silence implies we are reaching the end of the meeting. Are there any other items to discuss, any announcements, anything today?

I will say the Dev connect dates are public. That's the 18th to 25th. There's going to be lots of fun stuff going on. That initial calendar is out. We do plan on, doing some L1 R&D workshop stuff right at the beginning. So if you're going to make some portion of the week and not the entire one, I'd say show up right at the beginning. More details for that soon.

Cool. Let's close it out. Thank you. Easy meeting and see you all on, all these fun Kiln milestones. Talk soon.

**Everyone:**
Bye. Thank you.

## Chat Highlights

***From danny to Everyone 02:03 PM:***
[https://github.com/ethereum/pm/issues/475](https://github.com/ethereum/pm/issues/475),
[https://notes.ethereum.org/@timbeiko/kiln-milestones](https://notes.ethereum.org/@timbeiko/kiln-milestones)

***From pari to Everyone 02:10 PM:***
Would be great if client teams can share info on builds here: [https://notes.ethereum.org/D5xK4XrmTb6MKGudf_hcrg](https://notes.ethereum.org/D5xK4XrmTb6MKGudf_hcrg)

***From terence(prysmaticlabs) to Everyone 02:10 PM:***
[https://gist.github.com/rauljordan/dd5aef5c35a98ae67989601c83aafde1](https://gist.github.com/rauljordan/dd5aef5c35a98ae67989601c83aafde1)

***From pari to Everyone 02:12 PM:***
Docs for getting started with kurtosis can be found here: [https://notes.ethereum.org/@ExXcnR0-SJGthjz1dwkA1A/H11OzhRAK](https://notes.ethereum.org/@ExXcnR0-SJGthjz1dwkA1A/H11OzhRAK)

***From Adrian Sutton to Everyone 02:13 PM:***
Switch teku to kiln mode for the Engine API: --Xee-version kiln

***From pari to Everyone 02:14 PM:***
So the following would be the participants for merge-devnet-4, lemme know if other clients also feel ready. CL: teku, lodestar, nimbus. EL: geth, nethermind

***From danny to Everyone 02:14 PM:***
[https://github.com/ethereum/beacon-APIs/pull/190](https://github.com/ethereum/beacon-APIs/pull/190)

***From Mikhail Kalinin to Everyone 02:17 PM:***
[https://github.com/ethereum/execution-apis/pull/146](https://github.com/ethereum/execution-apis/pull/146)

***From Mikhail Kalinin to Everyone 02:23 PM:***
[https://github.com/ethereum/execution-apis/issues/137](https://github.com/ethereum/execution-apis/issues/137)discussion thread ^

***From Adrian Sutton to Everyone 02:27 PM:***
Teku implementation with some details of how it works in the PR description: [https://github.com/ConsenSys/teku/pull/4894](https://github.com/ConsenSys/teku/pull/4894)

***From Mikhail Kalinin to Everyone 02:32 PM:***
When are we having the first kiln devnet?

***From pari to Everyone 02:33 PM:***
I will plan to get one up tomorrow, can’t guarantee it will work. If it fails, I’ll try again on monday.Calling it merge-devnet-4

***From Mikhail Kalinin to Everyone 02:33 PM:***
👍

***From Tim Beiko to Everyone 02:36 PM:***
Link for context: [https://github.com/ethereum/pm/issues/459#issuecomment-1029529089](https://github.com/ethereum/pm/issues/459#issuecomment-1029529089)

## Attendees

- Danny
- Vitalik Buterin
- Carl S.
- Pari
- Terence
- Adrian Sutton
- Mikhail Kalinin
- Tim Beiko
- Paul Hauner
- Mamy
- Lightclient
- Dapplion
- Justin Drake
- Saulius Grigaitis
- Trenton Van Epps
- Enrico Del Fante
- Ben Edgington
- Pooja Ranjan
- Dankrad Feist
- James He
- Fredrik
- Rafael Matias
- Alex Stokes
- Andrew Ashikhmin
- Protolambda
- Dustin Brody
