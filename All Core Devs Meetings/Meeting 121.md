# Ethereum Core Devs Meeting #121 Notes
### Meeting Date/Time: 
### Meeting Duration: 90 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/379)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=XxozI0Wpr7I)
### Moderator: Tim Beiko
### Notes: Jared Doro
-----------------------------
# **Summary:**
* Discussed Consensus API improvements 
* Merge Call before Eth-2.0 call next week for one hour
* Discussed post merge syncing and reorg processing 
* Discussed EIP-3756 A global gas cap
* Discussed moving two previous EIPs for Eth 64, and Eth 65 to final status because they are in use and needed for Eth 66
* call for wallet and infrastructure support for 1559 at Friday 09/10 14:00 UTC
* Update for application developers to latest version of Web3.js to ensure you are using 1559 transactions to save your users money!!
-----------------------------
# Merge Updates
  
**Tim** 

hello everyone welcome to All Core devs number 121. I have a couple things to discuss today most of them are related to the merge two big things there so Mikhail put 
together a document a week or two ago about the consensus api for the beacon chain and the execution layer they communicate after the merge we discussed this in a merge call  
and then brand way out of time so we can kind of continue that discussion here and then a bit later in the call Felix from the geth team put together a spec for basically what a post merge 
sync algorithm could look like so that's the other big thing we'll need to 
discuss there and then a bunch of other other topics but yeah Mikhail do you want to start maybe just like give a 
quick like one or two minutes you know context about the document and then we can kind of resume where we left off last time 

**Mikhail**

okay thanks tim thanks for allocating the time for this discussion during the suv yeah a bit of the context we've been obviously there will be like two counter parties in the like client software 
after the merge which are the consensus client part and the execution client part and we need the communication protocol between them in order to communicate with blocks 
and other stuff and we have something already which been designed for the ___ hackathon project and it's been based on the json rpc but we might want to 
extend this protocol add some other stuff and other restrictions to the underlying communication protocol so there is a doc dropping it to the [chat](https://hackmd.io/@n0ble/consensus_api_design_space) that just the 
shapes and outlines the design space for these engine api so it is at the or in the link there is a consensus api so I just haven't changed the link but we 
do this renaming from consensus api to the engine api and yeah we started to discuss these documents and stopped like not far from the beginning 
so I'm going to share my screen to continue the discussion from the from the point we have stopped at and also I've made some adjustments to 
this document and updated it with the the result of discussion we previously had so I'm sharing my screen 

**Tim** 

you are not no no you're not sure okay yes go ahead yeah 

**Mikhail** 

yes I'm sorry is it the right place okay 

**Tim** 

anyway this is perfect well it's on the agenda yep 

**Mikhail** 

yeah I'm sorry yeah this is the agenda oh okay okay yeah this one is is the document right yeah okay cool so I would encourage us not to fall into deep discussions right now 
and if any item that we are discussing requires like to have like a more deep conversation on it let's continue let's just mark it as 
the like requires some pretty discussions and continue offline on discord or make like other kind of call so not to spend much time on every on 
everything yep so let me turn on the chat and persistence okay yeah so I was starting from from the above we'll go through the comments a bit 
here is the comment from Jacek that we should consider rest for this kind of api I would I'm a bit unsure about the rest and I think that it will not suit as well for 
this api but we are still in the designing stage so the things might have might be changed a couple of things that well that rest might not work well 
with is the bi-directionality of the protocol there is a couple of use cases that might need this protocol to be bi-directional which means the execution client may initiate 
some message run trip the other thing is that rest is related like is about the resources which are some entities so I'm not sure if this 
fits our this protocol as well so but yeah Jacek if you if you hear us just if you want to discuss this let's discuss it on this course more 

**Danny** 

oh real quick there are usually the counter to that is server side events which can facilitate that
with restful http but I'm not I'm just putting that out there I don't really want to discuss it 

**Mikhail** 

yeah yeah sure okay so on the previous call we have decided to like to replace the assemble payload with a couple of related methods 
they are here now so there is the prepare payload which gives a comment to the execution client to stop building the the payload it has these parameters here and it will keep it up to date until the get payload is called and this and this process of producing the payload stops then 
and the pay and the most updated and the most up-to-date payload is returned back to the consensus client and then it will it can take and embed into the beacon block and fire this block into the network yeah 
there is a note that if the prepared payload is called if they are now if they prepare payload with another set of arguments of parameters is called after the first one then the process of building should 
be restarted with this new parameter set which makes sense as we can like as the consensus client may receive a new block and it may become the head of the chain and it might want to restart this process because it will 
build on the other block it will build its block on the other one get payload have the same set of parameters here it could be argued that it should not be so but the reason why they are here is the 
first of all it can be used without the prepared payload this way so it can work as the assemble payload I don't know if there are any use cases for this or this like property but the other stuff which 
I think more important is the additional consistency check because the this like new block may be received by the consensus client and the prepared payload might be sent before 
they get payload with the same parameters all processed like yeah there could be a kind of racing between these two messages this is a very cool edge case very much an edge case but 
it could potentially be the case so this is why here is the set of parameters as well and if the if it's not it does not match to the to what was sent with ______ the block should be 
either adjusted if it's even possible or created a new one with this set of parameters and returned back to the consensus client and this is to avoid the weird case when 
the consensus client proposes a block with a payload that does not relate to this block what do you think about this like additional consistency check 

**Danny** 

I think that makes sense I think it also leaves optionality for a client to not support prepare payload and just do 
on-demand gets which you know probably is not an optimal strategy but is probably a reasonable thing to leave in there so to have the full information make sense to me 

**Mikhail** 

okay any other opinions in that 

**Artem?** 

what would if for example there would be change in the parameters what is the
expected time that the get payload would return this new unexpected previous block 

**Mikhail** 

this is a good question so the default behavior might be just yet all the transactions from the member it will require some time to execute them and build a block as as usual in the usual way and return it back as fast as possible 

**Danny** 

yeah I mean that might end up being a little bit of implementation specific on how to handle that strategy I don't know if it needs to make it into the actual protocol definition 

**Micah** 

I do worry a little bit about it 

**Danny** 

and say nope sorry I can't do that 

**Micah** 

I do feel like there needs to be some kind of expectations set even if they're not like part of the protocol just in general because if you say get payload without a prepare the node starts building a block and they can stop adding transactions at any time and so if there's a bunch of transactions transaction mempools that are for example attack transactions that are consuming a lot of time the  
execution engine could at some point have a timeout and say okay stop trying to build a new stop trying to add transactions cut it off here send the block because run out of time if you don't have any kind of sense of how long is acceptable then presumably the execution client is going to just do whatever it normally does to get a block which maybe means hitting a remote server maybe it means just building until the block is full and these things can take you know seconds 

**Danny** 

what is being able to return much quickly which is empty 

**Mikhail**  

yeah and what my case is also related to the preparatory law so it should be related if we are adding this kind of protection to the protocol 

**Micah**  

right like with the prepared payload at least you've got like this idea that if I get a prepared payload and I start preparing and then I get a get I stop whatever I'm doing and I give them the best I've got like as soon as possible instantly if that means all I've got is an empty block then I can send that right away whereas if all you get is the get payload then either you default to setting only the empty block because you have no time to prepare anything or you decide that I'm going to spend some amount of time actually build acquiring a block and there needs to be like you know some limit on that presumably like you don't want two minutes for example that's obviously wrong it's 10 seconds too long is five seconds two seconds 

**Mikhail**  

yeah as I understood you were like saying about malicious transactions in  mempool that could take a lot of time to execute and in this case we might want to add the this time restriction to the prepare payload as well because prepare payload has much more time in advance right and it could include all those transactions without any problem this is what I was mentioning 

**Danny**  

Micah are you suggesting that there should be a a note about a an expected return time and that's not necessary 

**Micah**  

I don't even know if it needs to make into the spec I just think that we should give execution client devs enough information to like maybe they did they differ a little bit but like presumably the consensus clients will have a timeout on their end yeah and we should execution 

**Danny**  

in that sense I think you could put note this is expected to return you know a viable block within 500 milliseconds or something maximum but that is that ends up being like yeah which is reasonable which is it doesn't happen 

**Micah**  

yeah and i think that would be I'd be totally fine with that if it was in this again I'm totally fine if it's also just like something that we just generally share amongst each other I just want to make sure it doesn't get left out and forgotten is all 

**Mikhail**  

yeah I do see value in doing this but if we want to discuss more on that let's continue on the discord what do you think 

**Micah** 

yeah I'm always happy with this 

**Mikhail**  

okay so so let's move on yeah and execute payload so it verifies the payload according to the execution environment rule set which is exposed in  
the EIP here is the question from Martin what if the parent block state is missing some error type will that be defined this document like has  
a section of the consistency checks of the consistency checkpoints which answers this question so once we get there we can discuss it the  
basic but the basic idea is that if you execute payload send something that can't be processed because can be processed by the execution client  
because of absence because some information is absent so the execution client responds with the corresponding message that something is wrong  
and yeah the consensus and the execution client starts the recovery process this is one of the option options or the execution client goes to  
the network goes to the wire and pulls of all this data this is the default at danny 

**Danny**  

oh I was going to say and this is getting ahead of ourselves but I think in a sync protocol it is going to make sense for the beacon chain to  
be optimistically processing forward without execution validation and I think that likely it's most simple to handle most of the most  
optionality of the sync protocol underneath for it to continue to run execute payload and just continue to send the messages to the the  
execution layer and in that sense i think there might be value in having an enum that's like valid and valid known and maybe sinking or  
processing such that it knows that it hasn't been fully validated but it kind of continues on optimistically but that I don't think we can make  
that decision without talking about a lot more sync so we can leave that 

**Mikhail**  

right this doc this like doc has a suggestion on the like sync status return instead so yeah it's it's optional so it it it also covered  
here but it depends on the sink entirely so yeah the consensus validated message which is mapped on the proof state consensus  
validate if you end from the EIP it's easy it's sent to the execution client by the consensus client when the when the beacon block gets  
validated with respect to the beacon chain execution or like the API says with respect to the consensus rule set so this is required  
before the block can be persisted by the execution client even if they execute payload returns even if the payload is valid with respect to the execution environment rule set yeah here is 

**Danny**  

we're processing a block and who hadn't checked the proof of work but you would have done all the processing of the block otherwise and then someone said hey the work style as well 

**Mikhail**  

right right yeah thanks Danny for this so here is the block processing flow you can check how these messages could be sent like there are two  
options so the consensus validated may be sent like while the payload is being processed or after that so this opens up like yeah the  
alternative would be to send execute payload after the beacon block has been imported which will cause a delay required to process the beacon  
block and like except keeping these two messages separate opens up the ability to parallelize the beacon block and the execution block  
processing which is nice next one is the any questions here any questions so far 

**Danny**  

if a consensus validated message is sent without an execution payload or sorry execute payload being run would that then run the execute payload or not 

**Mikhail** 

you mean that if it's sent before the correspondence 

**Danny**  

bypasses execute payload and just runs consensus validated with that just trigger xc payload plus consensus validate and return it 

**Mikhail**   

if you had yeah if if it's this  message is received but the payload is  unknown is this the case you are  asking for 

**Danny**  

yeah yeah the execute payload has not since validated his call on that that be a trigger to kind of like run all the processing and we can just note that as like a weird edge case to think about 

**Mikhail**  

right right but it could be cached like for a short time like consensually it's stuff in the memory and wait for it payload yeah this there is a like a cash section like here is execution fill out cash it touched this question a bit a little bit so the audio is that 

**Danny**  

so you could say invalid you could cache it or you could say hey this thing's telling me it's been validated I should process I should process it but I guess 

**Mikhail**  

yeah yeah if it's invalid then you yeah get back so there are we can check this one now okay yeah checking the chat okay cool engine fork  
choice updated there is the PR to the to the EIP I'll drop it into the chat that unifies the two previous events which was the chain  
headset and the block finalized into the one so this document is matched the follows the EIP currently or vice versa anyway here is the  
suggestion from the previous call and comment from Micah confer I've called it confirmed block hash which means that this block is confirmed by  
two thirds of the testers in the network they have been they have voted for it this is for JSON RPC for users JSON RPC actually  
here is like a bunch of stuff so this yeah there is a head block hash and finalize block hash which must be and the confirm block hash all this  
information must be updated all the changes related to these method call must be applied atomically to the block store so though in order to  
avoid where cases when the head block even four microseconds points to the do another fork then the finalized block hash and the confirmable hash  
as well so there is one out of this unification there is one note here this is more for consensus client developers in the EIP this event  
should the finalized block hash before the transition before the first finalized block hash it should be stopped with all zeros so this event  
will be we'll set we'll be sending the actual hat block hash but the finalized block hash will will be stopped with all zeros before we get the  
first finalized block hash actually in the system but there is nothing like no additional work required to do this kind of stuff because after the  
merge fork we have we will have the execution payload in the block which filled with all zeroes so the finalized block hash we will have  
this block hash already stopped serious I'm sorry I I could be a bit messy but you can read this and yeah it should be enough to to  
understand what I've just talked about yeah this was my first try on the introducing the confirm block hash stop so it's just stand for each  
each block the study status invalid and concurrent confirmed which is  

**Micah**
 
I was wondering why is so the engine consensus elevated versus engine fork choice updated what information do you get like why are those two separate like it feels it I'm guessing I'm just missing something but it feels like they're saying the same information 

**Mikhail** 

you can get blocked now actually sort of thing 

**Danny**  

oh just the consensus validated means like I checked the proposer signature I checked the attestations and the other like kind of outer  
consensus components of something I previously had you execute and check on the execution layer and that you can put it into your block tree  
updating the fork choice has is independent of the fact that a block was valid to insert your block tree and a block that I insert into your  
block tree may or may not ever be the head or in the canonical chain 

**Micah**  
it will happen before the block makes it into the head head block in the normal case 

**Danny**  

yes yes it's kind of like I'm just outer consensus stuff the execution layer can't validate and it's the confirmation that all that stuff was also valid 

**Micah**  

okay so the execute first consensus client will say hey here's a block please execute it the engine the execution engine executes it replies back  
this is good since this client then does some additional checks and then says hey my extra checks are also good and then some point later it'll  
say hey this is now the head block and then eventually this is the confirm block and eventually this is a finalized block like that's the normal 
path of a block through the process 

**Danny**  

a lot of that can happen in parallel so like checking attestations and things like that and then the final thing it's going to do is actually do the beacon state route which includes executions here and stuff and then passes it back one so okay 

**??**  
if consensus validated no returns that the consensus what was not valid then we can just throw away the data that throw a block 

**Mikhail**
  
right right you must yeah you must  discard this block 

**??** 

hey guys I just I was just quickly wondering like why is the fork choice like why so much like why is the fork choice stuff communicated to the execution layer in so much detail I mean I haven't really looked at this api you know ever and like seeing it now it's just feels kind of weird that you know like the execution layer should know like all of these details about the fork choice 

**Vitalik** 

like the idea for example is that the the execution clients knowing the finalized forces is really useful because the execution client has like different tricks for storing state that basically optimize for making it like really easy to update but at the cost of making it hard to revert and if you know what the final is hey but that like 

**Micah**
 
you're super quiet like I can tell you're talking but I can't hear a single word you're saying oh okay hold on sorry 

**Vitalik**  

about that and why ios super quiet now okay yeah basically I was just saying that for the finalized block hash in particular the issue is  
that like the actual execution clients have a lot of optimizations where they yeah basically trade off an increased efficiency of reading and  
writing to this to the state as it is now in exchange for making it harder to like go backwards and revert and revert to previous states  
and then so if you give the execution clients a finalized hashing so that it knows that it's not never ever going to have to revert past that  
point then the execution client can use that information to like basically like dump all the information like jump to the journal and like flash memory and do all sorts of things that makes more efficient 

**??**  

so I understand this part but what i don't I mean I it's obviously it's kind of important to know if the block is finalized or not but it I don't really get why for example it should know that the block is confirmed because this information seems like 

**Vitalik**  

yeah partial and partial finalization information is still useful like it's it's a trade-off space right so 

**??**  

about the api the problem is if you only have the latest block that is a very unreliable information and it might be even less like confirmed than currently on proof of work so we want most applications to follow a slightly less aggressive head basically that's why they confirmed this in there 

**Danny** 

so to be clear yeah you you want the head and you want finality and you want to update that information atomically so those are really required and then this notion of confirmed or safe is a definition which might help serving like web3 apis on on head and 

**Mikhail**  

here is the list the just proposed list of the new statuses for the block for the json rpc a new identifier sends json rpc for the block so it could be finalized it could be safe which means it's confirmed could then save which is unconfirmed and extend by say it's extended with finalized and safe and safe and safe will be an alias to latest according to this proposal so latest will be will always point to the confirm block and this is aligned with what we have currently in the fork chain because latest always like points to the to a block that is accepted by that that could be accepted by the network in terms of the proof of work verification and in terms of like consensus all consensus verifications so this this is like the same as in the proof of stake with the like confirmed blocks with the thirds of testers voted for a block 

**Tim** 

I can give you the head but it's good to atomically update a couple of other pieces of information with that 

**??**  

yeah okay I understand so basically the the plan is to treat this you know like confirmed block as the like head block like the way we treat the head block now and then you know there may be additional blocks after that but they are not like to be used really like I mean you can use but it's not not recommended 

**Mikhail** 

right for the depending on your use case 

**Micah**  

yeah yeah for your average for your average user latest meaning safe is kind of a very reasonable default behavior if you're using the app or whatever however if you're doing something like mev extraction or bot work or whatever then you probably almost certainly want safe but you also know what you're doing and you recognize that you're taking risks and you're building on you intentionally want to build very specifically on the absolute latest block and that's why we return both because both have different use cases 
**Mikhail**  

I'll remove this suggestion but I will move this kind of stuff to to this method just to give more context for the current block hash why isn't it any other questions on the fork choice update 

**Micah**  

just on the sorry I'm going back to that's validated again so it says block should be discarded is there absolutely no situation where the execution portion of that block may come up again like so for example could the next slot contain the same execution block 

**Mikhail** 

and no no because we have this run down for stuff we're going to have this house 

**Micah** 

does the render change if there's an empty slot 

**Mikhail** 

oh yeah yeah no no it depends on which render we use before the current slot and it makes like yeah I guess there's still the timestamp okay so yeah so there's no way for that right change yep okay yeah we have a downstep here actually which matters okay should we remove one 

**Tim**  

yeah and just as a heads up we can probably do like another five or so minutes on this side that we finish everything in the next five minutes yeah just to move on to the Felix document as well after 

**Mikhail**  

okay cool so block processing flow is here to illustrate yeah this couple of sequence diagrams it just illustrates how the er block will be processed I should probably add the focus stuff here the whole choice updated stuff here clarity I'll do that now we are going through the transition process and which this is a very critical part of this api and yeah all the transition stuff and all the stuff that is marked as scope transition including some parameters of some methods will be deprecated after the merge and could be removed from the clients in the next like updates when the merge has already happened so we have here like a couple of yeah we have here the couple of things that will help for the case when we would like to override the terminal total difficulty or set the terminal of work block which overrides the terminal total difficulty overwrites yeah so these two methods yes sorry  

**Danny**
 
I believe terminal prefer block override would need an epoch as well in which the effect goes in otherwise everyone would fork a different epochs do the merger 

**Mikhail**
 
the the epoch matters for the consensus client right but what matters for the execution client is the the block hash  

**Danny**  

right because it's just going to be waiting for that block hash and then got it got it 

**Mikhail**  

right and we should have the respective parameters on the consensus client side because the consensus client rules manage this transition stuff so if if there is like a kind of emergency and any of these parameters are communicated to like some channel on some public channel the clients should restart you should be restarted with either of this one and yeah they will be communicated down to the execution clients when they are set from on their consensus client side more on the reasoning behind this there is an issue here yep also by the way I forgot to mention that that this terminal total difficulty override will also be used for setting the terminal total difficulty in the normal case so once the merge work happens this terminal total difficulty gets computed by the consensus client and communicates it's why this method to the execution client so it will know at which total difficulty it must stop processing the proof-of-work box this is all specified in the EIP this behavior yeah I feel like we yeah we should we should stop here and if we have any time to answer the questions like we could do this 

**Tim**  

yeah and I guess one thing that might be worth discussing on the discord after is if we want another merge call next week to maybe finish this you know going through this like before the eth2 call right yeah we don't need to agree to this now but yeah I think it's just worth seeing it's definitely something we can do so yeah okay just thank you oh sorry danny go ahead 

**Danny** 

I'll say a call before the Eth2 call next week is totally fine 

**Tim** 

cool I guess yeah maybe we can just figure that out now does anyone here feel like that would not be valuable 

**Danny**  

we might have some juicy sync api things to discuss after our people sit on sync for a week too so 

**Tim**  

right right so okay let's do that let's do a call before before the eth2 call next week for an hour cool yeah thanks a lot mikhail for sharing this and yeah let's let's keep the conversation on on discord in the next week and yeah felix do you want to give us a quick rundown for your document around the the post merge thing 

**Felix** 

yeah I can I can do this I was actually kind of hoping to be able to like share the document in the screen but for some reason I can't seem to do this in here I don't know 

**Tim**  

okay I I I should be able to share it give me a sec yeah so 

**Felix**  

I'm really sorry about this but for some reason it's not it doesn't always work anyway yeah but I while you dig it up I can also just  
start talking so how we probably gonna do this is like basically I can just talk for a couple of minutes about the general idea behind this like  
sync stuff and like where we're coming from with this and then after this we can kind of discuss so I'll just tell you when you know you need to  
scroll sorry for this indirection but it's I think it's going to be the easiest so so basically yeah and Pooja also linked the [document](https://github.com/fjl/p2p-drafts/blob/master/merge-sync/merge-sync.md) so it's  
there yeah so maybe stop here so we can quickly talk a little bit about the background of this so a couple weeks ago we had our team meeting and  
in the team meeting we i asked peter a little bit about like his ideas for the Sync because he had been kind of busy thinking about it and  
trying out some stuff how it could be implemented and so on and then yeah he told me about his ideas and we made like some some some drawings  
and kind of yeah just like basically tried to get the like good picture of it and then peter basically went to on vacation and now basically  
I'm I'm right now the guy who's you know like basically carrying a torch forward and I suspect that he will come like when he's back he will  
likely take over and keep working on this so this document that I just released yesterday is basically only really concerned with the sync  
so this is kind of important because when i asked some people for review they you know immediately jumped out and were you know like yeah  
discussing like the api that is used in this document and you know like if it matches the the real api or that that is gonna be used between the  
clients and stuff and it's not about this api it's really only about like you know very specific part of the sync which is exactly the sync that  
isn't processing non-finalized blocks so basically the main interest here is about the part where the client is you know trying to sync up  
finalized blocks and then for the beacon chain it's like you know it for it to you know like basically for the clients to be fully in sync with  
the network obviously there it has to get to the real head of the chain and this in the end of the sync some it will you know basically just perform the same operation that it would always perform if it's already synced which is just you know like processing basically you know like 
very recent blocks so it's not about this part and it's also not really about like handling reorgs and things like that during this like later normal operation but this is really only about this like earlier part where it doesn't have the full chain yet and it's you
know like just trying to basically get to a state where it can start processing blocks so this is the main importance here and then 
basically i wanted to quickly go over the definition so basically we have what you can see there is that I define three operations 
which are basically calls that could can be made by the Eth2 client to the eth1 client and you will see these calls all over and it
might be a bit confusing for especially for people who are very familiar with Eth2 because these calls don't directly match you know
like the consensus engine api and they also work a little bit differently from you know how what you might expect and it will be 
changed later we already I have the feedback and it will be changed but for now we have the two most interesting calls which are final 
and proc and then the final is basically just for submitting a finalized block and this is supposed to be called for all finalized 
block not just you know like when finalization actually happens but basically every block that is moves into the final state will have 
this called and then proc is for all the non-finalized blocks and these calls they are generally less important in the context of this 
document but the proc is still used somewhere so this is why it exists but it's mostly about this one call which is the final and I 
just want to make it really clear that it's not doesn't really match the semantics of the api right now so now we can go basically to 
the to the Eth2 section sorry 

**??** 

b refers to a block or a block hash 

**Felix** 

no it's a it's a block this is the the the the terms are actually defined right above this so we have to I but i it's probably a good idea to  
go through it quickly so in this document we have case b for beacon chain blocks and uppercase b for app for execution layer blocks and the b is  
always a complete execution layer block and then we also have h which is for block headers so the block hashes actually never occur in this  
document is really only about like blocks and headers so just keep it in mind and then the the the the like subscript there is basically just it  
identifies the block so we can we can go to the I guess we can go to the Eth2 section now so in the from the eth I describe this thing in two  
ways so there's Eth2's perspective and there's the eth1 perspective but they happen at the same time and it's kind of important to to keep this  
in mind as well so basically when the idea here is pretty simple and you can see it by the picture as well so in the in the first step when the  
Eth2 client starts it starts we assume here at the week subjectivity checkpoint and you can see it it's basically the block where it has the the  
the the pink star and this one it has a star because you know like the the this is like the initial like it has the state of the beacon chain at  
this block it's available and it's a verified state so this is why it has this star and basically the idea is it provides this block actually  
only the header the execution layer header of this block it provides to the client in the first step and that's really it there's it doesn't  
really need to do anything else and then the idea is that from this weak subjectivity checkpoint block it the beacon client moves forward  
through the beacon chain up to the latest finalize block and it just has to kind of assume that the chain is valid or basically it cannot really  
verify anything against the execution layer because the execution layer doesn't know anything yet so it just kind of has to process it  
optimistically by signatures or whatever and once it reaches the latest finalized block this is the step number three now it actually provides  
the execution layer block which is embedded in this block to the eth1 client and now we can go a bit further down and go to the next part so now basically 

**Mikhail** 

I'm sorry Felix I have a question so the first final final b call should be made with the latest finalized block yeah in this case 

**Felix**  

yeah you had the question in your document yeah basically yeah it's just an assumption for now which it just makes it easier to explain the  
procedure yeah and then basically now since it it has provided a final block it just keeps providing the like finalized blocks as they  
happen so it keeps following the chain and it keeps providing the like finalized blocks and to the eth1 client and then it has to do this you  
know while the eth1 is sinking which will take you know like a lot of time so basically our assumption here it actually takes like t beacon  
blocks worth of time to synchronize and this can be quite long and eventually when the eth1 is done it will respo it will basically respond to  
one of these final calls with the signal that it is synced to this particular block that was just provided and once that's the case we can  
basically go into the regular processing and start you know like putting the the non-finalized blocks through so basically after this point  
when the Eth1 says that it synced up to the latest finalized block it is ready to process non-finalized blocks and this is basically the end  
of the sync so that's kind of it from the Eth2 point of view and now we can go to the eth one are there any questions at this point 

**Mikhail**  

I have one regarding this payloads execution after the sync is done when we got this message there are two options one is the  
execution client stores all the execution payloads and then then when the sync is done it just executes them on top of the pivot block the  
other option is that it communicates that the sink is done to the consensus client and consensus client replace these execution payloads in this case the execution client don't need to store them but yeah it should store them right I mean in terms of so the way I see it okay 

**Felix**  

so I was assuming basically that the execution layer is so my assumption is very simple basically the execution layer shouldn't really store  
anything that is you know like totally unverified and even the Eth2 client in this case it cannot really verify these blocks because it cannot  
process them because there is no state to process them on so I felt like basically it doesn't really make sense for the even for the for the  
consensus layer to you know like process or look at these blocks it can always look at them later you know like when it's kind of ready for it  
so these blocks don't need to be stored in the execution layer before it has reached the finalized block because these blocks you know might be  
totally invalid and and they can be re-org at any time so it's kind of you know like why would it even care about these blocks in the first  
place it should really mostly care about blocks that you know like have you know it can actually verify so this is why I didn't put it you know  
this option that during the sync it will also start providing the like non-finalized blocks because you cannot do anything with these blocks during the sync they are not processable so 

**Danny**  

just because it was finalized doesn't mean that it verified the state transition either so well that's that's and  

**Felix** 

that's another question so we will 

**Danny** 

kind of like operating in in block  headers and just looking at difficulty  and making the trade-off that okay when  I get to the head that was probably a  reasonable head because so everyone else  agreed and that had to hide  the following the beacon changing battle  execution is probably making a similar  assumption and so we are as 

**Felix**  

we we are assuming here that if the block was finalized by eth2 there is a pretty high chance that it has a valid state transition because the Eth2 should not be finalizing you know invalid state transitions 

**Danny**  

right right the head with respect to attestations station beyond finality is also you know there's a degraded amount of security but it's yeah operating kind of in the same 

**Felix**  

yeah but this is this this would this is just too complicated for me right now so basically I don't really care about this detail too much for me 

**Danny**  

I care about the detail because I think that it simplifies things like the consensus just continues to provide the data normally like here here's what's finalized here's the process here's the finalization process and that the execution no matter what their sync process is when they're at the end just transit ends up with a state the end to what the 

**Felix**  

yeah yeah we will get to the state so basically the way I want to do is basically I go through a document in the end we did we discussed so  
basically yeah so the the each one perspective is you know kind of you know like a mirror of what we just had so basically what happens is it  
gets the signal to start to swing this is the step number one in the diagram by you know receiving the first call to the final and previously it  
has also received this checkpoint header it's the it's the hw and now the idea is basically that very simply it starts downloading the  
historical headers in reverse and it does it until it reaches the genesis block and when it crosses the checkpoint it also has you know a  
validation step where it actually checks that the it also checks that the the downloaded headers match this checkpoint and this is just a  
safety net to basically not land on like totally invalid chain otherwise we would have to go all the way to all the way back to the genesis  
block to find out that it's the wrong chain so that's why we have this like intermediate thing we will obviously also verify the genesis but if  
it matches the weak subjectivity checkpoint I think we're pretty safe like would be kind of weird if that one's wrong so and then when we're  
kind of done with the headers we can actually download the block bodies in the forward direction so this is the step number three in the diagram and by the way the text for this is below the diagram so just if you look trying to look at the text this the text that describes all this is  
actually below that so and then you go basically through the block bodies and here you have two options you can either basically perform the  
full sync in which case you simply process every block body as you download it and incrementally recreate the state and then the other option  
is of course the state synchronization where instead of processing it you just download the blocks and while you're doing it you're also  
concurrently downloading the application state and we expected you know because we're like in the geth mindset we expect is probably going to be done with something like the snap sync and so the idea is that you will basically provide this and then what's really important to  
understand is also in the diagram while this while this like steps two and three are happening we are actually getting notifications  
about newly finalized blocks and these notifications need to be processed and this is this how they are process is described above the diagram  
sorry for the order but and basically it's the the process is that if you receive a block that exactly matches the next block then it's simply  
written to the database and it can also be used for example to retarget the sync to a newer pivot block which is something that is absolutely  
required for the snapsync it's less required for for example the full sync but it's it's really needed for the snap sync so this is why it  
ha also it has implications on the on the on the sync and then if there's any other finalized block provided then there are two options either  
the block is you know a historical block in which case it's kind of you know was provided for whatever reason and in this swing model we don't  
care about it so we just say it's old and or invalid and then if it's a future block then we restart the sync on this future block and the  
idea for this we will get to it later is for the like restart handling of the sync that basically like if the Eth2 client was restarted and now  
you know has reached a different finalized block then we basically just restart the entire sync procedure on the east one side and just you  
know like try and basically do redo the missing steps so now we can go even further down oh wait wait wait one second so what you can see is  
that basically after all of this is done basically you can see that two blocks have stayed in this diagram so one is the hg which is the  
genesis block this the state of this is always available and the other one is this like block b plus f b f plus t which is basically the like  
final block of the swing so when this block is reached we have to guarantee that the complete application state is available and this is why it  
has the green star in the diagram to show that this is you know the block with the you know final state in the case of the forcing we actually  
may have more state and we will get to the question of state at the very end but basically for now what you can assume that after the sync  
what is guaranteed is that this like the sync block has the state available and this is kind of it for the eth1 side because after that it will  
simply receive you know calls to to process non-finalized blocks and these blocks can you know be processed on top of the state which is  
available and there may also be reorgs and but this is really not the reorgs and the sync are like two different things for now so it's kind of  
not really related so we're done in this as well now we can quickly skip over the section which talks about the client restarts i don't really  
want to go into it too much but it I think this is going to be very important for the for the ethernet client authors to consider these things  
so basically here we mostly talk about like how to handle the content of the database when there are multiple swing cycles and how to  
efficiently reuse the information that was already stored in some previous sync we have a couple things here one is the handling of you  
know like when when when the chain that was previously stored is now like when when you're sinking at a different chain on top of one that was  
already synced then you need to erase the old information and you can reuse the parts by way of this marker system which is described in the  
second to last paragraph so it explains that basically if we have previously synced a an entire segment of finalized blocks we can  
efficiently skip over this segment and not have to basically recheck every single one if we already have it or you know basically we can skip a  
lot of work this way and I think this will be quite important to implement something like this especially when we change the sync later or  
when it you know becomes for example like if it is restart like every time you restart the sync basically you need to figure out what to do with  
the stuff that's already in the database and it's good if it can be reused efficiently so now we can get to the to the last part which is the  
reorg processing and i think this is actually going to be the main subject of the discussion in the upcoming week or two weeks basically this  
scheme what we assume here is basically that because the clients were the clients are supposed to start the sync on the latest finalized block  
and you know as the finalized frontier moves they have to also retarget their sync to this block so basically this this this state needs to be  
available in the peer-to-peer network in order to be downloadable so this is why we recommend here that basically the clients should keep this  
state available in their persistent store and it does argue that basically like since most Eth1 clients are now moving to the model where they  
really only store one entire copy of the state and then a bunch of additional information to facilitate reorgs in some way then basically we we  
argue here that it is the best to simply store this state of the state of this particular block because it is you know like it's the easiest to  
handle and we also described that basically like in order to facilitate the reorg processing it is recommended to then like keep other  
information in the main memory instead of the persistent storage because it just makes the reox a little bit easier and finally we get into  
this part that should probably have way more text so and it's kind of a bit of a controversial topic also no no it's not the issue section  
yet no for now we're still talking about the reorgs so we have the we have this thing with the manual intervention reorg so basically the  
issue is as follows so in the in the current ethereum one name main network what the there is an assumption in in the clients especially  
in guests like this is where we are coming from here so that basically there's got to be the safety net for handling issues that arise in the  
you know live network and for example if there's a consensus failure in the in the network and we just had one so it's kind of you know a really  
good example then it's kind of good if there is a little bit of a time window where reorgs are still possible and in the geth this time window is  
defined to be 90 000 blocks long so at the moment it is basically always possible like the geth will always ensure that it has the possibility  
to perform a 90 000 block re-org and the reason for this is not so much that like during the normal operation these reorgs will happen all the  
time generally it is not expected that there will be a 90 000 block reorg but this specific case where this is really really important is if  
your client version for example had a had an issue in its processing because in this case it will not be able to follow up on the new chain  
until you have installed the software update for example and because of this you gotta have you know like a bit of a time window to actually  
update your client and when you do so it needs to be able to actually you know like reorganize back even if the wrong chain has also advanced  
by a significant number of blocks and this did happen even with this you know like with the with the most recent consensus failure that actually  
because some of the pools were still mining on the like chain that had the that had the that had the bug in it it's kind of that  
basically you know like if if we wouldn't be able to reorg out of such a situation then you wouldn't really like you would have to re-sync  
basically which will take even longer so it's kind of a good idea to be able to have the safety net and we would really like to have this and in  
order to provide it efficiently what we recommend here is that the execution layer client should maintain backward divs of the state in some  
kind of persistent store so basically it should be able for them to re-org below the latest finalized block even if it is a rare occurrence but  
it gives you the safety net to be able to say like you know if there was a problem you can you can kind of reorg out of this problem by then  
applying these reverse divs to your persistent state until you reach the common ancestor of the two chains and from this point onwards you can  
then process forward to get to the good state so this is kind of we we feel pretty strongly about this and we would really like to recommend  
this and as we will see just now it is also probably going to be required to do something like this so now we get to the issues so the main  
problem that we discussed right away is that actually everything that I just said is you know like totally wrong because finalization doesn't  
work in this in the way that we in the get team you know initially understood it so it's kind of we were not aware that actually in the eth2  
consensus finalization is something that can you know take up to two weeks in the worst case so what this means for us is that our current  
scheme of you know like persisting the finalized block will actually like this we cannot just use the latest finalized block as the point where  
we store this date because then we would have to keep up to two weeks worth of state on top of this in some other store and we feel like this is  
too much so we haven't we have basically been thinking about solutions last couple days how to really do it so and what we find is that  
basically probably we're gonna have to adapt the sync a little bit to add this the notion of the calcified block which will usually be the  
finalized block but it may also be an unfinalized block and adding this calcified block will have a lot of implications on the string because  
yeah like it basically makes the whole thing a lot more complicated and i really invite you to like you know look with us through these issues  
in the in the upcoming weeks and figure out how we can solve it in the in the best way we will find a solution for this but yeah for now  
basically we would really like this thing to work in the way that is described in the rest of the document but unfortunately because the  
finalization can take so long it it kind of like yeah means we have to do some more engineering to really figure it out so we have reached the  
end of the presentation now if anyone would like to ask some questions I'm really happy to answer like everything now 

**Mikhail** 

thanks alex I have a question first how much space do you think those tips for these two weeks will take 

**Felix**  

you mean there's the reverse divs we don't really know about this so this is generally something that I that we need to discuss so the problem with the reverse divs is that it's I'm actually not sure it it might be that Erigon maybe someone from Erigon asian can comment you know like how they handle the reorgs I think they might have something like this already implemented 

**??**
 
hi it's sandra from Erigon yeah we have a reverse delta so we can really implement redox by implying reverse deltas 

**Felix**  
yeah so the question is just you know like what's the what's the usual size i mean I guess it's the same size as the forward you know approximately 

**??** 
yeah 

**Felix**
 
I don't know off the top of my head like Peter would know but I don't know what is the usual size of the diff of each block it it's it's it it's I think it's manageable they're quite like i mean it's definitely going to take some disk space I don't really know like what's your window in Erigon for these diffs at the moment 

**??** 

well it's configurable we even have the mode like in the archive node we don't prune anything so we have deltas for the entire history of  
the mainnet and it takes roughly one and a half terabytes to like for a full archive node with pruning it's configurable we can configure it for  
something like 90k blocks as well and then the total database size will be about half a half a terabyte but I don't know of the top of my head how much of that is the delta's the the changes 

**Felix** 
 
well that's that's that's pretty good information it kind of matches my expectations as well so okay yeah so there you have it so I think it is  
it is manageable to like if you know Erigon actually has it already implemented like this then we can definitely say that like this is a this is  
a manageable approach with the reverse diffs it does mean that the reorg's below below this point where we where we keep the like main state  
they will take a lot longer to apply because you have to basically you know like adapt the state incrementally for each block you can't really skip I mean you could store larger deltas but then that would take even more space yeah I will mute when I'm not speaking so yeah 

**Mikhail**  

yeah thanks the other comment that i have is regarding this creative finality so what could probably be used is the like if the  
consensus client would communicate the like finalized the most recent finalized checkpoint the most recent finalized block and the  
the most recent epoch the most recent the block at the most recent epoch boundary each time this boundary happens it could be used to  
like to handle this kind of this kind of non-finality periods if they are too long so the execution client may see these two checkpoints  
and decide what is the like distance between them and I think it makes sense for this calcified block conception and to use the blocks and  
the boundaries at some follow distance from the head so this just basic thoughts on that yeah also we could use the justification stuff  
justify checkpoints but I assume that if we have no finality then we potentially don't have the justified blocks but it could be also used so if if there is if the justified checkpoints might is much closer to the most recent boundary it could be also used as a pivot block 

**Felix**
 
yeah so the details there are like interesting but also like for us it's more like the main thing that we want to achieve is basically like we  
need to have some kind of threshold defined it doesn't have to be very smart about the threshold but the main problem is just it needs to it  
needs to basically not be further than like you know a couple hundred blocks from the head so anything that satisfies that is good enough and  
I suspect that we're gonna have to calculate this on both sides so I think it would be easier to just make it like a very simple definition  
so in my definition I just put you know like it's the finalized block or it's some block which is you know five twelve blocks away if the  
finalized block is older than that so it just basically just puts a bound on that and either way this the change to the calcified block will  
have huge implications because it basically requires that during the certain reorgs need to be need to be handled you know like in in in some  
way there are some cases where reorg is not possible during the sync due to constraints on the state so it it we will have to think a lot about  
these cases and also the the in general it's kind of like a bit messy because we're going to end up in a situation where like since the  
calcified block may not be final it can happen that even during the normal operation we will have to invoke this like emergency reorg procedure  
which will take quite a while it's still and then basically we will also have to put like really hard requirements on the clients to be able to  
satisfy any re-org between the finalized block and the calcified block and obviously how they implement it is kind of you know up to them but  
it would be good to have a recommendation that actually works and for now what I know is that not all clients are able to have such reorg the  
it's it it puts some like for example in the case of Erigon it's like yeah it's configurable but it will no longer be configurable in this in in  
you know for for anything after the merge because you will have to provide a certain number of these tips so you basically have to restrict the  
use of freedom there because otherwise their client will not be able to follow the chain correctly should the situation happen and things like  
that so it I think it has big implications on the clients the dislike adding the calcified block we were certainly not prepared for it when we  
were discussing the sync initially we were kind of thinking that we're going to get off really easy with this you know like finalized block but it seems like it's not not not so easy right 

**Danny**
 
right so I see I see the value i see the like practical engineering need for handling state in these times of non-finality and having things  
that do not go to the depth of finality I do note that in the event that you didn't have finality and in the event there's some sort of  
attack scenario network partition that if reorg's beyond the calcified state are very expensive then all of a sudden that actually becomes like  
a place to attack if you can get the chain to flip between states that are beyond the calcified state then you've now like grinded most  
clients to a halt trying to do that expensive reorg operation from disc so there's I know there's like very much practical engineering considerations here but there's also probably security considerations that need to be discussed in tandem 

**Felix**
 
yeah I would I would also like to note that basically like my first reaction was that you know like we should rather change the Eth2 to basically make the finalization a bit more reliable but i already heard it from like multiple people that unfortunately it's not going to be possible to change Et h2 for this so we're gonna have to I guess find the 

**Danny** 

yeah that would be like a two some other solution 

**Dankrad** 

well this is a fundamental consensus property that you can't have that 

**Danny** 

well maybe like from the plot finale you could you could be in a different mode I suppose but as long as the chain 

**Dankrad** 

well but if you want an available ledger then you have you don't have another choice no I get it maybe one comment on that as though maybe  
one one possibility to what danny just said would be to make reorgs beyond the calcified block manual because I mean I reckon when you are in  
that mode you would probably still say yeah sure reorg said large can happen but there's a high probability that it is actually an attack if that happened if that does happen so you might actually want user intervention to pick pick the pick the fork in that case and it could even 

**Felix** 

yeah well we could we could definitely specify it like this yeah 

**Danny**
 
Felix and I discussed that maybe when you do trigger that type of re-org the execution client responds and says that's really expensive are you sure and then that can either be trigger from annual intervention or the beacon node even trying to get better information before it triggered such an expensive reorg so there's maybe there's a lot of different like trade-offs on that spectrum 

**Dankrad**
 
there's also like I mean a question like when you say really expensive does that mean seconds minutes hours I mean that that makes a big difference there right again I mean 

**Felix**  

it depends on the on the on the implementation of the state and it implements it it depends on on you know like I mean I again since basically  
only Erigon has this exact system implemented right now so it was kind of you know like the way I wrote it was kind of inspired by how I think  
their their stuff is working seems like mostly works like that it's kind of that basically I think they might be able to give some context  
you know how long it actually takes to like reorg for example 10 000 blocks I don't know how long would it be great to get those numbers  
it's just a it's but again it's not really gonna be a guarantee because it it highly it's highly dependent on the actual on the client  
implementation how it is able to do this processing you know like what's going on in the client at the time we cannot really say I think it's  
definitely not going to be on the order of seconds because reorganizing many blocks in this way basically just means like a ton of of writes to  
the disk and yeah I mean you can always cache some things and optimize some things and it might be that we eventually get to the point where  
this stuff is actually kind of you know like fast but we can't really say for sure i would just basically really like to assume for now that it's an expensive operation because if it would be so quick we wouldn't yeah like I don't know we have to see 

**??**
 
I I'm rewinding and blocks is similar in time as going forward and blocks so if like a block is processing in 100 milliseconds that's probably your rough estimations but there's no 

**??**
 
it's not the same right you only need to write the diff you don't actually need yeah yeah it's not like because in executing a block you you always need to read and then write depending on what you just read and whereas this one you would already know exactly everything you have to write so I don't know what disks implement but I can imagine that that could be a lot faster  

**Felix** 

but it's going to ask definitely there's no evm processing involved 

**Dankrad** 

I'm not just talking about the evm processing I'm also saying there are no round trips involved like you you could tell the disc here's everything you have to write do  

**Danny**  

a reorg thing usually would include diffs that were in memory whereas applying this reorg backwards is going to be reading from from disc and so I think that's one of the main time considerations based off of instead of doing reorg's past the calcified yeah 

**Mikhail**
 
and in the worst case we will have to like in the worst case I mean like we have this nine ninety thousand blocks and we'll have to re-execute them like from the last latest finalized checkpoint so it just it depends on the time of the execution but yeah it's just a few hours to my communication  

**Felix**  

so Marius is there also has a good point in the chat so basically we also we already have this kind of optimization implemented in the get as  
well and it's definitely applicable here so like if you need to do like you know a basically really large backward movement on the state it's  
also possible to minimize the number of rights because you can just combine multiple diffs into one in into one in the memory before  
writing anything and doing this usually saves quite a bit of time because there is this the state has kind of high turnover so you may be able  
to skip quite a few operations if you just basically instead of writing it out every single block backwards you can basically skip over some  
and hope that you know the divs kind of cancel each other out it's usually the case so it's like something something else to keep in mind I  
don't think we have to discuss the details about this too much if anyone has like more high-level questions I think the scheme is pretty easy to understand I don't think there's a lot of new information here but if anyone has something then we can answer it 

**Danny**  

so I wanna I wanna just have one comment I think that as we consider this design that it's important to consider it to so we we're not  
writing like a very ad hoc communication protocol between consensus and execution for this particular sync and instead we're writing  
something that generically provides the adequate information to support underlying sync methods so that we don't like design this too  
pigeoned to the particular thing that we're dealing with and I I have some ideas for that and I think that generally what you've written can be adapted to that but i just I think that's a good design goal 

**Felix** 

yeah so for for now I will keep this like the operations that are being used there I will try to keep it a bit abstract because I think it's  
going to be really easy for us to later change it to the like you know like map these onto the like real operations and you guys have a lot of  
good ideas i already check out you know like the the api design document it is you know like there's a lot of information available from from  
the Eth2 node that can be used also during the sync and for sure we will have to make use of it when we redesign it for this calcified block for example we will likely need you know like some notion of like what's the current head of the chain and things like that so we will work it in  

**Danny** 

and I think like sending all procs during the thing as well as finality instead of just sending finalized information 

**Felix** 

yeah yeah cool any further questions 

**Tim** 

yeah I think we're kind of at time for this just because we have a few more things on the agenda and only 10 minutes 
I guess we can continue discussions about this obviously in discord and yeah I perhaps on the merge call next week I'm not sure if 
I'm kind of thinking maybe mikhail's doc will take the full hour but I'm not sure if maybe doing like half the consensus apI and half this makes more sense 

**Felix** 

I don't think we're going to have super big updates for it like next week okay yeah I don't think it makes sense to discuss it you know like over and over 
for now because basically it's just a matter of me updating it for this like idea with the calcified block which I will do at some point next week so yeah 

**Tim** 

okay so no rush then  

**Danny** 

invaluable for Erigon who I think generally relies on different sync protocols full sync and these rewinds 
and things to think about how they're going to be doing it in this context and see what what overlap and what differences their requirements need 

**Tim** 

right yeah 

**Felix** 

yeah I would I would really like you know some more feedback from especially 
from the eth1 client author so this is kind of written I mean like we have written it from the like geth perspective we know we can implement it like this in the geth 
but you know like how it's going to be for everyone else I don't really know and this is specifically about this later section which is about the reorg 
processing and the state availability like this stuff really touches you know on the core aspects of the client and we hope it's something that can be 
implemented by everyone in some way but we have to like this I think it's more a matter of you know like agreeing among the eth one clients how we're gonna do this 
and so it's important yeah for you guys to basically check it and and think if it makes sense for you or 

# EIP-3756: Gas Limit Cap 

**Tim** 

cool yeah so yeah let's definitely discuss it in two weeks once yeah 
different client teams have had time to have a look and you've you've made the updates felix but yeah thanks a lot for sharing this was pretty valuable 
and the last kind of big thing we had on the agenda which apologies we'll probably have to do a bit quicker and we can also discuss again that a future call is EIP-3756 
the gas limit cap Lightclient you've put this together do you want to maybe take a minute or two to give the context and high level overview behind it 

**Lightclient** 

sure I can keep it pretty short as well so setting some sort of in protocol limit for the gas limit has been something that people have wanted to do for a 
while it was originally a part of 1559 and then removed and then in march of this year there was eip-3382 the proposed hard code the gas limit and I think that 3382 failed for 
you know the main reason it failed was because it didn't allow miners to reduce the gas limit in the case of some sort of attack on the network and 
you know building on top of that EIP the next the next plausible solution would be to just have a upper bound of the gas limit and that's what three five three seven five 
six is it caps the gasoline that a in protocol defined amount and it allows for miners to still lower the gas limit in the case of some sort of 
attack on the network and the main reason that you want to cap the gas limit is that right now block composers have full control over what the gas limit is 
and this allows them to to bypass the EIP process in all core dubs process and in making decisions about the protocol that could negatively affect the decentralization security of it 

**Tim** 

right and one bit of context I think I would add is when we had the discussion around I forget the number but the previous EIP they capped the gas limit 
one of the arguments against that was kind of backwards looking saying you know miners have historically always been aligned and and you know like they've 
done a good job so it doesn't make a lot of sense to remove this this this degree of freedom from them and and I think over the past couple 
months we've seen like you know there can be external incentives like tokens of what not that that pop up to game this especially as block space on 
ethereum becomes more and more valuable so yeah I I think the the kind of reasoning that we had around like well miners have always been 
good in the past might not hold forever like looking forward basically if there's more and more incentives for people to to try and influence that process 
yeah I guess people's general thoughts are on this feel free oh a couple hands up alex I think you were first 

**??** 

yeah well my question is somewhere like for consistency of this EIP which was proposed in a very short form without any any estimates on 
what and the number of state grows what is actually there is a factor which potentially affects the security of the network most like 
I couldn't find any different questions in any way and in anyone's work any blog post or whatsoever like is it indeed that latency of __ __ is the stopping is like 
is the point which which is like is the most vulnerable point in processing the new block like what is a state growth rate what 
is what can be called acceptable state growth rate and then like what's the state growth rate per clients because as I was quite 
surprised to hear in merge call well I mean I cannot make a good contribution there but still very interesting for me that it's now was kind of implied 
that the clients would behave in the same way regarding how they store the data and like it means that it's break it's like in the future all the 
clients will behave in a similar way and potentially it will bring everyone's state down to the size of what aegon has at the moment which I believe is the smallest one so like in this current form 
it was very hard for me to react to this in any form so I would just ask to extend it and it would also affect obviously the number of the current limit but 
I I'm just curious and more consistency maybe it's just not in the EIP yet but there is already some analysis would be great to see it 

**Tim** 

right thanks yeah I'll just get to the other comment or Lightclient do you want to 

**Lightclient** 

oh I was just going to say briefly you know we can add more to the EIP I think there's a lot of benchmarks that have been done generally and we can we can add more things to it it was just something to propose the idea quickly 

**Tim** 

cool and yeah just because we're almost that time there's three more comments I think we'll take those and then we'll wrap up I think it was Ansgar and marius so asgard you want to go first 

**Ansgar** 

sure so I only like a specifically brief question as you're saying right like that the the the motivation here 
would be to just make sure __ base becomes more valuable but like miners basically don't succumb to the 
temptation at some point to like go like to to abuse the control there but the the situation is just that right now we plan on the next hard fork with any 
features to be the merge at which point that won't be minus anymore so I'm just wondering is this still a concern like for proof of stake and if if not if this is really mostly 
about minus do we plan on in case we end up with like a december ice age fork and they I don't know january february merge or something 
would we consider this EIP to basically be included in the ice age fork because otherwise it seems to me to not like like this would be the only circumstances 

**Danny** 

I would still say that this mechanism is right for abuse for any set of actors that can control it and I'm not I'm not claiming one way or the 
other on on this I don't really want to get in there but it is still contextually and if it's an issue with minors it's an issue with stakers and if 
there are mechanisms that can be designed to incentivize the miners to do certain things that same exact mechanism can be used on stakers 

**Lightclient** 

yeah and regarding the including an ice age fork the way it's written it could also be included as a soft fork before the ice age 

**Tim** 

cool andrew 

**Andrew** 

ah right so I think the weak consensus in the 
Erigon team is that we are against this this change but we are not going to die on this hill personally I think it's bad for two reasons first it if it requires a hard fork then it will distract us from the 
merge and second is that currently the fees are very high on ethereum so if the guest if the miners or the validators raise the 
gas limit reasonably then it puts some pressure on clients to like perform maybe make some architectural changes to keep up and I think it's a good thing 

**Tim**
thanks for sharing and marius I think you had a comment also yeah I think that's 

**Marius** 
I I would just like to react to that I think that's a bad argument that we would force current clients to change the 
architecture by increasing the gas limits I think all current clients are looking into increasing into changing the architecture in in similar ways as eragon does 
so the people are already looking at it putting pressure on the teams is just not going to increase the the speed in which this is going to be implemented the other the other small comment I have 
that it's currently in my opinion it's not about state growth with the current gas limit it's about dos I'm not sure if all of you are aware away but aware but 
like there are some dos vectors we found some dos vectors recently and it's pretty hard to measure this and so yeah I don't think this this this 
parameter is extremely dangerous and it should not be in the hands of people that are not familiar with what's really going on in the network 

# EIP status updates 

**Tim** 

yeah thanks for sharing yeah just because we're already past time you know we can obviously continue this conversation on discord and bring it up on a future call I think we have kind of some you know definitely areas to look at 
I think Pooja you had put a couple EIPs on the agenda EIP 2364 and 2464 which are basically the eth 64 and eth 65 protocol EIPs as I understand that the issue is like both of those are shipped but the EIPs are still like in draft right 

**Pooja** 

right so the main issue here is EIP-2481 which is for Eth 66. that is in the last call actually the last call duration has also passed and we would want to move that to the final status 
but the problem is that proposal requires Eth 65 which is 2464 and Eth 65 requires Eth 64 which is two three six four and both these proposals are still in draft status so we would want that these two 
proposals should move to the final before we could make move EIP 2481 to the final status I'm happy to make the request to request a status change it's just that we wanted to make sure that it 
is in knowledge of geth team if anyone from get team wants to volunteer and do that fair enough and if not then we can do that and we would need just author's approval 

**Felix** 

so thanks for the initiative what I can say is that I think the last time we tried
to do something like this there was like a huge amount of backlash for some reason because then people came on and you know like wanted to actually see some justification for these EIPs even 
though they are like four years old or something I don't really know like this is definitely something that I would like to avoid so I feel like these EIPs they have been you know we don't even 
use Eth 64 anymore it's already like past you know it's basically it's already happened like it we there is really no reason not to move it to the final because 
it's not even supported anymore and I mean the mechanism in it is obviously still supported because it's carried over into the newer protocol versions but the protocol version itself has 
already advanced like beyond it's like already like after it's end of life now so I feel like it's like from this point of view moving these eaves to the final is like 
totally justified and I really just want to avoid getting the same kind of weird discussions again that we had last time where someone then wanted to like you know for four reasons yeah  

**Tim** 

yeah yeah so let's just try and like if I think peter is the author on both so he'd have to actually accept the the change if I understand but like yes 

**Pooja** 

right yeah yeah I'll make a pull request to move the status from draft to review that would be the first step and 

**Felix** 

guys can you just commit it to the final I mean doesn't it no no no is it really necessary 

**Pooja** 

okay we have some EIP editors on the call if they have you I just have pasted like a link to the earlier pull request 
which we created for EIP 2481 where we received some comments from EIP editors mentioning that these two proposals should be moved so if we can directly make it to the final happy to do that 

**Micah** 

I can answer that quickly I'm not I'm not a fan of skipping straight to final because it encourages people to drag their feet because if you drag your feet long enough eventually you can just avoid the bureaucracy and as much as I hate bureaucracy I don't want to 
create perverse incentives for people to just like not to go through the process knowing that if they wait long enough they eventually they can avoid it 

**Felix** 

in review so can we please can we try to avoid putting it in the review I mean it's okay if they move to the last call or something but they like 
the review seriously this is it's inappropriate because what is possibly gonna happen we just put it to the last call and then maybe even wait if you if you if we have to I don't know it's a special case but 

**Micah** 

let's talk about this in discord only because I suspect 90 of people remain in this call probably don't care yeah okay 

# Announcement 

**Tim** 

cool and okay so last thing and that was it in terms of content but next friday support for 1559 yeah so if you are kind of an application or wallet or just generally interested in kind of broad adoption for eip-1559 you can join that we'll post the link 
in all core dev and there's an issue on the ethereum pm repo for it and yeah that's pretty much all we have thanks everybody I appreciate you staying real 

**Trent** 

last thing if you are an application developer please update your web3.js version to the latest it looks like it may be causing some 
issues with metamask it's supplying some different priority fees which are incorrect so just make sure to update to the latest version 

**Tim** 

thanks right yeah if it is a pre free 1559 3js version it doesn't return a 1559 transaction so that means you get the gas price to set to both the max fee and 
max priority fee and that basically causes overpayment for for some user sum thanks for reminding trent cool well yeah thanks a lot to everybody see you all in two weeks 

## Date and Time for the next meeting

* [September 17, 2021,  UTC](https://savvytime.com/converter/utc-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/sep-17-2021/2pm)
* [Agenda](https://github.com/ethereum/pm/issues/384) 

## Attendees
* Pooja
* Tim Beiko
* Mikhail Kalinin
* Micah Zoltu
* Felix
* Danny
* Dankrad Feist
* Alex (axic)
* Alex Stokes
* Alex Vlasov
* Andrew Ashikhmin
* Ansgar Dietrich
* Dave
* Gary Schulte
* Gottfried Herold
* Guillaume
* Justin Florentine
* Karim T. 
* Lightclient
* Lukasz Rozmej
* MaruisVanDerWijden
* Pawel Bylica
* Protolambda
* Rai (ratan.sur@consensys.net)
* Sam Wilson
* SasaWebUp
* Tomasz Stanczak 
* Trenton Van Epps
* Vub
