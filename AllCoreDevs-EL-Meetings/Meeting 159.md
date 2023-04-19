# Execution Layer Meeting #159
### Meeting Date/Time: April 13, 2023, 14:00-15:30 UTC
### Meeting Duration: 01:04:11
### [GitHub Agenda](https://github.com/ethereum/pm/issues/754)
### [Video of the meeting](https://www.youtube.com/watch?v=u8Nm8AGyCQM)
### Moderator: Tim Bieko
### Notes: Metago

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 159.1 |


## Shanghai Recaps

**Tim**
Okay. We are live, ACDE 159, I posted the agenda in the chat. Obviously, the chat about this Shanghai, Shapella, then some Cancun topics, and then a payload ID conversation that's already happened quite a lot in the agenda itself. Yeah, and anything else that comes up, but I guess to start. Yeah, great work, everyone. 

On Shapella, it worked. The network transitioned successfully. There were a couple issues, like minor issues that we saw. We can talk about them, but overall, yeah, this was very smooth. Yeah, great work, great work, everyone. Does anyone want to give a recap? Danny, I see you have three comments in the row in the chat. So, share your perspective. 

**Danny**
Those were troll comments. Yeah, I mean, it went really well. I think one of the most interesting things that I observed is a number of validators were attesting, but not proposing. And that's always kind of an interesting thing because it means their nodes are up and they're following the chain and they're kind of voting on things, but then this other component, the block proposal is forked. Sometimes that can be an issue with your local EL, but given that we have the map boost dependency, that's kind of also one of the potential targets there. And the person guys can talk a bit more about that, but it was a, a map boost issue. One that I think we would hope to see covered in…I think we might have seen a list of the options in the chat as well as in high tests, so we're kind of circling back to figure out. 

That additionally Lighthouse had some CPU. High CPU usage and that was resolved with a hot fix. I believe not yet on their stable branch. Other than that. I believe and maybe somebody can tell me if this is exactly what happened. We had a higher number of missed slots right at the fork. We saw something like 40,000 BLS change operations broadcast because there's more broadcast prior to the fork boundary and saw high CPU loads. 

So the expect my current interpretation of the highest missed slot boundary right there is the just essentially the gossip with honest messages, dousing some of the nodes around that boundary. So those are the main points I saw while I was paying attention last night. Anyone else?

**Terence**
I can add some color to the Prism issue. So this is so this was a Prism block that we missed to include the BOS to exact changes when we submit the blind block to the relayer meaning that the relayer will fail the signature verification because of this issue and so this issue happened because of we made the unit test case unfortunately. Also we did not have we probably did tested this in the production by production I mean test net, but given that there was so few validator and we're all data that's running with builder. I think probably one to two percent. We completely missed that. So we're working on postmortem right now. So that is to be shared by the end of the week. 

And what went well is that the circuit breaker actually ended up saving us because of Prism configured to be met missing five slots per epoch. So if we see more than five slots per epoch that's missed, we were defaultable. But we didn't. That ended up saving us that believe it wasn't for that will probably see a lot more missed block over epoch. And yeah, thank you for Chris and other really and for coming together and helping last minute. So they ended up banning Prism validators by use by forcing them to use local builders. If it wasn't for that, we'll probably also see more missed block along the way. So yeah, we're working on postmortem and then we will release that for later. 

**Tim**
And just one question I just make sure I understand. So when you say they're working on the banned Prism validators are you saying the flash spots relay basically refused to accept…like Prism validators connected to it? Is that right? 
**Terence**
Right, right, right. So they so they're able to see through the user agent stream like who is requesting the header to sign and then you can see there was a Prism validator, the relayer will reject that validator’s request. And I believe all the relayers ended up doing this except for one of the relayer. 

**Tim**
And Chris, as you have your hands up, a little bit more color on this?

**Chris**
 Yeah, a little bit more color. We have been watching the fork live with the ultrasound guys and with people from Prism and from Lighthouse. And we started investigating the issues together, collecting the data, and once it became clear that it's a signature error by Prism. We could implement a very simple check on the user agent that they really does not return any bits for that user agent anymore. And luckily we were able to identify Prism specifically by the user agent because they do send a particular user agent already. And we rolled out this patch analysis to the other relays that were basically on standby as well. Also shot out here to Mike from Ultrasound. 

We have been in this together and basically all the relays rolled out this patch on around 1 AM UTC and we sent the patch here, by the way, it's a very simple patch. Notably, we couldn't get hold of any of the Agnostic Gnosis relay people like it was impossible to try to get a ton of ways including calling them like they only disabled these at 7 am UTC. So there were additional missed slots afterwards by the proposal connected to the Gnosis here. 

In total I have some numbers. The flashbots really saw this invalid signature 43 times so that would be 43 missed slots through the flashbots relay, through the Gnosis relay 57 times the signature missed slots and the Ultrasound relay counted this 21 times. So this is all to get a 12133 big relays and all the other relays they applied the patch, immediately saw the overall like a two hour window roughly 2 and a half hour window where the Prism requests proposal would fail the missed the slot. 

**Tim**
Got it. Thanks for sharing. I don't know who would be the right person to write the post mortem on that side. Is that going to be part of the Prism one or like any people supposed to just I think it's going to be interesting to capture this information some more permanent than like the call?

**Terence**
Yeah, we are working on post mortem right now. I think that should cover everything. It's also what mentioning we issue a release yesterday that's 4.0.2. So if you want to run that node with your validator, then you should be running the release. 

**Tim**
Got it. 

**Chris**
Also, they're to run this out like either we can contribute our data and time stamps to the Prism post mortem or we do another post mortem and drop this somewhere else. I have both seems good. Just finally any proposal that uses the new Prism release. This will use a new user agent and this will automatically work again with the builder network. 

**Tim**
Awesome. Thanks. Yeah, we can chat online about where to add the info, but yeah, they should end up somewhere. Anyone else have just thoughts or comments about the Prism / MEV boost situation specifically?

**Mario**
Yeah, I can add for the hive test here. So basically the problem with hive was that it's using the ? layer. So this ? layer’s the only purpose is just to generate invalid payloads and check that they are well caught by the consensus client. But the problem was that for the happy pad, it was not very fine the signatures. So that's why it was missed. I think this company is a fixed in an upcoming new test for hive and we can catch this issue in future. 

**Tim**
Thanks. Thanks. 

**Pari**
Just a little more color. We also probably should have caught it on a shadow fork or one of the other test nets, but at least with the last shadow fork because we have the official builders and relays on them. But we were facing a different issue with signature verification and by the time that issue was patched the queue was empty. So we wouldn't have triggered this issue anymore. So I guess in the future we also have to try a few more scenarios with the release on that. 

**Tim**
Right. Then it's like if we can have it relays an earlier earlier shadow forks, then maybe we have more shadow fork there and we end up hitting this bug on one of them. 

**Pari**
Yeah, exactly. 

**Chris**
But not here like we did have the shadow forks and this particular circumstance was just not occurring. 

**Tim**
Right. 

**Chris**
I think on the main edge of the fork. So maybe there is additional steps or protocols we can add to increase like the test coverage on shadow forks to catch these types of edge cases. 

**Tim**
Yeah, and I think they're probably custom to each upgrade like the withdrawal or like the BLS change queue will probably never be as big as it was on the first block of this fork. But then thinking about what will be unique and like kind of stressing the network when we have the next fork and trying to like run through that specific scenario over and over is really important. Yeah. 

**Danny**
Real quick, so as you said in the chat that you think that the high missed proposals even on that fork boundary was just the Prism issue and not the dust. Do you have evidence of that? 

**Potuz**
Oh, no, but it's just a matter of statistics, right? So I think most of the network about like 80% are sending their block MEV boost and apparently according to Blockprint, 40% of those are Prism. And every Prism node would be failing at the fork if they sent to MEV boost. So and that more or less matches with the number of missed blocks per epochs that we had after the after the fork. So I think it's safe to say that most of the missed blocks were due to this bug. 

**Potuz**
But I think one lesson that we all should be learning is that at least I myself when I'm coding I often time think on the happy path, the happy path, which is a local execution. And we only have sort of like end to end tests where we test with a builder and we deploy to testnets or to. Or for the reproduction with the builder, but I think we should set up a way in that all of our coding is oriented towards testing the builder because most of our blocks are going through the builder. This is a ridiculous bug that should not have happened at all. Like there's many places where they should have been tested and all of them failed at the same time. This is just impressive. On Goerli, for example, we had we went back and checked the day of the fork and we only have like three missed proposals out of all of those that were due to this bug and just they were just lost in random noise. Which this is something that I should have tested and we should have tested in a unit test and we failed to do it. I guess it's because we're set up to think in not on the builder thinking on the happy local execution path. 

**Terence**
Also we don't run enough validators to MEV boost for our testnet. We only run like 10% so which means that there's about 1% of the total share of the network. So it was hard to catch this. 

**Potuz**
Yeah. We should definitely have a network testnet, which is more or less stable so that we can actually test our production in which at least most blocks go through the builder. So that we see these kind of things. We could not have seen this on Goerli where we only had like 1% of the network, instead of the 40% and everyone sending them to us in mainnet. 

**Tim**
Thanks. Any other comments or thoughts on the Prism bug specifically? Okay, I saw I believe Lighthouse also put out a new release. I don't know if you want to quickly walk through just anyone from Lighthouse actually who can walk through what happened there? If not…

Oh, okay. So this was also on Prisms on Prism. 

**Potuz**
Okay. It's a chicken and egg problem. So Lighthouse has some CPU issues in the way they process exits. And they failed to cache correctly the exits and process them correctly when there were missed slots. So they had this bug, but it wouldn't have been apparent if we didn't have the missing blocks that were because of Prism issues. 

**Tim**
Got it. Any other clients then have issues or interesting things they saw during the fork they want to share? 

**Ben**
Yes, just a quick one on Teku if I may. We are seeing occasional spells of slow block import for Teku specifically. So normally it takes about 100 milliseconds and most of the time it's still taking 100 milliseconds and it's fine. But for several minutes at a time this seems to shoot up by factor of 10 or so to over a second, which can sometimes delay block processing in total. So if it's a if it's a late received block beyond 4 seconds, making at a stations inaccurate. 

We are investigating haven't found the root cause yet. And it seems to be getting a lot better over time. It was seemed worse in the few hours post the upgrade. One hypothesis is it might be due to patches where there are long withdrawal sweeps, you know, where most validators have 0x00 credentials. So we haven't held it down for sure yet, but for anyone running Teku just be aware of that and we are investigating. 

**Tim**
Awesome, thank you. Any other clients? Anything to share? Okay. I guess anything else on Shapella that last chance to bring it up as we move on? Okay, well, once again, great work everyone like I think, you know, overall this went pretty well and the network is stable and which roles are happening. Yeah, very cool to see this finally live.

And I guess on to the next thing. Cancun. Yeah, Alex, you had posted an update to EIP 4788. Do you want to chat about basically the changes you've made? And then you also mentioned you wanted to have this considered for CFI. So maybe we can chat about that and just see if I find stuff in general afterwards. 

**Alex**
Yeah, that works for me. So this EIP was written a little while ago, actually for withdrawals. And we went down a different path that didn't really need it and that being said, I've gone back and looked at this again. I made a number of updates. I'll just run through them kind of at a high level. The biggest thing is moving while even just taking a step back. 

So 4788, the idea is to get some sort of a computer graphics accumulator from the consensus layer into execution layer. So, for example, this could be like the state route and that's how the EIP was originally written. So committing to the state of the beacon chain. And then the reason this is cool is because then you know, there's some EVM upcode or something. And you can access to this route and then you can make proofs or you can verify proofs. I guess this route. 

So that's the general idea is to have some way to access the consensus state in a trust randomized fashion. And the way this EIP originally worked was using the state route for the beacon chain. I changed it to use each beacon block route instead of the state route. The reason why is because the way the beacon chain works is every state has a unique state route. But not well, there can be the same block route if there's a missed slot. 

Let me refer to that. So basically if there is a missed slot and that's why the concern here, if there is a missed slot, then the block routes don't change because that's why it's missed slot. There's no block. But the state does change. And so what it means is if there was a room with slots, then there would essentially with state routes be this like linear amount of work, whereas now it's like constant time or constant amount of work. 

So we moved to block routes. The original EIP keyed in by block number like EL block number. And I've now changed that to key it by slot. And I think there's a comment from the original EIP PR. Vitalik went into reasons of why we want to use slots, which I think I agree with at this point. So, you know, insures better UX. We keep by slot. We also, so I changed this to use a ring buffer rather than just like writing them all to state forever. 

Just so there's a constant amount of storage that we use. This also measures the construction on the CL. So that's pretty cool. Just have the uniformity there. And the way it’s written now is that this block route is sent over kind of just like withdrawals are today. And you would essentially just append it to the block header. So what that means is that it's up to the EL to communicate which slots things are for if we keep the slot. And yeah, does anyone have any questions at like a high level right now?

**Danny**
I do. Okay. I just had one clarifying comment, which is I think one of the important things to consider here. So by moving not by moving to the block route, we don't have the linear potential load on the header. If there's missed slot, but there still is a minor linear component, which you do an S store permissedioned slot. So that's just when reading the EIP and thinking about security implications that there is a linear piece right there. Everything else is constant. 

**Tim**
Because I think this is like related to my question in the chat and the reason for this is because during a missed slot, you're still going to store a block route. You're just going to store it the previous one like the latest one you have, right? 

**Danny**
Correct. Correct. So you essentially play catch up for the missed slots. And there is an alternative scheme here. You could actually move the complexity to read. For example, if you tried to read slot in and maybe it was a flag value like zero, you could walk back to n minus one, n minus two, etc. And like have a higher complexity on read and unless you hit a non zero value, like return that and have a higher potential gas cost there. Given like the overhead of the block processing and the right here and the potential of missed slots and that can say it's, I think, much preferable to put the complexity in the write, but that's an option. 

**Alex**
Right. So, yeah. Well, yeah, I guess so the thing is there's one issue I see. Yeah, maybe just quickly if anyone has any other questions so far. 

Okay, so I'll take that as a no and then as written. So yeah, everything to any side is correct. That's an important distinction. And also right. So the one thing is that as written, this is assuming that the EL can essentially use the timestamps from the headers to drive slots, which I don't think they have a functionality now. I don't think it's being added say from 4844 or like anything else that might go into Cancun. So yeah, that's a question for everyone here. Do we, you know, are we comfortable out in this logic or would we rather not sort of leak that abstraction barrier between EL and CL. 

**Danny**
And what is the alternative to read by?

**Alex**
Well…you could just you could just send this slot over? 

**Alex**
So, you know, you're already trusting the CL for the roots, you basically also just look for the slots, so there just means there's more in the header. And you could imagine like having the start slot to end slot, you could like write the start slot to the state, so that you only need the one slot number. You can send them both. There's a couple different options. 

**Danny**
Or we could like try to have this by time stamp and have bad time stamps be failure cases on read and like other word stuff, but that would bring a lot of moderate amount of complexity into the construction. At a degraded UI. 

**Alex**
Right. So for the EL to compute these slot numbers, which is also something. Absolutely probably one at some point. You need two pieces of configuration from the CL. So it's not too much, but you know, it is something. And if I think the bigger thing is that it violates again the subtraction we have or like the barrier between each layer. 

**Mikhail**
Mikhail, your hands up. 

**Mikhail**
Yeah, I just wanted to add that we still have a non spilled EL or header unused, which sounds like a good place for a slot. So it doesn't add any data complexity and potentially we can expose slot on the EVM level in some in some future. You could think that it will be useful. So and avoiding the company derives and slots from time stamp on the outside. It's a good thing in my opinion because if we at some point in time change it. I mean like this slot duration. So we'll have to. We'll have to become a configurable effort very so more more configs more time between the two layers. If it can be avoided that would be. 

**Tim**
And are there…sorry…Alex? Are you going to say something?

**Alex**
So I'm going to call it EL devs because I see many of them here and I feel like don't have some opinion. What were you gonna say Tim?

**Tim**
I was going to say is there so if I understand Mikhail correctly it's like you remove the need for this precompile that you're writing to. You instead have this slot number as part of the block number for free as you know the non value. 

**Alex**
So right. Yeah so yeah so well there's kind of two things so one of them was just exposing the slot to the EVM as well. And that's like a separate downstream question. But then upstream is like yeah how do you even get this data to the EL in the first place. And one option is rather than try to look at the timestamps and the headers and compute the slot. You would just pass along with this blocker as well in the question that is where does it go. There's apparently this knots which I believe is bit 64 storage size is just sitting there and not used basically. So we could put it there.

**Tim**
And yeah and I assume there's no non upload right? Like I don't think this is previously exposed.

**Alex**
Don't think so yeah. 

**Tim**
I assume it would have dealt with it during the merge if that's the case. 

**Alex**
Hopefully. 

**Tim**
Yeah, Chris and any EL devs have opinions thoughts questions on this?

**Danny**
Then we can give some room to talk about it in one week on ACDC. We can see from a controller slightly but if the else come there we can also hammer it from that angles. If you have some time to look at it. 

**Tim**
Yeah, Potuz?

**Potuz**
Yeah so I'm a bit confused about this difference. So are we talking about like exposing this slot number on the EVM? On every block instead of just making the computation from Genesis time blasts this number of. And this time stamp? Just because we might change the slot ration. It seems to me that the complexity of changing the slot ration is going to be just adding a constant after a particular fork. And which shouldn't happen in many forks that we're going to change that slot time to sort of like adding data on the EVM on every single block to prevent this extra computation seems crazy to me. 

**Mikhail**
I'm not sure what you mean by the EVM. It's just you know pass the slot into EL header and we have a place there which is remains unused since the merge. So there is a field of you instinct for data type which is that filled with zeros currently. 

**Potuz**
I understand that, but and so we can use something useful to send instead of the data that is completely equivalent to the timestamp that we have already sent it in that header. 

**Mikhail**
Oh yeah, yeah, so yeah, that's very fair, but we will have to keep to have this complexity of maintaining a slot ration on the outside. Yeah, I get it. 

**Danny**
I have a quick question. So often when I think about the station distribution function, usually I wanted to be a function of the pre state, the block and then outputs the post state. And I just realized that I believe this actually makes this a function of not only the pre state, the current block, but also the previous block because it's doing a read from that rather than reading the time stamp from the previous block from state. Is that a concern? That's usually kind of a little bit of a red flag to me when we're abusing and extending the inputs of the station distribution station? 

**Lightclient**
Its is just a function. I mean, we also already need the last 256 blocks for the block hash off code. 

**Danny**
Right. But that's maybe something we don't want. And would want to fix. So I wouldn't want to like add another dependency of previous block. 

**Alex**
Yeah, the reason that this EIP uses the state and the way that it does Lightclient is for that reason, like it was designed in the past and away from having the states.Yeah. The pre state block post state, but also there's almost as like hidden input of this history of element. 

**Danny**
Yeah, but there's another hidden input right here, which is the previous block header. 

**Alex**
All right, so that can be changed to write. 

**Lightclient**
I mean, yeah, we need the previous block header for the 1559 verification, right. 

**Danny**
You tell me. 

**Lightclient**
Yes, we do. 

**Danny**
Yeah, okay. So the EL distribution station is pre block header, pre state block currently and likely won't change. And that's fine. I just don't want to extend the dependency. 

**Lightclient**
Yeah, I agree. Yeah, without consideration of 256 is we I think everyone thinks that's the general. 

**Danny**
Okay, thanks. 

**Tim**
So yeah, there's some comments in the chat about exposing it to the EVM as well. So I think there's like two separate things, right. One is like, where do we store this data? What are the states? The ones something like that. But then obviously how do we expose it in the EVM? Alex, you may want to take a minute or two to talk about like why we should expose this in the EVM and what's like the value that you get out of this?

**Alex**
Well, we're talking about the slot numbers themselves or this route? 

**Tim**
Either. 

**Alex**
Well, I assume. Well, one thing is not that like…

**Tim**
Yeah, the route is like the right spot. 

**Alex**
Yeah, sure. I mean, it's so right. I mean, there's all sorts of things around bridges and lightclients and staking pools and you know all sorts of things. I mean, like immediate use cases would definitely be around like more trustless, making pool designs where like right now, a lot of them just like have some Oracle that you know, there's like a multi stake updating or something like this. And then instead you could move that to again, just like proving some bit of the state to anyone can do this and it reduces a lot of governance risk for all these staking pools, by the rocket pool…

**Danny**
And you know, more importantly also reduces the barrier to entry to create something because getting a good Oracle hard.

**Alex**
Yeah, that's a good point. 

**Lightclient**
So was that the argument for putting in the state or that this is the argument for the op code in the first place. 

**Alex** 
Well, right. So we're just talking about. And the so well, there's a number of decisions here because it could also not be an op code, but basically this is just the idea of having the route to be exposed in the EVM. So like that's what the EIP sets out to do. That's the important bit. I don't think we should get tied up and like, is the slot exposed like what does that look like, all of that stuff. 

**Tim*
And sorry, just to make sure I understand why, like what's the value that you get from having this slot number if it's not exposed in the EVM itself?

**Alex**
Well, so it would be written in this contract and anyone could read it. So in that sense, it's exposed. 

**Tim**
So it would be it's in the state. Okay. Yeah. So so so just I guess so Mikael's idea. So like Mikael's idea of putting it in the nons. If we do that, then it's not within a contract. And so no, it would be like so. 

**Alex**
No, no, no, that's so that's just essentially like commit to it. Well, let's see. I mean, maybe we could think about something weird, but it'll end up written to the state according to the current EIP. 

**Tim**
Okay. Correct. Yeah. So it's like, is then later as a user I go and say, hey, what was the area that's locked? And I give it the slot number. 

**Tim**
Yeah. Yeah. Yeah. Okay. And then I can imagine also potentially if we if we are writing to the state as well. And we also write the block header that like off chain applications that like rely on block headers can get that information without having to read the state. 

Right. And yeah, let's assume the extra benefit that you get from having it there. 

**Alex**
Having the roots or or sub slot? 

**Tim**
No, having this slot number. Sorry, having this slot number in the block header instead of the nons. 

**Alex**
Well, it needs. Well, okay, those are the same thing to me. That's just a question of if it's appended or if it's a replaces the nons. 

**Tim**
I'm not sure I understand. So you're saying that sorry, the root is the same thing as the slot number because you can. 

**Alex**
No, so you need to send a number of the root and the slot number. And so the reason you want to put it in the header. Okay. So you want the root in there. The reason you have to put them in the header because I was trying to think if there's some way you could like not have this slot in there because if that's breaking constructions and all this, but either way if I'm off like syncing a fork for some reason, then I need it in there because the CL won't be able to tell me. So whatever it needs to go into the state will end up in the header. And we're right now is having the root and then one slot number. 

**Tim**
Okay, thanks, that makes sense. Thanks guys. Angskar you briefly had your hand up. I don't know if there's something you want to add. 

**Angskar**
I always just maybe was trying to clarify basically between the root and the slot number and everything, but I think Alex did a good job. 

**Tim**
Okay. Does anyone else have questions or thoughts on this? 

**Lightclient**
I think the only thought I have is I would like to consider more adding this as a piece of the state versus just having it as a ethereal thing in clients to fill the op code. 

**Alex**
Got it. 

**Tim**
Is that not what…

**Alex**
Do you mean getting rid of it or keeping it?

**Lightclient**
Getting rid of it out of the state. I'm trying to convince myself that it makes sense as a piece of the state. 

**Danny**
Yeah, I mean, the main thing is if you only have it as a like a…if you don’t have a state, you can only read the previous header, right, because you're going to the previous peak and because it's the only thing that's going to be available because it's going to be in the header. And at that point, you make the UX of sending transactions really tough like you have to your transaction has to be for precisely the previous block. So you cant see it into the next block because otherwise you're going to make making proofs against the root that's broken with respect to your proof. So the state and then being able to bound your proofs against a particular slot make it so that you don't have like weird failed transactions and bad UX round using the op code. Is that what you were considering? 

**Lightclient**
My understanding is that you have access to 8192 routes. Is that wrong? 

**Alex**
No, so yeah, I think what Danny was saying you could do that still with what Lightclients trying to do with having this like extra history parameter. So this point is just like do we want to have this like in position history or not? You know, Vitalik and others in the past have done something way from that. I think it's cleaner. Danny put some comments in the chat around how we handle this in the CL and again, I do think it's cleaner. 

**Danny**
Lightclient are you just claiming that you should just have them, like hanging out on a client. 

**Lightclient**
Yeah. 

**Danny**
That's really bad for statelessness, right? 

**Lightclient**
I mean…Why? Like we already have it for block cache and you have to have this data whether it's part of the state try or not. It doesn't seem right. 

**Danny**
But If it's if it's part of the state try, then it just becomes if people are accessing it in statelessness, it becomes part of the proofs. Whereas if not, then your client in statelessness has to have this data locally and like have gotten it from previous blocks or somewhere else and the proofs. So it makes the…

**Lightclient**
I see.

**Danny**
It just kind of adds complexity there, whereas obviously we have that complexity with the 26 block hashes. But reducing that actually makes like I would want to eliminate these things so statelessness is cleaner and has fewer dependencies rather than add to them. 

**Lightclient**
Yeah, okay, I think that makes sense. 

**Tim**
I just given the like amount of back and forth on the design on this, it probably makes sense for us to discuss it like next week on the CL call once people had a bit more time to like wrap their heads around it. Yeah, does that seem reasonable? No, no breakouts. I don't think this this warrants a break out. 

**Danny**
We can do this one. I think. Yeah, we have a low agenda next week. So we can spend 30 minutes on it. Its fine. And I think. Oh, sorry about. 

**Lightclient**
I just say obviously I think that this EIP is pretty important and that we need to come up with a way of getting the beacon block root into the EVM. I just want to come up with the best design. 

**Tim**
Yeah. And I guess yeah, in terms of like this CFI conversation, I feel like now that Shane guy is completely out of the way does it make sense to have the next EL call focused on just generally what are the things we might want to verify for Cancun and so that we're not like just making this one like one off decision now, but like we can also have like two weeks for teams to just look at the set of things that are being proposed and try to think about like what's like a coherent set of things we want to do. And even if we don't agree to like everything we want to do in the next week, like maybe we can like flesh out the one or two most important things on the next call alongside for it for 4844. 

Yeah, just I don't know. So kind of we don't just like add things CFI one by one and then realize we have like five EIPs we've created to without having like a higher level view. And I mean, I don't know if anyone strongly wants to like CFI this now we can have that conversation as well. I think otherwise having like a higher level conversation in two weeks probably makes sense. 

Last call for objections. Okay, yeah, so let's do that. And I guess over the next two weeks as well. We have this Eth magicians thread. I believe all of the EIPs that have been proposed are either linked in that thread or there's also a tag Cancun candidate on Eth magicians. So I'll make sure to update the main like the first post on that thread with everything that I'm aware about that has been proposed so people can look at that. If there's anything missing there, feel free to ping me either on Discord Twitter, Eth magicians. So I'll make sure to keep that up to date before the next call. And then yeah, if client teams and just folks generally want to like think through the various options what we should prioritize. I think that would be valuable. Yeah, does that make sense? 

## Capella Genesis

Okay, next up then I believe it was Pari, you put this on the agenda, the idea of starting devnets with copilot genesis. You want to take a chance about that? 

**Pari**
Sure. Yeah, I just wanted to bring it up to see if any client teams have already tested support. And if not, if we could start testing support. So we can start testnets from Capella instead of Bellatrix genesis states. And also asking that in the context which that supported in all the feature branches for the different. So I know for example, we can't start from Capella genesis and work it yet, but if it does work on EOF as well as 4844. 

**Gajinder**
For Lodestar, it should be possible to start from Capella genesis. 

**Tim**
Any other clients? 

**Pari**
Cool, I can also reach out to the teams separately for that. Thanks. One other time we had the ? testnet that's currently live that was meant to be public and test withdrawals. We'd like to officially announce its deprecation and we hope to take it down next week Wednesday. So if anyone’s using it for something active. Please let us know. Otherwise it will be deprecated by then. 

**Tim**
Got it. And I know in the 4844 calls, like two weeks ago, we were talking about setting up a longer lived 4844 devnet in the next few weeks or so as a spec, yeah, once we have that up, we can point people in that direction is like the main thing to go if you want to test the cleaning edge features before they go on public test. Okay, anything else on Cancun?

**Danny**
Just real quick, the way that we do releases on the consensus specs is they don’t release candidates until the rules are actually on mainnet, the rules and logic is now on mainnet so the next couple days will be releasing a consensus specs non RC release. This will also include the transaction type change to 0x3 on 4844. So I believe that will kind of give us a good target for testnets. 

**Tim**
Nice. And this reminds me we should mark all the EIPs for Shanghai as final now that they're on mainnet. So EIP authors of the Shanghai EIPs. Yeah, if you can open a PR just to move it to final given that they've all been activated as well. Sweet. Anything else on Shanghai or Capella?

## [State that payloadId should be unique for each PayloadAttributes instance execution-apis#401]( https://github.com/ethereum/execution-apis/pull/401)
 
Okay, if not, Mikhail, you had posted the engine API PR discussion. There's a bunch of people who chimed in on the agenda already, but do you want to give some quick context on that then? Yeah, we can discuss it. 

**Mikhail**
Okay, the original problem is that in that Nimbus and Besu here pair Nimbus and Besu combination, there was a bug when an Nimbus send a purchase updated with below said, pay load attributes initiating the build process, pay load build process, then it resend this in the same slot, if I'm not mistaken. 

The new payload attributes with changed with goals and the problem is that Besu did not factor in factor in goals into the payload ID computation process. So they did not restart the payload build process and that led to failure proposal. And it appeared that we didn't have anything about that in the spec saying that the payload addition is unique, they didn't apply the build process and be anyhow related to payload attributes. And yeah, hence the proposed fix to the spec. If I'm yes, if I understand correctly, there might be some other EL clients that are affected and probably guys somebody want to chime in and share more information on that. But respect to the fix, so the fix is here and there is a discussion happening in there. So soon to engage EL client devs to look at this PR and if it is okay, say something or participate in discussion. 

The idea also is that by having this in the spec, having the statements in the spec, we can then create the test and then force this behavior to avoid such problems in the future. So that's it. 

**Tim**
Thank you. Lukasz you have your head up. 

**Lukasz**
So unfortunately, Nethermind also doesn't include the withdrawals also when calculating the payload ID so we will be fixing that soon. 

**Tim**
Okay. And there was a comment, I guess, by Gajinder on the agenda where he said it should not be possible for a CL since withdrawals to like send it to payloads that are yeah there are two four chase updated messages that have the same attributes for everything except withdrawals. So he was curious when like what would trigger that. 

**?**
I don't know. 

**Mikhail**
So it should be bug on the CL side.

**Potuz**
Okay. Yeah. This is probably a bad cache head state. Like sending the word for different head state. 

**Tim**
Got it. And so the fix would mean that even in the case where you send like this buggy, FCU message, you still get a different payload ID because at least one of the attributes has changed. Is that correct? 

**Mikhail**
Yeah. And then you build process should be started to, you know, to factor in this the information withdrawals in this case, for instance. 

**Gajinder**
Yeah, but the proposal will still fail because withdrawals shouldn't be any different right. So if it's giving different withdrawals, then probably it has calculated the withdrawals incorrectly and the proposal will eventually fail. 

**Tim**
Yeah, Mikhail?**

**Mikhail**
Yeah, yeah, yeah, yeah, just. Yeah, there was a. Yeah, the failure is because the withdrawals were sent had different values. So yeah, that's the failure. So it's basically not because of the Azure only. In this case, because of the bug on CL side and this behavior on the outside as well, so which didn't match up with the new withdrawals information. Sort of makes. So, but yeah, we'd like to, you know, to. Yeah, I think it makes sense makes a lot of sense to have this in its back and. Of course…test this as well. 

**Tim**
Okay. I guess in terms of next steps here. Should we just go ahead and merge this change? Yeah, I think ? had a comment as well which I don't have time to read, but should we maybe leave it open? A couple more days just to make sure we address all the issues or like the comments on it then. Yeah, close it then?

**Mikhail**
Yeah, yeah, I would, I would leave it open for the next several days, probably for a weekend. Yeah, then just merge. 

**Tim**
Yeah, and at the very latest then on next week's CL call, we can agree to merge it. 

**Mikhail**
Yeah, yeah, yeah…

**Tim**
Yeah, yeah, do it before. Yeah, okay. Sweet. Anything else anyone wanted to cover? 

Okay, and Merrill saying in the comments, we can add a high test for this case as well. Okay, I don't want to be like we can yeah, we can. 

**Mikhail**
Yeah, we can basically work on high test and parallel. So it's still makes sense. Not wait for it. 

**Alex**
If there's anything else I have one thing to bring up around MEV boost. 

**Tim**
Yes, please. 

**Alex**
So there's an RPC. Okay, so this is about verifying blocks from builders as they go to the relays. And there's a custom RPC that flashbots implemented in their relay. And right now, basically, it's just in the fork of death. This came up on the MEV boost community call. One or two calls ago, where we'd like to have client diversity at this layer of the stack as well. And what that means here is having other ELs. EL clients implement the same RPC. Something like basically having a standard for this and then everyone's supporting it. Is this something that people are interested in doing? Do they see value in this? Do they think it's a bad idea? I think probably if we all think it's a good idea, then I can go and like work on some sort of RPC, RPC spec, but I just wanted to get some sort of initial temperature check before I go and do that. So, completely. The point is saying given a given a payload like is this payload valid. 

**Tim**
And in practice, I see we would have this in the execution API's repos. And I think, does anyone think like this does this not belong there? 

**Danny**
Okay. Wait, would this go into execution or beacon APIs. 

**Alex**
Sorry. This is a EL. So there's a separate discussion point for having this. Essentially having the CL parts be at the CL. And this is essentially the EL part happen at theEL. And I think we need both in different places. But yeah, this is just for having this via standard API across ELs so that's because very not basically all the relays are using network and got. And given how many blocks come through the system, you know, it kind of harms all that for it's been done with client diversity at that part of the stack. So it'd be nice to have optionality here. I'll take the silence as compliance. 

**Tim**
Yeah, yeah, yeah. So I think, yeah, you can just open a PR in the execution API's repo, which is where we have all this stuff specified now. Oh, yeah, Mikhail?

**Mikhail**
Yeah, I'm just recalling that we were agreed to double check on this thing, which is feel the right flag for get payloads. So what we have decided on the previous call is that if any EL team is willing to implement this heuristics for this type of flag before the next hard work, then it will make sense to, you know, to stake it out right now and start working on it. But as far as there are no like attention to this PR. So I'm just, you know, reading this as there are no intention to work on that. So I think we should just push it to the next hard fork and include it in the scope of Cancun Or function API changes that are go for Cancun. So if anyone thinks the opposite. So that's just, yeah. Go to the PR. The comment. 

**Tim**
Yeah, sounds good. And it was a comment on the PR. I think by Alex, who said it would be nice to see some prototypes of this working before we decided to add it to API. Yeah. So I don't know. 

**Potuz**
We know on the CL side, we can do this immediately. And on the EL side, I think ? has a draft. I don't know how much. Them that be worked.

**Alex**
And just to add some context. The comment there was essentially saying like this could all be done outside of having any formal stacker API that we all agree to. Like, you know, if the concern is like some sort of censorship resistance detection, then actually prototyping that out. Ideally and like, you know, clients may not, but, uh, yeah, it just happens in use case beyond like, oh, yeah, there's this like additional thing that everyone has to deal with for all time moving forward. And like it'll probably do something without actually you know, doing something. 

**Potuz**
So in my original issue, I added three different heuristics that I think are pretty valid. And they are, they just have a couple of constants that are configurable. So by prototyping them, you mean having some yield that actually implements some of those heuristics at least. Right?

**Alex**
Yeah, it would be nice. I mean, again, this is not a blocker, but. Oh, I can turn this other way. Go ahead. 

**Potuz**
No, but I think this is actually proposing this as a blocker, which I agree. I think we should have at least some sort of like draft PR of some EL that actually wants to implement some of these heuristics before we push to have this in the specs. 

**Alex**
Great. Yeah. 

**Tim**
Okay. Anything else?


Okay, then yeah, let's wrap up. Yeah, thanks everyone. Congrats again on Shapella and talk to you all in the EL call next week. Thank you. Bye. Bye. Bye. Bye. Bye. Bye. Bye. Bye. Bye.

### Attendees
* Tim Beiko
* Danny Ryan
* Pooja Ranjan
* Mikhail Kalinin
* Alex Stokes
* lightclient
* Justin Traglia
* Ignacio Hagopian
* Marius
* Joshua Rudolph
* Mario Vega
* pari
* Marek Moraczynski
* Roberto B
* Ben Edgington
* Moody
* Mike Kim
*Trenton
* Crypdough.eth
* Gajinder
* Marcin
* Guillame
* Danno Ferrin
* Andrew 
* Saulius
* terence
* Fabio Di Fabio
* Potuz
* Alex
* Lukasz
* Alexey Osipov
* Oleg Jakushkin
* Ayman
* Spencer
* Jamie Lokier
* James He
* Phil No



























