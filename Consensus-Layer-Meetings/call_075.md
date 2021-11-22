# Consensus Layer Call #75

### Meeting Date/Time: Nov 4, 2021, 15:00 UTC

### Meeting Duration: 1 hour 30 min

### [Github Agenda](https://github.com/ethereum/pm/issues/412)

### [Video of the meeting](https://www.youtube.com/watch?v=9U_xj_zCMYg)

### Moderator: Danny Ryan

### Notes: Joshua

## Summary

- Client teams beginning to implement Kintsugi
- There might be small spec Kintsugi changes over the next week but nothing major
- Pyrmont testnet to be killed
- Proposer boost fix (Fork Choice Vulnerabilities) has been thoroughly analysed by Stanford team. Results next week.

# [Kintsugi office hours](https://www.youtube.com/watch?v=9U_xj_zCMYg)

**Danny Ryan  01:16**

We made a commitment to deprecating the Eth 2.0 pm repo by mid November so the issues are now going to be tracked there, I still need to do some cleanup on where notes and things live. But the merge stuff has moved over there and consensus layer stuff is now moved over there so we can track all of our breakout calls and things in one place.  Okay, so Kintsugi. This was an effort that kind of spun out from the Amphora interopt with the plan to finish the many minor spec changes that came out of discussions at the Amphora in-person interopt. We did a sprint to finish those spec changes. And now the plan after that was to hit it hard in November with the target of a persistent testnet. Definitely approaching more production grade quality engineering, at the end of this month, the end of this month means probably something more like December 1 or second for the launch of that testnet and Perry is going to be helping us with that and helping us weekly when we do get some people hitting some of those first milestones doing a weekly devnet build. So we have released the stock Kintsugi. Thank you, Tim, for the excellent name here. [Here's the Doc](https://notes.ethereum.org/@djrtwo/kintsugi-milestones), I'm sure it looks like a lot of people have already seen this. And at the bottom, we note that both the consensus call and the all core devs call, which I might call the execution layer call, will the first 30 to 45 minutes of each call be dedicated to more of a cross layer, office hours stand up discussion. Just to make sure we're we're touching base and identifying any issues and sharing information along the way. So that's what we're gonna do this morning. I invite with folks from the execution layer to this call and I invite folks from the consensus layer to the all core devs call on the opposite week. I think we'll do like a little bit of a quick stand up kind of like we did in Amphora. Doesn't have to be too deep but I know not everyone has begun. But just a quick round if you are on the call, and you're on a client team and there's any update with respect to Kintsugi  we'll kind of run through that. And then we'll open it up for questions and discussion, I know there has been a lot of discussion on Discord already and I will note that we do expect especially in this first week for some minor changes to land in the specs and we'll make it abundantly clear that that is happening and through the month we expect less than less of that although there's always a chance that there's a minor change between a devnet build weekly. Any questions about anything at a high level? What we're kind of planning to do this next month or how things may proceed? Okay, cool. So let's do let's do a quick round on where people are out on Kintsugi. I know it's just been out for a couple days but if you have opened it up and begun, give us a quick update.

**Marius Van Der Wijden  05:21**

For Geth we started or I started implementing the spec. It was finished, and then the API changed a bit again so I haven't haven't done that yet. But I'm going to change the PR to reflect the correct spec today. And I also updated the test vectors. Again, they are not up to the newest spec, but like only the fractures, updated method changed a bit in the newest version. So it's a good starting point for anyone looking into implementing this. Just to make sure that you have the basic format, right, I'm not sure if the format is correct. Anyways, it would be cool to double check with other collectives. That's it.

**Danny Ryan**  06:24

Great. And I will note that the Engine API spec changed out from under your feet because of the changes you requested.

**Marek Moraczyński**  06:36

So in Nethermind, we have just started implementation of the spec. So I hope we will deliver it very, very soon. Yeah, that is short update from Nethermind.

**Adrian Sutton**  06:46

For Teku, we are a little caught on the backfoot. We were merging all the Amphora stuff over to master and getting that production ready. And then somebody dropped a new release and said we're doing testnets. So we're going to try and do both and get that all into master and be ready for the first devnet, the updated spec, on master. Toggled off, obviously. So it's good code. Not as hacky as Amphora was, but not exactly production ready.

**Danny Ryan**  07:26

Yeah, I apologise for any failures and communication here. I think those at the event were very aware. And maybe we had mentioned on some calls that this was the plan, but did not make it very clear. So I apologise if we caught everyone off guard on there.

**Adrian Sutton**  07:41

No, it's not a problem, I think. I think it's the right way to go for us anyway, to be honest even if I was more aware of it. So good.

**Terence Tsao**  07:53

Yeah, I can go next. So for Prysm we are Yep. Short and sweet. Were are aligning the consensus spec, we are aligning to the new API calls. So hopefully we'll do those things soon.

**Mehdi Zerouali**  08:08

Yeah, same for lighthouse. We just started the work on Kintsugi. We have a PR open that documents our progress - PR 2768. So early days for us. But yeah, not much to report from the fact that Paul's been working on a production ready optimistic sync implementation for lighthouse. He's going to document his findings as usual and sharing that with you shortly. He's also looking at how to structure the beacon node and validator client API for giving early notice of block proposals. Same here, he'll update everyone on his progress.

**Adrian Sutton**  08:49

Yeah, that's probably one of the big things to address is updating the standard API's, particularly the ones the validators need. So I did see that ticket in the lighthouse repo, that's quite useful. I need to digest it a little better and get to that point, but getting some of that stuff into the actual standard API repo with proposals of what things look like could be really good.

**Saulius Grigaitis**  09:11

So we started to work on the tests and most of the tests for the merge are passing. But we are are missing the integration of the execution layer code. I think this will be done in a week or two.

**Danny Ryan**  09:50

Any other updates?

**Mamy Ratsimbazafy**  09:53

For Nimbus, we are always keeping track of the spec. And for Kintsugi specifically We have a call in two hours for monthly planning. So this will be high priority.

**Marek Moraczyński**  10:12

Lodestar: we created an issue today, hopefully put some resources and work on the next week.

**Marius Van Der Wijden**  10:35

If that's all of the clients, I would like to talk quickly about something that that's happening in Geth. So we haven't yet merged the changes from Amphora to master. And so we also cannot, like I want to get those changes in first and then get the Kintsugi changes in second. And then we also need to update, we also don't have to reverse header sync in master. So we have like three open PRs that need to be merged until then we cannot have a working testnet from our side. So even though like, I've implemented the spec there's some dependencies because it doesn't have any syncing in it yet. So for the for the interopt we hacked something together, but we don't want to do this. It might take another week for us to create a client that is can actually sync.

**Danny Ryan**  11:54

Makes sense. And that's one of the things I want to talk about was when we have at least I think one client on each side of the aisle. We do want to begin to do these weekly devnet builds, but my current intuition is that that is not one week from now, but maybe two weeks from now, on that Thursday. Does that seem reasonable? Is anybody eager and thinks that we might be doing a devnet build in one week? Okay, so we will skip the 11th and target the 18th. And plan on doing the 18th and the 25th. We'll do a devnet build and and bring in more clients as already. And then that following week, assuming things are going well target that persistent testnets. Are there things that people would like to discuss synchronously? Are there questions with respect to anything in specs? Just open time for discussion?

**Terence Tsao**  13:25

How's everyone feeling about testing optimistic sync is saying because like testing in production doesn't sound nice, right. But this is not something you can also sky test. So I think by using merge mock, the two that the Proto and Lightclient wrote would be nice. So just want to ask, what's the progress on that?

**Danny Ryan**  13:52

So another tool to disposal is definitely Hive. And there are some members of this call and others that are are looking into it. But yeah, lightclient do want to give us update on merge mock?

**Matt Garnett**  14:07

Yeah, I'm currently implementing the latest Engine API spec on Merge mock, that's should be done the next day or two. And then like the longer term goal in the next week or two is to have a way of accepting like test vectors that are statically generated into mock so that we can all kind of run the same sorts of tests rather than what it's doing now, which is just sort of generating random valid message follows. And then you should be able to just use that to test either your execution client or your consensus client.

**Danny Ryan**  14:43

Does anyone want to give an update on hive? There were some discussions at the in person event on strategy here. I don't think we've dug into those strategies, but to discuss what the the high level plans are here?

**Diederik Loerakker**  15:01

I can give a summary of where we're at with Hive. There's this one PR open that's introduces ETH2.0 clients into hive. I think this is just the prerequisites before we can look at the merge at all. You need some kind of base to introduce Ethereum 2.0. Then after that, if that's stable, then you can replicate that but then instead of running the phase 0 or Altair fork, you can run the merge fork. With the merge the change this connection to the execution layer. So there's the slight change the configuration that authorises the same setup, and it does spin up the whole thing. So boot nodes, Ethereum 1.0, and Ethereum 2.0. And then after that, once you have this general testnet, simulator working, we should look at the next type of tests where it tries to do something more interesting, something less common.

**Danny Ryan**  16:16

Although testing hive, etc, doesn't get is not as exciting as some of the other stuff, I do think that testing is probably the long tail here. So if someone on your team wants to dig in, that'd be very, very valuable.

**Marius Van Der Wijden**  16:38

So I also started fuzzing. I created a fuzzer for the execution layer engines. And I started fuzzing Geth against Besu. And found some differences already. I'm going to also continue working on that next to hive. I also have a tool for sending fast transactions to the actual testnets. So once the testnets go up, we can create fast transactions.

**Danny Ryan**  17:26

Got it. And there are consensus layer vectors, as usual, but there's probably some spots will show up in the next couple of weeks. And we get an iterative testing release out. And the plan I'm sure is to integrate merge builds into the the decomposed infrastructure when the time comes. And then on the execution layer side. There are certainly a series of vectors we do need to create around this random opcode and some of the other things. So that and then integrating into the normal fuzzing infrastructure, what's the normal path on getting the execution layer EVM style vectors written?

**Marius Van Der Wijden**  18:21

So we have a test team, the Ethereum test team that is working on the EVM test vectors, so we can just ask them to create some for these new opcodes. The problem is that the infrastructure is very much based on ethhash and the current way it works. And so I think they need to put a lot of time into making sure the testing works post merge.

**Matt Garnett**  19:01

How are you expecting that clients should import these vectors? Because like today, you're kind of using this import sub command, it's just taking in RLP blocks. But after the merge, if you want to test things from the consensus layer as well, and you need to have some sort of directors from the Engine API. Is that something that would also be supported by the import sub command?

**Marius Van Der Wijden**  19:29

I'm not sure.

**Danny Ryan**  19:33

Does the import sub command actually need anything from the consensus layer or essentially just these inner blocks these payloads?

**Matt Garnett**  19:44

I guess I'm not sure how I would deal with a fork because like if I give it two chains that are the same length, it doesn't really know anything about what's the canonical head?

**Danny Ryan**  19:55

I didn't know if those test vectors dealt with a block tree. rather than just a chain, but they do.

**Matt Garnett**  20:02

Yeah, I think that the blockchain test just support sending like, whatever RLP blocks and you can submit a tree if you want.

**Marius Van Der Wijden**  20:15

I don't think that those are the important ones. I think the important ones, like for testing the random opcode is just the general state tests. And those are just basically just a transaction. This can be applied pretty easily.

**Danny Ryan**  20:42

And similarly, there's going to be some that we probably want to see rejection due to nonzero values and headers and things. But those should be the pretty standard, as well. Right, Marius?

**Marius Van Der Wijden**  20:55

Yes. So as long as you have like, give it a block that is invalid, then it should be rejected. This is pretty easy. But yeah, I'm not sure if we can.

**Matt Garnett**  21:11

If you give a valid block, will the RPC update without the engine command, because I like wondering if hive if I'm asking is this block in a canonical chain, meaning it was like accepted invalid, it may not return, because it may just be waiting around for like, for  updates.

**Marius Van Der Wijden**  21:30

If you if you set up hive with a chain, that is that is valid or like, doesn't even need to be valid, then you can query for the chain. But right now, you cannot really add a block to the chain, when you could maybe but like this, this is something that needs like there needs to be some more stuff implemented there. To enable it in the tests.

**Danny Ryan**  22:08

I think at a bare minimum, maybe in the next few days, we can create a spreadsheet with the vectors that we do want to get in, like the standard kind of pass fail vectors, and then figure out how to integrate those.

**Marius Van Der Wijden**  22:23

I also started when I worked on getting everything merge to master, I already started a document with things that I think are dangerous and that we should test for. I'm going to share this document in the interopt channel. It's just a general collection of everything that I think is going to be difficult, or something that we should test for. And if you have anything to add to that, then just please edit and in the end, we can go through all of them and make test cases out of this. Or check that this is something that cannot happen in the code.

**Mikhail Kalinin**  23:22

Like including hive and complex and errors within communication between the layers as well? I mean those Marius those, like test cases that you have just mentioned, are they for standalone testing, or should they CL also be involved?

**Marius Van Der Wijden**  23:46

Right now it was just a brain dump during implementation, so that I like I like those are the things that I thought about during implementation that could maybe go wrong. And so I'm not sure. Probably need some stuff on the consensus layer as well. I'm not sure.

**Danny Ryan**  24:13

My gut is to test things separately on layers where where possible, and where makes sense. So for example, like to reject a block with uncles, you know, that's an execution layer test. Whereas, certainly, integration style testing and more complex scenarios we want to hoist into hive and other places.

**Mikhail Kalinin**  24:37

Right but rejecting this kind of block should be done through execute payload, right. It should not be in general. Like I mean, the execute payload triggers a different code branch than the usual processing in the proof-of-work network.

**Danny Ryan**  24:59

Right? I mean, whether it's via execute payload, or essentially, if you're importing a block and your post merge functionality. So if some conditionals is hit, then that should be validated as such.

**Mikhail Kalinin**  25:16

Yeah. Okay. So if it needs to be discussed how to design this kind of tests. Will client support really all clients support this kind of flag that they are operating in the proof-of-stake environment? And then every input block will mean that happens. Adhere in the rules in the EIP-3675. Or not? Probably, it's easier for doing it that way, then we can keep the implementation of the EIP is the tests. And that test the implementation of EIP separately from the Engine API, which would be good, I guess.

**Jacek Sieka**  26:15

One way that this kind of conformance testing is done is through a mocking setup. Because we'll end up with very, very many combinations of different clients. Right. I guess. One potential test setup is that we have like a dedicated tester, because everything is through API's and should be able to validate that a client gives correct responses and does the right thing in response to being prodded the right way through an API.

**Danny Ryan**  26:54

Yeah, I agree, which may be merged mock is angling in that direction. To be that such a tool?

**Jacek Sieka**  27:02

Yeah, right. And that would sit like in right in the middle of the star with testing, instead of making a mesh of testing we make a star of testing with this in the middle.

**Danny Ryan**  27:16

Right. There's probably still value in on some sort of nightly or weekly build that actually tests literal client combinations with our nice n squared star. Mesh, not star.

**Jacek Sieka**  27:35

Yeah, but this middle tool is very helpful during development.

**Danny Ryan**  27:38

Agreed, agreed very much. Other testing stuff people want to discuss we are at the half hour, happy to I mean, we can take this as long as we want other Kintsugi related items we'd like to discuss today. Okay, the merge interopt channel on Discord is I believe, where a lot of the pretty active discussion around the finer details here will happen. So make sure you keep an eye on that one. A week from tomorrow. The allcoredev call will also have the opening dedicated to Kintsugi. If it ends up being valuable, and we want to schedule a call in between those calls, maybe something that's super informal, just hop in the chat on Discord. We can do so I guess just holler if you're hitting a wall or have some things you want to discuss, and we can maybe hop in on Tuesday or something. But for now, we'll plan on at least doing that weekly. Anything else related to Kintsugi before we move on?

**Saulius Grigaitis**  29:23

Yes, quick notes. There was this PR merge this morning. The update to fork just updated the order speak canonical for Kintsugi right now or how do we approach those?

**Danny Ryan**  29:37

Yes, I mentioned at the beginning of the call I think especially in this first week, we might see some minor updates based on discussions, make it in and we will make that very clear. Especially because we don't have the the first devnet isn't until two weeks from now. We do expect maybe between now and Tuesday or Wednesday to see a couple of minor iterations we'll make that very clear. And as we're approaching devnets make sure testing is in line with the releases and that the releases are very, very well known.

**Marius Van Der Wijden**  30:09

Can we have some, at least some internal version number or something? So that we know that if someone's like, just updated the code, and then something new comes up, then that they need to update again.

**Danny Ryan**  30:24

So essentially version, the Kintsugi meta spec?

**Marius Van Der Wijden**  30:28

Yes, because it was like I implemented everything two days ago. And then the payload id changed from 8 bit to 32 bit. And I didn't actually see that. And and now the purchase updated, so I need to update my code twice.

**Danny Ryan**  30:50

To be fair, you have you implemented before this was even released. So the the 32 byte always in the in the original release. But yes, we're gonna try to do this. Not a lot. I mean, we're generally in like a reasonable place. I think a lot of the decisions were made at the Amphora interopt. And I don't expect big things to be changed. But yes, we'll try to not pull the rug out from under your feet. And to make it very, very clear, what's going on here. And we can call, what is the update that will likely come out tomorrow, you know, Kintsugi v2, to make it better for internal versioning?

**Matt Garnett**  31:36

So are you saying that we're going to want to have another release of the Engine API with this PR? Are you wanting to wait a week to get feedback?

**Danny Ryan**  31:46

I don't expect a lot of changes to come. And so I do want to just kind of get them out pretty quickly.

31:53

Okay, so clients and right now it should be like, getting ready to do it with new prs? Not with the hashing of the payload, correct?

**Danny Ryan**  32:02

Correct. Again, I'd like to add anything that we do want to get changed do it very quickly, so that we can quickly conform on something and not worry about version changes anymore.

**Jacek Sieka**  32:16

For aync in particular, we discuss an addition of block export. So that the beacon blocks by range request can be implemented in the consensus layer, right? And something that would be nice to get in, inthat case.

**Danny Ryan**  32:37

I agree, I see that as at least barring the beacon blocks by range not having execution payloads. If that change ended up... deduplication across layers is a bit more additive. So, I would like to open up that conversation but I think we can get the core done without that.

**Mikhail Kalinin**  33:03

But there is definitely things to discuss. Because it could be a couple of approaches that could work.

**Danny Ryan**  33:14

We did take notes on some design options with respect to duplication of execution payloads across layers and calls to get them back. So let's surface those this coming week and try to get a plan of action done.

**Diederik Loerakker**  33:59

Is their intention to run like call the combinations of execution and clients on a testnet or this is like just one combo from each team?

**Danny Ryan**  34:15

The goal would be to run all combinations. All stable combinations I believe are run on the Amphora and Pithos testnets. And with the automation tooling that Pari, proto, and others have been working on, it is not too insane to do this. Make sure all the combinations are represented

**Saulius Grigaitis**  34:40

okay and this this automation tooling was mainly done not by client teams?

**Danny Ryan**  34:45

Correct. Pari you can you can fill in the gaps here. I believe build instructions and Docker images were shared and inserted periods. Pari, anything else that was critical and getting that done?

**Parithosh Jayanthi**  35:00

No, I don't think so. But if you're having any issues, feel free to text me on telegram or discord and I can help out.

# [Other client updates](https://youtu.be/9U_xj_zCMYg?t=2122)

**Danny Ryan**  35:19

All right, anything else related to Kintsugi? Let me find my issue. All right, we can generally move on, if you're part of the execution layer, by all means stay and join us. But if you want to go, go. Next up, we have other client updates if there's anything, research spec, etc. and actually we'll do a point in between those two, which would be discussion of Pyrmont. And then open discussion closing remarks. First of all, other client updates, anything that people would like to share, in addition to the Kintsugi.

**Adrian Sutton**  36:17

We're doing a fair bit of work on the key management API, we're hoping to try and get the current version that built as a more than a proof of concept, but can't really call it production until the API is fully settled. So I think that's happening in few clients, which is promising. And hopefully, we can start getting some stuff up around that.

**Danny Ryan**  36:41

Great, and there was a request to make a separate repo, I guess the potential counter would be to put it in the beacon API's even though that's not super semantically sound. Or there are strong feelings on separate repo versus beacon API's? James, I see you unmuted, but I can't hear you if you're talking.

**James He**  37:14

Sorry. Can you hear me now? Yes. Um, I don't, I don't think there's any, like, strong feelings to move out outside or keep it inside. That's why I ended up reaching out to you. I didn't know if anyone from like the foundation side could give any direction on that.

**Danny Ryan**  37:43

Yeah, I mean, ultimately, I think it's a matter of where people want things to live. Beacon API's kind of implies that it's the things you're getting from the beacon. Although we could have a totally separate directory and make it very clear in the readme, that there's also these things that you can get from the validator client. But I'm also totally fine with making a repo as well.

**James He**  38:12

I think the only argument for keeping it there was that not all the clients have separate entities called like the validator piece of it.

**Danny Ryan**  38:29

It's definitely a different kind of, you can logically think about it as a different module, regardless of ultimately if it's a different piece of software or not.

**James He**  38:44

Yep, I'm okay either way.

**Danny Ryan**  38:52

I think that there was the slightly leaning in direction of new repo, new API. Does anybody feel strongly opposed to that or voiced an argument the other direction?

**Marek Moraczyński**  39:08

I mean, this is the same discussion that many teams have with going mono repo or not. I think at the end, it's more of an organisation thing. So if you want to group issues, and you want to have support in the same place, also with CI, it's similar. So this question would like lay down more on that on how you guys want to organise? And how many records do you want to maintain it? That's an issue.

**Danny Ryan**  39:34

I'm also kind of going off the fact that execution API's are a different repo. Obviously they're even more carved out in a different place but I'm personally not going to spend a lot of time maintaining this. I so I would love for somebody else to have a strong opinion on it.

**James He**  40:08

I think we can we can break it out.

**Danny Ryan**  40:12

Let's give that a shot. All right, I can put in a request to make a new repo and get some permission shared and try to get this moving.

**James He**  40:31

All right, thank you.

**Danny Ryan**  40:32

Yeah. Cool, cool. Other client updates?

**Mehdi Zerouali**  40:52

We're quite happy with that release, and how things were running. And we're now back into our normal release cycle. Expect another release in the next few weeks, I guess. We've been also chatting with Flashbots, about how their system might work post merge, and making some good progress actually on that front. Paul has put together really, really thoughtful document that I'm sure he'll be sharing with you all shortly. I know Michael has been working on a bunch of slasher database optimizations, including some the duplication of attestations resulting in some great data disk usage saving. I'm sure he'll share that with you all as well. And the only thing I guess we should probably just discuss is allowing client teams to exit from Pyrmont to save server fees and maintenance labour. So I think we're on board. Not sure if that's been already active, but something to discuss.

**Danny Ryan**  41:57

Yeah, we'll pick that up right after the client updates.

**Terence Tsao**  42:02

Yep, I can go next. So from our end, and lots of optimizations on our beacon tree structure. So Nisha, has been doing great work on that. And we have been participating in lots of standardizations on the Beacon validator key API. So really happy to see effort on that front. And I have started looking more into the fortress fixes, in particular, the proposal boost. So I've been started refactoring our array for choice implementation to make you more modularized and testable. And I guess I do want to ask later, what timeline that we're looking at in terms of, I understand that this to happen, a synchronicity. We can roll this up to Mainnet. But I do want to know, like, what month are people looking at so that I can prepare or budget more work to it, but we can talk more on that later?

**Danny Ryan**  43:03

Yeah, let's pick that up right after this too. Anything else any other updates, we want to share?

**Marek Moraczyński**  43:44

Lodestar: we are connecting with the portal network folks to figure out how to decentralise the networking on the lightclient. And it's looking good. That's it.

**Danny Ryan**  43:58

Great. Okay, let's talk about Pyrmont. We decided to kill Pyrmont. We decided that a long time ago. And it's is now near about the size of main net and I plan to continue to to grow. Given that we've already made decision on this, I think that we can, if we are all still happy with that, kill it. I mean, obviously you can't kill a testnet fully. But you can just turn things off and see what happens. There are two potential things we could do with it. One would be to kill it and a bit more interesting way, you know, maybe turn off half of all the nodes and validators and observe just to see. Another thing that we can do is save it for the merge. For a mergetest. But we do have the capabilities to spin up very large testnets without too much problem. And so we can happily kill Pyrmont. And then in January, spin up a testnet very easily to do a merge test. Given that we do have a number of these proof of work and clique testnets. I think for any of those that we want to continue forward, what we would do is create a Beacon Chain testnet analogue against that one, and then do a merge. And for those, they don't need to be nearly as many nodes or many validators as Prater. So for example, we could just do like 100 validators and one node per team. And that ends looking more like a proof of authority net, and then do a merge and say, like merge drop centre or something, although I think they're trying to kill Ropstein. So even with the the merge testing and merge testnets coming, we don't need Pyrmont. And in fact, we already have a Beacon Chain in relation to Gourley, which is Prater. And so we definitely don't need Pyrmont. Shall we kill Pyrmont?

**Saulius Grigaitis**  46:22

Is it known how much of nodes are outside of the client teams?

**Danny Ryan**  46:38

I don't know the node count. But I believe client teams control something like 70% of validators on Pyrmont. Does anybody have a better estimate on that? Yeah, we have made it clear that Pyrmont is to be killed and Prater to succeed it. And I believe that one of the biggest operators that was still using Pyrmont was rocket pool, doing a beta until about a month or two ago. And that was one of the things we were still waiting on. I considering that there is Prater and considering that we did do the diligence to make sure that the people that really needed it got what they needed out of it. I think that we can move on and kill it. And I can in a blog post Monday or Tuesday, just around the various things going on, I will mention that it is no longer supported. And that Prater exists. I think it's been mentioned before, I will reiterate again. Okay, is there any, I suppose, even if we don't want if we want to do turn off half nodes or something, we can actually just do that on the EF side. So if anyone is interested in doing that we can but maybe follow up with me and Pari otherwise, let it burn. Anything else on Prymont. Pari, you want to turn off half our nodes and see what happens? How many what percentage of node validators does the EF operate?

**Parithosh Jayanthi**  48:57

I think 30%?

**Danny Ryan**  49:01

So maybe we'll just leave, we'll just leave the EF running longer than others. By a couple of weeks.

49:08

We can still add on we did finality tests on Prymont already. We turned off I think three fourths of the network or something and then brought it back up and Prymont recovered. So at this point, it's already done those steps.

**Mehdi Zerouali**  49:27

Okay, we'll just exit our validators if that's okay.

**Danny Ryan**  49:32

Get ready for a long execute. Okay, then I don't given that I don't see much value in even doing a non-finality test. But if anyone is inspired and has 10% of network and wants to just run it into oblivion, and become the new king of Pyrmont then by all means. Okay, we move on, the next item that was brought up was the fork choice attacks. And, and for vulnerabilities, thus potential attacks and related fixes. I did blog about this the other day, to just provide some high level context and I will share that context here. These are serious attacks and they the the proposer boosting fix in particular has been well formerly analysed by a team at Stanford with rigorous liveness proofs and analysis of, given the proposer boost what an attacker and what various sizes can do. And that formal analysis will come out hopefully very soon, but our on understanding is that given the simplicity of the boosting fix, and the formal analysis available with it, but that is the best thing to do, especially prior to the merge. So that PR has been spec since April. Teku, I think is even implemented behind a feature flag. And our understanding, now is essentially that that is that is the best thing to merge, and get implemented prior to the merge. So given that, I believe that we'll do a final pass on that PR, make sure that there are test vectors released and get it out by the end of this month for an inclusion in clients as soon as possible, with the latest inclusion date being the merge fork. Any questions or thoughts on this one? And as Terence noted, this this provides better liveness and real resilience in some of these edge and attack scenarios, the core of the fork choice is the same. And when you don't have attacks, you literally agree with the old fork choice and the new. And when you do, the more that are on this new fork choice, the better resilience you have against this. So with respect to a main net release plan, once we do have implementations and once people have put this on, on testnets, then I would say starting February, people should just begin to roll it out. But we can touch base at the beginning of January. Make sure there's no standing questions with respect to implementation and test vectors and things.

# [Merge Interopt Updates](https://youtu.be/9U_xj_zCMYg?t=3180)

**Danny Ryan**  53:18

Okay moving on any discussions related to or research updates, spec discussions or anything else?

**Ansgar Dietrichs**  53:36

So this is mostly actually relevant for the execution side. But I was thinking maybe to briefly ask you as well. There's been some thoughts around how to handle like missed slots on the execution side, but from from a base fee. But if you so very much execution logic, and but why this could be relevant here is just that [there's a EIP that's been proposed](https://eips.ethereum.org/EIPS/eip-4396) that could be included as part of of the merge already to make some small changes there. And one of the motivations for it would be that it could actually reduce the impact of individual validators going offline. And specifically, there were some people that were concerned that with the normalisation of validators, they could become targets of targeted DOS attacks, just around the time they were, like it was would be their turn to produce blocks, and would be could be taken offline. And so the kind of doing this change, including this change could kind of reduce the incentive there. And so my question would just be just in case any, like ETH 2.0 client team has any thoughts around like how big of a problem targeted, like the minimization and DoS attacks could be expected to be, could be helpful to inform whether this is high priority enough to consider for the merge itself or not? To me, it always was a bit more of like a theoretical concern. But if anyone, any team happens to have like some further thoughts on this, that could be helpful. Otherwise, I would just assume that client teams also considered a smarter theoretical concern.

**Danny Ryan**  55:24

I wouldn't call it a fully theoretical concern. I think that targeted dos is is definitely a problem in that the, there's probably a wide range of anti dos capability depending on the operator, depending on the hobbyist, depending on the home or cloud infrastructure. And thus, I think dossing, the entire network is probably not realistic, but maybe dossing somewhat significant percentage is and so still having VM capacity, fully passing that I think is really valuable. I think there's also just the the chance of a 10% node operator being offline, for any number of reasons, is, is probably high over some period of time. And so, it's also nice to have in that EVM capacity wouldn't go down not event. That's my opinion. Maybe we'll discuss a bit more on Friday, but I think it's a really nice to have, I do think that it provides additional security resilience. I do think that if it doesn't go in Ethereum is probably fine.

**Ansgar Dietrichs**  56:43

Yeah, I think I generally agree with that assessment. I was just wondering could have been there was one client team or something had spent some time thinking about this specifically or something.

**Mehdi Zerouali**  56:55

Okay, do you mind linking the EIP please? (https://eips.ethereum.org/EIPS/eip-4396)

**Ansgar Dietrichs**  56:58

Oh, yeah, they focus very much on the execution side but it does this the DDoS concerns and the motivation so I linked it in the chat. Thanks. Thank you

**Danny Ryan**  57:09

Thank you. Other discussion points for today? Okay, if if we do have further conversation we'll take that to the merge interopt channel on Discord. Anything else for today? Okay, down with Pyrmont. Long live Kintsugi. Talk to y'all soon. Thank you.

## Next Meeting: Thursday 18th November 2:00PM UTC

## Attendees

Adrian Sutton
Alex Stokes
Ansgar Deitrichs
Ben Edgington
Carl Beekhuizen
Cayman Nava
Dankrad Feist
Danny Ryan
Diederik Loerakker (protolambda)
Enrico Del Fante
Fredrik
Hsiao-Wei Wang
Jacek Sieka
James He3
Leonardo Bautista
Mamy Ratsimbazafy
Marek Moraczyńsk
Marius Van Der Wijden
Matt Garnett (Lightclient)
Mehdi Zerouali
Mehdi Zerouali
Micah Zoltu
Micah Zoltu
Mikhail Kalinin
muddlebee(answesh)
Parithosh Jayanthi
Presotn Van Loon
Saulius Grigaitis
Terence Tsao
Tim Beiko
Vub
Zahoor Mohamed
