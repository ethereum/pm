# Consensus Layer Call 110

### Meeting Date/Time: Thursday 2023/6/1 at 14:00 UTC
### Meeting Duration: 1:01:06
### [GitHub Agenda](https://github.com/ethereum/pm/issues/796) 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=050Jq9lO838) 
### Moderator: Danny Ryan
### Notes: Metago

### Deneb

## Pending Deneb Changes

# [Add data_gas_used field to ExecutionPayload consensus-specs#3391]( https://github.com/ethereum/consensus-specs/pull/3391) , [Change excess_data_gas and data_gas_used  type from uint256 to uint64 consensus-specs#3392]( https://github.com/ethereum/consensus-specs/pull/3392) 


**Danny**
Hello, welcome to consensus layer ACDC call 110. This is issue 796 in the PM repo. Here's the link. Looks relatively light, but we shall see. Got a couple of Deneb things. Research spec thing. Actually, some things not on the agenda.
And I'm going to go over. So there are a couple of pending Deneb changes that came out of the 4844 call on Monday. This is to, and this has parallels to the execution layer. So it's primarily updating the data structure. So adding data gas used field to ExecutionPayload and changing the access data gas type from uint256 to uint64. These are both very simple. They're approved and will be merged today. The intention barring anything unexpected happening probably on this call is to have a release out tomorrow for the updated testnets. Does anybody, is the related PRs for the EIP have those been reviewed and merged or are they still pending because that's kind of we're just waiting on that to push these through. 

**lightclient**
So if the adding the data gas used to the header is, yeah, it's getting merged momentarily. There's a couple of white space things, but on-screen just approved it. And we talked about on the call on Monday. So everybody was okay with it. Yeah, that'll be merged. Yeah…going to have to look at the changing the size. Yeah, we haven't discussed that at all. That kind of came after the call on Monday, So would like to just discuss briefly here before moving that into the EIP.

**Danny**
Right. So again, that's the access data gas going from a uint256 to uint64. I think if we look at the execution layer payload, there’s most fields that can’t fit within the 64 bit type to utilize the space savings. There's no concern that this would go in excess of 64 bits, right?

**Lightclient**
Yeah. The pr had some numbers, I think the biggest it would get, it's like 28, 29 bytes, 30 bytes. Sorry, bits.

**Danny**
And the this is bound generally by the supply on main net. If you had, you know, some crazy amount of supply, you could break that invariant?

**lightclient**
I would need to see where it breaks, but I think. Yeah, I don't even know if with 64 bits that allows, I think that like that would be more than the representable amount of way in a uint26 in general. I guess the account has a uint56, max.

**Danny**
Is anybody opposed to this? I think we're pretty fine on the consensus layer.


**Terence**
Not the poll, I just have a quick question about the proper ordering. Is data gas used before excess data gas…because the consensus spec pr is different from the EIP.

**lightclient**
Yeah, In EIP, its data gas used and then excess data gas.

**Terence**
OK. So the consistent spec needs to be said.

**Danny**
Yeah, we might have. It's not broken if we don't follow that ordering, but we very much might as well follow that ordering. OK, I can make a note of that. OK, cool. Is there enough execution layer representation here that we feel comfortable with changing the bit size on the payload or do we need to have a round from the one?

**Andrew**
Ok from Erigon.

**Danny**
OK, is anyone opposed? Because if not, why don't we drop it into Discord and get this merged quickly? And we can get the release out in the consensus layer. Can someone do a quick blurb on Discord to ask if any opposition? It's ceremonial. I don't think there will be any or could be any. 

**lightclient**
I'll post it. 

**Danny**
All right, cool. Thank you. Anything else on these couple of minor changes? Great. Alex, do you have an update to 4788, which is still intended to be included? Alex, can you give us that update?

## [4788 updates -- Update EIP-4788: key beacon roots by root EIPs#7107] (https://github.com/ethereum/EIPs/pull/7107) [9:38]( https://www.youtube.com/live/050Jq9lO838?feature=share&t=578) 

**Alex Stokes**
Sure. So there's a PR with the change to the EIP. No changes at the consensus layer. So basically from the CL, you're doing it at this point, SNR over the root itself. Say in the Engine API, we had discussed maybe sending the slot over and using that to change some of the UX from the pre-compile that we'll get to in a second. But that seemed a little clunky, and basically, it's kind of move away from that, the question is, what can we do without say that slot
information? So the CL will send over the root, and our question is how are these groups organized? And the EIP is here for 4788. Its PR is 7107. And what this does is basically change this so that we basically have the timestamp and the root inside the EVM that's written into this pre-compile, so the state of this contract as a pre-compile, which you can call. And yeah, really the last question here was how we key these things, how they're organized and the state of this pre-compile. And there's a little bit of optimality here. Ultimately, the simplest thing we get from the EL's perspective is we have the timestamp from the header, and then not this root. And that's kind of what the EIP proposes, is just adding the root to the header as well. So you have these two pieces of data. 

And now the question is, how do you write them to the pre-compile? What this pr does that I just posted basically writes the root and then the value to that key is the timestamp, just itself. And then the question is basically, OK, is this useful to anyone? And basically what this does is say, there's now a set of all the valid beacon roots. And if you know it's in the set, because you get back an actual timestamp, rather than say 0 or something. And yeah, generally, all of the thinking pools and different people in that space that talk to you are ok with this change. Yeah, there's one maybe question around bounding the size of these things. So right now the way it works is you would just, for every block, you would write parent beacon roots timestamp and just keep going.

Or an earlier version basically bounded this with a ring buffer. So we might want to add that back in. Otherwise, it's looking like 80 megabytes of state growth per year, which is not nothing. So yeah, I think we're going to have time to look at this PR. We're thinking about these changes. 

**Danny**
Yeah, I mean, my gut is to not have some unbounded state growth here, especially given all the sense that we have these double back mercantile accumulators and try to keep anything unbounded pretty small. I know this is relatively small. But yeah. 

**Alex**
So another option is rather than do root to timestamp, do timestamp to root, and then it becomes much easier to handle bounding them in time. 

**Danny**
Right, and then the impetus is on the 

**Alex**
The caller to juggle. Like, OK, if I'm going to prove something at the slots, then I need to figure out which timestamp that was. But that's not a huge ask. 

**Danny**
And the people constructing transactions have access to APIs. Yeah, I guess the other thing, you could have some weird map where you have time A and time B. And you always alternate between which one you're writing to. Or I guess you don't want to clear out memory like that. Never mind. 

**Alex**
So yeah, I mean, there's different more complicated constructions you can think of, but it's simpler to say. For example, you could say, OK, if you
want this many seconds worth of data, then basically just take the timestamp mod that. 

**Danny**
So yeah, I know we keep picking this one back and forth a bit. I would imagine execution layer people have a bit more opinion here. I'm definitely of the…it seems like kind of just…not the right word, but if we can avoid having unbounding growth with a simple change, I would lean towards that. 

**Alex**
Yeah, OK. I mean, I tend to agree. There's no reason to have this extra thing for fun and for state growth. So I'll make a pass on trying to do that. And have it ready for the next all core devs next week. 

**Danny**
Right. 

**Alex**
In the meantime, if you're listening, take a look. 

**Danny**
Are any other comments or questions for Alex? Great. 

## [6988 proposer shuffling invariant change EIP-6988: Slashed validator cannot be elected as a block proposer consensus-specs#3371 (comment)]( https://github.com/ethereum/consensus-specs/pull/3371#discussion_r1212357111) [15:22]( https://www.youtube.com/live/050Jq9lO838?feature=share&t=922) 

And then, Mikhail and I were discussing some stuff that comes out of 6988, which is that proposal, proposal shuffling mod that proposers can't be slash. And it looks like it might break at least a property that we have today. Mikhail, how can you give us the update on that one?

**Mikhail**
Yeah, sure. So there is the 6988 EIP, which makes the slash whether or not eligible for to become a proposal. If slash happens like within an epoch, it may change the proposal set for this epoch. But currently, we have this invariant
that the proposal shuffling remains unchanged throughout the…So this, like this, speaks, may break any cache in the beacon node or in the validator clients that we have and that the clients may use on the proposal shuffling for the current epoch or for the current epoch. And also, it can break some tooling.
So that's a question that I think is very important to discuss before we decide to have this change. 

**arnetheduck**
I'll just say right there that computing and you shuffling is very, very expensive.

**Mikhail**
Even on the proposal.

**Danny**
Sorry…about that, Mikhail?

**Mikhail**
I was just going to say that it's not like probably in this case, you don't have to compute to recompute a shuffling. It's just about if a proposal that you have in this cache, one of the proposals becomes slashed. So you have to swap this proposal for a particular slot with a new one. Yeah, probably it's also computationally intensive. What worries me more is that there is a cache on, for instance, whether a client side and whether a client will have to do some additional requests every time because it or otherwise will have to track slashes with which sounds like a quite lower hat for a rather client.

**Terence**
It definitely brings more complexity. I mean, yeah, for prism, you break our current safety in terms of using a proposal to the cache. I mean, it's not doable.
I mean, we can definitely fix that. So yeah, I don't. Yeah, so I think that's our stance.

**Danny**
Yeah, I mean, from my perspective is definitely realizing this. Like a higher complexity change than we expected a few weeks ago when we greenlit this one. So I guess where I'm at is do we have the confidence to move forward on this? Or do we want to put this in the back burner to do a deeper analysis and slots in some other time? I guess it's not really analysis of the spec. We understand the spec. It's just how much complexity it brings into clients. 

**arnetheduck**
I mean, the value that it learned, it has to assume that the proposal shuffling
can change anytime, anyway, because of reorgs. So I don't know if that's a big deal. 

**Danny**
Yeah. Right. So it's constantly reassessing. 

**Mikhail**
Yeah, a question to Terrence. So the recent cache that we used for that is attached to a fork, right?

**Terence**
Yeah. 

**Mikhail**
OK. Just assume that probably whether client can tap this kind of this type of cache. I don't know. So it's probably, yeah. Anyway. Yeah. Yeah.

**Danny**
But it brings up another interesting point, you can still propose just not on the parent or the ancestor that could slash you, which in the normal case, you then would be reorged. But it does bring in kind of like a weird side dynamic here. So zooming out, there are things that's 4788, there's 6988, there's 7045, and there's this fixed voluntary exit domain, which might have an EIP as well, that we intend to build down into the Dineb spec over the next couple of weeks
to introduce these relatively small features in relation to 4888 into the spec. 

So given that timeline, I guess we could focus on building the other three into the spec, I meant 4488, I said, no, no, I'm not going to realize it was totally wrong. But we could focus on building these other three into the spec to keep the discussion open for 6988, because this just came to light in the past 24 hours and readdress it in a call in plus two weeks. So likely, before that call, we'd have the other features built in for a release and then can make the final call in 6988 at that point. Anybody oppose that? I think it's a little bit of time to talk about this one and think about the engineering implications. 

OK, I see one thumbs up and hear no opposition. And that was a point I wanted to make as well. I meant to make an issue before this call, tracking the features that we tend to build into Deneb from here. I did not, but I believe that list of four is correct. Did I miss anything? 4788, 6988, 7045, and the Dapp Lion voluntary exit domain, which maybe has a number or not, I'm not certain.
I'll make a tracking issue for that and note in there that the intention is to build those down into the Deneb spec over the next couple of weeks. And we will bring up 6988 in plus two weeks. 

Please take a look at this. You know, this is moderate… in the intention here or what we thought was simple here. So let's have that conversation and surface this back into it. Any closing comments on 6988? Great. 

## Research, spec etc

# Big Data Experiments [23:16]( https://www.youtube.com/live/050Jq9lO838?feature=share&t=1406) 

Next up is Dankrad, which you're very welcome to share your screen If that's helpful, Donkred ran some big data experiments and has some stuff to show us.

**Dankrad**
Hello, can you hear me? 

**Danny**
Yes.

**Dankrad**
All right. It's the next screen as well.

**Danny**
Yeah, that's pretty small, but I imagine, whoa. Maybe you can zoom in. It seems like that's a great one.

**Dankrad**
This better?

**Danny**
Yeah, any additional amount of zoom would be useful, but this is beginning to be readable. I don't know what's going here.

**Andrew**
Zoom in the browser. 

**Danny**
Yeah, like command control. That's looking good.

**Dankrad**
So over the weekend, I did some tests on mainnet. Basically, I want to figure out how if we click like a watch. Yeah, those blocks and how many you put on the watch block and share this as well. So that you can all have a look at it.
It's a basic key.

**Danny**
Hey, Donkred.Are you your mic sounds not great? Are you going through your headphone?

**Dankrad**
Yes. I think I hope so. Wait.I'm going to go ahead and see if I can. Is this better? 

**Danny**
Quieter but clearer. Yes.

**Dankrad**
Great. So over the weekend, I was, I did some tests where basically I'm created large blocks on mainnet in order to see how much data we could support. I shared the dashboards that Sam created for this just in the chat so that you can all have a look at it as well. So basically, we created blocks. Well, I mean, this is not the actual size of those blocks, but that's how much basically extra data I try to integrate into each block. I started at 128 kilobytes. Went to 256 512 768 and one megabyte. So that corresponds to between one and eight blocks per block. 

In terms of amount of data we added. And what we saw was that for pretty much the whole range, the network itself was stable. Like there wasn't any crazy things happening. Although I will come to that on the second test at one megabyte. We did see some. We did see one reorged due to the late block. Reorg that sometimes have implemented. So one to start with. Here is like a dashboard that has created that shows how the bandwidth was on different clients. And yeah, you can clearly see that on those block tests. 

The bandwidth consumed went up quite a lot. And I won't go through all so like basically up to five, not 12 kilobytes and even 768 kilobytes as you'll see like everything looked very normal and stable. So this is the first 768 kilobytes tests. The red markers, they are the annotations for when the blocks were set, the big blocks. And these are block arrival times at different centuries on mainnet. And on this first test actually for most of them, it's like even well within the noise ratio when those blocks arrive like I mean you can see that.

Even under normal that were conditions, you get. The blocks arriving up to three seconds and past the past the slot time and that's also what we saw during the tests. So that looks pretty good. And most of this is just completely normal. You can see, yeah, almost a very, very small decrease in the attestation. And that's one, that's one decrease in attestation agreement here.
And the first, 

**Danny**
And that's head agreement. Correct?

**Dankrad**
Yes, I think so although like, I mean, yes, in this case it is. But that's unfortunately not what the stash code always shows like when nobody agrees to the head, then the zero apparently indicates the block before. Yeah, so that is the first seven 768 kilobytes. Second one is here on this one, I think it looks like a bit more like there was a little bit like maybe the blocks were a bit larger. I haven't looked at exactly detail but like yeah, you see a little bit more of spiking but it's still within the noise range. And. Yeah. And you'd be also see a little bit more people missing the head on some of these. Overall, I would say like 768 kilobytes looks very stable to me like this. There's nothing I would be worried about in these metrics.

So I think we can relatively safely go to up to six blocks per block. And then I also run tests at megabyte, which would correspond to eight. And then the blocks, this is the first test, which again looks fairly okay, in terms of block propagation, while sometimes spiking to 3.5 seconds here but when you look at like the other dashboards. That's even again something that you sometimes see for not even very big blocks. And then there's spikes and block propagation here. And yeah, you seem. 

**Danny**
I think you're on the 756.

**Dankrad**
No, this is one megabyte. Yes. 

**Danny**
Okay, I got it. This is the first test. And yeah, you see a little bit more people not voting for the head here on some of these blocks. And then on the second test, we saw for the first time something's going wrong. So like can actually stay here. So very nicely like one of the blocks actually arrived more than four seconds into the slot time. And so it was what actually happened is that it was often. That's like we checked the next proposal was present so I assume that what happened was that they decided it didn't have enough attestations and intentionally built on the previous block.

**Danny**
And it was something like they had 8% correct head rate. 

**Dankrad**
I do not know that number. 

**Danny**
I thought it was in the chat under discussion. I’d have to look at it. 

**Dankrad**
Okay. I don't remember that. Okay, maybe. Yeah, it looks like that that's this is what happened. I would say the network was still stable but this, but we just didn't manage to get it before that deadline but like nothing crazy happened.

**Danny**
Yeah, pop said 92% attested to the parent of that block and 8% attested to that. It shows you, you know, something about the kind of delivery boundary.

**Dankrad**
Yeah. Yeah. Actually, if someone is able to get I haven't got this is this is the slot for that. This is the often block if someone is able to get the block for the slot and could tell me how big it actually was because unfortunately, I don't have that number. I suspect that we meant we created a block that like some of the later blocks were actually much bigger than we even up to 1.7 megabytes and those made it in. So I suspect that this block as well might have been larger than we were intending because yeah we can't perfectly control topic.
The blocks are going to be that way. 

**Danny**
So given, given the note stock, especially the first one, is that enough. Does that give other people that want to dig into the data enough enough note about which slots these tests are happening on.

**Dankrad**
Oh, yes. Yeah. Yeah. In this, the second node stock, in this talk here, and it has all the block and slot ranges. So I guess some of the potential orphan blocks become harder to do historical analysis on but, you know, if somebody 

**Dankrad**
was only a single block that was, that was often there was another actually in the second range that's another missing block. But that validator was just offline. And so that that wasn't us. It was already offline before that.

**Danny**
So I do think it would be valuable for if somebody wants to, or multiple people want to do more data analysis on this rather than just looking at these dashboards like better understand kind of the variance better understand.
I guess some of this is going to be hard to do. If you don't have century nodes that we're already looking at this, I guess, primarily we just have chain data.
Done loss. 

**Dankrad**
Yeah, so my, I would say basically based on this that since this is actually quite pessimistic like we are actually creating those huge blocks, but we decided a while ago that we're going to separate block and block propagation.
And also, we should consider that we were actually going through the mem pool with 64 kilobyte transactions so that additional load that's not going to exist with the blobs which I have used the more like the less spent with intense mem pool where like people do a lot of work all rather than push. So given that I think like, going to like an element of six blocks and a target of three blocks, blobs would actually still be safe. 

Yeah, so that would be my recommendation based on these. Maybe that I will maybe want to think or like recommend, we start thinking about is whether they are four seconds deadline for blocks is still appropriate. So what we have done is that we have now we're adding more and more things that need to happen in this first third of the slot, like we had this four second deadline originally already when we launched the chain. And back then the only thing that needed to happen is the beacon block itself. And we also didn't have a four second deadline because we didn't reall played blocks. And since then we have added the execution block which now needs to be propagated and verified. We're going to add the blobs. And we are also like, we have now added this kind of block slot. Poor man's blocks twice kind of through through like this we are.

And it may be a good idea to think if we want to move the deadlines around a bit in the slot at least it would be interesting to see what we know about when like attestation's happened when attestations happen. And maybe it makes more sense to prolong this first phase where we wait for the block and have a little bit less time for the second and third phase. And that would give us a lot more. 

Yeah, we will first it would make the chain probably more stable and second it would also give us make it much easier to like increase the number of blobs a little bit at least. 

**arnetheduck**
This is really nice. Two points. If we're moving back times which I'm generally positive about. What happens today is that there's like a big bandwidth spike around the time when attestation's are published. And then the aggregation publishing is actually not that bad anymore because we removed duplicates much better. And then that will be interesting to see like, look at when the bandwidth spikes happen and also in clients implement this rule that we're allowed to test as soon as we've seen the block. This kind of evens out the bandwidth profile of the stations. But I think not all clients implement it in fact, maybe only nimbus. 

**Danny**
Sorry, what was that what was the second thing you said and maybe nimbus only?

**arnetheduck**
So the rule for when you're supposed to publish the attestation is currently when you've seen the block or when 4 seconds happened…

**Danny**
Which kind of causes potential weird race conditions. 

**arnetheduck**
So the big burst at the fourth second mark if you don't implement the first rule because everybody then at the four second mark sends an attestation like literally the whole, well, a 32 second of the validators at which quite a lot of validators today. And they all just spam the network at the exact same moment so so that's bad. So if if clients were to implement, send that the station when you see the block, or a little bit after that would even out that flow.

The second good news is that thanks to the split we've also opened the PR on the lipid pieceback, which introduces a new message. It's called, I don't want, instead of I want, and it's basically. Oh, great. And you go, thank you. Take also does this. Even sending the I don't want it basically says that I don't want my neighbors to send me a particular piece of data because I already have it. So this is really good for big blocks and big blobs. So if anybody's interested in that kind of network optimizations check out the lipid to be spec repo where there is a PR app about this which I forgot the number of but I'll post it later and consensus dev R and D channel.


**Danny**
Yeah, I'm definitely eager to see some of those types of optimizations make it through. I think they certainly complement the type of data analysis we're currently doing. Was there not a race condition problem with the releasing the attestation right when you got the block, is that why there's some sort of like short time delay us out after?

**arnetheduck**
There is, if you send the attestation to a client that hasn't yet processed the block. It might ignore that attestation unless it has a queue, which queues unknown attestations for the current slot. Yeah, that race is solvable. Let's put it this way. 

**Danny**
I guess so, so Docker does have a concrete recommendation, which is to change this from two four to three six. Is that in the cards, is that is this data convincing, is there more analysis or additional longer experiments that should be done? So, just temperature gauge on that, we have some time to tune this value. If we are, if there is an intention between the value, we need to begin to have that conversation now. It is nice. I think one of my goals in this experiment was to see that two four was safe. And I believe that we have that data now which is good. There's also then the question of, and what else. 

Dankrad, for the data that's behind those dashboards which came from the sent freeze that the dev up seems running, is there a raw  version of that or an API version of that that people could do more analysis other than just look at the dashboards or are we pretty much sure we have the dashboards and that's what we got. I don't know.

**Dankrad**
I don’t know, I'm sure they can provide that. I can, I can ask them.

**Danny**
This is awesome. I really appreciate you taking the time. 

**Dankrad**
I would like to also because I see a lot of like messages in the chat being like, oh, we should like start slowly and not like I have a lot of people asking me when blobs are finally coming and they are like several teams which are building products at the moment, really needing us like I, I think people underestimate how much this is going to be used and how big this is going to be. 

**arnetheduck**
We need that argument. It starts slow. 

**Dankrad**
Why

**aretheduck**
For this simple reason that the data that like this experiment, it shows behavior under unsustainable load right?

**Dankrad**
Its sustained. It's 10, 10 blocks in a row.

**arnetheduck**
Okay. Okay. I don't know. 

**Dankrad**
Actually a lot better than I thought. 

**Danny**
…really consider trying to do a longer one, although it just becomes very expensive. If there's value in attempting to do more repeated experiments or longer experiments we can attempt to do so. Okay. I do believe there's also kind of a side conversation going on, on the ever pending honest block reorgs specification. And if there should be additional changes about the percentage of attestation scene and potentially stronger circuit breaking and then there's some kind of a mechanism so that you know in the event that every block is taking more than four seconds for whatever reason. You don't you get more than 50% of the blocks. 

No, I believe on Prism there, there's some sort of justification circuit breaker that was set in the chat. Does that mean like if there's not sufficient blocks to justify they would actually circuit break and stop doing the reorgs. 

**Terence**
So there's a circuit breaker. So there's, so there's actually a bunch of circuit breaker that's defining this back right so we look at whether the parent block is missed and we don't reorg like the first slot of the e-pog and we also look at the participation as well. So yeah.

**Danny**
Gotcha. Okay. Well, let's let's continue that conversation. And yes, a longer test would cost multiple hundreds of thousands of dollars.

**Dankrad**
So, I mean, I, well, I mean, that's what I said, we saw that much. We could do a longer test. I wonder what what would we get out of this like what's like what. What would happen. I mean 10 slots already a lot realistically, most things that could happen to just a standalone should happen after three slots already right, like what would you will learn from at 20 30 or 40 slot tests.
Someone can.

**Danny**
Yeah, I guess. A full epoch. A full epoch and then through a epoch transition might like that's the only kind of like milestone thing that's happening is like does sustained. 

**Dankrad**
I mean, okay.

**Danny**
So, I guess the full epoch into that epoch transition do something. 

**Dankrad**
Okay, but like the, the load doesn't make the epoch transition more difficult. I can see having it in an epoch transition would be interesting, but I still don't see why the full epoch would change anything. 

**Danny**
Yeah, I guess my intuition is that it likely would not, but then there might be like small things that compound, like for example, if you know you're having trouble processing everything due to delays and your cues are getting more full, random stuff like that. But I agree that the actual network component side of it should be. You know, if you're in more than three slots of sustain load you're probably seeing a lot of what you're expecting. 

**Dankrad**
And we can check we might have already hit me upon epoch, I’ll get pretty back to you.

**Danny**
Right. So, do we have any other questions for don't grow the data as it currently stands. We can see to the extent the data can be opened up for a more, more analysis. So let's continue the conversation in the census chat or all core devs. Thank you very much Dankrad. Okay, anything else on Deneb for today? Great. Thank you.

## [Engine API versioning [RFC] Engine API: do not bump method's version upon datatype change execution-apis#376 (comment)]( https://github.com/ethereum/execution-apis/issues/376#issuecomment-1547720683)  [48:09]( https://www.youtube.com/live/050Jq9lO838?feature=share&t=2889) 

There is an engine API versioning RFC from the go. 

**Mikhail**
Thanks. So there is an intention to start from Cancun. So from then to allow for every engineAPI, method only one version of a structure that it can accept. Because having like multiple structures accepted by the same methods brings an ever growing checks and complexity to the outside. 

And we were discussing this in more details during for it 4844 call this week, but the question is basically some of the CL clients already used relies on the feature that the most recent methods, the most recent version of which methods and engine API supports all the previous data structure so they can use the same method for sending a, for instance, for sending a payload for Paris, for Shanghai and for Cancun. 

And the other question is how hard it would be to break this reliance and to get back to one to one relation on the CL side between the matter version and data structure version. So that's basically the main question for that discussion. 

**mark**
I think the main reason that we had the decoupled was so that we could do couple, so we could deprecate old methods, as well as update to newer methods outside of forks. I can, I can see how we could still deprecate old methods if we linked up the versions but decoupling them from forks could be difficult if we enforced a one to one mapping. 

**Mikhail**
So you mean that if any change happens between the fork, it will be difficult to switch to a new map version, right?

**Mark**
Yeah

**Mikhail**
Yeah, the same for supports has two methods versions like one is, v3, for instance, the other one is v4, and when v4 is available, so the difficulty switch to v4. Is that what you mean?

**Mark**
Yeah. 

**Mikhail**
Okay, I see.

**?**
You're talking about when the same method has the same actual data. So you cannot switch based on the data that you're passing but, but just using the latest available method, whatever version is it, it is, and no matter to that you're passing. So if it is data driven, you cannot switch to easily to the next version of it if this is the same. That's the problem?

**Mark**
Well, like, we'll take the adding in of the value of the payload as an example that was a change we wanted. So if we wanted something like that to change it we would, I guess presumably have a new method. But yeah, the proposal is to have a one to one mapping like execution payload V2 to new, new payload V2 to execution payload v3 new payload v3, that's the proposal.

Whereas right now, we can have any of the, any of the underlying data types go with the versions basically the versions have supported all previous data types.

**Mikhail**
Yeah, and so in order to make this kind of switch, you will have to request the available capabilities and then see that some new capabilities available and start using it with the old data structure. I mean, like with the data structure of a previous version. And this basically what you would probably do anyway, because if we new capabilities added between the four, which means that something new has been some new data has been surfaced to CL or some new data are requested from CL. So you don't have to anyway handle this somehow.
I mean it's not just you know you're switching to v4 and sending the same basically the same data. But that's actually how I see.

**Mark**
Yeah, like presumably you could create a version, but like a new method for the interim before the next fork. That, I mean then we would actually, we would have to add a new method. Like if we have new behavior, we can't just use it right away with the method that we will use in the next fork, we would have to have a method for the interim.

**Mikhail**
Yep. And probably will. Yeah. I mean like it, it, this does not. I mean like having a method handling all previous data structure types, data types, doesn't seem to help much here. That's, that's just my intuition. 

**Mark**
What if we, what if we like, didn't make this kind of a hard rule, but like so that we could in the case where we still where we want to do something between forks we could support two different types, but in cases where we only need to do it at the fork, then we can keep this one to one mapping, just kind of a hybrid I don't know if that makes it too complex but 

**Mikhail**
I would say that we have a precedent that we really eager to introduce something. You know something in between the forks. And that would be the case that we will really need these two versions supported in it. I'd say that let's discuss it by that time, but by default use one to one. I mean like not make any commitments for the future, but if it will be reasonable to do this way. Why not. And the question for lighthouse. Do you think it will be really difficult to get to get back to this one to one thing. 

**mark**
No.

**Mikhail**
Ok, cool.

**Mark**
Yeah, it's just mostly not losing the ability to deprecate old methods and not losing the ability to upgrade independent of forks, which is the point of exchange capabilities. 

**Mikhail**
And yeah, the bad implication of fault methods I was thinking about it so we can currently deprecate we want or we to and say that with three handles all of those data ties but basically, which is deprecating methods, but these methods, a lost method version has all the complexity that those methods has so in one to one, there will be just, you know, this complexity…And layer across different methods while with this approach that we currently have is just in one method so I see, I don't see big advantage of, you know, of having those deprecated while you have all these stuff checked anyway.

And deprecating the data structures is really a difficult thing, because we want to allow for lock steps in, since Bellatrix are so that that would be another question. Does any other CL clients and tech went to Light House relies on this feature. So CL can pass whatever data structure to new payload, for instance, to the most recent version of it? So, yeah, so I think that I can make a PR, if we are agreed on that so I can make a PR to make the global extension for sophistication, just with one version. 

**Mark**
With this comes the additional complication here comes in how we actually switch over, because we're changing the behavior unless we enforce it at ? fork or something. 

**Mikhail**
Yeah, I mean, like this should be, this should be agreed that since, I don't first I guess that the new this one to one should be implemented and CL that is not the added supported. And then we can plan it for some dev net, or for it for for dev net.
So, you have all those methods, all those previous methods and you can just, you know, start using this logic that we send we want to be one and with two to two and so forth.

And then, yeah, EL can just, you know, drop all these things from the three.
And then the first proposal is just start to do it since it's since with three, but we too will remain a change. 

**Danny**
Yes, I see how clients can switch over to this new version and then once we're confident that obviously also done that them. And then CL can migrate. Anything else on this one.

Okay, so you do have that open RFC if anyone else has comments or.

**Mikhail**
Yeah, yeah sure. So, and I'm going to open a PR. Can discuss it more if any concerns will arise.

**Danny**
Thank you, Mikhail. Okay, anything, anything else under discussion today.
Great. I will put together, we're going to have a release. We're going to have a release next day with these minor changes the types in the additional field. We'll put together an issue that's tracking the handful of EIPs that we're going to build into Deneb over the couple of weeks. And we will talk about 6988 in two weeks. Please take a look. This is, you know, the, the change to the proposal with respect to slashing. Okay. Thanks everyone. Take care. Talk to us. Thanks. Thanks. Thank you. Bye bye.

## Attendees

* Danny
* Tim Bieko
* Gajinder
* Mikhail Kalinin
* Ahmad Bitar
* Paritosh
* Phil Ngo
* Spencer
* Fabio de Fabio
* Dan (danceratops)
* Preston Van Loon
* Marius Van Der Wijden
* Roberto B
* Carlbeek
* Andrew Ashikhmin
* Lightclient
* Fredrik
* Zahary
* David
* Pooja Ranjan
* Ben Huntington
* James He
* Anna Thieser
* Mark (ethdreamer)
* Mario Vega
* Stokes
* Sean
* Terence
* Etan(Nimbus)
* Dankrad Feist
* Saulius Grigaitis
* Marekm
* Arnetheduck
* Hsiao Wei Wang
* David
* Ansgar Dietrichs
* Marek
* Recordbot(D)
* Stefan Bratanov
* 0xTylerHolmes
* Matt Nelson
* Anna Thieser




