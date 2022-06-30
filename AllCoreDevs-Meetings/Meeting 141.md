# All core devs meeting 141 notes

### June 24, 2022, 14:00 UTC
### Duration: 90 minutes
### Youtube Stream: https://youtu.be/qu5idP-JLyQ
### Zoom: shared on #allcoredevs Discord server shortly before the call
### Notes by Darkfire_rain

# Gray glacier updates

**Tim beiko:**[cool](https://www.youtube.com/watch?v=qu5idP-JLyQ&t=0) are we live. Okay i'll assume we are so good morning everyone thanks for coming to all core devs number 141 and a couple things on the agenda today. First, just set up on Greg glacier which is happening next week, then a bunch of merge related stuff then like prime had a small issue around the debug namespace you wanted that to get feedback on. And then finally. Paul from light house here has has made a suggestion for changing the day that we have these calls on to be more friendly towards the parts of the world where it ends up being Friday night or Saturday morning, so we can chat about that at the end, there are two eips that  we've been dumping from call to call to discuss and never had time for them, but then one of the champions has some issues that they're looking into for EIP 5027 and then for EIP 4444. There is also like an update that was posted on the github there, so we can discuss both of those on the next call but it folks on it check it out a sink in the next two weeks so at least we have the context when we're when we're talking about that.  First yeah so Greg glacier happening next week it's expected around July sorry June 29 and there's a blog post, with all the client releases out In them if you haven't upgraded your node now is the time to do it, I don't know if there's any client team who wanted to chime in about the upgrade.

# Merge

**Tim beiko:** Okay. So yeah did you notice that, and next up moving to the merge stuff we had our seventh main that's shadow for earlier this week, Perry, do you want to give a quick overview of just generally how the fork Web. And then I noticed like basically and nevermind had some stuff they are sorry basically and Aragon, I had some stuff that they wanted to go over as well, but I do want to walk us through the high level of the forklift.

**pari:** [yep](https://www.youtube.com/watch?v=qu5idP-JLyQ&t=206) so we hit.The chain was launched, I think, last week, on Friday, or so.**pari:**And we hit gtd around Wednesday after an override like a D earlier. We hit an ad a couple hours later, which I guess is a sign that it is changing even drastically within like a span of a day. But irrespective really hit add, and we will finalize for a while, I think we immediately drop down to around 80 ish percent so about a 20% drop off on nodes. And over the span of the next 12 hours a lot more nodes dropped offline. Later we figured out that most of the notes that dropped out were for either Aragon or baseball nodes. As far as I know, the Aragon issue isn't really an issue, but rather something related to how they shadow what they're looking for a blog but essentially don't have PR who's providing the block to them so they get stuck. There was a I think that enabled the experimental overlay and there was an issue with each stats that are enabled on the config. So I removed, both those flags and, since then, Aragon is progressing, I think we saw like two or 3% come back online. Hopefully motors come up online soon. The best issue, however, is a deep one and let someone from the better team talk about that.

**Justin Florentine:** [yeah](https://www.youtube.com/watch?v=qu5idP-JLyQ&t=294) I can take down this is. Justin from the basics, if you already go now.

**pari:** This one second This is one more time yeah i've updated the same tracker we have for checking for proposing empty slots. I don't have any data from.This Oh, of course, but from the other ones, the only combination that proposes an empty slot so without transactions would be numbers Aragon so we're doing. pretty much as well or slightly better than what we did with ropsten that would mean there's no real compatibility right now but there's no regression, at least.

**Tim Beiko:** [Nice](https://www.youtube.com/watch?v=qu5idP-JLyQ&t=340). yeah I don't know, maybe yeah thanks thanks very. Maybe anyone from Aragon wants to go over to the Pier in one. Before if this is like a bit simpler and then we can begin to base you in more detail.

**Andrew Ashikhmin:** [yeah](https://www.youtube.com/watch?v=qu5idP-JLyQ&t=363) I can briefly describe the issue, the issue is not. per se, with the marriage, but where the shadow forks is. Because we have kind of we don't have a network split, so we have peers from the shadow peers and upstream, vanilla mainstream theorists and. Occasionally we don't have enough PS from the shadow for so we can not download block borders or something like that and Aragon and become stuck but I don't want to spend too much time because this shadow for testing as a bit artificial it shouldn't happen. On real person that's already on real main main that.

**pari:** [We](https://www.youtube.com/watch?v=qu5idP-JLyQ&t=416) did get me and. So we just did a small slab update we just added static fields and that pretty much all the issue.

**Time beiko:** [Right](https://www.youtube.com/watch?v=qu5idP-JLyQ&t=421) did like for future shadow forks. Is it like straightforward to just we could literally peer all the shadow 4k nodes together right like that we run.


**pari:** yeah, I think, from next time on what I just use static fields that might just be easier.

**Time beiko:** cool anything else on the Aragon side.


**Time beiko:** Okay i'm just didn't do you want to walk us through what's happening on basic.

**Justin Florentine:** [Okay,](https://www.youtube.com/watch?v=qu5idP-JLyQ&t=500) so with regard to mean that shadow work seven we saw a long running issue that the team has been tracking get dramatically exacerbated. i've attached a hack into right up that goes into much more detail to the agenda in the comments there feel free to read that and send any comments my or anyone on the team slack. But the nature of it is has to do with our bonds I storage system and the concurrency issue that we found in it. In the past, this has been fairly rare and we've never seen it actually hit all the nodes at the same time around the merge like happened on on shut up work so. We don't think this has merged with it we still maintain that this is a concurrency issue in bonsai and we have been working this issue pretty rigorously, since it first showed up in late April.  We made a lot of progress on it. And we do have some ways to reproduce it now that we've got better hive test adoption. The fallout, though, was basically made up 25% of the network and all the basic nodes failed so we started to fail finalization. Participation dropped there wasn't enough to keep maintaining we did continue to propose blocks, but all the blocks are empty so that's not terribly useful. So this is an issue we are tracking it, we have made it we haven't managed to make it worse, which we actually like because it makes it easier to reproduce I think you all can appreciate how hard concurrency issues are to reproduce and analyze. We are continued to working it come to work it and if there's any need for greater detail i'm happy to elaborate and I hope everybody can get to the hat can be on the on subject.

**Tim beiko:** Thanks, and I have a quick question I know. I think bonsai trees is like the default storage mode now if if that's right but I assume that non bonds I storage still is supported in basically is that is that.

**Justin Florentine:** Correct Yes it for us to still support it is actually still the default bonds.

**Tim beiko:** forces the default.

**Justin Florentine:** Yes, bonds, is no longer experimental However, it is not the default.

**Time beiko:** [Okay](https://www.youtube.com/watch?v=qu5idP-JLyQ&t=500), and I assume just because, like bonds is is is smaller from a disk size perspective that's all we've been using for for shuttle forks but. Correct yeah and so, if. yeah I guess a quick fix there, and this might be hard for like main net but it's like using are actually no because it is the sink, but like yeah I guess a good tricks is, we can just use the non bonds, I noticed on the bases sided and see if those.If those work smoothly.

**Justin Florentine:** Yes, we'd like to suggest next time we do a mix of forest and bonds I notes for the next shadow for yeah. yeah we've also discovered that this is more exacerbated when running and docker are canaries that we run don't run in docker and be. very, very rarely see this issue, we do see it, it does happen outside of docker docker does seem to exacerbate it which kind of led some credence to you know timing and concurrency issues.

**Time beiko:** Right. Okay anyone have thoughts questions on this. Okay, so it's encouraging it seems like the two big issues we hit our like client issues but not motivated issues so that's that's good that's progress anything else about the shadow fork in general.

**Marcin Sobczak:** I would like to add that there was another my notes and all of them was successful on transition. And right now I are still healthy, but on to we have three exception like both nodes with tech who are down, for now, and investigating what's going on.

**Time beiko:** OK so. The nethermind take who pair is having issues.

**Marcin Sobczak:** I guess, but he was like.day or even modern day after transition.

**Łukasz Rozmej:** That i'm working on. Somewhat related fix so this might get fixed by this, but we are not entirely sure if this is the root cause.

**Tim beiko:** got it. Okay and I know there were a couple other merge like related topics around like latest added hash and sink that we wanted to chat about, so I think it probably makes sense to get through those before we start talking about like the next shadow forks are supposed to. yeah just to make sure we're all kind of on the same page. But yeah. Anything else if we change.

**pari:** yeah and I have another update. But this time regarding ropsten. So, Sam from the devops team unfortunately isn't Australia and couldn't make it to the call, but he wrote a really nice write up have to share it in chat right now. about the automated tests that we have that he ran on robson all the Code and the repo and shuts everything is open source, so people can reproduce it if they want. Essentially, he thinks up the head on robson on every combination, then he runs complexity tests, for example, stop the year for one up and then he stopped he. stopped the car for one he probably start the year or do it the other way around, or policing year and then such and assessing conceal and so on. yeah, the results are there and I think some tests, need to be villain but essentially it is synced ahead tests middle the results that the staple guys found as well and, as far as I know, those already have open issues.

**Tim beiko:** Nice. Anyone have questions comments on that.

**Łukasz Rozmej:** yeah I have one so are those tests like available to be rerun are being run somewhat like high stress or something that's because we are still working on that code and you'd like to be, it would be great to have some kind of test to potentially a spot regressions.

**pari:** exactly they are. Let me just link to the repository it's just a github actions things, similar to the matrix and you can make a PR over there it's whatever you want to change, and it should be reflected. So we have a sync test coordinator and then it triggers off the sync tests by a good batch and then the result of the sink test is also viewable on the action, but I thought it's easier to give an overview with the team. In case you guys have any questions about the setup piece reach out to Sam is on Twitter and discord and I can connect you if you need to.

**MariusVanDerWijden:** I also rent my own robson sync test today and what really stood out was that. I ran lighthouse gas and lighthouse took 15 minutes to sing. For. I think three weeks worth worth of Blocks now and get took. Like 15 or 10 minutes. And so, like the consensus layer sink is way slower. than the execution layer sync just something to keep in mind.

**Paul Hauner:** I think the last thing cuz some a bit of improvements do as well we're adding some concurrency and sounds do some benchmarking about how fast we can sync with emerge. I think in general consensus think is not an execution, I think, but. The checkpoint sink is kind of what we need so it's not hasn't been a huge target to improve sinking states and the consensus layer

**MariusVanDerWijden:** How how long, would you expect the.The checkpoint sync to like. How long do we need to sync with a checkpoints in like two weeks or three weeks or how.

**Paul Hauner:** We can usually do it, since the last analogy certainly have to sync you know, like 6400 bucks or something like that I think tech ooh and lighthouse we'll do a checkpoint sink in less than a minute around about a minute.

**Péter Szilágyi:** yeah but I guess, for you know one thing you need to manually.

**Paul Hauner:** yeah you can also point to like another they can note endpoint and they can pull it down so you can use like a centralized repository you can use another node that you have. check, I think, is is a requirement for proof of stake sinking basically. It for it for any any period off the genesis of a matter of weeks.

**Péter Szilágyi:** Well, I guess, the idea that somebody could pose a checkpoint every my association with Jeff bornstein will be that you put in a checkpoint and then you just use that for the next three months or five months or six months and then eventually just choose another one, but. I mean it takes super long to synchronize even from a two three week or checkpoint and I get to get annoying to always have to go somewhere infection, the most I can imagine, most people will just. configure their nose to just looking for on BLU Ray which can be.

**Paul Hauner:** baking in like three months, six months checkpoint state isn't how it's gone with the consensus clients, has been able to talk around it i'm not sure if you want to discuss it now, but that's that's not the way it's going.

**Paul Hauner:** yeah maybe this is a good one to discord or something like that.

**Péter Szilágyi:** yeah I think i'm Irish just want to bring it up because there's this big discrepancy and. Essentially, the the experience that people would have people going through menopause currently is that synchronization could become even catching up with becomes or so and would be nice to at least. know too much load on top.

**Paul Hauner:** yeah I agree definitely be better to to make it faster. I think the the staking Community a pretty familiar and comfortable with checkpoint sync as well.

**Micah Zoltu:** yeah and only problem with validator stickers right, this is the problem with for anyone.

**Paul Hauner:** yeah that's right, I guess, the point I was trying to make that was that people who are used to running bacon so people who.Even people who have decided that running big note seem to seem to get stay with check wasting pretty well that definitely not i'm saying we don't we couldn't benefit from. Improving because that's the slicing spades.

**Time beiko:** yeah. yeah I don't think we're gonna we're gonna improve the full six Speck on the seals right now but i'm definitely something something people should be aware of. And I guess yeah we can continue to sharpen the discord. either in the consensus Dev channels or awkward of. Just to take a quick step back any thing else marius you wanted to share from just the sig best you've been doing.

**MariusVanDerWijden:** No, it was oh yeah but you for. Much happened we I think we're getting. Much exactly 50 slots per second and after the merge hit. I synced with 30 slots per second so. This is the like the. engineer payload and purchase updated. So yeah that's the footsie with. blocks.

**Time beiko:** thanks and Andrew I see you've had your hand up for quite a while so.

**Andrew Ashikhmin:** yeah so about check when sync do we have inferior for option, because to my mind it's very important to check. to test the checkpoint Sim because for for the main net it's pretty much. A must, so we should definitely test it more on robson and other test nets and, to my mind, it should be the default for for like all public test sets you can opt out, but by default jackman sinker should be 1.2 inferior or something that that's my thinking.


**Paul Hauner:** yeah so it's been pretty hairy putting ensure and as a default that's why we struggle to put any default checkpoint sington i'm not sure if, as if you're or a beacon an API provider for robson make my guess is no, but I could be wrong.

**Péter Szilágyi:** I mean just. Just mentioning that for us probably makes sense to just wanted a name for not care because there have been ideas, it should be as pleasant experience as possible but, for me, I think it would be a very bad idea, very bad public view to just point.


**Time beiko:** So. yeah and and. i'm not sure that there is a whether it's in for or like another that there is like API provider for drops then became chain, obviously, like a bunch of the support drops in at the La or. yeah and I also feel pretty strongly that like whatever decision on that front that much more like a client level decision than like protocol level decision. So you know you could imagine lighthouse using it for and prism using alchemy, and like Members not using anything you're like using something that they maintain so. yeah I feel like this is probably. it's not something I don't think we have the like checkpoints to do but also if.yeah if we do it feels like. enshrining any single provider. At like a protocol level spec feels feels quite wrong, but then clients obviously free to do whatever they want in terms of like improving the ux for their users and yeah.

**Paul Hauner:** Just gonna say it's potentially an interesting point that we might not we might be under testing checkpoint sink on these tests and from a I meant many interested in it from an. Execution layer perspective just execution ID gives it kind of looked like your consensus layer just comes online. Say like in the last like say 128 slots of the chain and just start sending you payloads from there and then syncs to the head and then just wait for you to catch up. So maybe something to think about is trying to make sure that we test checkpoint seek a bit more with non execution consensus, I have clients, I know that lighthouses is not something we really thought about before Maybe someone else has.

**Péter Szilágyi:** So that's. Essentially, the preferred way to synchronize and guess though just give us the head as soon as possible, and we will figure out the rest. So for for gather these execution wise and the later heather you can give us the better we don't care if they are gaps I don't care about beginning of the changes can be the head.

**Łukasz Rozmej:** Yes, similar for another mind.

**Péter Szilágyi:** So I think that's kind of layers who can. Work corpsing fasting or whatever, in order to do that, they need. A header or something as close as possible, so that's kind of the expectation.

**Mikhail kalinin:** Probably we should just be more attention more users attention to us in the checkpoint sank in the documentation or the other places.

**Péter Szilágyi:** 20th or that users don't want to use it, I think it's more like being no idea how to use it, or what the point is that, so if we could somehow make that obvious or some helpful to me go along.

**Łukasz Rozmej:** kenton checkpoint be like download through peer to peer like wise it's like you have to point it somewhere I don't understand that this is.

**Péter Szilágyi:** The point of templates that you provided.

**Paul Hauner:** yeah so how it works in sense clients now is that they go and query a beacon note API so the standard http API on beacon notes and then they get. I think most of them will get like the array get the finalized checkpoint and then get a State download a full bacon say, which is order of 100 Meg and then it became block and then they'll start sinking forward from that. The reason the idea behind it is supposed to be like it from a source that you trust so like your friend or something like that how that turns out, and in reality is slightly different but. The reason that we haven't done it over the p2p network is for two reasons, one, because if you get eclipse at the start. Like when you first bring you and have a great setup fee is, and if you get eclipse then to start from a bad place, and you can never really correct from that. And then second is because it's just transferring that lodge state over the B2B network has been been a bit of a challenge and we haven't really got to it will think quite a need for it.


**Łukasz Rozmej:** So actually nevermind we have similar idea that we can optimize some things around this in terms of sinking and we actually bacon that hash. into our conflicts on every release and but released fairly often like every two three weeks so yeah.that's how we handle similar thing we're just bacon for every sports network.

**Paul Hauner:** That has also been discussing consensus land, but it just hasn't. sentence lelay I mean it just hasn't happened that way might be a good kind of discord conversation.

**Andrew Ashikhmin:** yeah because otherwise for main that it will be prohibitive this slow like I strongly think that for the main next checkpoint sinks, should be the default like whatever is used in fewer becton passes or whatnot, but it should be the default.

**Łukasz Rozmej:** For you have a debate then then even the user wouldn't specify something new, or you will have a fallback right.

**Péter Szilágyi:** I think, making a checkpoint thing is perfectly valid and we get has been doing that, since forever for the lifetime. Since you whenever the assumption is that whenever somebody downloads a new client, I mean they are trusting us, I mean we are handling their keys they everything, so if they don't crack the code down why even right. So the cost is there and the code can actually ship something. reasonably new, the only downside is that it's kind of a pain in the ass to update these checkpoints every two weeks when we do a release and and also, if you have a. lot of people what they do is that they upgrade get funders hard fork and then they don't touch it on to the next part for. Which means that it might maybe there are six 812 months passed in between, so if you try to use the five month old client to sync with an old checkpoint and it's going to be hurtful so you know for this developer constituent points to work people kind of need to run the latest code. At this fundraising.And I still think pointing the bigger guys doing horrible idea that's going to backfire.

**Łukasz Rozmej:** So, like I said I will do it this way that I would take in some. defaults at the point of release and allow people to overwrite it course with something you're.

**Péter Szilágyi:** yeah that seems the same question.

**Tim beiko:** Okay anything you are on checkpoints. Okay, but yeah obviously we can continue this in the discord and yeah encourage people to check out the documents that terrance link to the chat where Danny has gone through also some of the different approaches. Next up mikhail you wanted to go over some issues around latest valid hash and you want to give a bit of context on that.


**Mikhail kalinin:** yeah. So latest well attached, we have been discussed it like a while ago, and apparently there are some difficulties in support in it, at least from what i've heard, at least in gas. And yeah I just what I think it makes sense to start from like somebody from I guess explaining what's the difficult says they have to support it, this this data and this back and then just.


**Péter Szilágyi:** I think just. Just make sure that we're on the same page, the idea is that when. I don't know new payload or South fork first update the idea is is that states that we should, if the beacon client. tries to push us content inbound chain, for example, gap nodes mind for really long in value chain and and that sort of nevermind client tries to feed that to the mental mind. Execution layer that the expectation is that the execution client starts processing this long side chain and then halfway through where it hits an invalid state transition it just stops and returns that okay block 500 out of the 10,000 is invalid. This is the theory now the practice is the problem is that this new payload or fortress update, we are expected to return instantaneously to, for example, be returned and Okay, we don't have this chain yet so we returned sinking. that's why some of all, we have a 10,000 long chain which halfway through is broken, so we say okay thinking, but by the time we discovered at the top is broken, we already have, like the bigger clients so We only know that block 500 was broken. And then let's say one minute later the beacon client says that hey here's a previously it gave us a have to block 10,000, and now it gives us new block have 10,001. But again, we have absolutely no idea what the stock 10,001 is so we need to start a synchronization of. The me to go back all the way back and then eventually we will reach the same decision that okay like 500 was bad. But again, we have to reply much earlier, so we never have the response available to tell the be become client that a block 5000 blocks ago was invalid so every time we figure out that there was a bad luck as blocks ago it's already too late to to tell this. To the beacon client and the only way we could work around this would be to maintain entire chain or set of bad locks and, for example, when I.  The beacon client tells us hey here's 10,000 locks and the 500 is bad, then I will need to start tracking everything from 500 upwards thousand. As bad luck and then whenever I get a new fortress of data somehow need to link it into check it there's there was this in this set of bad locks the parent is present there.If you're sending to somehow figure out, which was the origin of the bad locks and, in general, it just gets a bit messy to maintain a big pool of bad things because. If the client works perfectly everything is nice if there's, for example, a database, or something in the client, then you could end up with simply blacklisting the colonic crushing the food chain, because, and if this actually happened at one point we can get. Three four years ago, the snapshots had the bug and very rarely. A block was rejected, for whatever data is, but if you try to import it a second time he succeeded so nobody really. notice it, I mean we got issue report that sometimes you got bad blocks, but the network didn't care because i'm just continued. But where we so if we had a bad lock blacklisting within the client implemented. That actually every single time one of those clients had this bakeries issue, it is a terrorist issue, they would have just dropped off the network essentially gradually order those dropping off the lateral they will blacklist dimension, and this is our. are concerned and it's not trivial to maintain it and track it and anything that if something goes wrong, it can have really, really bad consequences and, for example. This is the primary reason why gap does not have any form of reputation management doesn't have any form of bad block tracking penalties nothing the likes and just a another storing. Probably not many people here were President during the experience Olympic desktop works, but at that point. get these have blacklisting every reputation management and everything on the network and at some point the entire network just fell apart into thousands of side chains. and eventually every single guest was on its own little side chain, because there was some bug in the bad luck tracking and every every little black dress that pretty much everybody else on the network so every minor was just minding their own little chain. It was that it was a horrible show and in the end, the solution will actually could just remove all the blacklisting and just try to be as robust as possible to bad things and try to reject bad stuff as fast as possible but but not track it beyond processing. very long. background.

**Mikhail kalinin:** So the risk is if we have this blacklist, and in particular same gap, so the risk is to just mess up with it to have a bug in it and. probably say that something like on the value chain is actually invalid say this to cl client that makes its own decision support, I mean do they get it right from your description. So he so.

**Péter Szilágyi:** pretty much two things, one of them is tracking the the bad blocks or bad change is very expensive we if we do it in I mean we could do it in memory. i'm not sure what how valuable, that is, or not, if we have to touch the disconnect becomes super messy and ugly and since tracking, it is not necessarily super obvious. Any mess up can have.

**Mikhail kalinin:** Really catastrophic consequences.

**Péter Szilágyi:** And the question is what's the point, why Why is so important to be able to say that when you give me a lot I should be able to respond that 5000 blocks ago the chain was bad.

** Mikhail kalinin:** yeah that's that's like another question yeah but for. answering this question. One thing I was just my naive thoughts was OK, so the client has if the client has all this like data it's been fed by cl. ** Mikhail kalinin:**And it follows eventually and validating and encounters an invalid block in the middle of the chain. Right but it knows what the deep of this invalid chain is and yeah the naive implementation that i've been thinking about is like Okay, so we found we encounter a bad block. Then we take this bad block asked the downloader or whatever component is responsible for tracking the not yet seen but sinking in progress chain. From the tip of this chain and okay store the steep and these bad block like again have a map and just in memory just in kind of in memory cache knots not persistent it to disk and then, when next time the cl sandy and sandy sends you paid off. check that the parents hash and the actually the block hash are not in this like invalid cash right so, and if it's an invite if it is in this cache of invalid tips like off deep something valid chains then respond back with. This information with the status invalid and also add this latest spell it hash which can be. stored in discussion as well, so that was like naive approach me thinking on it.

**Péter Szilágyi:** So one issue with that Ryan approaches that what happens if. For example. He you give me a head and for me to discover that there's a bad blocking taking 10 minutes because they have the same from genesis and then I actually discovered there's a bad thing on the blacklist your tip, so to say, but there are already 530 5000 maybe. 200 new blocks on top so next time you give me a photo someday it's going to be.There so essentially there will be something in certain cases that could be gaps between the stuff that you give me so me blacklisting the tip is not enough, because it won't. The parent might not be in the steps up So yes, when the download or start processing the downloadable seven also has to be aware of this blacklist and constantly cross check blocks against this blacklist and that's exactly how they.
**Péter Szilágyi:** can apply that was the exact implementation we had there.

**Mikhail kalinin:** yeah yes right and yeah the assumption for this implementation work is that cl will be sequential in what it gives to El if if there is a gap, there is no way to. like to link this to feel this get applied to respond back correctly, so that was just kind of assumption, and we assume that basically cl always sequential almost always eventual course there could be failures. But if there is a failure, so it will just start sinking again with this chain right yeah will encounter this. bad luck, once again, and like second time we assume that cl. Previously yeah. yeah so you just should converge at some point.

**Péter Szilágyi:** So the. In the catch there is that there's a so you have I mean that's the other. thing and then run the cl analysis and you had was the execution is sinking, how do you handle that you just moved in you had to just update sink to the new I mean that's what kept us, I had no idea what what other clients do so it's. it's not super obvious and that that's a very specific implementation detail and relying on all these different foundation details.Is a bit going fishing is a bit far. I guess, my question is so at the end of the day, everything is solvable and the question is how much pain, it is and how why we needed so. If there is some super strong reason why we must do it, then, is, I mean you probably can't figure something out that we feel comfortable with maybe won't be super robust, but something that we kind of can sleep well at night with.But it would be nice to know why it's so essential.

**Mikhail kalinin:** yeah yes and yeah that's that's the like I think at the essence of this discussion Okay, so why it's why it's important so. There is a risk, there is an attack vector. Basically, the risk of this attack vector is is actually very low it comes in the very, very particular network conditions when see. network is not finalized in for some period of time and adversary has a portion of my own State certain portion steak. or there is a bug in the fourth choice or both, or whatever, so there are some where where a particular conditions in which, if email clients did not respond and not support this latest valid hash as per the spec currently the whole network. Like the whole all the data nodes let's suppose that. Neither El is supporting this correctly right so it's always returns thinking.vIf cl sense keep keep following this invalid chain so. And if all the data in there will be forced into the fork where the reason invalid block somewhere in the middle, we get the network. The network of validators that are in never ending sinking look, and this is a kind of like whiteness baylor that will require manual integration with intervention to get recover its problem.But once again, it comes with like where where a particular network conditions it's like not something that should happen ever on the main map, but still, so my intention and why, like. Like my intention of having this implemented across all the clients, is that we just you know remove this vector from the table and don't care about it. So that's that that's that's the reason why we should why why we have to support why we must support this. Like I will not like go in the details and the weeds of this like that at that concert, or like and conditions, but we can do this, I mean I don't want to spend time here like discussing we can do this offline in this court or anywhere else.

**Time beiko:** Lucas was here sorry Lucas has had his hand up for like. 10 minutes was this related to this and yeah. yeah okay.

**Łukasz Rozmej:** So oh. I just want to say that we implemented this nevermind I think we still have some bug or two when when the syncs with the sink scenarios so don't don't treat it as a spinal or production ready or anything but we definitely do something like kyle explain that we have a very simple. cash in memory, I think, currently it's 512 when we just keep a hash of the block and last valid hash for the block if there is a detected that it's wrong so when we think when we are thinking. Of when we detect invalid block we go for all the. The sentence of the block. And mark them. With that last bullet hash, so we are keeping that tips of the chain mark if it's longer than than our cash you're keeping the tips of the trademark not just wanted, but like potentially up to 512. blocks in that tip which we considered good enough. So when the new one comes build up on this on this one of those blocks, we will be able to respond with cash, so if the consensus layer is a sequential enough. We will have eventual consistency here that we will be able to respond with cash but. yeah that's that's how it's being been built. The one big potential issue is with state thing if we state thing. The problem was with the State in terms of why the block is bad, like the state routes doesn't matter, the state, we want in some of previous blocks, we we want to catch that that's I think beyond the. scenario in mind that we cannot really detect in the vault hash with state sync with snap single us. yeah but I mean that's that's kind of the limitation of. You start, so the assumption is that when you finish the first initial thing then the had locked was that the was valid, yes it that doesn't hold on I mean all bets are off and you're on the wrong chin and therefore coming back. But with these initial things that you it's easier to only once, when you start up your know the number again so it's extremely hard to.  back it because somebody needs to be listening exactly at the correct time and on the correct network prepared with the exact attack vector just tailor made for that specific chain condition so it's extremely unlikely. 

**Mikhail kalinin:** And yeah this this like risk of this attack is only this kind of attack makes sense only on foolish intense online notes so it's definitely what we would like to prevent is only related to the blocks in when we when the client is executing blocks, not the state sink.

**Péter Szilágyi:** What happens so. let's say. You feed me an invalid chain, I remember that  this chain was invalid and the last valid block was 5000 blocks ago the next time when I when you tell me to importance child, I will tell you that Okay, the last. I mean types of Blocks ago we got a bad law. What would what would be the reaction of the concerns client and specifically more interestingly, what would happen if I would have a respect that once I returned that. This change is invalid, I will actually forcefully forget that it's invalid, so if you try to read it to me the third time. I will again do the processing for the fourth time every report symbolic for the fifth time I will again the processing for the sixth time I will report it's invalid. Then it will be I would tell the execution client sorry the concerns clients if I if I. consecutively twice in the same issue, I can actually tell it to that okay if i'm getting the same issue. But I would actually give myself the chance of reprocessing it and maybe getting out of some weird data so some weird scenario, so will the concerns client show consumption behavior on.

**Mikhail kalinin:** So, because it's quiet will. remove this chain from certain frame this blog from from the book choice, I guess, and from from the. disk if it was persisted and while we work to the other chain which is valid. that's the expected behavior I don't know if, like. In the next time when I think its implementation dependent. But asked to consist their client developers if this same chain will be given like once again to only consists, there will, will follow will be consistent client start following this chain and do the same actually. I mean like encounter the same yeah but I guess what what happens in this case is that. Execution their clients will really have a State right and. yeah and if the same block is given, once again, then it will just be invalidated instantly.

**Paul Hauner:** lighthouse we would.  If the Al told us that it was invalid, we remember that it's invalid, we read on mark that entire chain is invalid and we wouldn't try to apply anything to it again. And anytime that we were told that if we were told, then, again, that it was actually valid we'd log an error, saying that you know you told us it was invalid, but it's actually valid now so there's a consensus fault.

loescaped from that stage, I think.

**Łukasz Rozmej:** Peter and catch what you're saying, but we are not, for example, blacklisting knows that this thing logs that we kind of failed on the validation or processing of validating the state route to do think this is recoverable in any way that I can see those recoverable.

**Péter Szilágyi:** No that's actually happening again, so that, as I said about four years ago, there was a gap where there was some I think it might have been to the father pruning in memory from the more I mean not in a snapshot there was a point when a. Essentially, is very, very rarely a block would get rejected because something else was also mutating the trial touching the try and if you try to reinforce the same block, then he succeeded, I think it was a lot processing. concurrently with pending block execution. So there was this weird scenario where to execution running at the same time. and corrupted the try.

**Tim beiko:** But if you actually.

**Péter Szilágyi:** tried to be important block it succeeded because it was super rare for that to happen.

**Łukasz Rozmej:** OK OK that's fine it's scenario for a bug I fixed you feel it sounds like that's in nevermind. I see what you're saying i'm not sure if we could recover as easy, but maybe we could.

**Mikhail kalinin:** yeah we should probably discuss continue this discussion. Some other place but before like we.  will finish with the latest well has a question to the bathroom and Eric on do you have any difficulties in implementing this as well.

**Andrew Ashikhmin:** We have implemented some basic caching so yeah you have that cash of invalid blocks and for each blog because the last leg or hash but it's kind of it's not very elaborate.

**Time beiko:**So maybe it makes sense, we have a testing golf scheduled Monday to use that to like focus on the some more and obviously we can we can use the discord like in the in the meantime, but. yeah it seems like clearly. spending more time discussing this on the call because it's probably valuable.

**Łukasz Rozmej:** If I can have one last comment here. Because it's in the morning of the mind so restart if we like like this something incorrectly the restarting would rise starting tomorrow so that would be a recovery scenario.

**Mikhail kalinin:** yeah. And also, I think yeah we should continue elsewhere and yeah one of the options, I think that i'm like in strong favor to keep it as this in this back and require this clients to follow this. Requirements. One thing that we could probably do if it's really hard to difficult to implement and some clients, we can accept that it will be implemented somewhere soon after the merge. Because, as i've said that the like risk of this attack is really low and comes with like very particular network and condition and so forth, so we can probably remove it like from the critical path to the merge. So, but I would strongly be in favor of leaving distance back as this and also yeah the hive test that we have if we if we collect keeping this requirement in this back so. We have the half tests in place just accepting this some tests that are related to these particular issue or just feel for the clients, this is the one of the options that we can take.

**Time beiko:** Okay.yeah I think that make sense yeah so let's yeah let's continue this conversation on discord and then on the dustin call Monday and.And yeah we'll follow up from there, but. yeah I don't think this is something we're going to resolve in the next like five minutes.And yeah thanks thanks again for for bringing this up and the client teams for for sharing all the details related to the implementations and any final thoughts on this before we move on.Okay. so I guess yeah The next thing we had was basically, I suppose, and how we feel about about moving forward there. I guess a high level the simple yeah we can chain is live it's run through Bella tricks so it's basically you know just waiting for it to be to be to be set. So polio, is also a bit different from robson and gordy and that the validator set this is permission kind of like gordy was pre merge or sorry gordy is today on on the execution lower. So it's much easier to coordinate like a network upgrade there. Because yeah but the node operators are are kind of large entities that that we can reach out to and yeah so I guess i'm curious from five teams like.  I know, on the cl call there were talks about potentially merging soboleva sometime in the next week and yeah i'm curious to hear from like email client teams what. What do you all feel is like a good timeline to to to emerge suppose yeah yeah Lucas.

**Łukasz Rozmej:** We are planning a release with some fixes next week. would be great if we if it was after that release, so we. Either late next week or or week after that is fine for you, every week after.

**Gary Schulte:** We can curse from from basis side as well.I think our consideration is that we don't want to overload the end of next week, seeing as how it regulates there's going to be going out but yeah.Either before after with a preference slight preference or after.

**Time beiko:** Okay. I guess Aragon.

**Péter Szilágyi:** it's just about something that needs to be and doing the release we can do that, whenever it just our request to be that. It would be nice to give people a heads up of let's say maybe a week that okay here's a new release run this for support them. Okay, so you have to be done, from my point on, we can just release the same day or the next day and.

**Time beiko:** Okay. Aragon.

**Andrew Ashikhmin:** Yes, so the same in Aragon, we can make a release relatively quickly, so no no hard preference.

**Tim beiko:** Okay. In that case. Would it make sense I don't have to add value now because I wasn't too sure if the date but would it make sense if a Monday. I can, I can come up with a tdd value, and then we have client teams put out two releases like.Ideally around mid week so if it was like Wednesday, so that, like Thursday we can announce it, and then we can we can forge some time like mid the week after that so there's like roughly a week.I went for it, by the way the the next week so two weeks from now on, the fourth of July is a big holiday in the US, so we probably don't want a fourth on the fourth of July. or yeah so maybe like you know, in a couple days after after that yeah. Peter.

**Péter Szilágyi:** yeah. Just a quick note. Last week we also configure the DNS. discovery for support here so. I know which client support it, I think many clients and execution client supported, but. The tl Dr is that you can also pointed. To support. To run this story. should work, it should actually have a lot with fighting peers, because everything was kind of annoying.

**Time beiko:** Yes, I complained about this on Twitter at everyone was. Suddenly meter you know my dad so glad to see that this is going live.cool yeah okay so let's do that so by Monday i'll have suggested TV or shared on the discord get like a plus one from all the client teams and and will aim will do like we did on on robson basically the tdd will be like very high such that, like it's unlikely, we would hit it.ourselves or sorry it says, actually, we would hit it to the straight, but then we'll rent some hash rate to accelerate when it actually gets hit. And so yeah we can have this value shared on Monday to two teams and. teams have a really South by like mid next week, like next week we announced this and then. Mid week after that, like around the July, five or six, we can have to the for capital i'm. just anyone haven't.

**Péter Szilágyi:** Yet I haven't. If we're going to do the same thing that we did for Austin please, so the drops. The whole mining was a bit of a pain, because. Essentially, we hash power points to the mining machine just overloaded with the mining machine I think overloaded, the the mining pool and. I think, Mario was saying that essentially there's not really not really good Open Source mining pool so it's kind of the expectation is that you won't be able to throw too much hash power at it without choking so. Dr Dr let's not run out 200 gpus and through all of it and then wait three days, because all hell breaks loose so.

**Time beiko:** yeah we can maybe yeah we can maybe also like start because we haven't been a heads up to, we can start renting some gradually as well, so yeah it doesn't have to be all as close and it's like. If we rent seven and we see other people are mining, we can obviously turn off our rigs so yeah we we can definitely try to yeah make it a bit less chaotic the cyber OPS.

**Péter Szilágyi:** Or alternatively, you could we could do is to. I mean running a small yellow and probably mining pool is fairly light so maybe we want to run out a significant number of gpus and maybe you could spin up I know 234 mining vm and point rings two different vm so that they like. super overloaded.

**Tim beiko:** Right yeah that seems like something that's.

**Péter Szilágyi:** predominantly ranting what is vs costs, I don't know half $1 an. hour $1 so it's not really relevant. 

**Tim beiko:** yeah okay. yeah that makes sense yeah and I might ask mariel to pin you Peter to chat about that some more but yeah definitely something we can do a bit smoother than the last time. i'm okay so yeah that makes sense, so let's aim for like a emerged date for supposedly of July 6 more or less plus or minus a day and then having client releases out by this Wednesday, ideally, so we can announce things on Thursday. Yeah. and cool anything else on suppose. OK, and then one thing I just I didn't want to get back on back to you from earlier is a shadow forks so like. We have obviously the main net Greg glacier fork up sorry Peter just about to do.

**Péter Szilágyi:** Yes, just a quick question.

**Tim beiko:** Go for it.
 
**Péter Szilágyi:** There was a discussion on how to avoid the not enough ether issue that appeared on the early and just a question was that salt on the client side.

**Time beiko:**All right, like yeah so that that I think I think what Gary Gary and give it a better.
 
**pari:**yeah I can yeah it is on the peaking plant side essentially what we did was.  Set the balance value of each and every validator to be a million at the genesis state and it looks like that it fits supply by about 1.5 billion, so a temps what it is. And a couple of other models that we can turn to ease the pressure over the cut over the coming years, I made a comment on that on github i'll have that view because that has a more concise explanation.
 
**Péter Szilágyi:** For Okay, I guess, the only catches that mean to. survive with the reality that the genesis location that teams until now so yeah for public process essentially I think every team was allocated. 100 girls, or something like that. During the grief meter and maybe within the country with a bit.

**Time beiko:**yeah i've been i've been doing that, by the way, so i've been sending a couple million support ether here and there to various facets and people, so there will be more and more faucets like spun up in the meantime, but I think I think will survive with the genesis allocations. Until we basically have withdrawals ship on support yeah and then from that point we'll get basically infinite inflation from from validators for very high inflation validators. And yeah Perry shutter sure linked in the chat about this. okay I yeah yeah The next thing I like to chat about was I settle forks so if we have Greg glacier and next week and we have a supposed to do the week after do we also want to schedule this shadow fork in the next couple weeks. I don't know Perry, do you have thoughts on that.

**Péter Szilágyi:** Yes, so since. The shadow from from yesterday was an epic fail. I think the fact that we are pushing them the test that shouldn't mean that we should. On pushing the main and since I mean pushing the desktop isn't too much of an effort, at least on my end developer from Stephen problem from Paris perspective. But still I think, as long as we have, there are no issues with the main channel for us, we should hammering along with.

 
**Time beiko:**Okay, and I guess, then the two things that would be needs to do on the next shadow fork is one run based to. Not in bonsai mode and to like manually set peers or static please appears and Aragon, to make sure that they have some some shuttle for peer I guess yeah that's a question to you Perry mostly like. what's a realistic like time for us to to get that setup.
 
**Justin Florentine:**I think, basically, here we prefer maybe a mix of.

**Time beiko:** frozen yeah we.
 
**Justin Florentine:**We plan on having fixes in in in that next build, for whenever perry's ready.

**Time beiko:** Okay.
 
**pari:** yeah I can work on conflict so on Monday or Tuesday usually the notes take a few days to sing cuz I mean that and we can have the shadow for probably Monday or Tuesday after.
 
**Time beiko:**So yeah so we'd have the shadow for basically at around the same time as. The support for like the day before or after.
 
**pari:**The same weekend yeah. yeah.
 
**Time beiko:**That makes sense. And Peter is your hands still up for something else.  So yeah so expect a shadow for not next week, but then the week after i'm. Okay, we only have 15 minutes left and there's like two things left on the agenda so there's the debug one from my client. But I know so Paul had one about the awkwardness time and I want to make sure we get to that too, because it's basically middle of the night Friday to Saturday for Paul and so yeah. Anything else I guess before we do anything else, just like on the merger shuttle forks otherwise, I think we should we should go over pulse pointed the rabbit with like hi oh.

**Andrew Ashikhmin:** yeah I have one question on the knowledge, I think, in the gifts like like i've raised this issue that some seo clients use NET network ID instead of his chain ID but by the engine API spec we should only. Enable. expose East methods so but, but the problem I saw on this court is that in in guess, for some reason East chain ad doesn't work before he. won five five transition, but can we somehow solve this issue because I mean we could expose the either make youth chain ID available from the start, or decide that okay just let's expose NET network ID.

**Paul Hauner:** formula that's perspective we're using on that idea at the moment and it's just kind of like a mistake by getting rid of it. We also come across guess not supplying the chain ID for a while, but we've just kind of worked our way around that i'm not sure if there's any other seo clients that are having different troubles, but I guess for lighthouse things to kind of find is they are.

**Andrew Ashikhmin:** Okay.

**Péter Szilágyi:** yeah I mean, I think the idea was that. Before you have a chain ID so. I don't know if this is probably more of a legacy thing that on wonderful scene, it was introduced to them. Before the fork it just. returns meal, because there was no change it, and then, after the 40 staff regarding the chain idea and.

**Time beiko:**Probably we just went with it.

**Péter Szilágyi:** The I guess the question interesting question is what happens Maybe it was also a bit of. Trying to guess the future will we ever change change change the chain I leave Probably not. yeah I think it's kind of a semantic philosophical question whether we should return a chain it for it or not, we can probably the current Chennai different from the get go.

**Mikhail kalinin:**yeah just quick thing, there is a PR intervention API El clients under certain conditions may skip the focus of data processing. And this PR makes little bit of change and may, in terms of like making it more precise these conditions with your client deaths go and check this PR and if your email client how it's currently implemented it's like broken by this change just that leave a comment. Oh yeah, otherwise it will be merged soon into this back.

**Time beiko:**Okay anything else on the merge. Okay, Paul, the floor is yours.

**Paul Hauner:** Oh yeah sure thanks so I was just pointing out that for a lot of Asia Pacific This call is kind of at times between, say 10pm and 2am on Friday nights that's places like China, Japan. Singapore Taiwan, Australia, New Zealand, I think that. it's not a great time for in terms of work life balance of people it's just kind of you know, Friday nights to socializing Saturday mornings, if the family. I think, also if there are any time so bad decisions to be yeah so I thought i'm just bumping it back. So, like 24 or 48 hours or something like that would be a huge help another point as well, is that places in Asia Pacific, so this is Friday night, so the next working day for us is in two days are actually things the next day is quite hard it's also quite difficult. To like, if you want to listen to the recording the next day, you need to either do it on the weekend or wait until the next day so yeah i'm just proposing the weekend, I mean, as I suggested pushing it back 24 hours someone else said, do 48 because people like to drink on Thursday nights. On a really show people like to drink all the time, but I think, at least on Friday nights clearly should be kind of sacred times in the five day working week so that's my proposal same time but just 24 48 72 hours earlier, please.

**Time beiko:**yeah Thank you. yeah and worth noting, obviously the cl calls happen on Thursday basically so that's a natural, it would be. nicely aligned with like this was on Thursday like people know every week on Thursday there's one of the others yeah I guess you know, the main stakeholders here our client teams like i'm curious to hear from like a different time teams could say Thursday 14 utc worked for you. Okay, so marius is fine I guess does anyone on like a client team feel strongly that like this is not a good idea.

**MariusVanDerWijden:** Only thing I really like about this timing is that afterwards I.can go to the weekend. it's like.  end of the week. Oh yeah I could just end my weekend. You can still go through the weekend.

**Time beiko:**After. 1400 utc on Friday, but yeah I I agree it's a nice way to wrap up.bet Okay, it doesn't see any objections. I I personally prefer Thursday is my favorite proposal like one because it alliance. One because it aligns with the cl calls and two because it does give us like one next one day after the follow up on stuff like I also. find that like an issue because I paid you everyone after this call about different things, but it's basically already Friday night in Europe, and so, people will respond to my messages. So yeah i'm. i'd like to do that and. I think what my my like preferred probably way to do this is to just like have the next El Cortez be the last one ever on a Friday and so people kind of get the. heads up like we typically try and not like change things like if I don't know if somebody in the next two weeks comes up with like a really good objection for this, I think it's hurting the needles, in time, but. yeah I would basically make the next awkward as the last one on Friday, give a heads up that like so it'll be it'll be on Thursdays and. Then have it on Thursday 14 utc. Last call if someone has an objection. Okay well yeah thanks a lot for coming on. yeah. yeah let's do this.

**Paul Hauner:** yeah Thank you very much, much appreciated really do appreciate it. cool.

# Standardizing namespace ethereum/execution-apis#247

**Time beiko:**um and last thing on the agenda, like client you had a proposal to standardize debug namespace ED across clients.

**lightclient**: yeah just a quick thing. This is sort of come up a. couple of these like in person. interrupt situations where we're trying to test why different clients are having. different issues and we've talked a bit about having like certain rpc endpoints to retrieve information I think in Amsterdam at that connects we talked about maybe having one to get the raw receipts from a block. And so, just like over time there's been a handful of these different endpoints that. would be nice just to have as a like standard across clients, and so I have a proposal to make four of those standard under the debug namespace and the idea would be that we you know each client just implements this. These rpc endpoints and they're all conforming to a spec we have this open rpc spec if you haven't seen i'll post a link to to the PR and that way we'll actually be able to run tests against these. against these endpoints and high to make sure that everybody conforms to it, I think this is just you know. Not only is it nice having standard interface across clients, but then we can build some more tools, on top of those interfaces to help debug clients without having you know individual behavior for each endpoint. So if some yellow teams could take a look at that proposal and, just like let me know what things you've already implemented, and you know what things. You would like to see implemented or maybe you don't think makes sense in this like super easy debug namespace that would be really helpful.


Micah Zoltu: For feedback on like. Things that would be useful, or should it be constrained, but I think that would be useful, and are relatively easy. Right now, and.

lightclient: I feel like it is better to go for things that are useful and relatively easy just you know it. I don't want to put more work on people, but it would be nice to have this as soon as possible, just so that there's you know less interface of people to worry about if we're trying to debug like more of these issues and test nuts. And so that's kind of why these. ones that we have are just basic getters stuff that like. A lot of clients already have but useful ones would be helpful to know as well, I would open an issue on execution api's and we can talk about it there.

**Time beiko:**Andrew.

**Andrew Ashikhmin:** So it says that guess supports all of these so my question like why kick me simply use the Internet to get current get interfaces as the basis what's is there a reason to deviate from gets interfaces.

lightclient: I mean we can but there's the to the data get header our therapy and get blocked or LP only take in like a json editor which is just different than all the other rpc endpoints they take hex strings. So I went ahead and took the liberty of just making not conform with the other types of numbers that we take in.

**Péter Szilágyi:** Yes. So I guess when the when the specification, the idea is that older clients can just.  tell what they would like to see, and how it would they would like it to work so it's not just get enforcing it's so these methods that are in gas. We just implemented the way we did because we whenever we give up something he did it and we just had the table. They weren't particular in well thought out and now you understand it is, it would be nice to actually put 10 minutes on thinking behind them before the client implemented whatever get us.

**Łukasz Rozmej:** I have a comment about the buck good but blocks because it's not really to implement correctly, so one implementation that I think we have enough of this PR in nevermind but. Yet is just to keep it in memory, but then, if you don't have the bug enabled module you have to restart it stand out to the naval it potentially we can have the personnel to see anatomy model to the table department robot again model is also disabled by default. So when you restart you lose this cash and you lose this but blocks potentially you could start them and some database persistently I think it does that, but then again, you need to turn them, potentially, which is like.  A lot of complexity i'm not entirely sure if you want to have it in the standards.

**Péter Szilágyi:** So we do not store it in a database that's fine we just storing the memory and the other thing is that gap, so if you attach to get on the IPC the old api's are available always so if it's not exposed on the rpc worst case scenario, and the national locker came out from there.

**Łukasz Rozmej:** Okay, and I PCs always exposed.

**Péter Szilágyi:** On PCs always unless you have specific.

**Micah Zoltu:** reason, never mind doesn't expose the book by default.

**Łukasz Rozmej:** Yes, if your endpoint is public, then you know it can cause a lot of load on the node.

**Péter Szilágyi:** The question was why don't expose it on it so https was aka gap is also very restricted butter on these unique socket we just I mean you're already on the machine within the docker container analysis or enable.

**Łukasz Rozmej:** You to be told we added IPC only like a year ago and didn't really think about configuring it this way it's disabled by default so might want to enable it by default and expose all API Sir.

**Micah Zoltu:** My we didn't talk about this somewhere else, since we're close on time, but my initial reaction is some unclear what the attack vector is where having debug exposed publicly is more problematic than having the.  Exposure locally like someone wants to take down your notes and six philosophically just hammer pretty much any endpoint and you're gonna. Oh no eventually.

**lightclient:** If you have said head explodes publicly, then you can just.

**Micah Zoltu:** Arbitrary sure sure, but said, have this cross out i'm assuming for this exactly.

**lightclient:** Okay you're just saying yeah.

**Micah Zoltu:** The ones that we have provided beginners.

**lightclient:** I think it's. I don't do it, but I see like with good bad blocks that's a little bit more dependent on what the client sees on the network. And so it's possible that if you're trying to run a like a proxy in front of several clients, you might have different responses, based on which one you're out to the command to.

**Péter Szilágyi:** Know it's tough to. Sorry, you will have the same issue, if you have two clients with mismatching change that every time request block for head they're all the different assets so. I think, once you start getting the bug you don't want anything in there.

**Łukasz Rozmej:** yeah like I mentioned, there is a set habit and only available, so you might want to like either move that or like admin module or something, and if we want to make the buck public, we need to review what's there potentially rebel some things from the pack module is.

**lightclient:** yeah the list of methods is just for methods right now it's in the the link that I sent.

**Micah Zoltu:** yeah no it definitely only advice I can give a public if it is get her, certainly if there's any writing and I agree, it should not be public.

**Péter Szilágyi:** I think we can all agree that this does that they should be just a read only thing, so that you don't have to hear. And Mary has had a really nice idea to what to call the chain modifier namespace you can call it a node and then you can say no setup.

**Time beiko:**Okay. i'm Okay, I guess we're basically a time i'm. Not I guess yeah people can can go to the PR there. That's probably the best place to keep discussing.

**lightclient:** yeah that or the json rpc API channel and discord i'll be watching both.

**Time beiko:**Okay. cool any final thing anyone wants to bring up pretty quickly. And Okay, if not at the lesson yeah i'll just share is like the tip is that people wanted to discuss that we're moving to the next call there was an update on 44444 and.five zero 27 So those are both link to the agenda if people want to have a look and we'll try to get them on the next awkward Apps and yeah thanks everyone for coming.

# Attendees
* Pooja
* brayton
* Sam wilson
* MIkhail 
* Tim 
* MariusVanderWidjen
* Justin florentine
* Ben edgington
* stokes
* Andrew ashikhmin
* Gary schuite
* Phil ngo
* Marcin sobczak
* Lightcilent
* mrabino1
* Pari
* metachris
* ansgar dietrichs
* caspar
* Helengeorge
* fabio
* protolambda
* Karim
* lukasz 
* pseve

# Next meeting
July 8, 2022, 14:00 UTC

 
# zoom chat 

Tim Beiko
10:08
https://github.com/ethereum/pm/issues/551
 
MariusVanDerWijden
10:44
I'm against more australians
 
brayton
10:54
oh no
 
Sam Wilson
11:19
Well that was tame.
 
pari
11:39
CL vs EL
 
lightclient
11:44
lmal
 
Paul Hauner
11:45
I’m a lover not a fighter ❤️
 
Tomasz Stańczak
11:47
at least DevCon Australia next year to pay back
 
Pooja
11:56
we are live!
 
Paul Hauner
12:06
Plenty of kangaroos around here for you to box though 🦘
 
carlbeek
12:28
researchers are the refs and the rules keep changing
 
Micah Zoltu
13:17
Do kangaroos actually punch with fists, or is it more of a stab with giant claws?
 
MariusVanDerWijden
14:04
https://www.dbentertainment.co.uk/category/sumo-and-action-suites/32/kangaroo-boxing
 
Paul Hauner
14:47
Hmm good question, I think it probably involves some claws. They’ve got some pretty serious front claws and I assume they use them.
 
Micah Zoltu
15:01
🤔
 
MariusVanDerWijden
18:36
Don't use only static peers though, otherwise we don't get the tx's from mainnet
 
Tim Beiko
18:47
Besu issue: https://hackmd.io/@RoboCopsGoneMad/B1reW1G9c
 
pari
19:01
Yea, I’ll use static peers for erigon and regular bootnodes for the others since they had no issues with peering
 
MariusVanDerWijden
19:48
When did you update erigon with static peers?
 
MariusVanDerWijden
20:01
We should see them syncing up now, right?
 
pari
20:09
2-3h ago I think, they’re syncing up last I checked
 
Ansgar Dietrichs
21:22
producing empty blocks (if it's a small share of the network) is still better than no blocks at all, because it then doesn't impact overall network throughput (because of 1559)
 
stokes
22:55
yes but afaik this set of bugs was around empty payloads, pairs could always produce _some_ block
 
pari
24:07
https://notes.ethereum.org/@samcm/By9o2Qg59
 
Justin Florentine
24:23
here is the writeup on besu - https://hackmd.io/@RoboCopsGoneMad/B1reW1G9c
 
pari
25:49
https://github.com/samcm/sync-test-coordinator
 
pari
26:58
Sync tests github action trigger: https://github.com/samcm/ethereum-sync-testing/actions
 
Justin Florentine
27:23
do empty cells in the tables indicate test hasn't been run yet?
 
pari
28:12
Yup, most likely there's a note relating to it and/or a previous test failed and it didn't make sense to run the subsequent test
 
MariusVanDerWijden
30:28
Geth-CL tba
 
lightclient
30:50
xD
 
Micah Zoltu
33:06
I'm not a fan of putting a centralized provider as a default.
 
Łukasz Rozmej
33:07
well thats centralization :/
 
Afr Schoe
33:17
/kick
 
Mikhail Kalinin
33:34
@Marius do you have an idea where the delay increase is coming from pre vs post merge? Is this in processing newPayload/fcU by EL or a communication overhead of calling these messages?
 
Micah Zoltu
33:40
Ah, if this is for testnot only I care less.
 
lightclient
33:56
*micah deactivates*
 
MariusVanDerWijden
34:12
Processing by EL most likely, shouldn't be too much overhead
 
Afr Schoe
34:29
I strongly disagree, if we cannot deal with testnets, how shall we deal with mainnet?
 
Micah Zoltu
34:29
😆
 
Micah Zoltu
34:37
👍 on per-client decision.
 
Micah Zoltu
35:12
@Afr I think the problem is that the set of people who use testnets is vastly different from the set of people who use mainnet.
 
pari
35:27
We can add checkpoint sync tests to Sam's sync test codebase
 
Tim Beiko
35:35
Is it easy to set up a checkpoint "provider"?
 
Ben Edgington
35:50
Any beacon node can serve checkpoints
 
Ben Edgington
36:05
They are just the beacon state
 
Afr Schoe
36:16
the problem is cannot identify mainnet problems if we treat testnets differently
 
Phil Ngo
36:21
We've been hosting our own public endpoints for people to test/use for Kiln, Prater and Mainnet. We're going to get one up for Ropsten shortly. Although this doesn't solve the issue completely
 
pari
36:34
Yup, its just a bit non-standard as to how you provide the checkpoint to the CL. Some take it in as a --checkpoint-sync URL and some require it to be passed in as a --initial-state
 
Phil Ngo
37:14
Lodestar of course doesn't want to be a centralized provider of endpoints
 
Afr Schoe
37:20
btw a prater sync takes around 5 days
 
Tim Beiko
37:28
full sync?
 
Afr Schoe
37:35
yes
 
terence(prysmaticlabs)
38:12
Nice doc summarizing what we’ve been thinking around checkpoint sync: https://notes.ethereum.org/@djrtwo/ws-sync-in-practice
 
lightclient
38:27
i feel like we need a standard for serving the data needed for check point sync and then a mirror list of ppl serving the data
 
lightclient
38:40
i think nimbus was working on a standard like this?
 
Paul Hauner
42:59
The checkpoint sync data requirements are fairly well specified, it’s just objects from the HTTP API.
 
lightclient
43:41
is it easily hostable w/o a beacon node?
 
lightclient
43:58
is it only the ssz of the beacon state at that point or more data?
 
lightclient
44:13
(sorry for such stupid questions)
 
Ben Edgington
44:23
For teku it is exactly that (SSZof the state) right now.
 
Paul Hauner
44:31
Yep, all present BNs will provide checkpoint sync for LH and Teku (perhaps others, not sure about them)
 
Ben Edgington
44:55
As an optimisation you can add some data about the deposit contract state - I think this is what Nimbus is working on.
 
Ben Edgington
45:34
It's just static data. so can be served by any fileserver.
 
Afr Schoe
45:40
why can't all clients serve checkpoint states p2p?
 
stokes
45:58
how do you know which state is the one you want?
 
Ben Edgington
46:17
Any finalised state will do. Preferably recent.
 
Afr Schoe
46:25
how do you know which api endpoint is the one you want? ;)
 
Paul Hauner
46:30
States are ~100mb and serving an object of that size is tricky for DoS attacks.
 
Afr Schoe
46:38
gotcha
 
stokes
46:47
right so you supply a hash and then we could definitely do something like "state sync" for the beacon state over p2p
 
Paul Hauner
47:21
Yeah the argument goes that if you got the hash from somewhere then you might as well get the state too.
 
Afr Schoe
47:27
EL has a state sync and the EL state is huge
 
Paul Hauner
48:06
And EL state sync is very complex from what I hear!
 
stokes
48:18
partially bc it keeps changing
 
stokes
48:23
becon state has less thrash
 
stokes
49:05
but i think paul's point about "just get the state from the trusted hash provider" makes sense
 
stokes
49:17
just need someone who can host states and provide the bandwidth
 
pari
49:47
IPFS?
 
pari
49:57
We run an IPFS server for sourcify + devcon videos
 
stokes
50:02
has no availability guarantees 🙂
 
lightclient
50:14
list of ipfs providers
 
pari
50:30
of course, its best effort at that point. Step better than what we have now i guess
 
MariusVanDerWijden
50:53
Clients teams run their own big servers, similar to the bootnodes
 
Afr Schoe
50:57
it should be p2p state sync long term
 
Ben Edgington
50:57
Since Adrian S is not here, his last couple of blogs are quite relevant: https://www.symphonious.net/
 
Afr Schoe
51:38
it's different hosting a bootnode or sharing consensus relevant state
 
stokes
51:43
one consideration here is if client teams should be responsible for both choosing which chain is canonical and moreover incurring the cost to provide all of this infra
 
Phil Ngo
53:21
There was somebody previously working on a WS checkpoint provider server, but not sure if this project has been abandoned: https://github.com/adiasg/eth2-ws-provider ... the idea was to allow people outside of client teams to spread this info
 
Afr Schoe
53:29
we came full circle if ethereum clients rely on infura :p
 
stokes
54:16
yeah i was hosting checkpoints for a hot second
 
stokes
54:42
it sounds like it is time to revist
 
lightclient
55:26
would be cool to have a binary that just connects to the local bn and serves this data
 
Łukasz Rozmej
55:43
sorry was off for 3 min
 
Łukasz Rozmej
55:55
I still want to add something
 
Tim Beiko
56:16
Will get to you after Mikhail's comment :-)
 
Łukasz Rozmej
56:29
sure, thats the best way to move on :)
 
Łukasz Rozmej
01:14:25
so merge around 6th?
 
Micah Zoltu
01:14:57
Huh, I didn't realize Sepolia was PoW. 😬
 
Tim Beiko
01:15:00
Yes :-)
 
Tim Beiko
01:15:21
to both Łukasz Rozmej and Micah
 
MariusVanDerWijden
01:18:14
@pari looks like the erigon nodes are all stuck again (probably because the CLs are not sending heads)
 
Gary Schulte
01:18:31
1.5 bil!
 
Paul Hauner
01:19:20
Time to move your Sepolia assets into something inflation-proof.
 
pari
01:19:26
https://github.com/eth-clients/merge-testnets/pull/14#issuecomment-1152570001
 
pari
01:19:35
^info about sepolia inflation
 
MariusVanDerWijden
01:20:14
yes more shadow forks
 
Karim T.
01:20:14
yes +1
 
Łukasz Rozmej
01:20:37
we can do shadowfork ~week after sepolia
 
Paul Hauner
01:20:55
Also keen on more shadow forks. We have a decent change coming to LH in the next week or two. Would like to see testing on it 🙏
 
Karim T.
01:21:12
we also want to tests some fixes regarding bonsai on the next shadow fork
 
Gary Schulte
01:21:14
or a mix of bonsai/forest rather.
 
MariusVanDerWijden
01:21:46
:raised_hands:
 
MariusVanDerWijden
01:23:40
Rene's fix bites us in the ass :D
 
Micah Zoltu
01:24:02
I'm not a fan of exposing net_ stuff over the engine API.
 
terence(prysmaticlabs)
01:24:08
Prysm is also fine
 
Micah Zoltu
01:24:12
Complicates things to expand to additional modules.
 
Mikhail Kalinin
01:25:08
https://github.com/ethereum/execution-apis/pull/244
 
Afr Schoe
01:25:28
isn't network id something different?
 
Micah Zoltu
01:26:38
😆
 
Micah Zoltu
01:26:56
@Afri It was supposed to be I think, but ended up not being?
 
Łukasz Rozmej
01:27:21
I'm drinking right now :P
 
Mikhail Kalinin
01:27:25
lol
 
Micah Zoltu
01:27:27
🎉
 
Afr Schoe
01:27:31
both can be different for the same network, e.g., for classic
 
Micah Zoltu
01:27:48
I like having it the same time as CL calls for that reason (Thursday).
 
MariusVanDerWijden
01:27:51
Fine by me
 
stokes
01:27:57
+1
 
Andrew Ashikhmin
01:28:02
fine with me
 
Phil Ngo
01:28:03
+1
 
Ben Edgington
01:28:05
Yep (Teku)
 
terence(prysmaticlabs)
01:28:08
+1
 
Łukasz Rozmej
01:28:19
when? -24h?
 
Micah Zoltu
01:28:22
Translation: "Does anyone on a client team hate Australians?"
 
Micah Zoltu
01:28:46
@Lukasz Yeah.
 
brayton
01:28:50
(perhaps a very small factor is that party lounge also goes rather late and is worth staying up for while being unrecorded)
 
Micah Zoltu
01:28:57
-24 hours from today's meeting.
 
MariusVanDerWijden
01:29:04
@Micah Me (as we established earlier)
 
Micah Zoltu
01:29:13
Ah, I missed that.
 
Ansgar Dietrichs
01:29:29
gonna be a challenge for the party lounge, harder to justify wasting half of Thursday ;-)
 
Micah Zoltu
01:30:30
Only if your priorities are wrong.
 
Paul Hauner
01:30:30
🙏🙏🙏
 
Łukasz Rozmej
01:31:10
+1 to move ACD in 4 weeks
 
Justin Florentine
01:31:16
yes! intermittent state roots too!
 
lightclient
01:31:28
https://github.com/ethereum/execution-apis/pull/247
 
Micah Zoltu
01:31:31
debug_blockWitness please.
 
Micah Zoltu
01:33:50
👍 for bringing these in line with other APIs in terms of "style" (hex strings).
 
lightclient
01:35:40
badBlocks is less about correctness IMO and more about the spirit of trying to provide info to devs
 
lightclient
01:37:57
fair
 
MariusVanDerWijden
01:38:39
heynode_pleaseSyncToThisBlock(h header)
 
Łukasz Rozmej
01:39:18
its godd you clarified the joke part ;)

