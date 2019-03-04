# Ethereum Core Devs Meeting 56 Notes
### Meeting Date/Time: Friday, March 01, 2019 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/82)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=q3ylladkuYY)




**Hudson**: Welcome to Meeting #56 of Ethereum Core Developers meetings. We will start with first item, which is Roadmap.

# 1. Roadmap

## 1.1 Constantinople Success!

**Hudson**: Constantinople activated successfully yesterday. Yay !! I don't think there is any problem with it yet. 

## 1.2 ProgPoW Audit

**Hudson**: I will give a quick update on that. 
Cat herders will publish more official blog post on ProgPOW which will provide details on it. I want to clear up something about ProgPOW Audit from Ethereum Cat Herders prospective who are designated on to organize and get signals from the community on what is going on with the audit.

* There are two components to the audit: 
        1. Benchmarking: It is less important in my opinion because the community has been benchmarking lately. But, that one is to see if by running graphics card on NVIDIA and AMD, if either one of them is performing better in an unfair way. White block has a bounty out right now on both Bounties.network and Gitcoin to perform that work. Thats a way to raise funding form Benchmarking on ProgPOW. 
        2. To see how long it would take an ASIC company to actually build a ProgPOW ASIC? How performer it would be compared to a GPU by a factor of 1x, 2x or 10x? So, we can see if it is even worth to implement or someone is just make another ASIC in 3 months and all of our work will be for nothing, since the work isn't entirely done yet. I feel it is a major factor in considering whether or not to go forward with ProgPOW.

* As far as signals from the community, we have a hashvote (if someone has a better name, let me know) thats where miners are signaling at the Ethereum network using the extra data field whether or not they support ProgPOW. SO far all the miners who participated, supported. There is a page on [EtherChain](https://www.etherchain.org/charts/progpow). 
* There is also a coinvote and they are also overwhelmingly YES. However I want to stress that these signals and the third thing, the official twitter poll that Cat Herders ran, all of these things are signals and not the deciding factor. It is more of figuring out which stake holders thinks what. So, we know that current miners on the network overwhelmingly support ProgPOW, which was already known but this kind on cements it. 
* We have an interested party who just send me a proposal for the second part of the audit on how longer it would take to build the ASIC.
* 55 % voter turn out miner signaling, which is very high. It is more than half of the Hash Powers.

**Lane**: Yeah, I think its 55% hash power.

**Hudson**: Yeah, that make sense. The other company that will get back to me hopefully early next week, then we will start getting the Gitcoin grant together, looking for funding like we did for Whiteblock and see whats that all about. Charles, Joseph, Pooja - anything I missed? 

**Alexey**: I just wanted to say that I have seen it somewhere that there is an other interpretation which could potentially be useful of the miners signaling. Essentially if those 55% that turned out and they all voted in the favor that gives you essentially a lower bound on how many GPUs are currently mining in the network.

**Hudson**: Yeah that is an interesting thing to think about.

**Danny**: Potentially, there must be some sort of misdirected effort where someone wants to slip in but I agree generally, it seems like a lot of vote. 

**Lane**: Also, most of the votes, we know which pools they came around, looking into EtherChain link.

**Hudson**: Sparkpool was going to vote Yes is that what I heard. I don't know if they got around in doing that extra data but that would also represent an even bigger amount of hash power than what is already represented. 

**Lane**: They are not voting yet.

**Hudson**: Alright, well that makes a big difference too then. 

**Lane**: It might be worth asking them why, may be not.

**Hudson**: The last I heard, they were just trying to figure out how to do it for scale.  up something like that.


**Lane**: If you wouldn't mind talking about something more on funding yet. I know there has been some question about it. I know there is at least one application that Andrea submitted to EF but I am little unclear on this myself like what was submitted and the official statement on the part of foundation on what they won't  be financing of this plan or any thing on this part will be helpful. 

**Hudson**: Yeah, absolutely. It is very important that Andrea get it's funding for ProgPOW if we decide to go forward with it. In my opinion, even if we don't just because it started to trend in a way that we would go forward with it, I think its important that he continue to work because he has been working on it without pay on ProgPOW. I think he stopped working because its not sustainable without funding. As far as funding sources from the Ethereum foundation, I was not involved in those conversations and I don't know any of the official view points. I heard that there was a grant application submitted that they got rejected. I don't know if people know more about it.

**Pawel**: There was an EF grant application that I actually interested to do an participate in the process as an applicant but I didn't apply any funding for myself. That was redirected following the standard grant process.

**Hudson**: Sounds like we have an answer there from the Ethereum foundation perspective for the grant.


**Lane**: I guess I was just wondering if there was any color there on whether that was more of a political decision or the technical decision. If technical decision, fine ; it happens all the time in the grants process. I don't have any inside information but if the case is EF is saying  I don't want to fund this for a stance, I think it will be helpful for the community to know. 

**Danny**: What was the grant?


**Lane**: Pawel, could you explain the grant?

**Pawel**: The grant was for two developers to work on ProgPOW implementation of Eth miner and also to work on Stratum protocol, the new version of it that will help to make the POW switch. There were two more tiny items also included related to mining and infrastructure. 

**Danny**: I wouldn't read this political. I wasn't involved, but I know past 4-5 months it was more of making to the priority straight and to ensure that they are giving grants to things to distinct value. If they didn't, then my interpretation will be may be there is a lot of ProgPOW work going on and will be going on and assumption that it will go with or without that.  

**Pawel**: The official statement is just that there are a number of application program and we selected some. We can't expect any other statement by the team. 

**Alexey**: I just want to make a few  comment about the grant. 
1. First of all, I do know that other grants have been rejected, so this isn't the only thing that has been rejected as I know other applicants that did apply and got rejected, so I think this isn't political at all. 
2. Second thing that I want to point out is that if you think about what EF should actually be funding then it should be funding the things that otherwise can't be commercialized and used in a profitable way. So, if you think about it, you might conclude that some of these work actually be profitable for some people. Therefore, they might try to find funding elsewhere. This is my personal opinion.


**Lane**: Thanks Alexey,thats helpful. I agree, lets not read too much into EF grant. Then the question in my mind is what are the other options on the table? I know that we have at least two bounties requests open for Andrea and Whiteblock. 

**Hudson**: That's correct.


**Lane**: I was just making people aware of things. 

**Hudson**: I know that ConsenSys has $500k grant thing, have not much info about it though. 


**Lane**: Its not like officially up to the core devs to worry about funding and get people money. I do think, we need to have an honest conversation about it in this context as well as broader context. Does anyone has any other thoughts? As I think some of this work is pretty essential to the ecosystem that without picking sides and having favor, in general there should be funds available for this kind of work.  

**Alexey**: I would say the last thing as well. I read some in Eth magicians about the funding but there are other ways to think about it. The CArbon vote, where people actually voted with Ether,the number of Ether which was voted for was about 3 million Ether. I looked at where it came from, basically very large amount up to 200k to 500K came from three different entity. So, actually huge entities have actually interest in this project. SO may be we should ask them to fund this. 

**Hudson**: Yeah, that's not a bad idea but I don't know if we should be the one asking. Not collectively but individually, I agree. Any other comment before we move on?


**Greg**: The best thing that we can do is speed up the process. It's almost two months there and they can just let us know "yes" or "no" so we  move on when we have funding or not. Not everybody can hang out for months  waiting whether to go get a job rather to help Ethereum. 

**Hudson**: Okay, Good feedback.

**Pawel**: I have one more comment, I think I tried to make a note in some of the test discussions that to clarify ProgPOW never claimed its ASIC resistance and there is no way to make an ASIC. What ProgPOW claims to provide is the difference on performance between GPUs and ASICs  to simplify will be much less than Ethash. So, I don't think its really that important for the audits to figure out that how much time will it take to make an ASIC for ProgPOW. Because, somehow its not really relevant.  The question should be like that if it is really true that the maximal difference will be 20% in favour of ASICS?

**Danno**: Kristy mentioned that incentive could be up to 30% of the high bandwidth memory which is very expensive. But I agree that we all have audits to verify that those balance have solid reasoning. 

**Alexey**: I remember, when we had this discussion on Gitter channel, I have been asking the question about the success criteria for ProgPOW and I never got the answer. What Ferrin is saying is probably be the answer because when actually try to  pin it down, there is always a thing like 'oh but GPUs are also ASICs', 'oh probably the can be created but in 3 years ...' this kind of things. If this is the success criteria, then audit is probably not going to deliver much satisfaction. 

**Hudson**: Thats interesting. 

**Greg**: Anybody who knows the answer has damn good business reasons to keep their mouth shut and make the assets.

**Hudson**: Yeah that is actually why many ASIC manufacturers had declined doing the audits in first place. 

**Greg**: Why would they, its competition. 

**Hudson**: Luckily, the person who is offering to do that and is sending the proposal is independent of ASIC manufacture and seems pretty excited to potentially do this and has the background, as far as I can tell to complete some thing like this and have a team behind. 

**Greg**: I am still confused, why we are doing this? What part of our consensus wasn't clear for revisiting these issues?

**Hudson**: That's a good question.

**Greg**: It's my only question. 

**Hudson**: I am trying to remember the meeting where we decided to do the audit and what we came to ?

**Greg**: We were looking only for the technical problems like holes in the algorithm not whether the algorithm is going to have a certain percentage of fact. I think we knew that we are in arms race with the ASICs and at some point we will either decide to maintain the race or decides the ASICs wins. For the next nine months we decided we do this unless there is a technical problem with the algorithm. Not whether somebody thinks it may be the ASICs can win the battle over some period of time. 

**Danno**: The argument about the ASICs in the margin of efficiency is one of the claims in the EIP. I think that is a technical problem because they claimed in the EIP. 

**Greg**: Okay!

**Hudson**: Any other people have comments on that?

**Alexey**: I have also been asking whether we would like to keep fighting ASICs or we just do one attempt and we stop at this because I heard, the ProgPOw has different parameters that we can change. My question is are we actually going to do this, to keep tuning it to basically do hardfork every six months. Because this is not defined, the conversation just go all over the place whenever we start discussing it, because it has never been decided. My concern mostly comes from the appreciation that the bandwidth of the change in the Ethereum protocol is  actually limited. That some thing can hold this hold agenda of this meetings for months. That makes it really hard too do the other improvements that we actually do  need as well.

**Greg**: Thats when you form a working group and tell them to go away and come back with information. 

**Alexey**: I completely agree with that Greg. The working group should take over, remove it from agenda  and not talk about it every single time. 

**Greg**: We don't have to decide through this hardfork what we are going to do next time.

**Hudson**: Yeah thats a good point and also when you say working group thats what kind of Cat Herders are doing. So we don't have to have it in future agendas until have the audit done. It was more the community requested to have it on the agenda  so I decided to put it on because this is something that people want to hear about on the technical level in some ways. I agree that it shouldn't be on the agenda every time.  It is pretty clear what we are doing, even if it is not clear why all the time, its clear what we are doing.
I agree Greg, your question was clear. 

Anyone else have any ProgPOw comment? 


## 1.3 Istanbul Hardfork Roadmap

**Hudson**: I forgot to add the hardfork coordinator role. Afri is no longer the hardfork coordinator. A very good question about how he became hardfork coordinator, it was discovered that I talked about it in a meeting but I hadn't . Technically, I just decided that he was the hardfork coordinator for fork along with the Cat Herders. It was like, 'Oh! Afri wants to do it, thats great.' But we didn't talk about it in here. So, we should talk about it right now. What do you think about having a hardfork coordinator? What I get from previous discussion that everybody wants it, but any one against it?

**Greg**: Who wants to do it?

**Hudson**: There are some people who come forward.

**Lane**: Before we get into that Greg, I agree with Hudson's question, we need to talk about what the role is and whether we all think it's worth having? I share a quick thought. I think, there is value in it and the reason is because the number of teams and the number of individuals working on even just the Eth 1.x workstream not the even mention the Eth 2 team, but of course that as well has grown quite a bit.  Size of this call has grown, the complexities, the coordination, the work required, to get everyone in the same page and getting these hardforks to happen has grown as well. I do think and hope that I am expressing the consensus  of this group when I say that we like to do hardforks more often or upgrades more often, you see the coordinator role can help a lot. SO, I see value in it. But I am curious as well if anyone disagrees. 

**Alexey**: My question to the hardfork coordinator role is whether this person / group of people is going to be only concerned with the actual hardfork meaning something which starts say one month before the block of the hard fork and ends on the day of the day of the hard fork? Or is it more like loosely defined and spills over to EIP and all sort of stuffs? Where does the barrier between EIP coordinator and hardfork coordinator starts? But I do agree with Lane that do you want to reflect things that why we are doing things the way we are doing it and may be we should do better. ANd may be we should do more hardfork frequency, then yes that might be important role. 

**Hudson**: Yeah, to answer your question, they would not be an EIP editor, they would obviously have to read EIP, coordinate some of the core EIPs that are going into meta EIP in upcoming hardforks but in general hardfork coordinator in my mind is someone who between now and the next hard fork decides hard dates for deadlines of submitting EIP for consideration. Deciding on those EIPs implementation and testing and finally, what day the hard fork would be. Of course, they wouldn't be the dictator in this regard but they would come up with suggestions and different options on the table because, no one has time to do that so far. Also if there is any kind of disorganization over it like any kind of confusion over what people want, they can kind of shift through core dev meetings and online discussion and filter through that. Thats my idea, but it can roughly expands to things on what the release coordinator feels like what they need to do.  

In general, a few people came to me and said that they want to help, so, I am going to collect a group of those people. A lot of people suggested to have community vote on who should do, I don't know if that's the best route or not to hear opinions on that. I want to hear opinions on that if core devs should be deciding on who the core dev release manager should be or the community  decide on who the release manager is? 

**Joseph**: Is it also possible  that we might split the role to 2-3 people ?

**Hudson**: Yeah, thats absolutely possible.

**Greg**: Who actually wants to do it?
 
**Hudson**: Joseph comes forward and said he would do it. 

**Greg**: Good, volunteering.

**Hudson**: There are some other people whom I would want to give a chance to say there part since they came forward but I hadn't had a chance to talk to them deeply, not even Joseph. 

**Greg**: Is there any objection to this person? Its not like we have so many people who would want to go through this abuse.

**Hudson**: Oh yeah. No, there is not. Its more like people understanding if there is more than one person. If the core dev really don't care then they can delegate it to the Cat Herders can pick some people. They either split the role or let one single person do.

**Greg**: If the Cat Herders volunteers the group, go for it.

**Lane**: That was going to be my question. Do we see this something that falls under the purview of the cat herders?

**Alexy**: It is still not clear and I hope it will get clear that what are the  decisions that these people are going to make. Because what we do want them to do is essentially is to aggregate some information, make a decision or we don't want them to make any decisions and they are going to be information aggregators? What is it?

**Husdon**: We have a blog out, did we release yesterday? Pooja do you know about it?

**Pooja**: Yeah it's on medium, I will post the [link](https://medium.com/ethereum-cat-herders/further-introduction-the-ethereum-cat-herders-c42bf026fb7c). 

**Hudson**: That would be great. Alexey that would answer your question about the scope of the Cat Herders. 

**Alexey**: Its not about the Cat Herders its about the release manager. If we decided its going to be the same thing?

**Hudson**: I think people don't really care they just want some one , its what I am hearing. Because I am not hearing a lot of comments on it. SO, we can do this. Lets have the Cat Herders figure out who wants to, get them all in the same chat room and split the role. I think that sounds good to me. Anybody does have any ideas? 

Okay the Cat Herders will do that then. Alexey you didn't get your question answered yet, could you re-explain it?

**Alexey**: It is okay. I don't expect all of these questions to be explained all straightway, it requires a bit of figuring out. In the GitHub issue, I was proposing couple of things, couple of changes in the actual process in the preview of the core release manager. eg. I am suggesting to appoint dedicated reviewer for the change than to wait for someone to look for the change. If the HF is not really near, it takes a lot of time for some one to actually pick up and look into the changes in that because there is no dedicated reviewer. Thats a shame because we waste a lot of time waiting for it to happen. There are very small number of people who are expected to look at the changes. We rather have some appointed potential people who are not even on the call but they want to review the changes and come in the call to explain to what they have found. So, that we can iterate quicker over thing having lying down. 

**Hudson**: Hopefully, we can find that role and if we can't then we have the release manager poke at people who would review that such as EIP authors to do more review. 

**Alexey**: Well that don't need to have a permanent role of reviewer. I mean for each change somehow we pick the reviewer, probably one to do the review and reviewers are not necessarily the core devs who are initiated in this call but somebody else, who actually wants to do it. 

Second thing I wanted to propose is that we need to revisit the assumption that we have to bundle a lot of updates to have a big release. I heard before, it is really very hard to coordinate the release. I hope this new role of release manager or group of people help us to understand if it is really good or not.

**Hudson**: Yeah, I agree. I think those are good ideas. I am sure the release manager would take them into account. 

**Danno**: One other thing I would like to put out is before Afri left, he did a set of schedule. I think some of these roadmap things will help us, to get the things done, to make a decision to put it in or pull it out.  I think some changes are ready, and we are going to come out in pace if roadmap is still valid. My opinion on multiple small releases, its going to make things even longer. There are a lot of meetups and preparation that goes towards these releases out, is that I have seen. Doing it multiple time in smaller thing is going to be a lot work. It will take about 6-9 months of every release if it comes to small releases. I think its more efficient to bundle multiple to put in but it is something for the release manager discussion. 

**Alexey**: Thank you for this comment. But I think, it is based on the assumption that we continue doing things the way we did before. This is why I put another comment. 

I also propose to have high standards in the EIPs. Then  we need to require some kind of proof of concept, probably pre-generated test cases, so we don't leave it to the later. My proposal is about appointing reviewers might be helpful because I think a lot of people think that we have to sit on the change for months before it actually gets in. We did a bit of retrospective on this in the workshop. You don't actually have to sit on this for months, if we find the reviewers quickly, the implementation doesn't actually takes that long. Generating test cases usually takes long because only one person or two are doing it. If we make it burden on EIP author to actually do that to help the testing team then I think we can move much quicker than before. 

**Danno**: I agree, EIP should cover test metrics. 

**Hudson**: Yeah, thats a great idea. Moving on. 

# 2. [Subroutines and Static Jumps for the EVM](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-615.md) - [Magician's Thread](https://ethereum-magicians.org/t/eip-615-subroutines-and-static-jumps-for-the-evm/2728)


**Hudson**: This is something Greg wanted to bring up. 

**Greg**: I didn't wanted to discuss any details. I just wanted to heads up that its coming. Because there are people on this call who would love to have some review and might not hear about it otherwise. 

**Hudson**: Great. Thank you for that.


# 3. [[Reject EIP-1355]][(ethereum/EIPs#1785)](https://github.com/ethereum/EIPs/pull/1785)

**Hudson**: Pawel, you want to go ahead.

**Pawel**: It was original proposal that was to counter ProgPOW but in the end we realize that its not very effective. Considering how much time does it take to discuss Proof of Work changes and related. It wasn't possible to be done in the time, so to clear it up ; I marked it as rejected. 

**Hudson**: I think according to EIP process, correct me if I am wrong, you can withdraw an EIP if you are the author of it, basically has roughly the same meaning as rejected. Because rejected would be the core developers deciding it is rejected because of a technical issue. You can change the status to withdrawn and then its withdrawn

**Pawel**: I didn't realize that. I think that might be better. 

**Hudson**: Sounds good.

# 4. Working Group Updates

## 4.1 State Fees

**Hudson**: Alexey just release part 6 of reflection from the Stanford working group. Alexey if you want to give updates on that then I have some comments. 

**Alexey**: I wrote it after the event and I have added more data analysis and more thought on it. As it reflected in the workshop and I realized that there are some blind spot, I will talk about it a bit later. But essentially the main thing that we carried out in the workshop is that there are four major problems that are performance problem that are coming from their growing state.
1. Failure of the snapshot sync
2. Duration of the snapshot sync
3. Slowing down of the block sealing
4. SLowing down the transaction process due to the state size.
The blog describes in detail what are these problems , how are we planning to handle some of those and to address them. Ex. the first problem we deemed as the most critical one is by introducing a better sync protocol. I know that there are already some work going about it in Parity and Go Ethereum. They have a different names for this.Also, Andrew is not working with me on Ethereum 1.x, he is also working on the modeling and documenting the other version of this protocol. For our version of this protocol, he came up with this cool name "**Red Queen**". It should not be confused with the queen of hearts. The Red Queen is the one which basically says that 'in order to even stay on the same place you have to keep running.' The idea is that you have to keep following. When you sync, you actually have to try to chase the head of the sync  while you are syncing. These all efforts will hopefully converge once we start having specification. I don't think we need hardfork for that but we need some coordination in terms of implementing protocol.
**Blind spot** that I talked about is that I want to come back  to the idea of of the stateless coin and this is not the same as stateless contract that was described in my state fee proposal. Stateless clients are actually the idea that the blocks propagating through the network, they are augmented by some more information which provides you the sort of state subtree with all the hashes that essentially provide the proof that the data that the transactions are reading are indeed belong to this state. The update the transaction are performing result in the new state root. SO essentially, by having simply the blocks, the state roots and those augmented data which is like the block proofs, then we will be able to execute the transactions without even having access to the state. This is previously been researched a little bit. I wanted to do some data analysis a year ago on how big this blocks could be. I know Vitaik has done some analysis and Casey did that too. But this time I wanted to do it more seriously meaning that I am almost doing the proof of concept for this to make sure my estimates are correct. I will publish the details of how big this things are and we will see, if this is something that we could combine with state fee. After this workshop I have realized the most expensive and laborious part of these projects is existing research which is analyzing the  the all possible contract which is currently very popular one and figuring out how they can change and adapt to the state fee which potentially could take months and cost a lot of money. I am tying to see, if it is truly necessary. I am not being optimistic and pessimistic on this but being possibilistic on this. Any comments on that?

**VB**: We talked about it privately, but the idea of using stateless clients for contract storage definitely has lot of advantages to it. As I read, it seems it would break a lot of existing stuff which is nice benefit. Doing it just at contract level and not at level of the whole system remove a lot of risks that I see it. I guess the main challenge in all of this is definitely going to be whether or not the cost of much higher  bandwidth is worth it or not. As part of that a couple of questions: How would we actually do  gas cost for the bandwidth? Would we still have a fixed gas cost for accessing storage or not? Would we try to do gas cost based on the length of Merkle branches, would we try to inside device having smaller trees and inside device reusing access, would we try doing something else? Otherwise what is the cost of data? I know we decided at the workshop to call data would be be overprice by now. Whats the price for the world was? 

**Alexey**: Thank you for the comment. To answer the question about cost, Yes, definitely according to current idea, these extra proofs they would have to be paid for by the transaction sender. In this case the payment go to the miner rather than being burnt because essentially the introduction of this system relives everybody holding nodes apart from the miner that actually having stake. Everybody else doesn't even need to have the cash trie  in their memory because they can simply verify the proof and not update their database. Even if they have the entire state in their database, they don't actually have to cash it in their memory. It means that everybody apart from the miner will get huge boost in terms of performance and resource consumption. I would charge not in terms of length of branches but basically per byte of the proof. Currently, I am working on this little proof of concept. I am actually going to calculate the two parts of this proof - the actual hashes that are companying and the data. The data is what you actually have read during the transaction. If the proof turn out to be super big, we could also use something like STARK proof or SNARK proofs to actually to compress them in such a way that there will be a fixed size per block for all the proofs but you would not be able to compress the database. Once explored, within a week or two, I will publish some data so we can have some discussion about it. Its not sort of decided yet, that this is the pivot we are going to take but this is the potential pivot. 

**VB**: Ok. It definitely make a lot of sense that to look in both past and parallel and see how viable both of them are. Just quickly, has there been progress on figuring out on what the cost of bandwidth data are? I guess the proof data of this kind seems like exact same cost as the transaction data, so do we have better ideas on how much that in theoretically should be charged for?

**Alexey**: No, I am not aware of such analysis, but is definitely important so I have it in my plan. Very good point, thank you.

**VB**: I guess like final point, this sort of stuff should be made four time more impressive if we replace the hexatree with any kind of binary tree. Should tree replacement be part of this ? If so, for very big contract, is there plan on how to do that?

**Alexey**: I have thought about it but not for very long time. As far as I can tell now, it is very challenging to try swap the binary tree. That is why I hope, if we get some STARK or SNARK proofs, we might try it altogether. But I haven't figured out it yet. 

**VB**: But instinctively, STARK proofs don't  seem like that sort of thing that would be viable within the next 1 - 1.5 years. 

**Alexey**: I am bit more optimistic on that. 

**VB**: Okay, that would be good. My concern on this side with all of these technical issues is that Zero knowledge proving things in general purpose has an overhead of factor like anywhere in between 100 and 100000 depending on what how ugly the computation is. Hash functions that we used today tend to be on very ugly side. Given, what I know about the efficiency of roll up which seems to be very similar case to this that doesn't seem optimistic. It seems like that would basically require block produces to have a whole other GPU dedicated to proof generation. 

**Alexey**: I would start exploring this with the guys from STARKware. Once I have the data may be they would give me some hint whether this is viable or not.

**VB**: Okay. I may ask you to be there as when 2.0 team probably be having the same conversation with STARKware people.

**Alexey**: Absolutely yes.

**Lane**: Alexey, thank you for the update. The kind of stuff you just shared, I don't recall seeing that in latest Fellowship Ethereum Magician thread and the stuff that you posted on latest store management state fees. I have a lot of questions and ideas but better to take of in other forum. Where should we have that conversation. I have started working on it three days ago and hadn't got a chance to publish anything yet but I will hopefully publish something in like next few days. I am looking to finish this coding first and then would write something. I brought up this in this call because this is important to know about the potential of common pivot but I simply didn't get time to put it in writing yet. 

**Lane**: I will keep my eyes and look forward to it. Thank you.

**Danno**: SO you mentioned that Parity, Geth hybrid whatever sync. Is there anyplace where these prototypes available that we can play with and try?

**Alexey**: This is the challenge of the moment and if someone from Go Ethereum and Parity  in the call they can correct me but at the moment there are some prototypes in the code but that is not written down as spec or a model. So, one of the thing that we would like o do with this Red Queen is actually try write the spec as well as a modeling. At the moment it is too early to say and I would like to encourage other people to write the spec as well but it  a bit early stage.

**Danno**: I am hoping they could share that.

**Peter**: At least in Go code, there is a pull request. I am not sure it it is a pull request or my branch but I can share the link. The code is fairly simple. I guess you get the idea but there are still a few corner cases that I haven't solved completely. Honestly, I wrote that code a year ago and I never visited again because something always came up. 

**Hudson**: One other thing that you talked about Alexey was figuring out the P2P protocol, are you talking about if we are using P2P or something new protocol?

**Alexey**: No, I was talking about the thing called ETH 63 which currently is used to essentially shuffle the data around the network. By the data I mean the headers , block, transactions. SO each of the type of data there is normally pair of operative. Get block, Get block header, get block this and also announcing. What I mean by changing P2P protocol is actually adding more operative to that. It means that we need to sort of upgrade the protocol that clients can understand each other. These operatives are dedicated to support this new advance protocol which pretty much never fails, hopefully.

**Hudson**: Got it. Okay. Anyone else has comments on Alexey's update?


## 4.2 EWasm

**Hudson**: There was an Ewasm working group if it is still a working group or not. Lane do you have any updates or comments on that.

**Lane**:  I think there is some confusion here. I think the Ewasm working group is like the Ewasm team and unfortunately neither Casey nor Alexy is on the call. Pawel, do you have anything to say? I don't know if I have anything to say on that.

**Pawel**: I don't have anything in particular. We are actually preparing for EthCC.

**Hudson**: Great.

**Alexey**: Hudson, if I may, I can throw something in for the Ewasm as well?

**Hudson**: Sure.

**Alexey**: What I have been thinking about in terms of Ewasm after the workshop and before that, if some of you may remember the first proposal of the state fee or state rent, it was called, I was actually suggesting linear storage. It is like a new type of storage that doesn't exist in Ethereum yet. One of the reasons why I actually like that is  Ewasm is essentially operates in a linear memory, the idea was that you can do the memory mapping, the storage into the memory in a very straight forward way. I still think its a good idea. May be I will propose it as part of the hostage management thing, may be I will propose this linear storage thing again but in a different guys. May be integrated in the Ewasm itself. I just wanted to throw this in.

**VB**:Just to be clear Linear storage does that mean the storage as a byte array? 

**Alexey**: Yes, the current idea is for example if we introduce a new type of contract, for example we have Ewasm code instead of EVM code and instead of mapping storage, it is essentially an array of bytes and words and then lets say we do some sort of Merkle mounting ranges on top of that Merkle trees which is friendly to the expansion. It means whenever we execute Ewasm, we map the part of the storage into the memory and you can have this really great benefit because then you can have this sort of libraries from lets say Red black trees and some sort of structures. Because all these libraries are written in the assumptions that you have a linear memory instead of like Ethereum storage. So, I see this a potential for code use. 

**VB**: Would you be expecting the storage size to be fixed to be of one size, something like extendable size, possibly capped by 24k or some similar number? 

**Alexey**: I thought about this because I remember your suggestion idea somewhere. I think it might be a god idea, at the moment, I am thinking about expandable.

**VB**: So, you would still be able to go into S store like byte number like 547 Gazillion?  


**Alexey**: Kind of. But it will cost you astronomically much , a lot of gas.

**VB**: Oh I see. 

**Hudson**: Was that all the comments?

**VB**: Another quick thing for Ewasm, I made a comment on GitHub asking what does the Ewasm team think should be the interface of Ewasm with respect to the rest of the system? This would basically be the call for a foreign function interfaces environment variable and function would be accessible. It would be nice to hear if the team has any thoughts on what is the ideal kind of interface to work on? Do you want simpler than what we have now or to add any new kind in future or something else? 

**Pawel**: How it looks now is we have version from SIM + EVM. We need  to take some iteration over it if other teams figure out what are the requirements on the other side. There are a number of proposals mostly in the design pull of the EWASM. That has some proposals on how to make it related to web assembly. I would have to proceed that in some way where probably other team are set.

**Lane**: Other question for you, do you think it would look like ECI, the work you have done on that or this be a very different type of interface?

**Pawel**: I think the aspects, how much compatibility we need with EVM and what we have learnt from the EVM, both are good parts of it and like bad parts of it. This is how you actually want to access data from Ethereum environment, lets call its this way. They would probably look as imported functions in web assembly but broader aspects of it how actually it interact between contracts because both of them are written in web assembly. And web assembly provide some more efficient or more direct ways of calling one from the others. This opens another set of possibilities. I am trying to keep it on high level one. 

**Lane**: Alex also mentioned in the same thread that were investigating different ways of doing contract linking as well. I think thats what you are just talking about. 

**VB**: Okay great then I will probably like poke into the Ewasm design and wait for Ewasm people to come up with more things.

**Lane**: I will take a look as well in the design repo Vitalik and try to map some of the open issues there are some question and topics you raised in this as well. 

**VB**: If you want to poke through then give me the pointer to you think will be most value , it will be good too. 

**Lane**: Will do. 

**VB**: Cool.

**Hudson**: Cool Anything else on that?



## 4.3 Pruning/Sync

**Hudson**: pruning / sync ?

## 4.4 Simulation

**Hudson**: Anyone from simulation?

## 4.5 Appetite for future in person meetings?

**Hudson**: We talked about that last time. Anyone have any comment on that. I kept it there because there wasn't any comment last time but there is different group of people this time. 

**Alexey**: I would say that the in person meeting are important but I wouldn't do them very often because there is a certain amount of work, traveling fatigue. Some people think that people are not very inclusive when people gather around. I must say with the example that the workshop that we did in Standford, I was skeptical before I came but after that it turned out to be very very useful thing to do. I know a lot of people could not make it but I say that it is definitely useful but we shouldn't try to do them too often. When we think we have enough divergence in our mental model then we come together. 

**VB**: As far as making them more inclusive they have to happen like bouncing them between  is also helpful. Like the last one was in San Fransisco and some people were descending off Australia and both of which were not convenient for people from here. At least in 2.0 calls we have been getting someone constantly badgering having one Barcelona. SO it might make sense to do something in Barcelona at some point.  I am sure there are a lot of people who just found a way too inconvenient to come to longer distance what ends up coming to that one. 

**Lane**: I know a lot of Eth 2 folks are planning to meet in Sydney and I am just wondering if any Eth 1.x folk is also there. May be be we can take advantage of that or may be not. 

**Hudson**: That sounds like a good idea as long as people will be there. 

**VB**: I definitely don't want that kind of good job peoples taking 20 hrs of flight. If anyone is coming then will be happy to chat. There are meeting plans during EDCON already. 

**Greg**: I think its just enough warning, international flights get more and more expensive as the date approach. Often, they are sold at with warning, so its not possible. 

**Hudson**: When is EDCON?

**VB**: April 14.

**Hudson**: Yeah, its pretty soon.
It sounds like there isn't appetite for future meetings but we may need to have enough lead time. SO anyone who wants to take initiative on planning those meetings can go ahead and do it, even if its more adhoc and not like really big one. They can really skip the opportunity and people can attend. I know, EDCON is pretty well attended so that would be a good one for someone to take up the torch on. I can't because I won't be going but someone else could. 

**Alexey**: I would say that for specific detail on it, from my point of view, it might be too early as I haven't even digested the previous workshop yet. I mean I have been digesting for like month and a half. 

**Hudson**: Yeah and figuring out the specs a little more clearly. Thats a good point. 

**Lane**: It sounds like may be Barcelona, may be sometime in summer, may be its too soon to pick a date. but yeah just back of the mind, thats helpful.

**Hudson**: Cool, I think we can get off the topic. 


# 5. Testing Updates 
**Hudson**: Anyone has testing updates?

**Pawel**: There was small change to blockchain test recently which aligned the configuration for what actually happened on the mainnets yesterday, which is Constantinople. The Constantinople fix were activated on the same block. Feel free to see the blockchain test for this case was a bit different and we changed that. Some set of test are different now and they were uploaded yesterday. Thats I think, clients team can take a look on. 

**Hudson**: Okay, thank you very much for that.  

# 6. Client Updates 

## 6.1 Geth

**Hudson**: Clients update. Geth?

**Peter**: Update wise, i think that two more interesting updates are that to be managed to finally merge all the changes that slims down the database and  cut out down the data, so we are down by about 16 gigs compared to our previous one which puts us in the same ball park as Parity. I am really happy about that. Apart from that, we recently found some bug in Level DB, which we fixed and this seems to speed up our archive syncs quite a bit but we are still not happy so we are still looking into it. Apparently, we managed to shave off quite a bit from the sync time. Those are mostly our success stories and apart from that we are working on the networking via some discovered protocol, light client and essentially the pull off of historical state pruning. But it seems to be a bit tough debug. Thats about it. 

**Hudson**: Ok.


## 6.2 Parity Ethereum

**Hudson**: Anyone from Parity, here?

## 6.3 Aleth/eth

**Hudson**: Aleth??

**Pawel**: No real update except the information that we haven't done the stable release of Constantinople fix yet.  We are a bit behind the schedule for that. 

**Hudson**: Okay.

## 6.4 Trinity/PyEVM

**Hudson**: Trinity?

## 6.5 EthereumJS

**Hudson**: EthereumJS?

## 6.6 EthereumJ/Harmony

**Hudson**: Harmony??

**Anton**: Nothing special from Harmony except we successfully passed the hardfork. 

**Hudson**: Alright.

## 6.7 Pantheon

**Hudson**: Pantheon?

**Eric**: Yes, big news this week that we release Pantheon 1.0. The big improvement there is cutting of archive sync time down, we cut it in about half. Which brings us to about half the speed of Geth on Ropsten. More to come in future releases but this is a pretty big one for us. We will be continuing to work on performance, reliability and sync. We also want to get involved with the work on the fast work POCs. We actually haven't found any details yet. SO, if you are working on that and wouldn't mind to reaching out to us or pointing out to us in the right direction, that would be much appreciated. 

**Lane**: Congrats on the 1.0 milestone.

**Hudson**: Yeah, Congrats. Eric, did you add anything?

**Eric**: Thats it, thanks.


## 6.8 Turbo Geth

**Hudson**: Turbo Geth??

**Alexey**: Hi, its me again :)
It is progressing. But I  haven't re-based for the Constantinople upgrade so it doesn't actually sync past Constantinople yet. SOmething that I have fixed recently in doing this stateless coin thing is I have this the bull GBI recently introduced in the memory only mode, where you actually put anything on the disk. It was surprisingly slow but then I found why it was slow and now I am hoping that I will have an option to basically have the entire current state  in the memory but not in the format of trie but in the format of B-tree which is much more compact and it takes about 8-10 GB if you have that sort of memory. That would result in ultra fast archive sync but I haven't tested it yet. But I would do it afterwards. At the moment I am most using Turbo Geth is basically a working horse for all the data analysis which is pretty awesome. I haven't caught up with the other things yet. 

**Hudson**: Ok

## 6.9 Nimbus

**Hudson**: Nimbus?

**Jacek**: I can give you update. Congratulation on the Constantinople release. On the Nimbus side, we are making slow progress. We are almost there for the first  sync fork. We have been able to sync like a million blocks now, running all of them through the EVM and so on, which is pretty cool. Slow and steady progress.

**Hudson**: Great.

## 6.10 Mana/Exthereum

**Hudson**: Mana/Exthereum ?

## 6.11 Mantis

**Hudson**: Mantis ?? I still want to get those devs here but I am not getting touch with the right people. 

## 6.12 Nethereum

**Hudson**: Nethereum ?


## 6.13 Web3J

**Hudson**: We have someone from Web3J. Do you have any update? 

**Ivaylo**: Nothing really apart from implementing EIP 712 right now in Web3J.



# 7. Research Updates 

**Hudson**: We have Danny go first then Vitalik.

**Danny**: I think Vitalik left. We are focused highly on the Eth 2.0 specs, the phase 0 which is the core kind of POS and stuff is through out  stable  and people are moving towards simulation and testnet and things. Phase 1 which is consensus on data of the shard chain, the bounds of which exists in the spec document but we expect this to go through highly iterative design phase, similar to phase 0 design phase. If you are interested in , check me out in proof of custody game stuff and writing,  it is probably good time to take a look. In Phase 2 , this is something that we want to see and is being ramp up the efforts in parallel. There is Vitalik headed an issue inspect repo, where we are beginning to discuss this kind of large science space. Thats generally what is going on research side. Check out a few research, if you are more interested in research area.


**Hudson**: Ok, thank you. I think thats all of the group in the agenda. 
# 8. Anything Else 
**Hudson**: Does anyone else have any item of thoughts or anything else, agenda item that weren't there? 

**Lane**: I think there was a little bit of debate on the issue about specific EIPs  that were proposed for Istanbul HF. Alex put three of them forward. Alexey had also said before we do that why don't we talk about some high level question that he brought up earlier. I just want to acknowledge that these EIPs were there. I don't want to talk about them necessarily today. 

**Alexey**: Yes there was Qn. no 4 in my comment about a deluge? Do we want to create a deluge of EIP and sort through them? Or do we want to first figure out things in a different way this time, that is my question.

**Hudson**: Do you have an idea of an alternative way to do it? 

**Alexey**: Well this comes back to my two suggestions is about the processing EIPs quicker by pointing the reviewers and potentially making the releases shorter. Therefore, we don't make everybody hostage of everybody else.  Thats my two suggestions. Generally, we might also do reflection on the past and retrospective whether we did the best we could in  the previous two releases? 

**Hudson**: We might discuss that in the next meeting. But for the moment everybody be thinking may be not putting down like on that meta EIP but thinking about the different EIPs that you would want to go to Istanbul  and we can talk about it. Feel free to put them on the agenda that I am going to put it pretty soon. 

Anything else that anybody have? 

Cool !! Bye everybody. 


# Date for next meeting
March 15, 2019

# Attendees

* Alexey Akhunov
* Anton Nashatyrev
* Charles St Louis
* Daniel Ellison (ConsenSys)
* Danno Ferrin
* Danny
* David Murdoch
* Eric Kellstrand 
* Greg Colvin
* Hudson Jameson
* Ivaylo (Web3Labs)
* Jacek Sieka
* Joseph Delong
* Karalabe (Peter)
* Lane Rettig
* Pawel Bylica
* Pooja Ranjan
* Vitalik Buterin
