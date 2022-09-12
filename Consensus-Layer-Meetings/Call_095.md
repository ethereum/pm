# Consensus Layer Call 95

### Meeting Date/Time: Thursday 2022/8/11 at 14:00 UTC
### Meeting Duration: 1 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/618) 
### [Audio/Video of the meeting](https://youtu.be/ir-gnBm2GZ4) 
### Moderator: Danny Ryan
### Notes: Alen (Santhosh)


## Intro [3.29](https://youtu.be/ir-gnBm2GZ4?t=209)
**Danny**
* Welcome to the consensus layer. Call number 95, not number 99, which is what I had on the stream. 10 minutes ago, I had this issue 618 in the PM repo, and we have a few things on the agenda today. I do not believe this will be a terribly long call, but you never know. we'll go over anything merge related, go one thing there specifically, but can open up for discussion then research spec, et cetera, and open discussion closing remarks. on the merge front, before we get into the specific issue, are there any updates related to Testnet main net, or anything like that? Did we have a shadow fork? 

**Parithosh Jayanthi**
* Hey, yeah, we, the last time we had a shadow of work was last week, so that was mainnet shadow for 12. it went without a hitch, which is great news. We used, we used all the versions recommended by the EF doc post. I have seen that some client teams have updates after that version. And I think the blog post has been updated as well. So shadow fork 13 will be using the latest releases of our plans and it should be happening tomorrow. 

**Danny**
* Okay, cool. 

**Terence**
* Confirm that 13 is a, is the last one, right? Pari? 

**Parithosh Jayanthi**
* Yep.  shadow fork 13 will be the last inner shadow fork.

**Danny**
* Got it. I do. I do think, you know, we might consider maybe not testing the merge transition, but, you know, this being weekly being part of our build process or something as, as people of new clients, but I think that's probably a separate conversation. ultimate little Canary zone. Okay. Anything,  any questions about the shadow forks? Any other comments about Testnet or preparations for mainnet? 

**Parithosh Jayanthi**
* I just wanted to put it out there again. We will be deprecating, Ken after bellatrix fork happened successfully. So I'd I guess,  so we haven't heard anything about anyone using Ken for any sort of testing. So I'd like to officially deprecate maybe tomorrow. 

**Danny**
* That sounds good to me. Okay.  some other thumbs up from the chat. Okay. I do wanna plug at the start and we'll plug it at the end. There is a merge community call, just in case you're listening and you're gonna get bored and leave. there's a merge community call tomorrow, Trent, will actually, Trent, can you just give us the heads up on that right now for any of the listeners? 

**Trent**
* Sure. Yeah. You basically shared all the relevant information, but it's same time as the All coredev slot. So 1400 UTC, 10:00 AM Eastern,  and it'll be similar format to previous calls where we'll just go over the latest on Testnet,  things that have happened, any new information from clients or researchers, and just, yeah, basically have an open forum for,  validators to ask questions,  community members to,  bring up any concerns that they might have. but there's not much between, well, there's, there's really nothing between now and the merge, so it may not be that dense, but we welcome anybody to join, including researchers and client teams. 

**Danny**
* Great. Thank you, Trent. 

**Micah Zoltu**
* Not, not just for validators,  any user who runs a node,  feel free to stop in and ask questions. 

## opti-sync tests Add optimistic sync tests consensus-specs#2982 [7.39](https://youtu.be/ir-gnBm2GZ4?t=459)
**Danny**
* Sure. Yeah. Great. Okay. Let's Mikhail, you have an item here on the updates on optimistic sync tests. Can you bring us updates? 

**Mikhail**
* Yeah. Thanks, Danny. Yeah. So, so has been working on optimistic sync tests. basically this is an extension of the Fork choice test of the fork test format.  it's extended by adding a new payload info, which provides the, payload status,  the status that El client is returning,  once receiving the payload. So the idea,  when,  this payload is available,  the El mark,  that is used by test runner gets feed by this information and responds accordingly to the, to the test, to, to the information guest from, from the test. and yeah, that's how we can,  like, have a syncing payload. Then it turns out to be invalid.  we can test, latest, valid hash stuff and sophisticated scenarios with like multiple,  syncing, forks,  when all of them becomes invalid at some point. And,  yeah, and the test cl client behavior in the deterministic. we got initial feedback,  from,  client teams on implementing these tests. And one thing that,  has been discovered is that,  there is a valid flag on every,  block on this test format and was like a bit of, kind of a source of confusion, what to use, what's the right value for the valid flag. We seem to figure it this out.  everyone can take a look at the,  most recent comments,  on the, yeah, on the PR just dropped in the chat. So, yeah,  the, the problem with valid block is that what to do when,  the payroll is syncing, but it eventually becomes invalid.  so what's the right,  flag for,  what the right value for this valid block. We decided that's gonna be true because,  the valid block should always be true.  when on block doesn't return an error. And,  when the payload has been seen is syncing when the status is syncing, this is the case when unblock doesn't return error, unless the state transition fails other checks in the state transition. So please take a look. I think we can move this from work in progress to, like to actually the PR and yeah, I would, my, my preference is this to get merged like on the next, during next week probably. Yeah. Next week is the merge week. So yeah. Yeah. Just,  yeah, engage in everyone, every sale client team to take a look at this, it's gonna be hard,  test. See it soon. 

**Danny**
* Cool. Thank you. Mikhail for that. if you haven't taken a look,  please do, and there's also attached in the header comment, our,  some actual sample tests if you want to do an attempted integration, you can see if there's any other, issues that arise when you, when you do so. 

**Mikhail**
* Any questions about this issue Also to, yeah, one thing I, I missed this tests are optional kind of optional, so, yeah, but it's definitely added to have them implemented,  and supported by CL clients, but yeah, as optimistic sync is like an, a side thing to the main consensus facts. So,  we also try to make it like a side sync thing to the maintest suit. So fork choice tests  will not be affected by this change. 

**Danny**
* Great. Moving on other merge related discussion points for today, What is it happening? I don't know, is, is,  the Soth Sayer on the call? No. you know, I think we've been monitoring Bortel. We can share these links on YouTube. and I think the other alternative, which is something of a linear regression that looks over the past three weeks, I think the other interesting one, the other interesting algorithm is just the kind of naive algorithm looking at the latest head, the naive algorithm accelerated, and then slowed down Bortel kind of stayed relatively stable,  as hash rate fluctuated, looks like, you know, 14th, late UTC into early 15th, but who knows? I will say there's a lot of misinformation around the when merge website.  it seems like they're counting down to the difficulty bomb, which I don't really know what they're doing there, which then estimates the date of 13. And so I think a lot of people think this is happening on the 13th, but then if you look right below that they talk about TTD, which happens a day later. So,  do not be misinformed I'm by this website. Okay. Anything else merge related? Excellent. There is one other discussion point in the agenda today. This is also by Mamy. and this is related to a, PR in the beacon APIs on checkpoint sync. 

## checkpoint sync api Checkpoint Sync API beacon-APIs#226 [14.05](https://youtu.be/ir-gnBm2GZ4?t=845)

**Mamy**
* Yes.  we are planning a release,  currently for Nimbus that will be high,  importance,  with,  a couple of convenience,  fixes,  to tell,  users that they are well connected with the El client, for example,  or to avoid,  the warning on basu geth that,  you're not connected to numbers,  and also, an important performance fix. So you'll have all the details in the,  release notes,  and they should go in a couple of hours or tomorrow, early morning. 

**Danny**
* Got it. 

**Mikhail**
* Getting back to checkpoints in API.  there is a PR,  there is a discussion in the PR as well,  which is valuable,  to, to, to read. It gives more context and,  all, like, more and gives more details on this, proposal and on the general checkpoint sync stuff. yeah.  one thing before we go,  further is that there, there was a comment by Micah that if we have this API, it should exist.  it should, it should be run in a separate port, like a separate piece,  of the interface. I completely agree with this, but,  before we,  make this into this spec, I would first like to just know the general opinion on this API, whether we go into implement it as proposed, or not like the general feeling and,  what,  cl client developers do think on that. And,  related to like the feedback, that I'm trying to get here,  is that this API actually has basically two end points. And,  it means that clients that does not, it implies that clients that does not,  yeah. Are aren't capable of starting from aren't capable of being bootstrapped from just the state and requires some other stuff like,  block that is in the state, that is referenced in the state.  they will have to, be adopted for being able, being capable of starting from the state.  why I think so is because,  the purpose of these API is to keep it as,  much,  lean as possible,  to increase the adoption by state providers to get actually more state providers across the network, but to provide the state. And if we extend this by like one more or a couple of more endpoint,  this will, I think it will significantly diminish the purpose of the whole proposal. And,  as for me,  we bet to not accept it and, you know, just use the, regular, beacon API for strapping,  the notes. So, and that's like one of the things that I would like to figure out, before we move on with,  this proposal. So do do,  client about risking that it is possible for everyone to, and it is it's possible. And it is, it does make sense to, to start from, from the state. Is it like difficult to be implemented,  clients that are not yet supporting it? 

**Arnetheduck**
* I think I can speak to that for numbers at least. and I think the issue is basically that when you get a state without a block, you're kind of forced to connect to Lipi to P without having a block, which means bringing up the network before you have a database, basically, whereas with the block, you can already have like a full featured database, exactly the same as you have when you start from Genesis, because Genesis is unique in that you can generate the block from the, from the state. So it's not impossible. Of course it's inconvenient. 

**Mikhail**
* And, But Why, why do we need this block body at all? I mean, is it like a requirement on the P2P,  request stuff or whatever else? 

**Arnetheduck**
* It's not a strict requirement. It's more, that much of the logic is built upon the block being there. Although we can pull similar information from the stage from latest score Cutter. I think it's just a code organization,  matter, because we can assume that all non finalized blocks are available to the client when it's starting to validate incoming blocks of whatever kind, whether those be,  concept blocks or, you know, get blocked, get, beacon blocked by route requests and so on. And, there's actually a similar issue facing like clients, which is basically that,  clients that are snap syncing or that are checkpoint syncing this way. They probably shouldn't be connecting to gossip the same way, but they should be making requests from, you know, get blocked by route probably. and,  those, those are kind of front facing clients that don't like until they have downloaded that block and, and sort of fully initialize themselves, they're kind of Frankenstein clients. And I know that,  you know, it might be difficult to maintain connectivity while you're in this Frankenstein state because full clients will not know exactly what's going on with them. So, so it's certainly not impossible, but it's also a bit of work. 

**Mikhail**
* So it is more about like,  the inner logic of cl client, which requires the block to be there, not like the, some kind of hard requirement on the P2P a to be able to serve this block did Get I, 

**Arnetheduck**
* Yeah, I would call it the gray area of the peer to peer spec, the peer to peer spec doesn't really It only considers full nodes. Right. And there's a couple of other gray areas. So the spec explicitly says that you're in order to be a participating client, you have to serve blocks. But obviously when you're checkpoint syncing, you're not syncing block. You're not providing blocks for sync, which is also kind of a gray area in the spec. And we should probably address that at some point. 

**Danny**
* Are there other clients that also have this requirement that wanna make a case I've been, 

**Seananderson**
* Well, I'm not too familiar with the checkpoint sync lighthouse, but, from forking around a little bit, it looks like we do use the state and the block when we initialize it. So we might have a similar sort of requirement, 

**Danny**
* But I believe does, can lighthouse pull down a weeks of relativity state currently and start, or does they have to pull down both the state and a block? 

**Seananderson**
* I have to spend a little bit more time looking to answer that, but can add some feedback on the pull request to the beacon API repo.

**Danny**
* All right. Yeah, that'd be good. I do, I think some conformance here is moderately high value, sooner rather than later. So yeah, if you can, if you can do a little bit of diving and anyone else that is also unfamiliar with the exact requirements, but, to chime in, that'd be great. I certainly agree. you know, I've had a feeling, maybe this shouldn't be in the beacon APIs spec repo. I, but I, if it is to be actually specifying a separate port and thus like enabling being kind of a separate flag and, I think is the safe path. And I, I do think that that's a ni a better compromise than trying to put it in another repo, cuz it is an HTTP API on the beacon API on the beacon node. 

**Arnetheduck**
* I mean, the other thing that I thought about that PR was a balancing thing. Like if you're providing a state already,  first of all, we already have a URL for that. So having another URL for the exact same thing, isn't really strictly necessary, you can still have an API that offers, you know, the current URL on the new port. the other thing is that the state is massive, right? So offering blocks as well at that point feels like a minor minor thing. so if we're going to standardize an API for, checkpoint syncing in, in a way it feels like it's also useful to offer up blocks because that enables,  clients to actually download the blocks as well from,  from that checkpoint provider and thus not burdening the peer to peer network with, with that. And at that point I would also use like the standard block URL include that in the, you know, minimal block sync supporting port, 

**Danny**
* So state is only the state access is only, that's a debug namespace, right? 

**Arnetheduck**
* Yeah, I guess. 

**Mikhail**
* And yeah. Would it make sense if we like,  if the checkpoints in API would provide like a block and state in encoded, is it difficult to, to, to make this pair out of? I dunno. 

**Mamy**
* So everyone is cheating and providing state and block in practice. 

**Mikhail**
* You mean that we already have it? 

**Mamy**
* Yes. 

**Mikhail**
* Yeah. You mean that they provide in state and block and like one response. 

**Danny**
* Yeah. Is that bundled? 

**Arnetheduck**
* No, it's not bundled. 

**Mikhail**
* Yeah. Yeah. And we want this endpoint to,  to return and coded object. So if we would like to, you know, provide the block as well. So we can have this, a new type of container, which is basically very simple, probably that's the other way. I can.

**Arnetheduck**
* I mean, we already have an API that returns to block. This is the encoded as well. So making one or two requests, doesn't, it's a massive difference. 

**Mikhail**
* It doesn't make like a massive difference, but if you have an end point that,  there could be first there be a race racing issue when you're requesting the state. and then you're requesting the, the block, the finalized block. it will have to, yeah, it will have to, I don't know what if like this, this gets ruin by some provider.  so you are bit between the two requests that you are making. I, I would prefer this to be one request and if we want a blog on the state,  they should rather be,  responded in one. They should just be bundled together in the response. And these checkpoints in API could not only be implemented by clients,  and,  exposed as like a client, as, as a part of a client. But it could also be some, I don't know, very simple HTTP server that just, you know, exposes these binaries and these binaries are in updated by, by some client. So the client doesn't,  isn't available from outside of the internet, but this restricted HDP service is that that's the other way to, to, to be, to become a state provider. And yeah, in this case,  we, we would like to have as less information required to be exposed as it's possible. 

**Arnetheduck**
* Well, I will mention the alternative here, which is basically, we've talked to a couple of providers and they're actually open to serving a files as well, and a files contain exactly what you're saying, except that it's a full day of blocks instead of just one block and one state. so that's, that's kind of, that's a ball that's kind of rolling very slowly,  because we've been focusing on the merge, but nonetheless, it's, it's also out there as an alternative, 

**Mikhail**
* This, they can be exposed by this API as well. 

**Arnetheduck**
* Right.  I mean the information. Yeah.  Yeah. I mean, they're, they're just dumb files, right? So you just, you just run a static HTTP server, serving a directory, basically. and that's it, 

**Mamy**
* Or be Bittorrent, I've put an example, error server,  on the chat. 

**Danny**
* Thank you. Does Arnetheduck want to specify a PR that for the errors on the API? 

**Arnetheduck**
* Sure. It's actually a good time because I was just gathering my notes for that the other day. So I post there's a new post on these research linking to other relevant stuff. I can also put out an API beacon, an API spec, a consensus spec or something else. 

**Danny**
* Okay. I do think that we're probably at the, limit of making progress in this, on a live call. I do ask teams to chime in on this issue, as well as opening up that discussion of the air files.  you know, simplicity is nice, but if block is ultimately a blocker, I think adding another end pointer looking into bundling, isn't too crazy, but let's take it there. and if it's not decided by Devcon, we will have to hash it out in person. 

## Research Specification [31.18](https://youtu.be/ir-gnBm2GZ4?t=1878)
**Danny**
* Great. Let me find my agenda. It looks like anything else on just,  research specification, anything in that domain. 

**Lightclient**
* Can I ask what people are thinking about the various, UX PRs for improving the connectivity between El and CL? We, we currently have three proposals. If you haven't been watching there's one that sets a default location to put the JWT on the file system, then Yik, had an idea that we should just expose the engine API on off at,  or whenever it is bound to the local host because it's not accessible externally. And then Martin has also now proposed that, as an alternative to that, we still have it off whenever it's bound to local host, we just use a set key and his motivation for that is that that doesn't allow anything from the browser to call and potentially manipulate the engine API. So I'm curious if anyone has any thoughts or feels strongly about a certain direction 

**Danny**
* By the set key? it meaning it is predefined 

**Lightclient**
* Predefined. Why Does that it either be empty? All zeros? I think the rationale Martin gave is that in the browser, you can't set a header field like that. And so it's not possible to actually call the engine API. Whereas it's not clear if you can call out from a brow, someone like correct me if I'm wrong, it's not clear if you can call out from a browser and not have the origin header set. Cause my original proposal  proposal was to just in the El have the ability to block anything that's coming from an origin difference than what we're hosting the engine API on, but I'm not 100% certain it's possible in a browser to, ever to ever call out without origin. And so the simple thing is just to put a fixed key in and then it's just not possible at all. 

**Mikhail**
* You mean that fixed, defined,  default kind key that is known by every client. 

**Arnetheduck**
* I mean the fixed key option sounds good to me. It's easy to do. 

**Lightclient**
* Okay. Anybody against the fixed key option? 

**Danny**
* Yeah. I mean, if we want to go the local host path, just if we think that's a sufficient patch, that's sounds nice. 

**Lightclient**
* You're saying without the fixed key, 

**Danny**
* I'm saying if the fixed key is a sufficient patch for the browser, I'm not a post, Right? I do not have the ability to currently assess that. 

**Lightclient**
* Yeah. That's what I'm trying to understand as well, because I mean, it doesn't like I would rather not have a fixed key. Like it feels a little bit like a hack rather than a proper solution. but it As a hack, Fair enough. Okay. I I'll look into it a little bit more and I will, I I'll drop some actual PR and I'll post the, 

**Mikhail**
* I'm just curious how it'll informed and supported by else. So if you have a not so if you don't have,  sorry. So if you, if you change the, the IP address,  from which connections are expected, right? So you have to it'll create a JWT WT secret file as it currently is, if nothing is specified, then the default is like the local host IP or the local host name and yeah, this, this default key. Right? 

**Lightclient**
* Right. So if they pass the JWT CLI flag in, then we'll do things the same way. And if they don't pass it in, we'll use the fixed key when they're binding the,  the engine API on local host. 

**Mikhail**
* Cool. And,  on the CL side, it will just try to use if, if no key, if no JW secret is,  specified, it'll just use this fixed key, right? 

**Lightclient**
* Yeah. Default. And I'm wondering if maybe it would make sense, like even if a JWT key is passed to like try and fall back, if it's on local host to try the fixed key and throw like a warning or something, because right now, like suppose the user is only setting the JWT secret CLI flag for the cl. Now if they update their El client, it'll use the default key. And if they don't change the command line arguments for their cl, the cl will continue trying to access that old JWT and connect via. So that could be a consideration. 

**Danny**
* Okay. I do given there's many proposals, I do suggest maybe closing out some in favor of others, refining one and then circulating it, just to reduce, you know, if there's key people to look at some of the proposals before you close them. Absolutely. But just to reduce the overhead of getting a round of thumbs up, I think hone it on one. 

**Lightclient**
* Sounds good. 

## Closing remark [37.51](https://youtu.be/ir-gnBm2GZ4?t=2270)
**Danny**
* Thanks Matt. Anything else before closing remarks? Anything else? Technical. Okay.  Tim has a late comment into the issue, Tim. 

**Tim**
* Yes. so I, I posted about this on, on this discord yesterday and was curious to get kind of a sanity check from, from folks here. basically everybody's been working really hard on the merge for a really long time. and there's kind of some,  pressure building up to discuss, okay. What happens in Shanghai from here and how do we sort all that out? it feels like, you know, given that we're about to have the merge, there's DEFCON coming up soon. And I, it doesn't seem like people have like, spent a lot of time or had a lot of bandwidth to think through all the Shanghai stuff yet. it might make sense to like take a couple calls off,  so people can get a break,  recharge a bit and also take time in like a more async way to review all the different themes for Shanghai. And that we could,  you know, have a call start again shortly after Devcon. and you know, there were different like flavors of this. Some people said they really like having weekly calls and maybe we can do something that's like less formal in, in the party lounge or something like that. but generally curious what people think about taking, you know, three or four calls off,  once the mergers happen and we've had like a call or two to debrief, and maybe trying to set up a more async process to review the different things for, for Shanghai and three or four, meaning the sum total of consensus layer and all core dev. Yes. Correct. 

**Danny**
* So like a month total give or take, and that month includes Devcon, Which, you know, for the consensus layer calls, I think we would have the one on the 22nd, not that's right. Have the sixth and not have the 20th. So those are the weeks straddling Devcon. 

**Tim**
* Yeah. And then, yeah, I, I think for all core devs, we could probably skip the,  lemme look at the numbers here.  we would have the call on the 15th, assuming that the merge is not happening at the time, or we might have the merge on the call. We'll see, ABO would skip the one on the 29th of September.  and then we would probably also skip the one on the, on the 13th during Devcon. Yeah. And we'd start again, basically two, except to Devcon on the 27th And generally look at with Lucas's comments in R &D server. 

**Micah**
* Then I would rather just keep the pattern, keep things regular and consistent. 

**Arnetheduck**
* I don't mind because I'm going on vacation. Haha Right. 

**Danny**
* I mean, from a, from a practical standpoint on the consensus layer, I believe people will begin to be traveling on the sixth. Yeah. And I know a lot of people take the week off after Devcon those considerations. push me towards this Recording. 

**Tim**
* Yeah. Anyone else have strong opinions? Okay.  we, okay. So I guess, yeah. 

**Danny**
* I have heard some, you know, moderately not as strong, but lots of thumbs up, outside of this call, just to add that weight. 

**Tim**
* Yeah. And I guess O obviously this is like the CL call. So like, you know, if the idea of just like skipping the call before and after Devcon, makes sense to the group here, we can discuss, you know, what we do with all core devs next week on the core devs call. but yeah, and, and, and there will be no core devs call at Devcon. So it's like even just skipping those two cl calls plus All core devs at Devcon basically gives you like a three week gap between, between the calls. 

**Danny**
* So Cool. Thanks Tim. 

**Tim**
* Sweet. 

**Danny**
* Okay. Anything else for today? Anything else on this call before the merge? Cool. Okay. Well, happy merge everyone. Talk to you all soon. 

---

### Attendees
* Marius Van Der Wijden
* Danny Ryan
* Mikhail Kalinin
* Stefan Bratanov
* Chris Hager
* Sean Anderson
* Pooja Ranjan
* Saulius Grigaitis
* Terence (Prysmatic Labs)
* Enrico Del Fante
* Paul Hauner
* Thegostep
* Phil Ngo
* Ben Edgington
* Carl Beek
* Hsiao- Wei Wang
* Trenton Van Epps
* Dustin
* Caspar Schwarz-Schill…
* Gajinder lodestar
* Lion Dapplion
* Andrew Ashikhmin
* Fredrik
* Mamy
* Micah Zoltu
* Pari
* Stokes
* Cayman Nava
* Mario Vega
* Arnetheduck
* elopio
* Dankrad Feist
* Viktor
* Preston Van Loon
* James He
* Marek Moraczynski
* Saulius
