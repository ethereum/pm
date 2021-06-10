
# Merge Implementers' Call #4 Notes

### Meeting Date/Time: Thursday, May 13th, 2021 at 13:00 UTC
### Meeting Duration: 60 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/316)
### [Audio/Video of the meeting](https://youtu.be/uzjhLPtvTMQ)
### Moderator: Mikhail Kalinin
### Notes: Santhosh(Alen)

# Agenda
- Rayonism updates ☀️
  - Nocturne devnet
  - Wrapping up Rayonism discussion
- Research updates
- Spec discussion
  - Consensus API standard
   - https://eth.wiki/json-rpc/API
   - https://ethereum.github.io/eth2.0-APIs
  - Execution
    - Different blocks with the same state root
  - Consensus  
 - Open discussions
   - Proposal to move the call to an hour before Eth2 Implementers call
   
# Intro
**Mikhail Kalinin**

Welcome to the Merge Implementers' Call #4
* First item on the agenda is the Rayonism Updates and we are currently running nocturne devnet.

**Mikhail Kalinin**
* Nocturne devnet which started yesterday has reached finality and look stable.
* Have been a few edge cases which we saw on this devnet and there is also like an issue with deposits with in particular with if one deposit voting - We near to solve this issues and see the deposite.
* 8 teams are running a validator and several community team are trying to break the deposit by submitting bad blocks and forth - It is shaping up great
* Couple of questions with Nocturne devnet: 
 * We've plan of testing of transcation propagation - Is any from Ethereum team on the call?
 
**Proto**
* It is a holiday in Germany, so most of the team will be offline.

**Mikhail Kalinin**
* Proto, probaly you might know, whether this PR is about to be merged or has already been merged, which allows transaction propagation.

**Proto**
* I believe there is one pr gary that improves on some of the things, but I'm not sure about transaction propagation. The test net will continue to run for a couple more days, so we can try again later.

**Mikhail Kalinin**
* Okay, that makes sense.
* The other question was about state sync, but I guess that was more at rest to go Ethereum team again so let's just keep it, yeah if someone wants to join Nocturne you're free and you're welcome to do this. You can reach out proto or just drop message in the iranism discord channel and request for any if you get deposited yeah but we need first two deposits to be resolved.
*  so here's the layout for Neptune all right proto, do you want to add something about Nocturne.

**Proto**
* Well, about Rayonism in general maybe I think yeah that's like the next step. Let's [start talking about this](https://youtu.be/uzjhLPtvTMQ?t=222)
* So with reyanism, I think we should basically wrap up the hackathon kind of things and think of the merge more as this thing that we are going to work towards with production, and this basically means that we want to do the rebasewhich i'd like to call it if you're playing with git terminology we have altair and london first this is this missing functionality which has been developed in parallel,  but now it's time to try and like layer the merge work on top of these updates and then implement the new api

**Proto**
* That sounds like the rough plan, so the rough plan is to wrap up Rayonism and then concentrate on Altair and London while client implementers are focusing on Altair and London.
* We will continue to do some spec and research work, such as determining the transition phase. We'll do some proof of concept research on top of the infrastructure we get from Rayonism.
* Thanks a lot to Proto for doing trmendous amount work on it.
* We'll be back after Alair, and London is almost finished.
* We like spawn another merge testnet. Hopefully with the state sync with the new consensus API which is going to be discussed as well and specked out during this period of time a month or two, thats my understanding. I think this kind of plan makes a lot of sense.

**Danny**
* Yeah, I think we'll even expand the consensus test vectors for the merge, which there's a ton of work on spectrum right now, and it'll definitely be ready for the next wave of development.

**Mikhail Kalinin**
* Yes, it has been planned to deploy the Vistrol's devnet and focus on charging during realism. This work will continue in post-training because it is not like pendant and hopefully we'll have yes, as I already said, we have all tools like infrastructure blog,explorer, scripts dockers, just to spam devnets and test nets easily.
* Anything else regarding randomizing? 

**Danny**
I agree with Mikhail that proto deserves kudos for putting in so much work, as do all the contributors and others. It's great to see the devnet up and running.

**Mikhail**
*Yeah, we'll have seven clients that have introduced the initial merge stack, which is an awesome outcome.
* Which client is not present? Yeah, open Ethereum is missing, and I'm guessing Turbo Gath is as well. But they can catch up with the changes from go ethereum, but I'm not sure if that's possible right now.
* Micah asked a query. I'm not sure how to react to it. Will the open very room be able to merge?

**Micah Zoltu**
* It's fine if no one knows the answer. I'm just curious if anyone has any clues.

**Tim Beiko**
* I believe they are still making a decision about it, and I do not wish to talk on their behalf.

**Micah Zoltu**
* Okay

**Tim Beiko**
* Yeah, it's likely that someone learned something that makes sense to share here, but if not, let's skip this.

**Mikhail**
* So, I think that's it for anism. We're now moving on to analysis updates (9.37 seconds)

* One update from my end: I was supposed to start working on the transition process, but I didn't have enough time to do so in order to create any you know readable spec or this kind of stuff for research that I was supposed to do, but yeah, I guess we'll start the next week was actually a bit busy with the orionism other stuff.
Is there any other research news?

**Danny**
* Mikhail, the main reason for this is to adjust the transition component to be a dynamic total difficulty dependent on fork.

**Mikhail** 
* That's it, I was going to discuss how difficult it could change over the voting period and what meaning would make sense to how, what would be the correct way to extrapolate digital complexity that we could anticipate.

**Danny**
* Got it! Yeah, let me know when you open that up so I can assist you.

**Mikhail** 
* Sure, so it's reasonable to use the if one data voting for to get the block hash that we'll use for extrapolation because otherwise, we'd need to reach consensus on this block hash first, which doesn't make much sense, but we'll see.

**Mikhail** 
* Well, that's fine. Are there any other research updates?
* Withdrawals, perhaps?

**Dmitry Shmatko** 
* Yeah, I could say a few things. I received positive reviews from the previous call, and I made some changes. edit partial withdrawals section it appears viable but it will be restricted to validators with bls withdrawal credentials so it's very limited for use in shared pools, I think we cannot do anything on chain interfering one with it but something like shamir's secret, vls could work in of chain pools you could check an updated dog with rewards withdrawals section and provide me with some feedback on, thanks.

**Danny**
Will do

**Mikhail**
* Anything else before we move on?
* Let us now move on to the spec discussion 

# [Spec Discussion](https://www.youtube.com/watch?v=uzjhLPtvTMQ&t=796s)
**Mikhail**
* The first item is the consensus api standard, and I think it's a good time to open this can of worms and start the conversation. Well, I'd just like to share my opinion off the top of my head.
* On that, we'd like to have a json rpc discussion about how the consensus api will be supported by execution engines, and which underlying protocol will be used. We will use for that, and once we have decided on this protocol, we will be free to design the specific endpoints and move forward, so far we have the json rpc api, which I believe most people here are familiar with, and the eth2 api. The beacon node api so json rpc is based on the https as well but yeah it's the rest api and in general I'm leaning towards the rest api it's like convenient it has a lot of tools it can be secured and so forth but the argument for using the json is that it's already implemented in all of the ethon clients and we would only need to reuse the code but one thing that w Because of the close relationship between the consensus layer and the execution layer, I believe that implementing this from the ground up with a rest approach makes sense from this perspective as well to avoid bugs and in the re-implementation that will relate that will abuse the, it will like damage the security, anyhow, so yep, let's just discuss it and any opinions that we should use json rpc for this consensus api.

**Lukasz Rozmej*
* I have a question: can you give me any more specific examples of what we can gain if you re-implement it? Simply saying that there isn't any tooling doesn't really tell us anything, so if we can concentrate on what it can get us and then decide whether or not to do it.

**Mikhail**
* Yeah that's fair, Danny?

**Danny**
* I'm going to pull up an old comment from Peter and Martin when we were debating the api between a beacon and validator and Peter jumped in and gave a long argument for using restful http instead of json rpc and regretted the choice of json rpc on current ethernet client and here it is I won't go through it all here but if you're interested take a look
* That, I believe, is extremely important when making these kinds of decisions. Obviously, I believe what is suggested is that one of the key disadvantages of changing this sort of thing is adding support for another api type on clients that already serve json.

**Micah Zoltu**
* You just said restful http, did you say that or is that a mismatch? Are we talking about http, which means network sockets are out, or is rest over websocket still considered part rest? They are already on the table in this situation.

 *Danny*
 * Well, I mean rest of the design pattern.
 
 **Micah Zoltu**
 * I'm curious because I'm a big fan of rest but I'm also a big fan of websockets and especially for what's essentially going to be a long live connection like this websockets make more sense in my opinion and so rest over websocket I'd be a huge advocate for where I'd be a much weaker advocate for doing all the work to do rest over http or or websocket like we do with json
 
**Danny**
 * I'm not going to respond because I don't have enough resources.

**Mikhail**
* Could you explain why websockets make so much sense in this case, Micah?

**Micah Zoltu**
* Because, correct me if I'm wrong, and maybe I'm here, but there will be a fair amount of traffic over this channel, and we want to make sure we're not being inundated by just http overhead with websocket you spin up the websocket When you open the link at the start and leave it open, the overhead per message is very low compared to http, while with http, you always end up with more overhead from hp headers than you do for the actual payload.

**Mikhail**
* Yes, we have a lot of people who are actually working on http

**Danny**
I think you're overestimating the amount of communication and overhead there, not because of the variables themselves, but because the number of requests that have to be sent and the payloads there are probably pretty tiny.

**Dankrad Feist**
* I mean, it doesn't seem like the header should be as wide as, say, one block.

**Micah Zoltu**
* So, for one, I'd vote for http because it's just so easy to do things like curl and requests and stuff like that, while every other api seems to have far stronger blockers if you just want to experiment and do some fast stuff.

**Mikhail**
* You meant to say you're on the side of rest, that you're in favor of rest? Since json rpc is also used

**Dankrad Feist**
Yes, I agree with http rest.

**Lukasz Rozmej**
* If we want to do rest and web sockets together, we may have to simulate some sections of the rest in websockets, such as having stuff from the route, which requires some code encoding, and so on, since rest was built primarily as a http api, if I'm correct?

**Mikhail**
* Yes, and Micah sorry.

**Micah Zoltu**
* Yes, I'm going to switch off websockets if there's not a lot of traffic, and I wouldn't be surprised if I'm overestimating the volume of traffic here. Do we have any idea on the, so one of the arguments for json rpc is that it allows clients to reuse code because they'll need to open a server on a different port, does that change how much code they're able to reuse like do we know our client?
* Our clients have been built in such a way that it's easier to spend up another copy of the same type of server inside their client or will it be just as easy to spin up a different server?

**Paul Hauner**
* Oh yeah, I wasn't trying to answer that question; I put my hand up before I could try to answer it, but I'm guessing you're right. Oh yeah, I wasn't trying to react to that question; I put my hand up before I could, but I'm guessing you're right.

**Lukasz Rozmej**
* So, to answer Micah's query, it's very simple for us to spin up a second port; we're already doing it for websockets communication, so simply adding another one will suffice.

**Micah Zoltu**
* Is it substantially easier for Nethermind to spin up another json rpc server or is it just as easy to spin up a rest server inside another mine?

**Lukasz Rozmej**
* A little easier to spin up only the second second port I don't think doing a rest uh will be that difficult but in the rest you have to for example correctly use um http code for communication yeah that's part of rest a little bit like carefully designing the responses etc error responses which are more or less specified in the json rpc already

**Mikhail** 
* Paul, do you have any other thoughts?

**Paul Hauner**
* So, as far as I can tell, one of the things we haven't figured out about the interactions between the consensus and execution clients is how to deal with them syncing with each other. For example, if your consensus client is long running and you tell it to wipe the database of your execution client, how do we get them to sync with each other again? Um, has this been fleshed out somewhere because it seems like it could be one of the most important factors in determining the communications that we use, and I'm especially interested because I know that rest can be um, I think it's great for this reason, but it can be restrictive at times, and I'm I need to think through but I'm not sure if we'd start to run into problems with receptivity.

**Mikhail**
* In this situation, I don't think the rest can add much more overhead in terms of sync than the standard json rpc, but that's just my view.

**Micah Zoltu**
*  Is there some correlation between the two stateful at all, or do you hypothetically have three execution clients on the back end talking to one um consensus client and all will be perfect, or is there some kind of presumed state?

**Mikhail**
* It's stateful because it depends on the design of the execution client or the execution engine, like if we have three servers in front of the execution engine 4 that processes blocks, that's one design, and if we have the monolith architecture that we have today, that's another, so yeah there's a one to one relationship or one to many to one many beacon node relationship.

**Dankrad Feist**
* It doesn't have to be stateful; the only state will be whether or not the execution node has obtained the block, but once it has, I believe that should be the only state.

**Danny**
* The execution engines rely on a notion of the current head for a lot of things that could be changed and you could just provide a more dynamic representation of the block tree and several different potential heads, but they currently rely on like when you set the head there are some things that are optimized in terms of what state is available and which pending blocks are being created and that kind of stuff.

**Micah Zoltu**
*Is it possible to design in a different manner?
* It would be fantastic if this could be a stateful or stateless relation, for example, can we make it so that when the consensus client makes a request of the execution engine, it gives the execution engine all the state it needs to respond correctly at that point in time?

**Danny**
*  I mean, you certainly can, and I believe the inserting block has the state that it requires, i.e., you either have the previous block or you don't, and a symbol block, I believe, right now tells us the head you want to assemble on, and then the information is there again, but there are still likely some optimizations and reuse of how these things work today that that head becomes and the other methods i think would work fine but it doesn't reuse existing code quite the same.

**Micah Zoltu**
* Okay, so if a consensus client asks an execution client to build me a block, it will give it enough information to either get a correct block or an error saying "I can't build that because I don't know about this head you're talking about," but it won't give back an incorrect block.

**Mikhail**
* Okay, so let's say there are three execution engines and one consensus client in front of them, and in order to stay in sync and maintain the full state and execution chain, this uh consensus client will have to feed all three with new blocks and any other information required.

**Micah Zoltu**
* So, effectively, whatever routing you have there will have to do a broadcast so that it receives a new block new set head from the consensus client and then broadcast it down to all of its related execution clients so that they all update themselves, right?

**Mikhail**
* Yeah, like set had a new block

**Danny**
* I believe one of Paul's concerns is that if  consensus says insert block but the execution engine doesn't already have the parent in there, what is the communication protocol to recover from that? Does the consensus just walk backwards until the execution engine has what it's supposed to have and then inserts from there or is there some other more complex communication protocol to recover from that?
* Just walk backwards until the execution has what it's supposed to have and and then inserts from there, or is there any other more dynamic recovery that's I don't think we've quite worked on and that's the kind of like how are these two things in sync um you know what happens if one shuts down and then you come back up and it doesn't have a database like that kind of stuff we haven't worked through it

**Mikhail**
* Yeah, actually, before the assemble block with any parent hash is sent, we have this new block with this parent hash right so if that wasn't the case, then yeah, there is a consistency between the beacon chain and the execution chain uh if we're talking about like uh one consensus engine and one execution engine uh if this is like the infrastructure where you have several we can become we can change clients using like a few execution engines or something like that yeah probably that could be the case.

**Paul Hauner**
* It seems to me that a test would be if you had one um consensus client, then a proxy, and then three execution clients behind that proxy, so you know the walking back process procedure that Danny was talking about would just doesn't makes sense if you start bouncing off random um execution clients based on the proxies.
* It makes me think that maybe rest isn't the best thing we're chasing after. I mean, naturally, I'd prefer to rest just because it's a good thing to do. It's preferable to a json rpc because I like it, but this just feels a little bit more like a rpc to me, like a one-to-one rpc.

**Mikhail**
*  Yeah, I get it. What I don't like about json rpc is that it has custom error codes and custom error messages, but as previously mentioned, we're all familiar with that. One thing to consider here is that all if two clients already support json or pc and have a json rpc client to fetch deposits and get eth1 data for the rewards, we won't have an overhead and we won't have to implement this json or pc client either.

**Paul Hauner**
* Thank you, I was just about to mention that the new design has these two different mechanisms for consensus and execution.
* I think that's the direction we're going for now just because it makes sense, but um a world where they're wrapped in the same process, not necessarily maintained by the same team, but they present as a single binary um seems appealing to me, and maybe using something like json rpc is nice because we might start to use something like an ipc socket as a comms transport between them and if we're doing something like that, instead of having instead of having two processors we're importing them as a binary then that works very well for them to talk between each other um whereas like having a  http client server between these two like inside the same processes is a little odd as well

**Mikhail**
* And, when you say binary, you're referring to the binary protocol.

**Paul Hauner**
* So I'm talking about binaries in the sense that you know what I'm talking about .exe is a type of executable file in Windows.

**Mikhail**
* Okay.

**Micah Zoltu**
* Correct me if I'm wrong, but if the consensus client says, "Hey, assemble me a block with this parent," and the execution client doesn't have that parent, is it correct that the execution client then goes to its own gossip network to get that block and doesn't respond to the claim? The block does not respond to this argument, so it is still one-way communication or request response rather than two-way communication.

**Mikhail**
* There are two options for returning an error, one of which is a database and consistency error, since these two parts are actually one client and their data should be consistent. The other option is and try to go to and download and pull this block from the block, not from gossip, but from the protocol network protocol and to get those blocks, but yeah I guess what was i kept in mind is what like it's just responded with error so there is no such parent block so

**Rai**
*Do you still request the block through ether or did we remove it as part of the networking to make the execution engine a little more efficient?

**Mikhail**
No, we didn't take this out, but we did cut out the vlog gossip.

**Danny**
* It can also be used because of how initial sync, especially state think, is performed, and there's certainly an interesting design decision here if the execution engine detects any sort of inconsis consistency because requests are being made for things it doesn't know about, it can use that endpoint to go and fill you know the unknown stuff and to use the peer-to-peer network to get back in sync with the consensus node, which is fascinating because it probably works right out of the box, but it's also strange.

**Micah Zoltu**
* I like it because it makes it so that the consensus engine says, "Hey, do this thing for me," and the execution engine says, "I can't," and then it basically fixes itself on its own, like it's essentially a self-healing system, and then if you had an edge server proxy server between the two, you might notice that oh, we got a consistency area, take that execution", engine out of rotation because it's down for a while and then we'll try it again later, and in the meantime, I can fall back to a backup execution engine or just it's got three in rotation now it's just got two in rotation or whatever, and then the whole machine ends up being reasonably self-healing if the execution engines can heal themselves when they get a request that means they're out of sync right?

**Danny**
* Yeah, I like it as well. I mean, it gets to use exactly what the execution engine does today to heal itself if it learns about things it doesn't know about, but it can still complicate things, especially with one-to-one communication. For instance, if you talk to an execution engine locally and it doesn't know something, you just kind of Sit back and hope that it knows about it in the future because it presumably aids in self-healing, and the consensus can't be as proactive as it would like to be.

**Micah Zoltu**
* I see, because it'd just have to pull it because it's a one-way communication channel before it returns a success, right? Yeah, the case we're talking about right now is

**Mikhail**
* If a consensus client asks for assembling a block on top of a parent that isn't known for that isn't like presented in the execution chain, it means that the consensus client before while importing a parent of this block failed or something bad happened, because if the execution engine response is like this block is true, we assume that the consensus client before while importing a parent of this block failed or something bad happened.

**Micah Zoltu**
* The reason I keep harping on this is because I believe pragmatically, what we'll see is a lot of people running validator clients and very few people relying on third-party providers for the execution client because the execution client is too expensive to run, like I run a few and they're not cheap and they're not easy like it's.
* It's you basically have to run operation center to run an eth1 client or an execution client right now and that's not going to change in the media future like we're working on it but that's a long way off and so I think realistically we'll see people going to places like infra and fast node and all these and alchemy for their execution client and they run their own consensus client.
* And,  in that case, we do have exactly this where you've got you reach some proxy server and the processor is going to route you to one of 100 execution clients and so I suspect that's going to be the typical scenario rather than the rare one as we would like which is unfortunate but I think the real I suspected truth.

**Dankrad Feist**
* I think an operations operations center is a little exaggerated um I agree it's a big problem it's like where it connects more than twice um but also as a comment like uh from a research perspective we're thinking about how to change it like using improve custody where we make it necessary for people to run their own execution like we want to make it very hard to do

**Zahary Karadjov**
* who we have users at nimbus who run both, gets an investment from a Raspberry Pi.

**Micah Zoltu**
* I've heard of such people, but I'm not sure how they do it. I rent a server, and I'm struggling to keep it running.

**Paul Hauner**
* Yes, we fail to hold gath up on a box with eight gigabytes and four cores, but it sometimes works perfectly.

**Micah Zoltu**
* Just a quick question: if everyone agrees that we're going to brick people who aren't running both execution and consensus client, then yes, I think we should design for the one-to-one connection and focus on making that good and smooth if we think that, at least for the time being, that's what we're going to allow for and enable.
* People to do things like use alchemy and infira, so I believe we should design for that because I believe that will be more popular, so maybe the first question is which one are we actually designing for?.

**Danny**
* There are two types of validators uh sorry i'm getting a lot of feedback there's validators where there's an explicit desire to put a proof of custody on execution so that it's not outdoor school but for users in general there's all sorts of uh design considerations you know running a beacon chain then and getting proofs about state uh execution their state or running a light.beacon chain and not running execution at all or you know amongst several different versions of that so it's not just the validator that we're developing for here not sure also to add

**Dankrad Feist**
* Maybe to add that the one-to-one design might include things like secret shared validators and stuff like that we should also consider that because it might make sense for example to run a secret shared validators where you have uh four separate beacon nodes but only one execution node uh designs like that uh made possible so I wouldn't necessarily say that only because we don't know
* Yes, that's correct; sorry, go ahead.

**Paul Hauner**
* I was going to say if we look at one too many do we have this then the idea that you know if a consensus client requests a block from the execution client because it doesn't know the parent and goes and tries to find the block itself don't we have the problem that the execution client can't rely on blocks being valid unless it can verify them with a consensus client right and Okay, so if it gets a request for a block, it can presume that it's canonical, but that kind of breaks down when you get to infuria, where you'll only have people spraying something at it. The validity of waiting is independent of the right of consensus.

**Danny**
* So you might tell it to follow an execution chain and it would be valid in terms of execution parameters, you know the evm transformation correct, but the consensus any any consensus kind of outer layer on top of that is not going to select that chain if there isn't a valid set of transactions, I mean a valid set of transactions.

**Paul Hauner**
* Wouldn't there be a trash can by then? I could only fill it up.

**Danny**
* Completely, if you open it up to the point that anybody can trigger anything you're talking about, I believe that's a loss factor.

**Mikhail**
* Yeah, because that's what I was trying to suggest, that it has to be a consensus block first, so it can't just get the execution block hash and heal itself.

**Danny**
* Tt's possible If it's a trustworthy partnership, I mean, if in bureau running execution layer clients and not getting any view into the consensus layer, I mean, I think they'd have to build their own trust model here on these endpoints. I don't think you can open up any of this stuff to arbitrary requests regardless.

**Mikhail**
* Returning to json or the sea rest api, are there any reasons for or against json rpc? Does anyone have anything to add?

**Paul Hauner**
* I have the impression that we aren't quite at that point yet, that we still don't understand the nature of the communications between the two things, and that I believe that when Amica spoke about one to one or one to several, that's probably what we need to be thinking about in abstract terms before we start picking protocols, but maybe I'm wrong.

**Danny**
* Danny: Yeah, I'd tend to agree that these one-to-one, many-to-many, and many-to-many questions, as well as the staying in sync question, should be poked at least for a week or two to see whether the current communication protocol is sufficient, and if it is or is not, that would tell us what we want to do here. I mean, my gut tells me that respiration tv is better, but based on what I already know, but I believe there is more unknown

**Paul Hauner**
* If I had my way, I'd like to see it be like one-to-many restful http http because I think that's pretty versatile that'd be that'd be cool to aim for, I think.

**Danny**
* Proto, because of the authentication model, you had a small preference for wrestle hdg. Is there something you want to share before we move on?

**Protolambda**
* So I think separation between the two different rpcs is really important for security and just stability. I think in the current design there's a lot of assumptions on the e1 connection on the existing event connection for the deposit data fetching and sync and um in this test net it's really been a struggle mostly to work around these assumptions to make it stable and I think just Starting with a new relation that is based on consensus and is separated and protected is simply a better approach.

**Micah Zoltu**
* If I understand you right, you're saying that by using a different protocol, we can almost guarantee that we won't have clients with bugs that trigger bleed between the two.

**Protolambda**
* Yeah, so inside the json rpc they're like it's the client that reveals it and declines that fetches from it that have these current assumptions around it for deposit data sync and at the same time we mix it up with the previous existing code and I think it's just like you just increased the surface for books in the consensus api and I think it's just like you just increased the surface for books in the consensus api.

**Paul Hauner**
* So, Cody, are you attempting to make a case for dedicated deposit endpoints on execution clients?

**Protolambda**
* I think that's a better idea as well. We've seen different I also like books in the receipt logs and whatnot, and if they break anything this important, then yeah, it would have been a lot  i would not mind separate.

**Mikhail**
* Is there anything else you'd like to say, Lucas?

**Lukasz Rozmej**
* Lukaz Rozmej: so a little bit on the side because we are I heard some talk about uh one too many clients um connections is that right oh it's okay uh we were also thinking about making it many too many so uh arbitrary number of clients could talk to one uh ethereum to letter in one node and vice versa so uh we were also wondering what this would be this would require some additional work on our side to enable that and we will have to differentiate the clients and keep some state for them uh some block tree info about the current state and some transaction pool uh need need to be separate uh but the rest could probably be shared that could be a good way to like reduce resource use because if each ethereum to validator node would need an ethereum one node that could be quite a big If we can share each ethereum onenote for like 10 or 100 ethereum two nodes, it will be less of a pain and easier for providers of that infrastructure, for example.

**Mikhail**
* Unless there are any more arguments, I believe we can conclude, and uh yeah we are already using json rpc for consensus api and we will continue to do so for the proof of concept and development phase um yeah that being said it is yet to be determined what are the requirements for this communication protocol uh with regard to the sync process so we'll see we'll see more inputs to this question and get a response Okay, let's move on to the next one, spec discussions and execution (51.41) First and foremost, we encountered an interesting edge case uh with the catalyst on nocturne.net um there was a kind of uh yeah okay so the case is the following uh like um suppose we have a block uh and we have like two children of this block um and these both children have the same state route which is legal because we no longer have uh minor rewards and these two blocks can have empty transcations list. 
* What catalyst does is reject the second block and observes an error like yeah this, and this process is part of a mechanism that defends against state mirroring attacks. 
* I'm guessing no one from go ethereum is here to address this specific action, but I'm sure Proto can add more here.

**Protolambda**
* So this state mirroring attack really just applies to like long range attacks, like beyond like 100 or so blocks in the test net when they're done with many transactions, it's very common to have the same state routes and rewards are issued in the consensus protocol and not in the execution protocol, so you'll end up with the exact same state and maybe we could redesign this so that we have a unique state route parent block and this would be changed if here in one side.

**Danny**
* Okay, I've got a similar issue, does anyone know?

**Mikhail**
* Any other econ clients have a problem with, or have problems with, or have any protection against, having two blocks with the same state route?

**Danny**
* Is this an issue? While there is an alert from guess, does it currently harm the functionality?

**Protolambda**
* It will inserts when it adds a side chain and reorganizes the blocks.

**Mikhail**
* Yes, just reject the block.

**Rai**
* So, at the very least, we need to read Martin's right away to see if it affects us because we don't know what the conduct is right now. It's on my to-do list.

**Danny**
* okay, so if the consensus side tries to insert what the execution sees as a block it already has and it just returns and says okay I I have that already um then then you point then you did a set head assuming the method exists um will there be much of an issue here because essentially I I suppose two different we talked about this a little bit but Like two different beacon chain forks might point to the same underlying execution layer chain and that all of them essentially if you reorg from this to that you'd say the head and then point to the same place and the execution layer probably doesn't care I think there's probably only some minor things to work through here but I don't suspect that we will really need to enforce that Every beacon chain execution layer root is distinct across forks; obviously, you could accomplish this by inserting.

**Protolambda**
* So the problem why we protect against this attack is to optimize the way we sync these execution padlocks in the ethereum one client so if you can trust the state route then you can basically skip ahead and when there's this kind of long range mirror attack I don't know the details so you may skip this validation and so even though the state route is the same the block contents could be different and then you could get into this dangerous kind of sync scenario

**Danny**
* What exactly do you mean when you say that the contents are different?

**Protolambda**
* If you optimize to trust the state route, you could run into a problem where your block contents aren't federated correctly if you reorganize and then accept the state route because it's the same. Then your block contents may not be federated correctly

**Lukasz Rozmej**
* I have a question, we're talking about mirrored state attacks, right? I believe it's related to pruning, and we'll prune once we've finalized a block from ethereum to consensus in the ethereum one execution engine, since we can't prune before that.

**Mikhail**
* Yeah yeah I agree because with europe with you on that also I think that this is not related to potential and prune state try pruning implementations this is I could be wrong here um it's probably better to ask your ethereum but from what I understand um it's related to how geth does state try pruning and yeah this kind of attack is specific to geth and to this particular pruning algorithm When they have like this side chain that is not executed until it reaches a greater total difficulty than the canonical chain, they switch to the side chain and if there is like a gap where they can't retrieve the state because it's been pruned, they trust like this portion of chain they can't execute that's and that's where the state mirroring appears yeah so is it. as a result of reorganizations Yes, during reorganization and as a result of pruning.

**Lukasz Rozmej**
* Yeah, so if we don't pronounce it before the block is over, we won't have this issue.

**Mikhail**
* In the context of executing and the context of execution on the beacon chain, I don't think we need to make state routes unique for each block, but this this is just an edge case that appeared in the nocturne devnet as a signal to consider um this state route is not unique for each block and keep in mind for further um design or like testing and so forth.

**Lukasz Rozmej**
* So, never mind, we endorse side chains because we want the state to be consistent because of the low level of traffic there, and we're cool with that in general.

**Danny**
* You said there was a write-up on this from Martin, and that's right.

*Rai*
* Yeah, he recently posted it in the um private key base that these one developers have, um yeah, I had to read that, and I guess it's essentially just a connection to a github yeah.

**Mikhail**
* Well, so is there anything else that implementers would like to inquire or mention on the execution side?

# Consensus discussions [1:00:26](https://www.youtube.com/watch?v=uzjhLPtvTMQ&t=3626s)

**Mikhail**
* Okay, so the next step is consensus discussions.
I don't think there's anything to discuss here, but just in case, does anyone want to discuss something or ask a question? 
* Okay cool, so let's go to open discussions, and there's been a proposal to move this goal to the same day as if another scrum is being made, so we'll just make it but for the same time slot, so it would be like one hour of u merchant panerai school and then the two implementers call just curious what do people think about it and probably Paul this question and probably paul has will express his opinion

**Paul Hauner**
* Yeah, thanks for bringing it up, Mikhail. Um, these days, this call is 11 p.m. now, and then midnight when daylight savings kicks in, so stacking them together is appealing to me. I'm not sure whether anybody has reasons why that's not a good idea, but I think meeting fragmentation is also something that interests me.

**Mikhail**
* I'm just curious if we'll be able to see it for two and a half hours, particularly if we have a lot to talk about with the merchant about other e2 things.

**Danny**
* The other issue I see is call fatigue after an hour or two, but these two calls are normally fairly light. I think that will change a little bit as we move into altair output, but those calls are mostly only 30 or 40 minutes long.

**Mikhail**
*  Any objections to trying it out and seeing how it goes? Well, so we have a youtube letters target next week, so I think we'll try the new time for the vertical three weeks after today, right?

**Danny**
* I think that's a good idea, a little extra time now that Rayonism has subsided and there's a lot of work on Altair in London that'll happen, that's a good break.

**Paul Hauner**
* Yes, thank you all for your thoughtful consideration; it means a lot more than you would think.

**Danny**
* I have a guest room available for you to move into in Colorado time zones are fairly consistent.

**Paul Hauner**
* Sure, I'll check with my government to see if I'm allowed to leave.

**Danny**
* Yeah, I guess you won't be able to enter this country.

**Micah Zoltu**
* I've lived in the United States, and don't believe anyone who claims their time zones are anything close to reasonable.

**Danny**
* Yeah, it's wonderful; we're awake; I'm awake; I have calls at six a.m.; it's wonderful.

**Mikhail**
* Okay, any closing remarks okay, thanks everybody, thanks for uh this fantastic month of work that I've had the pleasure of being a part of, and I'll see you in three weeks, 

-------------------------------------------
## Speaking Attendees
**Mikhail**
**Danny**
**Micah Zoltu**
**Rai**
**Paul Hauner**
**Lukasz Rozmej**
**Protolambda**
**Dankrad Feist**
**Dmitry Shmatko** 
**Tim Beiko**

---------------------------------------
## Next Meeting - June 03, 2021 at 1300 UTC

---------------------------------------
## Zoom Chat:

09:00:18 From  Mikhail Kalinin  to  Everyone: starting in 3 minutes
09:06:20 From  Mikhail Kalinin  to  Everyone: https://github.com/protolambda/nocturne
09:11:11 From  Tim Beiko  to  Everyone: Yeah, this was great!
09:11:15 From  Micah Zoltu  to  Everyone: Which client is missing?
09:11:19 From  Tim Beiko  to  Everyone: OE
09:11:24 From  Micah Zoltu  to  Everyone: 👍
09:11:36 From  Micah Zoltu  to  Everyone: Do we believe that OE will be able to make The Merge, or is there worry that they may not make it?
09:11:58 From  Tim Beiko  to  Everyone: We can let them answer that.
09:15:41 From  Dmitry Shmatko  to  Everyone: https://hackmd.io/@zilm/withdrawal-spec
09:16:14 From  Dmitry Shmatko  to  Everyone: rewards withdrawals are here https://hackmd.io/@zilm/withdrawal-spec#Partial-withdrawals-
09:17:12 From  Micah Zoltu  to  Everyone: It is already decided that execution engine is "server" and consensus engine is the "client" and there are no requests that flow the other direction?
09:18:15 From  danny  to  Everyone: that is the current design, and a design goal unless we hit an unexpected snag
09:18:21 From  Micah Zoltu  to  Everyone: 👍
09:20:16 From  danny  to  Everyone: https://github.com/ethereum/eth2.0-specs/issues/1012#issuecomment-489660765
09:23:24 From  Micah Zoltu  to  Everyone: I'll back down on WS if the throughput is low.
09:27:04 From  Micah Zoltu  to  Everyone: My very weak and meaningless vote is REST over HTTP at this point I think.
09:35:27 From  Lukasz Rozmej  to  Everyone: https://github.com/ethereum/eth2.0-specs/issues/1012#issuecomment-489660765
Read through it. I agree on everything. The only thing this is relevant to public current JSON RPC API. I don't  see anything that would be related to the merge communication.
So if we would be moving to all REST API - then I am all in. Just for Merge - I don't see the point.

09:36:47 From  Lukasz Rozmej  to  Everyone: unless we want to pick this as a starting point for migration of other API's
09:48:10 From  Micah Zoltu  to  Everyone: I still like REST over HTTP, even after that conversation.
09:49:29 From  Lukasz Rozmej  to  Everyone: Micah I like it too, it just doesn't bring any benefit to the merge itself
09:50:13 From  Micah Zoltu  to  Everyone: If we need them to stay in sync (bi-directional), then I'll probably switch my non-vote to WS with *something* (maybe JSON) for payloads.
09:50:24 From  Micah Zoltu  to  Everyone: 👍
09:52:03 From  Micah Zoltu  to  Everyone:I like proto's argument.  I'm a fan of making it hard to add a bug to a client on accident.
09:53:33 From  Mikhail Kalinin  to  Everyone: 👍
10:04:55 From  Tim Beiko  to  Everyone:If it helps with timezones, let’s do it :-)
10:05:45 From  Micah Zoltu  to  Everyone: Do what I do, don't get any human socialization other than meetings, then meetings become the highlight of your week.
10:05:52 From  danny  to  Everyone: lol
10:06:02 From  Mikhail Kalinin  to  Everyone: ahaha
10:06:31 From  Tim Beiko  to  Everyone: +1 to 3 weeks

---------------------------------------
