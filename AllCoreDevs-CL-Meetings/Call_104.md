# Consensus Layer Call 104

### Meeting Date/Time: Thursday 2023/3/9 at 14:00 UTC
### Meeting Duration: 57:48  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/738) 
### [Audio/Video of the meeting]( https://www.youtube.com/watch?v=C5SmmkriuwA) 
### Moderator: Danny Ryan
### Notes: Metago

### For quick summary: [Ben Edgington](https://hackmd.io/@benjaminion/BkIOGvPy2)

## Intro

### Capella

**Danny**
Hello, welcome to ACDC 104. This is issue 738 in the PM repo. Looks like a relatively light schedule, at least as planned, Capella, some spec discussions around the merge, and any sort of closing remarks, and a quick SSC shout out. Okay, cool. So start with Capella. I believe Goerli is imminent. Is it Tuesday? So call it five days, any announcements or discussion points around Capella? Tim? 

**Tim**
So we have the blog post out, which has all the client releases except Nimbus, I believe. So expect an update to the blogpost Nimbus, and if they have it released out, maybe they can give it a shout. And then on Monday at 15:30 UTC, we're going to have another community call to answer people's questions about Capella, Shanghai, if a couple folks on the client's or research slash spec team want to show up, that's always great. People usually have clients related or spec related questions. Yeah, it's pretty much it. Oh, sorry. Yeah, it's stakers doing a live stream. This is in the blog post as well, but so it's at 10:25 PM UTC on Tuesday, its stakers going to start a live stream at 10 PM UTC for anyone who wants to watch the actual upgrade on Goerli. 

**Zahary**
And the Nimbus release is being prepared as we speak. It's likely to be out today. 

**Danny**
Okay. Great, we'll update the blog post then maybe tweet it. 

**Ben**
I asked question about BLS change credentials. Is there are any plans to flood the network on Goerli at the change or do anything which looks like what we expect to happen on mainnet. 

**Danny**
Not in a concerted effort, not a playing concerted effort. The teams could spam a portion of them if they want. I don't believe that the devop team has. 

**Pari**
Yeah, we don't have any plans to do this on Goerli. We have done so in devnet in the past and haven't noticed any real issues, but if there's concern, then we're happy to coordinate that for Goerli. 

**Danny**
Yeah, I guess it's if it's possible why not, especially Goerli probably has more nodes than the networks we've run so a little bit of different gossip pattern. Granted, I would withhold some amount just so that we don't have forego the ability to test further BLS changes in the future. Okay. Other compiler discussion points for today.

**Terence**
I have questions about builder and relay rating. But I don't see the relevant parties here. So there is an MEV boost community call an hour after this ends. So if you're a builder, you have questions. Feel free to join that call. 

**Danny**
Thanks, Terence. Is there's a link to that? 

**Pari**
And just following up on that one, we did have a couple of MEV related scenario testing. So we had Mario's mock relay running on mainnet shadow fork two. And we asserted that the circuit breaker works with taking the relay offline, asserted local block production, having X number of blocks missing in a row, or in an epoch and having the release of invalid data. 

**Danny**
Fantastic. Thank you Pari. Okay great. Other Capella related discussion points for today. Okay. 

### Deneb [11:06](https://www.youtube.com/live/C5SmmkriuwA?feature=share&t=666)

Moving on to Deneb. We did have a, it seems like one of the most lively discussion points still, is giving this beacon API's blob signing PR emerge. Sean, we did discuss this on Tuesday. Is there a status update? 

**Sean**
Yeah, so I think on Tuesday, we were thinking we would have blobs just blinded by default in both, both current block production end points. But further discussion on the pull requests, some other like use cases were brought up for having like the full block signing flow also included full blobs. And that would be good for that would be good for like separating a beacon node you want to use for proposals versus like a beacon node you want to use for verification. And also like broadcasting sign blobs to multiple nodes. So I think there's enough like of a desire to have unblinded blobs in the current full block flow that updated the PR to reflect that. 

**Danny**
Does that mean you can optionally have them blinded? 

**Sean**
So how does right now is like we have one endpoint for full blocks and that will now include full blobs as well. And then the blinded block endpoint also includes blinded blocks. 

**Danny**
Okay. Okay. So we have the like the stable endpoint for blinded and then 

**Sean**
Yeah.

**Danny**
…kind of like state. Okay. Okay. Gotcha.

**Sean**
And then the other thing is I think people are on board with having just like a single request to submit a signed block and all signed blobs as opposed to like splitting up that request just because it reduces like the complexity around like when the beacon node response to a message about whether it's published a gossip or imported the block. It simplifies that. And then one other point that's been brought up on that PR is generally like, should we keep in mind like means of providing blobss from like a remote source that isn't a P to P and like design these APIs. And so there's still active discussion around that point. Maybe we should move it into an issue somewhere else, but the idea is that…yeah, the idea is that like obviously like home stakers who have their limit with bandwidth might not be able to follow via gossip. So having like a remote blob server might help these cases, even though it's obviously better to be participating in gossip. Maybe a remote blob server is something that's like better than forcing home stakers to exit the validator set. 

**Danny**
Is this independent of production or do you mean our remote server to get them for production? 

**Sean**
So I think both for production and for just following the chain. 

**Danny**
Okay, but that should be relatively independent of this PRA. 

**Sean**
Well the. An idea was brought up that maybe blob provisioning like or providing blogss shouldn't be a beacon node responsibility. Maybe it should be like a separately defined API that a beacon node could implement. That was the question. 

**Danny**
I guess to keep the devnets moving. I'd love to get the first and shift that to an issue. It seems like a deeper discussion point than just the base signing here. 

**Sean**
Yeah

**Dankrad**
what's mean by providing blobs? 

**Sean**
Like just an API to like a…

**Dankrad**
Providing to…

**Sean**
for example, like if you want to sync a node, you could add a like a remote server that sends you a blob for each block rate you request. So to a beacon node for following the chain and to a validator client for producing a block. 

**Dankrad**
Right. Yeah. Okay, so like providing, but I didn't understand that part because it's still the beacon node that verifies the availability of all the blocks. So I. So like the beacon node needs to get all the blobs. But I guess there's a question of how do they get to the beacon node, right? So that could be an internal functionality via ? or an external block provider. Is that what you're saying? 

**Sean**
Yeah, it's about like should we keep, I guess, remote servers in mind when designing the APIs for like how you would achieve blobs for different roles? 

**Arnetheduck**
I would say probably no. Like we have an interface for getting blobs right already. But the other point is that we're in parallel also investigating ways to minimize the bandwidth impact of blobs in general. So like I'm hoping that most of the additional bandwidth will be able to regain through optimizations and then blobs and blocks aren't like the biggest consumer. They're big, but like at the stations take up a lot of bandwidth as well. Those are the most problematic ones. So I mean for the purpose of producing a block, I think. We have to assume that the beacon node has the blocks and blobs and then we're designing this particular API for the purpose of signing. And you block and blob. So whether or not there exists a separate facility for downloading blobs somewhere feels kind of orthogonal really. And then point. 

**Gajinder**
I think there is another aspect to where we basically say that beacon nodes can link up to an external service ? the other blob, which is really not gossiping the blobs. So there are 2 kinds of beacon nodes which are being proposed as of now. In this particular functionality is that some beacon nodes will process the blob…? gossip and other beacon nodes which will not and which will then use this external service to come the block. So overall…bandwidth for them because even if they pull from external block and they still have to gossip and then with some time doesn't go away. So this is I think the additional concern that it's also raised in the PR comments regarding not getting the block from an external service. 

**Danny**
So I'm of the mind that the parameters here given in addition to the algorithms available should be tuned such that home connections can use this and that if we're beyond those limits, then we should be rethinking those limits and the optimizations available rather than hacking a centralized server into here. 

I will also echo to a Yaasic’s point that the box by root and box by range requests already do allow you to get blobs from an external server. Obviously that's generally tuned to the p to p but you could have a service that relies on that you could have direct peer to peer connection that relies on that and so it seems like reusing that is actually the appropriate path rather than having this creep into the beacon APIs or am I missing something?

**Gajinder**
So in the external configured blob provider, basically there would be two beacon nodes which might not participate in the gossip of the blob

**Danny**
So even in such a case, you could not be on not that I'm advocating for it, but you could not be on the blob topics, but you can still publish into them. And so you could publish to one peer into them or a couple of peers into them and not be on that topic and still participate. They're still push out so I again, I don't know. I don't know if the beacon APIs needs to be handled at facility. I do think we should take this to an issue. Because this is certainly a departure from assumptions and design. And I think a lot of people have insight that went into. 

Sean, would you mind opening up an issue and summarizing the discussion up to this point? 

**Sean**
Yeah, sure. I think I get, should I open it on the specs repo because it was brought up in the APIs, but I think it's sort of a broader question? 

**Danny**
Yeah, that's probably reasonable. Right, because it's not just APIs, it's how to use gossip, how do you think of that kind of stuff and the resource environment. 

**Sean**
Okay. 

**Gajinder**
And another thing I want to bring up, sort of clarification on is that currently the blinded drought we use for build a block. But more and more like it seems like you know blinded drought from normal execution blocks would also be a good, for things. And so, can we add some sort of end point or some sort of flag for that that this is an execution block from the blinded ? produce ? published by?

**Danny**
I'm having trouble hearing your mic. And so I didn't quite catch the question. 

**Gajinder**
Am I audible now? 

**Danny**
Yes. That's a lot better. Thank you. 

**Gajinder**
Okay, so one thing is that currently we have blinded droughts for builder blocks and for execution blocks we use full routes. Now with the blob being full on the full on the execution block routes. I think it would make sense if we can sort of add another end point or some flags to indicate that we've won execution block on the blinded route between the communication between validator and beacon node. 

**Danny**
Like if somebody wanted lighter weight communication, even if they were the beacon node had the full blobs. Is that what you mean?

**Gajinder**
Correct. 

**Danny**
That does seem like a reasonable configuration parameter. I don't know. Would you put that in the request itself?

**Gajinder**
Yeah, sounds good. I have added in the comments, but I'll sort of clearly mention it. 

**Danny**
Okay, gotcha. 

**Arnetheduck**
There is one more related question. It's also brought up in that issue, which is basically that should the blinded block end point provide non blinded blocks like or other, like if you get a block from the execution layer, which is not blinded should you respond with that block on the blinded request, meaning that the beacon node has to keep it in its state, while their client is signing. 

**?**
So we get blinded and we get ? because the response of that idea is by design, blinded. So the VC's spec expects it as a blinded. 

**Arnetheduck**
Yeah, indeed. And, and like we don't so we had an issue about this or somebody was asking about it. And like the spec doesn't really say that you should do that. Like, what I'll catch this. 

**?**
Sorry, just a question. What about the flow is ssz because you don't know in advance if it's blinded or unblind that even if the milestone is the same. So are you JSON based on the or what do you do when SSZ encoded. 

**Arnetheduck**
Well, we have to request right? One gives you a non blinded block and the other one gives you a blinded block and on that non like we assume that the validator client will do the kind of like multiplexing or selection of which of the blinded and non-blinded blocks to use. And so then we don’t have to really keep that in the beacon node. Because then the beacon of the stateless with respect to block production, it doesn't have to cash unsigned non blinded blocks ever. 

**Danny**
Right, but it does seem like if somebody's using the stable access point, the assumption is…you're saying if somebody uses the the stable access point, but you have the full block, you should just put it in the in the request so that it can be stateless in that mode. 

**Arnetheduck**
Yeah, I mean, thats certainly a convenience because then the beacon node does not have to remember anything. The beacon node is kind of forwarding, you know, data from either the proposer, like the block builders or from the execution layer. But it doesn't have a real interest in what happens in between, until the block is signed at which point it includes it in its own chain. Sort of. Its this middle state where the block has been produced by the beacon node. But it hasn't yet been signed so it's not part of any canonical history. So it needs its own little space and right now in my reading it's ambiguous whether beacon nodes should support this or not. 

**Danny**
Would you actually throw it away though, like isn't it actually good to keep it because you it has pre compute and other things on it. 

**Arnetheduck**
I would actually throw it away. Yeah, I mean that station pulls and so on like when you build a block, we capture a snapshot of the at the stations at that time. And then then the validator client would sign it and return it, but it could be that the validator client decides that it doesn't like that block and asks again right and then we would build a new block. Or we could have like multiple validator clients and cases like this. It's like that intermediate cash. It's kind of I see it as a bit annoying. I would have preferred actually a single request. That gives you either a blind or a non-blinded block depending on what the beacon node chooses to produce and then the validator responds in kind. So it gives back all the data to the beacon node that the beacon will give it that would have been my ideal design. 

**?**
Yeah, to have them completely unified and maybe introduce some other headers that says, oh, the beacon node is respnding back with this particular the blinded or unblinded version. So even if we are going in SSZ, the VC can can do the coding accordingly. 

**Arnetheduck**
Exactly, exactly like that. One unified question. 

**Sean**
Yeah, so is that something we would want to try to migrate to as we're like changing these endpoints for blobs, because like I agree it does sound nice and we have actually seen misproposals before with lighthouse in this interaction between like the blinded flow and fall back where ike you're switching beacon nodes and we like assume the beacon node you're talking to has the block cache so that design does sound better. 

**Arnetheduck**
I mean, it's in the peeling moment in time because we have to muck around with that request anyway. 

**Sean**
I'm happy to make the updates if people are all in board. 

**Danny**
Yeah, no opposition. Cool, anything else on this or beacon API is in general? Great. Other than a discussion points for today. 

**Etan**
I mean the SSC stuff is. 

**Danny**
Yeah, you did drop that link. Yeah, if you want to give us the update on the link you just share, that’ll be great. 

**Etan**
Yes, essentially I was asked to create this summary of all the EIPs that are related to transitioning the micropatricial tries to SSC. It is something that is that will be looked at by all teams, especially the execution teams. Just to review them provide any feedback I had a discussion with Marios today in the Sharting data channel. I also linked it from type transactions that's the canonical channel. Would be great just so that we could discuss it next week maybe

**Danny**
Okay, thank you. Any further comments or questions on here before we move on? 

**Arnetheduck**
I could talk about a PR that I raised as part like. It was mentioned during the for it for for decouple development, which is basically that when we receive a block or an attestation, we don't know the slot of the parent or block that this entity is derived from, right? For example, when we receive a block we don't know if the block is building on the parent that is already been finalized if we don’t know the block route of the parent and the same thing for attestations. 

We don’t know if we are receiving kind of like a block route or a block that was very old because we never transmit slot, only the block route right? What we have to do is we have to do another to discover the slot and figure out whether we should keep these other things around. So there's a PR I open I don't have it in front of me right now so I don't remember the number but I'll post it to the consensus dev channel. The idea is to include the slot whenever we have a block route in the protocol. So that's kind of like in the attestations So that's kind of like in the attestations you put there's the beacon block route. You could also put the beacon block slot in the block. You could put the parent slot. And so on and so forth. I wanted to gouge interest for this. It's kind of like a small change which enables a few more checks. Like a few more sanity checks before we allow gossip and it closes a few little loopholes that otherwise require resorting to let's say uglier constructs like bad block lists and things like this. I did not finish the PR in the sense that I provided an example of what it would look like but I haven't really gone through all the possible places where the slot should be. 

If there's like a clear no right now and then I'm just going to close that PR and save myself the work. If it’s a maybe then then then I can invest in some time in it. And if it's a yes, then I can invest in time in it with urgency. So if you fall anywhere on that scale, do let me know. 

**Danny**
Yeah, I'd love some engineering input here or on that PR to know that if others see similar issues and similar gains here. It's 3249 on consensus specs. I certainly understand the motivation. But you all would know better. The pain. Okay, if you haven't taken a look at that and have an opinion, please do and leave a comment. Okay, other than that, discussion points.

I believe Guilm has joined us. There is the verge. Verkle stateless spec graphed up in the consensus specs as a PR spin up. A little bit more than a month. Just been a little bit of review but you know once he goes a quick walk here to let us know what's on this feature. 

**Etan**
You're muted. 

**Gballet**
Okay. Yeah, so just one identity to make a very quick introduction. So there's that PR that's called this number. Yeah, 3230. And the idea is very simple. You just add to the execution payload you add a field execution witness. And this is a structure that is described further down the documents. So we don't have to go through every single field. But basically, yeah, well, one of them, one of the points of bringing that up today was to get your attention on this. But also, there's a couple of questions I wanted to raise. And one of them was that both the execution payload and the execution payload header have the entire structure. And this structure can be fairly big. So I wanted to figure out what the opinion was should the header contain the entire witness or not. If not, I suppose with the witness would be transferred a different way through a different type of message. 

**Danny**
And how big?

**Gballet**
 Well, I mean, it's in JSON, it's like an array of values, of three values. I didn't get exact numbers. So we just, by the way, I wanted to say we just relaunch Calstinem with this format today. Like a couple, a couple of hours ago. So I didn't, I didn't get exact numbers. I can, I can share that a bit after the call. But we're talking about an array with a thousand entries. 

**Danny**
Right.

**Gballet**
We do? I'm talking about the JSON itself. I don't know. Yeah.

**Dankrad**
Wait, why is this in JSON? 

**Gballet**
Because it's for the source. I mean, that's true. There's, it's also passed over the network, but this, this field is provided by the execution engine, the execution layer. So it also has to go over the JSON RPC. 

**Dankrad**
But like as binary, we know it's like probably like hundred kilobytes for typical block and up to two megabytes for in the worst case is that our estimate?

**Gballet**
 Yeah. Yeah. 

**Dankrad**
And yeah, with JSON, like probably a factor of like a bit more than two on that. 

**Danny**
Yeah, my question would be, do you need the execution payload header? Like are there things you can do with the execution payload header where you need the entire execution witness. Or is it if you had the execution payload header and maybe you're doing like lightclient things, you just need a portion of the witness or not of the witness. And otherwise you get the whole block. 
So if you're a state full clients, you don't, you don't need really the. 

**Gballet**
Well, actually, I mean, you could, you don't need that data. You can get it from your own state. And if you're a stateless client, yes, you will need the entire payload. 

**Danny**
But you also get the entire block, right? You wouldn't just get the header. 

**Gballet**
Right. That's true. Yeah. Ok.

**Danny**
I guess I'm curious if there are use cases where you'd want the header, but the whole witness. 

**Gballet**
Yeah. 

**Danny**
And that would, that would help me understand if you'd want to ship this with the header, because my gut is to do the root unless there are some sort of use case here. 

**Gballet**
Yeah. 

**Dankrad**
I mean, that could be, that could be a case for it. And some sinking type use cases like where you have a trusted source for us. And you just want to update….you need to update your state… 

**Danny**
But it doesn't know if it's, but even then you could download the witness….facility

**Dankrad**
Yeah. But most of the time, I think if you want a witness, you also want to fill the sexecution payload. 

**Danny**
Right. Okay. 

**Gballet**
Okay. So yeah, I think, I mean, I can modify this to be just a root in the header. And if indeed there's a need, we can change it again. But yeah, I don't see any immediate need for that in the, like for the whole witness in the header. 

**Danny**
Yeah, that's my intuition. Cool.

**Gballet**
So there's a second point I wanted to address or atleast raise. This is the transition when you perform the upgrade. So the execution witness, I suggest would be empty because it's not really clear to me what's supposedly before the transition, the state is still officially an MPT. So it's quite difficult to, and potentially not really necessary to have a proof that would be proving dif between MPT and Verkle. So currently, my proposal is to have two empty fields on the transition boundary. So only have the execution witness after one block past the, past the verge. Yeah, I just wanted to see if anybody had any opinion about this. 

**Danny**
Yeah, it's unclear to me how we would do a different case here. So, it's intrucible, but if there's a different option, I'd love to hear it. 

**Gballet**
No, I don't, I mean, at least I'm not aware of any other option, but yeah, if someone, if someone is, I'd love to, I'd love to hear from them. 

**Danny**
Yeah, like you don't really have the option even do a pre compute because that's that block came out of lie and you don't have a lot to get so. 

**Gballet**
Well, I mean, in theory, everybody would have a, like a very already representation of the state, long before the transition. So you could still provide a proof with respect to this state that is not officially enshrined in the blockchain. Yeah, you could, like in practice, everybody will have this, this verkle state. But in theory, you could do the transition at the last moment in theory, never going to have work for real, but. But yeah, no, I think I think this is still the most, yeah, sensical approach. 

**Danny**
I'm taking a look at it all think about if that like, messes of any proof stuff that I would just probably with it. 

**Gballet**
Yeah, okay, great, thanks. And there was the last thing. It's more like a nitpick by a deplion. Where is it like he was saying yes, so you have those two fields CL and CR. Oh, he actually answered since. But yeah, this represents some symbols that are in the paper, the IP, IP, paper, paper. So it has to be read like your lab tech. Feel like C underscore or subscript L and C subscript R. But apparently in the specs things tend to be lower case. So I was just wanted to ask if lower case C underscore L and lower key lower case C underscore lower case R was the sufficient or not. 

**Kevaundray**
I think that uppercase was basically used to show that the CL and CR are just commitments. So it might be fine to have the lower case, but according to this book. 

**Gballet**
Okay. Well, if there's no other, if there's no dissenting opinion, I'll change that to be like this. 

**Danny**
Some live code review, I think you mean colon instead of equal sign here. 

**Gballet**
Possibly. Yeah, I don't know that much Python, but okay. Good, thank you for putting that out. And with that, I think yeah, that's that's pretty much all I wanted to discuss today. 

**Danny**
Is this built upon Bellatrix or Capella? 

**Gballet**
Right, yeah, it's so it's built upon Bellatrix at the moment. Yeah, it doesn't have a Capella like he's not rebays on top of Capella. The code. So I mean, the goal is to have it on top of deneb, obviously, but currently it's Bellatrix. 

**Danny**
Yeah, okay. Cool. I guess keeping in Bellatrix for initial review seems fine and maybe letting deneb. So going to be able to stabilize and then re-basing on that instead of doing three bases. 

**Gballet**
Yeah

**Danny**
Great. Great. Are there any other like gotchas in here or is this primarily data structures on the consensus side? 

**Gballet**
It's, yeah, exactly. It's primary data structures. There's a gotcha indeed. It's where is it? So there's something. There's a bit of a twist for Calstinen. I'm looking for the structure. Exactly. I'm looking for the structure. So there are two values in this truck while three fields in the structure current value, new value and suffix. So we don't have new value. So ultimately, you should have the pre state and the post state, but for Calstinen, we just put the pre state. 

**Marius**
Why? 

**Gballet**
It's just like it's just more maintainable at this point when more people join when codebase stabilizes. It will be easy enough to add. 

**Marius**
So you can already compute the codebase. 

**Gballet**
Yes. 

**Danny**
Okay. Thank you Guilm. Yeah. Any other questions for Guilm? 

**Etan**
This is optional is this an SSZ? Do you need SSC unions or just optionals?

**Gballet**
So used to be unions, but Mikhail said that now optional was added to the to the spec. So yeah, it's an SSZ optional. 

**Etan**
It's still a proposal like a draft, but if you don't need the union, then I guess writing it like this is the cleanest. 

**Gballet**
Yeah. So it is currently at least in the code it's implemented as a union. Yes. 

**Danny**
Okay. And then yes. 

**Gballet**
Actually, there are no more questions. I had a I had one. So Deneb is the name for fork 4 and  ? and… back in in Australia suggested Electra. So do I have the permission to start referring to this as electra? 

**Danny**
In terms of the name of the fork. Yeah. I guess as long as it stays in this underscore features directory, I would give it like a feature name because the fork ultimately might be this combined with some other features. And, you know, there is a modicum of a pocess for deciding fork names. So maybe we should respect that. But again, like having something in underscore features as like a star name, would I think be confusing and this should hang out and underscore features until closer to ? fork so we can kick that can down the road. 

**Gballet**
No problem.

**Hsiao**
I have a question. So how ready is this pr right now, like this is a still a draft. So I didn't go review it, but if we want to merge it to the future. So then we should make it executable and then we will found many small and big bugs in this process. 

**Danny**
Right. 

**Gballet**
**Gballet**
Well, there's so we have a running testnet at the moment. So I'd say it's pretty ready. But yeah, before we enshrine it this way, I assume other clients should implement it. I know Nethermind like Tanishk has also an implementation of verkle trees. I don't know how far along he is from implementing this specific spec, but I would say I would wait for tanish. Well, Nethermind, at least to catch up to this spec before we before we merge it. 

**Danny**
Cool. Okay, anything else here. Thank you. Thanks. Any other general spec and research discussion points for today. Any other discussion points or closing remarks before we close. Excellent. Okay, seems like high priority. Continue on this beacon API's discussion. Sean, please ping relevant members when you do the next update. Otherwise, bunch of small discussion points that will continue and issues and ? talk to you all soon. 

**Everyone**

Thank you. Thanks everyone. Bye. Thank you. Thanks. Bye. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you.


### Attendees
* Danny
* Marius
* Kevaundray
* Etan
* Dankrad
* Terence
* Gballet
* Pari
* Hsiao
* ethDreamer
* Pooja
* Trent
* Tim
* Ben
* Zahary
* Crypdough.eth
* Dhruv 
* Stokes
* Carlbeek
* Saulius
* Gajinder
* Mike
* Sean
* Mikhail
* Peter
* Phil
* Marek
* Fabio
* Anna
* Protolambda
* Ayman
* Arnetheduck
* Barnabas
* James

