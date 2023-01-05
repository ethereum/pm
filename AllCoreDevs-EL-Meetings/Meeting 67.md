# Ethereum Core Devs Meeting 67 Notes
### Meeting Date/Time: Friday 2 August 2019 at 6:00 UTC
### Meeting Duration: 1hr 30mins
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/116)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=fJd_xYnYrUU)
### Moderator: Tim Beiko
### Notes: Pooja Ranjan
	
----
	
# Summary
	
### DECISIONS MADE
	
**DECISION 67.1** : EIP 663 , EIP 1380, EIP 1985, EIP 2045 and EIP 2046 are tentatively accepted and will require benchmarks.

**DECISION 67.2** : EIP 1352 and EIP 1803 out of Istanbul due to lack of championing.

**DECISION 67.3** :  All the gas cost EIPs are moving into tentatively accepted, still would require a lot benchmarking to be considered on a hardfork.

**DECISION 67.4** : EIP 1559 stays withdrawn.

**DECISION 67.5** :  Using ReTestEth to generate reference tests for all the tentatively accepted and accepted EIPs.

**DECISION 67.6** : The next all core dev call be the last call for something to go from the tentatively accepted to accepted list to be included in the October fork.






### ACTION ITEM

**ACTION 67.1** : Get a status update from  both Geth and Parity before next call.
	
-----

**Tim**: Welcome Everyone !

# 1. Istanbul EIPs

## Client implementation updates for Accepted and Tentatively Accepted

**Tim**: Last time we had a decision to have  both tentatively accepted each and properly accepted EIPs and try to get client implementation for all of them. Then depending on how far along we would get with those to potentially split into two upgrades. The one that would be scheduled this fall and the other one early next year. So, I guess we could start with any clients around just how they are doing w.r.t implementation.

### Pantheon

**Danno**: I will speak for  Pantheon what we have implemented. We don't have ProgPOW, we don't have EC Curve implemented. But we have as well as spec EIPs out there in our current development branch.

### Nethermind

**Tomasz**: We passed the EIP 1344 , EIP 2028 and the remaining two we are starting soon. We don't have progPOW,  it's about the binding sort of library.  We are waiting here for some decisions on EC arithmetic,later this will be coming in. Everything else seems to be rather small.


### Geth & Parity

**Tim**: Do we have any other client teams on the call doesn't look like we have anyone from Geth or Parity, right?

**Alex V**: I can partially help with those. There will be two reference PR for implementations for Geth and Parity. Parity us ing Rust implementation. Geth is using binary  library. If someone else wants to use the library, it's also an option. This is for EC pre-compile.

 **Tim**: Got it, thanks for the update.
Obviously, it would be great to have the status update from Geth and Parity, so take that as action item before the next call to get a status update from  both of them. Does anyone have anything else to add on this?


## Last call for "Tentatively Accepted" EIPs

**Tim**: Okay until the second the second part of this agenda item was the last call for any EIPs that want to be considered for tentatively accepted section. So in practice this means it's very unlikely for the October fork but possibly for the January part. Anything that has been proposed for Istanbulbut  that hasn't been accepted yet. Does anyone has opinion or suggestions here?


**Casey**: Yeah, a few of them in there that I'm interested in, we're interested  Ewasm team. Unfortunately neither Pawel nor Alex could make the call but we'd like to see partical gas cost 2045. We've been to the tentatively accepted category.  I can elaborate on why, in some ways  it carries the torch for 615. There's a call a few months ago and during the 615 discussion people asks for benchmark to show what kind of speed improvement could  be expected and so it turns out two speed improvements are possible even without introducing subroutines and changing how jumps work. And we've always benchmarks showing speed ups that are on the table. So from Ewasm team's perspective also this particle  gas cost, I would argue, it's alternative to introducing Ewasm. One of the big potential benefits of Ewasm is to speed up. Well, it turns out that , if you just optimize EVM and  the client and which will be a lot easier and having much sooner than integrating Ewasm. So,  I think it's fair to say that reduce in gas costs was the main part of the Ewasm chain. So we're definitely interested in that one.

**Danny**: So one of the things I would like to see what that is a possible schedule . We have particle gas cost, what would be the proposed gas cost for all for the operations? I think that would give us a better scope for how impactful it would be. 

**Casey**: Yep that's a good point and that's something we want to work on. So obviously that a new gas schedule , we're not going to have enough time to propose that by Istanbul - I.  But for the the follow-up, I think there is plenty of time to propose that. Once you have the the new gas cost table, then the implementation  is fairly trivial with the exception of versioning.  If it's going to be version then obviously that adds to the complexity but that's a different discussion.

**James**: Before we dive into this more can we get a list of what are the ones that are trying to get in and I can start from that.

**Leonardo**: This is Leo from Solidity. I think Pawel wanted to discuss,  I mean he's not going to be here but he wanted to start discussion on 663. Regarding some comments about a multi by opcodes and backwards compatibility.

**Tim**: yeah there was that comment and Alex that put  the first comment around having themeatic hardforks if you want. And in the second, it was about Istanbul saying you might be nice to focus on gas repricing because we alread have 1108, 1884  and  2028 as tentatively accepted . It might make sense to also consider 2045, I believe the one just discussed, 2046 and 2200 as of to just have this focus around around gas cost changes. So there's those, there's 663 which was just mentioned,  does anyone on the call have other ones they'd like to discuss?

**James**: I would like to add 1559 to that.

 **Alex V**: I'm interested in what's with 1109 or similar EIPs which are about reduced cost to pre-complies. I mean for a static call to precompile. 
 
**Danno**: So 1109 is on list rejected / withdrawn. And this is because they didn't have a reference implementation 2 weeks ago. So they were declared out of scope for Istanbul. The same with the one about the few market change because there is no prototype although still design is going on with this. It doesn't mean it is dead in general. Work should progress, it could make the next train but I think we made the decision then that if you didn't have a reference, then it is not ready for the October hardfork.  

**James**: Yes, and that fits with the October hardfork. There is a conversation I think that's worth having thinking about a January or February hardfork. Specifically if we're talking about balancing and repricing really coming together with these two forks.  We just released today,  a full implementation - implementation study of what it would take you to 1559 and I can go into that one then it's time to talk about that right. That is something that I would like to address on this call. 



**Casey**: Back to the question about reducing gas cost to precompile. There is EIP 2046 in the proposed section. That looks like an option it should be moved up to tentatively accepted.

**Danno**: 2046. It look simple. The question is the benchmark support. So for January it should be easy if we can get me on someone run benchmarks on it.

**Tim**: Do we want to agree to move 2046 to tentatively accepted, does anyone disagree with that? 

**Tomasz**: I just like to ask, if we measured how would the combined results of the  implementation and the reduce static call affect the performance of the EVM, the precompiles? Because we'll be going down from 1200 to something like 190.


**Danno**: Good point, that needs follow up. Technically, it's simple EIP. 

**Rick**: Do we have some sort of analysis or simulator that can  show us what these gas changes would do to existing contracts?

**James**: No. And for me that for those kind of gas cost or one's talking about the gas cost, that should be the barrier for them to be moved from tentatively accepted to actually getting it. The changes are small but instead of having a lot of work around implementation and testing, there should be a lot of work about investigating the effects of the gas changes.

**Rick**: We all know , this gas bucketing thing is a knapsack problem. I mean, the way the gas model works, naturally a lot of work that has to be done to assert that these gas changes are safe that's just the nature of gas , well Ethereum gas at least. I'm very aggressively in favor of changing gas pricing to make it better and I actually understand that it'll be a continuous effort . But because, it'll be a continuous effort, I feel like we should have a more formal approach to making changes.

**Casey**: I mean , there's a pretty good benchmark system, a couple of them actually. The one for pricing precompile. And both were done by Martin Swende where it gets complicated with this 2046. The Benchmark scripts benchmarks the precompiles themselves but not really considering calling them from other contracts. The EIP explains that it's just reducing the cost back from when it was raised, when the cost of call was raised. The cost of call was raised because when you call another contract, there's just latency. When you call the precompile,  there is no disk latency so it doesn't make sencse to charge the same for precompile as it charge to call a contract. But benchmarks of calling contract for calling precompiles, I don't think that's been done yet.

**Tomasz**: Rick I generally thing that's just analyzing the existing contract when I'm bringing gas down maybe it's not the most important thing. We could explore any security issues, but performance wise, I think we should be much worried bringing the gas much down. And someone posting the contract with the EVM, the same thing and if it's under priced, it caused the trouble us in the past.

**Rick**: yeah, I'm just security focused, generally speaking. So I completely agree with what you're saying in terms of what the engineering exercise should be but the approval process should include. We should be able to literally analyze all the existing contracts on chain and say that this isn't going to cause any of them to become a DOS factor. I am not trying to make extra work for people it just seems like we've already run into this problem once and it's in something that's like very well understood to be a hard thing to take into it. Since,  we spend so much time , I think its important to improve gas, so why not just run some tests to make that process formalize, to make that process better. yeah I agree with the engineering effort.


**Tomsaz**: I think we have amazing work from Martin Swende on particular opcodes on the pricing, current pricing and the relations to the actual call. But we don't have the same tuning for finalizing contract at least not posted as a researcher report showing the results. The other thing is I wonder if the precompiles were always analyzed  with the cost of all something that I assumed or the precompiles were analyzed as the independent thing. That's why I was asking about the EIP 1108 in combination with 2046 if it's still safe?

**Alex V**: As far as I know at least the existing  1108 was benchmarked only one based on codes without anything touching on the EVM. 

**Tim**: So based on this discussion do we want to move any of the gas cost EIPs into tentatively accepted, kind of dependent on those types of benchmarks? Unfortunately Martin's not on the call and it doesn't seem like they are the champions for both of the EIPs  are either. Or do we want to go over to specific EIPs and discuss those on a case-by-case basis, perhaps move them in or out?

**Danno**: I'm kind of thinking we should leave them proposed unless we're certainly want to do and we're just waiting. We're getting quite late to be moving the chairs around before we ships on a hard fork if we're going to do it. So we should probably go over them but I am a little skeptical.

**Casey**: Was there an expectation that today, that this meeting was the last one to move on to tentatively accepted, is that no longer the case and it will be an option on later calls?

**Tim**:  Yes, this is the last week to move to tentatively accepted and that too the second part of Istanbul if it's broken down. I was asking because if we'd like to have in probably should discuss them today and try to get the consensus on them rather than waiting a few more weeks to do that.

**James**: I would support them getting in with the with the conditions that you said. Most of the tentatively accepted one have some implementation and gas ones have their own specific one too then I feel that is totally fair to put them in that category.

**Tomsaz**: I would suggest going over them one by one so we clearly states that they're going to tentatively accepted. But, I generally think that we are all right to move them to tentatively accepted.

**Danno**: Okay let's go through the list.

**Tim**: Yeah and then I guess just to clarify the list, the ones that were proposed are 663, 2025, 2046, 2200 and 1559. Does anyone has anything else to propose?

**Tomasz**: It's a different list as I see 1559 is rejected and 7 in proposed.

**Tim**: Okay, yes so you're working from The Meta EIP. I was just looking at the agenda. We can go through the list of proposed because it's pretty small and  one that's not in that it was rejected such as the 1559 that James suggested he would still like to discuss given their report from today . Let's **go through the proposed list** and just include  1559 as well. 

Just in order **663** ?

**Tomasz**: I am okay to move it to tentatively accepted.

**Danno**: What about the concerns, does anyone want to speak about that?

**Leonardo**: Yes we were talking about that yesterday. I don't know how you guys feel about accepting it or like doing it without the account versioning. Because , as Andrea posted,  he writes test that would be broken with the multibyte opcode. Pawel  suggested to scan the current code contract to see if this would affect any, but still even if you don't affect any at the moment or if you can get like a confirmation that most contracts wouldn't be affected. How do you feel about this being a general conceptual problem? 

**Danno**: So where's that test to be broken with? 

**Leonardo**: The Ethereum magicians thread.

**Danno**: Is that also broken for push 1 through push 20 ? Are  those safe from that as well?

**Leonardo**: I think those are safe.

**Danno**: I'll discuss this on the thread. 

**Leonardo**: Okay, I just wanted to bring that to your attention.

**Casey**: Just to add to this versioning  issue. Versioning might also be  a good combination with 2045 and it is obviously much longer discussion then we can have in and want to call. The only way to continue the discussion and leave them as options for Istanbul part 2 is by moving them to tentatively accepted. So I'm in favor of moving these to tentatively acceptance so that we can continue the discussion.

**Tim**: Great, does anyone opposed moving it to tentatively accepted? Okay so **let's do that**.


**Tim**: Next one on the list was **1350** to specify the address range for precompile / system contract.

**Danno**: This is when we're not sure if there's any evm impact on it?Hasn't been much discussion on the EthMagician thread about it.

**Tim**: I don't recall much discussion on the core dev call about it either. At the very least kind of in the handful of calls. Does anyone feel strongly that this should be in for Istanbul and if not should we just reject it from Istanbul and leave it as a consideration for another upgrade , if anyone comes on a future call and advocates for it?

**Danno**: I think we can get the value out of this without having to put it as part of a hard Fork just get a practice that certain ranges are reserved. I think this isn't out of hard Fork EIP. Lets move it out unless we have an objection. 

**Casey**: The same for 1803 as well.

**Danno**: Second it.

**Tim**: Okay, does anyone disagree with **moving 1352 and  1803 out of Istanbul**?

**Tomsaz**: It's fine.

**Tim**: Great.
So that leaves **EIP 1380** .

**Danno**: I think that falls in the same category that Rick has  mentioned about needing to have some more analysis on gas impact. That could go on the condition of good analysis.

**Tomasz**: Yeah I would agree let's **move it to tentatively** but let's have the results of benchmarks for all the EIPs that are affecting gas cost.

**Tim**: Sounds good, anyone disagree?
Okay and then just to be numerically consistent, the next one would be EIP 1559 although it's not exactly in the list and James, you wanted to give an update on that. 

**James**: Yeah it's okay to do that, that one last.

**Tim**: Sure, so then the next one would be **EIP 1985** State limits for certain EVM parameters.

Does anyone feel it should be pushed in otherwise default is dropped from Istanbul?

**Tomsaz**: I woudl like to see some more work on it because it's long outstanding. I would like to see it in tentatively accepted but I am not strongly favoring it. 

**Danno**: So, that's about to not kill it.

**Tomasz**: But a week vowed not to kill it.

**Casey**: I know Alex cares about this one so I voiced his support and his absence.

**Tomsaz**: Let's move it to tentatively accepted then?

**Tim**: Yeah. Just for the record what we would like to see to take it from tentative to fully accepted?

**Danno** Reference tests with extreme numbers that shows breakage is probably I would want to see how the clients acts when presented with the valuse outside the ranges.

**Tomasz**: Yes, this will be important and also what Martin mentioned is the question of whether we look at it only from the EVM perspective or also from outside of the EVM perspective. Because it affects how we define what the transaction is constructed or not in the same for probably a few other items within the domain. Like probably non block headers, but this is the idea , right? So, do we only change the way we look at gas in EVM inside or when we deserialize and accept RLP or not?

**Danno**: I think the reference test can handle will it accept RLP of block headers and transactions. So, I think that's really what we need is unit tests, this is reference tests, what we need out of it.

**Tim**: Great, anything else on 1985?

**Tim**: Next one on the list is 2045 - particle gas cost. 

**Danno**: This one we need the table of proposed and the same gas analysis we're asking for all the gas was. Although, it might be hard without an oimplementation.

**Casey**: Absolutely, we do have an implementation for this.

**Tim**: Do we want to move it to tentatively accepted, does any one disagree?

**Tomasz**: Just didn't see much discussion because, I believe it was added quite later.

**Danno**: It was proposed at the deadline and there was a lot of stuff that got discussed before and it didn't get near it. Because there wasn't room to discuss. I'd say lets not kill it yet.

**Tomasz**: I am not opposing it. I think it's an interesting change, just would like to see more discussion in it and some benchmark as for the others. 

**Tim**: That make sense. So, **EIP 2045 as tentatively accepted **as well.

Final one on the list is **EIP 2046**.

**Danno**: And there is gas cost, don't kill it yet. 

**Tim**: Does anyone disagree moving it to tentatively accepted?

Okay! Just for the record, **all the gas cost ones are moving into tentatively accepted still would require a lot benchmarking done to be considered on a hardfork**. But hopefully having the final list helps us focus the discussion and gives the team championing the signal that they need to work on those benchmarks.

Now that we're over with this list, James  do you want to talk about 1559?

**James**: We had Matt S. do an **implementation study of 1559** and further go into. Specifically, we're in the Geth code, what changes we need to make in order to implement it. He recomended a 2 fork process as one of the updates. 
First introducing the transaction fee change and both transaction types exist at the same time then a transition function that will make it over a period of time.

The gas to the 1559 will be given more allocation and the and the original transaction type will get less allocation. And then after that they'll be a second Fork which will clean up the old transaction type and then we'll unlock any that's left of the 60 million gas limit  that hasn't been reached with that function. The reason why it's important to talk about what this conversation is, in the process of going through 1559, we realized that taking away gas is easy to do but the more difficult part is going to be incentivizing wallets and users to use the new transaction type during the time when there's this transition of them both existing. And the simplest solution to solve that is to provide an incentive to move to the second transaction type. And specifically gas cost is that is easiest way to do that so with the reduction of gas cost or any changes to gas cost being tied to be using the new transaction type means that's where we get our incentivize leverage from . So if we go through a fork that does a very heavy on optimizing gas price and gas cost and we don't have this fee change implemented at the same time we lose that incentive mechanism for transition.


 
**Danno**: So, 1702 is clearly defined, would have rules apply to the current contract address members of the contract? 

**James**: This would propose a different scheme where any gas prices would not be tied to the contract version of the executing code but to the transaction originating to call no matter how far down the stack.

**Rick**: Can you repeat that question I'm not sure I entirely understood it?

**Danno**: 1702, the versions applied  to the current contract message frame, whatever contract message frame were in. So when I was implementing it in Pantheon, the gas price changes with only affect. If we were to make the gas price changes, it  would only affect the contract version. But I want to make sure that this would propose not that strategy but a different startegy which is the gas cost changes don't matter about what current contract we're in. It's about the transaction that initiated all the calls. So, if the transaction came in with the new format all of the contracts would get the reduced fee they recall  no matter when they were deployed;  whereas if you call the old format they would all have the old version it wouldn't matter when these contracts were deployed. 

**Rick**: Yeah, my previous comment anticipated these discussions. W  hen we're having all these things that are messing around with the gas cost, it's not clear what the interference is going to be, right? So for I wasn't aware of 1702, what I proposed this sort changes. I think it's just a matter of when 1702 gets in. If 1702 gets in before 1559 then it would apply to the old transaction types and the new transaction type. If it's withheld to be applied with 1559 then it would only apply to the new transaction type. So there's to be a big branch in the code that says it's a new transaction or an old transaction. 

**James**: There are specification for how to do this process in the implementation study as well.

**Rick**: Did that answer the question because I'm not entirely sure. 

**Danno**: I think it did. Because we haven't decided what's going to be assigned to any versions. 1702 is kind of on the bubble because versions are falling out of favor since 615 has been withdrawn by the authors. We could just let this win and have something  to figure it out when it's ready to come back in the scene.

**Rick**: Yeah. I think in terms of timing, part of the reason we took our time and got this proposal written and have been talking to simulations. I've continuing to talk to teams that do simulations it's because having two transaction Types on the network at the same time as pretty intense. To me, it's just the parsimonious way of allowing. We're changing how transactions work so every piece of software that interacts with the system is either reading or writing transaction. So we can't just get rid of them. So the reason we are taking our time is to make sure that we actually have sufficient testing in place and obviously that testing those testing frameworks those harnesses what you have you could be reused. In these cases where we have potentially interfering the EIPs that we want to test them all together. We're going to have to be taking forks of Geth and then running in the simulation. So I think that just be a part of the process. Once we've done that obviously moving forward all EIPs could use that process.

**Tomasz**: I've mixed feelings here so there are few things first of all the specification doesn't define clearly of the splits into two stages. And the second thing is, it was already rejected so I'm on a unwilling to have some some kind of situation when we reject something and read the rights and it opens the door for others.

**Rick**: How would it get into Istanbul-II? This is what we're doing moving forward having a part 1 part 2. If you get rejected from part 1 you're rejected from part 2?

**Danno**: I think that was when we proposed part 2, that was. the idea.  That would still be going on whether it's in April or July and things that are rejected are still eligible for that.  I think the original idea for the two part was just to have the biggest ones and not have it collect everything which would have been the EC generic contracts and  ProgPOW coming in January. Because, those require a bit more client implementation time testing after the smaller ones were consisting mostly of gas cost changes. We could get reference tests together much easier for proposed hardfork of the testnet beginning in September. So I think that's what was the original idea of it and I do sympathize on if we're going to keep the trains running on time, we need to set deadlines. When the cabin door closes the planes on its way. If you're not in,  you now talk to your travel agent and get a new ticket.

**James**: I respected that was in the context of the October fork. It's a lot different now that we're talking about using all of the gas cost changes at the same time which that is an important part of getting the adoption , having the incentive mechanism work for 1559. 

**Danno**: What If instead of applying to different gas schedule on each version of the transactions, what if there was a multiplier that the old ones cost 1.1 as much and they cost 1.2 as much up until  it costs 2 or 5 times as much from the gas to get away multiplier. Because  was that approach considered or was the schedule approach found spare to that for something?

**Rick**: We didn't really think about adding  an artificial multiplier to make gas more expensive. Again it seems to me to be less parsimonious. Here is how I'm looking at the conversation right now and apologies because I bet  I'm not participating all the time. But if collectively we agree that 1559 is important which I don't know how people feel about that then and we agree that we need to have an incentivization  mechanism to have people move to 1559, which I think is something that we should all be able to reach to or disagree very quickly. I am not opposed to the policy at all of saying something is postponed or what-have-you but if all of the gas fee changes are used the we have to come up with this other method that is probably going to be more complicated. So by partitioning the changes that seems to me to be the most parsimonious solution. I am totally open to doing other things that add to me more complexity and I'm open to suggestions. I'm fine if EIP wasn't ready, it wasn't ready; I'm not upset about that either. But I'm not in any particular rush frankly but I am concerned about how we're going to incentivize people to transition to the new transaction? That's my concern.

**Danno**: I think plug-in to different schedules based on how the transactions put in the system I think is is more difficult then after the transactions executed I'm looking up on a table and a plan of multiplier to the gas cost. I think that one is much less of an impact on the code when using multiple schedules and using multiple schedules needed complexity. I mean it is one way to incentivize it but I think the cost is higher than we expect.

**Tomasz**: I think we should make a strong statement that we generally would like to see 1559  as a moving forward for the entire network and I would like to keep discussing in separation from other EIP and say it should have its own way of incentivization and not be delivered by under gas cost changes. I remember, in April it was suggested to like split the the block gas limit and 1/2 and one 1/2 would be reserved just for 1559 style transactions, is that still the case?

**Rick**: That still the case. Then if the  old fee market and block gas and if that's filled up, there's a natural incentive for people to go to like the express lane that's with it's more open and deeper.

**Rick**: Yeah but that incentive is at the user level not at the developer level. Someone has to actually write patches to the changes and they're not incentivized to do that if their transactions get through if they don't push a patch. And their transactions just work then they're going to wait till the last minute. You might as well just do a hard switch.

**James**: And that includes  UI/UX changes for wallets as well. So, that it's not  like a wallet can say hey just use new transaction, it'll be pretty significant.

**Tomasz**: : Yeah for that reason, the sooner we say that we seriously consider that change to  be introduced, the better for the wallet creators to adjust. At the same time the amount of discussion that we having the round it's now, would say maybe it's too early to say for be in the Istanbul.

**Rick**: Fine with me. I wanted there to be a discussion around the document. That's what I said in Eth Magician. I am  happy to have a discussion regarding this document and maybe additional documents. But I don't know if that'll be necessary or not. At a minimum, I'm happy to have a discussion about this one.

**James**: I would do that with my proposal to talk about it is also at the same spirit. 

**Danno**: So considering how fresh the document is and how much coping questions there are; I do think there's too much uncertainty to get any January Fork.

**Rick**: Okay, thats fine with me.

**Danno**: I think it's a good idea and we should continue with that. 

**Tim**: So we're going to have open it tentatively accepted section for the next hard fork ..... just kidding
Just for clarity, do we want to say **1559 stays withdrawn** or rejected from Istanbul but  we obviously want to see this change and just point people towards the document.

**Danno**: Yeah maybe we should change rejected withdrawn to say 'missed the boat' or something little softer. 

**Tim**: I think for now just lets not get into the EIP 1 discussions. Let's just say it's out of Istanbul.

**James**: And the * is when we're talking about gas changes,  we should also think about 1559 in context.


**Tim**: Great so I think we made it through the first agenda item. There  was a comment about 2200 in the GitHub agenda. If anyone could speak  about that but basically a proposal to flat-out reject 2200.  I'm not sure if anyone has strong opinions there if not it might make sense that to pause the discussion and tells someone who does is, is on the call. 

**Danno**: So looking at the [GitHub](https://github.com/ethereum/pm/issues/116#issuecomment-517370111 ), there's three arguments for that. It hasn't been submitted finally as a draft which can be fixed relatively easily. It's based on 1706 which is still a draft, it's actually replacing 1706. So really, 1706 be withdrawn but the most substansive argument is about two things relating to alternative fixes for 1283. My take on it is, so far down a process there's so many ways we could fix this, we got to pick one. And unless the one that 2200 proposes is objectively wrong, we're letting perfect be the enemy of the better. Maybe it is objectively wrong that's probably the discussion we need to have though.

**Tim**: Just because no one is jumping in for the counter arguement,  I think it might make sense to just not remove it from the tentatively accepted list and potentially have this conversation on the next call because the person who posted the comment can't make it and neither his wife who's been championing this EIP. 

**Danno**: Yeahs they would be the best one to defend it. Because he's got the most details on it. I seem to recall that the second argument about the one of the arguments about why don't we just give a bigger refund later withdrawn last week. one of these arguments before he has better memory about it. but  me personally, I'm not seeing anything that says that except proposes a solution is not objectively false. We're picking colors  but I shed at this point but if it's objectively wrong, we should fix it. So that's what we need to look for is those sorts of requests.

**Casey**: So would there still be a chance to move 2200 from tentatively accepted to accepted for Istanbul in October or on the testnet?

**Danno**: I thought it was accepted last week.

**Tim**: It's tentatively accepted. I feel like for what the consensus was for all of the tentatively accepted one was if we can get the implementation done soon enough that we can hard for it to testnet  that's still on September 4th. Then it makes sense to have that as the  part of the October hardfork and realistically I guess that means if clients have not implemented by the next call then it's probably not making it to October because the next call is mid-august then we'll have one that'll be late August which is like a week before the 4th. So I feel like next call is probably the one where if  the clients have not all implemented it and they're still implementation details fit to figure out; then it would get push back to January.  This is my opinion about this, i think everyone else  also thinks about this.

**Tomasz**: I would be in favor of changing this requirements from all clients are implementing it to just there are tests like tests available.  If there are tests and the clients follow-up. Geth and Parity will be important and if they are there and if we've tests, it's enough.

**Tim**: The reason I was focusing on client implementing because the call 2 weeks from now basically be 2.5 weeks before the testnet hardfork. From last call it seemed like the minimum time you would want between releasing your version and actually forking the network a new version and actually forking the network 

**Danno**: There is part 1 of Istanbul and part 2 of Istanbul in January in and Asiago is in April. 

**Tim**: So  there wasn't  final consensus on either of those. I think way last time had an objection with January say maybe February would be better. Say that part 2 would be sometime q1 and then there was a discussion about whether or not the next update should be in April or a bit farther so like around the July.

**Tomasz**: okay

**Danno**: We can look at it as maybe we're pulling Asiago up two months then pulling Brie up 3 months, the way we're going at it right now.

**James**: January-February then April-May for the next after Istanbul.

**Danno**: Probably July. February - July feels a bit better than doing two 3-month Forks. But maybe we'll be good at it by then, I don't know. I think it's too early to call Asiago. I think we need to see how Istanbul - I lands. 

**Casey**: Does that mean part 2 is the name is Asiago?

**James**: No part 2 is the thick fork.

# 2. Conformance Testing


**Tim**: Just in the interest of time, because we could spend a full hour figuring out the name. I know conformance testing was the second part of the agenda and it all the people wanted to discuss this any kind of ties it to what you were mentioning Tomasz.

**Tomasz**: My mention was more about we say that it's enough to have reference implementation why I wouldn't like to have situation we have one reference implementation and is considered to be enough for inclusion in the hardfork because the testing is much more important for other clients usually than just the reference implementation. Because testing has to be in the end based on a reference implementation. So it's a bit more of a strong requirement.



**Danno**: I don't see Dimitri  on the call to speak to this.  But one of the things that he's the writing is a tool called **ReTestEth** and what it does it take the reference test and instead of expecting a client to read the JSON,  expected client to expose on JSON RPC Port. So in theory you could stand up right now Aleth and geth will support it. You could write you a reference test against Aleth and Geth and have the fillers figure it out from there. Pantheon should be coming in about a week or two. So from that you can write your reference tests for whereever your reference implementation is. Hopefully it's going to show up on Parity shortly. That would be great if Trinity will be agreed at too. But this is a tool that  we don't have to be Aleth  hackers to figure out how to make the filler work. We can follow the instructions that Dimitri left online to write the reference test. So I think that is something that as developers and authors of these EIPs we should know for the next community hard fork,  I personally want to apply it on the hard rule and  not only do you need to have reference implementation, you need to have test cases. Ideally test cases in the form of reference tests. For the gas changes these are like the ideal tests because there are no easy things that say that the test is great in a reference method. SO, its something that we could throw against other clients to make sure that they have the same logic as they're writing it. We definitely should, I don't know who's up for it. Just right some of these reference tests for these changes that we think should be going in. If it's your EIP, you find the doc that Dimitry wrote and spit it up against the Geth or Aleth if that's for your reference implementation is.

**Tomasz**: What we see is that all the EIPs proposers are very happy to implement as much as they can. Very often they are stopped because they have to wait for some of the client developers to deliver the implementation for them. If we deliver a good set of tools and ReTestEth as something amazing something that we really need, there is a bigger chance, the EIP will be proposed in a more holistic way that will allow us to introduce something without really worrying whether it can be implemented or not. 

**Danno**: yeah because Dimitri earlier today on the Gitter said, so if an EIP is accepted, I see the proposal is in test sections. The questions how obligated to provide the test for the EIP. There will be many EIPs and only one testing team. Here is an example kind of test might be needed for the opcodes and you may link to something in the Aleth repo. So this is something that we can't just throw over the fence and hope the QA teams  handles. I think we need to pitch in and do these things at Levels.

**Casey**: The direct answer is there isn't anybody. I'm just being frank about it or not to mince words.

**Tim**: So given that Dimitri is not on the call.

**Dimitry**: I am here. oh I thought I am the wrong Dimitri, sorry.

**Danno**: Did I sell ReTestEth sufficiently for you.

**Dimitry**: Yes thanks very much. you described it very well. It actually supports geth right now and then the state test so you could run and you could generate the state test using the Geth  version. Aleth is not stable and the blockchain test generation is not supported yet. so I guess for blockchain test, I will have to I will have to use Aleth test. This is the one I used all the time and the state test could be generated.

**Danno**: Are the blockchain test generated straight from the state tests or does it need functioning inside of Aleth right now ? 

**Dimitry**: The difference between the group of tests that function test could  contain many blocks and many transactions and some malicious blocks and the state test is a basic form of test is one transaction. so it could  easily be converted into simple blockchain test with one block and One transaction. This test are run  by hive. So,  it's enough to create the simple one transaction test. These changes that include like your EIP couldn't include the change and you could test it with one transaction. It should be enough so majority of the test cases could be implemented by this one transaction change. It's not very critical that's function tests unless you're supported is going to be implemented soon. 

**Tim**: So are we **agreeing on using ReTestEth to generate the testing for all the tentatively accepted and accepted EIPs**?  And trying to get not only Dimitry to do that to try to involve as many people as possible in generating those tests?

**Alex G**: Sounds like a good idea. We are already doing this for EIP  1962.

**Rick**: Sounds like a good idea to me as well.

**Tim**: Great, let's just make sure to communicate that clearly that EIP Champions / teams should should be looking at ReTestEth and trying to generate the reference test for their EIPs.

Does anyone else have anything else about testing they want to discuss ? 

**Tomasz**: One thing is that even if we assume that's all the EIP Champions going to generate some tests, I would love to see some centralized  green light from the testing team. From Dimitri to say that the test coverage for a given EIPs is enough. Like they still some over seeing process and generally we should focus now in testing since we have the list of accepted tentatively and accepted EIPs.  The testing should be just our Focus now and we should clearly state okay we transition to testing stage now, the next requirements used to set of tests and this is the way we going to implement everything.

**Tim**: That seems pretty reasonable is there a way to ensure that there's not like a duplication of work so that EIP Champions don't do the same work in parallel?

**Dimitry**: I have some ideas if you analyze the byte code you could potentially detect the patterns which are repeated in already implemented  test and this is just an idea.

**Alex G**: Maybe it makes more sense that EIP champions are responsible to produce  test in order to duplicate the work.

**Casey**: One thing has been the first testing team has been working on for a while is generating code coverage reports. In particular Geth and Parity, so this would show the code coverage of both the state test and then there was testing Corpus and gaps are and so forth. So it would be nice if that can be published on a kind of dashboard. I assume another piority will be to get Hive tests up and running again. Because that seems to be in maintenance right now. I mean it's up but the tests clearly aren't working correctly on the hive dashboard.

**Tomasz**: I would love to hear Hive team on this call may be here in may be the next call. Because testing will be our focus now. So obviously Dimitry can give us some update now on what stage we are already. Dimitry, are you involved in Hive as well?

**Dimitry**: I'm involved in the part of providing the blockchain test status that we have. I am probably not working right now because there was some changes to the blockchain test organization. I split the folders from  you need to do some changes to the script of the  Hive. 

**Casey**: yeah sometimes the hive team has a hard time keeping up with Dimitry :)

**Tim**: Okay so I guess just to summarize this we're saying **EIP Champions should own generating the reference test for EIPs but we should also have the testing team kind as a central point, looking at everything and green lighting it and we should try to get the hive team on the next call to discuss this in more detail**, does that make sense?

**Tomasz**: Anything else on testing?


# 3. Testnet Upgrade & Istanbul Next Steps


**Tim**: Okay so the next agenda item was basically looking at the testnet upgrade and next steps for Istanbul. I feel we've kind of done this ad hoc across the the rest of the call, but does anyone have anything they want to add on this?
I think it might just be worth noting that it would be good on the next call to pick a block for the  testnet just because it'll be the second to last call before we actually want to Fork.


# 4. Review previous decisions made and action items

**Tim**: yeah and the next agenda item was reviewing the previous decisions and  action items from the last calls but I just wanted to leave the space if anyone has anything else they want to discuss?

* [Call 65](https://github.com/ethereum/pm/blob/master/AllCoreDevs-Meetings/Meeting%2064.md#new-actions)

**Tim**: Okay . So the previous call, basically we had a lot of both accepted and tentatively accepted I won't go over the entire list because we hashed it already. We didn't have any outstanding action items. 

* [Call 66](https://github.com/ethereum/pm/blob/463126de2b9289b54d3d042f3171a189f928eee4/AllCoreDevs-Meetings/Meeting%2066.md)

**Tim**: Then the call before that because we didn't get to reviewing stuff on the previous call.  we had a lot of EIPs accepted in terms of the decision so no need to go back over these. The actions required were reviewing 1283, 1706 this seems to be happening and we touched on the earlier around the 2200 discussion. Some notes were about the next core dev calls which were having a right now. 1344 which we've accepted and then continue discussing 1962, so we definetly done that. 



# 5. [Working Group Updates](https://en.ethereum.wiki/eth1)

The next step on the agenda is just updates form and working groups testing clients or research so if anyone has anything they want to share, please do.

**Rick**: Well we already covered it but just for completeness there's a document up at The EthMagician's with the proposal. That James already said that basically cover is how we would actually write the code . I have sort of a first pass analysis of the impact, how people feel about this proposal? We may do another a more in-depth economic impact as well for EIP 1559.

**Danno**: Was there an intended time frame between Phase 1 Phase 2 how long would be given ?

**Rick**: yeah  I don't feel comfortable unanimously making that decision. We just need to open it up for the community and have a conversation. I am open to just the next fork, whatever that plan is. I don't think we need to plan a fork just for that change. I think whatever forks go in, it would be good to just get into a Cadence and follow along.

**Danno**: So something on the order of 6 months?

**Rick**: Fine with me. Maybe 3 months instead of 6; but I'm really open to suggestions there.

**Tim**: Thanks for the update Rick. Anyone else have anything they want to share?

**Alex G**: I just wanted to clarify there was a question earlier in the call or somebody said that they didn't start working on some EIPs because were tentatively accepted and some decisions has to be made. To clarify, the tentatively accepted EIPs must be implemented they are going in either in October or in January, is that correct?

**Tim**: So my understanding is, especially with the ones we've added today is that the clients should begin the implementation  but some of them still have outstanding issues like that for the gas cost the benchmarks, for ProgPOW was the audit. So client should start on the instrumentation but I don't think we're ready to assume it'll get included in upgrade for sure if  the outstanding issues with these EIPs don't get resolved. Does that make sense ?

**Alex G**: Maybe we should call them somewhat differently. Because some of this EIPs are like we know that we need to get them and it's just the matter of getting the check  done. And some others are still maybe not decided completely. That doesn't make sense to differentiate within these two types. 

**Tomasz**: For tentatively EIPs we know exactly there are some actions required. For ProgPOW we need audit. For 1962, we are waiting for the review of a correctness. I've seen some discussions on all core devs. For some others, we wait only for benchmarks or gas repricing.

**Casey**: My understanding is that the ones that are currently in tentatively accepted would still need to move to accepted and that would start happening either after testnet activation or October mainnet fork. Then that's when the discussion begins to move EIPs from the tentatively accepted lists up to be accepted list. That's what how I would expect it to go.

**James**:  the big the big question there is if it's part of the October or the January one and then that will be kind of decided by those things. I think it's also important to say for people who are listening to this from the outside that saying that it's in now doesn't mean that there isn't going to be something that comes up through testing that we have to kick an EIP  out due to something we don't understand yet. So it isn't like  we're going to do everything where we are locked into all of these being in. **These are the yeses and everyone should move forward that these are the ones until we find out a reason for them, not to be**. 

**Tim**: I will plus one on that to James. One thing I'd maybe like **to propose is having the next call so the mid-august one be the last call for something to go from the tentatively accepted to accepted list so where it's basically the last chance for something to be included in the October fork** which anyways just time wise it kind of is but maybe that's a way we can better sort of discriminate between the two forks is moving whatever's tentatively accepted to accepted in the next call. Using that accepted list for the October fork and then continuing to discussion on the other tentatively accepted list for the  q1 2020 fork.

**James**: yeah I was thinking that as well 

**Danno**: Agree.

**Tomasz**: I think, the strong message for the community is these are  EIPs and these are the actions that we are expecting from both champions and community  need you to deliver as for benchmarking testing and pointing out any vulnerabilities, security wise and the clear message as well what we  rejected it is not coming back. So people know that there is 10 or 11 EIPs on the list, as we see on the list that they clearly considered for Istanbul and this is what we are focusing on now.

**Tim**: Great does anyone else have anything they want to bring up?
Okay then for the first time in months we finished early, so happy to give everybody four minutes back. Thanks everyone !!

# 6. Testing Updates
# 7. Client Updates (only if they are posted in the comments below)
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
# 8. EWASM & Research Updates (only if they are posted in the comments below)
 
	
	
# Attendees
* Alex Guchowski
* Alex Vlasov
* Adrian Sutton
* Casey Detrio
* Danno Ferrin
* Dimitry Khoklov
* Georgios K
* James Hancock
* Rick Dudley
* Tim Beiko
* Tomasz Stanczak
* Leonardo Alt


# Date for Next Meeting: August 15th, 2019 at 22:00UTC.
