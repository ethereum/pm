# Ethereum Core Devs Meeting 55 Notes
### Meeting Date/Time: Fri, February 15, 2019 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/77)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=NUz9_SpG84g)


# 1. Roadmap
**Hudson**: Thanks everybody for joining and we will get started on Agenda. 


## 1.1 Constantinople
### 1.1.1 Ropsten fork / status
**Hudson**:The first one is Constantinople fork on  Ropsten network, how that went? and Status on Constantinople that is going to happen in roughly less than two week. Any one want to go over the particulars of that? Did anyone followed the Ropsten that day because I wasn't online much that day?

**Martin**: I can't say I followed much that day but from what I heard it, it went pretty well. The only thing that would concern is consensus issues, small amount of miners and stuff like that but interesting.

**Hudson**: Great, any other comments on the Ropsten part of the fork? Kovan network have done their Petersburg fork (to revert the Constantinople  effects), everything okay. One testnet has gone through that, I don't know Görli has any problem.

**Afri**: With Petersburg, we had some issues at block zero, but we are trying to get in there. Other than that everything is good.

**Hudson**: Okay, sounds good. Constantinople fork is coming up in less than two weeks. I know that the plan for the CatHerders is to start reaching miners probably a week ahead. We are also going to stick some reddit thread, some twitter reach out to people to let them know whats going on. We will also be posting a blog post on Ethereum website. Thats what I plan on doing. Does anyone think that we need to do more than just trying to let people update. Is there any client side stuff that we need to work on?

**Martin**: I am going to update to you if I have some better information.

**Hudson**: Okay Great. Anybody else?

**Danny**: Is fork monitor running?

**Hudson**: Like currently,is it running? 

**Martin**: Yes Fork monitor website is running and has information of couple of clients. It will be updated.

**Hudson**: Sounds Good. I think we are all good on Constantinople. 


## 1.2  [CREATE2 side effects for education](https://github.com/ethereum/pm/issues)
H: Today, Jason Carver and Jeff Coleman wanted to talk about CREATE2. There is recently some article is put out and there is misinformation in the community that there is a bug found in the  Constantinople and it will be delayed. That was because there was an Augur prediction market to say that there is going to be a Constantinople delay, the fork would be after the 27/28 February. The cool thing about that is because the block time is variable, there is not a good way to know about it until it is closer and it gets more accurate when its closer. Its kind of the tricky prediction market but it cannot be said it is delayed because of the bug. So people are kind of nervous because of that. There are some things that people doesn't realize that they are going to happen because of CREATE2. So, we start with Jason, Jeff will come into with his perspective and then will have other peoples.

**Jason**: Sure. I am not going over the issue itself just this idea that Create 2 allows contract to be redeployed after selfdistruct. Things are a little tricky about redeployment, basically known by the EIP author. We need to work on writing up article, letting community know about it. Most of the people that I talked about didn't notice that it was coming and  there it was - SURPRISE ! The idea is a bit more difficult to think about how contracts work. It's definitely something that you can learn your way around, but its not right there right now. 
I can think of two options that make sense:
1. We need to educate people a lot and a lot quickly. 
2. My instinct will be to remove that without else being knowing that and do the fix but thats way up and there is the deadline.

**Hudson**: Jeff , comments?

**Jeff**: I think some education awareness is to be made around this. I think a lot of people are not familiar with the whole thing what CREATE 2 can do. I think, we definitely need to do a better job in communicating out. Like to get some more information on Twitter or Reddit and things like that. I might end up writing on it. I think, Jason has done a good job on emphasizing that we need more on kind of tutor things on Selfdestruct. I think I can broke down to tutorial for it.
1. When we look forward, how are we going to be handling state and storage and all that. I know there are a couple of cases where it has to be used. My recommendation would be nobody should use the SelfDestruct right now. 
2. Emphasizing that init codes are really important. Theoratically redeployment can change the contract byte code because the address has to be in the init code and not. Definitely people needs to be aware about that  init codes are part of it and non-deterministic approach are a problem.
I think these are the two messages that I really wanted to get out there. 
On the question of whether there is something that could be pulled back, now that this is pretty late begin. Given the niche impact of this, I don't think people who are writing contract are looking to make them auditable and hit impact like this, just don't use SelfDestruct.
Jason has created and is working around CREATE 1. Create 1 has this great assumptions around address.  The solution that I can see right now around saving the data that are being lost is to keep this extra data around state tree. Going forward, I think its really a bad idea as there are a lot of assumptions that continues to break down. Looking at the starting proposals of how we make the stashing and retrieving storage, and looking the things like generalizations, that kind of shock, all of these things are going to be changing with assumptions. When we look forward, what we want would be contract based addressing of contracts and not just order based addressing which is CREATE 1 is. So be in the place of standard getting CREATE2. Obviously looking through that sort of the things as a place where we can get you, I think that having CREATE 2 in its current form is the best you can do.       

**Hudson**: Do other people have any comments on that?

**VB**: I think the one thing that we needs to keep mingling in the future which is when we start thinking about  rent and delusion and thats a way when contract can go from being the the state to being not in the state without a selfdistruct operation. So, we need to be careful to either just disallow, basically require creating a contract at that point to have a mobile proof or proving that it didn't exist before. Some other schemes that prevents the contract from being popped as contract that exists. Thats not something the we need to take care in next couple of weeks but still useful to keep in mind specially since we are trying to get the Eth 2 sharding phase 2 VM spec starting very soon. 

**Martin**: This whole discussion started two years ago. What we really should do in my opinion is to take these discussions happen whenever these happens and put them in a condensed form like security consideration discussions. If this information is spread out over EIP discussion and fellowship discussion, it might be hard to find out. I guess this is the reason that it is re-found again and again.

**Hudson**: Its a great idea. Anybody else? Thanks Jason and Jeff.

## 1.3 ProgPoW Audit
H: For ProgPOW audit. The CatHerders and the related parties have been looking into ProgPOW audit. Here is the latest on that. 
* We've found a company to do a series of benchmark testing.
* Some of the sticking points for some people on the space was that it wasn't clear that if AMD or Nvidia card will be getting a performance boost unfairly based on ProgPOW being implemented. This benchmarking will be some unbiased scientific marking on the cards to make sure that ProgPOW works similar across all of them. 
* The problem that we are having is finding a company that will look at it and provide estimate about time and budget for  ProgPOW to be created, what people will have to do and some other stuff that we are interested in getting information to community to make a decision on whether or not to go forward with it. We are having trouble finding those auditors. If you know someone interested in this, send them my way. 
* We are having the trouble finding right set of people because people who are primarily the experts have conflicts of interest because they are in ProgPOW mining themselves whether that be GPU or ASICs. 
* I hope we find someone in next few weeks  and get started on an audit and get completed as soon as possible.
Any comments?

## 1.4 Reject EIP 1355 "Ethash 1a"
**Hudson**: Powell commented that he wants to reject EIP 1355 "Ethash 1a". The EIP that does reflect to make tweek to EThash to break the current ASICs. I think he is the author of that and he just want to reject it. Now that it is not useful anymore and he isn't here to really talk about it so we can skip the item. 

## 1.5 Istanbul Hardfork Roadmap
**Hudson**: Afri you want to take that?

### 1.5.1 Proposal Deadline May 17th
**Afri**: Not much changed from what we discussed last. The only question is that shall we delay everything with one month since we delayed Constantinople or shall we just with the initial timeline?

**Martin**: I think we should just proceed with initial.

**Afri**: Yeah: I tend to suggest the same. 

### 1.5.2 EIP 1418 State Rent

**Hudson**: Is is Alexey's thing?

**Afri**: Someone else can look it up?
If he is not around , will skip it for now.
H: I didn't see his comment before. So, Alexey is not here so we will skip the item for now. I know that he came out the other day with version 3 of State Fee Proposal. 

### 1.5.3 HF Naming challenge
**Hudson**: Is the HF naming challenge one on the Reddit where people are like putting a bunch of names to see bunch of HF name?

**Afri**: Thanks for bringing up. I almost forgot about it. I don't think its a problem of $10M (funny), so just avoid. 

**Hudson**: Sounds good.

## 1.5 Outlook: PoS finality gadget on PoW chain (Serenity)
**Hudson**: This item has been here for few weeks and I forgot who put it on and why? Does anyone remember?

**Danny**: Don't remember who put it on but it is something that community is interested in. I am interpreting that this has something with Beacon chain and to finalize proof of work chain. The main challenge in creating that is a viable Light client for Beacon chain, which is something that we are actively pursuing. This is technically feasible and we see it very much like something that community want. So, our intention is to continue putting the pieces in place that continues to allow to do that.

**Hudson**: Anyone else have comment on that?

**VB**: I would say generally not much of a worry for me from developers point of view. In terms of implementation eventually there are two possibilities that could be used: 
1. make a Eth2 light client inside of ETH 1 
2. we require Eth1 clients to hold the Eth2 clients. Its basically kind of merge mining.
I think it will be nice if we can make a Eth2 light client inside of ETH 1 but if not then other could be a possibility.

**Danny**: In the contract?

**VB**: Basically, one approach is the approach that doesn't really change the Eth1 consensus and the other approach is the approach that it does.

**Danny**:I am not sure if I am 100 % following the one that doesn't change the control.

**VB**: Oh! this is the one that basically stick to Eth2 light client inside of a contract in Eth1.
I am in process of writing up this light client and I think itr will probably take a couple of days. The one good thing is that the interface is fairly clean which is a 32 byte state which is just like the latest node hash and functions verifies the certificate of updating it.  Theoretically, once that function is done then you can show how feasible in it.

**Danny**: If anytime you update this transition function on to update this contract.

**VB**: It depends on what kind on update. Because it shouldn't be verifying the entire blockchain update but the bunch of global proofs.

**Danny**: Okay, cool.

**VB**: One of the things of relevance is that these light clients  certificates could potentially be fairly big in size. you can think of something like 500KB in every 9 days. In absolute sense it is very very small sense of load but in a burst sense it will be 10 times bigger than the current block size limit. This may be one of the things that we may want to think about in potential cost in Eth1.x discussion. 

**Danny**: Given that it will give the changing the consensus role, and you know group of people are watching. We could have  an exception for the state transition that involves payload contracts.

**VB**: I am not sure that it requires that much privilege. The only privilege that the contract would require is basically the rights to withdraw from the deposit contracts, if we end up wanting to make Eth2.

**Danny**: Differs the fork choice rule?

**VB**: Technically, we don't even need that risk of assuming neither system will get 51 % attack. 

**Danny**: I think we are talking about two different things, one is Finality Gadget and one is bring in something similar. Then we have two different goals.

**VB**: The purpose of the Finality gadget is the Eth 1 chain would be independent of Eth2 fork choice rule.

**Danny**: I think stuff like that are most achievable early than the other stuff like next step, in my opinion. We are pursuing couple of different paths. Any questions regarding that before we move on?


# 2. Working Group Updates
## 2.1  Ethereum 1.x Stanford Meetings Overview
**Hudson**: Already talked about it, unless anyone has to say anything about it. 

## 2.2  State Rent
**Hudson**: Alexey is not here, so we skip.

## 2.3  EWasm
No update since last the time

## 2.4  Pruning/Sync
No update since last the time

## 2.5  Simulation
Simulation team fly over to Denver, so not in the call.

## 2.6 Appetite for future in person meetings?
**Hudson**: Borris asked in the comment, should there be a thing for in-person meetings? We could start it later after some of the working group meetings but in general does any  one has an appetite for future in person meetings?

**VB**: Is this going to be an Eth1.x thing or anything similar?

**Hudson**: Eth1.x thing or either thing. Its Borris's idea.

**Greg**: I would like that. Most of you are Avatars and something that may not have anything to do with your name.

**Hudson**: Yup, that is true. Anybody else?? Its fine to have no opinions today, since this was just brought up but will try to organize one in the future and that would be cool.

# 3. Testing Updates (time allowing)

**Dimitry**: No major issues in clients passing its tests. All the tests are updated for a couple of weeks now.
The Trinity client has arisen an issue. There is a functional RPC protocol and test RPC protocol that are about to be discussed for implementation. 
It just goes with the direction of implementing test RPC matrix and will detach the testing object from cpp client as well. After the HF we will remove or detach this logic from cpp client.

**Martin**: We recently fixed a ticket and faucets are currently running back again.
# 4. Client Updates 
## 4.1 Geth
**Martin**: Not much update. We are going to have a big team meeting and will release bug fixes in next two days. 

## 4.2 Parity Ethereum
**Afri**: We just happen to came out of security issue and asking everyone to run Parity upgrade. 

## 4.3 Aleth/eth

**Hudson**: Anyone here to talk?

## 4.4 Trinity/PyEVM

**Jason**: No major update. 

## 4.5 EthereumJS
No one available

## 4.6 EthereumJ/Harmony
**Mikhail**: There are no major updates. Most of the work is on side of Eth2.0.

## 4.7 Pantheon
**Tim**: Working towards 1.0 already, implementing fastsync right now. We have release next week and official release in about three weeks from now.

**Hudson**: Which fastsync protocol are you using right now?

**Tim**: I think we are doing things similar to Geth. Danno might be able to provide much insight on it.

**Danno**: We are using the one Geth is. The future hybrid sync will also need this fastsync, so it gets us closer to where we want to be on. We wanted something faster, so we better get in sync with fastsync.

**Martin**: The future hybridsync is the one Peter has been proposing.




## 4.8 Turbo Geth
No one here.

## 4.9 Nimbus
No one here.
## 4.10 Mana/Exthereum
No one here.
## 4.11 Mantis
No one here.


# 5. Research Updates 
**Hudson**: Research update - Daniel / Vitalik

**VB**: Sure! Since the last call, one major piece of news is the first release of Phase 0 spec was made. It includes all the proof of stake parts of Serenity release. It doesn't include the Sharding specific bits.  When we made that initial release, we mentioned that a couple of features were missing where one of them was mandatory deposit ordering and the other is the Shuffling order. Since, the release is now about to go out, that is also going to be included. BAsically, Phase 0 is in the refinement mode at this point of time. Thats all from research side.

I have been starting 
* Sharding of data
* Non sharding of computation

Phase 1 from a specification point is very simple, or at least very simple given all of the work already done on the Phase 0 side. The one hard thing is actually specifying the full proof of custody game which we are still in the process of doing.

Phase 2, which is basically state and Execution is the thing that I think we can contribute and try doing in parallel to Phase 1. SO, I think we should not fall into the mindset of thinking that first Phase 0 gets done then Phase 1 gets done then Phase 2 gets done without working a lot of work between them in parallel. Because if we don't parallelize then we are going to take them to 2021 or whatever the trolls are saying. 

The nice thing is Phase 1 is primarily Peer to Peer networking  **implementation challange**. Phase 2 is very significantly a **specification challange**. So, I see a huge amount of opportunity to do them in parallel and I would argue that its time to start the real discussion on concretifying what Phase 2 is going to look like in.I have been starting to reach out to 1.x people on more of something to put up research post about Cross shard transactions. 

One interesting thing, that is worth getting a lot of peoples input is what would be a dream replacement of ERC 20 would look like that would be done on top of Phase 2. Both because, this is what a lot of people want; but it will also be a quick test of how easy it is to build things that are actually interesting on top of whatever Phase 2 is building. So, I am in favor of doing in parallel work and am going to push things. I hope to get feedback from a lot of people. Specially this is the area where we need a lot of input from people who have experience with actually trying to build in and deploy things on top of current platform. 

**Greg**: I may have misheard, but why it would be trolling to expect Phase to be done about 2021?

**VB**: I said 2020, whatever. There is definitely people saying out , its 2021. I think even 2021 is not the date honestly we should be shooting for. Because the thing with Phase 2, in terms of specification basically needs to start today is what I am trying to say here. Because we know that Phase 2 has larger specification challenges to it and Phase 1 is kind of relatively heavy on implementation process of Peer to Peer network. It is relatively light on that and heavier on these other complexities. SO, its essentially in our hand to try to work together and make phase 2 things not delayed than it is necessary.

**Hudson**: Cool, any questions or comments on that?

**Hudson**: Danny posted a link to Phase 2 pre spec document at EthMagician. You might want to look at that.

**Greg**: Do we have a critical path analysis to say whether these tasks can be done in parallel?

**VB**: Which tasks are you talking about here?

**Greg**: Running through Phases of development in parallel, it takes a critical path. If actually that is possible?.

**VB**: That would be recommended. 

**Danny**: What sort of analysis that you want to see,  I don't think we have that. The way the account exist and are deployed and execution is independent of how it comes to consensus on the data. The specification and design space for Phase 2 is pretty wide and we should certainly be specifying it there in the design phase. Whether you have Phase 2 without having Phase 1 underneath is not a question right now. It's really you can really specify and narrow down that help a lot of decisions in Phase2.

**Hudson**: I had no idea about what a critical path analysis was. So, I posted it in Zoom chat. It's pretty interesting and has a cool graph,so check it out.

**Greg**: It is a 50 year old engineering technique. I don't think its used to proceed because it has a lot of Physics.

**Hudson**: Any other comments or items of the agenda?

: Yeah, just one more thing for everyone listening to take personal action about the redeployable contracts in post Constantinople , to help educate your networks about the redeployability and specifically this idea that someone can carefully crack the contract that looks reasonable to people who are in Constantinople mindset but definitely malicious afterwards. 

**VB**: Also add that in the least occurrence of kind of vegan nebulas set up proposals for Phase 2, CREATE2 is the only kind of creation occurred. This will help navigate people who are working around CREATE2 base contract system and work are even more important.

**Hudson**: Anything else anybody?
# 6. Anything Else 
**Hudson**: David posted about sync up on EIP 1193. 

**David**: We are planning to have a call, may be latter you can have an agenda for that. But loosely, we just want to talk about implementation and roll out of EIP 1193 which is only related to JS providers.

**Hudson**: Thanks for that. That sounds important. 

**Hudson**: Anything else anybody? W are half an hour early. Everybody, you have a good weekend and we will talk to you in two weeks.


# Date for next meeting
March 01, 2019

# Attendees
1. Hudson Jameson
2. Jason Carver
3. Vitalik Buterin
4. Afri Schoedon
5. Brooklyn Zelenka
6. Daniel Ellison (ConsenSys)
7. Danno Ferrin
8. Danny
9. David Murdoch
10. Dimitry Khoklov
11. Fredrik Harrysson
12. Greg Colvin
13. Jeff Coleman
14. Mikhail Kalinin
15. Meredith Baxter
16. Tim Beiko
17. Martin Holst Swende
18. Hugo
19. Pooja Ranjan
