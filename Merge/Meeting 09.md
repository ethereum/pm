# The Merge Implementers' Call #9: Engine API design space Call 2

### Meeting date/time: Thursday, Sept 9 at 13:00 UTC
### Duration: 60 Minutes
### [Github agenda](https://github.com/ethereum/pm/issues/385)
### Moderator: Mikhail Kalinin
### Notes: Darkfire-rain

## Changes in the Minimal set of methods

**Mikhail**:  Okay So welcome to the engine api discussion goal number two and actually discussion session around the engine api number three because we had an extra session during the previou acd call. The format of the call is the stays the same. if you want to ask question or just put  comment feel free to interrupt me at any point. if we are falling into a deep discussion around some particular thing,  we will likely  break it and follow up on that in the discord in order to not  destruct the general line of call.l And also we have an agenda for today as we'll start from some small change to the minimal set of methods that has been done since the previous discussion session and then go to the transition process. I'm no too optimistic that we will reach the end of the document today but I think we should cover most important parts by the end of this call.  Okay so let's get started with the change to the **minimal set of methods**. The first one is discussed in discord, I guess With micah and jim and I think it makes sense  if engine prepare payload, if  building a payload in advance is not supported by a client it should be implemented as a no op so it will just do nothing but the consensus client  will not have to adjust its  usual load building flow depending on the client on the execution client implementation so it makes a lot of sense. And i don't think anything to comment here.

 next is the  get payload limitation will now depend on prepare on this support of repetitive payload if it's fully supported then get payload should must return immediately with what has been built whatever it is even if it's just the empty payload, so the consensus client will have a guarantee that it responds immediately but if the prepare payload is not is a no op is not implemented then get payload will work as follows it just will go to the mempool, select transactions from it build the payload and return back so it will cause some delay. Also prepare payload and get payload might be overridden by clients that are optimized for mev and in this case the prepared product will be no op and the get payload will if there is the block builders in place it will just return the fully full payload to the consensus client so it will also it should also work like um it should also be an immediate return and yeah this is just an opportunity for movie clients how it could be implemented.

 **Micah**:  So we can discuss this further in discord i thought we talked about and agreed to and sounds like we misunderstood each other that get payload would always return immediately and it's up to the execution engine to you know figure out how to do that if they're running an mev client of some kind that might just be you know grab latest block and return it because presumably if they've already pre-validated those or if they're not running mav then maybe they should turn empty block or they return a block they built previously but i thought that get payload is always supposed to return right away like as fast as possible. and if you want to do more processing you should do it after you get the prepare.

 **Mikhail**: okay, okay I guess so it just builds a block on the prepare payload and doesn't update it right? this is like the potential implementation the potential behavior. if the client doesn't support this constant  updating of the block that is being built.

**Micah**: so even in that case like I guess my assumption is from from like an api
design standpoint it's very beneficial if the there are strong guarantees that the consensus client can rely on and timeliness of response to get payload is important because if you have if the client can rely on a very fast response from get payload then they can wait to the last minute to send it which is desirable because you want to wait as long as the kind of client feels is reasonable because you're more likely to get better transactions more expensive block et cetera whereas the consensus client has to assume that the yet payload response may be slow it means they have to send the get payload request sooner which means you have less time to build a better block and so I thought. again we can talk about this more in discord, I think you and i must have misunderstood each other as Well.


**Mikhail**: Yeah,  I get it yeah and yeah I tend to agree that.
 
**Gary**: Can we specify a time constraint that we get the response by?

**Micah**:   i think the trickiness with the time constraint is that it's highly dependent
on your like internet your architecture if you have your consensus and execution client both running the same machine then you know the round trip time is less than a millisecond and so you might have you might be able to wait until kind of even more the last minute versus if
you're running distributed maybe across multiple data centers or across multiple  machines across the world or whatever then you need to send it much sooner. so I worry about kind of doing a protocol level time constraint there um just because I feel like it's highly dependent on your architecture.

 **Danny**: the constraint is don't use this message to start doing really hard work and instead to final you know finalize the bundling of a block and pass it along. 

** Unknown speaker**: Isn’t that what the prepare payload is? 

**Danny**: This is when prepare payload isn’t called. so if a get payload is called essentially like should it at that point try to do hard work or should it just pass what it has which may be not something very good and I think the implication here is past what it has, it might not be very good or maybe it uses some sort of pending block structure and it should just pull from that but it shouldn't be a an initiation to like do work that's going to take a second or three or eight.

**Mikhail**:  i think that prepare payload must be called anyway anyway so it should be like a requirement so that get payload follows the corresponding prepare payload call.


**Danny*:  sure I meant if prepare payload was in no option

**Mikhail**:  oh yes yes okay I I thought you know 

 **Alexey**:  and I have a question so what is the what is the consensus Engine suppose to do between the calls of to prepare payload and get payload?

 **Mikhail**:  it's supposed to keep listening to the beacon chain network and probably update the head in between and call prepare payload once again with the new head.


**Alexey**:  so it may potentially issue multiple prepared payloads and then only one get payload is that's what you're saying?


**Mikhail**:  right if another prepare payload the new priority arrives yeah so it will the process of
building a block will very start it.

 **Alexey** so what i'm getting at is that the the reason why this things have been split into two pieces, right into prepare parallel and get payload is that because you might have a multiple of the first and only one of the second, right?

 **Mikhail** the initial reason is that the proposer wants to start, he wants to initiate the building of the payload in in some advance. it knows that like during the next slot or the next couple of slots, like the next few slots it will have to propose a block and at some point in advance it starts some point prior  the slot that it's supposed to propose.

**Alexey**: So it has all the information to prepare it but not the time to do it. right ?

**Danny**: It is the continuous nature of like proof of work where you're always about to try to you're always trying to make a block this is I actually know i'm going to be proposing a block and call it four seconds so I signal that the work is done and then I don't have to have this like pending block operation running continuously which apparently is pretty heavy depending on the implementation.

**Mikhail**:  actually, yeah this random parameter makes it no in this parameter. I mean it is like is it is only known after the parent block has received so upon receiving the parent block it will 

**Mark**: and every time the there's a new head the prepared payload needs to be called like i'm after in order to start building the block from that head?


**Danny**:  ifthere is a reorg, yes.

**Mikhail**:  right Yes yeah and also if like the block from the previous slot is delaying it could arrive later but the proposer might want to 

**Alexey** so it seems to me that this reason the real reason why we have it right now not in original reason is that you wanted to make this operation of preparing parallel interruptible so that you don't have to keep because obviously you could run it in multiple threads and you know choose the one that you wanted but you really want to interrupt the previous work to restart the new work.

**Mikhail**:  right it actually depends yes I mean yeah oh yeah we have an option here so we can add to the protocol that there is anOption 

**Alexey**: no because I think it's everything else could be could be simulated with other means I think i'm trying to understand the real reason why

**Danny** the real reason is that the when we were speaking with Geth on a call previously is that there was only the get payload which implied that either work needs to be continuously done before kind of like how pendingblock is done today. or it needs to be done at the at that call which can take a long time to get something valuable and now that we know what the proposer knows at least four seconds before proposal maybe eight   that they're going to propose and what they're going to build on they can send that signal and so that work rather than the continuous pinning block work being done all the time they can just signal to do it and then get it. there's the exceptional case that you then might want to handle where there's a reorg, in that time frame which is actually very unlikely in this this configuration but you could get say eight seconds before I think this is gonna be the head that's gonna be built on I know i'm gonna be the proposer i send it and then four seconds later i actually had to reorg and I want to override my previous repair payload and  then at the time of me proposing I call get payload and so the the motivator is is the is the prior thing that i've said but then you need to handle the case where rework happens which is why you might send to prepare payloads 

**Mikhail**: yeah right!  

**Lukasz**:  i have a follow-up question is there any sense if like we get multiple prepare payloads to construct multiple blocks and then one of them would be chosen on gate payload or is like if we get another we definitely should cancel the previous work is there any like case for that 

**Mikhail**: Yeah i've outlined in the like the section that is in in the bottom of the document. yeah it might be the case when you're um there are multiple consensus clients  that are using these that are sharing one execution client and they are concurrently building up who wants to build they want the payload to be built on top of different parent blocks but that's an exceptional use case and it should not be like.
  
**danny** yeah I mean that's also implying there's multiple heads which is not I think generally how this api is being designed

**Mikhail**:  right and yeah and it will have to support like multiple versions of mempool from what I understand if we want to keep building the payload um on top of different hat and if if these two heads are on the same chain  right if this is if this is these are the parent and the child blocks so it doesn't make sense to keep building the payload on top of the parent block if you already see that there is a child. Yeah in case of the child has been delayed and
was running late.

**Mark**:  just to understand that the dependency graph, so the only time, every time the the if you already called prepare payload and then you call like um new head I forgot what the fork choice updated, shouldn't it just,  I mean would you even need to call prepare payload again or
would it could you potentially just have it assume that okay actually you need to restart from
this new head and the dependency graph is always like to build a block you need a head


**Mikhail**: right but you should restart because this random parameter will be changed yeah it doesn't sound weird block choice

 **Micah** the the random that's in there is only known by the next proposer is that correct?

**Mikhail**: it's only according to the current spec yes

**Micah**:  okay 

 **Mikhail**: but there is a pr

**Danny**:  yeah not to mention a fork choice updated might even  change the proposed shuffling and so you might not even be building a block anymore at that point So i don't think you want the forward choice to automatically interrupt this work.

**Micah**:  is there a cancel build then in that Case yeah get up and get payload full choice changes you need to tell the execution engine hey stop building you're not coming up next you 

**Danny**: User can also just know to cancel if certain time stamp has Passed.

**Alexey**   well it almost it's, it seems to me that like you know one thing I first noticed when I saw this separation is that there is this assumption about some state which is inside the so associated stage is a kind of this makes it a stateful api so when you do the prepare payload it creates some kind of stay that then you later rely on you know but then now we are coming to the you know the suggestion oh maybe it should be cancelable but then   you know when you call the prepare payload you implicitly think that the identifier of the state is very apparent hash plus random so if somebody else gives the same pair of numbers then they will be referring to the same one so I think maybe it's it's better to explicitly return some kind of a state id then you can manipulate it doing cancellation or whatever you want to do because there's there's kind of a lot of implicit state here and then it might be That different  it might actually be complicating the discussion

**Micah**: i think it's technically stateless like I definitely see where you're coming from with it being a stateful because you're you're saying like you you anytime you have you know a then b sort of situation it generally looks stateful. i push back slightly just because the get payload actually contains the exact same information set and so the repair payload is more of just like a warning that you can choose to heed or not that's saying hey i'm going to be asking  for payload later with these exact parameters feel free to start working because when i ask for it later i'm going to need it right now and the the execution client can choose to not do that like it does
technically you could have an execution client that completely ignores repair payload it is not actually required for the protocol.  it's just required if you want to be able to have time to actually build useful blocks like if you're okay with not building useful blocks you don't
technically need it which is why I think  it's it feels like it's not actually stateful just because it's more just like an advanced warning system.

 **Alexey** well it is essentially you know what you said is that the the combination of parent hash random is timestamp in there it's like a kind of this id or this stuff which is

 **Micah** i wouldn't say it's an id it's more just like i'm about it's saying i'm going to in four secondish i'm going to send a request ask for a thing and that request is going to ask for these something built that it's a function of these  four items, if you didn't get that for some reason you would still get the follow-up request and you would still be expected to respond to the follow-up requesting just the same. Prepare payload are like a heads-up.

 **Alexey**:  sure but you know there's a lot of different thoughts of questions if you don't specific specify what is the id then you say okay what if I have one request which has got parent hash and timestamp but then other one has the same parent hash but the different time stamp do I need to keep the first one or replace it?

 **Micah**: I see.

**Alexey**:  i mean you know oh no of course we probably know the answers to all these basically kind of request id or something.

**Micah**:  yes so an execution client could definitely implement that by just literally just concatenating those four parameters or hashing them and that would definitely function as a request id and I can definitely appreciate an execution client choosing to implement that that way and so that way you can decide you know okay this is the one that's associated with that like internal if your internal architecture that's more amenable I think that would definitely work because you will get the exact same parameter set in the get right.

**Mikhail** i would like to read the prepare payload call as like in similar way as in the proof of work the new block has come and become the head and you need to restart the process which is constantly happening the process of building the block,   If yeah if this is turned on I don't know if it's turned on or not. if there is an option to turn it on or Not um I mean like the Geth  behavior is. So, Danny anything to discuss here?

 **Markl** i'm not sure what would cause this but what would what would cause an execution client or a consensus client not to send prepare a payload ahead of time and for where they were just suddenly forced to just call get payload and then if we're requiring that it be immediate would they just send something empty?

 **Micah** i don't think it's expected that that would happen I think it's just we need to design for in case like you just got a connection up for example and the consensus client had like as soon as your connection came up you're immediately up and so you only got to get just as a hypothetical 

**Danny**: it's kind of like how blocks are continuously mined and tried to be made better simultaneously and so very likely the logic would follow if you had to do something instantaneous that would be that like initial likely empty block with very little state transition and the hashing Completed. and yeah I agree that Given The that although prepare payload should be expected and which is the proper way to run this api that get payload should be able to be called in the event of like weird synchronization problems without the prior prepare payload.

**Micah**:  is it is it a correct assessment that there's we don't know of any like specific situations where you'd expect to receive only the gut it's just kind of hypothetical edge cases?

**Danny** Yeah

**Danny**:  i don't see any use case for that i think it's a fail a failure so you could handle the get payload failure i don't know I think you don't want to handle that failure statefully though 

**Mikhail**: right and we there are some sections in this document that covers this kind of failures yeah there is also the message ordinance section which is new which proposes much like just strict message orderingand we can discuss it later so unless somebody wants to say, i think we can move.

**Mark**:  here a second question, if the content or i the execution client fails to fails to respond to get payload in time and you have to propose a block can you just propose a block with an empty execution section like basically like a beacon block as they are now consensus client  

**Mikhail** like what does it mean fails to respond in time so it will respond later or what or not respond at all 

**Mark** if yeah supposing it doesn't respond and you have a you know you have to propose this block will the beacon client be able to propose a block with empty execution payload itself, is a fallback.

**Mikhail**: theoretically it could be implemented as a fallback and with the timeout and get payload response but yeah 

**Danny**: but the state does the state route Change?

**Mikhail**: No.  it should not as we don't have the rewards anymore 

**Micah** so i thought that the clients could do fill slots without an execution payload instead not correct or is that changing in the merge?

**Danny**:  that is not

**Micah**:  okay so there has to be something in that place and that something needs to be valid 

**Danny**: you have to still essentially be able to chain something even if that something was empty

**Mikhail**:  right

**Danny**:  and that's what and that is you need to be able to compute the hash  and a few other things.

**Micah**:  okay so it needs to be a valid block execution block header
at least ? like that's the minimum required to fill a slot

**Danny**:  yeah you could,  so I think that in general we're designing under the assumption that you can make this request happen and otherwise your client which is the unification of these two things failed you and you weren't able to produce block. you might be able to design some logic in the beacon chain client to be able to bypass this by hoisting some of the logic into there but I don't I wouldn't go down that path initially

 **Mikhail** right I agree with danny here so we have a client and is we have like a composite client and it just fails to produce a block in this case to propose a block whatever the reason is. and it should be identified i mean Yeah definitely the empty like the failed proposal will be noticed by their owner and the investigation will happen

 **Danny**: yeah validators they notice they're monitoring their monitoring infrastructure is so sensitive any time even they like get a non-optical association even when it's included they get warnings and they complain.

## Current block hash

**Mikhail** so okay anything else here  uh next thing i've added this confirm block hash stuff here with the like um temptative list of tags for jason rpc which will be extended from what we have now and there is the question by terence so and the proposal to like repurpose your list for the weak Subjectivity checkpoint which makes sense but could potentially break some apps I don't know or tooling that use get blocked by number earliest to get the genesis i don't know if this is a really really um frequent use case and important usecase yeah but we can discuss on this later I guess on Discord or on this kind of call . Okay yeah also there is like the there was the block processing flow now there is the **block proposal flow**  which covers the like block proposal stuff with yeah there is a couple of sequence diagrams that that are the example of how the block proposal flow should happen. so we may take on it and  take a look on it and get more understanding, I hope so yeah So any questions to the minimal set of methods before it moves to the transition process? Cool

##  Transition process

**Mikhail**:  um the transition process is also in the minimal methods like set but it's something new with respect To to the Rayonism which is a consensus Rpc okay so we will start from this one yeah terminal total difficulty override. i would rename this to terminal total difficulty updated because it's not only gonna use for override but for also to set the initial value of the terminal total difficulty that is computed by the consensus layer and the merge hard fork and then communicate it to the execution client. so it maps on the terminal difficulty property from the eip and yeah it could be reused further to override the terminal total difficulty with the new value in case if we want to accelerate the merge and there is the corresponding pull request to the consensus fx repository that adds this possibility and yeah the like scenario will be
 the following the consensus client gets restarted with the terminal total difficulty override Parameter which will and this is how the overridden value will be passed to the consensus client and then consensus client upon a startup and connection to the execution client will communicate this overridden value and the execution client must update this value and act accordingly according to the Eip specification.

**Danny**:  yeah we should probably state and i  think this is probably implied in how
this event will be handled in 3675 but probably say that it's a you know it's a no op or it can be ignored if the  transition has is in process or completed. maybe scope transition implies that

**Mikhail** yeah um okay see  actually yeah we should also add the corresponding event to the eip like which says that that the terminal difficulty should be updated upon receiving this event and with this event will the new value will come. okay so there is yeah let's go through like these two and then stop for questions. **terminal before block override** is the
and another way to accelerate the merge so in this case it it overrides also the total difficulty transition based on total difficulty and directly specifies the  exact terminal proof of work block
and it means that the proposer will need to be start building the proof of stake chains to to build the transition block on top of this exact proof-of-work block. it also implies that that execution client for example should must stop processing blocks after this one, it must disable the block gossip upon receiving this message and some other stuff which is  which is not yet clearly specified by the eip but it will be um specified like but once we once we get to this functionality. so it will be updated in the eip.

**Danny**:  so first this is also really just the first method is part of that minimal set like to get you know implementations going right?  you mentioned minimal set do you mean minimal set like minimal set to be a functional client or a minimal set to on like the next wave of
Uh devnets?

**Mikhail** no no it's like minimal required set for for the other function client so this transition stop is critical yeah okay so yeah there will be a corresponding um parameter in the consensus clients that Will set this value and communicate it and then because this client communicates it to the execution client likewise with the total difficult stuff.

**Mark**: would there be any advantage to using a block height instead of a block hash because you know you only know the block hash right as It's as it's been made the 

**Mikhail**: when it is certain block because in case of like attacks there might be multiple blocks at the same height and we need to specify the exact block that writes the chain over.

**Danny**:  this is an emergency like coordination in which you're picking a hash in the past that you're coordinating on and you're probably taking some chain down time  to do so

**Mark**: gotcha and and the terminal total difficulty is under unless under like attack scenarios is Superior and we also you don't do the block height you do terminal total difficulty
because somebody could have like a cheap shadow chain  that could  reach a block height much faster than main net and try to take over the merge so terminal difficulties chosen when
you're taking something in the future 

**Mikhail**: yeah 

**Micah**:  two questions-  one is it expected that the execution clients will have a default terminal difficulty baked in and they'll only receive that message if there needs to change or will they always can they depend on always receiving at least one of those messages at some point before it happens?

**MIkhail**:  they will receive it. it's not possible to to know it in advance. so it will not be hard coded.  i mean it's impossible but we we yeah we decided to the decision was made to use the computed value so it will be okay.

**Micah**: so the execution client will always receive at least one of those messages is that accurate the internal total difficulty override?

**Mikhail**:  right 

**Alexey**: you mean you mean receive it during one session so at the end of the beginning
of every session it just gets one of those things right that's the assumption?

**Mikhail**: that's a good question like session of communication right yes so because then it doesn't make an assumption about whether they stored in a database or they forgot about it or whatever 

**Mikhail**: right right right so yeah it will be computed once but it should be communicated every session as you've said

**Alexey**:  yes I think it could be written in the spec that the consensus client needs to send those at the beginning of every session to make sure that they in sync

**Mikhail**:  right here is the message here is the call that communicates like this kind of stuff total difficulty for a block cache so and we will reach this place in the dark okay at some point

**Micah**:  so you may actually receive that status message but not the override would that
be accurate

**Mikhail**:  right if it's been like um yeah yep exactly so the the the override will happen only once when it is overwritten or it is set initially 

**Micah**: so second second question the for execution clients is it easier for any of you to have the block number included in addition to the hash for that   terminal proof of work block override like when it comes to finding some old block um is the hash always enough you never need a block height like there's no database architectures that make are easier to find the block with a height?

**Mikhail**: my intuition is that it is straightforward to requested by block hash either from the network record from the storage log hash should be fine so assuming we just

**Lukasz**:  block hashes in the database 

**Micah**: yeah that's as I wasn't sure if everybody's database has a index by block cache or some of them maybe just actually have like a linked list for example.

**Tomasz**:  no it's index but block hash, we have also separate indexing by number but it's not from ​​number to block but from number to a list of blocks if you have multiple Siblings but by harsh you can find both the main branch and the non-canonical and non-conical branches so by hash is the fastest way of accessing the blocks 

**Marius**: same for us

**Mikhail**: so any other questions here?

**Mark**: if the session starts with um communicating the terminal difficulty um what like then the purpose of these two calls is if you is so you don't have to restart a session  if there's an emergency um 

**Mikhail**: yeah actually you will have to restart the session if it's yeah the client will restart it so 

**Mark**: so what what is the purpose of these two calls then like how would it be different 

**Mikhail**: Right 

**Micah**: one can imagine a consensus client where you could override the terminal total difficulty or the internal proof of work block via an api without a restart yeah I don't know if any of the consensus clients will do that but like from a design standpoint I can see that as being very reasonable like in theory anyway

**Mark**:  it's the consensus client that sends one of these two terminal messages and right they also start the session with information about the terminal

**Micah**:   i see so the both of them can change at runtime and one of the total difficulty isn't
actually known at startup. like today for example we don't know terminal difficulty there will be a point in the future where we will learn what that is and it was some time after the merge is
scheduled and so ideally we wouldn't W nt to have to restart everything just to propagate that new information 

**Mikhail**: right this could be sent during the session and these two will be sent
could be sent at the beginning of the session that'd be sufficient 

**Matt*: okay 

**Mikhail**: but this one should be supported but this could be supplanted by status message if we will eventually agree on adding the status one.

okay so moving on to get before block. okay this is actually this has um it pulls the same set of data that the get blocked by hash. the only difference here and this is important is that the execution client should request this block that requested by this hash from the wire if for some reason it hasn't been received from gossip and yeah we might not want to implement this um method and instead use the get block by hash but imagine the case when  the whole the the node stuck at the transition because  it hasn't received the terminal proof of work block why I gossip. I am wondering how likely this could happen and yeah if if it happens only a manual restart can help to recover from this case from this situation so it would be great if we have this one but i'm open to any opinions on that.

**Danny**: So what exactly is happening with when when would this be called?

**Mikhail**:  it will be called when the transition block is received the transition block is the first proof of stake block in this system and this method will be used to pull the parent of this block and the parent of its parent to verify that this is the valid terminal for a block and yeah this code is  running in the fork choice of the consensus client to accept the block

**Danny**:  when you call, okay so it's it's I have a proof-of-stake block and i'm concerned whether it actually was built on the terminal total difficulty block like on a valid terminal block and I use this on?

**Mikhail**:  yeah you may use this but it doesn't has this property of  making the execution client to pull the block from the wire if it's missed in the local storage 

**Micah**: so this is basically saying because this client is saying there exists a proof of work block out there that we are very confident exists if you don't have it go figure it ut like do whatever you need to do to  get this block um whereas get get blocked by hash normally it's like hey here's the hash let me know if you have this block and we want to be more authoritative here because this is the point where the proof state client is or the class client is taking over right and so they're saying you will you must have this block for me to continue working  is that accurate?

**Mikhail**:  right, right 

**Danny**: but otherwise we're getting stuck here and they imply that when they run execute payload on the transition block too  because the payload has the parent hash and this parent hash and you should go find it otherwise so i i'm not, i think i'm not understanding what exactly this method is used for?

**mikhail**:  you're not executing payload during the fork choice right so you're checking that this is the right um this is the right proof of stake block like the right transition block um so with respect to the transition process not with respect to the like execution yet so it will be executed later but at this point you just want to understand before falling into the state transition function 

**Danny**: what is pow block does that include terminal difficulty in it or something 

**Mikhail**: yeah let me open it here so here it is yeah it has all the required information here is what's going to help me and here is the code right so it's before the state transition and it's important to be before. and if if we get stuck here so we are not doing the state transition and that's it 

**Danny**: so essentially where another client wants to know that this is actually a valid   terminal proof of work block the when it sees the initial transition process and the exist the other methods don't really help us ascertain that and so there's an exceptional call here on this transition to make sure that somebody didn't create like a bad uh transition block just just because it might be a valid transition it might not have picked the right parent block or a valid parent block okay Um i suppose that payload can can do that though for you because execute payload knows the terminal total difficulty and could tell you if you built off of something invalid but it might be good to just be explicit here.

**Mikhail**:  the execute payload actually doesn't know about all difficulty but we can
check it inside of the stage position that is what you mean?

**Danny**:  i'm saying the execution client knows about terminal solid difficulty and so if you did execute payload and it was the first and executive 

**Mikhail**: oh yeah it's being built off of a workblock it could know if that was not oh yeah you you mean we can you  we can defer this check to the execution client yes


**Danny**: Right yeah i'm not convinced that that's correct I just am now understood yes yes why this block why this exists okay okay I want to  think about it a bit more I don't think i have much more to say on that 

**Mikhail**: yeah we have already some implemented we can use this one but as it's been said it doesn't go to the wire if the block is missed um uh the question to the execution final
mirrors how often the do you know how often how likely the gossip to be  to not deliver you a block or its hash um how often do you do do you do your like clients have to go to the wire to pull the parent of some block that you have received but for some reason you've missed the parent block.  yeah I agree with micah butm 

**Lukasz**: so this is fairly unlikely but it happens especially on like some network blips etc

**Mikhail**:  so yeah if you say that we are pretty confident that that this method will work um well so we will just remove this from the design space and forget it 

**Alexey**: well it might not work but we we're kind of thinking that the the the probability of this occurring everywhere it's very small like it might occur in one or two nodes or something so it means that if yeah there will be a very little portion of nodes that might get stuck right if we even have these kind of nodes 

**Danny**: so yeah if you if you follow the like execute payload path I think the input implication is that execution execute payload if it couldn't if it didn't know the parent would go find it with the network so it might be better to just run that path. 

**Mikhail**: then we will have to get to this check after execute payload right after the state transition and the execute payload will actually has an additional semantics for the transition period um it will need to go to the wire and pull the block if it's it and pull the parent block if it's not in the local storage.

**Micah**: I already it already has to do that though right in order to validate the current block you need to know what the parent block was you need to have seen the private.

**Mikhail**: right but currently a consensus client guarantees that that all previous blocks has been sent to the execution layer.

**Danny**:  that that i think actually when you start talking about failure modes and synchronization issues between these two pieces of software that like the  what we've previously discussed is say uh say the execution engine fails it gets restarted and it's 10 blocks behind and and the beacon chain client inserts a block that the execution client can then say no I don't have the parent or it could actually just go to the network and get all the you know recursively look up those ten blocks and handle itself.  so it's not out of the
question that yes your slide actually does do some self-mending when it doesn't have a parent.

**Mikhail**: Yeah that might work but if in this case execution client falls into the state sync to pull the state and the apple headers it might take some time which is but we are the transition process like it's time critical. pulling the block from the wire may also take some time but probably it is like yeah but probably it will have to pull uh like one block and its parent and so forth um yeah

**Micah** I n all happy paths it should already have the parent block I think the primary unhappy path is when someone act actively is attacking the transition and they have mined a the first consensus block on invalid terminal total difficulty proof of work block that's the time where you would maybe get a request to hey um execute this block the client doesn't have it because it's not a valid block and it never accepted such a thing.

**Mikhail**: okay um so we are like roughly agreed that it would be better to rely on get locked
by hash right and on the blog gossip so let's just I think i'm with danny i prefer relying on just executing the block later but this might be a good conversation to move or discord since run out of time.

**Mikhail**:  right right right um okay the next one is sync.

## sync
**Mikhail**:  there was a well like great work done by alex and get team on the merchant proposal i've outlined like this this thing status was in this document before but there is this sync checkpoint set which is required by which is yeah is is one of the required methods here to send the  to make the execution client aware of what is the block header at the big subjectivity checkpoint and consensus client knows that what's the header is because it pulls the state at the quick subjectivity checkpoint and can directly send it to the  execution client this is also the first step of the of thing process so it's like initiating the sync process. and also might be i might be a clear evidence that the execution client should switch to the proof of stake mode. so i yeah a bit of context on that,  we will have the execution client software after the merge yeah after the merge happened and before any execution client software updates  the execution clients will start  in the proof of work mode by default as they don't know that transition has already happened and yeah they will go to the network to look for the block and the peers with the   the greatest total difficulty value and so forth and listen to the gossip and other stuff  and yeah we'd like the consensus client to inform the execution client if the transition transition has already happened and this is how it could be done so once this checkpoint said message sent um aside from the initiating the sync process um the execution client may switch to the proof of stake mode and listen to the consensus clients instead of listening to the blog gossip and doing something.

**Dankrad**: does this have to be sent every time the execution client is started?

**Mikhail**:  i guess no it's it should be sent only  on the fresh client startup when there is no box or state in the local storage. so if there is already some state it should not be sent this checkpoint said actually it depends if if you're behind the wick subjectivity checkpoint then it
should be sent again.

**Dankrad**:  I guess no because you just said that it automatically it starts in the proof of work mode and that sounds.

**Mikhail**:  okay it starts in the proof proof-of-work mode because it's the fresh client and it doesn't know about the transition has happened on the network.

**Dankrad**:  wait but we are gonna put the the transition difficulty like into the hardt fork proof of work as well right? no. I mean i want to avoid the situation like imagine posts posts   like
post merge someone ex someone's ex sorry someone's consensus client accidentally crashes right  the execution client restarts and now they are in proof of work mode but they don't know it and their adapts will automatically use some proof of work chain that's like uh not really the ethereum chain that sounds dangerous.

**Mikhail**: right but yes but if they start after yeah this like switch I think it should be persisted by the execution client inside storage. so it will just start up in the previous state mode if it's been informed about it previously even after restarts.

**Micah**:  and and also the proof of work client should if it ever received and saved the terminal difficulty it should refuse to ever accept any blocks beyond that right?

**Mikhail**:  right, 

**Dankrad**: yeah exactly and also shouldn't we put the default value for that just in the client as an in the source code so that it doesn't have to like what if someone just keeps running a proof worklight without starting up their beacon client at all then once again they could end up in a situation where they keep following the proof of work chain. yeah so I think the default behavior should be to stop like all proof of work clients should ideally just stop working if they aren't connected to um a consensus client. all other behaviors are gonna be extremely dangerous.

**Micah**: i thought we didn't know the terminal difficulty until like a week before then merge or something? did that change I haven't followed that closely.

**Micah**: yes so it will be communicated like and it'll be communicated but we can't hardcode it because it right?
**Mikhail**:  right we won't know it until after everybody's deployed their clients

**Dankrad**:  Right,  why can't we just like do it but like with other hard forks where we all agree on one block height we keep they I mean i thought the end points to set it are for emergency like if you say like oh we need to change it but like.

**Mikhail**: yeah i'd stop here and let's continue um with this discussion on the Discord
because we have one minute to the next call okay thanks everyone um we'll see you soon again bye bye thank you bye thank you! 

### Attendees

* Mikhail


* MIcah

* Danny

* Mark

* Zahary karadjov

* Alexey akhunov

* Lukasz rozmej

* Jared doro

* Gabriel rocheleau

* Dustin brody

* Protolambda

* Dankrad feist

* Alex stokes

* Josef

* Lightclient

* Lakshman Sankar

* Sasawebup

* Trenton van epps

* Tomasz stanczak

* Adrian sutton

* Mamy

* Terence

* Marius

### Next meeting
(Unannounced)
