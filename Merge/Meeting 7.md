# Merge Implementers’ call 7
### Meeting Date/Time: Thursday 2021/7/1 at 13:00 UTC
### Meeting Duration:  46:09
### [GitHub Agenda](https://github.com/ethereum/pm/issues/345)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=6d944TCNpqc)
### Moderator: Mikhail Kalinin
### Notes: Jared Doro

-----------------------------
# Summary
- Merge call will be ending soon, discussing the merge will happen during the all core devs and the proof of stake consensus call depending on the part that is going to be discussed.
- Discussed limitations of current JSON RPC consensus API and it's future which brought up questions like HTTP vs WebSockets and The need or lack there of for bidirectional communication
- We are expecting London in a month and we are expecting Alitar in a couple of months. 
- A very high-level checklist will be added to the pm repo soon
-----------------------------
**Mikhail Kalinin**

Welcome everyone to the merge Implementers call number 7.
First congrats on goerli fork this is one more step towards the merge which is great.
We do not have much on the agenda today so its going to go really fast, we will go through a few updates and I’ll discuss plans for q3
# 1. Implementation
**Mikhail Kalinin**

I’ll start with implementation updates 
I have recently been working on the prototype of the transition process
the part of the spec has been merged a couple of weeks ago.
So, it has been implemented in teku I have worked with it on a local network a few things to share about this testing.
I have tried it in a positive test scenarios and a negative test scenario. 
where the block proposer tried to produce blocks before the computed transition total difficultly has been reached
It went well. 
We need more thorough testing with more mass on the network side.
like withholding the proof of work blocks by some parts of the nodes of the network and then releasing them and so forth
Also, one thing to bear in mind here is that I used local miner, so its results have high fluctuation in block time intervals.
One of the goals of the total difficulty computation is the predictable at merge time, that wasn't checked well locally because of fluctuations. 
So, it should be checked with a real miner which can produce more hash power
That is the update on my side but anyway it showed that the algorithm in general works which is great.

**Danny**

Very nice how do you think we best test some of these more complex scenarios for example partition in the network for 2 epochs after hitting the transition difficultly do we have anything in our toolkit to test that stuff of do we have to build stuff.
That is a good question I was thinking about simulation.
Like simulating the network stack if we want some predictable scenarios
so, we can have some parameters of the mass that we to have on the network layer
No, I don’t think we have any tools for that. 

**Danny**

We could do on the consensus side we could write fork choice tests that essentially like a chain being built and then another chain is reveled  with different difficultly and stuff.
There is a little bit we can do there in an isolated fashion, but the simulation probably makes sense.

**Mikhail Kalinin** 

Yeah, right what you have just said I was thinking about to stop the network that can be managed by some processes and send messages according to some time interval.
So, something like that needs to get done
Also about the fluctuations, I was wondering if we have stable time intervals for Robsten for example are they stable on Robsten?
are they more stable in terms of the difference of the mean time?

**Danny**
 my understanding is that it depends on the day and whos mining on it. 
 But I would suppose more stable than what you were doing.

**Mikhail Kalinin** 

Okay so I guess we can move on.

**Danny**

Given that clique  still use total difficulty can what you’ve written be anchored on Gorelli or clique relatively easily?
Because if so, that would give you good block time.
It is probably worth considering if that can be ported pretty easily. 
I think because it uses total difficulty it should be able to be just because we do have some test nets we do want to fork off of Gorelli.

**Adrian Sutton**

The one catch with predictability on goreli is that an intern block gets a difficultly of two and a out turn block one.
there is a lot of out of turn blocks. So, you are halving and doubling your difficulty a lot.


**Danny**

gothca

**Mikhail Kalinin** 7:25

Thank you, Tomasz, for the information on the Robsten
So, lets bear it in mind and get back to this question later on how to check the predictability
And yeah these historical data on difficulties could be valuable
Okay, any other implementation updates.

**Danny** 

I think were primarily London and Alitar.

**Mikhail Kalinin** 

Yeah, it makes sense London and Alitar okay
# 2. research updates

**Mikhail Kalinin** 8:18


let’s get to research updates a couple of PRs that have been announced in the previous call which is the 
cleanups in the beacon chain spec by Justin and Eden (I am not sure 8:40) they have been merged so cool.
also, I have been looking into the current limitations of consensus JSON- RPC 
let me share the doc this more of a problem statement than a proposal on how the consensus api should look like. [Link](https://hackmd.io/@n0ble/problems_of_consensus_json_rpc)
So, let me give you a bit of context on that we have the consensus json rpc implementation which we used for rayonism.
And it worked well for the purpose of rayonism, and it would probably work well in production.
But some of us are suspicious about it being production ready here is a few arguments contributing to this.

The main question here is if we go with the json rpc biased consensus api 
which has some restrictions and which lays some restrictions on the use cases
we might want to replace it at some point in the future.
So, the main question I would ask and the main question that the document states is that wether we are ready to develop and new communication protocol right now before the merge or should we take an easy spot right now and think about it and do it later.
So that is the main question, I can go through the problems real quickly that I have found in the current implementation and design

**Danny**

Before that I would say whatever does actually gets implemented it is probably very likely to be sticky in terms of difficult to replace once it is in production, I haven't read through this doc yet but if there are actual problems, I suggest we fix them soon

**Micah Zoltu**

Quick question did we answer the question from a few meetings ago?
as to wether this needs bidirectional communication or unidirectional?
like is it always requests from one end to the other end with response going to the other direction or sometimes does the other end need to innate?
 
**Mikhail Kalinin**

I see and this document denotes some cases where bidirectional communication is needed or highly desirable.
Yeah, this is one of the design considerations, so we use the 

**Jacek Sieka** 
   

**Mikhail Kalinin**

sorry?

**Jacek Sieka** 

Sorry go on.

**Mikhail Kalinin**

Jacek, please go ahead.

**Jacek Sieka**

Yeah, another big question wether we want to go to rest instead because that is what the new clients use?

**Mikhail Kalinin**

Right, there is a sub-topic in this doc also
let me just get to the problems, I don't we will not be able to come to a conclusion or any solution in this call
This is just food for thought for the next calls and meetings 
The first problem with the existing protocol, is it lacks one the messages that will tell the execution client that the consensus of the beacon block is validated.
Which is obviously required because the execution payload of invalid beacon block will be stored and served through the users json rpc could lead to some bugs in the services and software
We need this explicit message because we also have a set head message that also tells what is the head of the chain, but not every block becomes the head of the chain when it is imported so we need a separate message to signify that consensus is valid.

**Danny**

So essentially a commit after initial processing?

**Mikhail Kalinin**

Right, so it will look like the new payload is sent to the execution client its being processed while being processed it will receive this new type of message that the consensus block of this payload is valid or invalid and the payload will be easier discarded or persisted after the processing.
The next thing is we have several messages that are causally dependant like newBlock, newPayload, setHead, and this new type consensus process message.
Current protocol relies on the assumption that the order or all causally dependant messages will be preserved on the consensus and execution client side. so, they need to be pipelined which is just bug prone so we might want to just release this assumption. 
In order to do this execution client will have to store some state of the messages receive from the consensus client, like if it has received a new payload it can then receive this set head or in consensus process messages the order of these messages will not be preserved
Then it can gather this whole information in this kind of state and this kind of cache, and then decide what to do with the payload.
This is one of the things, the next one is http overhead which requires a new connection each time the request is being sent. Also, we can’t do asynchronous communication with http only. We can do this with techniques, that allows for this.
So, we might want to use something like websocksets which opens a way for bidirectional communication. 
LIke the last use case failure recovery, lets assume that the execution client just crashed the and the consensus client persisted some block while the execution client does not have the payload for it so it has not been persisted. so, it starts off and the consensus client will send the next block, the block which the execution client has no parent for. So according to the current state of the arts
the execution client will have to go to the network to pull the state to continue the execution which is suboptimal. We might want to look at some more optimized scenarios. like the execution client starts and send the status message with the head of the chain to the consensus client then the consensus client decides what to do. If the gap is one or two blocks it can replace those blocks with out making the execution client go to the network.
That was the last use case
The overall thought is it would be great to have it expandable in the future. 
It would be great to design a protocol that can be expanded with new messages and new use cases without need to design a new protocol
because we have some restrictions  
That is it.

**Micah Zoltu**

You said that before the failure recovery the execution client can go to the consensus client and ask for the last two blocks, does the consensus client keep?

**Mikhail Kalinin**

It can send the massage and say, "here is my head" and consensus client can decide what to do. It can ignore this message and execution client will have to go to the network to prove the state or prove those two blocks.

**Micah Zoltu**

The consensus client might store the last few blocks in memory or something so you can optimistically ask "hey by the way do you have this because I know you are local, if so give them to me. If not, I will find it myself" 

**Mikhail Kalinin**

Right this behavior could be more optimal than just going straight to the network
Yeah, even if these blocks are not stored in memory, they are stored in the database so they can be replaced.

**Micah Zoltu**

But not the bodies, right? you still have to go to the network for the bodies?

**Mikhail Kalinin**

No, the bodies are also stored, am I not mistaken?

**Danny**

No, the bodies are certainly in the beacon block, but you could imagine using the execution engine locally to store the bodies, so you don't have redundancy there

**Micah Zoltu**

I mean we already have a state flow problem, this feels like we are doubling that. Am I incorrect?
If the consensus client and the execution client are both storing full blocks and full bodies.
Then the only difference is the state which is only 1/4 or 1/3 of our total state flow problem.

**Mikhail Kalinin**

I guss that at some point beacon block clients will not store blocks beyond the weak subjectivity checkpoint.
 
**Micah Zoltu**

Yeah, that makes sense.

**Mikhail Kalinin**

Yeah, the failure recovery case is one of the cases depends on bidirectional communications also it could be a sync process we can if we need some rich scenarios for state sync it could also rely on the bidirectional communication

**Danny**

yeah, I think the one thing missing here in this document is the potentially messages required to communicate during state sync.

**Mikhail Kalinin**

Yeah, it has been mentioned in the last section, but just briefly.

**Danny** 

ahh okay

**Lukasz Rozmej**

So just one small comment from me, that each http request requires its own connection. that is available there are ways to have persistent http connections. I am not sure if every library we are using supports it. 

**Mikhail Kalinin** 

I see we can use WebSockets which is already supported

**Lukasz Rozmej**

Even there is a keep alive in http1 header that allows you keep the connection alive until the time is up

**Mikhail Kalinin** 

Yeah cool, great. I was thinking about http2. But why not use websockets as they are already supported by the clients   

**Micah Zoltu**

My gut tells me that given the problems that you have laid out that websockets seem like the way to go.
Just because its easy, yes you can use http keep alive its not too hard, but not too many people are familiar with it and libraries often do not support them out of the box You will have to fiddle some bits.
Websockets out of the box they will do exactly what you need, keep the connection alive, they will let you know when the connection dies, the connection won’t die randomly, and you can have it timeout in theory like the http keep alive.
They give you bidirectional communication, so you do not have to run an http server on both clients you just have one is a server and one is the client you just establish the connection and it just runs form there

**Lukasz Rozmej** 

one last comment from me http 2 connection are also persistent, but I agree that websockets are probably better for our use cases.

**Danny**

Maybe you mentioned this as one of the reasons but another reason that you might want bidirectional here is async processing of insert block so that the execution layer can tell you once it is done rather than you waiting

**Mikhail Kalinin** 

Right Yeah that can be done with http servers and advanced technique anyway yeah.

**Micah Zoltu**

how long does that take in worst case scenario like how async is that?

**Danny**

how long does it take to process an eth1 block?

**Micah Zoltu**

okay so like 250 MS order magnitude

**Danny**

Yeah, maybe the worst-off block is 10 times that.

**Micah Zoltu** 

Yeah, sure I was just wondering if we have to worry about http timeouts kicking in at 2 minutes or something.


**Danny**

Yeah No I don't think so, so maybe thats not a design use case but is Garry’s comment correct in that the primary reason that we want bidirectional is the failure recovery case?

**Mikhail Kalinin**

Yeah, but potentially other cases that we might have not identified so far. 
Yup asynchronous communitarian would be implemented with these bidirectional communication channels as well.
I do not speak about this today but if we will be looking into redesigning the protocol  we might want to also look into encoding the json. It’s probably better to use some binary encoding and then we can ask whether to use ssc or rlp or whatever else
    
**Jacek Sieka**

I mean that is an important consideration. we already have like two protocols that follow the same thing which is basically talking between components. the more we add the more increase the security surface and audits become tricky.
It’s just annoying to write a client
If we have websocket json rpc, http rest, and maybe grpc somebody will soon mention. That is a burden for developers.

**Micah Zoltu**

Isn’t the idea here correct me if I am wrong, but this conversation websocket, json rpc or whatever would replace http rest in the consensus client, or no?

**Danny**

So, this is the user facing apis that are defined in that restful http

**Micah Zoltu**

I see

**Danny**    

which this is independent of that and should be discussed independent but the fact that that exists in the stack already 

**Micah Zoltu**

yeah

**Lukasz Rozmej**

One question from me about the payload size. It is a question, so I do not know. wouldn't it be even better to just keep it as json, but just enable some compression methods rather than doing binary?
I am not sure what one would produce smaller payloads?

**Micah Zoltu**

Because we work with a lot of numbers binary will almost certainly be smaller because json numbers are gigantic because they are strings. That being said json does compress a lot and you do gain a lot by compressing it.

**Mikhail Kalinin**

Do websockets support, ahh  so it is completely on top of websockets.

**Micah Zoltu**

yeah, WebSockets are just bytes on a wire

**Adrian Sutton**

You can compress websocket text messages with gzip the support in servers was fitted a few years ago, and yeah it surprising what you can get away with when you gzip json, like very surprising I used to do market data over json.

**Danny**

Be careful about discussing modifications to the payload format it something that is opaque if we don’t necessary need it.
I’d like to see some numbers before we swap that with

**Adrian Sutton** 

the other thing is in the standard api we started using the accept header to negotiate content types so you can get ssd formatted block or state for example
But the default is json and that is really usefully to be able to upgrade to support ssd I want to save some bandwidth or whatever

**Micah Zoltu**

does anyone have an argument against WebSockets? 
I see a lot of people saying "Yes WebSockets sound great"
does anybody disagree with that?

**Adrian Sutton**

I think its probably a good fit here the only concern I have with WebSockets in the past is that it doesn't always go through
I have always done a websocket with a plain http fallback. cause eventually you find firewalls and things that just don't do the websocktes upgrade or just kill the connection regularly. But I don’t think that is a design consideration for us. Thats more public website kind of stuff 

**Danny**

 I just echo what j said with adding another thing, I think we should work through the design considerations that Mikhail has placed for us here and at least fully validate that we really need the bidirectional before committing to taking it on

**Micah Zoltu**

so websockes I believe are implemented in all major clients right now. for the json rpc endpoint you can use websocket or http
 so, for just the werbsocket part I don't think we would be adding any new technology.
If we did something new on top of WebSockets that would be new but json over WebSockets is already implemented.

**Danny**

on the execution engine.

**Micah Zoltu**

Yeah, that is true, execution engine only.

**Mikhail Kalinin**

yeah, but libaries that are implement clients of json rpc are supporting WebSockets I guess. 
  
**Danny**

Curious Jacek do you all have WebSocket implementation in nimbus eth1 side?

**Jacek Sieka**

Yeah, we do, it is not a problem that way really. Its more like it becomes an incredible zoo.
So, you want to use this beast and then you have to have a websocket server running and a http rest server running, and a http json rpc server running, and a devp2p port, and a p2p port, and a discovery v4 port and a discovery v5 port.

**Danny**

it should not have the v4
**Jacek Sieka**

well, you know, that is 6 already and I just ripped those off the top of my head.
That is where the complexity lies. it is just a lot for the user to even manage or set up.
Imagine the firewall rules for everyone, etc....
SO, I mean its not really a question of what libraries are available
because there is a ton of them, but each library brings in its own dependencies, its own configurable complexity the overhead to learn those frameworks really, like the ins and outs and the details of websockets vs plain http vs rest over http which has a different framing and so on. 
like that is more what I am talking about. THe complexity overhead in general not wether a library is available or not.

**Micah Zoltu**

I agree with the latter point you made for the first point though I feel like even if we did http here you should still be exposing this on a different port than the public facing json rpc stuff, at least for the firewall stuff you will need a new port I believe or should. I agree with the later half that it does increase complexities adding other frameworks

**Mikhail Kalinin** 

thanks for your valuable inputs and
I guess we should think more about it before making decisions and for potential use cases in the future before we chose one over the other solution.
What can a little bit reduce the complexity of design and implementation of this protocol is that these two parties communication via this protocol are going to trust each other so I don't think it reduces it significantly 
 
**Micah Zoltu**
My two sense on Danny's question wether we need bidirectional or not. again, my gut feelings form the conversations I have been overhearing is that there are enough situations that we think it would be valuable.
That it feels like eventually we are going to need it, sure we can argue that any of the individual examples we could get away with not having bidirectional communication, but they would be a little better with bidirectional, but I feel like there is enough of those that like my background tells me that eventually that is going to continue piling up and you are just going to end up making sacrifice after sacrifice after sacrifice if you don't have that bidirectional communication.
Wether that is long lived http or websocket or whatever matters less, but I do feel like bidirectional feels like the right way to go.

**Dankrad Feist**

I guess a question here isn't the kinda the future that the execution client becomes more and more minimal in its feature sets.
like more and more just be there for verifying blocks and maybe producing blocks.
So, I guess I wonder if its really true if the long term is different.
like should users really long term rely on the eth1 rest api to get their data? 
No, I mean they should use one api and thats probably the eth2 api because thats the only one that can get you consensus   

**Mikhail Kalinin**

yeah, but there is a bunch of api that is exposed by the execution client, so I guess a lot of servers sets? are using it
it will not be easy to replace one with the other, or to move it to another endpoint and another protocol

**Dankrad Feist**

I think we will just have to do it long term, if we don't do it it will always be pretty weird.
Do you think in the long term users will want to install two separate pieces of software and configure them and so on?
Like one of them should be really really minimal in my opinion, so more like a library.

**Micah Zoltu**

What I have envisioned which I know not everyone agrees with is that over time many years we will probably move to more pieces instead of less. But they will become packaged better. So, from an end user perspective you double click an installer and it installs 3 pieces of software like 3 services on your host.
You don’t know that because you are a user, and you just clicked the thing. 
But there is 3 pieces of software and one of those pieces is biased on a reverse proxy. it is just a thing that you connect to the two backend pieces.
This would be more the traditional architectures, I think packaging matters a lot there. I think we do want it to package into a single double click for users, but for more enterprise focused customers they will benefit form having those individual services that they can talk to separately

**Danny**

Yeah, I agree

**Dankrad Feist**

I guess I disagree in that I don't see why compatibility reasons you would want to talk to the eth1 client directly in the future.
because you don't care about some random state you always care about relevant state as in the consensus state, when you ask questions about ethereum, and so it doesn't make much sense to me in the future to ask eth1 client except if that is the only thing you can do because you have existed before this was written

**Micah Zoltu**

so, I think the primary reason that I wouldn’t want to do that is because each client has different feature sets that are added beyond the base feature sets, and your execution client may have a particular feature that you want like tracing that other clients don't and because it is not a standard feature you can’t access it thorough the consensus client. You need to go to directly to your client because it’s added a special feature just for you.
OR nethermind for example has plugins. so, I can write a plugins for nethermind the consensus client knows nothing about that  and so if i want to talk to nethermind I have to go directly to it

**Danny**

And the execution engine would does know what the head is so for many of the things you do want to query it does have an idea of consensus in that sense, but again once you have it packaged up nicely and have a standard proxy to get to it all, the common end user does not have to think about it.

**Mikhail Kalinin**

Every execution client will be  accompanied with consensus client which is this through and by
Yeah, also for these use cases probably we need the consensus data as well, so it could be like the unified advocate
that can request data from the consensus and combine them with data from the execution client. potentially this is one of the potential design solutions here and then get back with this data to the user so it will be one interface that has all of the things.
Okay so let’s stop here, thanks everyone for this discussion
Do we have any other research updates?
# 3. Quarter 3

**Mikhail Kalinin**

okay let’s move the plans for q3 this is the first day of q3. 
we are expecting London in a month and we are expecting Alitar in a couple of months. 
With all of this in mind we are expecting more focus on the merge during this quarter
regarding the plans fot this quarter, so far, we have the beacon chain or consensus specs are in the feature compleat state  
so definitely there will be some requirements, bug fixes and additions like on the network spec and api change as well, but in general we have the design we have the transition process so far and it makes sense for q3 to focus on the execution client specs on the eips on the consensus api. That is what we are going to do this quarter. 
also, would be great I think we will have more testnets coming in the second part of the quarter.
That’s the high-level view of the plans for q3

**Danny**

Yeah, I think the consensus spec will also rebase on altiar relatively soon and also integrate london changes to execution payload which would include something related to 1559 and also figuring out the testing standards we already have consensus side test factors being generated we will be extending that and then figuring out how the execution layer leverages the existing tests and extend them in this new context . I think that is something important to figure out in q3 
By default all the evm should just continue and they should continue, and they should operate independently, but i think we just need to kinda touch it and make sure we are happy with the way that tings are structured

**Mikhail Kalinin**

also, at some point we are going to stop making hte separate merge calls
probably will have one of two more then we will keep discussing the merge during the all core devs and the proof of stake consensus call depending on the part that is going to be discussed.

**Danny**

Mikhail  and I have been working on a very high-level checklist of all the things that we will share soon and probably put in the pm repo.

**Mikhail Kalinin** 

any questions and suggestions to the plans?
great any spec discussions?
Okay any other discussions?
Does anybody want to say anything else before we wrap up
...
Great
Okay thanks everyone for coming.

## Date and Time for the next meeting

Thursday 2021/15/1 at 13:00 UTC
## Attendees
- Jared Doro
- Pooja Ranjan
- Mikhail Kalinin
- Jacek Sieka
- Dankrad Feist
- Adrian Manning
- Adrian Sutton
- Alex Stokes
- Ansgar Dietrichs
- Danny
- Duston Brody
- Gary Shulte
- Hsiao-Wei Wang
- Karim T.
- Lightclient
- Lukas Rozmej
- Many Ratsimbazafy
- Micah Zoltu
- Protolambda
- Sajida Zouarhi
- Terence
- Tomasz Stanczak
- Trenton Van Epps
## Links discussed in the call (zoom chat)
- 07:58:13 From  Mikhail Kalinin  to  Everyone:
    Starting in 5 minutes
- 07:58:15 From  Mikhail Kalinin  to  Everyone:
    Agenda: https://github.com/ethereum/pm/issues/345
- 07:59:32 From  Gary Schulte  to  Everyone:
    Have a link to the closed source client?  Haven’t heard of it and google not coming up with anything
- 07:59:48 From  Mikhail Kalinin  to  Everyone:
    https://github.com/sifraitech/grandine
- 08:03:19 From  Adrian Sutton  to  Everyone:
    Görli has hit it’s 30mm block gas limit target. So that’s all sorted now.
- 08:03:50 From  danny  to  Everyone:
    https://github.com/ethereum/pm/issues/345
- 08:09:08 From  Tomasz Stańczak  to  Everyone:
    We have collected all historical difficulties and hourly / weekly / monthly vollatility of difficulty growth for mainnet.
- 08:09:14 From  Tomasz Stańczak  to  Everyone:
    On Ropsten the volatility is huge
- 08:09:15 From  Tomasz Stańczak  to  Everyone:
    Huuuge
- 08:09:28 From  Tomasz Stańczak  to  Everyone:
    Diff can go down to nearly zero and recover in a day
- 08:10:32 From  Tomasz Stańczak  to  Everyone:
    we will have charts for Ropsten since beginning probably this week
- 08:11:51 From  Mikhail Kalinin  to  Everyone:
    https://hackmd.io/@n0ble/problems_of_consensus_json_rpc
- 08:14:58 From  danny  to  Everyone:
    what we used on rayonism was uni
- 08:15:03 From  danny  to  Everyone:
    so the base was
- 08:15:09 From  Micah Zoltu  to  Everyone:
    👍
- 08:24:05 From  Gary Schulte  to  Everyone:
    Is the failure/recovery case the primary need for bi-directional comms between exec and consensus?
- 08:25:37 From  Tomasz Stańczak  to  Everyone:
    https://en.wikipedia.org/wiki/HTTP_persistent_connection
- 08:26:08 From  Mikhail Kalinin  to  Everyone:
    👍
- 08:26:19 From  Tomasz Stańczak  to  Everyone:
    WebSockets still the way to go (just linked http as a background to convo)
- 08:26:54 From  Micah Zoltu  to  Everyone:
    👍
- 08:28:50 From  Micah Zoltu  to  Everyone:
    "I don't want to speak about this today, but here is some nerd sniping bait."
- 08:35:25 From  protolambda  to  Everyone:
    Also consider yes/no websocket-upgrading via http as part of this. Eth1 clients all have different defaults here
- 08:35:37 From  Micah Zoltu  to  Everyone:
    Please upgrade with single port.  :)
- 08:35:49 From  Gary Schulte  to  Everyone:
    I was presuming that exec engine would be running the web socket server, and consensus would be the client
- 08:35:59 From  Gary Schulte  to  Everyone:
    But good point about multi-protocol
- 08:36:50 From  Łukasz Rozmej  to  Everyone:
    we  can always use compression with SSZ too
- 08:40:09 From  protolambda  to  Everyone:
    SSZ is designed for consensus/onchain messages, not API requests. SSZ has optional type for the data part of an insertion or response is useful, but not at all for API params
- 08:45:51 From  protolambda  to  Everyone:
    Time to rebase onto Altair too?
- 08:45:56 From  danny  to  Everyone:
    yeah

