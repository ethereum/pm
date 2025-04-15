# Consensus Layer Meeting 114 [2023-07-27]

### Meeting Date/Time: Thursday 2023/07/27 at 14:00 UTC
### Meeting Duration: 1.5 Hrs
#### Moderator: Danny Ryan
### [GitHub Agenda](https://github.com/ethereum/pm/issues/830 )
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=WtOQPxa6jOE)
### Next meeting [August 3rd, 2023, 14:00-15:30 UTC] 

#### Moderator: Danny Ryan

—------------------------------------------------------------------------
| Discussion Item | Decision                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
|Sync EIP-4844 and consensus-specs definitions consensus-specs#3462  |.  |


**Danny** [04:08:](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=248s): Welcome to ACDE 114 this is issue 830 and the PM repo if you're following along on the agenda. Cool, we'll go over a bunch of Deneb stuff. We have a placeholder for the e-star upgrade. Does that have a name? Did was it decided when I was gone? I saw there was a name that seemed to be potentially decided upon. That's a question all of you'all were on that call and I wasn't. 

**Ben Edigington1** [04:53](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=293s): Okay we went with Electra. Nobody's take it was just agreed.

**Danny** [05:02](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=302s):  Great! As long as it wasn't me, Creating it was great. Elektra, okay so we have a placeholder for Elektra. I will, I have some comments when we'll get there and then a handful of kind of Beck updates and presentations so we'll get into it. On deneb just some space for a general update dev ops testing. Anything people want to share with respect to progress?

# Deneb
## general update, devops, testing, etc
**Paritosh** [05:39](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=339s): Yeah we had a spoiler Shadow Fork last week. We bloomed the validator set a little bit. So we'd have some spending each one since we trolls are inhibit now and use that spending EIP to spam it with blobs. Potentially find anything useful on the network. So yesterday we tore it down but other than that we've just been updating tooling Etc. To make it a bit easier to test for Devnet 8. And I think Barnabas is supposed to the rough timeline of when we'd like Devnets 8 related things to happen on the internet interrupt Channel. So, hopefully by late next week worst case early week after we should have Devent 8 up and running.

 **Danny** [06:30](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=390s): Right and show away how to comment on because the spec release is likely Monday which is one. We need to figure out an item in here but there's also some renamings that are going into there. Cool any other General updates or deneb.

**H** [06:59](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=419s): That have a new PR here and thanks for protest and be careful for their previous reviews the current proposal is simpler than the previous one. So hopefully it will get included to the next release and from client to test. Yeah and if you have some feedback please comment. Thanks. 

 **Danny** [07:32](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=452s): Meaning the release on Monday or any or the nebulous release after Monday.


 **H** [07:39](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=459s): Hope it will be on Monday. One it's got it only three more test cases I'll review.


 **Danny** [08:00](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=480s): Okay any other General comments that are not on the Deneb agenda. Okay, I think there's been a lot of discussion about this over the past week. Essentially my Boost relay testing we are as we transition into full featured test Nets. With what we expect to be relatively stable features data structures Etc. It's time to begin to integrate you know additional testing around this piece of software. So I'm curious is Alex Stokes on a call?  So yeah maybe you have an update on kind of where we're at both in terms of. I guess there's two things one is the minimal amount of software and stubs such that consider clients can do testing in these new types and context and then more fully featured such that people on the other side of the party can test their setups the builders in real life.

 **Stokes** [09:11](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=551s): Sure, yeah, so Mario has I believe it's essentially like Hive testing, for like mocking the Builder API. I don't know I haven't looked at it. So I'm not sure if they fully support the Deneb specs. But it should be pretty straightforward to do if they don't. Perry's been working on more Hive testing to actually like run at least like the flashbots software, which would be amazing. I've been helping some with that and yeah so generally things are moving along I don't think the updates to the Builder specs that like for example flashbots would need in their relay or I think even my Boost right now aren't you know emerged but that works very much underway. So should all come together in time but yeah this is something we should focus a lot more on over like the next month or so as things stabilize.

**Danny** [10:10](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=610s):  Yeah cool I think the main reason to get on the agenda is like it's kind of that time to transition into having this type of testing. So just primarily a signal but thank you for the update and any questions or further comments on this one? we can certainly continue to discuss it in subsequent call. Tammy Ron muted did you mean to say something?


**Tim** [10:40](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=640s):  Oh no sorry I accidentally unmuted myself.


**Stokes** [10:45](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=645s): 
Oh I may be jumping the gun into the next topic but I would say the sooner. We can actually freeze the spec the better because you know for example a lot of the flashbot stuff is just going to wait until the thrash is settled so that would unblock sort of finalize the network with the builders in realize.

**Danny** [11:14](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=674s): Okay other than we are kind of entering into my Boost testing time. Any other comments or questions? Okay cool, thank you Stokes thank you others that are putting some effort into that. Shall we you had a PR open with some naming and consistency between yeah the EIP and the consensus effects? Do you want to go over that real quick.


**Hslao Wel Wang** [11:47](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=674s): Yeah so, it's still just an issue here because of it we didn't decide which place we should change? So one is about the inclus like it's called version hash version KVG and the EIP has a different name and another one is the custom type description for vlog. So they also have different definition. Please see the issue tickets there. So, my preference is updating the EIP and you know I think there are some EL client depths here and I don't know if does anyone has some strong opinion. So by the way this is not a blocker for the devnet 8. Because this two naming can be just changed without the stake. I mean it's not a consensus logic. So it's fine so just post sharing here and I hope you will be resolved very soon. And we can finally freeze the Deneb Specs. Yeah any suggestions? Yeah if no then I will try to open a PR on the EIP side on Monday and we can keep discussing there thanks.


**Danny** [13:48](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=828s ): Yeah cool so if you have comments jumping on this issue I think at PR being open and circulated for discussion before the execution layer call, Would be a good way to keep in mind, thanks. Okay cool next up we have the PR from agenda that we thought we might be able to get some consensus on early in the week but we're not able to. We do have a number of comments since we did discuss this last Thursday. A lot of them are in a negative light that we had not previously seen in the calls. I really think that we should make a decision on this today and be done with it again for context. The parent Beacon route is obviously committed to in the beacon block. It is not independently in the execution payload the data structure on the consensus layer. But obviously all of the fields that the execution layer needs are committed to within the beacon block. So you can kind of reconstruct it from the piecemeal components. The execution payload plus this additional field which is passed into the engine API as of today. It works there was definitely some discussion before we made the decision one way or the other. Gajinder brought it up that. Beyond just kind of aesthetic reasons it's a bit annoying with debugging. We've since that reopened the conversation we've since seen Enrico, Light client, Terence, Mikhail and Julio. Echo that they don't really want the data duplication in that in this pattern we should be able to just utilize the fields as they come. And Stokes in the chat says Mio we should leave it alone. Are there strong opinions one way other that want to be voiced Beyond kind of the distillation of the thread that I just gave? I think at this point given this is what people are working on and given some of the negativity and counter arguments brought up in the thread that the default is we're going to do nothing here um but there's a chance to Echo otherwise. 


**Mikhail** [16:35](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=995s ): Yeah I'm curious what is the reason to add this field actually to the consensus data structures.


**Danny** [16:44](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1004s ):
The arguments presented were that having the execution payload as kind of a self-contained thing from the what is on the consensus layer being able to map that directly to the execution layer. Allows for kind of this one-to-one mapping such that when you're debugging. When you're like grabbing things to maybe check hashes or whatever like it's just it's just like a very self-contained thing you don't have to think about Gathering pieces of data from other places.  Obviously like if pieces of data exist in other places tooling is just going to be built to be able to get it but it kind of adds an additional thing you have to think about. 


**Mikhail** [17:22](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1044s): I didn't get this because yeah, I don't understand how you can read the execution paper or decide from the beacon block that wraps it that envelops it so I mean like this field should always be around. 


**Danny** [17:39](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1059s): Yeah and then you're probably but you probably then have some sort of function or script that combines in a way to check it. But sure, if Gajinder wants to Echo some of that but when I did say the default is going to be doing nothing. I did see a thumbs up from good gender. I saw thumb up from Sean and maybe a few other people. 


**Gajinder** [18:02](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1082s): I think Danny you have covered it. I don't really have anything more to add.  Apart from that you know yeah it's basically self-contained and then yyou can just grab it and use it and also this particular field impacts the state basically state that is calculated in the EL. So, aesthetically also it makes sense but I'm fine with not including it and doing a few more operations to just construct it while debugging 


**Danny** [18:34](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1114s): Got it okay.


**Mikhail** [18:38](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1118s): Yeah I was just trying to think about this duplication from the perspective of a client that has both CL and EL in one binary. And this looks a bit weird from that perspective because we have this redundant check that the parent. You can look root corresponds to the one that we have in a beacon block. And we have this field duplication. So because the engine API’s basically and one of the ways that connects two layers together. So the other one is just you know as I've said using the same binary which is not does not exist today but probably will exist at some point in time. So I mean like from that  perspective. I think that this is really this duplication really weird thing that's one of the arguments that I was at the time having.


**Danny** [19:28](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1168s): Right like the engine API leaking even more. So into the consensus structures.

**Mikhail** [19:33](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1173s): Yeah exactly

**Danny** [19:37](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1177s): Okay I think we're gonna do nothing, unless anybody says otherwise. Okay we will close the PR and move on. Thank you for bringing back up for discussion go Gjinder and thank you everyone else for taking some time to consider the arguments here. Okay next up this is PR3431, Roberto and a number of others have been doing quite a bit of work in getting the new confirmation rule specified there is a minimal change to the store and how the store is utilized? I believe it was a change to the store certainly how it's utilized to enable before this new confirmation rule. To enable the functions and the analysis the security analysis,  it's actually relatively a simplification but it's something that is necessary. I mean the confirmation rule is very high value to get in. So there was a discussion point on again confirmation rule side which can be done and implemented independently. When and where we should be thinking about the confirmation rule prerequisites the fork Choice filter change. Should this be something that is specified tested and attempted to be rolled out into deneb? Does this need to be rolled out in a high coordination Point like a fork can this be rolled out relatively. There's just some things that we should be thinking about in the context as we prepare for the next work. Can someone maybe give us the TLDR on the changes and someone gave us a perspective on where how this should be thought of in relation to upgrade?

**Mikhail** [21:49](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1309s): I'll try to. So basically this change is relaxing the filtering. and the difference between what we have currently and what is proposed is can only be visible in some really edgy cases that are unlikely to happen on mainnet.  So basically the difference can occur when for instance canonical chain does not have a weakness of the previous EPOCH Justified. While the other side chain has this evidence. So in this case yeah the these new change will like allow to remain canonical change to remain canonical. So while today it's not going to be the case. So it will be filtered out and yeah while they're all rolling out this change so this is what we should take into account. As I've said this is quite unlikely to happen on mainnet but we don't want to I this is my personal personal preference and probably the preference of other people that we don't want to you know have this roll out take for a month or whatever. And from that perspective it is reasonable to use a hard sport coordination at least for releasing the software client. The clients yeah at the same time like all clients will support this change and when the software is upgraded this change takes into that.

**Danny** [23:40](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1420s): Right so there's two ways to use the hard Fork as a coordination point. right there's the actually do a conditional logic change at the fork boundary and the other is to. You know because there's maybe a three week lead time too hard Fork cut it into that release. And know that there's a transitionary period where there might be disagreement during that lead time but to not have to support both Logics in a single release. Which one are you suggesting?


**Mikhail** [24:13](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1453s): Okay so I that's the question to client developers. I don't know if we have this Fork obstruction for the fork Choice rule. I mean like can one version be discerned by fork boundary from the other and like the first the first point like the first question what do people think about right now Dancun. How big of this change it oh there are tests. Basically so it should be fine I mean like this picture is ready to you know to be implemented ready for implementation. I'm just curious how people think about it in terms of Dancun.

**Danny** [24:54](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1494s): And there are tests but there are not like Fork boundary tests.

**Mikhail** [25:00](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1500s): Yeah right correct. I'm taking silence as at least there is no stronger position to do this at Dancun.

**Ben Edigington** [25:26](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1526s): Speaking for okay we discussed it a little earlier I don't think we'd object to doing this at but would prefer the option not to enable it at the fork. So that we can enable it earlier. So that we're not supporting two versions of the fork choice in One release.


**Danny** [25:51](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1551s): Right which we don't have a history of doing so right now so that likely represents a lot more engineering complexity.

**Ben Edgington** [25:57](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1557s): Right.

**Mikhail** [26:00](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1560s): Yeah so the question is does any client support this forking work in the fork Choice rule? Okay so yeah.

**Danny** [26:24](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1584s):  It's not something we've done so I doubt. 

**Mikhail** [26:29](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1589s) : Yeah okay so and kind of related question is whether we want an EIP for it or not I mean like to comply with the process. So it probably straightforward to do I mean like in a way that some small changes already in the node. Or can we like merge it without an EIP?


**Danny** [27:09](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1629s): This is an interesting one because it's in the fork choice we haven't really done a lot of EIP stuff in the fork Choice. It's also an interesting one because we're just changing Bay zero instead of we're kind of saying this is the new correct logic rather than and coordinating at Deneb but not necessarily at putting it in Deneb slowly. Yeah, I understand Sam but this is also it depends as we usually do EIP’s and we change past behavior but this is also it's not networking but it almost feels like changing to P2P.


**Mikhail** [27:52](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1672s ): Yeah it's not the chance to the state transition. so this is this makes a difference disagreement. Though actually some networking updates can cancel, can also cause disagreement on split use. So probably no EIP for this one I mean like it's fine at least from my side.


**Danny** [28:30](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1710s): Yeah I'm not friendly fundamentally opposed but it would be a bit different than the way we've been doing them for deneb. You know maybe it would be an EIP and then an annotation in the phase zero spec on the line that this line has been changed since Genesis via the EIP.  I think we can go either way on that.


**Mikhail** [28:59](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1739s ): Yep so probably it makes sense to create an issue for you know for including this change into Deneb. So people can you know buy their hands there find GitHub.


**Danny** [29:13](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1753s): Yeah let's do that and we would have to think about when this actually makes it into the canonical test vectors and whether we want to cut kind of future Branch test vectors because clients likely would want to wait until you know T minus a few weeks from the fork to. Actually have it in their main net release. Right Gajinder, I guess the problem with including in the spec release at least the one a problem worth discussing is that that would kind of begin to force the hand of the client by its CI. To just get this out immediately rather than potentially waiting until just a few weeks before the fork to get it out.  So there's certainly like some considerations on how this would impact mainnet releases and tests best generation in relation to each other.


**Mikhail** [30:21](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1821s ): I think we can't yeah I mean like it is it would be too late to include it into devnet 8. So probably not I think.


 **Danny** [30:30](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1830s): I agree with that. Okay Mikhail can you open up an issue so we can Surface any potential pushback and or discuss a bit more about the strategy on how this is going to go under test vectors and releases?


**Mikhail** [30:54](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1854s ): Yep sure thank you. 


**Danny** [30:58](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1858s): Any other comments or questions on this one? Anything else on Deneb? Great so the next work is an e star name Electra. There is an issue up we're cataloging things that people want to have for discussion for Elektra. I personally and I'm open to discussion debate on this. I think we should be in the mode where we're maybe presenting these ideas and making sure people understand them but I don't really want to open up the Elektra Fork. What's going to go into the fork conversation at least until deneb settles down a bit more. So for example you know there's a quick update on 6914 there's a 6110, overview today but those are more in the context of like sharing technical information then getting into the debate of what goes on um is that cool that we push this back the the lecture inclusion debate until we have a bit more Insight on Deneb timelines and didn't have stability, silences agreement. Cool moving on. Research spec and other discussion points um pop had a quick update to 6914. If anybody's following that EIP is Pop on the call yeah pop do you want to just give us a quick on that?


**POP** [32:57](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=1947s): Yes, the  EIP 6914 is about using the volatile index. Yeah and initially we already have the EIP to to truly use the index that is not used anymore and there is an update on that EIP because previously we haven't we because previously we didn't update the selection index in the FORK Choice store.  So this EIP is about updating the Slash variator indexin the Fork choice store.


**Danny** [33:41](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2021s): Right so like the once you operate an index the past transgressions should be cleared with respect to Fork Choice store and so there's an additional Handler called on reused index essentially abstractly when you reuse an index you need to make sure to discard the associated index and equivocating indices in the store. I'm pretty straightforward. But if you're following 6914 definitely a very important update anyways doing prototyping and stuff.


**Mikhail** [34:16](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2056s ):  I have a small question here ? So the intention is to call the cell number used index whenever then you while they're with a reused index is created. Right or whenever you get the index renewable layer start to return this you know h so yeah it's basically probably the same.


**Danny** [34:38] (https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2078s): Yeah I mean abstractly you're calling this Handler anytime between the validator being fully exited and the validator being reused but it's not it's not like hooked into the state transition function it's more like upon reusing the index trigger cleaning up the store. I think that's better than trying to have the dependency of the Fork Choice store and the state transition being explicitly integrated. Again this is kind of R&D EIP so open to Alternatives and different ways to think about this.


**ethDreamer** [35:35](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2135s): Is there a reason that the EIP isn't in the EIP report right now is it just waiting in a pull request somewhere. 

**Danny** [35:42](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2142s): Is it a draft I think it's maybe a PR. I would have to open up yeah so it's pull requests 6914 and I opened the pull request and it's still sitting there which means it's my fault um I'll go clean that up.

**ethDreamer** [36:02](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2162s): No worries I was just looking for it.

**Danny** [36:07](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2167s):  Yeah cool I can get to that today. There's a like typos and stuff. Great, Roberto and a few other people have worked on a document kind of thinking about how to improve spec compliance across clients in this kind of unique domain. Roberto would you like to explain this?

**Mikhail** [36:48](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2208s):  I believe prepared so it's not on the call today and a ditch is not on the call today.


**Danny** [36:55](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2215s): Okay cool so there's this doc. I think Roberto edicha and Alex lassov have been thinking about you know our unique challenges in this distributed context. Especially thinking about some things like work Choice Etc where we probably don't have super high assurances on spec compliance and it produces Dock and outlying the challenges and also potential things that we could continue to do. I am not the one to present this doc so I will leave it at that the stock exists. There are people that are thinking about these hard problems and people that might be proposing additional Solutions pieces of software and strategies to enable better spec compliance. I invite certainly those folks to continue to come to the call and just discuss these but given they're not here. I don't have much more on that. Saulius!


**Saulius Grigaitis** [38:06](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2286s): Yeah so there is one thing that actually we discussed here internally that's related with spare compliance and I hope I can take a few a couple of minutes to express that. And yeah maybe this could be in line with what it is in the doc. So essentially we kind of often gets to this interesting problem where we see that there is a written specification and there is test vectors and in reality clients they are kind of compliant to something in between written specification and test vectors. Because all the clients seems at least at my knowledge all the clients targets to run test vectors and pass them. However there are multiple multiple optimizations in each client and that slightly or sometimes more than sometimes the best diverges from the written specification. And so for us the the problem here is that if we have a highly optimized code for the optimizations that at some point for ourselves it looked that it makes sense. Just for example this latest non-finality incident where clients implemented various optimizations that often involved with discarding the attestations that according to specification shouldn't be discarded. So for us the problem is that if after these optimizations test vectors are changed. And they covered some case which was not covered in the Forum then sometimes. We lead to you know to huge refactorings like that takes even months to to accommodate some some new test director that was added recently or something like that. So actually we are thinking to make a two modes in a client. So the whole mode is is less optimized that tries to fully Target or or Target as much as possible the written specification and another mode is optimized the mode which targets test vectors like you know like a little bit stripped down version in terms of the cases that are handled so this would allow us to quickly bring back the functionality that is closer to the written specification. So my question is there some other team that experiences something like that and see the Asia and in this in the thing that we think that it's an issue or we just going somewhere else from the mainstream with this approach ?

**Danny** [41:18](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2478s): Yeah so the question is has anybody tried this kind of dual approach where you maintain highly optimized and much more straightforward version.

**Saulius Grigaitis** [41:29](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2489s): Yeah this recorded version is more like a written specification compliant.


**Mikhail** [41:37](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2497s): Does it mean that the optimized version will be actually used by users and yeah and not optimized one like straightforward one will be used for compliance testing.

**Saulius Grigaitis** [41:54](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2514s):  No I would say this straightforward it wouldn't be just a very straightforward I mean the idea is not to just repeat the written specification. The idea is to have also pretty fast code but the code that handles these edge cases that are let's say covered with a more General written specification because you know test vectors are pretty Limited in the cases that they cover um because these are specific cases not a general uh specification. So for us this uh written specification mode. Let's call it that for now would the work just for the you know for the proposed that we have a code in the out in our code base that is a spec compliant. So if test vectors changes and uh and our optimize the version needs a huge factoring then we can easily switch back to this to General mode. And this from the engineering perspective this would be much faster than to refactor this optimize the version but the users would be running the optimized version. 


**Mikhail** [43:21](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2601s): Yeah but that also means that in some cases user will run the client that does not comply to the spec right.


**Saulius Grigaitis** [43:29](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2609s): Yeah but if you see at least from our understanding that I would say probably all the clients debates from the speca I mean I'm actually not sure. Did all the clients Implement uh the optimizations for the last non-final incident where like those weird attestations are discarded? But if if yes then I think all the clients does not uh are not compliant to the spec  at least from this perspective. So I mean I think that probably there is no point that is fully compliant to the specification. Or am I wrong?


**Danny** [44:35](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2675s): Yeah I think there are heuristics used by all clients on anti-dos considerations around which attestations too actually consider. II guess depending on where your view of the the spec compliance is you could have Divergent you could say divergent or not right if you're looking at just the fork choice in the context of which messages were given to the fork choice then there's probably a higher compliance but then if you're now kind of expanding that scope to um and then which messages are you going to give there's more Divergence. Yeah so I don't I don't think anyone is doing the Dual maintenance strategy. I think it would certainly be interesting to investigate and write about more if you do get on that path. Another nice thing there potentially at least is you could actually have some uh intra client conformance testing right. You could fuzz the interfaces of the optimized and non-optimized and see if you get the same results. So there's maybe a few other things that come out of there other than have the refactoring speed and stuff.


**Saulius Grigaitis** [45:58](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2758s):  Okay I think I'll probably try to check this this Doc that you Danny mentioned maybe they are talking about something like that.


**Danny** [46:14](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2774s): Yeah cool so take a look at the dock any other comments or questions in this domain right now. All right cool. If you do have anything in this domain certainly uh reach out to the authors and we can bring up points of discussion from the stock. Anytime subsequent calls  Thank you. Okay next up Mikhail and a couple people that have been working on prototyping EIP- 6110. I would like to give us an overview and opened up for questions just so we can better understand this feature as we're making decisions in the future. Again I think that certainly over the next handful of calls we do have some time if you have an EIP that you're want to get some feedback on or you're potentially considering for discussion for Elektra. It would be a good time to just take 10  / 15 minutes out of these calls to explain these things to each other so we get on the same page just in general. But Mikhail take it away!


**Mikhail** [47:36](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=2856s): Yeah thanks Danny so Kevin and NC and  myself like have been working on on the Prototype and this EIP for like four months and yeah of course we'll work with so we receive tons of help from Besu team and my house team which which clients we used to in Fernandez. This change to the design also thank many thanks to Paritosh and the devops team. We had prepared a document that is a compilation of our goals accomplishments and challenges all the other stuff. So I'll just share my screen now and we'll go over this talk okay cool. Can you see my screen? Yes, so to remind what this EIP is about is basically supplying the deposits on chain. So the way the deposits delivered to consensus layer. Is going to be changed by reading them directly from the execution payload instead of relying on it. One data poll the thing that we have today. And so there is the detailed motivation section in the EIP for those who are interested why so there are many points why this change is really desirable so in this project. We pursue several goals one is just obviously prove the design by by implementing it and also estimating the engineering complexity looking for blind spots in the specification and incorporating the feedback from the development process into this pack. Also covering the specification with tests have an additional stress testing and just making sure that the design work Works in general. So this EIP has a transition period transition from like the one beta call to the new Machinery we tested that as well. Yeah and like just briefly go over the  Accomplishments, we have Implementations we have spec tests, we have a kind of like I would say ready for implementations back now. We ran several multiplayer devnets the stress tests independent on that so like the conversation release is quite impressive on that. So I'm deferring it to Kevin and and Sean to talk about to go over the implementation side.


**Kevin** [50:27](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3027s): Yeah so on the CL site is EIP ads deposit receive container and this is now an additional field of the execution payload and to process those deposit receipts you basically reuse the applied deposit function and these are like the main changes on the CL side.


**NC** [50:53](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3053s ): All right on the EL side uh pretty much like we are extending the execution payload of V3 to be like v6110 and have like the deposit receipts to be in it. As such like the engine API the new payload and get payload will have a new version of it as well. And also for the yeah to change the block structure we have like deposits roots and deposits to the header and body respectively. So similar to Shanghai with the withdrawals. And also yeah so for the blog validations uh we are comparing the deposits receipts against the deposit receive extract from the transaction logs. And as such like we need to have a API decoder because those logs were from uh the you know the CL side so this is something that's very new um to the execution layer clients.  Right, yes so the current implementation that is Shanghai base is already incremented on Besu. And last night I saw that you know the 4844 PR from just in Floren time has been merged. So we are going to replace the current  implementation to be on Cancun. This is something that's going to be done next week yes go on. 


**Mikhail** [52:20](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3140s): Yeah I just wanted to add here that we used Cancun basically as the basement for this change because the Cancun is the fork that this change presumably will be rolled out after. And for for best zoo we used a separate Branch to have a base implementation based in Cancun for testing. And now the question is about moving these implementation to the main branch which is actually great. At least in the main one okay so we're rather several multi-peered devnets which was really exciting. And Kevin and NC do you want to say a few words about it? 


**Kavin** [53:10](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3190s): I can say that for local devnets we used ketosis um for testing some basic functionality. And then we um quickly ran a multi-peer devnets and received help for from the EF devops team for that I don't know NC maybe you want to say something about block Scout.


**NC** [53:33](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3213s): Yeah because of our inexperience with you know having blocks go working you know nicely with Besu. So like there's a lot of parameters that we need to you know juggle with. And as well like because uh block scale relies on track transaction to you know to populate the historical blocks. And of course and there is like a limit of 512 blocks that we can look back on Besu when we're on Bonsai. So as such we need to switch the storage option over to Forest to get over this limits so this is something that's very tricky to you know to discover this issue and then I don't think there's anything else to be mentioned. 


**Kavin** [54:22](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3262s): Okay so for stress testing we first used a fuzzer and which allowed us to make like 100 deposits per slot and to maximize the gas_limit we deployed a batch deposit contract to handle like 725 Depots per slot with one single transaction.


**Mikhail** [54:46](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3286s): Yeah and here is kind of results from this stress testing. There is a block_delay parameter that output and Lighthouse log so what we've seen is that there is like 1.3 seconds to input the block with 700 deposits versus like several Middle East for an empty block. This block_delay parameter should be taken as a grain of salt because it's uh because the breakdown of this timing is not like kind of visible and requires more deep investigation like uh obviously 725 herders have been created during this processing after processing this block so some portion of this time taken by the hashing of the state but obviously most of this time taken by signature verification. We also not sure if the batched signature verification used for deposit processing in White House. Sso that's kind of a question worse investigating if you want to like implement this new EIP I think that some optimization of war is doing on that front.  So I should also say that 725 deposits is really a huge number uh which we should not ever seen on the mainnet. But that stress testing was like trying to estimate and see um what uh kind of Dos attacks can  be employed by this new mechanism and the Dos analysis in the EIP outlined in the EIP shows that. Basically the maximum number for 30 million gas_block the maximum number of deposits in Block is around 1200. So it's quite huge number but yeah the attack does not seem to be like sustainable long term there is also a Besu section uh of like uh really uh deep analysis on the performance done by Ameziane from Besu team so there are some charts here. So for those interested we'll share this document you can take a look. So the conclusion of this section mainly so this new validation Logic on deposit does not introduce like a lot of an overhead. And surprisingly we had challenges during the work on these prototype so guys do you want to cover on that as well? 


**Kavin** [57:35](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3455s): Yeah so overall the biggest challenge of the whole prototype was Finding compatible besu and Lighthouse versions	of Dancun, because our implementation is based on that.




**Mikhail** [57:52](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3472s): Yeah so like my main takeaway and my main lesson learned from that part is that you don't want to try to build a prototype or whatever feature on top of a and on top of a feature that is an active development. So we had to chase for you know besu and um most the besu Lighthouse as well I mean like in their implementation of 4844 because they were at some stage they were at different you know status on this. And yeah I was just thinking it was just incompatible with each other. So the reason for that was like we have a spec based on Cancun. So it is obviously reasonable you know to base the implementation of Cancun as well. But that's really damaged the um the progress on this project. So that's to bear in mind for the future prototypes of this kind. So the open questions that are still open for this EIP this EIP currently I mean like this design suggests the Queueless approach. So there is no Queue for deposits alternatively there could be a queue in the beacon State to rate limits the deposits per block. Or sorry not per block but rate limits deposit processing per EPOCH. It does not affect the signature verification at all. It's more about like affecting the number of deposits that can be applied to the active whether like to the active balance as well because there are top-ups. And with this approach  like one decent number of the pops can bypass the churn which yeah one of the things that we might want to consider and also the Queueless approach. We try to to do it because like we don't want to introduce any Queues to the beacon State. We previously tried on that but failed with withdrawals. So there is a pushback from client developers but also on the other side we have been exploring the max effective balance. The exploration of max effective balance increase suggests that queues are not that bad actually. So we might review this revisit this design Point design consideration especially, if if Mark's effective balance will be considered for inclusion probably at the same time or I don't know at around the same time. So we definitely need to do like a deeper performance performance analysis on sale side  to look for potential optimization and the signature verification. So basically that's the remaining open questions on that and yeah there is a gratitude section thanks everyone who made this project happen. Guys do you want to add anything on that? Okay cool so we are happy to answer any  questions that people might have on the Call. If any questions will rise around this prototype or around this EIP VR in Discord, you can find us there.

**Danny** [1:01:58](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3718s): And Mikhail you said yay more validator churn which I know was slightly just to clarify this did not change the rate of validator induction it just changes the how quickly they kind of deposits appear to the beacon chain to then be decided to how to put into a queue and so like hitting that that 700 something number changes the amount of processing that might happen in a single blog it doesn't change the mechanics of the induction queue so just to clarify.

**Mikhail** [1:02:37](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3757s): Yeah! Thanks Danny for clarification. I was not clear on that so what we might care is top-ups with without the queue they can bypass the churn. I mean like they not bypass the churn they bypass they churn today but they are eight limited that's that's important probably important.


**Danny** [1:03:02](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3782s): This is awesome, thank you to the entire team. I mean it's really badass to see these things prototyped in the end. Before we're trying to make decisions on them so thank you very much. 


**Mikhail** [1:03:19](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3799s):  Thanks everyone.


**Danny** [1:03:23](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3803s): Okay Everyone, Great. 6110 is on the Elektra discussion list so we will be discussing in due time any other discussion points for today. Okay great thank you everyone. Talk to you very soon. 


**Alex** [1:03:59](https://www.youtube.com/watch?v=WtOQPxa6jOE&t=3839s): Thanks everyone.

# Attendees[](https://)
* Alex Stokes
* Danny
* Mikhail
* Marius
* Terence
* Ansgar Diatrichs
* Ben Edginton
* Roberto B
* Ahmad Bitar
* Prestine
* Sean
* Paritosh
* Tim Bieko
* Mikeneuder
* Hslao Wel Wang
* Lightclient
* Zahary
* Matt Nelson
* EthDreamer
* Fabio Di Fabio
* Anna Thiesar
* Saulius Grigaitis
* NC 
* Kevin
* Trent
* Carl Beek
* Gajinder
* POP
* David
