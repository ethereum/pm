 # Post-Merge MEV Breakout Room meeting Notes 

### Meeting Date/Time: Saturday 2021/12/11 at 20:00 UTC 
### Meeting Duration:  1.15 hour  
### [GitHub Agenda](https://github.com/ethereum/pm/issues/423) 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=ivcI_plFu1o) 
### Moderator:  Tim Beiko 
### Notes: Avishek Kumar 


-----------------------------

# Contents <!-- omit in toc --> 

- [1.Overview of MEV-boost & Flashbots for Ethereum clients proposal ](#1-overview-of-mev-boost--flashbots-for-ethereum-clients-proposal)
- [2. Milestones & timelines](#2-milestones--timelines)
- [3. Flashbots Kintsugi demo](#3-Flashbots-Kintsugi-demo)
- [4. Q&A](#4-qa)

 - [Attendees](#attendees)
 - [Next Meeting Date/Time](#next-meeting-datetime)

----------------------------------------------
# 1. Overview of [MEV-boost](https://ethresear.ch/t/mev-boost-merge-ready-flashbots-architecture/11177) & [Flashbots for Ethereum clients](https://hackmd.io/@paulhauner/H1XifIQ_t) proposal

**Tim**: Okay, we are recording. welcome to the post merge MEV breakout room. Stefan's gonna walk us through the proposal, architecture, some demos and then we have plenty of time also for questions, comments and conversations from the different client teams.  Yeah again this being recorded if you're not interested in that please jump off now. We will have full notes and recordings available for people who want to watch later. Yeah over to you  Stefan.

**Stefan**: Awesome, yeah thanks everyone for showing up with such a brief agenda. I will just cover some of the basics of what we're trying to achieve with mev boost. How it fits within sort of the transition from the current MEV geth. How it works on the network today and where we want PBS to go. And then I will try to get into some of the technical overview of how it works.I will cover some of the milestones and how we plan to implement them. Then probably do a quick demo of what we have with merge mock running right now. Jason, if he is here, would be the right person to jump on and buy that demo and then yeah we can go into discussion and I have listed in here. Sort of the open remaining questions too. They need to be figured out over the next couple months. Okay without further ado, let's jump into it. 
So I will just assume a good amount of background knowledge on/of geth. If you don't quite understand how the system works definitely go check out docs.flashbots.net. It has sort of a good description and highlight of how it works. But basically right it's a block space auction it allows for outsourcing parts of the job of block construction to basically anyone in the network and the way that it works today is with sort of this intermediary that's a relay that aggregates transactions as well as bundles which are like fractions of blocks. Filters all the like spam all the invalid stuff and then forwards them over to the minor. You know it's working right it achieves sort of the goals that we set out to achieve which is uh providing a block space auction mechanism. But it's by no way perfect. So I have just listed here some of the properties that we are looking to improve upon with my boost and with pbs. 

So the first one is **full block bids**, so right now it only accepts bundles but that doesn't allow for expressing sort of the full range of types of mev that can be extracted or really preferences on the order of transactions and so switching over to a system that is able to send full payloads. Right in the proof of stake context sort of addresses this issue.  

Another component is **solo staker participation**. So right now the way that MEVgeth works. We are sending all the transactions over to the miner in cleartext, so the miner has a view of all the transactions that are coming in and really we are relying on a trusted relationship between the relay operators and the miners to prevent the miners from sort of stealing those transactions or you know dropping censoring those transactions inserting their own et cetera. And the goal is to move away from this because it restricts the ability of solo miners to participate in this. So I have got today right. There's really only mining pools that are participating and only mining pools with a significant history of participation in the network. 

But we want to move towards a model where anyone can sort of just connect their proof-of-stake, validator node as long as they have. You know the 32-ETH stake they're able to connect to the system and start receiving payloads so to do that we want to withhold sort of the content of the transactions not reveal them and instead only forward over to the validator the header. So we have it sort of noted here as the validator gets the payload header from the relay and then it's able to return this signed header. So yeah this allows for the solo staker participation but it also sort of adds an additional sort of trust assumption on the way that the relay operates. 

Third component or third design criteria that we had was **client diversity**. It's kind of in the name right like MEV geth was built baked in directly into the geth client whereas for proof of stake. We want to really help and contribute to the drive for client diversity and so mev boost moves a lot of the logic to an independent middleware. So this diagram sort of shows right
the components that we're already familiar with: the boundary client, the beacon node and the execution client. Mev boosts sort of slots itself. In Between here as as a middleware and
interfaces with both the execution clients and the relays for performing block construction duties and then yeah. We can talk a bit about the trade-offs involved here. so complete privacy and trustlessness. Ideally we want to move towards a world where  the builders or the transaction initiators don't need to trust anyone when they submit the transactions and they are guaranteed to be sort of private or at least unknown until they are included into a block and propagated to the network here.There's sort of a an asterix because it does improve the condition over the way that mev guest works because the validators don't see the content of the transactions but it still relies on relays as sort of being actors that are not as you know profiting from the content of the transactions that it receives. So that's a property that only really gets removed in the full pbs at the protocol level where we are able to remove the relay component completely and the builder can communicate a payload  without revealing its content to any third parties and then yeah trustlessness sort of works in the same way but this is really from the validators perspective which is under the boost formulation of  the separation. The validator sort of receives a relay from receives a payload from the relay and signs it without really making sure that it's a valid payload and instead it trusts the reputation of the relay not to produce an invalid payload and it's up to further validators in the network. So you know validator is our future slot tenants to evaluate to see if the relay was acting malicious or properly and make sure that the payload that was  proposed by the relay wasn't a bad one and if it was make sure not to accept payloads from that relay anymore . So again in other asterix there's some improvements to the way that the
trustlessness works but it's not as good as it could be under a full pbs format. Yeah I am tempted to pause here to see if there's any thoughts, questions, comments before I dig into the rest of the presentation.

Okay cool yeah maybe I will try to keep an eye on the chat as well. If anyone wants to just drop questions there while I am going through. I will just try to answer them. So this I just want to talk a bit about, how I see network topology so I think one of the scary things about
looking at this is like wow! okay so there's one builder, one relay and then you know they are sending payloads over to the validator, that's not really the goal. The goal is to make sure that there are as many redundant parties that are operating in each of these roles and what this essentially enables is that if one builder serves to do censorship or something like this. It is easy and trivial to switch a different builder and like the other builders will still be able to submit their transactions. Similarly with the relay if one relay starts to propose invalid payload for whatever reason let's say they go offline. They have some infrastructure issue
the validators can sort of trivially fall back to to a different relay you know this is just network
redundancies to make sure that the system continues to operating as normal but in any case the validator sort of locally has still the ability to fall back to a local execution client if all
this fails and all this becomes invalid. So yeah we have done a few rounds of iteration on how the system works. So this is kind of like the latest sequence diagram of how the  messages are being passed. I am just going to go over it quickly. I think it's useful to highlight some of the calls that are sort of standard in the engine api today and then some of the calls that are modified to make the system work. So yeah this is a full life cycle of a block proposal of the block construction. It starts by the engine fork choosing an updated call which gets proxy to the relay or I should say to my boost that also sends that to execution clients and the relays. So right now this fork choice update is used for both notifying what's the latest head of the chain but also for communicating the fee recipient address that's going to be used by the slot tenant on their block proposal. Once it's time to actually produce the block here what we have done is we have replaced the familiar get payload api call with a builder get payload header call and basically you know the parameters of the call are the same but the return values are different. So instead of returning a payload that includes the full transaction list.The relays are only returning payloads that have the the root of the transaction tree.So they withhold sort of the content of the transaction list so that the validator is not aware of them until later. The other thing that mev boost does here is it needs to be able to compare the proposals from all the relays it talks to and the local execution client and select whichever payload is the most valuable and instead it's that payload that it returns to the consensus clients. Great the consensus client receives this payload it puts it into a beacon block it signs the block. We have introduced this new call which is proposed blinded block so this is blinded block is basically what we call a beacon block which does not contain the transaction list of the payload and said that is just null and then but you know the signature and the header of the block and the header of the payload are all still valid. So it
proposes this blinded block back to the booth middleware which is then able to route that block to the right place. In this case it routes it back to the relay who has the transaction list and then it returns the transaction list back to the middleware and the consensus client so that the consensus client can then propose it to the network at the same time.The relay is going to propose that that full beacon block to the network and you move into the next step of the block proposal with the attestation and everything else. So yeah I guess there's quite a bit of cover here but the highlight is these two new modified calls. Right? Get payload header and proposed blinded block which are sort of inserted as complements to the current engine api. So great where we go from here we have been working on this. On the implementation of mev boost, here under flashbot slash mev boost
and we sort of detail what are the different implementation milestones and what's involved with them. We split up the development into four milestones right now.

The first one is really just about the basic logic that's required for mev boost to be able to communicate with various relays and be able to propose payloads to the consensus clients and it also involves sort of the support by consensus client for these blinded blocks.So I highlight sort of the behaviour and the client modifications here but yeah the the consensus client basically the only change that's required to be compliant with this. This milestone is the ability for them to accept the get payload header calls and then return a blinded block from them. So shout out to the lighthouse team, they have been super proactive. Paul and Shaun at helping implement and provide feedback on this initial setup. Our goal right now is to have that ready for whenever consumi goes live to understand where we are nearing in a few days. So it will be super exciting to have live and get some of the members of the flash bots.Youtube working group. Also set up to run this maybe  for contacts if you weren't aware flashbus has set up this. This working group with various different validator teams and solo validators etc and in the community to provide a forum for discussion on both the design of boost collaboration on testing of the system ahead of the merge. So we will try to produce some package for them to get set up with that boost and I guess whatever clients support it for
for kintsugi. Yeah the other thing that we have ready is a merge mock implementation that supports. This milestone one so that's the demo that we'll jump into just in a few minutes.
So great we have the basic logic but by no means are all the questions I answered yet so the milestone two that we have laid out here is meant to implement all the remaining critical components of the system and those involve security. So having a fallback in the case that
Mev boost  like crashes and fails over to be able to fall back to a local execution client authentication so that all the communication between that boost and the relays are using
signed messages and and everyone knows who they're talking to basically prevent dos and spam and then the third one is reputation. So even if you're authenticated with a relay you need to be able to tell if the relay  turns malicious or starts sending invalid blocks etc. So there's some logic baked into mev-boost that needs to be able to identify if a relay starts misbehaving and react accordingly. So the goal for these is to have them expected over the course of the next month and implement it by the end of January so that we can do further testing with those now.There are another two milestones here that are worth discussing I think we can probably skip over milestone four which is just about configurations optional. Configurations and optimization that various validators might want to run if they have different preferences on for example privacy or you know where they want to optimize for latency etc. So that can be sort of discussed separately but one of the main topics I think that remains to be figured out is privacy and by privacy I really mean validator ip obfuscation.
There is a design of the system that avoids revealing the ip addresses of the validators to the relays. But it requires a lot of work with implementing custom channels or topics. I am not sure what they are called with lib p2p and just from initial feedback from both validators and
client implementation teams.It seems it's not really such a concern for them. So this is marked as optional and I think we will be pending more discussion with the client teams and to see if it's worthwhile to put in the engineering cycles to implement this or not. So with that
said I think it's worthwhile to jump into a quick demo of merge mock connecting to mev boost and then I could start highlighting some of the other open questions that we have here and move into more discussion. So yeah let's see. Jason, do you want to try sharing your screen?

**Jason**: Yeah let me go to the world oh no you have to stop sharing first looks.

**Stefan**: Should we get it? 

**Jason**: All right can you see my screen

**Stefan**: Yes sir

**Jason**: Awesome, all right so  this is the mev- boost repository. I am just gonna start up mev-boost real fast. It's written in go.It's very straightforward. It's relatively simple as far as
implementation goes. Let's move over, so I am gonna run in three separate terminals. So in the first term I am gonna run mev-boost. Second term I am gonna run merge mock the execution engine for those unfamiliar with merge mock. It's just a very simple stripped-down client for both engine and consensus. It's meant for doing mock testing and integration testing. So I am going to  start that up and I am going to start the consensus client as well. Something worth noting here is I am doing one extra flag here which is I am pointing the engine  at port 1850 that's where mev boost is running. So instead of how this normally runs? is this communicates directly with the merge mock execution client or with you know a geth or whatever execute clients in our case. We are instead communicating with my oost directly. Let's go back to mev boost logs and we can see it's successfully getting the payload
header and it's revealing the payload in the proposed blinded block call. So if you refer back to the charts or the documentation that Stefan showed earlier. We are no longer calling geth payload. We are calling the geth payload header and then in a second step, the consensus client will fetch. Well send a blinded block and then fetch a full payload back from mev boost. There's some areas here you're seeing. It is not actually communicating with the relay at all. This is only communicating with the execution clients. So for the purpose of testing mergemon, this is great right. We see it working exactly as it used to with the merge box execution client and I think we have plans to provide more extensive testing on the relay side
as well. We will  probably provide a mock relay to run locally as well but for this consensus client implementation purposes. This should be more than enough. You should be able to test the get payload and propose blinded block endpoints that's pretty. It's not much for a demo. Honestly it's just showing that it is working and showing that we are testing it with some clients.

# 2. Milestones & timelines

**Stefan**: All right, awesome. Okay cool yeah I can go back to share my screen and yeah we can sort of open the floor up for the discussion.I think yeah we can either talk about some of the remaining design decisions for this milestone and have a discussion about that or yeah maybe let's do that.I will just list these.I will list these open questions and these are all things that we are looking for additional feedback from. Feedback on them is currently sort  of underspecified right? They are mostly ideas and proposals but hopefully they will  move to being much more concrete over the course of the next few weeks.So yeah the first one is this validator ip obfuscation.There is a proposal for how to go about changing the way that messages are passed around and make sure that basically it's one-way communication
between the validators that send basically messages to the relays and and the rest of the network and those can be done over over peer-to-peer. But it doesn't really address the relays when they communicate messages to the validators, in particular. The most important one is getting the payload header from the relay here. So it's kind of a silly question mark on how to address this and the feedback that I have gotten is that it might not even be worth too much hedge scratching here because ipdn randomization still is an issue regardless. So the option two is just let the validator deal with it. If a validator is quite sophisticated, it should be somewhat trivial for them to insert a reverse proxy around their mev-boost client or like run mev-boost behind some kind of protection that even if it falls over it doesn't affect the rest of their infrastructure that's how miners are operating today. So I am just assuming that would be reasonable for validators to operate this way as well and the other option is if they disagree with this approach then they don't necessarily need to run mev boost at all and they can just fall back to running their clients the normal way without all this mev stuff. So that's one discussion topic another one is fee recipient authentication. So there needs to be a way for the validator to communicate to both relays and block builders. So looking at this the further needs to be able to communicate the relays and block builders, what fee recipient it's
going to use it. In the first milestone what we're doing is, we're using the fork choice updated call and sending that over to the relays to communicate that but ideally we wouldn't rely on this and it would be possible to just have some. Some authenticated message that mev-boost is able to get from the beacon clients that lists all the fee recipients that are associated with the validators that the leaking client is representing. So you know if the beacon client has like a thousand validators running behind it on startup or on connection boost would be able to request, hey give me all the fee recipients for all your validators.The beacon client would then request from each validator node to sign a message and then submit that back to mev boost would then submit it to the relay and the relay would make it available to the rest of the network. That's kind of the way that this proposal works right now.

**speaker 1**: Just on that does it make sense for a battle that is using eth1 credentials but it makes sense to just use that address.

**Stefan**: So you're talking about withdrawal credentials.

**Speaker 1**: Yeah

**stefan**: Maybe the problem is I would require that withdrawal address to collect all the fees for like transactions and mev and like even the block rewards.I guess not in e3 and in proof of stake. There's no such thing but certainly the transaction fees and the mev that would be where like all the fees would go.So perhaps if they're comfortable with that then yes I think right now the fee recipient isn't limited to being the withdrawal key.

**Speaker 1**: Yeah so there's no way to upgrade currently. So it's not the full solution but potentially becomes one. Yeah that's cool, thanks.

**Stefan**: It is true that I think even if the view recipient is a withdrawal key, you're not limited to withdrawing and so withdraw that value before stake withdrawals are implemented
because I guess.Yeah  the idea here is that it would be possible but not required right for the withdrawal key to be the few recipients. So the validator can pick whatever address they want.

**Speaker 1**: Okay so why do builders or searchers need to know the specific fee recipient. Can't they just use the coinbase opcode.

**Stefan**: So the fee recipient is what goes into the coinbase lab code but actually this
is a really good question. So the builders because the coinbase opcode is a part of the header and can be accessed through edm execution. It also creates a code path that switches based on the coinbase address. So when the builder or the relay are processing
their blocks in order for that block execution to be deterministic. They need to know ahead of time what is the address that's going to be used in the coinbase. So there's two ways to go about that one of them is like the validators communicates the fee recipient and then the builder like includes that as the coinbase address of that block and  submits that through
or the alternative is for the builder to set their own address as a coinbase address and then at the end of the block that they produce. They just have a simple transfer from the coinbase address to the validator address for the value of their block that they want to pay. So either of those sort of approaches should be possible and they remain the property that throughout each step the block is fully deterministic.

Okay cool next point is around execution client block value, so one of the key objectives really of this system is to enable profit switching between the payloads produced by multiple different relays as well as from local execution clients. So this step here right this logic where mev boost compares the payloads it receives and selects the most valuable one really requires some indication of the value of the payloads. So the geth payload header call and the like geth payload call need to be able to
return an extra field that says this block contains like x eth of delta in value for the fee recipient that is defined. So sort of talk about it here but that message needs to be returned in a way that boost is able to compare these different payloads. Just like the most valuable one and submit it and like a further enhancement would be for this call to include some kind of miracle proof on the balance change which would provide potentially further guarantees. The tricky thing here is obviously it requires some changes to the engine api and particular changes to the data that the execution clients expose. Next item here is fraud proof because the relays are not including the list of transactions and the header that they provide to the validators. The validators are signing blindly right and they just presume that the relay is proposing a valid block that's okay from the network perspective because once the full block is revealed it's still up to the attestation committee to actually validate if the block is valid and so the network will never finalize. An invalid block but it does cause the validator to lose the value that it could have received from both the mev and the reward for the  block proposal  and it basically just got a miss slot in the chain. So you want to have a system where other
validators can notice. So let's say you know this is the path that's taken you get a bunch of transactions all the relays propose a block to the validator here. This is the boundary of slot one, this is the value of slot , two the value of slot,  three slot four you know if the validator receives an invalid payload from the relay and submits it to the network you want the validator number two to be able to notice. oh wow like this really proposed invalid payload even if he sends me a payload for my slot. I am going to ignore them and just switch to using the other relays. The way to do this is using sort of this fraud proof message so because all of the relays and all the validators are listening to leia's state of the beacon chain,what you need is the validators to be able to communicate back to all the relays. Hey here is the payload that I received from relay one this is the one I decided to include in my block. I can prove it because they signed it and then all the other replies are like okay now we can validate to see if this payload was correct or not. If it's incorrect what they want to do is send this fraud proof message to validator number two that says hey look we really number one. Proposed this payload for this block height.You can see that it was invalid because you can
like see the state of the beacon chain. For that block height therefore you should no longer accept payloads from this relay. So this fraud proof system is sort of what keeps the mev-boost protected. Sort of automatically from relays that turn malicious but it requires further spec because there's likely to be some modifications to the way that it validates those payloads,  both with the local consensus client and with the local execution clients to run smoothly. There's a few approaches to doing this so it's worth sort of calling out as one of the remaining discussion points. Okay if you're still there if you're still bearing with me, the final one is splitting away the execution payload call. So one of the components I mentioned in  milestone two here is security under this description. The beacon client is only  communicating with the local execution client through mev-boost but really what you want is a situation where if mev-boost goes offline for whatever reason has some software fault, the beacon client is still able to operate all those duties by falling back to communicating directly with the execution clients. So this is just about making sure that this exists in all the beacon nodes. So you have that level of redundancy. If there's a complete system failure and yeah  that's all the discussion topics that I have listed some resources down here and some notes that Paul has put together. While we were iterating on the work that we have so far, so
definitely great german to check those out. Cool thanks.

**Paul**: Yeah so I am Paul from lighthouse. I have mentioned a couple times, I have been
working with flashbots on it. I  thought maybe I would just talk for a little bit about what I have been working on with it. So I have been online as a developer of one of the consensus clients, so I have been trying to get involved with flashbots to just make sure that this can be as safe as possible and that we can also maintain the concept of client diversity. So we are kind of when we bring in something like media boost flashbots. We kind of become at risk of centralising upon this thing not necessarily from like I don't like a governance perspective but more from like a piece of software that can fail and take everything down. Sort of perspective
so the designs reflect that now something I have been trying to make sure is that we have  the ability to fall back to the local execution node. You know nevermind geth whatever if things stop working and also what I think is very important as well is to not rely upon any of the boost for verification validation of payloads.So they'll give us a payload and we always verify it with our own node so that we can basically stops immediate boost from being in the position where we can finalise completely invalid transactions and things like that.So that's kind of what I have been working on as well is trying to make sure that it's multi-client compatible from a consensus client perspective. so try to make it so that it's easy to implement to consensus clients and make it so that there's a clear path to doing that. It means that we can get all of the consensus clients that are interested in implementing it. I can get them on board with a pretty low barrier to entry so that we don't end up with a scenario where you know if you want to run any of the boost you need to run some client and therefore we will skew the network. So yeah it's been great working with the flashbots team  looking forward to being involved more yeah and if anyone especially from the client teams have any questions or want to talk about it. My door's always open.

# 4. Q&A

**Stefan**: Thanks, Cool any other thoughts / questions?

**Speaker 1**: What's the best way for folks to reach out to the flashbots team as they are starting to look into this and like to have questions and what not.
**Paul**:  Yeah good question.So there is a channel on the eth r d discord called block construction under execution r d. I am almost always keeping an eye on this thing for any messages, so if you need to reach out to flashbots you can just add the ghost up there and I will see it. Thanks Lucas for his hand up.

**Lucas**:  Yeah I have a question. So as mev boost is kind of this middle layer that between
something that produces a block like an execution engine but we still have an execution angle to fall back to. Right? Would it make sense to like bundle it with an execution engine
processes like for example never mind have this plug-in ability. Would it be good to have a plug-in for mev boost that would think. So the next thing with the execution engine can have
a look at the current state of the network from the execution engine perspective as well as communicating to the river.

**Stefan**: yeah I think this is kind of like an open question of how deeply can mev boost be integrated with  both the beacon nodes and the execution clients. We have tried really hard to comply as closely as possible with the way that the engine apis work today. So that it's
like cross-client compatible by default that being said. I do expect that there's some advantages to having deeper integrations. We haven't spent that much time looking into it. To be, we have just been focused on how to make this thing as stable as possible and broadly compatible as possible but yeah I do expect there could be some advantages to integrate further.

**Lucas**: Yeah the beauty of it is abstract so it can be integrated in the exchange so that's the idea but the integration part is still part of the question. Maybe there are benefits to them too.

**Stefan**: Right like you definitely could.  I think implementing all of them mev boost logic as part of a module on nethermind right, probably and then you wouldn't have this like other pieces of software that's running in between. You would just have the execution client that's also talking to our relay and it ends up looking much closer to the way that mev geth is sort of architected but you do like to remove the need to have this other piece of software. So client teams want to explore that and just replicate all the logic. I think that that's something interesting to look at. Any other questions or comments?

**Speaker 2**: I have some. How can we make sure that the builders and the relays are not the same person? I think if you like if you run a successful relay or like if there's a cost for validators to like be at multiple relays in terms of whatever setting it up,bandwidth whatever
then they would probably only go to a couple and like how can we make sure that those
relays are not. 

**Stefan**: Yeah that's a really good question. So I can say how I sort of expect the industry to work around this and respond to this. Yeah let me talk a bit about this. So I think as everyone here is aware, not all validators are sold validators. They are running both their validator client they're making clients and their execution clients but in practice there are some individual stakers who do this. You know a big chunk of the proof-of-stake network right now works by either people running their own validator client but then outsourcing the beacon client and the execution client to some infrastructure provider or you know pooling together and staking pools where they don't control the value of their client either. So there's sort of an industry that's propping up around various different actors running different segments of the system. Even solo stakers who are running about a client and beacon client
are still outsourcing their execution clients and fira. So each component is sort of set up to be bundled together with each other in a way that provides a service that might be interesting to some users. I do expect somewhat similar things to occur in this level of abstraction. So while there will be builders who just focus exclusively on building because you know that's where they have their core competency of being able to merge transactions together being able to find some mev and produce blocks with it. There will be others who say. Yeah we don't want to trust a third-party relay, who you know will see the content of
the blocks that we produce and so we would rather be able to just communicate directly with validators and so they will try to run their own relay as well and get as many validators as possible to sign up for their relay. Similarly I do expect that some of the large validators will say well you know we think it's a big risk for us to sort of trust all these third-party relays. So we would want to also run our own relay such that we can like see the content of the payloads before we sign off on them and we are able to validate them and so we don't need to worry about this you know, this fraud proof mechanism but instead we can just sort of operates very similarly to the way that mev gas operates today where you have full  information and you can just sign off on blocks but it's really probably only going to be the large validators who do this and you know an example of this is ether mine who has been running um you know in the proof of workland both the relay and and their miners. So the I expect they'll probably continue to do this but there will also be these sort of individual entities that are incentivized to run relays so within the flashbacks working group right now. There is three entities that I have indicated so I am interested at doing this so one of them
is blocks routes who are currently running a relay for the proof-of-work version. They will continue to do this here. There is a consensus that's indicated they perhaps want to see if this is a product that would make sense within pure and then alchemy as well have indicated some interest in exploring this, so I do think there are some entities like those whose you know business model is very much, so on being an infrastructure provider whose role is quite fitting to run. This really infrastructure you know when you think about what running a
relay. Really it's opening up some endpoint to like as many people as possible as many users as possible to receive a bunch of different block proposals. Doing some highly scalable stimulation of these blocks and verification of these blocks filtering out all the garbage and then only submitting you know the best ones over to the validators. So that's pretty similar to a role that infurer does right now. You know receiving a bunch of transactions from users and then only submitting the ones that make sense to the transaction pool.

**Speaker 2**: And another thing, so regarding the issue that we need to know the value of the payload produced by the local execution client if we have a standardized format for paying the block producer. Okay now that doesn't do well like the  mev boost knows the transactions right. so if we had a standardized format to create a transaction that pays the fee recipient and put it in then. We would know how much someone would be willing to spend and so we could gauge mev based on that.

**Stefan**: Yes that's right actually I will shift over to here, I mean I have one line on here that describes it but it's something that's worth talking about.There's a slide on on milestone four that says consider adding merkle proof of payment. You know to shift verification requirements to the relay. So basically what this means is instead of leaving the option for the builders to set their own coinbase address or you know use the fee recipient of the coinbase address it would say. Okay no builders always set their own coinbase address and
They include a transaction at the end of the payload that pays the fee recipient and then what they can also do then the relay, can produce this proof that  transaction was included and has you know the right precondition on the balance of the builder to be able to complete the payment to the  fee recipient. So this would involve you know standardizing the way that the payments are made and then you can create this proof that the payment was included  and then attach that to the header to the payload header when it's communicated to mev boost and then in theory the execution client can do the same. You know I think if there's
a way to avoid this level of deep constraints and like remain maintain the ability for the builder to set whatever they want as a coinbase address. Simply say you know this is the change in the fee recipient balance and have that be sort of self-standing without restricting how the payments is made then that seems ideal in my mind because it's less restrictive.

**Speaker 2**: Yeah but it adds like some complexity to block building and two it also adds complexity to people that are not using maybe boost right because they have to opt into this
to the same api. I would be okay with having this as an optional field in the payload in the geth payload object but not having this required.

**Stefan**: Yeah I think that's fine. Yeah it seems fine for it to be optional for any other questions or comments.

**Speaker 1**:  I have a minor question about the last chapter, like a proliferated proof message. What would happen if Elijah is not revealing  the block at the end of all this interaction validates risks to just miss the slot right.

**Stefan**: Correct yeah so in this initial post right that describes this architecture. We list three ways that a relay can misbehave. First one is just producing a valid payload. Second one is misrepresenting the value that the payload has and then the third one is missing data. So just never revealing the transaction list. So there isn't really a good way to do a fraud proof for that right because it's just based on timing. You know I really can claim that the message came but just too late and I can just stall it out or or whatever, so I think this can be much more subjective. Maybe it has to be like a statistical approach where you know if a relay misses more than x number of slots within you know y amount of  block proposals then it becomes disabled that's my idea. I am wondering if yeah what do you think of that.

**Speaker 1**: Yeah thank you. Yeah I think it's going to be solvable without a complete chain. Maybe some complicated mechanics but it would complicate things but yeah it's still like a possibility of attack.This kind of not revealing the payload in the end of all interactions but yeah I think that good relies it's not interesting in twinsies. 

**Speaker 3**: I had a question kind of based on what you guys just discussed so you mentioned disabling malicious relays so who controls.Like what's a valid relay or not? like is there a master list of active relay that's controlled by whom?

**Stefan**: So there isn't  the way that it will work, basically the validator, when they start up mev boost. They can define a list of relays that it wants to connect to and so the validator is always in control of which relays it. It wants to communicate with something that we've discussed in the past. Does it make sense? There's always a question of  what
are the defaults right.There's a  default like no relay does it default to a single relay or does it like default to outsourcing to like a list that exists somewhere. We haven't really decided on this. I guess that's open for discussion, something that might be useful for solo validators is. I don't know if you all are aware of tokenless, if you use uniswap right like instead of uniswap
coming up with a list of valid tokens. You know the ones that aren't malicious tokens and making a decision themselves.They allow for like any third parties to submit a list and like maintain their list of tokens. It could be a similar system here where the validators can delegate to a third party list that's curated by, you know some entity that carries some reputation and who focuses on exclusively verifying the activity of the relays but really the goal is for always maintaining the ability for the validator to define which release they trust.

**Speaker 3**: I guess that makes sense, it just also causes a potential problem. If you are trying to punish  malicious relays but really it's a permissionless system then they could just probably find another way to get back on a-list or whatever obviously it's more difficult.

**Stefan**:  Yeah, it relies on this reputation so if the relay does something malicious super malicious and then they go offline and spring back up with a different identity. It's kind of up to all the users in the network to try to identify if the user is using a third party to do this reputation check. Then you would hope that that third party would be able to identify that too. So it's certainly a risk. I really could attempt to go. This direction but I expect over time as they build reputation that's sort of a sub cost and they aren't necessarily incentive bias to evaluate that.

**Speaker 3**: And like the remedy or or fallback mechanism for a potential I don't know mass denial of service attack against relays. Like obviously at some point that's just disabling mev boost but  is there any other way to do that or like the ip's not even exposed.

**Stefan**: Definitely the fallback mechanism if all the relays go down is like mev boost still talks to local execution clients and is able to produce blocks that way.

**Speaker 3**: Yeah, if every single one really goes down. Yeah but like if  some go down and then the ones that are around just get bad blocks that's kind of like I am imagining it. Yeah so you could have like an extended period. Let's say all the relays at the same time start producing bad blocks then you would have a cycle where validators one by one disable the relays right and so maybe just thinking about it the longest amount of time that the chain would go. Is the number of  relays enabled by all the validators? So ideally you have validators that all have a different list of which relays they trust and then you have a bit more diversity there.

**Speaker 3**: You don't want maybe an overlap between all of the shared relays.

**Stefan**: Correct but yeah worst case scenario I think that's the block. The chain misses the number of blocks equivalent to the number of relays after militias.

**Speaker 3**:  And are relays able to provide malicious blocks as opposed to just invalid blocks. So when they get something from the builder that is full. I don't know how to say it fully, sorry. So obviously they can either like not responding with a block which is the same thing as responding with an invalid block. But is there a possibility that they basically respond with a block that's  not been built by a builder and they just come up with their own thing and it's like a bad block in some way.

**Stefan**: Yeah so I can dig into like the three ways that I really can sort of do something bad. So the first one is just like it tries to send whatever a transaction from somewhere that
doesn't make sense or like just contains some you know some logic that doesn't work like the  header is formatted or something like that right? So the payload can just be invalid another one is like inaccurate value so something that a really could do is you know the block that it's actually producing has one each worth of value that's being paid to the validator but they claim that there's geth worth of value and so you know they can basically guarantee that they win the profit switching here even though the block that they produce wasn't that valuable. So I say that's probably like a clearly malicious thing that wouldn't happen by accident is over reporting the value of a block. So I am wondering if that's what
your question is.

**Speaker 3**: I had to step away for a minute to get a computer that arrived at the door but I posted a question in the chat. Did you guys answer it already? A couple of us were wondering, we were chatting on the side of relayers incentivized separately from the builders.

**Stefan**: so it's not defined within the system. You know actually neither is the builder compensation, I sort of propose the way that I think builders will likely want to monetize which is they set their own coinbase address and then they like have some payment and they can keep some delta between the two and still their incentive is to pay the most that they can because they're competing against all the other builders and producing this. I expect relay's business model to be more fees oriented so if we just think about how blocks route operates today right.They have a fee per number of messages that it inputs  and  you know obviously infuria and alchemy have a similar system where they just charge by api calls. So I expect those to be the  likeliest monetization routes for the Relay.

**Paul**:  Is it possible for the relayers to take some cut of the deals that they pass them through so that they're competing in price discovery like the builders.

**Stefan**: Maybe though I don't see that being super stable like basically would require adding additional transactions. Somewhere where they really would say you know we only accept blocks from builders who like pay us within the block that they produce and then they would like then for the payment on by adding their own transaction at the end of the block to
the validate year so it could be doable feels somewhat less likely to me but it's a possibility

**Paul**: Okay alright, thank you.

**Tim**: I was wondering what it is that's missing right now that makes us need the relays in mev boost but we won't need them later when we have the full pbs.

**Stefan**: Yeah good question, so we had a discussion last friday where Vitalik presented pbs and the properties that it has. So it's called mev boost. Maybe there's a way to surface a link to that but I definitely recommend checking out that talk . What you need to remove the relay completely from the system is the ability for the value to accept messages from any builder and to do that you need to have unconditional payments attached to a payload. So right now the way that it works is the builder creates a payload and submits it through. But if the payload is invalid right, if the payload reverts for whatever reason the validator doesn't get paid but under to have all the properties that you want to be able to remove the relay, you need to have this be completely independent where even if the block that the builder proposed is completely invalid and reverts or like just never gets accepted the payment from the builder to the validator still settles and that creates sort of the counter incentive for builders to produce valid blocks. It prevents the dos and spam issues and then you can handle basically making sure that you continue mining on the ballot chain by updating the fork.choice rule of the chain. So that's how pbs sort of handles this issue.

**Tim**: Anyone else. Okay well yeah if there are other questions comments as people look into.We mentioned earlier the block-construction channel is the right place to discuss this. Thanks a ton to the flashbots folks for coming on presenting this. Yeah agreed with the comments, this was really helpful and yeah thanks to everybody else who attended and asked questions and yeah I guess we can wrap it up. We will have a recording for this and I Will share it on the discord as soon as it's ready. Awesome thanks everyone thanks for the really great questions. Yeah looking forward to chatting some more on all of this.

 ----------------------------------------------------------------
## Attendance

-  Mikhail Kalinin
-  Tim
-  Pooja Ranjan
- Chi
- Charles
- Keenan
- Francesco
- Somu Bhargava
- Piper
- Micah Zoltu
- MariusVanDerWijden

## Next Meeting Date/Time :.TBD

## Zoom Chat

00:08:00	MariusVanDerWijden:	Why not create a new network protocol (like eth/snap) which is optional for nodes to implement 

00:08:19	stokes:	that could be useful @marius

00:08:21	MariusVanDerWijden:	Only for historical data, and modify eth to not serve it anymore

00:08:57	stokes:	would you worry about LES server type problems where there aren’t enough nodes seeding this new p2p protocol?

00:09:41	protolambda:	@marius, and then special nodes implement that historical data protocol? Or who serves the historical data then, if it's not stored by default?

00:10:31	MariusVanDerWijden:	Yes, so maybe portal nodes to implement this and/or make it optional in the normal clients 

00:10:58	MariusVanDerWijden:	But yeah the LES problem will be there for all ways to store it

00:12:41	MariusVanDerWijden:	10mb for network

00:13:01	MariusVanDerWijden:	2 mb with current gas limit

00:13:46	charles:	What are the implications of the calldata size expansion on block propagation? Is it negligible?

00:13:49	protolambda:	1,875,000 absolute max burst per block today (from EIP 4488 background)

00:14:08	protolambda:	https://eips.ethereum.org/EIPS/eip-4488

00:14:19	Keenan:	Is there a reason the clients can’t specify their own limits on historical data?

00:14:53	stokes:	why would you not pick the smallest amount

00:15:01	protolambda:	@Keenan, serving one snapshot is easier than serving many of different time windows

00:16:34	stokes:	@charles, idea is to not mess w/ call data unless the effects on prop are negligible

00:20:32	Mikhail Kalinin:	At 2mb MAX, 1mb target it’s gonna be up to 2.5Tb target per year. Ofc, it depends on the real block size, which is about to grow if rollups utilize calldata. Current block size is under 100Kb

00:21:56	MariusVanDerWijden:	Should be pretty easy to fork geth for that

00:22:12	Pooja Ranjan:	Piper would be joining shortly!

00:22:23	MariusVanDerWijden:	We hope so, but we haven't really discussed it yet

00:22:32	stokes:	and *ideally* it doesn’t become just a thing where geth is the only client that can do so

00:22:47	MariusVanDerWijden:	No, not very soon

00:23:14	lightclient:	gm piper

00:23:19	stokes:	gm

00:23:42	Piper:	morning

00:23:49	MariusVanDerWijden:	We will not support 4x4 before there is a good mechanism to retrieve the data

00:24:31	MariusVanDerWijden:	If you have the headerchain, and trust it, you can verify the blocks without executing them

00:24:37	MariusVanDerWijden:	Blocks + receiots

00:24:55	Mikhail Kalinin:	State should be recoverable from blocks

00:25:31	MariusVanDerWijden:	Blocks, receipts and snapshots at specific points (e.g. all historical forks) would be great

00:25:39	stokes:	state snapshots?

00:25:46	MariusVanDerWijden:	yes

00:26:06	Piper:	where are we talking about serving these from?

00:26:25	stokes:	no where yet

00:26:27	stokes:	@piper

00:33:11	Marius Van Der Wijden (M):	I would prefer having them accessible by hash

00:33:22	stokes:	does the hash need to support some kind of proving scheme tho?

00:35:03	Mikhail Kalinin:	If you have a hash of accumulator onchain you can build a proof of a block existing in the canonical chain and verify this proof with the recent state

00:36:04	stokes:	my model of this is that you already trust the archive snapshot you get

00:36:26	stokes:	or at least have simpler ways to authenticate

00:36:30	stokes:	its worth more brainstorming use cases tho

00:37:31	stokes:	ssz list!

00:37:46	Mikhail Kalinin:	> my model of this is that you already trust the archive snapshot you get

00:37:58	Mikhail Kalinin:	you’re about to check them or not?

00:39:53	Mikhail Kalinin:	I mean you will execute these blocks and will be able to verify the state root, you may check PoW seal as well. no additional proof in advance that the block is canonical is required. This is what you mean @stokes?

00:45:55	stokes:	i think my mental model around the trust model is evolving as this call goes on

00:46:05	stokes:	no further comment rn @mikhail

00:49:24	Marius Van Der Wijden (M):	bootstrapping torrents will not be an option for us. we will only drop history of there's a reliable and decentralized way to get blocks

00:49:35	Micah Zoltu:	Torrents are decentralized.

00:49:55	Mikhail Kalinin:	Do we want to provide any guarantee that this torrent won’t disappear 6 months after? EF and other authoritative parties serving this blob of data may be this kind of guarantee

00:52:54	stokes:	i think the vision is that we will always have altruistic players in the ecosystem who are seeding the data

00:53:33	lightclient:	if geth won't stop historical data with the torrent solution, i think we need to rethink our approach

00:53:43	lightclient:	pretty much a non-starter imo

00:53:50	stokes:	that’s what we are hashing out now lightclient

00:55:00	lightclient:	poap

00:56:28	Piper:	fair, torrent is explicit opt in

00:57:21	Chi:	not that torrents aren't reliable or not decentralised, it's that it's *not* the Ethereum protocol and therefore not controllable. *theoretically* possible to lose entire chunks of historical transactions. say bittorrent dies, and ethereum continues?

00:58:01	Micah Zoltu:	Bittorrent is a protocol, not a centralized thing.  So anyone who cares about keeping Ethereum alive can keep this data alive as well.

00:59:56	Chi:	Eth Portal Network is the solution. Needs to happen asap, and telegraphed to the dapp devs that this is the way.

01:00:18	Mikhail Kalinin:	Right. I think that if EF, Etherscan, Infura, and other authoritative players saying that they are storing this piece of data then it should be enough of a guarantee. Altruists can make it more reliable and available.

01:00:39	protolambda:	This EIP is trying to solve 3 different problems, which I think should be split up:
1. Standard import functionality for historical blocks, receipts, headers, state from storage.
2. Standard method of distribution of data
3. Removal of serving historical data as eth1 node

1. Is super valuable already, enables experiments with data distribution.
2. Many ways. As long as it can be imported into the client
  2.a. Torrent or something out of band
  2.b. Portal network
3. Relies on good execution of 1&2 to warrant, although some clients already do it (like not serving receipts). 
  Marius: geth will/should serve the data until 2 is done.

01:00:41	Mikhail Kalinin:	Erigon may want to serve this data as their sync model is to execute all the blocks since genesis

01:01:57	Mikhail Kalinin:	have to go, thanks everyone!

01:02:02	stokes:	thanks for joining!

01:02:06	lightclient:	c ya

01:04:04	charles:	thanks everyone :)

01:04:18	Marius Van Der Wijden (M):	cya

01:04:31	Chi:	thanks, really good
