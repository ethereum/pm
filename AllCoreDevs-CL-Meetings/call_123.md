# Consensus Layer Call 123

### Meeting Date/Time: Thursday 2023/11/30 at 14:00 UTC
### Meeting Duration: 44:18
### [GitHub Agenda](https://github.com/ethereum/pm/issues/916) 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=s3jIn3ot57g&t=1s) 
### Moderator: Danny
### Notes: Metago

## Agenda

### Deneb [4:13]( https://www.youtube.com/live/s3jIn3ot57g?si=PQ8hv1IJrbJA-bwU&t=253) 

#### Testing and devnet updates

#### Spec release – [release v1.4.0-beta.5 consensus-specs#3554](https://github.com/ethereum/consensus-specs/pull/3554)  

**Danny** 
Okay, we should be live. This is the all core dev consensus layer call 123. This is issue 916 in the PM repo. Okay, we'll hit anything on Deneb,and devnet testing and updates as well as a very minor spec release hopefully going out tomorrow, a clarification on maybe some ambiguity in by root requests just for quick discussion, and then a couple of process items from Tim. And if you have anything else we can get to it as well.

Okay, so first up what's going on with Deneb testing and Devnets. Did I see that there's a Devnet that's been launched? Does anybody want to give us an update? Do we have anyone from the devops team here? Did I start the call too early? Trying to train yall to show up on the hour. Okay, lets see we will table that for now. Any testing updates worth discussing today?

**Mario**
Yeah I can I can talk about the hive updates. There's been no major issues found so far, just a couple of ones but these have been mostly test related but so far the three consensus clients that I have tested are working correctly, no major issue so far. I will keep just adding test cases in the blobber side, and also in the builder side to see if I can find anything, but so far not nothing worth bringing up.

**Danny**
Okay 

**Mario**
And another one is maybe after, I'm not sure how long it would take us but I think probably this week or next, we might launch some equivocation tests on the devnet, with the blobber. It's basically ready but I guess that Paritosh would like to have the devnet more stable right now, before launching any attack testing.

**Danny**
Makes sense. Pari you want give us update on devnet?

**Pari**
Yeah unless you want do initial devnet updates?

**Barnabus Busa**
Yeah 11, we did a finalization kind of we took one third of the network off because we had to recycle the our machines for devnet 12, and we found a couple of bugs and a few clients. I'm not sure if there is here to discuss that, another thing is devnet 12 is very stable right now. We just started running blob to and yeah they now have blob 11,12 and all of the clients are onboarded except some.

**Pari**
Yeah I think we found like a exit related issue on devnet 11, as well as something on Reth. There was also an interaction between Nimbus and Reth that had an issue in devnet 11 but hey're all being fixed right now. So we probably keep 11 up until they're fixed and then once that's done we'll reproduce all, we try reproducing all the issues on 12.

**Danny**
Was that the finalization the bug with respect to the finalization issues was that on 11 or 12?

**Pari**
11. Okay but I don't think there was any finality related issues in itself it just happened the same time we submitted the exit so we assume they were related they weren't.

**Danny**
I see. 

**Barbanus Busa**
The thing is the exits would have probably been handled fine but Nimbus would have voted on incorrect it would have just said were invalid and maybe it have for away we don't really know what would have happened if have been no non finalized state.

**Pari**
Yeah and just to clarify the issue is not like a mainnet related one at all it's scope to just enun testnets. And the other topic we wanted to bring up was um now that we have devnet 12 and it looks like it's forked without any fanfare, should we start planning Goerly shadow fork, and we want to know what sort of timeline we can plan for that.

**Danny**
Yeah, does anybody have any thoughts on that? I guess what importantly what's the Prism timeline look like to getting on devnet 12? Is anyone from Prism here? We might have lost Terence because of the time change. It's now 6 a.m. Preston? Do you have any perspective on Prism's readiness for devnet12? 

**Preston**
Hey yeah I'm not totally sure exactly on the timeline. I think we're still a few weeks away. I have to check with Terence and follow up with you guys. 

**Gajinder**
I think on the Dencun call they said that they were two to three weeks away.

**Preston**
Yeah that sounds right.

**Barnabus**
Is it wise to …the shadow fork then? Without Prism?

**Pari**
Yeah I'd also wait for Prism before we do the shadow fork.

**Barnabus**
The shadow fork...before Christmas?

**Tim**
Yeah we should definitely do at least one before the end of the year I think. And yeah.

**Danny**
Mario is asking what's going on with timelines on Prism. Preston or do you have any perspective on what the major hurdles are at this point?

**Preston**
Hey, I'm not totally sure. Yeah okay what it was I think we're yeah I don't know I have to follow up offline.

**Danny**
All right we can get Terrence or ? to give us an update in the discord. 

**Pari**
In the meantime what all do we want to see on devnet 12, I know Mario spoke about adding blobber and doing some equivocation stuff, we're going to be doing that for sure we'll submit exits deposits. There's already blob spam, anything else that we want to do, any other scenario?

**Danny**
Assuming we'd run a slasher as well?
**Pari**
Yeah we definitely we do slashing as well.

**Danny**
Okay and something Mario probably said this but just the equivocations with just the sidecar headers will be like a kind of new path for the slashers to pick up, getting messages from that gossip topic exclusively so that would or those like potential multiple gossip topics so that'd be interesting.

**Barnabus**
Which of the clients slasher right now?

**Danny**
I believe Lighthouse and prism have a slasher.

**Pari**
That…something 

**Pawan**
Yeah that was just a question we had as well does the slasher need to be updated or is it just assumed if Lighthouse is able to track the chain, it can also produce the new slashing proofs?

**Pawan**
Yeah Lighthouse the thing that we have running on devnet right now it does include the blob headers from The Blob site C into the slasher as well so we should be detecting any proposal slashings that come through the way of blob side car as well.

**Danny**
Cool well we can give it a test shot. Yeah I mean if we have time doing you know non-finality, taking portions of the network offline and that kind of stuff is always a good, see what's going on. Also if we're going to be running devnet 12 for multiple weeks it might be worth knocking on a couple l2s doors to make sure their stuff if they've been doing development work, works on it. 

**Barnabus**
Yeah I think we're going to be running probably end if will take another two weeks to get on boarded I don't see a reason to relaunch it during like the Christmas week so 

**Danny**
And what's our Mev boost Builder situation on devnet 12 look like?

**Barnabus**
We have 225 LS running, it's only three nodes but they seem to be somewhat okay. We don't have ? working because is doing some Reth? on that so that is currently on halt.  So we don't have many two productions so local bus are preferred over building blocks as soon as we have running ahead then I think we're going to see a lot more M related too.

**Danny**
All right anything else on devnets and testing? 

**Barnabus**
We have the channel so maybe he can discuss the Nimbus block that was covered on devnet 11?

**Dustin**
Yeah sure so Nimbus essentially was not using the correct fork to validate voluntary exit messages on not the state transition but the sort of integrating blocks into its trusted database, so that ended up stalling progress in it for devnet 11, and so there's that and there was a smaller issue that kind of jointly Nimbus and there was a Nimbus Reth kind of, both had issues there but that was much less serious. This is a consensus issue but fortunately only to them.

**Danny**
Is that something we can catch in the consensus test vectors or is it a bit too stateful for that?

**Dustin**
Well that's the issue. That was my first instinct as well and I think the latter. At least this is or say because of Nimbus’s architecture, it's the latter because the state transition function is actually correct so when I got the state and block the prestate and the block and just we have a ? analog, it applied correctly, because the state transition function fixed to spec compliant, but there's an optimization that Nimbus has that all the clients have, is batch signature validation, and the way that's implemented is outside the scope of this, the state transition.

**Danny**
Sure.

**Dustin**
And honestly that's probably going to be made that way for this part of it, it varies a little bit but it is interesting question in general where the architectural boundary should exist with any of these things, but I think stateful is a good example and in particular what happens here is that by the nature of what it does is it collects signatures across the entire block like all the signatures in the block.

**Danny**
Right.

**Dustin**
And this is something that they would end up being attention between performance and sort of test coverage which we already see by the way like the epoch transition. Lighthouse has published a while ago this thing about…

**Danny**
Optimized version.

**Dustin**
Yeah and right now there's a really obvious tension between the test coverage right now. If you do that then you lose a lot of test coverage unless you very carefully, this is why Nimbus hasn't done this as much only some because to achieve that level of performance means losing a lot of the test coverage of the individual sort of components of that in the consensus spec tests. Here we made a different decision and it ended up biting Nimbus I guess in this case but where the  performance was not feasible to leave on the table, for the epoch it is right for the…

**Danny**
Right. No I understand. It'd be interesting given as the consensus layer is further integrated into Hive and we use additional tools like Kurtosis, if we can try to capture some of this in there, a bit further upstream or downstream, whichever your perspective is.

**Barnabus**
We ? because it takes a long time for an exit or deposit to take place, most of the time.

**Dustin**
But I would agree though with the idea of further testing, or I mean obviously more testing is always good, but more systematically figuring out how to incorporate more client functionality into tests that are run and maybe more automated ways, whether it's Hive or Kurtosis or something else, and I mean there are practical challenges there, obviously, with, I mean Docker image building and etc. I mean just timing wise but these if can be figured out or things can be factored well so that more of these tests can be run I think that would be definitely useful. 

The other challenge here and this is something that is worth, is like how standardized, and this is actually I think maybe a I don't know policy, or you know this is not just like a software engineering question, is how standardized should the behaviors be. It's been observed before in a number of context that all of the client you know as kind of table stakes they all correctly pass the consensus spec tests, they always do with all the devnets and testnets, and anything outside of that is a little bit up in the air and so is that desirable or not. 

Or are these things that are intentionally kind of left ambiguous or are these things you know what should be really nailed down by a spec versus what should be left deliberately vague. So I mean 

**Danny**
Yeah I agree with that but still some of these like when the statefulness kind of gets in the way of processing valid or invalid blocks, I think it's still like spec, you know it's hard to argue that if you're doing batch operations that they should fail when they pass individually, but I agree that when you get to the edges, especially when you start talking about like responding to network things and stuff that it's really hard to throw that all on conformance test. I definitely like, I don't know if we've had a consensus, we probably have maybe not live, but like most of the issues around consensus have been around things that work in isolation but then don't work in a more stateful environment regarding caches optimizations, and that kind of stuff.

So at least like some sort of like more bulk operations in Hive or Kurtosis.

**Dustin**
I'd agree with that I mean I think another possibility is the gossip validation and I think it's important, so really crucially at least for me there's a hard boundary between tests which depends on network and tests which don't. Network dependent tests are key and fail I'm sorry but they just do and I do not I want parts of at least the Nimbus and in the Nimbus definition kind of push for this actively where they never ever ever fail because of network weirdness or it can't access some external server, other tests that's fine and so in terms of the EF test I think that's a useful boundary as well and what I would also push for, what I'm getting at here is to say that the things like gossip tests there are many tests which actually could be done, there are bulk tests here, there more integration tests, but they do not depend on external access.

I would say it's a reasonable assumption and we're just hear it call so we can if somebody disagree with me tell say so, but I think that people have or can have refactor things so that there is something like a gossip validation function, there's some Oracle in the software that can say is this gossip message good or bad or ignore or reject. If this is the case given and that function probably is not doing any network calls itself and so I think one possibility is having a more formal test suite around gossip validation. 

The only thing I would say there is that what Nimbus does deliberately and I think is I think a deliberate ambiguity is the reject ignore conditions by reordering the tests for performance reasons, you can get different versions of those difference is the purity scoring and that we'll just take that, that's fine but if it starts becoming well no you failed the test, because you didn't put the signature verification last, well…

**Danny**
Yeah like you might have to you might have to wrap ignore reject is the same for this purpose.

**Dustin**
Yeah but otherwise I think that's an example of what you're talking about where I think…

**Danny**
Even those can be moderately stateful. I mean at least time like what is the system's time becomes a condition in there that is not part of the state transition, that's stateful, there might be a couple other things in there though you need to be careful about.

**Dustin**
That's true we deal with fork choice though no to some extent like with the fork choice test and…

**Danny**
Yeah it had to be baked in there so it could be baked in there although some of the like the conditions or did you see this other message so it's like you'd have to give a suite of messages rather than just a pre-state to so it is a bit more stable…

**Dustin**
I’m actually wondering…and the other part is ignore is so I think reject can certainly be tested I haven't really heard that but…

**Danny**
Because that should be just straight up…

**Dustin**
Yeah yeah right so I mean by their nature there's once reject always reject on all of that stuff so that should be I I see what you're saying though nor actually is a real problem and I would say probably I would say out of scope I would suggest for a first version of these, it's just too picky, and it also resolves the ordering issue to some extent of the test ordering issue if you only pay attention to reject at all, but but it's yeah anyway I mean that's an example, there are others I don't want to go too down that rabbit hole too much but I for one can find other examples where I think one could expand the scope and certainly in Nimbus that by the way would capture a lot of the batch validation stuff.

**Danny**
Because 

**Dustin**
Sorry go ahead 

**Danny**
I was questioning whether reject is even valuable if it's because reject are probably deterministic with respect to kind of things that would be caught in the state transition? It's really those ignores that are probably more…

**Dustin**
Yeah, Nimbus handles this differently though I can't speak for any other clients obviously but the Nimbus will tend to use the batch validation at that layer even…

**Danny**
I see.

**Dustin**
So at least for Nimbus it would be a useful kind of additional set of testing that it is stateful in a different way, but I see what you mean that it probably won't in general catch a huge amount, so that may not be the highest roi thing to add, there may be others I don't want to, that was just kind of a spur of the moment thought notation, but I think in general it was a way of saying I do agree with you that finding larger more stateful chunks if that state can be managed. 

What another hazard or risk of this I will suggest is and for people who have seen I know this is not the ACDE call but for people who have seen the execution tests, they take significantly longer to run in general, and in their complete vastness, and part of the reason is there's several reasons, there's more forks and all that, some part of it is just that they are they kind of lean much more into this idea of doing these integration tests with full on states that take a while. They're slower tests, what the tradeoff there is CI wise for people, I don't know, but that's another consideration.

**Danny**
Yeah okay, how or if and how should we continue this conversation; I know we've been ramping up CL stuff with respect to Hive, and also digging a bit deeper into some of the stuff we can do with Kurtosis, so maybe it's just a matter of making sure some of the issues that we do run into are documented so that Mario and others are aware of them and kind of can see if they can be integrated well, but maybe there's something else we should do here.

**Dustin**
I would say in terms of like things which are not sort of to be completed on this call but sort of having a complete set of what are the protocol actions that need to be tested, so particular for here what triggered this was in the wild as it were, Deneb exits. Like that, that was the new thing in devnet 11 that which approximately triggered this, so whether that was intentionally chosen for this purpose or not, like I'm not sure the previous devnets could have done this, like we've had previous Deneb devnets, but being more systematic maybe about saying like what are all the possibilities?

**Danny**
Yeah and seeing if we can catch some in some sort of CI instead of having to remember to trigger them on a devnet and catch them a little bit later. Okay does anyone from testing want to chime in here or and Dustin is there anything to document on your end so that we better understand this or is it simply triggering a bunch of exits on Deneb? Or is there like more details that are worth making sure that the testing…

**Dustin**
I don't think so I think it's basically just more and more exits on Deneb… not quite yet…I haven't made the pr for this yet but yeah like and so it'll just kind of pointlessly stall Nimbus until then but that's certainly my priority and as soon as that goes out and is running on the devnet 12, or 5 or anywhere else I think yeah then that bag sense yeah…

**Danny**
Cool and I don't mean to hound on this particular issue it's much more just like us all being mindful of that there are these like stateful paths that we need to be trying to make sure we test and think about how test so 

**Dustin**
No I appreciate that absolutely and I agree with it and it's like this is and as people as a system becomes more mature and people optimize more and sort of bake more assumptions kind of just over time into the software, deviate from the python pseudo code spec increasingly, I mean gradually but this will become, I mean obviously its just been happening from the very beginning since the merge, but this will become more typical.

**Danny**
So Mario you had your hand up do you have anything?

**Mario**
So I think a write up would be very helpful and also if we can also discuss this on the Dencun Interop testing call to bring it up again and just see how we can continue. We can pick it up there and see ways that we can implement this in the tests.

**Dustin**
Okay, so just like a hackmd or when you say right what would you like to see, for the write up, what are…

**Danny**
I think a quick hackmd, the high level things that happen on the network and anything that's maybe interesting to document with respect to Nimbus like that that was a bulk verification path or something because then that that might imply other types of bulk verifications that we should be… 

**Dustin**
Right I see okay right how what can be generalized from it, because obviously this will, I will say it's not solved quite yet, but let's say resolved that the mystery is has been cleared so sure okay.

**Danny**
Pari do you have anything?

**Pari**
Yeah I think most of what Mario was saying as well but we'd probably be talking to see which parts we can put into Hive and which one we want to put into Kurtosis. One of the things over the last few issues we've seen is that we just need some tool that can systematically execute a certain number of integration related behaviors, so exits, withdrawals, make sure there's a MEV block produced by every client, make sure there's a block produced by every combination, and so on and that sounds like it's something we can just integrate into Kurtosis, so we probably solve it by a mixture of Hive and Kurtosis, but yeah we we'll be discussing yeah that's my intuition an update.

**Danny**
Okay anything else on this?

**Pari**
Not from me.

**Danny**
Yeah cool, all right cool. So we'll keep it kind of in testing land, but if some broader progress is made on strategies and stuff here, by all means bring it back to all core devs. Terrence you hopped on, we're trying to get a perspective on Prism timelines and any kind of major hurdles that still exist and also if there's anything we can do to help.

**Terence**
Yeah sorry I was a bit late so I guess my apology that we underestimate how many people were actually like offline and on vacation this month that's why Prism is slightly delayed because of devconnect and like the Thanksgiving week, but yeah, we ended up redesigning a bunch of stuff, because of devnet 12, so we added a new fire storage layer, and then a new caching layer and that's why it's taking a while because without those like major revamp, if we just implement the pr as it is it would have been faster but yeah I we're still like, I would say two weeks away, but then like again like we can join devnet 12, which I think he just launched this today as well so yeah you don't have to wait for us but yeah we will join when we're ready, probably in two weeks. 

But yeah we should be ready for the testnet once it's out but yeah that's pretty much it.

**Danny**
Okay thank you. Any questions for Prism before moving on? 

**Pari**
Yeah if you guys have a branch whenever you're ready just let me know so yeah I can have some integration tests.

**Terence**
Yeah, sounds good, thank you.

**Danny**
Okay anything else related to testing and devnet? 

**Pari**
We have a tool that can reliably do reorgs now, the question is just does someone have an issue that was triggered by reorg that, we can toss in the tool to see if it can catch it plus that issue being fixed, so we can see that it can't catch it after it's fixed.

**Danny**
Right so like an old commit as well as old release and a new release?

**Pari**
Yeah.

**Maintainer.eth**
?

**Danny**
Anybody have a reorg related issue from the past that they can point Pari to? If you can't remember, can you please ask your team and then knock on Pari's door, and Pari, maybe drop this in the Discord for a broader ask? 

All right, anything else related to testing and devnets?

**Tim**
Not quite the devnets but we're going to put out the Goerli blog post today around Goerli validators being exited the later of three months after before or one month after mainnet, last call if anyone has thoughts comments on that, but otherwise the post should be up in the next hour.

#### Research, spec, etc [Add sentences about order of ByRoot responses consensus-specs#3544](https://github.com/ethereum/consensus-specs/pull/3544) [37:26]( https://www.youtube.com/live/s3jIn3ot57g?si=t2q7AGuwUEtqhBhz&t=2246) 

**Danny**
Great okay. We have a minor spec release that is slated to come out tomorrow. This primarily fixes some testing in fork choice testing as well as we're working on getting this when clients can serve block and side cores by root clarifications on like May should etc.. I had a review I put up last week and then did not click submit so it's a bit my fault, yesterday I realized that so we're doing some final stuff here.

I don't believe there's anything shocking, but hoping to get it done today, and get a release out tomorrow if not, release might come Saturday, Sunday, Monday. Are there any comments on this issue 3551 that would be kind of the most, we did talk about it on a call, a couple calls ago, so I don't think there's any surprises but I just wanted to give you a chance to service any comment or concern before this is finalized, otherwise this is not breaking, with respect to the devnets, so it won't affect, you can and should roll out changes with respect to devnet 12, but it's totally interoperable on the networking layer. 


Okay, there's actually one other clarification that might make it in there. This is PR 3544 and I wanted to just make sure that this is capturing what is actually happening, so it doesn't, the by root request don't actually say that if you're responding to root a b c that you would need to send messages in that order. I would I've assumed that is certainly the case that you know you're matching root zero to message zero root one to message one, you're not doing a like, you responded in some random order but I might be totally wrong here so before this goes in, does anybody have a comment on whether these are supposed to come in an order? 

**Justin**
Also maybe some clarification on duplicate requests, like the same route and the same request?

**Danny**
So like route AAA should not be you're saying should not be valid or yeah or maybe you should just return the just A once?

**Justin**
Yeah, exactly.

**Enrico**
Well if that is a set then the order should not considered, and also the duplication could be removed but if we want the order, I feel like duplication should not be allowed and then we respect the order.

**Danny**
Yeah well the order can also be weird right, because if it's A B C, and you don't have a you can respond B and C and which is the correct order by some standard but you still have to like do the matching properly right?

**Enrico**
The verification would be much more. Yeah.

**Danny**
Is anyone aware of how this functionality is actually handled or is it kind of ambiguously handled and maybe there's different functionality across clients at this point? 

Okay it doesn't seem like this is top of mind and that the people on the call have clarity on how this is currently done. We'll drop it in the discord and try to get clarification from some of the more networking folks on teams and get this clarified soon. Obviously things work but some of the ambiguities here might be cause of issue in weird edge cases, and it will be worth clarifying and cleaning up.

All right anything else on this one? this is not going to go in the release tomorrow okay any other deneb items or just general spec items? 
#### [Two process items from Tim](https://github.com/ethereum/pm/issues/916#issuecomment-1832882659)   [42:49]( https://www.youtube.com/live/s3jIn3ot57g?si=YSKc_Pv18l_egQCs&t=2569) 

Okay Tim had a couple of small items related process, Tim? 

**Tim**
Yeah so smallest one, adding fork folders to the PM repo. So we currently have things like devnet specs and whatnot like live randomly on hackmds, we've had these main net checklists for a few of the forks that also are living in random folders, so my suggestion is every fork we just create a repo, sorry every fork we just create a folder in the PM repo for that fork and put all those things there and when the fork is over we just move it to the archive folder. 

So pretty uncontroversial I think but if anyone…

**Danny**
No even standard files that go in it it's just files are relevant?

**Tim**
Yeah yeah so I'm not saying we have to create you know like a mainnet or anything yeah yeah but just we tend to and now they like either end up in hackmds or random places which is like a default place for people to shove stuff that's relevant to the fork that we're working on and we'll sort of get the and usually we don't struggle to find them during the fork but it's kind of nice that this way we'd have them you know in that repo forever After the fork yeah sorry eth panda op.md is not random but the and I mean even if we keep using hackmds we can just even link them from there and you know um know that this yeah…

**Danny**
You could drop a doc that said relevant notes if you didn't want to put it in there.

**Tim**
Yeah um so that was the first I just wanted to wait until I merged it to see if anybody had comments but it doesn't seem like there's any objections. Next one um so the other thing that's kind of weird right now is there's nowhere to know what's actually in a fork especially for combined forks um so on the El we have things in these random little markdown files so this is the one for Cancun obviously on the CL, the beacon chain spec has a list of the eips, but there's not like a single place where we have like these are all the eips going into the fork, the two place where they're listed for half you know each half of the network are kind of hard to find and like not necessarily obvious, so my other proposal is we bring back mea eips to just list what eips are in a fork so we used to do this for some reason, we stopped a few years ago I forget why yeah right eth panda Ops, the eth panda Ops hacken is maybe the easiest place to find all the eips but this is something that people on the outside aren't necessarily super aware of.

The other place the eips end up being listed at the end of their process is like on the hard fork blog post, which is kind of weird to have to rely on the blog post to like figure out like where to look at in the EIP's rep in the specs. So my yeah my proposal would be we add a meta EIP, literally just as a list of the eips included in a fork. If we know the fork is going to be coupled uh like Deneb and Cancun we just have a single EIP so we don't have the duplication of eips like 4844 4788. If we don't know that the forks are going to be coupled we can just have one you know per side and worst case if the forks do end up merging together we just merge to eips or something and we can either do this like right now for Dencun or you know start for the next work but it does feel like something where um yeah having a single list of eips for the fork somewhere is valuable, especially now as well that you know if we split the eips and ERC repo we can imagine uh starting to add like more custom fields to the eips and whatnot and aggregating them into a single fork EIP.

So any thoughts on meta eips and whether we should do one for dencun or just wait to the next fork? Okay one comment to do at ASAP. I can get it done this week um okay two yeses  that's all.

**Danny**
I'm not I'm certainly not opposed, we're happy with like how we bundle things into the specs on the 

**Tim**
Yeah I'm not saying we should remove them 

**Danny**
I know but a meta reference somewhere especially because of the cross layer makes sense to me.

**Tim**
Yeah, and I think I can do this now but I would link the specs assuming the bot lets me, so you know saying like these are all the eips in the fork this is where the fork is you know defined for the CL, this where the fork is defined for the E type of thing. Okay so I'll draft it this week and then this is urgent and just something for consensus layer folks to start thinking about if they want.

So we have on the El side this weird status of like considered for inclusion for eips which are things that basically client devs think we should maybe do but end up being like a superset of what goes into a fork, it's not clear to me if like having the status is a plus or not. In the past it was helpful because we if somebody comes on the call and you know they want a signal of like should they keep working on this EIP or not, this is like a soft signal we can give them, but it's also let the confusion of like, okay now we have this big list of stuff we might do or might not do, and so I was thinking on the El side either we should remove this, if it doesn't add value and just adds you know confusion, or if we keep it you know maybe makes sense for it to also be like used on the CL if people want.

And again now that we have the like split EIP process you could imagine making this like a a status of an EIP if we keep it where it's like you know something gets proposed for a fork it can be signaled directly in the EIP that it's being proposed. So I have a link to The eth Magicians in the agenda and there's a bunch more context there but yeah I don't think this a decision that needs to be  made now, but as we start planning the next fork figuring out, like do we want to keep this state that's higher than random ideas from random people but prior to accepted in the fork, which is roughly what CFI was but I think if we yeah it might be worth getting a more formal definition and like updating it, if both sides want to keep using it. Yeah that's all I had. So I'll get them in an EIP done and I'll merge the fork repo PR.

**Danny**
Well any other questions or comments for Tim?

**Pari**
What's the temperature check on the idea of putting fork fields on all of the eips and having placeholder fork fields for proposed and so we can you know filter eips uh by that field to see when it was implemented?

**Tim**
Yeah I'd like that personally on the eip side um I'm not sure what's the best way to do it but it would be nice to be able to click you know Berlin or yeah capella and get all the eips that were in that.

**Danny**
Anything else on this one? All right any further comments our discussion points for today? Okay great. Hope to see you all very soon thanks everyone. 

## Attendees
* Danny
* Paritosh
* Barnabus Busa
* Ayman
* Giulio
* Mario Vega
* Danno Ferrin
* Stokes
* Justin Traglia
* Tomasz Stanczak
* Mikhail Khalinin
* Bayram
* Guilliaume
* Pooja Ranjan
* Andrew Ashikhmin
* Preston Van Loon
* Tim Bieko
* Phil Ngo
* David
* spencer-tb
* pop
* Dankrad Feist
* Pawan Dhananjay
* dan (danceratops)
* gajinder
* Tomasz Stanczak
* Enrico Del Fante
* Marcin Sobczak
* David
* NC
* lightclient
* Matt Nelson
* Trent
* Ben Adams
* Peter Garamyolgyi
* Fabio Di Fabio
* Daniel Lehrner
* Hsiao Wei Wang
* Ignacio
* Ben Edgington
* Mehdi Aouadi
* Ahmad Bitar
* Saulius Grigaitis
* Fredrik
* Lukasz Rozmej



