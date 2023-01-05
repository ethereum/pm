# Ethereum Core Devs Meeting 77 Notes
### Meeting Date/Time: Friday 13 December 2019, 14:00 UTC
### Meeting Duration: 1 hr 35 mins
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/142)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=HpoBvMylPfk&feature=youtu.be)
### Moderator: Hudson Jameson
### Notes: Pooja Ranjan

----

# Summary

## EIP Status 
| Status | EIP |
|-------|----------|
| Push it to final when EIP reflects the additional text "that the block rewards are unchanged"       | EIP-2384, EIP-2387 |
| Discussed under EFI. Discussion to be continued in EthMagician thread | EIP-1962, EIP-1559 |
| Discussed under EFI. Decision required around needing a Hard Fork | EIP-1985 |
| Eligible for Inclusion Pending Champion. Not accepted into Berlin | EIP-1702 |
|May not be ready. Currently depends on EIP-1702 | EIP-663	|
| Eligible for Inclusion | EIP-1380, EIP-2046|
| Accepted | EIP-152, EIP-1057, EIP-1108, EIP-1344, EIP-1679, EIP-1803, EIP-1884, EIP-2028, EIP-2200|

## DECISIONS

**DECISIONS 77.1**: The difficulty bomb will be addressed at some point post Muir Glacier upgrade for push of #blocks.

**DECISIONS 77.2**: EIP 1559 - Discussion to be continued in EthMagician thread.

**DECISIONS 77.3**: EIP 1962 - Discussion to be continued in EthMagician thread.

**DECISIONS 77.4**: EIP 1057 - Accepted and final.

**DECISIONS 77.5**:  EIP 2384 - Push it to final once a line "that the block rewards are unchanged" is added in the EIP. 


## ACTION ITEMS

**ACTION 77.1**: ECH release the blog post on Muir Glacier on Monday

**ACTION 77.2**: Hudson to connect with client to get latest version for release on Muir Glacier.

**ACTION 77.3**: Hudson to create EIP IP telegram channel.

**ACTION 77.4**: Eric to be contacted to add "that the block rewards are unchanged" in the EIP. 

-----

**Hudson**: Hello everyone and welcome to the Ethereum core devs meeting # 77.

# 1. Istanbul updates, if any

**Hudson**: Let's talk about the Istanbul update that happened about a week and a day ago. Is there any update from anybody? It looks like it went well.  We had Community call that I thought went really well during it. According to Ethernode website 97% nodes are updated. Anyone else have Istanbul update?


# 2. [Muir Glacier Updates](https://eips.ethereum.org/EIPS/eip-2387)

**Hudson**: Okay so now we're at Muir Glacier. It is in last call and we're going to change that to final. The review ended yesterday and no one raised any concerns that I'm able to see in the magician's at least. I'm guessing they wouldn't have left it there as a PR.

**Tim**: So one concerned that I think was on The Magician's thread, that some people felt that the 4 million blocks was like too big of a push. A couple comments, pretty sure it's either on the EIP thread or on the hard fork thread or on the actual, I'm not sure. But they're just like a couple people saying that's like 4 million might be too far in the future. No one seem like super opposed to pushing but the amount being pushed seems problematic to few people. 

**Hudson**: Okay yeah I can see why people would think that okay but it doesn't sound like there wasn't any deal breakers though, because I'm having trouble finding it. Would you say that there wasn't anything that was like super show-stopper about any of the request?

**Peter**: So I know that's a we did the release for the Muir Glacier, the last week and they're have been a few comments, maybe a couple two or three.  And they said that it's not be released soon and or two or three people said that they don't really like it, that we push back too far. But the rationalization that they posted was that, it means that we are all of a sudden delaying Ethereum  2.0. So, for some reason people kind of link this delay to Ethereum 2.0, and from my perspective the two things are completely unrelated.

**Tim**: Those are the some of the comments. I think I just posted the [thread](https://ethereum-magicians.org/t/eip-2384-difficulty-bomb-delay/3793/15) I was referencing to. Two people seem to have concerned that if we  pushed a bomb so far does it make it harder to ship stuff like the Finality Gadget which will potentially reduce issuance for miners and what's miners incentive, upgrade to that if there's not the bomb in place anymore. So it seems like there's a little bit of concerns on the 1.0 side and or at the very least there are link between 1.0 and 2.0. It's not clear to me how like generalizable they are to the entire community?

**Hudson**: Okay, sounds good. I think that is fine then. I think we can go ahead and just continue to mark it final because the seems to be some misunderstanding with the implications of these 2.0, like Peter said. Anybody opposed?

**Peter**: Generally, my reply to these people are, we're pretty late to start the debate on weather 4 mil or 3.9 mil or however much would be more appropriate. So, my suggestion is that we go ahead with whatever, so that we can just release the thing and make sure if it still functions in a month, and if somebody feels really strongly that this is a bad number, I think it's completely fine to adjust in the next work, if someone is really opposed to it for some reason.

**Hudson**: Got it okay. I'm not finding those comments anywhere, I keep looking.

**Peter**: It's in Reddit with Geth 1.9.9 release.

**Hudson**: Okay yeah, I remember that thread. okay well I don't really need to see it. Let's go ahead and move on then then just say that **we will be addressing the difficulty bomb at some point**. I believe it'll be before the four million blocks hit.I think that's sufficient personally for dealing with the delay and adjusting it if necessary based on community feedback once that happens or after Muir glacier. I also encourage people who do feel like it's not accurate to make another EIP, that either adjust it, takes out the difficulty bomb extends the difficulty bomb, or whatever you want to do some of those could be up for consideration after Muir glacier.

**Tim**: The reason I think we should still go to final is the absolute worst case scenario seems that you know if it's true that like miners will not upgrade unless face with the difficulty bomb, which I'm not personally convinced of but given then, it seems like in the worst case, the Finality Gadget won't go live until you know the bomb kicks off which is like in a one and a half year or something like that. I'm not sure how quickly the Finality Gadget could go live, but it's like I doubt you'll see that the less than like 6 to 12 months. so at the absolute worst case scenario seems like you add  maybe another like six months before you can deploy this finality gadget either

**Peter**: I don't see that is realistic either because I think this whole miners will not upgrade originates from the Bitcoin world which is a fairly stable protocol. SO, people expect that not to change at all and you require quite a lot of force to change it back. In case of Ethereum, people are more accustomed to our regular updates. So even now we have two hard forks lined up, we have the crypto stuff that we can talk about after this one. we have Eth1.X research which will if we go down that path, will require probably multiple hard Forks. So it's not like we're freezing the Ethereum 1 as it is now.

**Tim**: I agree with that and I think the worst case scenario of like you know even if that were untrue is not that catastrophic so I think it's less catastrophic than like taking 3 months to figure out what's the right amount by which to change the difficulty bomb.

**Hudson**: Okay anybody else have comments, opposition, anything?
Actually one more Muir Glacier thing. So it activates on the  New Year's Eve.

**Peter**: Wait, when I saw that number, I also freaked out. But then I realize that there will be a difficulty increase in a couple of days that should add about 2s to every block. Its a rough idea, so someone please double check it. But if what we think is true, is true that it should bump the delay the whole thing by about 4 days. It should definitely not happen on the New Year's Eve, but please double check.

**Hudson**: Sounds good. I think we should have **a meeting in two weeks**, it can be very very light but just talk about Muir Glacier and probably recommend that people who want to bring their EIPs, maybe you should wait for a different meeting. Since it'll probably be very lightly attended, is my thinking, because it's like the week of Christmas and other holidays are kind of around that time like there's about to be New Year's Eve and New Year's. so yeah but I still think we should have the meeting in two weeks, anybody else have any comments on that?

**Tim**: yeah I think the light meeting make sense and we can put it at the agenda that it's just a discuss Muir Glacier.

**Hudson**: Or maybe we might not even need a meeting, maybe we can just decide if we want one in like a week or something. Because ya thinking about it like if we don't need one, why do it? I guess. 

**Peter**: I'm probably decide it 2 days before the deadline. Because a week before the block time wouldn't be that precise but 2 days would be pretty clear.

**Hudson**: So instead of having one in two weeks we could have one on an off-day right before Muir Glacier.

**Peter**: 2 days are. fine but will decide just few days before 2 weeks.

**Hudson**: Got it. okay we'll talk about it more on Gitter. I guess we don't need to actually decided in this call as long as we get to it in the next few days so people can kind of plan if they want.


(Just before the end of the call)


**Hudson**: I want to go back to Muir Glacier just real quick because I realized I didn't actually check with each client to see if they have a compatible version. The Ethereum Cat Herders want to release a blog post and so does blog.ethereum.org with a link to all the clients that have Muir Glacier. So let's just go through each client that's on the call and see where everybody's at. We know Geth has a client that's Muir Glacier compatible is there any other information we need to know about that or do we just go to the latest version?

**Peter**: No pretty much the only the latest version is the only one that's compatible. I think it's [Geth 1.9.9](https://github.com/ethereum/go-ethereum/releases/tag/v1.9.9).

**Hudson**: I think it is too.

**Martin**: Confirmed!

**Hudson**: Great. Aleth?
Pawel does not have a microphone, that's right. I'll just check Aleth, manually then, unless someone else can speak to it?
All right, Nethermind?

**Tomasz**: [Nethermind v1.2.6](https://github.com/NethermindEth/nethermind/releases/tag/1.2.6)

**Hudson**: okay

**Peter**: sorry just to confirm, these versions also have the Ropsten thing configured, right?

**Tomasz**: Yes, Ropsten block number and all the test passing and the mainnet block numbers.

**Peter**:Okay, Thank you.

**Hudson**: Perfect, Parity?

**Wei Tang**: We merged the block member to master but we haven't made a release yet. Expecting around the beginning of next week

**Hudson**: The beginning of next week, we can do a blog and that still gives us three weeks roughly, a little less maybe. Then we have everybody, who am I missing, as far as a client? Sorry, Besu ?

**Danno**: [Besu 1.3.6](https://github.com/hyperledger/besu/releases/1.3.6) we have on Ropsten and mainnet and we also pass the reference test.

**Hudson**: Okay, perfect. Am I missing anybody, else? 

**Tim**: We do not have a confirmation for Aleth?

**Hudson**: Pawel doesn't have his microphone working, so we'll just have to look that up.

**Pawel**: We've not done anything yet, in the beginning of the next week, we hope.

**Hudson**: Thanks for the update. Perfect,  Cat Herders are there anything else that I'm missing as far as speaking to Muir Glacier, this could be Pooja or Tim?

**Pooja**: I just have one question, like in the beginning of this call today, we discuss that it can be occurring earlier so in our post we're trying to suggest that it is coming around the January 6.  Do we need to amend it? During the Istanbul testnet when it appeared a couple of days before, we saw kind of panic; so can we change the date so that people should be prepared earlier ?

**Peter**: Well, honestly I suggest that before New Year's Eve everybody should really update. If the block numbers were consistent with the current speed that it'll actually land on New Year's Eve.

**Tim**: [Etherscan](https://etherscan.io/block/countdown/9200000) is showing the 30th now. I'm not sure how they did their calculations but yeah so it's like New Year's Eve or before.

**Pooja**: So, can we put a tentative date as like 30th of December?

**Peter**: It's kind of hard to say, because the difficulty just got bumped, 600 blocks ago. I don't know that's quarter or half an hour ago. Which kind of means that probably older estimates are a bit off now so let's wait for two more days and see what the numbers change the estimate that Etherscan and we can all suggest.

**Tim**: So, does it make sense then to **release the blog post on Monday**? Hopefully, Parity can have a release by Monday and like we can release the end of the day America's time so that means that you know Parity, I think you're all in the Europe, so it's kind of well past the end of the day. And we can use whatever numbers are on Etherscan on Monday and that should give it a couple days to readjust it's estimation, given that the difficulty change. does that make sense?

**Hudson**: That would be something we could do. What my suggestion would be would be to just say in big bold letters have this done before the end of the year but that say the estimation is currently + -5 days on January 6th plus minus 5 days.

**Tim**: I think, that doesn't really work for the worst case scenario. Like the worst case scenario is like the 30th or the 31st. I would almost be more comfortable to say to do this before Christmas in a way.

**Hudson**: Let's reassess on Monday and see if it has change.

**Pooja**: Sounds good.

**Hudson**: Awesome! yeah we can definitely talk more then and if it needs to be on Tuesday because of other clients releasing that would be fine. We don't even have Trinity on the call or Ethereum JS, so I can reach out to them manually or we can just hit up there Gitter channels.

# 3. Testing updates

**Hudson**: Testing updates, anybody have testing updates?
We can skip, Dimitri isn't here who usually has testing updates.

# 4. [Eligibility for Inclusion (EFI) EIP ](https://github.com/ethereum/EIPs/pull/2378)Review

**Hudson**: We're at the eligibility for inclusion (EFI) EIP review. The first one is going to be EIP 1559.

## EIP-1559

**Martin**: That is Fee market change. I wonder, if there is anyone here  who is it sufficiently knowledge about it?

**Rick**: Hi, it's this is Rick and Ian, the dev who wrote the patches is here as well. 

**Hudson**: Awesome, go ahead and speak on it if you'd like. 

**Rick**: Yeah, just a friendly reminder of what the purpose of it. The high-level points 
* it's an EIP by Vitalik.
* to **add stability to Gas Ether price**.
* it has some other useful side effects, in terms of **removing zero fee transaction**. And the way it does this is basically we add a base fee, we bring the gas pricing under consensus and then each transaction instead of having a single component in terms of the fee that goes to the miners. 
* you now have **two components** - some of the gas is burned and some of the gas goes to the miners, that's basically it. 
* Vitalik wrote skinny 1559 which is not what we implemented,
* we implemented what was in the implementation study which is two phases.
* another major benefit is it really simplifies. you **no longer need Ether gas station**. it really simplifies the user experience, that's much easier to figure out what your gas fee is going to be in advance. because it changes how transactions work, you know you can't just flip a switch and expect all of the downstream tooling to have changed overnight. 
To me, that was a much greater risk  and so we've **made it two phases** so that there's a period of time where both transaction types are valid which adds some complexity but I think it's necessary to actually get adoption without breaking everything. 
Any questions?

**Martin**: Yes,  actually two questions. So first of all it sounded that you're talking about EIP as one thing and implementation as  different thing. I'm kind of wondering what to discuss today? The EIP or the alternate version of the EIP?

**Rick**: Yeah, so it's the implementation. It's a pretty big change and the EIP was a little, in my opinion, a little under specified. we had hopes to have a EIP that referenced our implementation. well that's inaccurate.  what I had hoped to have happened was that we'd actually do some modeling and simulations to sort of proves that this isn't going to blow everything up. but we couldn't get funding for that. so what we got funding for was the implementation. so we wrote an implementation. And in that process, there was changes need to be made and you know the EIP is forthcoming. but those are separate tracks, those are two different people working on those things and so the implementation was the priority and it also coincidentally, frankly, happened to be done first. 

**Martin**: Okay, so it sounds to me that the this point is real **a bit too early to make some kind of call about the inclusion**. I mean, you have an implementation but not really an EIP to discuss. But I do have some more general question on 1559. So, it has this premium base fee and the premium. I don't really understand **what prevents all the miners from basically colluding and setting the base fee to 0 and still only accepting transactions which have highest premium and failing back, basically to the same situation we're out today?**

**Rick**: Before I answer that question, I completely understand what you're saying about the EIP and in the review. In my discussions with people, to be frank, it seem as though it's the shortest path to having a discussion of frankly. Since no one responded to any of my comments or anything else that wasn't. And I mean to say no one responded, I mean very few people responded. I was having a difficult time.

**Martin**: I think, it's fine. Probably, we won't be able to make a decision today. 

**Rick**:  No, I don't expect. perfect to have a discussion about. There is an averaging of the base fee over a large number of blocks and so the idea that the miners would need to kind of have an overwhelming amount of the transaction volume for a long period of time to adjust the price. They basically need to be the majority of demand, it's kind of a weird.

**Martin**: Does the base fee follow the premium ? what does the bass fee follow?

**Rick**: The base fee target the half-full block. We set up an initial value that in the original EIP, took a snapshot of time but the gas price at the time, that is deployed and so basically the idea is that initial price is set and then it can only vary so much per block and the target price is determined by taking some average number of blocks. These are the sort of questions where I thought they were very difficult to answer and  this attack that you pointed out we've sort of this sketch solution but I felt like giving the importance of the change we needed a lot more engagements actually answer a question.

**Peter**: There's another question. If I get it correctly, the idea would be the gas tries to keep blocks half-full. If blocks are getting fuller than the gas prices go up. The question is **how does this relate to the dynamic block sizes?** On Ethereum mainnet we kind of have it fixed at a million currently, but in theory, it should have been Dynamic. so if we add this, how will it do values in the place? because as the blocks are getting fuller the miners in theory will push the block size up which would make transactions cheaper and your proposal is doing the exact opposite. If we were to remove the limit on mainnet, this artificial 10 mil gas cap, then what would happen? 

**Rich**: I'm thinking about that. How do we decide what the criteria is for changing it? 

**Peter**: changing what ?

**Rich**: the 10 million gas cap. what in your suggestion, how is that changed?

**Peter**: The 10 mil gas cap limit currently, is an arbitrary limit set by miners. But based on the Ethereum protocol, it should be pushed upward if blocks are full.

**Rich**: I am sorry. That's under consensus.So, I think it would stay effectively, we don't change that, we just change the price.

**Peter**: yeah, so essentially the problem is that in theory what these Ethereum protocol specs is that if blocks are getting full, the original spec was that the gas limit should be raised. Now, you're saying that the price should be raised. But I think **it should be important to touch on  what happens on a network where we don't have this limit**. eg Rikeby. Currently, we configured if the blocks are 10 mil in size but they are allowed to go up until 15 mil if there is high network traffic. Now in this case,the trigger for pushing the block limit up would be that the blocks are full but at the same time in your EIP, this would also trigger transactions to be so expensive that the blocks won't be pushed up.I just want to make sure that we're not accidentally murdering an existing mechanism with this one.

**Rick**: Well, I appreciate that comment. I think that it would be intentional. I didn't realize that Rinkeby had that dynamic pricing or the dynamic sizing.

**Peter**: If you're creating an EIP that deliberately murders it, that's fine from my perspective. I am completely fine with proposing an EIP that clearly states that this will be murdered.

**Rick**: Thanks for the feedback. That is exactly the feedback that I was having a difficult time receiving it. 

**Martin**: I have another question, the right now there is a cap. we know that even when blocks are full, we won't go over but, here in this proposal, it looks like, we'll target 8-10 million but actually the  hard cap is at three times that amount. So it might be suddenly 24 million gas block would be valid, am I reading it right ?

**Rick**: yeah it targets much lower than. right exactly so during normal it has room for congestion.

**Martin**: It feels almost reckless, but I mean there are security implication about having the roof three times higher than where we want to be.  maybe want to be a bit more conservative actually.

**Peter**: It would be really denial of service. If somebody figures out the way to attack Ethereum all of a sudden if you have three times as much leeway.

**Rick**:  I completely agree with that and I think that if someone were able to sustain that. As far as I'm concerned you know, I sort of volunteered to shepherd the EIP through. Of course these stuff, you guys know this stuff better than anyone else. I think these are really great questions and these are exactly the types of questions that I was trying to surface prior to writing any code. but this seems to be what most of the people who were giving me feedback in the community wanted, they wanted to see the implementation before we answer these sorts of questions. 

**Hudson**: It sounds like the right way to go. I think it's good that you did that because then people can look at the code and then dissect it a little further than just a lot of hypothetical, I guess people would say.

**Rick**: It's not how I worked in my other professional capacities. I appreciate the feedback and will definitely keep that in mind.

**Hudson**: yeah taking this to like The Ethereum Magicians thread is going to be very helpful, I think to Rick and the rest of his team. so if anyone here has further stuff after looking deeper into the implementation, I think that would be important. and then even more important than that in my opinion would be an update to the EIP itself. even if it's not pushed through the EIP process having a PR that has the changes Rick that you and your team have implemented that might be different than the PR, which I think was last updated in April, that would be pretty important, so that people can comment on the latest one and not have to refer to a previous specification that's not updated.

**Rick**: yeah we'll take care of that hopefully this week.

**Hudson**: It's holiday, so it's not like huge rush or anything. 

**Peter**: Before we kind of deflecting to different topic, I want to emphasize on this because I've a feeling that it's not taken as seriously as Martin intended. Currently 10 mil gas limit that Ethereum Network is running on. The Reason why. it was capped at 8 million because that was considered the only sane limit, so that this guy doesn't murdered the network. Yes, we did some optimization and now people pushed up the gas limit to 10 mil. But, we really don't want to get into position that all of a sudden (random number) 15 million things starting to get screwy. Now if you all of a sudden allow people to expand 24 mil then  it's going to be really bad. that's why I'm saying that if we kind of currently feel that Ethereum network capacity is at 8 or 10 million, we should really have some very very hard caps in place so that you cannot really over blow the resource usage. So honestly instead of a 3x multiplier, maybe a  1.5 would be a lot more saner starting point.

**Rick**: Frankly, we went with the parameters that Vitalik  gave us, where he gave us then, so I don't know why he picked such a large value and I'll definitely keep that in mind.

**Peter**: The 3 X is not a horribly bad idea if you would look at the average Network usage. so currently gas can process blocks in them maybe around 150 milliseconds. So, if you act 3x to that, that would mean may be 0.5 sec, so that's not that bad. But the thing is the whatever people throw at it when they are using Ethereum, it's not the worst place possible effects scenario. and you need to keep the limit in control for that scenario.

**Rick**: yes so so that when he did look at the distribution, I do remember from the EIP that it was based on an assumption of block distribution that I thought didn't really fit reality, and I think that you're touching on that point from a different perspective. yeah I agree .  we're here having this discussion because I don't know how to demonstrate or simulate or make any sort of formal assertion about what that value should be? I'm definitely open to suggestion my intuition is that you would have to run a fairly robust simulation to answer that question. 

**Hudson**: Was there anyone else with comments? Anything to add at the end of Rick ? It's best to reach out to you on Ethereum magicians I'm guessing, was there any other outlets that you wanted to bring up as far as how to address this or contribute?

**Rick**: we can keep these conversation at Eth Magician, that would be great. I don't know what the convention is around PRs. I think the code size is relatively small obviously the impact is very large. when I say PRs, they mean I don't know if they want to help, people want to interact with, if they do just ping me in the gitter. [link](https://github.com/matter-labs/eip1962/tree/uint) is already provided. but If people have a hard time finding it or whatever we can sort of engage in the GitHub and EthMagicians.

**Hudson**: Awesome and just to extend my support on this, you can reach out on telegram, if you do have any questions about the EIP process or the process of getting this through for more potentially rapid discussion, I'm happy to talk to you about that.

**Rick**: Great thank you !

## [EIP-1962](https://eips.ethereum.org/EIPS/eip-1962)

**Hudson**: The next one that's eligible for inclusion EIP review is 1962. 

**Alex Vlasov**: I am here to talk about it.

**Hudson**: Perfect, go for it.

**Alex Vlasov**: First of all I am sorry for distraction. I was busy on academic side. Otherwise, there is only one major roadblock right now. this is how to measure the gas cost for a pre-compile call for one particular family. where my initial ideas on how I would do it, I actually fail. so I was kind of simulating that calls with a lot of parameters. Just drawn uniformly from available parameter space and then I was trying to do multiple parameter fitting. unfortunately dependency on some of those values, but it was a little bit weak so I couldn't factors them out and get the final formula. I will now have to do it another way by first dissecting the function call into three parts which are independent and we should have quite trivial priority parameter dependencies. then I will have to just combine the three formulas but fortunately I have to do all the measurements once again. After this event no technical problems, all the same stuff will be ported from the Rust to C++ implementation which was done before and the same way, they will be run or another facet testing to check the correspondence between those two. So, its plainly just to do some work and borrow some computation time from call provider.

**Hudson**: So this is the EIP about EC arithmetic and pairings with runtime definitions over such families as BLS12, BN, MNT4/6 is what the EIP says, right?
**Alex V**: It's a curve family which we have this problem is MNT4/6 type of Curves.

**Hudson**: yeah and I'm looking at the Fellowship of the Ethereum  magicians, it looks like has no one commented since August and the last time that someone has, it was July, that Danno talked about getting some test cases. so the ? is still that curve in order for you to generate test cases, am I reading that correctly, from The Magicians forum ?

**Alex V**: well, in the main repository where there is Rust code is rough few test factors which were dumped. Just do it for known curves can be pulled from either various papers or just where is kind of standard repository with curved descriptions. For those, I just dumped kind of binary encoded blocks which are in a right form of the input and then pre-compile should return some answer. I said yes, either boolean  or just as a series of bytes, those will be available but right now there are only two kind of implementation and almost full scale implementations which are both done by us. One in Rust and one in C++. To test correspondence between them to check for consensus between two different implementations. We do the faucet testing. For this I can definitely make a huge set of test vectors but final testing should still be done by just a lot of brute forcing and passing for difference between outputs for the same type of people.

**Martin**: The EIP links to Matter labs repository, is that the master permutation?

**Alex V**: Well there are two, one is which is my main working repository, which I use for, right now for task schedule estimation and as one is also in Matter Labs GitHub emphasis in C++ implementation which also is EIP 1962-CPP, I think. I know such people from EY as in Earnst Young were interested in trying to make an alternative one. I talked to them 3 weeks ago but they looked at the specs set of explicit formula which were also published quite a long ago on the GitHub.  but I didn't hear anything from them yet, so I would consider it for a first two implementation, it will be those two and they will be tested this way for correspondence with each other. There are two implementation  done by Matter labs. it's not kind of very much independent. I would argue that it's much easier to use just one because it lifts a lot of questions for a consensus result but it's kind of still the difference  between those two will be very small. SO, it's still  easier-to-use just one, even so while to be able to be tested for difference.

**Martin**: Right, but the core problem being here that this is extremely complex stuff. This is basically an EVM for complex cryptography.  I totally agree that it would be a lot simpler to just have one reference implementation. Because then you wouldn't actually need to specify everything in, just consensus by reference implementation. It feels kind of dangerous.

**Alex V.**: My argument is not that I want want to have separate implantation. I would want to have separate implementation but right now these two implementations that will be available in any form production ready. They will be both done by us and will be both done by the same set of public documents specs, the difference between them is so small, most likely. I mean there are different languages but the difference which one would expect will be small. Unless, it will be in next one the next one I need for this period of time, there is no next one and pretty much independent one. It's less risk to use one which will not crash, anyway give consistent results and then try to use two which are very much similar.

**Martin**: The Matter Labs documentation also contains an ABI interface description. That's part of the consensus, right?

**Alex V**:  Well, I mean the binary interface is one of the simplest parts and so binary interface is implemented in both C++  and Rust. This is just a way how you slice a byte and how you interpret each of those. he ABI part, first of all it is a repeater and it's can be changed a little bit,  but for now it looks reasonable and for the part where's the discrepancy may come, it's much larger chance that it may come from arithmetic, even while the formulas everywhere are explicit. Those are present in the separate document was also exposed to formulas. It maybe suggests jury's implementation  one check or not one just one missing. There is much larger chance that happened not in ABI  but in arithmetic. Despite a large number of lines of codes which were responsible for each of those. 

**Martin**: Yeah, I mean it's just the kind of a sign of how big this EIP is, if there is a full ABI implementation which isn't even mentioned in the core EIP. 

**Alex V**: yep because ABI design was kind of flexible and sometimes we started to make it. I can kind of make it freeze and solid, but I don't think it would help anyone. I mean having an ABI implementation without restless, isn't something which you would want to have for independent implementation. From firm's experience of previous run of faucet implementation, we've found a set of discrepancies which where kind of checks at some stuff was empty or not, for example. But we didn't find any discrepancy in ABI parsing code between our Rust and C++ implementation. It's just from empirical experience, there is much more chance to get an error there.

**Danno**: My concern is why do we even need an ABI that totally a separate function with a lot of different ways that you need to pack the parameters with a lot of different ways we need the gas, wouldn't be conceptually simpler just tto have each one of these pairs of function and curves have their own individual call and we could easily isolate the testing cases that way?

**Alex V**: This is not a problem. Yes, we can have the 20 separate formal pre-compiles for each of those. My point is the way how you pack the parameters in each of those,  it's just so similar. Basically I think two bites in ABI right now, we specify each of those calls and everything else is kind of uniform awake the way how you encode. eg., an integer using ? representation. The two bytes address, which call you do. And the rest is just uses the same set of partial functions to slice this byte and iterate in some way.  There is no dependency. Even if you separate the 20 separate functions calls, which is still fine. they will have very similar looking way, how would you call them. So, they will have their own binary interface. Maybe, I did use the ABI a little bit wrong, this is just the way how you pack the parameters mostly. Here is two bytes to specify which call you want to make.

**Danno**: why do we even need those two bytes? I mean you also know what's the issue with the gas calculation. There are different gas calculation for each curve and then to calculate this in the implementation and giant switch statement which I think could be easier just to say that this curve has his own set of functions with this gas calculation rather than this curve, you do this giant four-way \, switch depending upon which curve you're on, and you go down these complex things.

**Alex V**: Just from the perspective, how an implementation would be done. The difference between those is just literally one switch statement which is  much simpler parts and the rest of it. I mean for every function will use the entity which is a finite field and no matter which of those calls you will use, you've to first specify the parameters of these finite fields and then such parsing will be done inside the call to any of those 20 functions anyway. SO there is no good in dependency between them . That's why, when I was working on it right now I just didn't  separate them. Because there is no good separation between them. Any kind of the switch statement as a beginning, yes it tells you which functions you called but  after this all of those 20 functions use the same set of primitive to their work. since they're not that much independent and the same as for gas scheduling. I mean it still will be the same way, you just choose which function you call to do the estimations. 

**Danno**: But from a design perspective, the first thing you do is jump into a switch, maybe that's an indication that should just factor those out as independent functions. yes there's a lot of reuse  behind the scenes but why do we need to hide it behind a switch?

**Peter**: So an implementation wise, I also wanted to highlight that it's completely fine to have one single function implementation wise within the EVM that does a big huge switch and calculate everything the way that's cleanest. The reason people are suggesting the 24 or however many pre-compiles is because, the EVM is kind of old of all the other operations are structured in one way and if we were to have 24 pre-compiles, then yes maybe behind the scenes those 24 pre-compiles will just call the exact same single function. But, it would avoid introducing an extra encoding idea or concept into the EVM code itself. Currently , you can just say that you want to be on 256 multiplication, call this pre-compile, these are the parameters done whereas here, all of a sudden you also have to specify that not only do I want to call this pre-compile but I want to call something within this pre-compile. The question is that **is there a particularly good reason to add this extra complexity in the EVM level** because  of course we can make it generic and make a single big switch statement within the EVM implantation. But the EVM call level is their reason to have this extra complexity. 

**Alex V**: First of all I should know that such switch statement would anyway if happen at the level of EVM. But inside of the implementation because well at least how it's done right now. In the pre-compile implementation, just takes a set of bytes as input, internally parses it. I was  expecting this will be the way how data is passed from EVM pre-compile. This is very minor issue. The reason why I didn't want to put it initially is it. Just as a solid example, in any of those calls even if they will be 20 of those, the first parameter will  always be the same as his parameter will specify the modulus of the finite field over which one would want to work and define the curve. Even if they're 20 of those  independently, still have to specify those parameters which are very similar for each of those calls. This is not a huge statement anymore those independent calls. That's why I decided that it's kind of backward the same way if you have a similarity in the way how you call each of those. Then most like you don't want to separate them from just logical perspective. I don't have any argument that we should do one way or another strictly. If you want 20 separate functions, perfectly fine with this. I just described why I didn't put it initially.

**Peter**: So for me, having an extra ABI extraction layer just to have one single modulus. I don't care if funny function calls that have the same first parameter and you have to set so. What **I'm trying to vote against is adding extra ABI complexity just to hide something a bit further down the stack**.

**Alex V**: Okay, I mean if this is the kind of decision, I will separate this function, it is a required number of sub-calls, it's not a problem from any perspective. It's just this decision was never reach to the final point and I have always said I'm fine with any of those. If there is consensus, that we should make it 15 separate calls, then I will make it 15 separate calls, it's not a problem.  

**Martin**: From another perspective, I think it would be good for us to actually i had hard time to make out, what are the exact operations that are supported. Then I go to implementation on their side. I mean it's very hard to figure out what exactly would it be 5 different or 20 different or 50 different methods. What exactly are the operations? I think, they are vague on that. 

**Alex V**: There are few documents that describes it. Maybe I should really update it once again. I'll handle it to have a better description. In sort, what's a pre-compile does, it's a high level. It allows you  to do, right now it's 7 different operations. First of all operations which are arithmetic on Elliptic Curve defined over the prime field and there are three kind of operations which you can do there. It's an addition of points, multiplication points by scalar, and multi-exponentiations which is just very efficient how we can say from consecutive course of  multiplication  and additions of intermediate results. Those  are three functions. Then there is a set of functions which allows to do the same three principal operations - addition multiplication multi-exponentiation but not over the curve which is defined over the prime field. But over the curve which is defined over the extension. This is usually in most of the literature is used as a labeled as a G2 subgroup. Those are three more operations. The final operation is incorporation which is supported only for specific families of curves for which for a label. If I explicitly separate all of them, I will get to the number which is roughly 11 independent call. 

**Alex B**: Can I raise two different arguments? Not with the design, just in general.  **I think it's kind of premature to argue about ABI  encoding and how any of these operations should be laid out before their actual example codes using this pre-compile**. Because eventually what should be also part of the decision as the cost, the contract have to incur while interacting with these pre-compile and second the dev ex experience had to actually interact with these pre-compiles. So I guess from a language perspective, having the current ABI encoding or having individual  pre-compiles  are both kind of bad because it requires specific implementation in each language . If there is no language support then it would be some kind of an in-line assembly. Maybe another option would be just to follow the standard ABI encoding and by that it would just look like a contract. The pre-compile would look like a contract and calling a specific function and they would be clear you know what the function including is. Now probably the arguments against using the standard ABI encoding would include that, it may be just too big and therefore if he actually ? how the pre-compile would be used.  So, I guess in the pairing case it would be fine but for doing repetitive additions it would be just too big of an overhead. And the other argument I think people will say regarding the ABI encoding that it maybe just ambiguous, but I think that can be argued. 

**ALex B**: I think I can shortly answer both. I never said about using standard encoding. It maybe an option, I just didn't meter this. The cost of parsing is negligible compared to originals but I didn't estimated cost of forming an array of data in memory and during this call. This part I didn't estimate. We don't have a solid answer with this. For developer experience, I will link this to the Gitter, just to have state somewhere. There is an example of how one would call the pre-compile with the current ABI at least. Yes, settings of parameters into huge chunk of memory. But this is how you do it right now to  call the pre-compile. 

**Alex B**: On the example, I actually meant the real life example. Contract where tests would actually beneficial, which is not just like calling a single function of the pre-compile but I would assume in any case you would call it a bunch of times and different functions on the pre-compile. so I think **a complete real life example would I think be it necessary to actually reach a quick decision on the design**.

**Alex V**: I think I can write the equivalent to the current SNARK way of verification routine, how will it work with pre-compile. I think this will be a good example. There is a large reuse of the parameters which is possible to push the efficiency to the  limits that most likely developers would want and such optimization needs to be done only once.  Yes, it's not a problem to make one real life example. 

**Martin**: Great!

**Alex B**: Just one more comment regarding the cost you mentioned, I think they're too important costs will from the developer / EVM side. One the cost of preparing the message for a pre-compile, because we want to keep that cost low and  second the actual cost of the call the data sent to call I think they're the cost on the pre-compile side decoding any of these is negligible because we are creating the free compile in the first place because you think it's cheaper to do calculations on the client as opposed on EVM. SO, we want to keep the cost for the contracts, the lowest possible.

**Alex V**: For this part, if one would want to call this pre-compile to do the same set up operations over the EVM curve, obviously there will be some overhead in terms of message being prepared in memory because, one, will have to specify more parameters. After this part which I measure for  a gas cost right now. The second part which involve parsing which is negligible and then actually also arithmetic which is also required.  mostly because I don't have a way to affect how expensive is it cost of memory chunk in EVM. 
This will go substantially down, the call for pre-compile which will involve more arithmetic operations. 

**Peter**: To give an example, Axic was referring to- You're sayin that in your current ABI coding, you've 2 bytes that switch on various internal things.  It could actually happened that just setting constructing a memory that 2 bytes in the EVM will be a lot more expensive than just to have the pre-compile and just to call it. Maybe instead of using 2 bytes, using two 256-bit integers. so these bytes shifting operations are kind of expensive in the EVM an can be surprising too. Actually, what I am getting at is that if you pick an encoding that is as tight as possible that might actually cost more than picking a looser one.

**Alex V**: Well this part I didn't estimate. Reasons for having to custom ABI section is a little bit simplifying my own work because the way one scaler is encoded. they're just basically large integers. There is one byte  which tells how many bytes is after it encode this number. There is another limitation that the top byte should be meaningful. So, it's not zero. This is  kind of very simple set of checks which I would need to do and this will allow me to quickly estimate over how large numbers, I will have to do my arithmetic. Which is also beneficial to do the quick gas schedule check without actually parsing the full set of bytes and then checking again how many bits I actually have there if I have  the redundant encoding by using fixed chunks of 32 bytes. This was another reason to do the custom ABI. It is not an answer, it's just another piece of work. 

**Peter**: I guess we could always just check and see. If we'we have an actual contract for real use case then maybe it'll probably be a lot easier to just check that okay it's lot easier to encode with your ABI Axic's ABI or just a dumb  binary encoding, which would be preferable. Probably something we can try out if we have actually live codes to play with.

**Axic**: Probably my main message is that we definitely should have actual EVM implementations of contract using the pre-compile or any other pre-compile which is proposed because otherwise we're going to end up with a situation like with Blake2 where the design had no input from how you would actually use it from within the EVM and it ended up being sub-optimal in some cases. I think that applies even more to this pre-compile because it's it's like more complex . so my advice is that we should have actual examples probably written in solidity and maybe also some in using a line assembly and that should be one of those mean drivers for the design of the the ABI or how to interact with the pre-compile.

**Alex V**: yeah well it is a recent example of such code already and I will just link it together so it doesn't get lost. 

**Hudson**: All right there is an [EVMC binding](https://github.com/axic/eip1962-evmc) that was posted in the chat by Axic so if anyone's interested in that you can check out the zoom chat. Was there any other comments on this otherwise this was a great discussion and we can take everything back to The Magicians for this.

**Martin**: My last comment this that based on the specification I don't think it's possible to write consensus agreeing second implementation. I think it's only possible to do that by adopting existing code.

**Alex V**: I don't think that the specification quality is  top one, and it will still be appended. But right now specification, maybe it's just in two separate places now, I will check again. 
There are two document -  one is about basically the ABI and the verification of the input parameters and other one listed formulas which should be used to get the explicit result. 

**Martin**: Right, but they only define half a path they don't define the actual long path.

**Alex**: They do define exceptions and especially the arithmetic one, it defines exception. Luckily for us, how you can implement this arithmetic  if you use this for more explicitly.There are only two exceptions in arithmetic. Most of the exceptions which will kind of tell that pre-compiled didn't output any data. There are only two exceptions which happen in the arithmetic so it's just propagated and the pre-compile call just returns some error. There is much larger set in the ABI which is just verifications that also parameters were encoded correctly. Except of this if you just use the formulas and you just do some maths of prices, at the end of the day you'll always just get the same result. because this is how arithmetic work for us.

**Peter**: For example, if you have at least for a lot of crypto curves you can have invalid parameters. This needs to error out in the exact same way in all implementation. 

**Alex V**: Yes you are correct and this is actually there. This edge case is basically telling us if you don't have the inverse of the element which is actually the same as you, having kind of division by zero. In this case if you  encounter it anywhere in your coach you just prefer get all the way up and stays at well my code, you just propagate all the way up and say , well my code just didn't produce any output and this is an error.  if nothing like this happens, then at the end of the day, you'll get the same output in terms of it will be meaningless, but it will be the same set of bytes.

**Peter**: This is interesting question. In the Go implementation of the various crypto curve , various pre-compiles, if you input junk, it would actually just throw the whole thing out. for example of this point is not on the curve, bye bye. So, it won't just start computing junk and returning you the computation result. It will actually refused to compute it, because it does some pre-checks.

**Alex**: This is part of the checks which I go for checking the input parameters. When you're going to just formulas and formulas there is only one edge case and after you did all the checks. If they pass on the same input data, then after all the formulas you will get the same answer. There are checks for input. If you get into one of those checks, basically get an answer. There is always no result from pre-compile, so just an error on the large-scale. If you didn't hit out any of those, you'll get an answer which is always the same, if you just use the same for mode.

**Hudson**: okay, was there anything else? All right,   thanks for the discussion again **we'll just take this to the Ethereum magicians and continue working on this**. Thanks for taking your time to be on the call Alex.

**Alex**: Sure, I apologize for delay with over stuff. 

## [EIP-1057](https://eips.ethereum.org/EIPS/eip-1057)

**Hudson**: I think we're nearly done here let me go back to the agenda. We have one more EFI basically that EFI is not truly a new EIP that were discussing it's kind of just a formality that we need to all agree on for putting EIP 1057 programmatic proof of work and to EFI because it was already accepted and other ACD decisions back to basically a year ago, multiple times. So is anyone opposed to adding ProgPOW to the list of the EFI, granted that we before any of this process was discussed we made a decision on it? It kind of seemed like a like at least James and I it seems like a like a something that we would need to do just for procedural reasons so if anyone does have a comment on that feel free to talk to the gitter or bring it up here.


# 5. EIPIP (EIP Improvement Proposal) Meeting

**Hudson**: The EIPIP that you can prove a proposal meeting. I've dropped the ball on that a few times. We haven't had it yet and then I kind of start thinking about it and everyone slowing down because of the holidays so it might be better just to push it till January, unless there's a different opinion on the call and until then I can make a telegram and start you know getting people in that to have ideas and suggestions, from those who Express they wanted to be involved in it. Because, I think yeah at least Wei and I think Danno reached out and I think Pooja will be a leader on that one and a  few other people want to be involved. So I'll make a telegram for that and then probably the next core dev meeting just ask again who  wants to be in it and then add more  people along the way and then in January, will address it in a formal meeting after we collected some ideas on the telegram,  any comments review?


# 6. Review previous decisions made and action items

* [Call 76](https://github.com/ethereum/pm/pull/141/files#diff-f4372da277e245afa9faab2d0e51df8d)

**Hudson**: 76 is done, I merged it today. Because, there was a few corrections that need to be made. It's have the decision, so EIP 2348 was listed as accepted and Final that is the validated EVM contracts. Let me go to it to make sure we're on the same page. 

**Danno**: I haven't done any updates on validated EVM contract. I was going to wait until the new year to I have another round of discussions on ACD. 

**Hudson**: I wonder why we have it as final, is that mistake?

**Tim**: I think it's a typo is 2384. 2387 is the Muir Glacier hardfork EIP. SO, 2384 was the actual change in the upgrade. 

**Hudson**: Can someone let Brent know to change that?

**Pooja**: Yes, I'll take care of that.

**Hudson**: Thanks, Pooja.
Also,  EIP 2387 is put to last call that one that one is hard Fork meta for Muir Glacier. So, 87 is the meta and 84 is the difficulty delay EIP itself,  got it, okay so this just basically covers Muir Glacier. Okay if that was the decisions made, that's fine. 

**Alex B**: Last call was supposed to end yesterday?

**Hudson**: yes 

**Alex B**: We said initially, just to take the standard 2 weeks but since a couple of comments came up as Peter mentioned earlier on the call and maybe if it should be extended, because it cannot be considered final yet? I'm not sure what to say to something, really. 

**Hudson**: Honestly, I'd say that they are both Muir Glacier ones are final at this point because we address the concerns that were brought up in the comments by saying that we are going to in one way or another address the overall idea of the difficulty bomb or after Muir Glacier comes out. So I think that, that's sufficient but if anyone has a dissenting opinion speak up.

**Peter**: At this point in time, nobody will start debating and spec'ing out and releasing new clients for a brand-new change hardfork so we're going to go with it either way.

**Hudson**: yeah that's kind of the reality of it. 

**Alex**: I think there was one comment on the wording of the EIP itself , regarding 2384. In the comments said that the EIP refers to its previous difficulty form delay EIP and just explains the difference which is the block number; but the person who raised the issue said that the other one, extra deals with reduction off the block reward and **this EIP should also mention that the block rewards are unchanged.**  But it was only just a technicality on the wording of the EIP.

**Hudson**: Okay if that needs to be addressed, who thinks that needs to be addressed? Because, the last difficulty bomb adjustment did deal with issuance reduction, I believe, but since this one doesn't,why need to be included? Did they explain that in the comment?

**Tim**: I agree it might make sense to have like that one line change to say specifically this one doesn't. **I think the Meta EIP might capture some of that**. I know James have had added a section about the rationale, of like why we're doing this upgrade and about the difficulty bomb.

**Hudson**: Okay , it wouldn't  hurt to put that in there. So I would say that yeah **let's just ask Eric to have that line in there and hold it on last call** . I should say **push it to final once that line is added**,  does that sound good? I hear no descent. That's cool!

# 7. Next call
For right now let's say the **next calls in two weeks** and because we can have just a really short call if we need to and if there's not much on the agenda I can almost put it is like a semi optional call on the Gitter so we will make note in the agenda itself this will be a light call . So the people shouldn't expect a lot to get done so if you are coming to talk about an EFI EIP you might want to wait till New Year. Anyone else have any further stuff to talk about ? Everybody have a great holiday and we'll see you in two weeks.

**Date for Next Meeting**: Friday 27 Dec 2019, 14:00 UTC
Will be decided on Gitter, if there is any change. 
	
# Attendees

* Alex Vlasov
* Alex Beregszaszi (axic)
* Chami Rachid
* Daniel Ellison
* Danno Ferrin
* Felipe Faraggi
* Guillaume
* Hudson Jameson
* Iannorden
* Louis Guthmann
* Martin Holst Swende
* Pawel Bylica
* Péter Szilágyi
* Pooja Ranjan
* Rachid CHAMI
* Rick Dudley
* Tim Beiko
* Tentonvanepps
* Tomasz Stanczak
* Wei Tang

## Links discussed in call:

* Muir Glacier discussion: https://ethereum-magicians.org/t/eip-2384-difficulty-bomb-delay/3793/15
* link to code: https://github.com/matter-labs/eip1962/tree/uint
* 1962: https://eips.ethereum.org/EIPS/eip-1962
* There is also an EVMC binding here: https://github.com/axic/eip1962-evmc
* https://etherscan.io/block/countdown/9200000
