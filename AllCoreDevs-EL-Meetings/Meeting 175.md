# Execution Layer Meeting 175

### Meeting Date/Time: Nov 23, 2023, 14:00-15:30 UTC
### Meeting Duration: 60 Mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/901)
### [Audio Video of the Meeting](https://www.youtube.com/watch?v=_by0UBqrYng) 
### Moderator: Tim Beiko
### Meeting Notes: Avishek Kumar

_______________________________________________________________________


## Dencun Updates

**Tim Beiko** [5:23](https://www.youtube.com/watch?v=_by0UBqrYng&t=323s): We are live. Welcome everyone to ACDE # 175. Today as always we'll be talking about Dencun get some updates on testing. I believe there was an execution API PR we wanted to discuss as well. And then figure out where we're at with regards to launching devnet #12. And what we see as the next steps after that and related to this we discussed in the past that this would be the last Fork on Goerli in a world where we forked Goerli before the holidays. It would have made sense. I think to announce that as part of the hardfork announcement, but I think if we're not going to hit that we should still announce how long we plan to keep Goerli around for after dencun. And so if we could get a feeling from teams today around how long we want to maintain at least the client notes on Goerli that'd be great. And then to close off Micah has a proposal for a new RPCN Point eth_multicall. So I guess to start, I don't know Pari /  Barnabas either of you want to give an update on testing so far and Devnets where we're at there and then we can go to the client teams as well.

## Testing Updates

**Barnabas** [7:00](https://www.youtube.com/watch?v=_by0UBqrYng&t=420s): Yeah! Sure I can give you an update. So basically we are running Devnet #11 right now and everything seems very stable the only pair that is not able to keep up is ethereum JS with loadstar but it seems to be some peering issue. Gajinder, can look into that. We wanted to launch Devnet #12 next week. But we heard some feedback from the prysm team that they think that this is a bit too soon. So we might as well hold off for a bit longer because this week is Thanksgiving week in the states. And we expect that maybe not all client teams would be ready to go with Devnet #12.

**Tim Beiko** [7:44](https://www.youtube.com/watch?v=_by0UBqrYng&t=464s): Got it. And just could you remind us Devnet #11 does not have the latest CL changes right Devnet #12 is the one that will have the Blob signing changes. Got it.

**Barnabas** [7:56](https://www.youtube.com/watch?v=_by0UBqrYng&t=476s): Yeah. That's correct. So I do have a spec sheet also for Devnet #12. Give me one sec. I will get the link.


**Tim Beiko** [8:04](https://www.youtube.com/watch?v=_by0UBqrYng&t=484s): Oh! I literally have it on the agenda. Let me post in the chat here.

**Barnabas** [8:12](https://www.youtube.com/watch?v=_by0UBqrYng&t=492s): Okay. Yeah, so the only change should be just that one change that we discussed last time.

**Tim Beiko** [8:19](https://www.youtube.com/watch?v=_by0UBqrYng&t=499s): Got it.

**Paritosh** [8:20](https://www.youtube.com/watch?v=_by0UBqrYng&t=500s): We did test a couple of things for the lighthouse team. I think they changed what gets gossiped in which order as well as support. And I think Pawan has like a bunch of information collected out there. And then we turned on MEV back in Devnet #11. So we're going through the entire MEV work on Devnet #11 as well. 

**Tim Beiko** [8:45](https://www.youtube.com/watch?v=_by0UBqrYng&t=525s): Nice.


**Barnabas** [8:49](https://www.youtube.com/watch?v=_by0UBqrYng&t=529s): Yeah we should Probably, sorry, so we still want to enable all MEV boost for all the different clients right now it's only running for loadstar and nimbus. But by the end of this week we're going to enable it for all CL’s. 

**Tim Beiko** [9:05](https://www.youtube.com/watch?v=_by0UBqrYng&t=545s): Got it. Anything Barnabas, Pari, otherwise I will go to Ben.

**Barnabas** [9:13](https://www.youtube.com/watch?v=_by0UBqrYng&t=553s):  Yep that's it for
Me.

**Ben** [9:18](https://www.youtube.com/watch?v=_by0UBqrYng&t=558s): Yeah just wonder if we should do a straw poll ready on devnet-12 starting in a week. If it's only prysm who is unable to make it they can catch up later. So just in terms of kind of keeping up the Cadence whether everybody else is ready or not. We could just put a finger in the air and see Teku. We believe we should be ready.

## devnet-12

**Tim Beiko** [9:41](https://www.youtube.com/watch?v=_by0UBqrYng&t=581s): Awesome! Yeah,  how do other clients feel about that? Is anyone else ready to start devnet-12 next week? 

**Gajinder** [9:51](https://www.youtube.com/watch?v=_by0UBqrYng&t=591s): Loadstar can start devnet-12 next week as well.

**Tim Beiko** [10:01](https://www.youtube.com/watch?v=_by0UBqrYng&t=601s): Anyone else?

**Marius** [10:03](https://www.youtube.com/watch?v=_by0UBqrYng&t=603s): I think all the execution layer clients probably can.

**Tim Beiko** [10:07](https://www.youtube.com/watch?v=_by0UBqrYng&t=607s): Yeah I assume there's no changes. I don't know if there's anyone. So prysm said they can't. I don't there's anyone from Nimbus or lighthouse on the call?  Okay. Well if we have all the EL’s and then at least 2 of the CL’s potentially up to 4. Yeah, I'm curious Pari /  Barnabas do you think there's value in standing up the devnet even with a subset of clients. It feels like we might learn about something breaking. Especially given like the new CL change by doing that next week. 

**Barnabas** [10:47](https://www.youtube.com/watch?v=_by0UBqrYng&t=647s): I think we can do I think we can do a kurtosis test for sure and then if we have like three clients then we can start the devnet. 

**Tim Beiko** [10:57](https://www.youtube.com/watch?v=_by0UBqrYng&t=657s): Okay. That sounds good. I guess what I'll do then, I'll post in the Discord asking for if there's more CLs.  And we have a testing call on Monday as well scheduled. So yeah we can bring that up there as well. And see if there's a 3rd client but, I think, let's try to do it you know even if it means it breaks and then there's a devnet 13 or something I think we'll learn a lot by trying to get the the devnet 12 up. Yeah so okay. So I'll do that. I'll ask in all core Dev. And then we can discuss this on Monday.

**Barnabas** [11:55](https://www.youtube.com/watch?v=_by0UBqrYng&t=715s): Like Wednesday or Thursday would work for loadstar and teku.

**Ben** [12:02](https://www.youtube.com/watch?v=_by0UBqrYng&t=722s): Yeah, I think so the 30th was the original plan I think that's good with teku  possibly earlier.

**Gajinder** [12:09](https://www.youtube.com/watch?v=_by0UBqrYng&t=729s): Yeah loadstar is already even this week as well. So yeah we're good.

**Paritosh** [12:17](https://www.youtube.com/watch?v=_by0UBqrYng&t=737s):Yeah I think Lighthouse is ready as well.  So we can just try to make sure the devnet is up before the call next week thursday.

**Tim Beiko** [12:24](https://www.youtube.com/watch?v=_by0UBqrYng&t=744s) Yeah that would be amazing if we can get it up you know on Wednesday try to run it for a day and see if it's still up or broken by ACDC. 


**Barnabas** [12:38](https://www.youtube.com/watch?v=_by0UBqrYng&t=758s): Yeah okay sounds like got plan just ping me your branch that I should use for Devnet #12 and then I will build images.


## disallow VALID <-> INVALID equivocation execution-apis#493


**Tim Beiko** [12:50](https://www.youtube.com/watch?v=_by0UBqrYng&t=770s): Awesome thank You. Anything else on devnet #12. If not Mikhail you'd link the PR and the agenda by but the PR round disallowing the VALID, INVALID equivocations. This is an execution APIs PR. Do you want to give some context on that.

**Mikhail** [13:25](https://www.youtube.com/watch?v=_by0UBqrYng&t=805s): Yeah. Thanks Tim. So a bit of a background Austin, from Nimbus, raised a problem in the Istanbul and the problem looks as follows that actually some EL clients when they first time receive a some
execution payload can validate it and return the INVALID status. So saying that this payload is INVALID but if the same payload sent to the same client for a second time the response could turn to VALID. Which actually, which must not happen. And obviously it must not happen. and basically is implicit in this fact that U the VALID or INVALID status is like the end status. And it
must never change for the same payload. And because we have some clients which does not follow these implicit requirements. We decided to make them explicit and Rise awareness that this thing should be fixed. Because on the CL side this is really unexpected behaviour. And I guess that for other reasons and not only for CL side like receiving something. Then that will be changed in the future. For other reasons this is also the behaviour that the Client should not have yeah Dustin, do you want to give more context from CL side what  bad things can happen because of that.

**Dustin** [15:16](https://www.youtube.com/watch?v=_by0UBqrYng&t=916s): Yeah sure so the main issue from the CL side is that it is defined in Spec that a VALID block cannot be the descendant of an INVALID block. And an INVALID block cannot contain again Per spec on the CL side. An execution payload declared to be INVALID by anyel. So what this means that it is valid and legal and actually a quite common optimization. For example for gossip rejection for things like this for a CL to say. Oh no this the EL already told me that this execution payload was invalid. Anything I see that refers to that just Skip and discard and move on. And what this means is that the Stalls chain progress for the CL. Now different CLs do handle details of this
Differently CLs can try some do some are more strict about just saying no they saw it once and just stop and never use it again. At least in the past I believe that some have saved the
rejection to disk in some format. But I think they stopped doing that a while ago so most be starting will wipe the slay Queen on this point. But that's essentially though is that it really cuts off the validity of the chain. And that's the harm that it causes. And to the degree that some
CLs seem to tolerate it. That's because like they're they're just retrying and honestly it's not clear to me whether they should. 

**Mikhail** [16:57](https://www.youtube.com/watch?v=_by0UBqrYng&t=1017s): Yeah. So basically if some payload is dimmed INVALID and this is actually an incorrect status of this payload. It may also cause temporal Network splits because validators will not vote for INVALID blocks for a
blocks containing INVALID payloads. So this is quite important to fix this bugs if they exist in EL clients.


**Tim Beiko** [17:32](https://www.youtube.com/watch?v=_by0UBqrYng&t=1052s): Just to understand is this an issue where the spec on the execution API is currently more permissive than the spec on the consensus layers. And therefore we only need to fix a spec? Or have we seen actual cases of this happen on like a devnet like I guess I'm trying to understand what what leads an EL to First classify something as INVALID and then valid? And if we've seen examples of that or is this just yeah a spec issue that we want to make sure everybody's following?

**Dustinl** [18:08](https://www.youtube.com/watch?v=_by0UBqrYng&t=1088s): Both are happening. So first is the case that this is and I in the wink spec that or issue PR that Mikhail  Winks. Actually the very first link within that description is to the optimistic syn spec and the optimistic sync spec already essentially requires this. I mean very, I think explicitly if people want to debate that. That's fine but as far as I'm concerned this is basically just implementing what's already in CL specs in the engine APIs. So at the end, for various reasons I guess the engine APIs had not strictly required this. And what had happened was there's, let's say, some evidence that engine API implementers on the EL side have not always looked at nor should they have to. If the specs are well factored out pure CL specs which is to say the optimistic six spec. Which is how they operates. So they did not necessarily see the you know direct outcomes of this equivocation necessarily because this the EL spec doesn't clarify this that's part of this that's half your question. Now the other part is is this essentially theoretical or is this just sort of a spec alignment. For the sake of spec alignment. And no it's motivated. There
are multiple ELs this is very clear I'm not picking on one EL here. I have encountered this with multiple ELs  where they and there are open GitHub issues. And Discord threads in eth R&D Discord where they're, I mean, the latter are theoretically public kind of hard to find just because you know Discord UX but you know where I have discussed this with said  EL and provided examples from their walks and compared from these devnets. Yes because that's actually a great way to harvest these things because then I can log in and see the exact same network situation with you know Nimbus Geth nimbus nethermind nimbus, Besu Nimbus Aragon and just compare them and and how they react to each payload. Beyond just looking at the like Beacon chain instances. So yeah and there are absolute examples of this and in the  devnet up through devnet 10 or 11. So it's become less common, sure, but I think almost the fact that it has continued kind of at all at a lower frequency these days than it used to is part of what suggested to me. That maybe it's an issue of well it should be in the specs because it's clearly not because look Hive tests many many things just this is a de I don't mean to make this a degression that will last longer than a sentence or two but it's going to feed directly back into this Hive tests many many things and empirically EL's are quite responsive to when Hive finds issues with them because hyp tests El specs and what would I was reading out of this was that this was one of those like regressions that was never really tested for. Therefore it kept happening again and again. Because it was not one of the metrics people were trying to hit. And so my goal is essentially to add this explicitly back into one of the constraints about how Els works as EL sees it when they Implement their own code, not just when they happen to look over you know. And into CL Specs. 

**Tim Beiko** [21:54](https://www.youtube.com/watch?v=_by0UBqrYng&t=1314s): Got it. Thanks. Yeah. That's really helpful context and then there's a comment in the chat by Gary saying you know one case where this could happen is if you have a stateroot mismatch and then you restart your node and it turns out fine and then you're processing the same payload. But yeah I guess I'm curious to hear from EL folks like first does anyone think we should not do this change and then two how should we test for it. Because something like this where it's like a stateroot mismatch and you have to reset is there a way to test for that in Hive or somewhere else. So, that we can catch those bugs earlier in the process.

**Gajinder** [22:37](https://www.youtube.com/watch?v=_by0UBqrYng&t=1357s): Here I want to seek some clarification on behalf of ethereum JS. So the problem is the oscillation between VALID and INVALID or between INVALID and syncing as well. I mean it could happen that the node could not would not keep the cash off INVALID blocks or would clear out its cash at some point and and might if the CL again is trying for an INVALID block which it should not. But let's say because of their syncing strategy they're trying again to sync a block. and that is responded as syncing. I think this is also being mentioned in the PR but I want to sort of confirm that is this also sort of a Nogo?

**Dustin** [23:21](https://www.youtube.com/watch?v=_by0UBqrYng&t=1401s): Not as  unambiguously so this is discussed in the issue went the PR between Mikhail and I. Actually as far as and obviously other people's well input yours anyone else's is welcome. So strictly speaking the for compatibility with the CL specs optimistic sync which is sort of the reference I'm going with here because that's how CL’s work. This is all the CLS of this. And so an EL which breaks this sort of contract really makes things difficult but the only thing that Swift requires is exactly what you said at first which is it cannot cycle between INVALID or invalidated obviously Blob cash Etc and valid. The syncing is okay. For this purpose there is a question. It's a good question. I think what the correct thing to do about the sinking is because what you describe of course is true as far as keeping pre states around and all that. It strictly speaking though is a little bit distinct from this issue and that's one of the questions actually that I think we would love Mikhail and I would welcome input into how to incorporate that or not into the this PR.

**Mikhail** [24:52](https://www.youtube.com/watch?v=_by0UBqrYng&t=1492s): I think that previously we decided that INVALID Sync is probably fine but VALID sync is not fine. And also INVALID and VALID switching between the two is basically something that must never happen. And as it's been said that one of the easy ways to fix that could be say we have a cash for INVALID blocks and when the next new comes with the same block hash. So we can pick the value hit this cache and see if the pocket is INVALID and respond invalid. Even though this cache makes sense for other reasons. But I would like to emphasize that this easy fix for this particular problem should not be applied. Because really jumping from INVALID to a VALID state is quite can be quite detrimental dependent on the share of the Market of other Market that the certain client that do this has so yeah. This has been said chain splits, that's some and some CL clients will have to be manually restarted to accept the block that was deed invalid Incorrectly.

**Tim Beikol** [26:24](https://www.youtube.com/watch?v=_by0UBqrYng&t=1584s): Thanks. Lucasz?


**Lucasz** [26:33](https://www.youtube.com/watch?v=_by0UBqrYng&t=1593s): Change this here things I want to add that one I think those are mainly bugs right. So and they're unexpected bugs so bugs that something got corrupted either like corrupted and stored but that's a bigger bug or corrupted like in memory. Like you have something that breast fixes it for example this is especially the case for State try, State root mismatch. So they are unexpected but we don't expect this to happen but you know they are there sometimes. So I think it would be hard to test for it because the scenarios can be really really wild.  And the other thing I think is mostly a social problem that we need to just treat those bugs with high priority and try to fix them. And communicate them well between CLs and ELs if this happens. So I yeah that's that's kind of the thing. I don't think there's much of like changes in make sure this communication Sounds well.


**Tim Beikol** [27:58](https://www.youtube.com/watch?v=_by0UBqrYng&t=1678s): Got it. And so and to be clear I assume this means you're in favor of making this explicit in this spec and then treating any issues we see that break this as basically a consensus issue in terms of severity or potential consensus issue. There's a plus one from this to this from teku. Any other EL team have thoughts on this or how to approach it to make sure that. Ideally we don't hit this but then also that we document or or test it. Okay and yeah so there's a comment by Gajinder around basically a plus one in yet as long as we can still have INVALID going back to syncing. So maybe we can give a couple more days on the PR but assuming nothing else comes up. It seems like making it explicit that you can never go from
invalid the valid as part of the spec. I don't know if we want to explicitly
call out invalid the syncing. And then for now unless the testing team comes up with a really unique way to test this. We probably can't add more test because of how hard it is to create this bug but if we do see this on devnets or or somewhere else clients should fix this with like really high priority. Given it can affect what a validator attests to on Mainnet. Does that make sense to everyone?

**Dustin** [30:10](https://www.youtube.com/watch?v=_by0UBqrYng&t=1810s): Sure. I have a question actually to as a wrapping up question in terms of how to phrase this in term, would EL implementers is this is the preference for kind of enumerate all cases? Or very specifically address the cases which changed which is to say for I specifically have in mind things like the invalid syncing thing here. So if this PR functionally would not change anything with invalid syncing. Like it says that it can happen now it can happen after it's fine is the preference to say. So explicitly or to leave it out and then have that inferred. 


**Tim Beiko** [31:03](https://www.youtube.com/watch?v=_by0UBqrYng&t=1863s): Any thoughts from EL folks? Okay there's one comment saying it's good to have everything explicitly in the spec. Okay. Another comment in favor being explicit. Oh sorry Mikhail?

**Mikhail** [31:34](https://www.youtube.com/watch?v=_by0UBqrYng&t=1894s): Yeah just want say that we'll work on the exact statement how to spec this out  taking into account that INVALID Sync can is fine jump in between these two yeah and we'll just then publish it in some on some of the channels that is ready for review.

**Tim Beiko** [31:56](https://www.youtube.com/watch?v=_by0UBqrYng&t=1916s): Awesome. Yeah thank you both for bringing this up. Anything else on
this? Okay.

## Goerli Shutdown

So next up I guess I wanted to bring up Goerli. So originally I think we thought we would upgrade Goerli to Dencun before the holidays.  obviously with the CL spec change that's pushed things back a bit. So I think you know realistically if we wanted to upgrade Goerli before the holidays the lay list we could do that is on December 20th. Which means in like one or two week we need client releases out to do this. My feeling at this point is this is unlikely unless I don't know if client teams disagree with that. Maybe now is a good time to voice it. And okay if that's the case so if we're feeling like it's really unlikely that we do get Goerli Fork ready to go out in the next week or two. I think we should have a proper announcement about Goerli being shut down. So we've already said it was deprecated but just to clearly announce to people when is the network literally going to go off. And obviously the anyone can validate on
Goerli. So it's not a call that lightclient teams make on their own but client teams do run the vast majority of the validators on the network. So the
day that all the client teams decide to shut their validators down at the very least. It's going to cause a lot of instability on the network. And it's  unclear how many other entities or orgs will keep running validators long term there. So I was curious to get a feeling from teams around how long should we keep running teams validators on Goerli. Once it's upgraded to dencun I talked with a couple people adhoc this week. And the rough number that I got was maybe something like three months and then potentially we do like one month where we start doing you know slowly shutting down validators to maybe do some Controlled Chaos testing or stuff like that. But yeah, curious how people feel about that. So there's two comments in the chat saying until we Fork mainnet which would probably be less than three months it' be closer on the order of like one to two months. If that's the case then I think that raises if no one wants to run the nodes for like three months after the fork. I think that raises the urgency as well that we should announce this because it might be effectively like three months from now or something. So anyone I guess yeah does anyone think we should do longer than after the mainnet Fork happens because there a couple comments in the chat about that. 


**Gary Schulte** [35:14](https://www.youtube.com/watch?v=_by0UBqrYng&t=2114s): We know  how many infrastructure providers are still using Goerli?

**Tim Beiko** [35:19](https://www.youtube.com/watch?v=_by0UBqrYng&t=2119s): A lot.

**Gary Schulte** [35:21](https://www.youtube.com/watch?v=_by0UBqrYng&t=2121s): Yeah. That would primary concern I think is that we want to give them the Controlled Chaos option I think.

**Tim Beiko** [35:28](https://www.youtube.com/watch?v=_by0UBqrYng&t=2128s):
 yeah I my personal feeling is like mainnet is like maybe a bit close it's obviously we don't know when we're going to Fork mainnet but if happens like a month and a half after Goerli that feels a bit short . But it's maybe the shortest possible we can do. I think there are yes sorry go ahead.

**Paritosh** [35:48](https://www.youtube.com/watch?v=_by0UBqrYng&t=2148s): Yeah my main argument against announcing until we bunch mainnet is that there's no date for mainnet. I would prefer just a static Goerli Fork plus three months something like that. It's easier to communicate and it's easier for people to and that can by default mean that mainnet is already merged at that point. Sorry already Forked.

**Tim Beiko** [36:16](https://www.youtube.com/watch?v=_by0UBqrYng&t=2176s): Yeah. So Pari I think is arguing we should gate the Goerli shutdown on the Goerli Fork date but then there's some comments saying we should gate it on the mainnet Fork date. One thing that's nice.

**Barnabas** [36:39](https://www.youtube.com/watch?v=_by0UBqrYng&t=2199s): Based on the Goerli fork because if something very happens during the Goerli Fork then maybe it's going to take more than chances to get it fixed before we can even Fork the sepolia or maybe if we push out a fix on Goerli. It might take weeks or months. So right, I think  we should assume that everyone is going to run their validators at least the client teams until we hit mainnet a plus few weeks here and there.


**Tim Beiko** [37:15](https://www.youtube.com/watch?v=_by0UBqrYng&t=2235s): Yeah there's a comment by Ansgar, saying maybe we do the later of Goerli plus three months or mainnet plus one month. I kind of like that it'll be a weirder thing to explain in the blog post. But I think it's probably the soundest approach. Yeah, does anyone disagree with that? And then yeah there's another comment also in the chat around. Didn't we Fork sepolia first last time but we agreed to Fork Goerli first this time because it's the end of life. So if we break it, it's less bad give worse a sepolia. We want to keep around for a longer time. So yeah does anyone disagree strongly with Goerli plus 3 months or mainnet plus one month. Whatever happens the latest. And obviously in a case where we have something break on Goerli. So badly that it takes us 3 months to fix we can also write another blog post saying we're going to extend things  but that feels Unlikely. Okay I'll take this as a yes.

And then the other question I had so once we hit that point. Do we is are there any specific tests? Or anything we'd want to run are ways we'd want to like handle shutting down the client validators that I don't know give us more valuable data? Like the obvious thing is just triggering inactivity leaks. But is there a period of time over which we'd want to run some tests in a more chaotic mode on Goerli. And should we pre-announce that some way. So saying you know after 3 months it's going to move to like this chaos testing period for a month and then will shut everything off. Does anyone have strong opinions on that?

**Paritosh** [39:42](https://www.youtube.com/watch?v=_by0UBqrYng&t=2382s): Perhaps we can just the time point where we said we're stopping support for Goerly as the time Point chaos stuff starts. You can do chaos for roughly a month. And I would advocate for everyone than doing honest exits. So that whoever's left over can just continue validating until they feel like it.


**Tim Beiko** [40:06](https://www.youtube.com/watch?v=_by0UBqrYng&t=2406s): Yeah and a month feels sufficient. I assume a month gives us enough time to
try out any flow or thing. We'd want to try out. 

**Paritosh** [40:21](https://www.youtube.com/watch?v=_by0UBqrYng&t=2421s): Yeah, I would say so. I can't imagine too many things that we want to try.

**Tim Beiko** [40:26](https://www.youtube.com/watch?v=_by0UBqrYng&t=2426s): Okay. There's a question: how long will the exit take? Months.

**Micah Zoltu** [40:40](https://www.youtube.com/watch?v=_by0UBqrYng&t=2440s): Should people who are exiting continue to be good citizens and validate until they successfully exit. 

**Barnabas** [40:47](https://www.youtube.com/watch?v=_by0UBqrYng&t=2447s): I think we could just slash do a Math slashing that should be a lot more fun and a lot more quick.

**Potuz** [40:54](https://www.youtube.com/watch?v=_by0UBqrYng&t=2454s):
It's not quicker. 

**Barnabas** [40:56](https://www.youtube.com/watch?v=_by0UBqrYng&t=2456s): Oh they would still need to exit right.

**Paritosh** [41:01](https://www.youtube.com/watch?v=_by0UBqrYng&t=2461s): Yeah they would still need to I would actually just case it's per validator basis. So if you decide to be good you can keep it up if you don't then Network's dead anyway.

**Tim Beiko** [41:19](https://www.youtube.com/watch?v=_by0UBqrYng&t=2479s): Okay. So I think overall this makes sense so three months after Goerli or one month after mainnet whatever comes to latest. Then we have one month where we do some testing and then we assume at least from the purpose of from the point of view of client teams and EUF devops. It's no longer maintained or supported but obviously anyone can choose to run their validators on Goerli if they want. And then the other thing is we won't have it as like a canonical testnet for the future hard Forks. So after this Fork it'll start being out of sync with Mainnet. Potus?

**Potuz** [42:00](https://www.youtube.com/watch?v=_by0UBqrYng&t=2520s): Half joking but if it's really an issue for devops we can always hardcore the higher exit channel on Goerly. 

**Paritosh** [42:11](https://www.youtube.com/watch?v=_by0UBqrYng&t=2531s): I actually don't get that.

**Tim Beiko** [42:15](https://www.youtube.com/watch?v=_by0UBqrYng&t=2535s): So meaning that you changed. Does Goerli has specific configs basically that are different from.

**Potuz** [42:22](https://www.youtube.com/watch?v=_by0UBqrYng&t=2542s):
We can hardcore more validators exits for blob.

**Tim Beiko** [42:30](https://www.youtube.com/watch?v=_by0UBqrYng&t=2550s): I know on the EL we never wanted to do changes that were just like only applied on testnets. But if you're all fine doing that on the CL side.

**Paritosh** [42:37](https://www.youtube.com/watch?v=_by0UBqrYng&t=2557s): Isn't it just a spec value though.

**Potuz** [42:42](https://www.youtube.com/watch?v=_by0UBqrYng&t=2562s): Yeah.

**Tim Beiko** [42:46](https://www.youtube.com/watch?v=_by0UBqrYng&t=2566s): So and I assume this has to go live with the hard Fork though right. Yeah maybe let's I don't know if somebody can make, I assume this is like a literal one line PR where you change the number. If somebody can make that PR
and then just post it on the agenda for ACDC next week. I think it'd be good to get like a proper consensus layer discussion on it. And it might be a good a good idea to do it. But we should decide soon. So, I think if yeah, if we can get a PR for this in the next couple days. And then confirm it on ACDC. But I think for everything else. And I guess if anyone has objections to any of this on ACDC next week as well? We can bring it up but I'll draft the announcement following everything we discussed today. But I won't publish it until the call next week. 

**Barnabas** [43:47](https://www.youtube.com/watch?v=_by0UBqrYng&t=2627s): But this is not yet implemented in any of the clients right? Potus? 

**Potuz** [43:54](https://www.youtube.com/watch?v=_by0UBqrYng&t=2634s): What this is not officially. I was just joking but every client implements. We take a file with the spec constants. So we just need to change the spec constants that the presets that were that we saving for each for each net.

**Tim Beiko** [44:12](https://www.youtube.com/watch?v=_by0UBqrYng&t=2652s): And I guess yeah are the presets Network specific or are there just minimal and Mainnet I thought there were two but is it one per testnet.

**Potuz** [44:23](https://www.youtube.com/watch?v=_by0UBqrYng&t=2663s): So they are minimal mainnet. However you can just load anything the fork ID is one of the values. So it's something that we can just change on two networks repo.

**Tim Beiko** [44:36](https://www.youtube.com/watch?v=_by0UBqrYng&t=2676s): Okay.  So they cofig values not PR values got it.

**Potuz** [44:39](https://www.youtube.com/watch?v=_by0UBqrYng&t=2679s): Yeah both of them.

**Tim Beiko** [44:43](https://www.youtube.com/watch?v=_by0UBqrYng&t=2683s): Yeah look I think  if we want to make this change on the CL and it's easy and teams like it then we can discuss it. But, we should probably make that decision on the CL call next week. And I assume it's a small enough change that if we decided to do it wouldn't delay anything.  Okay. Sweet. So let's do that and then hopefully by the end of next week we can post an announcement about Goerli just to let people know. Anything else on that. Okay in that case last thing we had on the agenda was a proposal by Micah or Not by Micah but advertised by Micah for eth_multicall do you want to give some background on this.

## eth_multicall ethereum/execution-apis#484

**Micah Zoltu** [45:57](https://www.youtube.com/watch?v=_by0UBqrYng&t=2757s): Sure. So the short version of eth_multicalll is basically the same as eth call except for you can do multiple transactions in a row that are applied in sequence on top of a shared State. And so you can  the simple example of this is very commonly you need to do an ERC 20 approval followed by an ERC20 transfer and you can queue up both of them basically. And simulate both of them against you know head of mainnet for example and see what the outcome is instead of whereas right now you can't do that you have to do the approval put it get it onto Mainnet and then do the Eth call afterwards. Unless you use specialized tooling this has come up in multiple times. So a long time ago I wrote a plugin that for nethermind that I use that does this hard hat and Anvil have similar features called main networking and and whatnot Cena from the Geth team built or wrote a proposal up in the execution APISs a while back and then  another team built off of his proposal and had another proposal and so this basically just keeps coming up that people want this. And so we finally got together and nethermind and Geth have  implemented the spec that we have for this. And currently we have tests and we're basically just fixing miscellaneous bugs and coordinating resolving differences between clients. And so we're not quite to the point where we can't make changes to the spec anymore. And we wanted to run it by the core devs and see if anyone has feedback and before we lock in a spec. And actually put out in release clients. And so again this is currently implemented nethermind and Geth. We'd love to get it implemented in Aragon and Besu as well. The spec is linked in chat by Tim there. The big differences between eth_call. And this is besides just the ability to do multiple calls in a row is we the JSON RPC method is named eth_multicallv1. And so the purpose of this is of course versioning because we've run into problems before we need to make a small change or something that's backward and compatible to feat RPC endpoint.And so we added the V1 there and this is something maybe is a little bit controversial people have other ideas we talked a lot about various ways to do versioning of Json
RPC  we don't necessarily have to do it this way this is the way we all decided was the best but it's open for discussion we also added in here eth transfers now show up as ERC20 logs from address zero  this is because people who are doing accounting on chain. It's very frustrating to have ERC20. And so this is we felt like this a good place we can kind of test this out. And this idea of having ETH transfer show up within a transaction as logs. And this is
 there's a config flag in your Json RPC. RPC request where you can enable or disable. This so if you we don't want to, I think it's off by default. So we don't confuse users who aren't used to receiving ETH transfers in their logs. It also allows for Block override. So because you can do multiple calls we also have the concept of these calls are inside of blocks that you can control. So you can set things like the time stamp on the Block. The block author basically any field on the Block you can set  this is particularly useful for things where you want to maybe simulate. 
What happens if I you know vote for this proposal and then three weeks later I want to see what happens when that proposal is actually executed for like governance contracts and whatnot. And so the idea is that by overwriting the block you can set the timestamp of the next block to be. You know two weeks in the future or whatever and then your EVM is going to execute as if it's two weeks in the future. So this allows you to do better simulation of things like that has state overrides state overrides I believe already exist in eth call for several clients. So that shouldn't be anything new there really it also does allow pre-compile overrides though. So you can replace a pre-compile with some EVM code. This is particularly useful for EC recover because it makes it so you can simulate what happens if you did have an accurate signature for a thing. You can see how the execution would flow. And so you can override the EC recover pre-compile with some code that just like always returns success or whatever. And  it's very powerful because it allows you to do things like simulate permit to or permit  an ERC20 contracts. It also ignores the normal validation of no calls from contract. And I believe eth call does this as well. So I don't think this is new but  this is important because few hard forks ago. We disabled the ability to do calls from contracts. And this makes it kind of enables that for this eth multicall contact only not of course not for execution on mainnet. And this allows you to do the simulation of governance contracts time lock contracts stuff like that. And
the last thing that's a notable difference is we have two different modes one is validation on one is validation off.  validation off basically just keeps the client's current eth call validation semantics. So whatever your client does for validation, keep doing that.  Whereas the validation on that serves two purposes one it's standardized across clients. So eth call currently the clients all validate different amounts of things in different ways like I think for example nethermind just completely ignores your eth balance. And allows you to go negative effectively in terms of this gas spending whereas I believe gass does not allow you to go negative error. And so you get these weird little idiosyncrasies between clients with eth call and so we're trying to use this eth multi call as an opportunity to try to standardize that and so this validation mode allows us to do that. It also allows us to have a kind of more strict eth call. And so when you're trying to simulate something that  just before you deploy you run it on Mainnet. You want to make sure that this will actually run on mainnet ahead of time and with eth call previously. You could run it but you know because it wasn't fully validating the transaction you could still error on Mainnet. And it was very frustrating because you'd waste gas and so by having this validation mode on it basically makes it. So you are doing exactly like if this was on a mainnet chain. Almost all the validations on and you can look in the spec there's a couple of things that are not validated of course  transaction signatures are not validated in that mode. And I believe the no calls from contract is also not validated. Ask for the coredev team here is basically just take a look at
the spec and please give us feedback we would like to get this out into Mainline on the various clients sooner rather than later. So people can start using it and apps can start building on but we also want to make sure that everybody has an opportunity to give feedback and discuss. Tthe last thing we want is to deploy spec that everybody you know if they would have been given opportunity would have said oh wait this is a bad idea because X or Y. And so really what we just want here is everybody to take a look at the proposed spec and like I said there's implementations in Geth nethermind if you want to fiddle around with them. You're also welcome to join us we have a little weekly call between the various implementers and parties
Involved. And so if any wants to join, talk on there or  feel free to talk to us you know Discord or telegram or wherever if you have any feedback. And that's it if anyone have questions
happy to answer anything.

**Tim Beiko** [53:03](https://www.youtube.com/watch?v=_by0UBqrYng&t=3183s): Thank you. Any oh Danno?

**Danno Ferrin** [53:08](https://www.youtube.com/watch?v=_by0UBqrYng&t=3188s): So I just barely seeing this spec  one feature that's I would find useful for some of the work I'm doing is rather than moving a pre-compiled call and giving it code is the ability to say here's a set of inputs and here's a set of outputs you're supposed to give if you get a call to this address is that something that there be for that in this specification.

**Micah Zoltu** [53:28](https://www.youtube.com/watch?v=_by0UBqrYng&t=3208s): We talked about different ways of handling the pre-compile contract. So we we've talked about a few different ways to handle the pre-compile overrides a one option we talked about is just like
doing EC recover. Just special case where you can just override to recover because that's most common. We think the rest of them are like math things. There's not a whole lot of reasons to redefine math in your execution. The tricky part I think is with what you're describing with the kind of here some inputs here some outputs is that it makes It's actually kind of hard to get that into Json RPC right. So we can do kind of bite arrays. We have a mechanism for that via xerox strings. I think the other solution I would suggest for what you're describing is someone can make a contract and even Deploy on. If they wanted and that contract can just have some State and because we can do state overrides as well. We can give the pre-compile contract in question some state. So you can basically say override
it with my fixed input to Output mapping thing. And then you just have your you define in your state overrides what the input output mapping is. And so you can just literally put kind of write
a mapping in. And so I think there is a way to do what you want that being said. I'm definitely happy to talk more about this. And if you have other ideas on how we can get this in I'm not against what you're describing. I do think what we have could satisfy your needs  it just might not be quite as simple way.

**Danno** [55:03](https://www.youtube.com/watch?v=_by0UBqrYng&t=3303s): Okay because I mean thinking of using this for like L2’s let's say there's a system contract called get like L2 / L1 bridge and all sorts of stuff that may not be reflected in ethereum state. So I guess I'll call in the call and I'll put proposal I don't think it would be an array byte arrays. I think it'd be an array of structure we have input in response but yeah I'll definitely call in and workshop this because I think there's a huge Market for here's a magic value here's a magic output and it's completely external it's the EVM what those are and it's not necessarily like derivable from the from the call values.

**Micah Zoltu** [55:35](https://www.youtube.com/watch?v=_by0UBqrYng&t=3335s): Yeah I definitely think we can make something like that work. I don't know what the exact Design's going to look like but if you we out to me or  any of other people mentioned in the PR or just comment on the PR. We can definitely have a discussion. I think it's definitely possible to do what you're looking for regardless of how we do it when are these calls. Currently they are Monday. I think Monday morning UTC.  All right I don't know the UTC time check in real
quick Monday around 13 o'clock UTC is when we currently have them and we're also all available on various messaging platforms if you want to talk there.

**Danno** [56:17](https://www.youtube.com/watch?v=_by0UBqrYng&t=3377s): And where's the website with this information is it in the log somewhere.

**Micah Zoltu** [56:22](https://www.youtube.com/watch?v=_by0UBqrYng&t=3382s): Yeah. I'd say if you scroll up a little bit in chat here. Tim posted the spec PR that's the I don't think we actually link to the calls in there but we can do that and if you feel free to just drop a message to remind us in case we forget.

**Danno** [56:38](https://www.youtube.com/watch?v=_by0UBqrYng&t=3398s): Yeah I'm not seeing a link to a call in the spec PR. I'm looking at that.

**Micah Zoltu** [56:42](https://www.youtube.com/watch?v=_by0UBqrYng&t=3402s): Yeah I don't think it's in there yet so either message me on Discord after and I get you invited we actually talked about this just before the meeting about get making the calls a little more public. Previously there kind of invite only between the teams implementing. And so we will we do
have plans on getting that link out there. And if you just follow, subscribe to that PR. It will almost certainly show up on it before Monday. I hope there go just post a link to the calendar
Invite. Any other questions concerns thoughts. Sounds like not.  Okay. So just please reach out to us if you have any thoughts or feedback if we don't hear anything from anybody then we'll probably move forward with getting this merged into Mainline Geth and nethermind once all our inconsistencies between clients are worked out. We're pretty close unless we get feedback from someone so please reach out and read this back when you get when you get a chance.

**Tim Beiko** [58:00](https://www.youtube.com/watch?v=_by0UBqrYng&t=3480s): Thank you . before we wrap up  so in the chat  there were some more discussion around this. Idea that PO is brought up. And I think we've landed on a consensus that it's a bad idea. And we should not do it. So instead you know simply keeping Goerli configs and presets as is keeping the like Goerli +3 months Mainnet +1 month and then some chaos testing but not trying to mess with like the amount of validators that can be exited from Goerli per Epoch. So I just want to call That out one last time if anyone feels strongly. We should change those config on Goerli otherwise. I think we can just call it a day and move forward with the same plan but no proposed changes for Goerli. So last chance if someone wants to make the case for it. Okay  doesn't seem like it. So this is everything we had on the agenda. Was there anything else anyone wanted to bring up before we wrap up? Okay then yeah thank you all for hopping on and we'll see some of you on Monday's testing call. And then most of you on ACDC next Thursday. Yeah, have a good day everyone.

# Attendees
* Tim Beiko
* Pooja Ranjan
* Killari
* Danno Ferrin
* Kolby ML
* MauriusVanDer Wisden
* Maintainer.Eth
* S1na
* Dragon Pilipovic
* Echo
* Paritosh
* Micah Zoltu
* Terence
* Vid Kersic
* Peter
* Dustin
* Fredric
* Ben Edgington
* Barnabas Busa
* Guillaume
* Andrew Ashikhmin
* Marek
* Gary Schulte
* Piotr
* Mikhail Kalinin
* Mehdi Acuadi
* Tukaz Rozmej
* Oleg Jakushkin
* Stefan Bratanov
* Ignacio
* Marcin Sobczak
* Daniel Lehrmar
* Ahmad Bitar
* Ben Adams
* Spencer - tb
* Enrico Del Fante
* Damian
* Nishant
* Fabio Di Fabio
* Gajinder
* Mario Vega
* Dankrad Feist
* Matthewkeil
* Aneziane Hamlet
* Ansgar Dietrichs
* Phil NGO

### Next meeting [ 7th December, 14:00-15:30 UTC]



