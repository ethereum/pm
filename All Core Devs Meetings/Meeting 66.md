# Ethereum Core Devs Meeting 66 Notes
### Meeting Date/Time: Friday 26 July 2019 at 14:00 UTC
### Meeting Duration: 1hr 40mins
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/113)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=DzmfR2P9kFk)
### Moderator: Tim Beiko
### Notes: Pooja Ranjan
	
----
	
# Summary
	
### DECISIONS MADE
	
**DECISION 66.1** : 1344 will be part of Istanbul.

**DECISION 66.2** : 2200 accepted.

**DECISION 66.3** : 1057 re-entered in Istanbul.

**DECISION 66.4** : Take the list of what we currently have and make it into two hardforks. Concurrently we start planning for the next public fork to get extra EIPs in.  

**DECISION 66.5** : Istanbul fork on Ropsten on September 4th, 2019. 
**Accepted EIPs** are 
* 1108 (Reprice alt_bn128)
* 2024 (Blake2b) / 152 
* 2028 (CallData Gas Reduction)
* 1344 (Chain ID Opcode)
 
 **Tentatively accepted EIPs** are 
* 2200 (1283 + 1706) around the s store which got the one that got pulled out of Constantinople 
* 1962 (Generic ECC Precompile) 
* 1057 (ProgPOW)
* 1884 (Trie Dependant Repricing)

1702 (Account Versioning), we are not sure where that ends.

**DECISION 66.6** : Last opportunity to get on the tentative accepted list is before the next ACD call.

**DECISION 66.7** : 1829 is out of the fork.
	
	
-----
	
**Tim**: Welcome everyone! 

# 1. Istanbul EIPs go/no-go

**Tim**: Main thing we want to resolve is which EIPs go in Istanbul. Right before the call references are updated. **So far 4 EIPs have been properly accepted**.
* 1108
* 1702
* 2024
* 2028

Couple of EIPs are rejected on last call. James can't make the call today. 


## **EIP 1344**

**Tim**: Let's go over EIPs that we didn't get a resolution on. First is 1344. Does anyone want to chime in on that?

**Bryant**: I am here. I am championing 1344. What I can tell there is a whole lot of contention about it going in. There is some talk about implementation detail behing it. And I'm not quite sure how much needs to be captured in the idea at this point? or how much is actually just implementation details discussed?

**Peter**: You're talking about the Chain Id EIP? The previous more complicated ones were rejected and the question is whether this can go in?

**Bryant**: Yes, there are some opcodes that returns the chain id. There were sme discussions whether the chain id comes from the field in the transaction or a field inside the client. There is a lot of trade off there but not sure if it's actually going in.

**Peter**: Looks good to me. I would say it's safer to take the chain id that's withing the chain and not the transaction because transactions are still valid which don't have a chain id. Thant might be a bit of a surprise your smart contract all of a sudden can or cannot receive different chain id on the same chain.

**Bryant**: I agree with you there. I think there is another EIP about adding it to JSON RPC. So, it even make more sense in that case that you just have a client provided number. 

**Peter**: It seems pretty obvious to me. 

**Tim**: Does anyone have any objections to 1344 or do we agree it's accepted for Istanbul?

**Alex**: Just to clarify, it means the chain id opcode is entirely decoupled from the transaction. And the use for accepting the transactions outside of the scope.

**Bryant**: yeah so all it says that there's an opcode when you call it and returns a number we don't know what the number is. It returns a number and implementation detail doesn't come from transaction, somewhere inside the client and like it's safer. And generally I think more people are on board with the client just providing a number is the same one that transactions would get rejected if they don't have that number. It was a question on whether like you want to go deeper maybe inside a different EIP about actually rejecting transactions that don't have that number at some point so we don't run into a situation. But there's so many ways to jump on the rabbit hole on this one. I think just considering a number that is provided by.

**Alex**: I guess the last clarification there was some discussion what would happen if there's no chain ID in the transaction. Then there were different proposals what would be the value return; but all of these issues are non issue if the value comes from the client and not from the transaction.

**Bryant**: That is correct, yes. 

**Tim**: So Alex, just to be clear, this address your concerns?

**Alex**: I just wanted to clarify it to myself and maybe to others on the call it sounds reasonable to me. 

**Tim**: So, do we have consensus that this is expected, does anyone disagree?
Okay so **1344 will be part of Istanbul**.




## EIP 1283/1706/2200



**Tim**: Next one on the list was the whole set of 1283 / 1706 / 2200. I'm seeing from the Gitter that there was some issues that were brought up this week but don't seem to have been addressed; I don't know if anyone can comment on that?

**Peter**: Where are you pulling these numbers from this, because I can't find the list that you're looking at ?

**Tim**: Agenda on GitHub. So 1283 was the one Net Gas Metering for SSTORE that got removed from the Constantinople and then 1706 was the fix for Istanbul. Then on the last call, Wei had proposed EIP 2200 but that might still be a [PR](https://github.com/ethereum/EIPs/pull/2200) and not a proper EIP yet, which was basically a combination of both. If no one on the call has the strong opinion then maybe we move on and then call for it later on. 

**Peter**: One thing I want to ask if any one oppose to accepting some variation of this. From my perspective those thing that we have to decide is whether we want to implement this feature. And that if we do alternate plan to this feature then probably client developer will start hacking on it and there will be some minor tweeks. To be honest, the three EIPs are more or less the same thing. So, technical variation aside, it's trying to do the same thing.

**Tim**: That's the consensus we had in the last call, like feature-wise it seem like people agreed but the documentation issue hasn't been worked out. I believe, Pawel had highlighted an issue about it last week. I think that was the the main remaining concern.
So this is the [link]( https://gitter.im/ethereum/AllCoreDevs?at=5d31988ae2d1aa6688d09f39) to the issues that were brought up I don't know if anyone can speak to this.

**Alexey**: Oh yeah so this is Alexey so basically the whole thing about 2200 there was an extra bit which I think was migrated from another EIP that is at the end of the opcode is checking the remaining gas and if the remaining gases is less than 2200 then it fails. So, it's basically something depending on gas left and I think there was a bit of a problem with that. So it might actually preclude certain optimisations that's what I understood from Pawel. I was suggesting to make it to restructure in a different way, basically to make a mandatory charge of 2300 in the beginning of the opcode so that it doesn't have a branching on the remaining gas and then adjust all the other bits to refund a bit more. And somebody pointed out that it's not equivalent because of the refund limit because the funds are limited to the half of the of the spend to gas and things like this. I don't know where this conversation went. I don't have a strong preferences either way, but that was my suggestion. 

**Tim**: To come back to  Peter's Point around do we want this feature and can people just hack on it to get to something, given that we're supposed to hardfork the testnets on I think it was August 14th so this is like 2 and 1/2 3 weeks from now. Do we feel there is sufficient time to resolve those issues?

**Peter**: Well, I think I'm missing something about forking in 2 weeks, that's kind of news to me. Given that we are talking about which EIPs to expect, does anyone here thinks that we are going to fork in two weeks?

**Tim**: To be clear, I took this number from the original roadmap we had for Istanbul. So, I think August 14th was the date and then the upgrade was supposed to be right after DEVCON. I don't have the date handy but it was something like October 16th. That was a point further down the agenda but obviously yeah it does have an impact if we have enough time to implement these changes.

**Peter**: To be honest, as long as we don't have a final list of EIPs, I don't see the point of agreeing on a date because we have no idea how much work it would take. But I can promise you that this won't be done in 2 weeks.

**Danno**: Is it time to have a general discussion about schedule, if the current schedule is achievable?

**Peter**: May be we first finish the EIPs first. 

**Tim**: If this EIP was independent of hardfork schedule, is this something we agree that we want for Istanbul?

**Peter**: So this EIP is a relatively simple. I mean I haven't looked into the technical details, but the previous one that was cancled in the end. It's not a hard EIP to code, so it may be 50 lines  of code.  So I don't see any particular issue of excluding this just because of timing concerns. And I think it's a useful feature. Unless there is a technical reason to not accept, I think we should go forward with current variation of this. 

**Alex**: So, we're still talking about 1283?

**Tim**: yes 

**Alex**: I think 1283 is implemented in most of the clients. But, the last call we decided it should go together with [1706](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1706.md) which is the extra check. I don't think it's implemented anywhere. But that's where Pawel build up his other option. We should introduce kind of new semi static mode.

**Peter**: Can you please link the EIP because I've no idea what you guys are talking about? 

**Alex**: So the coming from Pawel is the last [message](https://github.com/alex-forshtat-tbk/EIPs/issues/1#issuecomment-508693797) from Tim on the chat. That says that the calling a contract for the stipend only would disallow  sstore in any other state modification except logs. it just would be another option to solve the re-entrance issue discovered with 1283.
My question is maybe to Peter and the others on the call. I do like the semi static mode idea, but is it  realistic to be implemented ? 

**Peter**: I'm still looking for the EIP.

**Alex**: it's a comment 

**Peter**: Well, this discussion that you refer to says that the EIP 1706 discussion. I have no idea what EIP 1706 is?

**Alex**: I see where you're confused. so yeah it's on the EIP. Pawel's comment is the alternative solution and you don't need to know what 1706 does. Because you can just handle the idea, on it's own. 

**Danno**: So 1706, I was just the part where they charge tried to 2300 check and filling out that store.  2200 include that entirely.

**Tim**: So is it worth moving on to something else or do we want to wrap up this discussion ? Or does everyone just need time to look at the different options?

**Peter**: Just to react, I haven't seen this semi-static thing up until now or I somehow missed it. But personally I don't really like the idea of introducing yet another internal states to the EVM that tracks whatever. I mean from my perspective, we're going to shoot ourselves in the foot eventually with the more these behavioral subtleties we introduce. So, if there 's an alternative that can work around and not having these special cases then I would go with that. 

**Danno**: What alternative is to hide it behind the versioning flag. Only allowed 1283 to be uses on newly deployed code with the 1702. 1702 is the version EIP. That's  a discussion later down - which of these EIPs we have, are subjective to versioning and which ones are going to be under all versions of the EVM? On the section the one that's enumerated 1706 is to use versioning. But people felt that they wanted to have this available to previous existing Dapp developers because we try it on Constantinople. There is some some feeling we should try it at least subversion 0.

**Peter**: So honestly, I'm not a fan of version accounts because then we have to maintain two EVM. That's a different discussion but I would really like to not have special features for different versions as much as possible.

**Danno**: This is more different accounting in different versions not as a  special featuring different versions.

**Peter**: But if there's a way to solve it for uniformly for everybody then why would we pick a solution that doesn't solve it for old accounts?

**Alexey**: My comment on the versioning EIP. Originally the real reason why it came up,  there was two reasons why it came up 
1. first of all was the EIP 615 which was the static jump and extensions to the EVM which has now  been withdrawn.
2. then did another reason for that was the potential introduction and Ewasm engine into the Eth1.0.0, which is now also not very uncertain, probably not going to happen. 
So from my point of view, we lost the appeal for it. We lost the real initial reason why the account versioning was proposed.

**Danno**: So, that's the discussion I want to have after we get it some resolution today on some of the EIPs was number two on the discussion. I kind of agree if we don't have 615 or EVM then, do we need versioning now or do we bring it in then? But, do we  want to table 1283 and discuss versioning or do we want get resolution on 1283 first?

**Peter**: I just wanted to say that if there is a version of topic 3 that can solve issues for all the accounts and doesn't require versioning and doesn't require behavioral changes to the EVM. I mean adding extra subtle EVM modes then I would just go with that. Problem solve self-containe the EIP, done. 


**Danno**: I think it's a trilemma. I don't think we can get all three. 

**Alexey**: Well I think this is what the EIP 2200 does, right? It basically the combination of the old one, 1283 + extra fix  for the stipends and it doesn't introduce any extra EVM features. I think that's what it is.

**Peter**: That's exactly what I wanted to say that if this last version 00 let me to 00 fix, then that seems like the correct choice to make and it seems like a good thing to have in the next hardfork. So unless somebody can actually say a legitimate technical reason why 2200 shouldn't go in, I don't see a reason why it shouldn't go in.

**Tim**: So does anyone on this call have a technical reason?
So, I think at the very least it make sense to use 2200 as this sort of going forward point for discussion on this. So at last week's call, we were so  spread across all different EIPs. Do we want to say 2200 is accepted or do we still need to flesh out those technical details before we are comfortable accepting it?

**Alexey**: I think it should be accepted but I do understand that there are some new optimization reintroduces.

**Tim**: Does anyone oppose accepting 2200 ? Okay !!

**Peter**: At this point **we should just implement it and then have a discussion based on an existing implantation whether its meaningful or not**. 

**Tim**: Sounds good. And just to be  100% sure, I understand this is the **equivalent to accepted**, right?

**Peter**: I would say Yes.

**Tim**: Got it.




## EIP 1057

(TimeStamp : 27:50)

**Tim**: Next one on the list is 1057 ProgPOW. I'm not sure if everyone here saw, but that there was a [blog post](https://medium.com/least-authority/https-medium-com-least-authority-kicking-off-our-review-of-progpow-be1368ae9a50) about the audits that came out this week. Basically saying that I think the audit should be done by the end of August. Does anyone wants to speak to ProgPOW?

**Danno**: Oh no, no one else is interested? Is anyone else interested in a word  about it ? 

**Peter**: Well, I guess it's just a question I think the hard part in ProgPOW  is actually implementing it but as far as I know more or less every client has already implemented it. So I guess the discussion is whether we go ahead with it or not and that probably depends on the results of the audit.

**Danno**:  And I don't think that the audit is going to come back without remediation recommendations. I do have a concern about the hashrate changing at the fork block and a potential change stalling issue. That's something that they're looking at. And I think the timing of the audit is coming back, I don't think, we have enough time to fully digest or mediate it before we need to decide go no-go for testnet. In fact, according to the original schedule the test that should have been launched. The testnet putting the Istanbul changes should have been launched by the time  audit comes back. So for those Reasons I'm not comfortable putting it at Istanbul. I  much rather see something like this either in the next fork in April or on its own to work independently if other developers support it well.

**Peter**: Just to counter that, I guess  we can expect that they won't be changes made to the ProgPOW.

**Danno**: We don't know what's going to come back from the audit, should we wait until we know what's come back from the audit?

**Tim**: And on that point the Auditors Lease Authority said they would come and present this on the All Core Devs call, once it's done. But realistically, that would be end of August or early September.

**Bryant**: I also think you'd like the political contentiousness of it having it in Istanbul would be a risk for Istanbul being adopted? I think the majority of people would prefer to be its own separate fork.

**Peter**: What I want to say is that ProgPOW is really ultra separate EIP that could be pulled even at the last minute. So one alternative would be to consider it doable and if the auditors come back and tell us that it's a no-go for whatever reason. I think it should be really easy and simple to just tear it even at the last moment. From this perspective, it's a bit tough and bit of an easier EIP then, than other ones which mess with the EVM. Because this one is just the stand-alone separate thing that doesn't touch consensus, that doesn't touch anything or I mean doesn't touch execution concerns.

**Danno**: What is the last moment, before the testnet launch or the mainnet launch?

**Peter**: Well, I had the suggestion that instead of the hardforking the testnet what we could do is create the so called "shadow fork", where we don't upgrade to the testnet rather we just create a side chain for the test. So we still propagate the same transaction, we just start executing with this new engine. It would be public but clients who don't buy before switch over, they could rather have a special flag that says play around with this testnet. And then you have the feedback that you can see the clients agree with each other. You can test everything but it's not live yet officially. The chain will be discarded anyway or could be discarded. I don't really want to figure out the new forking strategies at this point.

**James**: And we also haven't forked the testnets yet. I agree with Peter then we should continue as The Core Devs have already said which is accepted, pending on the audit given that technically pulling it out isn't that big of a thing then I don't think we need to say hey let's stop at today we are actually is anything running to you and stop it from being in.

**Danno**:  Are we going to fork the testnet according to schedule or we are going to schedule out? Because if we're not going to move the schedule out, it has been stated the audit will not come back before we have to commit the code to test them to the current  forking strategy.

**James**: Well, the schedule is going to be a later part on this call so far we're just going through EIPs.  

**Danno**: Okay so **if it can be pulled out of the  testnet then consider it in**.

**Tim**:  Okay and I think we might want to re-discuss this after the schedule but for now does anyone has any final comments on ProgPOW? 



###  EIP 1962
(Time Stamp 34:10)



**Tim**: Okay moving on the last one was 1962. There was an update for its [posted](https://github.com/ethereum/pm/issues/113#issuecomment-515403686) in the agenda.

**Alex G.**: I can summarize what has he done since last week the discussion on the call and in the forums. We integrated the C++ clients into Geth. Now it compiles seamlessly so developers have a choice that they want to use Rust with some additional compiling compilation or just use the C++ version, just make it. We have started the **fuzzing testing**  and it's **running for 6 days already now with 32 core**. SO, its like over half a year as a testing running with **12  million operations per hour**. And we indeed found four  cases where the clients mismatched. It was due to last version not following the input specification precisely which was corrected. No problems into the arithmetic itself were found. And  finally we have implemented the library for conveniently calling the EIP, which is what you just referred to. You can take a look at the examples there, if you want to call the function. We have some further questions from the community which we need to get answers to understand what's decided to do so. There is **a concern that we should have multiple separates address for this precompile**. We would like to understand to take some decision and we can do either version. It's very easy to adopt. At the moment, the library hide all the complexities of having the first byte determining the operation. but if you decide that it's better to have separate addresses, we can easily do this, this is the first question.
The second question is, **is the current pace of fuzzy testing enough or do we need to increase add more hardware to support more than 32 parallel processes**, so we can get two years of CPU time in testing? The Gas metering is in progress so gas metering functions are there, we just need to get the proper constants. And we want to collect more data for this and then we will proceed to the state tests and implement tests which can be run by every client consistently.
There was a concern about the specification. We wanted to prepare it for this call but unfortunately Alex who is in charge of the precompile is sick that he needs a few more days to recover then we will do the second part. The first part was the specification for the input formats, which we already have. And the second part was for  what was actually happening the formulas which are very straightforward arithmetics, we just need to put the formulas there and put gas metering in constant in  place and then everybody can follow the instructions and implement as we compile directly from the specs. Its going to be a very straight forward process. It took us just one week to implement the C++ version. I don't expect much difficulty, if still there, we are happy to assist anybody to do so. To come to the question, do we need separate addresses for operations or can we keep one with this library, increasing or not the fuzzing testing parallelism, thats two questions.

**Peter**: I am not familiar with the EIP apart from I saw it before, but thats kind of it. However, is there a particular reason why people are asking to have separate precompiles?

**Alex G**: I think the main reason was the ability of calling, its more natural to call different precompiles  for different operations. Although they are doing their sync code under the hood. I think this is addressed by the library. Because the library makes it very easy to call any elliptic curve, any operation. It backs all the parameters together with nice typing with every entity like the point or point there having separate structure. So I think this is addressed by this but if anybody disagrees, we can switch to also having different addresses.

**Danno**: SO, I have been the one asking for four addresses. One of **my big concerns** is we **have to read the byte stream and interpret and based on that branch on four different functions for the gas calculation**. If we're doing four separate not just constants but straight up different formulas in the gas. It sounds like something that should be split up into at least four and because there's a G2 G3 separation 7 methods to calculate the gas so we don't have to basically run the library program to calculate the gas. If we keep the gas function where there's seven main branches get seven main functions.
The **second thing** is also **this matches the design pattern of what went on the EC with the RPM 128 function**. There is a pad, I multiply the pairing check . This library adds an exponentiation and is also for G1 and G2. So, I also follow what we've been doing with our other pre-compiled were there. There is basically one function and not one giant function hiding seven different functions with four different gas calculation formulas. I think it would be a better reflection of the true complexity of what's going on here.  I think parameterizing the particular curves is fine but I think the operation  should match existing pattern we have without.

**Alexey**: I  actually just now thought about it.  I know a lot of people do not read the bytecode but some people do.  when you read the bytecode and you see the pre-compiled code, that basically put the address of the caller of the other pre-compiled onto the stack and then you do another six things in the stack and I need you to call. And usually if you know what you're calling, you can actually see from the bytecode that you're actually pulling.  However if you encode the function as the first byte of the parameter than it actually ends up in memory somewhere and it might not be obvious where it is. I guess, from the EVM bytecode readability will be easier to identify which precompile is calling. And might not also be easier from a static analysis point of view. But as I said that not many people read but sometimes I do. 

**Alex G.**: Okay so we can switch to this. Does anybody disagree with **switching to having separate addresses** for the operations? 
It seems  there is consensus, so we will just change the code to this. 
Then the second question is do we need to increase the parallelism  or do you guys think it will be enough to have 32 parallel processes for the remaining time?

**Danno**: Until we have an implementation that's written by a patent author,  the fuzz testing is good but we won't get the real value until we have the independent implementation in the fuzzing.

**Peter**: It would be nice if Martin could weigh in who adores anyone who has been fuzzing because from my perspective I can't meaningfully say anything

**Alex G**: So if everybody's sound I assume, we can continue for like this for now. If somebody has a concern that this is not enough, please just post it to the forum or to the chat and then we can increase. In my opinion 32 is fine because we're going to run it for several months and it's going to be overall  years of CPU runtime with 12 million operation per hour would be fine.

**Tim**: Thanks Alex. Again just for clarity are we saying, we want this accepted for Istanbul and to start working on independent implementation? Does anyone oppose starting to work on client implementations?

**Peter**: If you guys want to **fork anything in 2 weeks**, I can guarantee that **this won't make it**. At this point if anyone wants to create an alternative implantation.

**Alex G**: We already have two different implementations in different languages one was created in 1 week. So if somebody wants to create it in different language we can assist and even help with resources. The question is whether anybody wants to do it at all because the formulas are direct like it's purely functional. There is no state. The complexity is actually much lower than lower complexity function with state by orders of magnitudes. People can just use what we have with a choice of Rust or C++. If somebody wants to implement a separate version then its perfectly doable now, if at all there is such a desire. We should simply define a criteria for this precompile, which is a very long awaited pre-compile for from  in two years from now. We won't meet any update on this until we have a fully flexible Wasm implementation because it covers all the cases. People who want to do anything with the elliptic curves will be able to do it. If we find a new curve people can use it. SO, if we want this at all in Ethereum ever, we should just define criteria. When this is fulfilled then we can include it.  If we don't define the criteria now, if the criteria is never going to be fulfilled then it will never make it into Ethereum and it's gonna be pity. Because people really know any of this. If you define the criteria now then we can see okay, can we fulfill them by this hardfork.

**Danno**: There is a criteria that Beacon chain is using for their launch and that is two independent author representations on fully compatible Beacon chain. I think that's one criteria that should be added is that there should be an implantation independently. I'm willing to do that but I agree with Peter the deadline if we're going to fork for the schedule is rather risky. As I mean the EIP is supposed to be finished in may not continue to be had to go through halfway through July. So that's one of the issues are having with the schedule. Is it that we had this details of where this EIP was in as of May, it would have been easier get that independent implementation done before the fork. 

**Alexey**: Well you know, basically after this process of weeding out and I'm pretty sure that most of the EIPs are now going to be dropped out and if we say that  we going to stick to the schedule then it looks like, for example this EIP might not make it, okay that's fine. But we basically going to end up with maybe like three or four very simple EIP to implement. That's fine if we want to do that to just to keep up to the schedule but that also means that these these things are pretty simple then I would also propose that you do another upgrade may be shortly after that one with the more substantial features because basically the Istanbul is going to be pretty much chain id, the little bit of Gas reduction in with something else. That will be like three things. For me this pre-compile is actually one of the main features of the next release.

**Peter**: Yeah so I kind of agree there, that just for the net gas metering and for Chain id,  I don't see a reason to hardfork because it's just a huge coordination. I mean I don't see the value of it. From my perspective, I'm perfectly fine if we decide that we wanted to have ProgPOW and this one in and we're going to push the fork up until the point where these two get in. I think, from my perspective that is acceptable.

**Danno**: There is also intrinsic gas cost reduction  and blake 2b was missed in that list.

 
## Other EIPs to consider for Istanbul
(Time stamp 49:30)


**Tim**: There was only a single more EIP that someone wanted to discuss which was **1884**. Alex you asked if Martin had thoughts on that and he's not on the call so it might make sense to just move to the schedule discussion because we've been hinting at it across every single EIP, does that make sense?

**Danno**: Let's do schedule.

**Tim**: Yeah, Alex, I was saying right now the accepted EIPs we have for Istanbul are the chain id opcodes, net gas metering, percompile and blake 2b to be an account versioning

**Alexey**: There is also **2028**, which is intrinsic gas reduction.

**Peter**: Did we accept **account versioning**?

**Danno**: About a month ago, yes.

**Peter**: There is absolutely no point because nothing is going to use it.

**Alexey**: Yeah, I would suggest to actually retract it because I don't see the point in doing account versioning anymore.

**Peter**: If something is going to use it then sure but if we're going to introduce account versions and we absolutely have zero use cases for it then that seems  like  a dangerous path.

**Danno**: I agree with that. That was one of the things that's on the agenda, right before the schedule ,I think is.  Which EIPs going - the new b1 for account versioning and  which ones don't. And you're right, it was brought in for 615 , it was brought in for eWasam and since those have been pushed strongly out of Istanbul. The authors are like giving up on it because of the political issues. But I still think they're valuable and I want to come back. But 1702 was really in for that and if we really don't have any need for it then let's keep everything on one versioning, do you think that make sense?

**Casey**: It has been suggested to use versioning 1702 for particle gas cost reductions that we like to do in the particle gas costs EIP  2045 

**Wei**: For the 702 there is balancing. At this moment all of our EIPs are pretty simple, but I would still propose that we include the account versioning in testing because I mean they'll provide a stable ground  because there are other use depending on that. Also, if we want to do some other stuff like I also have some of other ideas that have yet is depending on  conversioning. So, if we're kind of having a really stable ground, it will be good thing.


**Alexey**:  I don't think that the State Rent EIPs actually depend on account versioning. Some of it are actually conflicting  with it. so which means that they are basically have to be made in sequence way, but they are not depending on account versioning.

**Wei**: Yeah but I would pretty opposed if we do provider the state rents like the additional account items item without a conversioning because. That way you will be like quite a match for the account RLPs.

**Peter**: Like I said I'm against this account versioning is that this seems like an abstraction that we want to ask. So that later we can build stuff on top of it but you don't have yet the stuff to build on top of it.
My concern is that you're going to shoot ourselves in the foot by deploying an account versioning that later may turn out to be not perfectly suitable for whatever use cases  that's why I personally would say that account versioning should go in than when we actually have a use this for it.

**Wei**: yeah but like what I'm saying is that I've seen it's a good thing if clients can implement it at this moment and so it'll be a lot easier for other features appearance. Like if it only included in testing and it's kind of like because it's a big feature like pushed into the future. and all those features depending on account versioning  will be like quite hard implementing. 



# 2. EIP Refactoring

**Alexey**: I brought another solution on this line and I've put it in the agenda for two times in a row for the meetings but never managed to get to it. So it's called the **pre-emptive refactoring**. I understand what you're talking about. But maybe if we get to this point, we can discuss there.

**Tim**: Yeah these past calls we haven't gotten through a lot on the agends. So, in that spirit, may be just to bring back the conversation around the roadmap. I wish we wanted to discuss. It seems there's  **3 big things** that might benefit from extra time on roadmap: 
1. 1962 which we just discussed 
2. ProgPOW because the audit will be due late August, so realistically mid-september; everyone will have to wrap their heads around the audit
3. Alexey, we've discussed your EIPs and you've mentioned before that you might not be ready for the actual Istanbul deadlines.

I guess there's two sides to this : 
* one is **how much extra time** would we need if we wanted to take on these more ambitious changes and
* second how do we **make sure** that if we extended the deadline **we're not in the same position** as two months from now because we got whole other barrage of EIPs  to go through?
 
**Danno**: If we delay we don't accept any more EIPs. If you're not on the list,  I don't think we should allow  anymore open calls for EIPs. That's going to be in the next time of the community open call happens.  
My thought is we have two realistic options. 1 month or to delay 3 months because we don't want o hardfork over Christmas, that's not an ideal situation

**Alexey**: Or another option is to not delay and basically do what we already have and then try to do whatever we can do that timeline and then see. Beacuse, it's again another experiment to we're trying to do here. Maybe we can do the another hardfork shortly after that because we discussed in the past that we wanted to make the hardfork which are more meaningful but also potentially, as soon as something is really ready and high quality and is really in demand, why not put it in?

**Wei**: Just want to say from client implementation perspective, I will be in favor of having simple hardforks than complex. It's just simpler to test and harder to make mistakes and nice things out. 

**Tim**: So one idea we are having here to discuss that is having the hard Fork as scheduled then potentially having another fork in January, which would include too big / too ambitious / too contentious for Istanbul. In parallel, trying to start organizing another public hardfork for April or later than April. But basically, we will have Istanbul on schedule. Whatever was too big for Istanbul, in another HF shortly after and a bit after that we have another HF open for new EIPs, which will basically happen in parallel to Istanbul +HF.

**Wei**: Does it mean we have a HF after Istanbul which is only like two or three months? I think, that's quite a short time and I worry that some clients may need balancing and bounds for the release. Need time to inform the community and to gather the miners and exchangers on the same page. I think that might be a little short. We also need a lot of time for testing.

**Peter**: I think **the idea was that we take the list of what we currently have and make it into two hardforks**. Essentially everything that simple and that can be finished really fast and can be implemented fast then we start this whole procedure of testing it and rolling it out etc. But, concurrently we can already start working on the on the second part of that list - ProgPOW or the crypto stuff. Essentially,  we don't have to wait until the Istanbul HF passes to start working on the heavy PR. So, that would be the advantage of this approach where we have this Istanbul is open where anyone could suggest anything and then we have his follow-up PR which is just the hand picked heavy modifications where the teams can actually focus on those two or three EIPs which are really happy and it's not open to the public. In the meantime, **concurrently**, we can already **start planning for the next** public  thing to get extra stuff in.  

**Danno**: Here's an idea, let's keep the opening dates the same and just move the actual hardfork out for July.

**Tim**: Oh, so you would open them the same as you would have opened the April one, is that what you're saying?

**Danno**: Yeah because we need the time to sit through all the entries.

**Tim**: Does anyone disagrees with this from schedule perspective to break Istanbul out in two parts - have our agreed upon schedule which implies we fork a testnet in 2-3 weeks time and then mainnet upgrades will happen in January and July. 

**Peter**: I am still convinced, we can not fork the testnet in 2 weeks time because there are EIPs to be implemented, somewhat tested because people still rely on testnet so you can't just blow it up. After it's implemented and semi tested or it seems to be solid butthen clients need to do the releases, people need to upgrade to testnet otherwise testnet going to fall apart and become unusable. 
You need I would say after everything for the EIPs are  implemented they seem to be working okay cross client mini test, that also work, at that point if clients with the release; I would say you still need two weeks to convince people to operate and I think shorter is not realisti. it's just going to be chaos.

**Wei**:  I like the idea in general. From client implementation perspective, I just think January days is a little bit short because it's only 2-3 months after October. The  1st one is in  October. So if we move that a little bit further to February, I think it will be a little better.

**Danno**: I think the original idea was that we actually try to implement this piece on the schedule date for original Istanbul - October. Only if we see that it's not enough time by a few weeks then we can pull them over to the second part. But we  actually have a chance to also get them in October.

**Peter**: No, if you fork the testnet then you need to stick to that. We can't fork the testnet with half the EIPs and then do a big fork with extra EIPs.

**Tim**: Wei, to come back to your point; you're saying January is too early even if we're just doing these extra Istanbul EIPs, is that correct ?

**Wei**: My point is it is too short because we're doing two forks in a row which is too short to each other because clients will need to make releases and we need to inform to other people.

**Alex G**: Can somebody summarize these bigger EIPs which will go in the second part?

**Danno**: ProgPOW, EC

**Tim**: Potentially some of the state rent EIPs.

**Alexeys**: So far we got, one of the state rent EIPs,  if we don't have time to do the precompile, then thats and the ProgPOW.

**Tim**: Coming back to your point Peter, around the 2 weeks not being realistic no matter what if we push that out one month so instead of middle Aug -  mid-September and then to hard Fork instead of mid-October mid-November and then also have a hard Fork potentially in February, which is still like a 3-4 months. I guess I just tried to see if we do push out  Istanbul one month because and you would like there's no way we get it out in 2 weeks what does a schedule look like?

**Alex G**:Will we be able to include all the big EIPs, what are the other ones except 1962? 

**Tim**: I think what Peter was saying is that  the current timeline for Istanbul is not realistic even if it benefits only the simple EIPs.  

**Peter**: My concern is not with the Istanbul, rather with the testnet, the Istanbul fork for testnets.

**Tim**: SO, you're saying, you would be comfortable keeping the mid October date but perhaps pushing the testnet dates.

**Peter**: yes. If we want to really push Istanbul then I would say if we pick up late August or end of August beginning of September as the hardfork for the Istanbul to put on testnet Ropsten. Then depending on the EIPs, if they're implementable within 1-2 weeks,thats realistic. that we can release within 2 weeks and let everybody upgrades within 2 weeks. If we keep this timeline and I don't think we need to push the mainnet Istanbul further.

**Tim**: So, September 4th is basically the middle of the week of the first week of September. Would it make sense to agree to the date for Istanbul testnet then keep October 16th as Istanbul mainnet. I don't know what the next fork looks like but maybe keeping our  back pocket EIP around, potentially  having a January / February fork along with one later in 2020 where we accept new EIPs,  does that make sense ?

**Peter**: At this point I would say that we should either decide. I guess this crypto EIP is legitimately useful. So if ideally we want to get that in then option A is to do two hardforks.  One of them fast so to say and the other one soonish enough afterwards. If we go down that path then we should probably already now decide that you want to do second hardfork in January and we want that EIP in, so people can work already.
If we don't want to do two hardforks, then I would push the main Istanbul a bit so that there's a chance to get it into the original Istanbul. If this EIP is worthy it to be included then I would figure it out now how to include it?

**Danno**: So, there's a meta discussion I think, how we want to handle our network upgrade forks going forward? Do we want regular predictable Forks or do we want to have forks so we get what we think the demand is ? are we going to fix the date or are we going to fix the features.
The advantage of fixing the dates is that we can do the more regularly, we can do twice or may be 3 times a year but the downside we have to harsh when things get close to the end. And  things aren't ready, we have look and say,  "great idea you're going on the next train, you're not going on this train". That's kind of the moment of truth, which model do we want to adopt? Obviously I'm an advocate of the schedule next train approach, but there's no consensus around that to commit to it.

**Wei**: i wantt o propose an idea to actually submit EIP several weeks ago . The **2123**, which is basically **hardfork scheduling on signal based** version. I think in that case, we wouldn't need to have this discussion today. If we do similar harforks and implementing whatever feature is ready and then they deploy it to exchanges and miners. Then the hardfork can be automatically logged in whenever enough network have already upgraded their client version. It would be more convenient for developers.

**Danno**: They still have to come a consensus as to when the fire that contract. We need to have some governance who has the keys to update the numbers on that contract. 

**Tim**: Because there's clearly a lot of discussion to be have and that we had another call next week and that's a lot of people are not on this call. they might be worth punting the discussion around the schedule to the next call but perhaps just agreeing to move the testnet date  for Istanbul because no matter what, we will have to do that. So would anyone disagree with just moving the testnet date of Istanbul to September 4th  and then having your follow-up conversation around the hardfork schedule we want, past that?

**Peter**: If we just say that lets discuss it next week then we're going to be in the exact same position next week. In my opinion, the hardfork in the testnet in two weeeks is not going to happen, so we need to push that. What we could do is to say that, we will **fork Istanbul on Ropsten on 4th September**. For this fork we surely know that we have the list of EIPs which we should list now so that developers know that we want this in. Let's try to target that fork today already. So that client developers know what's happening and they can seriously consider including whole thing. After this we can also say that besides these five EIPs that are surely going in, heres 3 more that you should start working on seriously. and then next week  we can discuss where people are at?

**Danno**: I like it.

**Alex G**: Sounds good.

**Tim**: okay , just for clarity, hardforking the testnet on the 4th. What is the list of EIPs we want as a  must have and what are the other ones that we want this seriously start working on them.

**James**: I think we should have the list be finalized  on the next call so that gives us an opportunity for people who aren't on this call to have there input. 

**Danno**: I thibk we should get a preliminary list down. 

**James**: We have a preliminary list already, I don't want to say this is it without havng at least a little bit of time for we've changed just how are we going to do things and give someone that was un-anticipated.

**Peter**: We do have a list of 5 EIPs that seems we're surely accept and they were two or more EIPs that would be really awesome to have. but they either might require some extra input auditor or they might require some extra work with enough time. I think we should have this list unless somebody starts yelling really loud, that's what we're going to go with.

**Tim**: So looking the PR you put up James and my notes from this call that just happened right now, what seems to be the list of stuff that's going in and that's been accepted is 
* 1108
* 1702 
* 2024 
* 2028 and then
* 1344 was added on this call.
 And then on this what seem to be tentatively accepted , start working on them and we'll figure out if we can put them in seem to be 
* 2200 
* 1962 
* 1057 (ProgPOW) 

**Peter**: Could we have a written list?

**Tim**: There is going to be notes.

**James**:  We can update the forklist the 1679 and to have a list of the 'Yeses' and 'tentative Yeses' can be this more list of , once we want both needed for their work.

**Tim**: Exactly, just to wrap this up, aside from putting 2200 1962 and 1057 is there anything else we want on this list ?

**Danno**: I think we should move 1702 account versioning into the next fork maybe because I think we come to a consensus nothing in this list requires it.

**Wei**: I mean at this point, it's not require at the mainnet, but I still want to propose, we include it in the testing as early as possible date, may be the  1st Istanbul fork because at this moment, we have 3 client draft implementation. It doesn't affect mainnet but I think this is a really good thing to have if we include it in the Istanbul testing. 

**Alexey**: We could actually do something like preemptive refactoring instead so that  in  the future if you need to do this EIP, it will be super simple. Because a lot of complexities is now actually in the refactor.

**Wei**: yeah but if you do the refactoring then why not this? it's the same thing.

**Danno**: But we don't have any EIPs targeting version 1 and not version 0 is the big issue right now.

**Wei**: Say if we implement the account versioning, it doesn't really affect the mainnet because they don't have version one and version 0 is backwards compatible.

**Peter**: I guess that's the reason why I am reluctant to go this path because we've this EIP that we figure out that we needed, in the end it turn out we don't need; I am questioning the viability of it. SO, why do we need at all in the future?

**Wei**: I am pushing it for review because I like to see some more comments and reviews. I really hope that we have a stable foundation. The current description of EIP is like bare minimum you need to implement account versioning. I really think, if we have this we have a really stable foundation about why we need a conversation in. We can have this foundation so that other EIPs can build things easily on top of that.

**Danno**: Unless there's reference test against it, testing some form of it, I don't know if I'll be able to validate our refactoring to know all the various clients are compatible.

**wei**: I think, we are working some reference tests at this moment. I just hope all the clients take a look and do some review and include it in Istanbul testing.

**Danno**: Can we table this and finish this discussion online during the next call about where 1702 lands?

**Wei**: Yeah.

**Tim**: Just because we only have 5 minutes left on this call, is there anything that's missing from this list we have of what we would like client implementers  to prioritize for the testnet upgrade?

**Casey**: okay where's the, they want to increase the cost of s load? I forget the number.

**Tim**: It's 2200. Its tentative and not fully accepted yet because..

**Alexey**: That's not 2200..

**Alex**: 1884, the one I asked to discuss.

**Tim**: For that one we got in the schedule discussion instead, do we want to discuss it now?

**Danno**: Technically it's just price changes. the technical issues I don't think of the big ones. Oh there is a new opcode self-balancing. It suddenly became more technical.

**Wei**: I would be in the call for the net gas metering discussion. But if apply 1884 after net gas metering, then we can disregard 1238 and 706. Are we doing the light weight, we need 2200.
**Tim**: Just to be mindful of time,  let's just part the discussion until after 1884.  so do we want to include 1884 in either the tentative list of either side ?

**Alexey**: I don't think we ever got to discuss it, to be honest. I would say yes, but we never really got to that far.

**Danno**: Maybe we have that be the first item on next call.

**Peter**: I guess this is Martin's PR and he's not here. I can't say just a couple words, just food for thought for  next week.
The idea that Martin dis a lot of benchmarks on essentially was measuring how much time individual opcodes take? and the Geth implementation compared to their price and then he picked out  a few opcodes,  compared to the other ones are really cheap gas wise. But they computationally more than the others. And then he does try to balance it out so that one gas approximately can require the same computing resources. Whether that's substraction or that data retrieval. This is essentially trivial EIP, so unless there is something somebody has a reason not to do it,  I think we could do this. But I agree, lets postpone discussing or accepting  it marking in here, next week. But the EIP itself is  probably 5 lines codes.

**Wei**: No, I think it has selfbalance of code, so that's a new opcode. 

**Tim**: Let's add that as the first agenda item for next call and have people review at in the meantime because we have a final minutes. Does anyone have anything, they wanted to bring up that they feel hasn't been addressed, it can be resolved quickly?

**Alex**: Can you state the the final list of accepted and then the finalists of tentatively accepted?

**Peter**: Please also state the title of the EIPs because the numbers don't mean.

**Tim**: Got it. For the **testnet hardfork on September 4th** the list of **accepted EIPs** are 
* 1108 (Reprice alt_bn128 - 1108)
* 2024 (Blake2b - 2024) / 152 
* 2028 (CallData Gas Reduction - 2028)
* 1344 (Chain ID Opcode - 1344)
* 1702 (Account Versioning - 1702) is contentious. We're not sure where that's fit. Currently it's accepted but might move to the other side or might get dropped. SO we still have that conversation.
 
 
On the **tentatively accepted side**, the EIPs are 
* 2200 (1283 + 1706) around the s store which got the one that got pulled out of Constantinople 
* 1962 (Generic ECC Precompile - 1829 / 1962) 
* 1057 (ProgPOW)
* 1884 (Trie Dependant Repricing - 1884)

1702 (Account Versioning - 1702), we are not sure where that ends.

**Alex**: I have two comments probably agendas for the next call for this list.
The first one is for **Blake2**.  Probably two weeks ago **there was an issue raised** by one of the people close to Blake2, I believe, with zcash. That hasn't been addressed yet. So I'm not sure if Blake 2 is going to be finalized with the time frames. Probably just a good topic to discuss next call. And the other question I have is regarding to 1962. **1962** states that it depends on the gas cost reductions precompiles because some of the ability reasoning is that some of the operations are  so cheap that the call cast itself woul dbe bigger than the cost of the operation and  it would be a big drawback and then the question is, is it still requirements and if it is then what happens if none of the reduction pre-compile call reduction EIPs are accepted?

**Alex G**: It's not a requirement because it's mostly like for the greatest benefits comes from the heavy operations like bearings. It makes sense to do it in many case regardless of what the othe EIPs are. 

**Alex**: Could you update the 1962 to make this clear because currently it states that it requires to reduction.

**James**: Just a note for the community, this is the last week for any EIP to get on either one of those lists on the accepted or the tentatively accepted.

**Tim**: We're a bit over but is there anything else anyone wants to bring up urgently and I think one important thing also  that a lot of people have mentioned we want to discuss it still have never got into his just like conformance testing and initiatives around the testnet and stuff like that. So it might be worth having that discussion on the next call.

**Casey**: Sorry will you clarify if this week or next week is the last opportunity to get on the tentative accepted list?

**James**: Next Friday next 

**Casey**: Even if they don't make it into in October, it would be good to target them for January. It wasn't clear if the target for January would only come from the tentatively accepted list or a broader list.

**Peter**: If we want to go down the path of doing the double fork I mean splitting some EIPs because we want them in but they are too heavy and need a bit more work. Then  I would say that, for that second fork, whatever is not on this list, won't make it for that. Because otherwise we end up in the same situation from where we have all this tiny stuff that we discussed.

**Tim**: So if anything that's already been proposed for Istanbul that has not been accepted or tentatively accepted yet, next Friday is the last deadline to potentially be included. but we're not looking at the brand new EIPs. 

A note about next Friday's call it'll be 10 p.m. UTC 

**Alex**: We said that we tentatively accepted 1962 that states that supersedes 1829 which is also proposed and has maybe a smaller feature-set. Can we just agree that 1829 is rejected because we set the 1962 which is the super set is tentatively accepted? 

**Tim**: does anybody disagree?

**Danno**: If we need that formal stuff, sure all the lists I have seen always confind 1962 and 1829 considering to be one thing. To formally say **1829 is out of the fork** , I think it's fine. 

**Tim**: Okay well thank you everyone will see y'all next Friday

**Peter**: Thank you very much and then client developer start coding everything.

**Tim**: Yes, basically :)



# 3. Conformance Testing
# 4. [Testnet Upgrade Block Number](https://eth.wiki/en/roadmap/istanbul)
# 5. Review previous decisions made and action items
* [Call 64](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2064.md#new-actions)
* [Call 65](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2064.md#new-actions)
# 6. Next Network Upgrade
# 7. [Working Group Updates](https://en.ethereum.wiki/eth1)
# 8. Testing Updates
# 9. Client Updates (only if they are posted in the comments below)
a) Geth
b) Parity Ethereum
c) Aleth/eth
d) Trinity/PyEVM
e) EthereumJS
f) EthereumJ/Harmony
g) Pantheon
h) Turbo Geth
i) Nimbus
j) web3j
k) Mana/Exthereum
l) Mantis
m) Nethermind
# 10. EWASM & Research Updates (only if they are posted in the comments below)
	
	
# Date for Next Meeting: 
August 02, 2019 at 6:00 UTC. 
	
	
# Attendees

* Alex Beregszaszi
* Alex Guchowski
* Alexey Akhunov
* Brent Allsop
* Bryant Eisenbach
* Casey Detrio
* Danno Ferrin
* Daniel Ellison
* Dimitry Khoklov
* Guillaume
* James H.
* Lane Rettig
* Louis Guthmann
* Paweł Bylica
* Peter Szilagyi 
* Pooja Ranjan
* Tim Beiko
* Trenton Van Epps
* Wei Tang
	
	
## Links shared in the call 
	
* https://github.com/ethereum/pm/issues/113
* https://github.com/ethereum/EIPs/pull/2214/files
* https://github.com/ethereum/EIPs/pull/2200
* https://gitter.im/ethereum/AllCoreDevs?at=5d31988ae2d1aa6688d09f39
* https://github.com/alex-forshtat-tbk/EIPs/issues/1#issuecomment-508693797
* https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1706.md
* https://medium.com/least-authority/https-medium-com-least-authority-kicking-off-our-review-of-progpow-be1368ae9a50
* https://github.com/ethereum/pm/issues/113#issuecomment-515403686
* https://github.com/ethereum/EIPs/pull/2123
