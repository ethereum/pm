# Ethereum 2.0 Implementers Call 64 Notes

### Meeting Date/Time: Thursday 2021/05/20 at 14:00 GMT
### Meeting Duration:  1.5 hours
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/218)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=A1L7wLYAqnM)
### Moderator: Danny Ryan
### Notes: Jared Doro

-----------------------------
# **Contents**
  - [1. Client Updates](#1-client-updates)
  - [2. Altair](#2-Altiar)
    - spec and testing
    - engineering progress
    - planning
  - [3. Research Updates](#3-Research-Updates)
  - [4. Spec Discussion](#4-Spec-Discussion)
  - [5. Open Discussion/Closing Remarks](#5-Open-DiscussionClosing-Remarks)
   



Change merge call time to directly before the Eth2.0 call.
This change takes effect next meeting.

-----------------------------
**Danny Ryan**
We are going to experiment with moving the merge call right before this call instead of offset weeks. 
In an effort to help with people in different time zones, stack some calls.
The first time we will be doing that is two weeks from now. It might be a long stretch, we'll give it a shot This call is usually short enough that I don't think it should be too bad.
Lets go ahead and get started
  
# 1. Client Updates
**Danny**
Client updates, definitely let us know what is going on with Altair how things are going with respect to getting things implemented both from the state transition and also if you have had any change to stand up any short lived test sets with all the features.
Okay we can go ahead and start with lighthouse
  ## Lighthouse
  **Paul** 
 Regarding Altair we have been doing some successful tests with the networking side of things so switching on an off the correct gossip networks.
 It's looking good. We are now finalizing the changes to the VC.  Once we have those done and merged together we have I think a full stack so to speak of Altair. So looking forward to testing with that.
I personally am doing a pretty detailed review of Altair changes, because we are going to be merging them to master soon and I want to make sure we don't break anything now and when we hit Altair of course.
That is about it for Altair.
 Regarding the merge we shut down our Nocturn nodes. That was good, they ran without incident the whole time. Which is pretty cool so that’s thanks to all the execution clients we ran as well. Well done to them.
Published a blog post regarding 1.4.0 release which has lots of features you can find it on our blog.
  //I Cant Find Blog
  Weak subjectivity it's working for us but we haven’t got backfilling done yet.
  Interested in if other teams are backfilling to genesis. I haven't been able to find any clear information about it.
  We are not going to release until we can backfill to genesis so we can keep those blocks going.
  I am interested if there is a general consensus that we are all going to do that?
That’s it for me.

  **Adrian** 
Teku is backfilling to genesis at the moment. I would like to be able to cut that weak subjectivity checkpoint distance, but obviously that depends on all the clients not needing sync from genesis and that not being a common thing and probably having some other systems in place to get blocks.
So I think for a little while I think at least the backfill to genesis makes a lot of sense and it is not a huge ammount of disk space.
**Paul**
 Yeah ok cool that is pretty much along the lines we are thinking as well.
**Dany**  
I think the idea would be eventually to bound what the P2P layers are responsible for and have git methods for accessing historic stuff, but for now it is safe to do so.
## Nimbus
  **Mamy**
 So regarding Altair we are currently we have merged Altair the changes we have are due to the validator client. 
We are doing infrastructure changes at the moment, but we are expecting to start the initial tests soon.
 Otherwise we released yesterday V1.3.0 this has migrations guides to and from nimbus and the other clients. Something that was due for a while. 
  We have also a new comment to test the validator performance, so that people can insure that their hardware will be sufficient to handle the load of the network.
We now support official binaries for Mac OS and we also support Apple M1 so the new apple MacBooks and Mac mini.
  We have activated for everyone a pruning of the slashing  prediction database and optimized queries  
  This lead to a very significant improvement on the disk IO and speed usage of all nodes.
This will allow us to have more validators on the same hardware in particular a raspberry Pi.
  We have improved validation of attestations received from the rest and json rpc API.
So we don’t  broadcast and validate attestations when they are received from those APIs. 
 We have also improved the attestation submit transition timings to improve CPU and bandwidth usage.
 In terms of problems we have a gossip subnet working logic that was inefficient.
  Coming soon in next release and already being tested we have yet another large IO improvement.
  Regarding to how we cache state, this will be in the next release next week or in two weeks.
  That’s it for me.
 ## Teku
  **Adrian** 
  We are looking pretty good for Altair we have been able to put together the whole package validated duties are preforming and sync committee networking stuff is in place.
  The peer management was added just recently to make sure actually find peers on the subnet we'll need and maintain those connections
  We have seen that work with small networks of multiple nodes being able to finalize and preform all the duties
  Paul Harris has been putting up a whole bunch PRs for the standard rest API kind of defining the new parts of that around sync committees and to do with the different block structure and state structure. 
   There is a few them open mostly by stop of Jim McDonald's initial proposal and just putting it into the open API spec
   So that what’s reviewing for those people working on the open API stuff
  Teku's implementation of those are pretty much done the one that isn’t complete is the state stuff. 
  We got upgraded to the alpha 5 release just today. Which has the final change to sync committee in state so that needs to go into the rest API and it should be able to link.
  I don’t know if it is useful for people for us to stand up a node that is starting to just run chain. 
  I have in mind just running a really small test-net but keeping a node up with a public endpoint so we can test syncing against it since we have plenty of notation.
  If that is useful to people let me know and we can get that up pretty quickly. I don’t intend it to be an actual proper full scale test-net or anything.
  
**Danny**
 I mean if you do stand it up I am sure people will do some basic interop on it in the next week or so.
 ## Prysm
Okay Prysm.

  **Terence:** 
On the Altair front we align to alpha 5 we are passing all the spec tests regarding the state transitions.
  So now we are working on networking, VC, and the actual forking logic.
  So, we do face some unique challenges with Altair due to the lack of generics for go.
  So, we are a bit behind, but I think we can catch up pretty quickly.
  So, on the merge front we shut down all the nodes and validator instances. Great job to all the teams working on that.
  We released version 1.3.9 last week with a number of improvements. Including updated Go library to 1.16.4 
  Also the proper is using this fancy Max-cover algorithm so to be more profitable.
  We also working on weak subjectivity sync.
  We almost done with the checkpoint syncing and we haven’t though much about the backfilling yet.
  Our production optimized slasher is going to be released next week so keep an eye out for that.
  That’s It.
  ## Lodestar
**Danny** 
Thanks, Lodestar.

  **Cayman** 
On the Altair front, I think we have got  all the pieces together at least the alpha 3 release level. 
  We got some simulation testes, that test a small ephemeral test-net for a few epochs working on just a single node and then a multi node setup.
  We are in the next few days we are going to be working upgrading to the alpha 5 release.
  We also are putting together a light client prototype, currently we have a website that can demo this but it hooks to a mock beacon chain because we weren’t quite ready on the Altair side but it communicates over a custom rest API to receive sync updates and request proof we will hook it up to Altair when we are ready.
 
 # 2. Altair
   **Danny**
Nice can you share that link in chat?
 Thank you everyone it sounds like Altair progress is much progress and that things are getting pretty close most people are aligning to that alpha 5. We will shift into talking about where we stand on all that and to planning a little bit. Alpha 5 had a lot of progress and refinement. We got a lot of review on my team and some others to enhance testing and do some final tweaks to the future set.
  We are slated to do an alpha 6 tomorrow which is primarily again more testing. I think that all features are stable.
  Other than what will be the addition of this resource unavailable error code which is being discussed right here and I think we need to get a PR up for that in the next 24 hours or so before we review and release tomorrow.
  That won’t be a spec freeze, but it will be an intentional freeze like future completeness and not meddling with thing unless we get some feedback from engineering teams in the next few weeks as we are working on test-nets that something is wrong or something won’t work in production as we though it would.
  So, I think that Alpha 6 will be that intentional target and then once we stand up some multi-client interop and validate that we are all running the same stuff and it all works then we will do a freeze and pick fork dates.
So last time we discussed first half of June for short lived test-nets. End of June for forking current test-nets and the end of July or early August for that actual main net upgrade.
  I think we are definitely on target for that first half of June short lived test-nets, and a final spec release then.
  As for end of June or early July for forking the current test nets and as for target end of July early August I think we should still see how things play out in the next couple of weeks with those still being the targets. 
Other than that I think Medhi has been working on the fuzzing.
Is there updates on that Medhi?

  **Medhi**
    Things have been going quite well. With our live beacon chain I don't think it is a good thing to disclose some of the bugs we have been finding.
    We have been finding a couple interesting bugs over the last few weeks. We have meet with the relevant teams and they’re working on fixes, but yeah it has been going well.
    So we reached out to all client teams and two of them are ready for our fuzzes to start targeting Altair branches, two are not just yet FYI.
 Yeah, Things are going quite well on our end. 
 
   **Danny**
 Great so it still looks like we can get some Altair fuzzing running in June which should give us some good coverage by what the intentional fork date is.
 Other than that, is there anything to discuss with respect to Altair?
 
  **Protolambda**
 So this is not directly related to Altair but comes with the same updates, maybe there is this one PR that is open to improve the config formats.
  So that we can improve the experience of developers running local test nets and configuring their own chain. 
  It separates the presets, the compile time configuration from the runtime configuration.
  I will link the PR I am looking for feedback so we can get this right.
  
  **Danny** 
Proto is this something you are intending to get into the release tomorrow?

  **Protolambda**
Yes, so it was announced earlier in the chat ideally if we get enough feedback we can put this in the release tomorrow.

  **Danny** 
For the engineering teams they don’t have to change anything immediately they still have same values, but it does allow them to over time migrate to support stronger compile time constants and also have configuration in a separate place to match the spec over time.
  
  **Protolambda** 
Right. So, the variables are fairly compatible there is no change there and no change to the consensus.
  It’s really just focused as improving the experience configuring of the clients.
  So, think of all the configuration variables that effect typing or that go into that compile byte plan of a client. Those get separated from the runtime configuration so say for example if you run a nimbus client on a custom test-net and we adopt this kind of configuration separation then we don’t have to recompile the client for every different test net.
 
 **Danny** 
Right. But if we get this out tomorrow, does it put any required immediate work on clients or not?
  
  **Protolambda** 
The remaining open question is the change to the API or not? there is this one endpoint that returns the configuration. 
  What we could just do is keep it the same and return the union of compile time and runtime configuration and then in the future we could either create another endpoint for the runtime configuration specifically.
  Or just drop the compile time part of the response.
  
  **Danny**
Gotcha. Okay It looks like we have gotten some feedback from a couple of client teams, if you haven’t taken a look please do.
  I think this generally makes things cleaner on your end over time, and that’s kind of the intention.
  So, we are just looking for sanity check thumbs up from various teams.
  Okay great.
  There has also been some discussion about this resource unavailable return code that I did share this 2414.
  I am going to catch up on that right after this call jump in and try to wrap up this conversation very soon so we can get that in the next release.
# 3. Research Updates
**Danny**
as we are not having a merge call this week or next week, it would be the following week.
It would probably be a good time to give everyone a quick update where we stand on rayonism and the merge and things like that.
Mikhail, Proto would you want to give us an update?

**Proto**
Regarding rayonism we just closed the test-net yesterday it was a success. 
We had 4 consensus clients on the test-nest 3 execution clients, but going forward with the merge what we really need is to rebase on the production calls and implement the proper API separated from the user layer we need this specification for the merge transition.
This is something Mikhail will continue with. 

**Mikhail** The plan is to work on the transition in the meantime and also there is work on the state sync that is happening as well by the Geth team which is great.
While the clients are focused on Altair and London we will have time to do this research and spec work and get back to the merge after Altair and London.
Another probably bigger merge teste net with the transition process, with the state sync, with the other probably tiny changes we will have on the research side.
The major things that are going to happen is the transition process figured out and tested in the local test-nets and sync process as well that is an important one.
Also there is the discussion about the consensus API, but this is more technical than research so it should also be finished by that time.

**Danny** 
Question about that. In the initial state sync work do you think that API is sufficient or do you think there might be an additional endpoint that needs to be added for the communication on that or around that?

**Mikhail**
 Yeah, it’s like according to the current state of the arts the (24:37??) message is going to be enough, yeah, the current message sent is going to be enough for state the sync but we will see when it is finished.

**Danny** 
Right, Okay great.
Any other questions, comments, discussion points on merge progress before I move on?

**Mikhail**
 I just want to say thanks everybody who participates in the rayonism and in the nocturn which was the last dev net. It was great a lot of excitement and progress had been done.

**Danny**
 Yeah, very much agreed.
Okay other research updates for today?

**Vitalik** 
I have added the Altair spec to my annotated spec repo. If anyone wants to look at that any feedback always welcome

**Danny**
 Great Thanks Vitalik.

**Mikhail**
Also One thing we might have missed that sharding work will be happening after the rayonism.
(26:24??) will be working on the implementation and proto will probably work on the spec side as well.
Also, withdrawals we have been planning to deploy the withdrawal dev-net as well.
So it is still planned, but it will just happen outside of rayonism frames.

**Vitalik** 
Is there a good place to find a spec for the withdrawal design you will be attempting?

**Mikhail**
Yeah I will drop it in the chat.

**Danny** 
Okay any other research related items today?
-long pause-
Okay great.
# 4. Spec Discussion

**Danny** 
General spec discussion, testing discission, open discussion anything else people want to chat about before we close.
# 5. Open Discussion/Closing Remarks

**Hiao-Wei Wang**
 I have a proposal about lining the Altair block epoch with the sync committee period posting the PR here.
I would like to hear the opinions from the client devs so its all the authentic consideration but also ensure that we won’t start with too short a sync period at the beginning of the fork.
But the drawback is that it might be more difficult to coordinate a reasonable forking block time for people, but I don’t know this is a global project, so let us know the perfect time for everyone anyway.
So open this PR for discussion it is not urgent. We still have time to discuss the block epoch, but just thought to raise the issue here.

**Danny** 
Is the primary benefit to not have a truncated sync committee period? Because the transition function can handle starting anywhere, right?

**Adrian**
Yes it does.

**Jacek**
I think one other convenient constraint that I have been thinking about is that we store I think its 8192 roots before we accumulate them in historical roots.
So it might be convenient to place it on the 8192 boundary.

**Danny**
Interesting so you have the same type throughout the accumulated chunk?

**Jacek**
Yeah exactly.
I mean this is related to something I have been thinking about that if we have the block root in there in a separate accumulator, we can actually verify the entire history of the Ethereum2 (30:35??) with exact layers.
Which means it would be useful to identify like a chunk of 8000 blocks if we ever want to discuss alternative archive solutions for example.
So, one can imagine that if the convenient chunk of blocks to keep together and identify via their accumulator hash and then you could actually verify it with any state.
You could actually verify the whole Ethereum history from any state if it were that way.

**Danny**
  So, you are saying historical roots rather than combining block and state, keep them separate?
  
  **Jacek**
Yeah, exactly so you would have historical block proofs it would be in the Merkle root of 8000 blocks instead of as it is now 8000 blocks and state.
  I mean yeah with the state you can’t actually verify it, because the state root changes for the slot as well so you actually have to apply the block if you want to run full verification on everything that lead up to today.

**Danny**
  Right someone can’t give you a bunch of blocks and you can verify them you have to actually have the associated state root given to you or calculate them?
  
  **Jacek** 
Yeah exactly that would be super convenient for large archive nodes or putting Ethereum on BitTorrent whatever right. 
You would have this very natural identifyier to go by and it would actually be part of the state.
  I have kind of wanted to get this for Altair, but I haven’t had time to make the PR.
  It’s a very simple change borderline trivial, I could type it up today or tomorrow, but then there is the freeze right?
 
 **Danny** 
Yeah, I guess the next step is definitely typing it up and putting it out for discussion.
 
 **Adrian** 
I guess just coming back to Hiao-Weis original question around sync committee alignment, we found with the validated client that there was some interesting corner cases when it didn’t line up, but not particularly difficult to deal with.
  So Teku now handles the fork starting in the middle of the sync committee it just seamlessly goes through it just doesn’t really care.
  The main thing is just being aware in a few places, when you are looking for a state that you can use to calculate the sync committees from or get the sync committees from you need to make sure it’s actually in the Altair fork and so there is just one more min/max type condition in there. 
It would make  sense to not to be to close to the end of a sync committee period.
Like I think we should aim to align it or at least at least be towards the middle-ish rather than necessarily being right at the end.
But we know those first few slots are going to be fairly awkward anyway so it’s almost worth kind of abandoning that first sync committee period.
Give it 6-10 epochs of setting up networks and so on so the next committee starts off and does the right thing.

**Dankrad** 
Sorry, what difference does it make when it at the end of a sync committee?

**Adrian**
 It’s just when you first hit the Altair fork that’s the first time you know the sync committees until you have to go and find peers that are also on those sub-nets. 
People take time to broadcast all the metadata.

**Dankrad**
 Worst case it just fails. What’s the big deal? you just loose a few hours of sync committee.

**Danny**
 Also Adrian the first two sync committees are actually the same.

**Adrian**
That’s true.

**Danny**
So, in that case it doesn’t really matter because you see stability on the next side of the committee threshold as well.

**Adrian** 
So in that case it probably doesn’t matter at all when do it, cause you basically have a double long sync committee.

**Danny**
 Right so they get a change to find each other.

**Adrian**
And the first few epochs or however long it winds up being is always going to be a mess.
Because you are not going to find peers, so your signatures are just going to be dropped on the floor pretty much.
But once that network stabilizes then it should pick up from wherever it is.
The one advantage we had is that our validator client knows about the sync committee periods and we took that into account when we are calculating duties.
So it was then very easy to ask for the last epoch because the standard API is epoch based when requesting sync committees.
If other people take different approaches to scheduling their duties then maybe that has different impacts and engineering wise might help.
Otherwise, I don’t think there is any great pressing need to align them from my view.

**Dankrad**
 I think having to align it will just make for coordination so much harder. You’ll find that rapidly you’ll only have a few windows every few weeks or something where you can do it.

**Adrian**
Hiao-Wei was your only concern just that it was kind of untidy or was there something else on your mind?

**Hiao-Wei**
 Not particularly, so just wondering if people think this is a good benefit if want to remove the half period of the beginning, but if it’s not a big problem for the client devs then I don't have a strong opinion on it.
Also, it was filed in the previous PR feedback so just wondering to get feedback from you guys.

**Dankrad**
 I mean clients could just ignore the half period at the beginning. I don’t see that as a problem.

**Danny** 
But I mean if it wasn’t too bad if it was pretty easy to exceptional logic and the fact that it’s the same committee on both the first two periods.
Those would lead me to believe that it’s probably fine to just leave it as is and be a little bit more flexible on the fork.
**Hiao-Wei** That’s good to know, So yeah for the sync committee period thing is fine to just not totally ignore it, but we don’t have to make it to align in the state.
But we still want to still consider the accumulator?

**Danny** 
That one’s even tougher, because that’s like 32 days or something which would make it very difficult to align things.
I don’t know maybe we should talk about that offline unless people feel strongly about it one way or the other.

**Hiao-Wei**
 Sounds good to me.

**Danny**
Cool.
Any other items for discussion today?
I mean I would suggest in the coming week or so to try some basic interop stuff I think that is probably the next natural progression in this thing and then we can stand up stuff that is a little bit longer lasting.
We will talk on the internet and talk to you all in two weeks.
Thank you.
## Date and Time for the next meeting: June 3, 2021, at 1400 UTC

## Attendees
* Hiao-Wei Wang
* Danny
* Pooja Ranjan
* Micah
* Adrian Sutton
* protolambda
* Mikhail Kalinin
* Paul Hauner
* Mamy Ratsimbazafy
* Jacek Sieka
* Mehdi Zerouali
* Alex Stokes
* Ben Edgington
* Ansgar Dietrichs
* Cayman Nava
* Terrence
* Carl Beekhuizen
* Dankrad Feist
* Parithosh Jayanthi
* Leo BSC
* Aditya
* Raul Jordan
* Vitalik
* Zahary Karadjov
* Nishant
* Lion dappLion
* Preston Van Loon

## Links discussed in the call (zoom chat)
From Danny to Everyone: 03:09 PM
https://github.com/ethereum/eth2.0-APIs/pulls

https://github.com/ethereum/eth2.0-specs/issues/2414

From protolambda to Everyone: 03:18 PM
https://github.com/ethereum/eth2.0-specs/pull/2390

From Terence to Everyone: 03:25 PM
https://github.com/ethereum/annotated-spec/blob/master/altair/beacon-chain.md

From Mikhail Kalinin to Everyone: 03:26 PM
https://hackmd.io/@zilm/withdrawal-spec

From Hsiao-Wei Wang to Everyone: 03:27 PM
https://github.com/ethereum/eth2.0-specs/pull/2417
