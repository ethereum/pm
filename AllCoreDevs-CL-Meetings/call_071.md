# Consensus Layer Call #71 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2021/08/26 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  1 hour  <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/233) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=DZiy3RhUgNY&list=RDCMUCNOfzGXD_C9YMYmnefmPH0g&start_radio=1) <!-- omit in toc --> 
### Moderator:  Danny Ryan<!-- omit in toc --> 
### Notes: Avishek Kumar <!-- omit in toc --> 


-----------------------------

# Contents <!-- omit in toc --> 

- [1. Altair](#1-Altair)
- [2. Client Updates](#2-Client-Updates)
- [3. Merge discussion](#3-Merge-discussion)
- [4. Research Updates](#4-research-updates)
- [5. Spec discussion](#5-spec-discussion)
- [6. Open Discussion/Closing Remarks](#6-Open-Discussion/Closing-Remarks)


  - [Attendees](#attendees)
  - [Zoom chat](#zoom-chat)
  - [Next Meeting Date/Time](#next-meeting-datetime)

-----------------------------------------------
# 1. Altair

**Danny**:  The consensus layer call number 71. Great! so we will focus I think a lot on
Altair today as usual. Then we'll do some client updates and we can do quick merge discussion. 

##  new release

**Danny**:  Although we had quite a merge discussion over the past hour on the engine API then research updates and any closing remarks spec discussion et  cetera v110 beta 3 is now out and the test vectors are being uploaded currently I will try to keep. I have to upload each file of those targets independently or github dies. So I will do them one at a time during
this call and hopefully they'll be done at the end of the call. Thank you for your patience on that and huge shout out to Alex for greatly greatly increasing test coverage so hopefully some good stuff will come out of that. Cool so that was the beginning of Altair. We do have a new release. There's some other goodies in there with the merge and sharding if you're following along on those. 

## pyrmont testing status
**Danny**: Pyrmont upgraded one week ago and we do have some coordinated testing going on. I believe today we should be turning finality back on it. Looks like some of y'all have begun to do that we're back at 60. We have been non-finalizing for 720 epochs, which is very cool. There are a number of other things that we like to get on there. Specifically get a bunch of deposits get a bunch of exits make sure we have all the different slashing types covered and you know do weird things to your heart desire. Is there anything on pyrmont testing that we'd like to discuss.

**Terence**: Right. so for food transparency would run into an issue where the prysm could not sink under a finalist period but the issue was quickly fixed and patched and then we got a new release out. So yeah personally I am really grateful for this type of test that  allows us to catch issues like this .

**Danny**: Was it a fresh sink that you had issues with like trying to start up?

**Terence**:  No, it was the checkpoints sync and then if checkpoint sync for such duration
with the e-part that's not finalized for some reason we couldn't process the block but yeah let me post the issues here and the details are in the issues but yeah.

**Danny**: Gotcha cool. I mentioned this elsewhere but we are looking into doing a more
concerted effort to do scenario type testing in real large but kind of controlled test nets. This is just a bit of a taste of that hopefully we can get some of that going over the next couple months to harden Altair stuff and get ready for merge. Great any other on pyrmont I think
technically once we finish running through at least what I shared in that issue 59 on eth2 networks.we will consider it deprecated obviously you can do whatever you want with it. You can continue to run nodes and see what happens or call today. I think as we approach the merge we would spin up a pretty sizable test net against each of the eth1 test nets that we want to keep and do kind of emerge practice on each one of those. I guess even regardless of wanting to keep them but we can discuss that Later.

## Prater in one week
 
**Danny**: Okay  prater will launch in one week minus two hours I believe. There is a config up, it was merged. If you haven't taken a look please do a final sanity check on that. If you are listening to this call keep an eye peeled for prater. Altair releases on your client of choice
and upgrade if you are on that test net. As we approach that one week from today. Are there any comments or questions on prater? Pari you're gonna work on upping the validators on prater. Can  you give us a quick answer?

**Parithosh**: Yeah I have just reached out to all the client teams to figure out who's gonna be taking part in that? I am just creating a small dock to figure out who  would have to turn on the validators? on which date? I guess I do the reposits over the weekend or early next week and should hear more from you next week

## Planning

**Danny**: Got it, so obviously after prater we do want to target a mainnet launch.So, I think we have a handful of things in the works that will continue pyrmont testing. Seeing prater go well and also probably not. Well I guess we could turn off the finale if we want. I think there's a marginal gain to doing that but hitting it with operations and different things. The test vectors that just came out hoping that doesn't uncover anything crazy and then I think we need to be eyeballing a mainnet launch. I do not think that we need to set a date today. I think we should get through what happens in a week and then set a date but any thoughts, feelings, desires with respect to mainnet timing? Main thing is that we give people plenty of time to upgrade between when we announce it and get releases out too.

**Parithosh**:  Yeah, when it actually happens, we will depend on the community for this one. Right? Whereas we've controlled them all .

**Danny**: Absolutely and we'll do. We can certainly have blog posts with all releases and things like we do and I have done on the proof of work chain. What do you think of the suggestion time? 

**Jacek Sieka**: I know I am going to prove a different question which is basically we've been considering whether to make two releases before a main at Altair or  just one release like a big one with a bunch of features and stuff and then just a small one with you know an
epoch update or two releases and i'm kind of curious what people think about that.

**Danny**: So I think lighthouse has probably done a version of that. And that they just put
1.5 out officially last week which they think was a big release. Then Altair obviously would just be something more minor with an epoch. But as we approach my intuition would be doing a release within seven days of each other or something like that might cause more confusion than it's worth but I don't know.

**Andrian Sutton**: I am pretty keen to see each client have an actual release with the  product config in it rather than an RC or so on. How does that tie into big features for you? Is
kind of a side effect but actually have Altair merged the main branch. It's a full release that clients are upgrading to? Because then it's ready. The one change you have to put into mainnet is just a conflict change which you know. Hopefully you can't screw up whereas anything else is kind of merging and doing other kinds of more complex stuff. It's much easier to introduce other bugs and effectively haven't tested it. So that's kind of my view on it. I would lean towards whatever gets you there but beyond that uses these are pretty slow to upgrade unless you tell them. This is going to completely break if you don't upgrade, so I think it's really just going to come down to when you put out the release that says you know this got the main net fork in it. You have to upgrade that's when a lot of users are going to actually pull the trigger and apply it.

**Danny**: Back to the prior question Adrian, do you have in or you or any other others have an opinion on when those releases are? The lead time between those releases being made and getting into a public blog post and that fork date is that a two-week minimum three-week minimum more.

**Andrian Sutton**: I would say two-week minimum but I would be very tempted to learn from
what each one side has done and what kind of timelines they normally set.  Because I think that's the expectation most users will probably have. Right?  It's a good baseline anyway.

**Jacek Sieka**: Yeah I am not looking at London guests who had releases  like what a few days before . Well that is very true but that was also exceptional. Scenario I wonder when the initial blog post went out on the lead time though which we can figure out probably quickly.

**Andrian Sutton**: Yeah I mean emergencies happen and you can get it upgraded fast. Probably the best example of that was when the first constantinople thought got cancelled and it was you know 24-48 hour time to turn around and get new clients out to cancel it. It went very smoothly so it is possible to do it fast but..

**Danny**:  Yeah I think we might not cover all this in altera but I think there's a desire to
define a bit more clearly what the binding bugs and disaster scenarios and things like that are especially leading to the merge. You know rather than very subjectively being. We are fine defining a bit more clearly what our like halts and arrows are. Although once you publish those mainnet releases

**Andrian Sutton**:  For some reason I had just in my head a month after we fork prater. So  like a month from next Thursday that probably could happen quicker. I guess if we wanted to. But I am not sure that I think it seems like we are pretty much there in terms of engineering. It is just kind of waiting for it now and perhaps giving a little bit of extra time for people to move over and a little bit of extra time for us to run these test snaps is good. I am not sure that I can't at least for us it seems. I am not sure we need a deadline to push us at the moment. We are pretty much there when the deadline was the test nets.

**Danny**:  Yeah, I mean I think that puts us at the last day of september which I think is
a pretty good target and then we need to subtract probably two and a half weeks on mainnet releases and two weeks on really getting that blog post out which I think is looking at the calendar that all adds up in a pretty reasonable way assuming that we don't run into any unexpected.
 
**Paul Hauner**: What's the subtraction on the blog post?

**Danny**: Oh I just meant you know if we're gonna release, if we're gonna do mainnet on september 30th which would be one exactly one month after the prouder upgrade. Subtract two and a half weeks on the deadline for mainnet releases and the blog post going out a couple days from there. So like you know the september 13th would be everyone needs
to have their mainnet releases out and then the blog post is coming out the 14th or 15th which gives. You know slightly more than two weeks of lead time otherwise you'd have to do mainnet releases the week prior and if you're trying to get the blog post out in like three weeks time.

**Adrian Sutton**: All right because you want the blog post to have the client versions in it. Is
that right ?

**Danny**: That is historically what has been done on the upgrades on the proof work chain yes

**Adrian Sutton**: I suspect that timeline will work well. We can probably pick a candidate upgrade epoch around the time private forks and then agree on it. Not long after we see it's working. Basically that starts the release processes and kind of gives. Yeah, I should plan out.

**Jacek Sieka**: Yeah,I feel the same that let's wait for the broader release before we make that decision also because you know the latest test vectors were released today.

**Danny**: Yeah cool I am comfortable with our abstract tensive plans and we can pick this up in one week's time. Okay anything else we want to discuss with respect to Altair planning
anything that is glaringly missing from all of this or we generally have the pieces in place that we're happy with. Cool the minimal target is on the spec test release now and now the general is. But now I am gonna have to add the main net which should take a few minutes
if anybody bonus points anybody that runs minimal on their local build before the end of the call.

# 2. Client Updates
 
**Danny**: Okay back to the schedule. Let's do a quick round of client updates. I suspect it has a lot to do with Altair. No need to hit us too hard.

## Nimbus

**Danny**: We can start with Nimbus

**Mamy Ratsimbazafy**: Hi  as you said a lot of Altair upgrades, especially performance improvement to make the blocks between slots and also e-box way faster and also rest api updates as well.

**Danny**: Great! Grandine

**Grandine**: Yes they sold us from the team so we still work mainly on this separate forks running on the separate runtimes thing and even though it has every pencil this Altair tests however there are still a lot of work that needs to be done in order to connect everything into one piece as running in the separate runtimes. It comes with a with a different with a new
challenges really for example just an example to understand the complexity when the altair run time starts to work it needs to  get the history before the merger. Before the fork  point in order to have four choices working. so basically the initial idea that we thought that after the merge any history of the previous fork. It's not actually valid as we need to have at least some history to make a four choice on the Altair runtime work,so we are solving a lot of these interesting issues.

**Danny**: Great, thank you

## Loadstart


**Lion Dapplion**: Hey everyone Lion here, so finally we have released our browser
like a lion prototype. Super excited had very good reception and looking forward to add more
transports. Next we have also hacked an alternative representation of bytes in javascript
which has allowed us to reduce the size of the hashing cache by half and it's been great to reduce garbage collection performance Biermann went well and we are looking next week allocating a portion of our team to implement the merge and hopefully having it ready soon
Thank you.

**Danny**: Thank you and on that I think maybe it goes without saying but on the execution engine side I think people are expecting to be heavily in kind of prototyping over the next month and so beginning to shift a bit of allocation on your side to implement the latest on consensus layer merge specs will help unblock. Cool, great.

## Prysm


**Terence**: Hello everyone, so for the last two weeks, we've been mostly reviewing Altair changes and merging those changes into the developed branch and then as you know last friday there was a minor incident with the validators. So I think they were proposing blocks fairly late and due to that we found a  few deficiencies with how prysm handles attestation mempool. So first we were not re-inserting orphan attestation back to the main pool and that is fixed. We found another deficiency where we did the attestations when the blocks got verified  instead of blocks becoming kind of canonical. So also fix that as well and on top of that we're just working on e2 api and then uh gearing for the v2 release yeah that's it.

**Danny**: great

## Taku


**Adrian Sutton**: Yeah hi this is Adrian. So we have got a release that should be coming out tomorrow. It's just doing the final kind of staging process at the moment that will be
21.8.2 and it will have the alto upgrade epoch baked in for prater. It'll also have some really nice optimizations particularly around reducing garbage collection time so lower cpu and memory usage.We have done a bunch of research with teku working against particularly in
fiora but anywhere you have load balanced beacon nodes and so there's a new option to disable producing early Altair stations because it's quite common to get from one node a head event saying they have the block and then you produce the attestation against a different node and it doesn't have it yet. So you wind up with a bad head vote.So we have seen performance dramatically improved against load balance at bigger nodes and infuria with that option. It will also include a change for the remote signer api so that we can send Altair blocks through to things like web3 sign up which is a block v2 type. We'll get the rest api specs for web3 signer updated with that. Yeah that should be should be good to go with the prior then hopefully and that's it from us.

**Danny**: great

## Lighthouse

**Paul Hauner**: Hello everyone paul here, so this week we released version 1.5.0. It seems to be going well. There's a couple of reports of myths that just like a lowered at the station
performance happening but i'm not sure if that's just limited to lighthouse or it's network
wide. I am still trying to figure out exactly what's going on there. We have a 1.5.1 release scheduled for Monday that's going to include our prater. The prater fork, so 1.5.0 means that we have all of our Altair stuff in master now. We are also started working on remote sinus support for web 3 signer which is what Adrian from techy mentioned just before so that means I believe that my house and teku will both be able to support the same. Remote signer from their vc which would be pretty cool. Our week's objectivity progress is going well. We've done some successful starts and backfills now. We are just working on getting review ready for production and that's it from me.

**Danny**: Great thanks Paul.

# 3. Merge discussion

**Danny**: And number three is merge discussion if  there's anything people want to try
about by all means. I think we hit the engine api pretty hard this morning so, I would defer additional conversation on that to discord and some fault conversations rather than doing it here but are there any other merge related items we'd like to discuss today.

**Mikhail Kalnin**: yeah I have some. Yeah we decided to continue our engine api discussion during the next all core dev call. Great, spend a bit of time on it. Yeah with regards to other stuff on the merge. There is the post by Dimitri who has been evaluating the
precision of the total terminal difficulty computation that we will use for the actual transition from proof of stake to proof of work. A bit of context: this terminal total difficulty is going to be computed during the merge fork. It targets the seven days after the merge fork is happening for the actual transition to proof of stake and this research is about evaluating the precision of this prediction on the historic data. Yeah the key takeaway  from it is. We might want to use a more precise value for a more precise value for the second spur for the fourth block than the 14 seconds which I used currently.  It will increase like the precision  of this. Yeah it will make the prediction more accurate. You may take a look at the comment  below this post 
for the comparison table but yeah it will like make it more accurate but the precision is like we should expect the merge within the 20 hours interval which will be around this you know
target time which is seven days according to the current spec. So this is because of the difficulty fluctuations and because of the stochastic process that we have to drive the block building of the proof of work chain  I don't think we can do anything better here and as I understand we have the London hard fork slightly after the predicted time. Am I right?

**Danny**: I am not sure

**Mikhail Kalnin**:  Okay anyway so there is a 20 hours interval but we might increase it. We might move this into a wall and to make it more accurate if we change this second square block parameters. So I would suggest adding a new parameter to this pack and get back to evaluating the average block time. As we are close on the historic data is where close the merge and settle with some value that will be otherwise to the state of the network by that time. So that's it. That's just a suggestion.

**Danny**: Got it i sure as one confounding factor might be if we are approaching an ice age which may be the case.

**Mikhail Kalnin**: Yes and we want to approach the ice age right towards the merge. So we should take care of it as well. Yeah that's all for this post to take a look at it. It's just a nice collection of statistics data and thanks to another mine team who provided us with data from the mainnet for this research.

**Danny**: Cool,  thank you Miguel. Any other merge related items we'd like to discuss?
Okay, it looks like there will be some continued refinements that come out of enter into that engine api over the next couple weeks,so keep your eyes peeled and like I said as Altair wraps up getting merged prototypes that are in the direction of the current merge specs and the eip that is up will help move for it.

# 4. Research updates

**Danny**: Okay cool any research updates people would like to share today. 

# 5. Spec discussion/Open Discussion/Closing Remarks

**Danny**: Okay, any spec discussion/ open discussion/closing remarks. 

**Paul Hauner**: I have been asked to mention something in the configs about the temporarily set fork versions. How would people feel about nulling them? I don't know the background for this so I can't make an argument to it but I am doing what  I am asked for. There is an issue for this. I will find it.

**Danny**: Yeah sorry what? can you repeat that one more time?

**Paul Hauner**: Sure there's an issue on the consensus specs569. It's about knowing using null instead of u64 max value. Sorry the 64 minus one. Yeah I am not. Yeah there is I am just trying to see if people would be against that.

**Danny**: I would like to see more justification here. I just know I think that the justification of at least some legacy is better clarity. I think the alternative argument is that you don't have to have any exceptional logic because you can just use your basic comparison operator and not really worry about what the value is. I don't feel strongly here but does anyone else want to jump in or shall we just move to the issue.

**Paul Hauner**: Perhaps we can just move to the issue. I am  going to ask people to put some more justification there. I feel like it doesn't warrant it at the moment for bringing it up.

**Danny**: No, it's good. Take a look at issue 2569. okay snowman is going off in the chat youtube chat having a conversation. Okay cool I think that we are good. Anything else?

**Leo BSC**: I have a question concerning the peer id. When the nodes update on their
client it seems that the peer id changed this to a new one and I would like to know why this is? Is there any particular reason? Why is this like this or is it just an arbitrary decision?

**Danny**: Update as in change their client version or just like cycle their node and is this all clients are just a couple you're seeing.

**Leo BSC**:   I am not sure about all clients. I noticed that in a couple of them and yeah update like if they get a different a new id and because of that it's difficult to track. You know the evolution of new versions drawing out. So we have been using the crowler to see how
you know people adopt new versions and how this evolves, but the thing is that what we see in the figure is that when a new verse for example a new version comes up. We just see kind of an increase so, we see the new version a lot of notes getting up the new version but we just see a lot of new notes and it just we don't see a decrease on the other ones and this is because I think they changed the id and then it's difficult to track. You know we just see them as new notes. We don't see how these notes just change from the previous version to another version. I don't know if that makes sense

**Jacek Sieka**: Yeah so we explicitly change peer id for every restart for privacy reasons. There's no reason to keep it the same. By changing it at least we casually break the link between the beacon node and validator every now and then. We've actually considered every connection. The last thing about crawlers that I say that I will say is that we don't
when our peer table is full. When we have all the connections that the user has configured it to have. We will no longer accept connections on the socket even. So we won't allow the crawler to come in. So those are like common sources of why song crawlers might be skewed in general. In lighthouse we persist our peer id.

**Danny**: Yeah I mean i think it's a very reasonable to keep that as an optional design to be
able to cycle or persist. It's unfortunately probably in the impetus of the crawler to figure out
what is stale and what is not. Because I think there are very valuable privacy considerations for wanting to be able to cycle and move things around.

**Paul Hauner**: Peter from geth I think at devcon prague did a really interesting talk about
tracking himself around the world by his peer id. So it's definitely a privacy leak.

**Danny**: Right and I do. We also got you all have no. You don't have a target and a max so that you can accept inbound connections and then kind of like prune them back down. There's just a strict max.

**Jacek Sieka**: Well we have a strict max for the simple reason that every time we accept a
connection. We have to negotiate a key with those new connections so that is actually one. Way to dos a client it's just like keep opening connections and we kind of want to save those
resources so when the connection table is full,it's full. I mean we're not going to be talking to these people anyway. We have considered softening that but again like the only one that benefits is. Again you're leaking a little bit.

**Danny**: Yeah I mean you can imagine an extreme where you have a lot of network rigidity and it's difficult to join. If everyone was following this strategy as opposed to say target 50 max 55 allowing. You grow up to 55 and then like having some pruning strategy, which could still potentially handle the dos as long as your pruning strategy wasn't really aggressive and you could always open new connections. But anyway I don't think there's a strictly correct behavior here.

**Jacek Sieka**: Well even there right you'd still get pruned. right presumably

**Danny**: well sure, your pruning strategy would depend on some sort of heuristic algorithm, which then all of a sudden becomes potentially an eclipse attack vector depending on if somebody can find an exploit in that algorithm.

**Micah Zoltu**: I think it's a tension between you wanting to rotate clients to prevent the like. Danny you said from the network being too rigid and getting stuck with. You know no one knows you can't join because you have everybody's at max and on the other side you want to prevent eclipse attacks which definitely get opened up a lot if you allow. If you have a well-known strategy for rotating clients. People can exploit that to force their own nodes to get rotated in and other nodes rotate it out. It's not easy.

**Adrian Sutton**: The flip side there though is that it's much easier to eclipse you. If I can just fill your connections when you first appear and you can never just be the first one to connect to you and then you never connect to anyone else and I own you forever.
 
**Jacek Sieka**: Yeah so like we did two things to balance, so one thing is that we have
quite a high peer limit compared to the others. 160 ish and this works well because gossip sub itself which is like the bandwidth hog manages its own bandwidth usage through the mesh right, so having lots of peers connected doesn't really affect bandwidth that much. Then yeah there is a peer scoring  system in place where we occasionally get cares that are
not pulling their weight. So at the end of the day we still have some dynamic behavior. It's just that the moment that it's full, we no longer spend resources on it. New pairs until we have determined that some pair is useless.

**Leo BSC**: But if we update the prd so frequently. Doesn't this damage the pr scoring algorithm?

**Jacek Sieka**: Well both ways right it forgets penalties and it depends like we can't assume that others will remember our peers course across connections. So we start with a clean slate with the new peer id and we work on that  reputation right?  The reason is I think guests do also drop peer reputation on this connective. I remember right and they motivated this with the fact that you know the moment that you restart something completely different might be happening even if it's the same peer id connecting so there's like difficult to reason about security and peer score.

**Danny**: Right it goes both ways you could have fixed a bug in your client that made your fear score bad or you could have made your client malicious trying to leverage what was  your previously good score but you could also make that change to move towards  maliciousness without cycling but anyway. Yeah I mean Leo I think there's something at odds here fundamentally you  know there are. It's not always in the best interest of a client to make things easy for a crawler because of privacy issues and other  types of issues. So I  think as a crawler you have to try to just navigate the emergent landscape.

**Leo BSC**: Absolutely Absolutely no I completely understand and we will figure out a way
to  just you know discard the connections that we don't see for a certain time and we will figure that out. I just wanted to bring up the discussion a little bit to understand and another thing  just to remind, please all the clients about the standardization approach. I mean the effort that we are making because we are trying to start  building these dashboards with all the standard metrics. We agreed so yeah just keep an eye on that. The next releases have all those metrics and use the standard metric. Sorry naming system that we that we are
open on. Thank you

**Danny**: Okay anything else would people like discuss before we close today

**Grandine**: Regarding this idea, the thing is if I understand correctly, the actual benefit for the client is to keep this idea to keep the score. I am not sure I mean if you just said is there a suggestion to make this optional or mandatory to roll these ideas.

**Jacek Sieka**: I mean the suggestion is that you choose for your users or you let them choose. There are reasons for both we allow both because for example when you're running
a boot node is a stable node that some users presumably trust the same. The peer id is also used as a source for the public key that verifies that you are  connecting to the node that you think.  You're connecting when you have a trust relationship between two nodes. For  example you're on yourself with two nodes and want to make sure they're connected obviously. You need to keep the peer id but on the other hand there's a privacy issue. So I mean right now in the network design is the most private thing. We can actually use a different pair id for every connection that we open and that is an extreme option that I don't think any client does right? Now it's certainly a possibility it would cost a little bit in terms of dht lookups and like it would be a little bit more difficult but it's certainly possible.

**Grandine**: But this issue was mainly raised because of the crawlers or somebody asking for the increased privacy.

**Jacek Sieka**: It was discussed at early stages. What to do about the causal link between beaker node and validator? The main issue is that if you know which validator is using.  Which beacon node you can trivially dos them in the targeted attack and then if they don't have a good backup strategy then potentially you can like a low-cost craft  grief individual validators basically.

**Grandine**: Yeah, just disconnect them from the network. Okay thanks

**Jacek Sieka**: I just mentioned that changing pair id is not foolproof. It's not secure in that sense. It's just a tilt in that direction all right.

**Danny**: Okay  other items people like to discuss. Great prater in one week, if you're listening keep your eyes peeled for releases that include these updates and you can join us on the test net fork. Talk to you all soon thank you.

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
- Lightclient
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

## Next Meeting Date/Time : September 9, 2021 at 1400 UTC.


## Zoom Chat 

From danny to Everyone: 03:07 PM

https://github.com/ethereum/eth2.0-pm/issues/233

https://github.com/eth2-clients/eth2-networks/issues/59

From terence(prysmaticlabs) to Everyone: 03:08 PM

https://github.com/prysmaticlabs/prysm/issues/9450

From danny to Everyone: 03:22 PM

https://medium.com/chainsafe-systems/lodestar-releases-light-client-prototype-40f300361c65

From Mikhail Kalinin to Everyone: 03:27 PM

https://ethresear.ch/t/using-total-difficulty-threshold-for-hardfork-anchor-what-could-go-wrong/10357

From Micah Zoltu to Everyone: 03:31 PM

Ice Age doesn’t need to be immediately after the merge. It just needs to happen sometime after the merge to achieve its original goal. So we can give ourselves lots of breathing room on that front.

From Mikhail Kalinin to Everyone: 03:32 PM

Right, it will need to be set in some advance to give us a room for setting the exact merge fork epoch

From Alex Stokes to Everyone: 03:33 PM

https://github.com/ethereum/consensus-specs/issues/2569


