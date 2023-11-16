# Consensus Layer Meeting 121 [2023-11-2] #898
### Meeting Date/Time: Thursday 2023/11/02 at 14:00 UTC
### Meeting Duration: 45 Min
### Moderator: Danny
### [GitHub Agenda](https://github.com/ethereum/pm/issues/898)
## [Audio Video of the Meeting](https://www.youtube.com/watch?v=dAStyB2Vv4s)
### Notes: Meenakshi Singh

# Agenda
## Deneb
## final decisions on Add blob sidecar inclusion proof consensus-specs#3531, release, and testnet plans
**Danny** [05:29](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=329s): Okay. Welcome to All core Devs Consensus Layer Call 121. This is issue 898 the PM repo. A couple Deneb items, which will probably have some things that ripple into how we discuss testnet plans and then an item around SSZ spec from Jacek. Okay if you haven't been following the repo or for the discussion that's Deneb Discord. We've gonna go back and forth on the proper way to do blob sidecars. Or at least ever since the split  there was an additional signature put on the sidecars by the proposer that serves as at least the reduction of the DOS condition of the DOS ability to essentially just the proposer.  There's always kind of likely concerns around if this was sufficient. If we needed slashing additions on this new message type. If this could increase the ability to do view splits and timing splits and short-term forks and reorgs and MEV. And all sorts of stuff.
And the stream hasn't started, interesting. I am streaming. Give me one second. Let's see if I can see if my stream key is off or something. 

**Tim**: Are you not able to stream the call?

**Danny**:  No,  apparently my stream key is also being used on the testing call so it went to the wrong call. Yeah, Dencun interrupt testing is live. Okay we'll rename that sorry everyone. Okay back to the Soliloquy on blob sidecar. Hey man, I don't know that's my key someone reused my key. 
Okay cool. So we went back and forth on this. This has also kind of created tough gossip conditions where you're trying to remember. What you've seen but also conditionally upon have you seen the block or not when you're making the decisions on the gossip network. I believe that most of the issues that we've seen on the devnets in the past six to eight weeks have been in relation to complexities around handling these messages.When to invalidate them, how to invalidate them, and what to premise those invalidations upon. So we're talking with some of the pPrysm guys one night who were not pleased with the design and even tossing around potentially recoupling and Franchesco saying well why don't we just send around the block header and a proof which I think once that was said allowed outloud most people said. Oh yeah that's a better design. You don't need to open up the VC for an additional signature. You those messages you cannot send redundant versions of those messages duplicate versions of those messages with different blobs or commitments if unless you're willing to get slashed. And you don't have this potential rage condition where you might have the sidecar and not the block or at least the block header. So you don't really have like conditional the same type of conditional gossip conditions. So we have a PR up with I believe  put it up 3531 that we've all been going back and forth on iterating on. I have asked for any Nays in relation to this. um and there's been a little bit of discussion. But it doesn't seem like any outright Nays. I believe this will largely be the removal of code from clients. And especially in a what proved to be a pretty complex Hhot Sspot. I'm getting right. Obviously there are  implications here in terms of relationship to getting Deneb out in relationship to what devnet 11  / 12 look like. But it also from my assessment looks like a much. It could actually be the same time to mainnet because this is simpler to get right. And we're not going to have as bug ridden Devnets. It's also almost certainly going to give us a safer mainnet because it's a simpler and more easy to get correct specification. 
So I guess first of all I'd like to hear are there anyone against moving this forward getting this into the spec ASAP, likely doing a release in the next 24 hours. And kind of recalibrating the software and devnets from there. And then assuming after we have that conversation we can get into the there a couple of little final points in design that I'd like to just make sure we're in agreement. Okay, but again we've heard positive generally from everyone. I'd like to hear if there's any negative. Please voice now.
Okay cool and there's a Pull request up for the Builder specs and there's a Pull request up for the beacon API. If that is in your domain of review please take a look at those. Okay I know there was in chatter in other places maybe you know worth having the conversation of why did it take this long to figure a better design out. And let's have maybe have that conversation but let's get through what we need to get through today first. The simple answer is well we hadn't talked to Franchesco or Franchesco hadn't truly parsed what we were doing. And hadn't had the idea but maybe there's a better answer than that. Okay cool. So there are a couple of herding items here Mikhael looks like we're deriving a depth parameter but then not really using it. And we need we should probably simplify and remove that depth parameter. Is there any Mikhail did I get that right.


**Mikhail** [13:01](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=781s): Yeah I just think that if we don't use this constant I mean like in deriving the depth. Yeah then we probably don't need it or if we have this you know this parameter defined. So we have to we should probably use it instead of Computing the depth from G-index. And I think that Hsiao Wei said that she's agree with that. Yeah so we can just make an adjustment. I think it's a small thing. Really it's kind of like more. Yeah it's more aesthetic side of things rather than yeah it's a small you know mainly to small discrepancy. So I would not like we can fix it in a separate PR whatever.


**Danny** [13:50](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=830s): All right. Well, let's just fix it there get it done. Potus do you mean that even if the spec does not define the depth you're not going to YAML compute it for regardless but do you even in that case. Do you think the spec should have that constant? Okay I'm having trouble person you don't allow me to unmute but this seems like a personal problem. Okay cool. Regardless, I think that Kasey agrees. Cool. I guess regardless we shouldn't have the Constant that were not being used. So let's go and clean it up one way or the other . Okay Mikhail was that the last your final lingering point or is there anything else.  


**Mikhail** [15:03](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=903s): It was just  there is another constant there is a parameter that defines depth and there is the constant that Define Gindex. So this constant is just used for computing the depth. Like it's not like actually not Computing it but just in the comment which explains how the depth was computed. So I think that this can be removed. I don't know because we're Computing these Gindex during the run time using the function. I know what clients will do actually. Probably they will define this constant in the code. Anyway then it makes sense. Probably to leave it in this back. 

**Danny** [15:49](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=949s): Okay so you're this this is kind of the secondary question is should we dynamically compute the Gindex or should we Define it up in the constants right? 

**MIkhail** [15:58](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=958s): Yeah.

**Danny** [16:03](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=963s): I guess all these questions are aesthetic questions. I don't feel very strongly I think it's kind of nice to be able to talk about independently but um matters too much. I guess let's both make sure we clean up both of these and in a consistent way. I see that you're unmuted. The only thing I can do to you is mute right now.

**Potuz** [16:38](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=998s): Oh now I'm muted. Thanks.

**Danny** [16:44](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1004s): You got anything is there okay um these are both aesthetic cleanups. Let's just make sure that they were moderately consistent. And Kasey had one more well. First of all Kasey did point out that we must and this is definitely an oversight we must link the Blob to the KZG commitment to. So that the blob inherits the consistency of the signature of the block header. So super good call on that otherwise anyone can mutate these messages on the P2P. And they'd still be valid. So that's in there. He did bring up one more discussion point on if you're doing a sidecar by range or sidecar by route check that you should also verify this Consistency. And that is accurate. I guess if you're putting things into your like verification pipeline. You will do so but an early kicking out of bad messages is probably a good call. Well on the buy root requests you like have the block and so I wouldn't put like a must or even should on the calling of this Merkle proof. Because you can just look and see if it's correct but nonetheless. I think we could add on both of them to do a consistency check. So I'll take a look at that right after this call.

**Mikhail** [18:24](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1104s): One question here is will the clients use the blob sitecars by root by wrench like without a block without having a block is this supposed to. 

**Enrico** [18:35](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1115s): Yeah I think we do. So if we are kind of haven't seen anything. So we actually try to get blocks and blobs together and ask for everything even without knowing the blocks. So we know that at some point the peer will only return the blob the blocks the blobs that are in the block but we don't know in advance the the corresponding block.

**Danny** [19:13](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1153s): Yeah it's like you definitely can parallelize by range if you're syncing. And then make sure that both streams kind of match up to each other. The other is I guess these cases where you see a random route in maybe you're recovering the block but you also might want to recover other messages in relation to it. 

**Enrico** [19:34](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1174s): Yeah it's definitely applied only to by root. I say the by range should be different. 

**Mikhail** [19:43](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1183s): Yeah if this these two RPC calls I used send along to blocks like not complimentary to blocks. Then it's probably worth verifying validating the signature because after this PR will have a block header in the blob sidecar. So this request will return block headers as well. And yeah right so the proposer signature needs to be verified as well. It depends of course on the use Case.

**Danny** [20:16](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1216s):  Yeah well and the kind of implicit is anytime you get one of these sidecars and you've either gotten another sidecar with the same header or you've already gotten the block when it says verify the signature you also just know that you verified the signature before if it looks the same. But I let me do a pass on both of those and just make sure that we're tightened up and consistent both in relation to discussing the proposer signature as well as the consistency of the commitments in relation to the One. 


**Kasey** [21:01](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1261s): Yeah I just want to clarify one thing like you can obviously verify that the commitments you know apply to the the blob without checking the proof. But it's more that you you would have a sidecar propagate one way but not the other. So it's more of like a network view split concern. I don't know how big of a concern that is that's why I brought it up?

**Danny** [21:27](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1287s): I see. So you're saying the same mess like you could if you're not actually verifying that merkle proof. Someone could be sending you a totally different message because they could just have junk in the and that would have not propagated on gossip but would have propagated in the root and then all of a sudden in relation to message IDs and stuff you have totally different messages coming in even though they're valid. 


**Kasey** [21:52](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1312s): Okay yeah in the proof yeah.

**Danny** [21:56](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1316s): Yeah. It's probably worth making sure that's just consistent. Terence?

**Terence** [22:03](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1323s): Yeah. So currently there it's sort of like a minor dos concern with The Blob sidecar in the event that you don't see the parent block. Your client may choose to insert that into a queue and process later when you get a when when you when you get a parent block. So that part if you compare the Block versus the blog sidecar the block actually does the signature check. Before you do the parent check versus the blobs sidecar. You don't do that, you actually do the signature check. After you do the parent check because of that right it's actually fairly easy for someone to construct blob sidecar without valid signature. And just kind of Dos the Queue. If today client implements that Queue. Yeah so that's something to watch for I can leave a comment on the PR. 

**Danny** [22:57](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1377s): Okay and this is if you're reading the conditions sequentially you would prefer the parent sign the signature people before this conditional Queue.

**Terence** [23:09](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1389s): Yeah just like how the block does it today.

**Danny** [23:12](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1392s): Yeah all right cool yeah if you can drop a comment there so we don't miss it.

**Arnetheduck** [23:17](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1397s): That it. I don't think anybody implements those rules in that order because the order in the spec is odd with regards to cost.

**Danny** [23:30](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1410s): We've talked about this before yeah there certainly there's an attempt to get the easy checks that invalidate things in relation to others before you do hard work in the order but obviously the real world assessment of that is probably different than as specers.

**Arnetheduck** [23:47](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1427s): Yeah and there's a different there's another well it's not really a concern but if you do ignores before rejects you might not de score a client on what would have been a reject if you first ignore it. There also like little differences like that if you depending on the order of things. 

**Danny** [24:15](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1455s): Nonetheless I do agree the attempt to if someone can make you do like an asymmetric work like filling up a queue if there's a condition that would prevent you from doing so having that before is probably a better way to write it.

**Arnetheduck** [24:37](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1477s): You know the Queue should be able to deal with it otherwise you haven't predicted your Queue.

**Danny** [24:44](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1484s): Yeah fair but like do you want a proposer to be able to fill your queue or do you want anyone to be able to fill your queue.

**Arnetheduck** [24:53](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1493s): Depends on the other costs. 

**Danny** [24:57](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1497s): Okay. All right, well at least drop that comment in their terance, so we can look at the configuration of that in relation other things. I believe that we can get this merge in the next few hours. And I believe that we can get a release out tomorrow. Cool. All right any other comments on this?

**Stokes** [25:43](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1543s): Can I ask one follow-up question since the relevant parties are here for the Builder specs. So there is an open question uh essentially who computes these KZG inclusion proofs. If you're going to a MEVrelay. The way the PR works that I linked right now. It has the relay compute them independently with the proposer instead pretty easily the beacon node could pass them along in the API. Does anyone have any preference here or see one way being better than the other. So I think it comes down to will the beacon node want to compute these proofs sort of optimistically. Because it would essentially send them well. Actually no. So if you send the block that's kind of a done deal so then the question is just is it easy enough to make those and then send them along as well and then the relay has less to do.

**Gajinder** [26:50](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1610s): I would prefer that Beacon node compute the proof and trenches along.

**Stokes** [27:04](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1624s): Okay.

**Danny** [27:05](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1625s): Any other preference here? 

**Stokes** [27:08](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1628s): Yeah if anyone has any comments just take them to the PR I suppose.

**Danny** [27:12](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1632s):  I guess one thing is like the node is going to have that logic. So that the node can locally build. So leveraging the utilization of that logic from the node might make sense.

**Stokes** [27:28](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1648s): Right like the Realtor will still verify these proofs but it's like one less thing. They have to compute and keep track of and maintain and debug and all this. I mean originally I made the PR with it you know where they're done independently just because it couples them less but it feels like it's better just stuck beacon node to it.

**Danny** [27:53](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1673s): What's the structure passing those between the beacon node and the relay like.

**Stokes** [27:58](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1678s): They would just be stapled onto the side line of beacon block.

**Danny** [28:03](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1683s): Okay just and some adhoc data structure they're not like. Actually trying to compute like utilize the network data structures okay.

**Stokes** [28:14](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1694s): I don't see a reason to.

**Danny** [28:22](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1702s): Actually may me feel a little bit differently about how it than I just said but it seems weird to pass like a small portion of a what's going to end up being a message that the relay is going to have to like verify and package into a larger message anyway. When the relay has everything to just create the whole message the message being the sidecar. But I don't know I don't feel very. 

**Stokes** [28:55](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1735s): Yeah I mean the thinking is just give Reay when last thing to do. Because the beacon node already have this code it'll be tested debugged all that.

**Dan** [29:12](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1752s): Then cache just go bit.


## proposer reorgs Allow honest validators to reorg late blocks consensus-specs#3034 -- merge?
**Danny** [29:19](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1759s): All right any other comments on this one. Very cool. Anything else on this spec change and or things in relation to the spec change. All right there's a longstanding PR in which at least a couple of clients have implemented on my mainnet. This is 3034 allow honest validators to reorg late blocks. This has come up on discussion quite a many times it seems that the clients that have nothing with it are have not because they want to see it in the spec. And there's been a push to clean up tests and other things in relation to it. And so I also believe that on this call we've done a signal of like yes merge. I'm doing that one more time because it has been cleaned up and is in a ready to merge State. Is anyone on a no merge relationship to this PR. Brow could not be here but also signal as the author that he is ready and comfortable for this merge. 

**Hsiao-Wei Wang** [30:55](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1855s): I think I can push the minor constant change like right now. So we don't have to open another PR. So just wait a couple minutes to make the CI pass. 

**Danny** [31:13](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1873s): Which I'm talking about the honest reorg PR now.

**Hsiao-Wei Wang** [31:19](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1879s): Oh sorry sorry you're that one.  Hope this PR looks it's in Finish point to me.

**Danny** [31:41](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=1901s): Cool and this is written as an optional thing so it can also be a no op. It doesn't have to be work.

## Research, spec, etc

Okay we can at least give some room for discussion on Deneb testnets Devnets. I don't have I've seen you know estimates of casual estimates of call it three weeks to to rework what's going on in the network layer in relation to the spec simplification. Is that approximately the signal here that approximately what people think. That we could maybe Target a debate in a few weeks. But that we should probably just weekly be assessing. Pari I'm not certain if that includes connect  next week or excluding. I'd say regardless that we are going to be looking at revised estimates for that in the next  couple calls. Okay cool any other discussion points around Deneb around Devnet around testing around anything before we move on. 


**Paritosh** [34:03](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=2043s): Yeah just one thing we have Devnet 11 up. It's going to be around probably till we launch a new one with the proposed changes but if anyone wants to Target something with testing. Please target Devenet 11 and Goerli Shadow fork Zero should go live tomorrow. So we'll also have some statistics on how long it takes to compute blocks and so on.

### ssz: Byte type and canonical JSON mapping consensus-specs#3506

**Danny** [34:31](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=2071s): Great! Okay, Jacek, you have a proposal up from September around byte type and Canonical JSON mapping with an SSZ. This is PR #3506 in the consistent specs repo. Do you want to give us the high level. 
**Arnetheduck** [35:05](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=2105s): Sure. So this is kind of an old PR. It dates back I don't know, maybe even around mainnet I think. Starting from the beginning like when we were developing SSZ. It was kind of useful that we had JSON. So that humans could read it for SSZ. And then out of that we kind of built tests that were using JSON to verify that our SSZ libraries were correct. And we're kind of past that stage now but I thought it was useful to maintain this one to one mapping between JSON and SSZ regardless. Many binary protocols do probuff for example has a canonical mapping. And it's just convenient to document how we do it in the tests. So that's basically what that PR does it documents how we encode SSZ. When we want to present it to predominantly humans in JSON in YAML and so on. Initially the PR assumed that everybody thought that 8 bit integers and bytes are the same. But then there were many Java developers and JSON developers upset about that. They really think that bytes are different from 8 bit integers. So the new version of the PR doesn't change any of that. It also doesn't change the one thing the one place where we actually use an 8 bit number. The participation flags of the debug State API which is mostly unused. There we have a Flags field I'd say that's a bite but for historical reasons that's an integer. So the latest revision of the PR it really only documents our existing practice it kind of takes all the SSZ type that we have. It gives them a corresponding JSON encoding. And if somebody like the beacon API’s spec wants to base their work of that. We can drastically simplify the beacon API spec because right now what the beacon API spec does is that it declare is kind of a myriad of little types for every field every field has its own encoding and that's just a mess. This one and that's because the beacon API spec is written such that it depends on the specific object types that we declare later on whereas if we have this canonical mapping. If you're writing a JSON library on top of your SSZ library you don't have to consider specific types anymore you can just rely on these or SSZ types to fully Define, how to encode JSON. So I think not that I necessarily agree but I've removed all points that anybody could disagree with so far that people have disagreed with from the PR. And I think in that version it shouldn't should be kind of a no-brainer to just put it into the spec. And then whatever  discussions we want to have over bears on the relative importance of the byte. We can leave them for later. that's it. 

**Danny** [39:02](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=2342s): Any questions for Arnetheduck? Any opposition? All right I'm going to Ping Discord about this and try to get any final comments. And then we can need a merge. Thanks Jacek. 

**Arnetheduck** [39:48](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=2388s): Lovely to get this off my list.  I hope. 

**Danny** [40:00](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=2400s):  Yeah I didn't when I said it September ,I didn't look at the referenced PR that was from 2022 while ago. The original Let's help Jacek with his list.
Step one little Indian step two just on mapping.

**Arnetheduck** [40:26](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=2426s): At this pace I'm going to have to find like a new like a new Hill to defend.

**Danny** [40:33](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=2433s): I'm sure we can find something for you. Okay that is all we have on the agenda for today. Any other discussion points before we close? Okay thank you very much. We will work on getting a release out absolutely as soon as possible. Getting these final all points in and thank you everyone. Take Care.

**Stokes** [41:23](https://www.youtube.com/watch?v=dAStyB2Vv4s&t=2483s): Thank you.

# Attendees
* Danny

* Potuz

* Guillaume

* Ben Edignton

* Kasey

* Pooja Ranjan

* Enrico Dell fante

* Stokes

* Terrence

* Tim beiko 

* Mikhail Kalinin

* Paritosh

* Sean

* Andrew Ashikhmin

* Roberto B

* Pawan Dhananjay

* Tony Wahrstaetter

* Carl Beekhuizen

* James He

* Anna Thieser

* Arnetheduck

* Marek

* Marcin Sobczak

* MauriusVanDerWijden

* David

* Phil Ngo

* Nishant

* Zahary

* Daniel Lehrner

* Lightclient

* La Donna Higgins

* Justin FLorentine

* Ahmad Bitar

* Stefan

* Trent	

* Joshua Rudolff

* Tukasz Rozmej

* Fabio Di Fabio

* Caspar Schwarz

* Ignacio

* ECO

* Hsiao-Wei Wang


# Next Meeting: Nov 16, 2023 at 14:00 UTC
