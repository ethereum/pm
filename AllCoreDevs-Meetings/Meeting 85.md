# Ethereum Core Devs Meeting 85 Notes
### Meeting Date/Time: Friday 17 April 2020, 14:00 UTC
### Meeting Duration: 1 hr 35 mins
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/164)
### [Video of the meeting](https://www.youtube.com/watch?v=KlzwFLOj6Bw&feature=youtu.be)
### Moderator: Hudson Jameson
### Notes: Pooja Ranjan

----
	
# Summary
    
## EIP Status 
| Status | EIP |
|-------|----------|
| Accepted     | EIP-2315, EIP-2537| 
| Discussion continued | EIP-2515, EIP- 2583 |
| Dropped from Berlin. EFI, but Request for Champion | EIP-2456 |
| Client to do more test and measurement|EIP-2046|
| EIP introduced  | EIP-2565, EIP-2602 |
| Eligible for Inclusion | [Refer EFI tracker](https://github.com/orgs/ethereum/projects/5) |

## DECISIONS
	
* EIP 2537: Clients will give an update on plans for integration in next meeting. 
* EIP 2456: It's on the Berlin list but without a champion it doesn't make sense to move it so James is moving to remove that from the Berlin list but remain it as EFI with a tag for a request for Champion and go see if someone shows up but until then won't be discussed on this call.
* EIP 2046: Clients just need to do more tests and the measurements.
* EIP 2583: Needs to get more input from developers.


## ACTION ITEMS

* EIP 2565: Benchmark it for Parity and testfactors to benchmark this for Parity to see if in terms of speed, they’re on par with Geth.
* EIP 2515: James will work on charting to have a better discussion about it. 


-----

**Hudson**: Hello everyone and welcome to the Ethereum core devs meeting #85 of Ethereum All Core Developer call. I'm Hudson and we're going to start with the first item on the agenda. It is the Berlin EIPs that are confirmed getting implementation updates from the clients and seeing if there are any issues anyone's having so far with that. I'll pass it over to James to go over the Berlin EIPs.

# 1.Berlin EIPs

**James**: The ones that we talked about so far are EIP 2315 Simple Subroutines for the EVM and EIP 2537 which is the BLS curve operations. Ones that may or may not be included are the 2515 difficulty bomb and 2456 time-based upgrade. So, let's start with 2315. Is there any updates?

## [EIP-2315: Simple Subroutines for the EVM](https://ethereum-magicians.org/t/eip-2315-simple-subroutines-for-the-evm/3941)

### Geth

**Martin**: It's not been updated content wise but testcases. Yes, there was some bug in the go implementation, how the Opcodes are defined. I demanded one more test case.
Implementation wise - started implementation in Parity. There’s a new one brewing and we will start making EIP test cases into actuals based on Geth implementation. That’s it. I don’t know if Parity has to add anything on that about implementation?

### Open Ethereum (Parity)

**Artem**: Open Ethereum is up and starting review and hopefully, it will be sent. 

**Martin**: Cool, thanks.

**Rai**: Hey you mentioned adding the test case, were the test case is not sufficient in the EIP or was there some corner case or was it more of a mystery to EIP?

**Martin**: Just a clarification. I try to write a  test cases for everything that can be a bit quirky and one of the quirk cases that you might have seen at the end of the code segment and when you do return from the subroutine it should continue after work leftoff which is outside the range of actual code. That's what I do. 

**James**: Are those things that should be added to the EIP itself or do they just need to be ..

**Martin**: I already added them to EIP itself, it was just a clarification. So nothing really changed in the EIP recently.

**James**: And then there's a Parity and Geth somewhat implementation?

**Martin**: yes

**James**: Okay is there anything from Besu?

### Besu

**Tim**:  We also have an implementation, the PR is up, still under review. I think we should probably have it by the next core dev call, it should be pretty final.

**James**: Great! and as we're transitioning from talking about developing the EIP to implementing it, we previously had updates like Berlin updates have been from authors about the EIP itself, but moving forward I'd like to get updates from the clients on the status. So kind of expect that those questions will be on the agenda for the next few calls until we're ready to deploy.
Is Nethermind here? Tomasz?

### Nethermind

**Tomasz**: We didn’t start implementation but I don’t expect any trouble with this one.

**James**: Yeah that's great, we can move on unless there’s other thing someone would want to bring up on that topic or I'll move on to the next EIP?

## [EIP-2537: BLS12-381 curve operations](https://github.com/ethereum/EIPs/pull/2537)

**James**: Okay so for 2537, is the BLS for of operations. Who do we have on the call for representing that ? What is the the status of implementation for that? Is Alex here?

**Alex V**: Well I can respond, as far as I know at least Danno has asked me to reference implementation. It's complete and it's updated to the latest spec which was changed due to general sentiments that kind of one precompile should be made into two, for clarity perspective. It else was updated to reflect at IETF draft was changed recently. But reference implementation and Go implementation are by (?) follows a use spec,  so it can be just taken and integrated.

**Martin**: I have a question here. So the reference, the IETF spec was changed, is that correct?

**Alex V**: Yes, the IETF spec. Its separate document and IETF wasn’t that I was asking anyone. It was changed, say change the suggestion, how to watch a treat as a sign of field element because there is a selection rule for square root and you’ve to select one of those. It was changed, it became much simpler but it would change the output of the function so the code was updated to this new version of spec.

**Martin**:  How’s that related to the existing stuff in Eth2.0? Does it relate at all ?

**Alex V**: As far as I know and seen in discussion, it’s not a problem for Eth2.0 because it will be (?) based and even much more previous and outdated spec. So, for them even the previous versions of spec would be breaking changes. So it's not a problem,as far as I know. Maybe someone else here, they can answer, but I am not in Eth 2.0 directly but it's at least what I know right now.

**Martin**:   One thing I think we should talk about is this split into two EIPs. It was proposed by Danno. Axic was a bit against it. I really don’t know but I guess it makes sense to officially decide how to go about that ?

**Alex V**:  What do you mean by changing it into two EIPs?

**Martin**: Well, let the current operation into two separate - Z1 and Z2

**Alex V**: Just following the discussion in the Pull Request, I change the  mapping function which before the change, could take other 64 or 128 bytes and output also different lengths. I change it to be explicitly to separate pre-compiles. One taking 128 and another taking 64 bytes. 

**Martin**: Maybe  we weren't on that discussion so maybe we should just decide  in this forum if it was a good thing or not. Because Dannoo wanted it, Axic was a bit opposed it and I really don’t know and I'm just curious to know if people have opinions about it.

**Alex V**: Maybe I should clarify some general sentiments from Axic. Right now it's nine separate precompiles.  Sentiment from Axic was it should be collapsed into one with another binary interface.  Sentiment from Danno was just, previously it was 8, which one should be separated? So, its kind of either we have separate function or we have one with much more complicated binary interface. Because before it I think people wanted to have a simple pre-compile possible.  So one to one function and no internal routine, I changed it to separate ones. It’s up to the discussion. Previously the sentiment was to split it as much as possible. 

**Axic**: In my comment, I made it clear that would be the ideal case for me but I know the sentiment was really in favor of having separate pre-compiles. So I don't have any hopes that it will collapse into one. I just didn't want it to , you know never bring it up. But I know that this given BLS pre-compile in its current form is an expected result of the same discussions that it was one complex pre-compiling, it was split into separate pre-compiles. So I don't think my comment would be taken into consideration anyway.

**Martin**: I thought your comment referred to only the most recent but then I was wrong. 

**James**: What do you want to say, what your reasoning is for that Alex so we can just have that as part of the record ?

**Axic**: It’s coming from a developer experience point of view, the original four pre-compiles  which is SHA 256 and easy recover the identity and those were supported by all the  languages true language constructs. But then a new pre-compile wasn’t and every case, when somebody is making use of those pre-compiles there implementing the own way of passing data and the same is going to happen with these 9 or 10  pre-compiles.  We've seen one example of that done in the deposit proxy and the complexity that introduced there and my reasoning is that we already have to swell a well understood ABI encoding used by the system and I think it would be really nice to make use of the ABI encoding for the pre-compile because then you wouldn't need native language support but you could; I mean Native specific language support for new pre-compiles you could just rely on the standard encoding to interact with pre-compiles. The reason this was bought previously, maybe even a few times. The reason I am against using the ABI encoding was that it is supposedly ambiguous but I think the encoding logic is strict but the decoding logic isn’t. We can make the encoding here quite strict so I think this reasoning wouldn't stand. I also made a comment there that  even if we have  multiple pre-compile, I’d still prefer to use a version of the ABI encoding for the same reason. The last reason I mention why it could be useful to have a single pre-compile is looking into the future when maybe these precompiles won't be precompiles any more rather they gonna be contract and in that case because they're such an overlapping functionality between at least some of these new precompiles, then you’d duplicate all of them into its new contract. For this reason it was probably too far-fetched and it shouldn't really be taken into account but the other reason, using the ABI encoding I think is a valid one. 

**James**: At this point, I think it’d be hard to go back and be able to meet the Eth2  stuff to get done so just from a practical perspective, going back I don’t think is really a good way right now. But an ABI encoding is something that can be resolved later or have like a ABI encoding precompilers that developers to use for better experience? 

**Alex V**: (Not clear) All the internal packing just go by itself.

**James**: As for my memory, Martin the primary reason to split them is for security in reducing service area for vulnerabilities. So maybe the middle of between is  at the precompile and ABI.

**Martin**: I don’t know I haven't particularly looked at the actual form of the inputs for this precompile. I think it’s sound okay to have ABI on the input format. I also think that we should keep them in its current form as separate precompiles.

**James**: Okay so we should add a note to or maybe Axic you and I can talk about getting something about the ABI; what did you say that inputs need to be more strict?

**Axic**: I mean is it possible to specify really strict version of  rules, while still being capable of using the ABI and encoding as it is. But actually just want one comment, going back to the original question which was whether the precompile for mapping. But anyway, the question was whether it should be a single one where it determine the operation based on the input length or there should be two, each of them expect a specific input length. I think with the ABI encoding  those should be also separate because it makes the ABI encoding some more clear and so probably, my preference would be also to separate them.

**Martin**: Yes I think we’re in agreement then. 

**James**: Great, are there any other thoughts on this from the group? 
Alex V. as far as spec and implementation and stuff like that how is kind of timeline or the amount of work that is a how finished is it versus not finished ? could you spend a second to talk to give an update about that?  This is in context in trying to get a schedule.

**Alex V**: As far as I know, right now we are at two full implementations which were done specifically for this precompile are a legacy from 1962 in Rust, which I did. Another one in Go. As far as I know, Go implementation it now also confirms to update the spec. So in this time source are complete. Also starts with fuzzing testing for now it's only been tested separately so just to find internal bots with a lot of internal protection disabled, so far for like a day already I didn't catch him crashes later I will continue to cross test 1 versus another. But at the moment I would say those are ready to be integrated. 

**James**: So what's left to be done is I guess another question?

**Alex V**: What’s left to be done is just cross test some against each other. For integration, it’s not to me it’s to client developer 

**James**: So cross testing needs to be finished before integration starts or is that something that can be started?

**Alex V**: No, integration can be started, already. Fuzzing testing will continue anyway separately in parallel. In any case fuzzing testing will not affect the bindery interface and gas price.

**Hudson**: You're cutting out a bit Alex V. but I think we got the idea.

**James**: Yep I thought that was my internet so it's good thanks for letting me know Hudson. So perhaps **we leave next meeting to get an update from clients on plans for integration** or is it something we should talk about now? Tim you have something to say ?

### Besu

**Tim**: In Besu, we already started to look into how we integrate libraries as part of Besu and its WIP. It seems like it shouldn’t be too complicated and in the next couple of weeks we should have it done.

**James**: Okay, great!

### Geth

**Martin**: From Geth’s perspective I don't think anyone has done any work on it. 

### Nethermind

**James**: Nethermind?

**Tomasz**: Don’t expecting any issues. 

### Open Ethereum

**James**: Open Ethereum?

**Artem**: I think we had a pull request to merge 1962 but I think it was Alex and it was close today and not merged by the author. I didn’t really look why but other than that, we have no progress here. 

**James**: I see.

**Alex V.**: I did close a pull request  for 1962 as its not going to be integrated. I did not perform any integration with Parity for 2537. Ideally I would appreciate, if Open Ethereum developers can  just do it themself and it's just an easy one to feed the inputs to the function switch to take bites and output  bytes.

**James**: I think that's good for that EIP, is there anything else someone would like to bring up on the BLS recompile EIP?

So the next one so those are ones that we've already decided as going into Berlin.


# 2. Eligible for Inclusion (EFI) EIP Review
### [EIP-2515: Difficulty Bomb](https://github.com/MadeofTin/EIPs/blob/patch-16/EIPS/eip-2515.md)

**Hudson**:  All right and then we can move on to EFI now. We can go back and forth on this. 

**James**: You can moderate it and I can talk about it.

**Hudson**: So,  the first one is the EIP 2515 for the difficulty bomb EIP related to Berlin so I think that’s James, right ? We can go right ahead.

**James**:  Yeah, the feedback that I got last time I talked about this in February and January and then we haven't really talked about it since in the call. So, I'll give a general overview and find the [link](https://github.com/MadeofTin/EIPs/blob/patch-16/EIPS/eip-2515.md). So the idea is to do pretty much the same thing that the difficulty bomb has done except for say that it will start on a specific block so you in a x number blocks in the future you say at that point freeze the difficulty and an increase by 0.001% each block perpetually. So you get the effect of the difficulty increasing block times and making them doing all the same things that the difficulty bomb has done. We just know exactly when it will happen.The updated design was having that linear increase happen instead of it just freezing which is a better design so I've updated the EIP to have that information. One thing to confirm is it something that the group wants and then if it is, is it something that can be done in time for Berlin? And the current open question is do the increased function of difficulty should it be linear, Iike purely linear or like a 1000th of a percent are sufficient? Which of those are your preference? So going back to the group on general sentiments and stuff. I did a lot of polling and talking to people on Twitter about it. So I've since reduced it to being what it is now. So feedback on the design or change?

**Tomasz**: James, the linear growth is a bit dangerous because it's disconnected from the actual hash rate curves and it's potentially being exposed to miners, we are signing a lot of mining power and spitting up the block creation, which is against really the idea of the difficulty bomb. I was thinking about the solution, I mentioned it to you once, about changing the target block time instead of changing the difficulty. Because one of the parameters of the difficulty calculation is the one that points us more last at how often the blocks would be created. I was suggesting to grow this parameter and then we know that the whole thing will behave as it should behave. So automatically adjusting the block time depending on the hash rate, hash rate curve but at the same time will achieve the goal of the difficulty bomb, so the blocks will be  longer and longer and still be growing ideally linearly with each block. And still can adjust based on your main design idea of starting at a particular block and having predictable time when it launches.
**James**:  Yeah, it does. There is a potential that if it goes off the miners could rush and then they would rushing into the end where they no longer can catch up.  So it'll have the same effect as an eventual obsolescence of the chain because no one can mine it cuz it's too difficult. Blocks will be so slow that it won't be mined.

**Tomasz**: But we’re talking here about the linear growth so, the miners will assume the exponential growth for the hash rate, so there will never the time when they will not be able to catch up.

**James**:  Well, there also will at some point never be a time even if it's linear. I give it doubles in about 15 days which is the current algorithm.

**Tomasz**:  No it doesn't matter because the thing is you removed from the equation entirely, the hash rate from the previous blocks which means that you leave just in your linear growth  and the hash rate will be growing eventually faster than linear even the miners do not do anything in specific, you’ll expect the hash rate growth will be extra linear. 

**James**: Oh there has to be some limit to the actual amount that can be done and this is assuming that we’re not working to fix it. So perhaps this is an argument for having it remain the exponential and so not linear growth and having it be percentage of the last block 

**Tomasz**: As I said, just leaving the parameter, the target stay block length and changing this parameter would be enough and then we stay with the behavior of the function and adjust pace on the hash rate. And we’ll not risking the suddenly it will be more than we plan for less than we planned and it’ll be just linear growth of the block time which is very predictable. 

**James**:  I don't know enough about client implementation to know which one of those is easier to put into the client.

**Tomasz**: I am not talking about the client implementation, sorry! I am talking about Ethereum, the algorithm that is there, the defined algorithm for calculating the difficulty.  It's taking into account the previous block time and adjust based on the previous block time. The faster the blocks are the more of the adjustment there will be. And I assume, if I understand properly the algorithm proposed by is a linear growth which removes entirely the previous block time from the algorithm.  Suddenly the growth of the hashrate becomes linear and this is risky because whatever miners do,  we lose the control on adjusting the times of the blocks based on the previous block time. 

**James**: To clarify, the new design isn’t linear; it is an exponential curve to start it just starts at a certain difficulty.  I am curious as to the group, cuz the in the in the code itself it checks whether it's less than 10 seconds or greater than 20 seconds and then it has an effect and the mathematics of it is also kind of a little bit hard to depart. So changing those variables over just having over having a extra linear increase on hashrate overtime, is there a preference to the implementation? For me both of those end up in the same place indicating that it is in the super linear (or whatever you want to call it) equation.  Or if you're increasing the time they both get to the same place, so I would be curious from the client implementation side which would be a preference? As per the design, they are both good. 

**Tomasz**: Client implementation is really such a simple thing here. It’s just fine line difficulty calculation. I think we should just discuss the function itself whether it is correct or risky or what the outcome would be. I think any function that  removes the previous block time from the calculation, I wouldn't be happy to introduce such a function to the difficulty bomb.

**James**:   Can I get some other thoughts here perhaps Martin or the Besu team on preferences ?

**Martin**: I need to ask a question, the first one that you proposed, what would happen if there was a large increase in hashing power as the linear thing started? It would rise up  a lot fast, right?

**James**: Yes.

**Martin**: There would be a quick block and the linearity would rise very quickly. Whereas with what Tomasz proposes it would adapt to the hashing power more gracefully, right? That sounds to me like perhaps the simpler Model to keep using the time instead of just block numbers. I don't know, it sounds like it's me.

**James**:  All right, I get some help on changing the design again and making sure I get that right, is my concern but that can be resolved.

**Hudson**: I lost my link here. Okay so for that one's there will be more discussion offline, I'm guessing?

**James**:  I guess so if is there more people that would agree with the preference that they having just addressing time would be a better function here cuz I'm I'm happy to do that I just like to know that's the direction I should go, from the group ?

**Wei**: I think that would be better than linear increase like Martin mentioned, what if there is a large hash rate miners coming in. I see a problem for the current design. 

**James**: Besu, do you have any thoughts?

**Tim**: None on my end. One thing that I’d just like to see is different models, if there is a way to graph different scenarios and see like high level overview like what Martin said, what happens in case of an increase in hash rate. I know that EF team has done that for 1559, I just shared the [link](https://github.com/ethereum/rig/blob/master/eip1559/eip1559.ipynb) in the chat here. Something similar to that would be valuable as we’re discussing this with the community and say, hey this is the current bomb and here is why it’s bad, here is this different proposal. Here’s what happens when hash rate  increases /decreases you know that the kind of basic edge cases.

**Martin**: Yeah, the way I see it as, in one proposal the block number is in the x-axis and on the other proposal you have the calendar on the x-axis. Do we prefer linearity graphs with time on x-axis? Or do we want the linearity on the graph with block numbers on the x-axis?
Another thing is a key difference between what we discussed right now. 

**James**: Tomasz what would be your response for that?

**Tomasz**:  I understand the problem but I don't know how exactly. I'm just trying to find a plot that you are using whether there was time or block number on the x-axis? Generally, I think that's what we want to have a small as you want to target there's axis like they don't do approaches to be equal, like the growth of time is more or less similar to the growth of the block number on average. And then for the difficulty bomb you actually want them to start diverging, so over time they while the time is expected to be stable the Block number would be expanding and then the plotting would be with the time would be better . More or less I’d like to have the block time on the y-axis and the time on the x-axis and show how the difficulty bomb would cause this particular chart to behave.
I want the difficulty bomb change if we decide to change it because it's not like I really need this change. They don’t like the block time to keep growing and then we want to see different scenarios whether we assume the linear growth of the block time or the exponential growth of the block time or like step by step as it was in the past like exponential steps. These are the functions that I’d like to look at  and then I'll like to adjust the difficulty of the collation function to lead us to one of the preferred scenarios. I see Martin's Point in mentioning how we would like to chart it and how we would like to discuss it.

**James**:  So I'll **work on charting** so we can have a better discussion about it. It will be done offline.


### [EIP-2456: Time Based Upgrades](https://ethereum-magicians.org/t/eip-2456-time-based-upgrade-transitions/3902/11)

**Hudson**: Okay, sounds good. Next up we have the time-based updates EIP 2456, that's the one that Danno did and then I forgot who took up on that if anyone.

**James**: I can take over for this one. We had two calls ago Jason Carver was on and we talked a little bit about this and we arrived at a, this is my read of the of the group and if I'm wrong, please correct me on this but it seemed like if we could do time-based fork that would be preferable.  The issue is if we do it with the current Uncle rules then we have to have a look back function for it to be safe and that's not preferential for due to some client developer user experience and then also user experience for contract developers. To fix, the other option is to fix the uncle rules and so that you can have just the time and not have to have a look back function but that seems to be possible yet complicated and so what's left for that EIP
will need someone to Champion moving it forward and 
to understand is it desirable enough from the community or the people that would want it that it's worth the trouble of putting in ?
And I don't know the best way to answer that last question. But that's kind of the status of that EIP.

**Hudson**:  Is anyone championing it?

**James**:  Not at this point.

**Hudson**:  I think it **should be dropped off from discussion if no one's championing it**. Since that's what are the requirements for something like this to move forward in the first place and otherwise just going to slow down chat every two weeks.

**Martin**:  Yeah I agree. We’ve been discussing it every two weeks and not really making any approach. 

**Hudson**: Yeah , if someone wants to be a champion on this feel free. You would talk to James me and Danno about it or really either one of us three and we would connect you where you need to go to be the new champion on it. 

**James**: EFI, but Request for Champion makes sense at least for a time. If a champion doesn’t show up then it should expire EFI. I’d propose.

### [EIP-2046: Reduced gas cost for static calls made to precompiles](https://ethereum-magicians.org/t/eip-2046-reduced-gas-cost-for-static-calls-made-to-precompiles/3291)

**Hudson**:  Next EIP 2046 reduce gas cost for static calls made to pre-compiles and the last time we talked about this we were talking about how measurement has been done in Open Ethereum and was found to be safe to reduce those cost but that it would need to be looked at on different machines on different clients, if I remember correctly. And then there was a lot of discussion on whether we can lower this, these other precompile costs and we can raise these other costs. So I don't know if we concluded anything last time that was like a substantial next step of the day that the Blake2 cost is higher than Keccak that would be discussed offline. I'm not sure if anyone took up on that or not. Also that approving gas cost of Blake2  may help them move to stateless Ethereum. I don't think we had anyone who could confirm that last call so this is just going over what was discussed last call about it. I think this is Axic’s  EIP and he's championing it, am I right or someone else doing that Alex ? 

 **Axic**: So it’s about 2046?

**Hudson**:  Yes, are you the  champion currently the EIP and are there any updates to it from your end from any discussions you had?

**Axic**:  Probably I am a bad  champion of it and Alex V has done quite a few benchmarking steps, we discussed it on the last call but I think neither of us have done anything to incorporate those results into the EIP, I think. We probably still don't have a final idea what would be a good proposed value of what Alex did was benchmarking to precompiles to make sure that none of them would be a risk if we were to reprise the static call. The finding he had is that two at the precompile side. If I recall correctly, I think these two are slightly under price so they would need to be increased.

**Hudson**: Martin, did you have something?

**Martin**:  Yeah I think I took it upon myself to do corresponding benchmarking at Geth and no progress there. 

**Hudson**: Sounds good.

**Tim**: I want to ask Alex, we also have been doing this benchmarking for Besu. It’s on a to do list and we just want to make sure that it is still a valuable thing for you.

**Martin**: As a node implementer is it valuable to you? The prices are set?

**Tim**: Yes,  so I guess I'm the last call there was a discussion that may be lowering the prices even more and I was just wondering how we're moving along. Obviously once we implement this, will benchmark and make it work but  it is valuable if we say benchmark and find as low as possible price and it works and bring them back to the EIP?

**Alex V**: Well if I may add a little, I started writing a much more radical proposal in a sense that we should really reprise all the precompile by having more approach to it and else would be more restrictive about what would be performance differences between different clients.  Just because for example the implementation in which is used by Open Ethereum  is just very slow compared to everything which exists for the last 2 years starting from to work on zcash to now implementations of 1962. And there I wanted to include a proposal that we actually make call data and precompile to be  zero and always absorb the cost of doing the gas estimation into the precompile cost itself. It will basically increase constant contributions but we will now pay a reasonable price for what precompile actually does. And this will actually make Blake viable and they will build the changes to Keccak precompile to better reflect it’s internal structure.  That it actually doesn't make any difference between 0 and 128 bytes. I am not done with this spec yet. 

**Hudson**: I really like that idea of doing a broad sweep of all the pre compiles and seeing what can be adjusted to make it more efficient in clients but also as fast as possible in clients. Any other comments on that? At this point, I think for this one we'll talk about Berlin timing in a second but it doesn't sound like there's any word we're kind of just still doing some measurements right now and then this new EIP is being developed by Alex V. so that is the latest for that one.

 **Martin**: That doesn’t have anything to do with this particular EIP which is  on the discussion.

**Hudson**: Well that doesn’t have to do with it specifically but if he makes that, that will be superseded and that would be something that makes sense.

**Martin**:  Yeah 

**Hudson**:  Okay, so **the client just needs to do more tests and the measurements**,  that sounds good.  So that's all for EFI. 

# 3. Berlin Timing

**Hudson**: James, do you want to go over the Berlin timing?

**James**:  Yes we're pretty close to I'd like to kind of a good estimate of what the integration time it would take to get the BLS EIP done cuz it sounds like that's the one that would take the most work at this point. Is there a sense for how long that would actually take from the clients ? I guess we could say it will be done in 4 weeks and then we can have a testnet  running for 4 weeks and then we can hit go on the fork.

**Martin**:  Yeah, I don't know what Peter says I would say no sooner they cannot be integrated before anytime sooner than 4 weeks. What would you say Peter? 

**Peter**: Are we talking about single EIP ?

**Martin**: Single EIP with 9 precompile, BLS 381 curve operations?

**Wei**: So probably something about our current timeline is based on just having two EIPs in Berlin, right?

**James**: Right, that and possibly the difficulty bomb one if it is simple enough to have in but not something that we should push back anything for. So those two plus maybe the difficulty bomb. 

**Hudson**: From what Alex V. said, there is a Go implementation and a Rust implementation  but it hasn't been close looked at by the client implementers, it's just been implemented outside of the core implementer team, is that accurate ?

**Martin**: Yes.

**Hudson**: So if that's the case then until they look at it I don't know if there's going to be a good estimate,  is my guess for that one. For simple subroutines that's something that they have been are the most clients have been implementing our have implemented and we talked about that earlier and I think most people said it was on its way to being implemented and wasn’t too bad, right?

**James**:  Okay so rather than say how long, let's do the list of priorities like we did last time and just say that the BLS 12381 Curve operations should be a priority unless someone disagrees so that we can by next time have a better idea of Berlin timing and we don't kick the can down the road. Anybody opposed to that or have any comments or alternative ideas ?

**Tim**: Maybe just like **highlighting both the EIPs** like if I guess clients can look at 2315 and the BLS one. I think we **will get the implementation started** if possible and in next two weeks we have a feeling for how far along they are?

**Hudson**: I think that's the best we can do today in my opinion. Anybody have a different opinion?  How's that sound James, this is kind of your call ?

**James**: That sounds great to me.

**Hudson**:  Alright ! unless there is anything else, we will move on to item number 4.
This is EIP 2565 repricing of the EIP-198 ModExp precompile.

**James**: Before we do that should we just say outloud the process point for the time based one, so that can be recorded? it just came up a lot. 

**Hudson**:  Yeah sorry I forgot. So you’re talking about the thing that we’re talking in the chat?

**James**: Yes. You can go head for the record 

**James**: It's come up because it's on the Berlin list without a champion it doesn't make sense to move it so I'm moving to remove that from the Berlin list but remain it as EFI with a tag for a request for Champion and go see if someone shows up but until then we don't need to talk about it on this call. I motion for that.

**Hudson**: Yeah sounds good to me and if there isn't a champion, this is something that the EIP IP meetings can look at, for the process flow of something being made into EFI and then losing a champion cuz we don't have a process flow for that right now.


# 4. [EIP-2565: Repricing of the EIP-198 ModExp precompile](https://eips.ethereum.org/EIPS/eip-2565)

**Hudson**: Going back to EIP 2565 Repricing of the EIP-198 ModExp precompile, that's Kelly I believe.

**Kelly**: Hey everyone!  so I just wanted to take a few minutes to introduce the EIP 2565 s Hudson mentioned it is a repricing of the ModExp precompil of a EIP 198. EIP 198 was introduced a couple of years back by Vitalik for Marginal Exponentiation Operations. It was foundational arithmetic operation of a variety of cryptographic operation. I believe Vitalik introduced it  for RSA signature verification.  We've been using it for VDF proof verification and it's also relevant for things like snarks and accumulators in a variety of other cryptographic operations. As we started (screen sharing)  what we saw is  that the pricing of this EIP or what you'll see these blue dots here was significantly more expensive than some of these precompiles. On the order of 100s of millions of gas per second where is other precompiled begin the most recently the Blake 2 EC recover or all sort of this 20 to 30 million gas per second range. So, the core of this **proposal is to change a single parameter in the pricing formula and e i p 198 from a value of 20 to 200 and what that would do with it would shift disorder blue curve here to pricing in line with this yellow curve now so we get about a 10x reduction in the cost per operation and it still remain sort of more expensive than some of these other things like the Blake precompile in EC recover by provide the good practical savings for the precompile with very minimal implementation changes**.  So basically just changing its parameter from 20 to 200. We did explore other ways to improve the efficiency of this pre-compile, the one of the things that and you can also see if you look at this is that we did devise a more accurate pricing algorithm, which can be seen here for different input values into the precompile versus the existing one. 19% vs  20% in this is because this new algorithm better relates to how the arithmetic is done and big integer libraries. Currently we do not recommend making this pricing change as it may have a higher implementation cost than just changing that parameter. Although it is something that we’re open to and wanted to get some feedback from folks on. And then finally I guess the last thing I'll say we did also look at the efficiency of this precompile in the library that use today versus some other big integer arithmetic libraries, there are further games again here by switching out this underlying library but again **this is not something that we're recommending at this point because it has additional implementation complexity**.  Summary is basically what we'd like to do is change a single parameter in the EIP 198 pricing formula from 20 to 200 which will bring the pricing you know closer in line to you know some of the other precompile fits around this 30 million gas per second.

**Martin**: I have a question. So those with benchmarks, what was the underlying implementation.

**Kelly**: These are all using Geth. 

**Martin**:  Because on old benchmark, we did say that Modexp could be like cut in half at least in Geth but Parity was actually (could not catch). And there was note that  the exponentiation by squaring plan to optimize it. I have no idea if they done so, they're still 
exponentiation by squaring. So I don't know how these benchmarks that you have charted out in the EIP are actually sustainable on part.

**Kelly**: Yeah,   it is something that that we looked into, we haven't run those benchmarks yet. We did notice though that sense that  this EIP was implemented, I believe that there were some changes to this precompile, I'm not sure if that was the underlying library or maybe they're more cosmetic changes but we did see that servers are commits against sort of this precompile of the code base.  So I think we can certainly look at it for Parity as well to see what they have it and what their benchmarks look like?

**Alex V**:  Even while I don't work in a Parity client, I looked at their implementations before. The problems their at least before was it say they use the native (?)  library which is standard Rust library for this and internally this library uses 32 bit instead of 64 of Mother processors, which makes it highly inefficient. While Geth uses the Go library provided by Google which uses optimal. SO, I think a simple update to the underlying library would be sufficient to Parity.  

**Kelly**: Yes thanks Alex, that’s great feedback and I think I would be happy to take a look at Parity to either run the Benchmark or come back and provide any updates on that, if folks  would like. As shown here, there's a variety of other benchmarks that could be used or other libraries that could be used like GMP and Open SSL. I suspect that similarly for Parity there reduction but that's something we cannot into the EIP is in the Benchmark on Parity.

**Peter**:  So just to point out something, so probably start using open SSL and stuff like that. The reason they will be a lot faster is because they will probably use all kinds of SSA , EVX etc. which as far as I know, Go does not use. The downside of this is you are pooling in a big soup of C code and also losing a bit of portability. Eg. standard way of using open SSL, you’ve open SSL installed and use it as a shared library. Which means if I’ve EVX engrave, my open SSL will be faster; if you don’t have then yours will be slower. But Go the static linking, it essentially means if we build Geth on some machine which has EVX and then you try to run it on the machine which does not have it, it will blow up and if you do it the other way around, then you just lose the performance. So you  start on producing these kinds of strange build timer constraints. 

**Kelly**: Yeah, I know. It's a great point, I mean I think .  Just to reiterate you know our hope is that as we go Benchmark Parity.  But right now at least the repricing doesn't require any change to the library under Geth, right? With no underlined Library change or pricing algorithm change you know it still stays in line with our precompiles. Our hope is, we see the same thing for parity. As Alex mentioned, maybe Parity already using the improved libraries vs the benchmarks.

In the case of Geth, we got 2x better, and these are just from underlying improvements in the Go libraries, essentially. Parity has also seen similar improvement. At this point, action item is **to benchmark this for Parity to see if in terms of speed, they’re on par with Geth** and if so, the recommendation is just changing the parameter from 20 to 200 and not changing the pricing formula or underlying libraries.

Okay great, I mean unless there are any other questions, I think that's it. I think just to factors that are there and then we will take a look at what that import of what that implies from the sort of gas per second for Parity. This precompile is more expensive than the other precompiled, right? So we're not trying to move this down below like pricing of EC recover or the Blake 2 precompile. And if we can achieve that with this simple parameter change then, that'll be all that we’re advocating for.

**Hudson**: Awesome, one last question and you might have said this and I just missed it but this repricing what is the **ultimate goal** of this as far as use cases go ?

**Kelly**: **Marginal exponentiation is used in writing cryptographic operations, verifying RSA signatures, verifying VDF proofs, RC Accumulators as a replacement versus Merkle roots  or something like that, verifying SNARKS basically a broad number of cryptographic operations will benefit from this repricing.**

**Hudson**: Okay awesome!
Anybody else has any comments?

**Tomas**: This is a great justification. This is what we’d love to see for every single EIP. This is why we change things and tell the community that they all review why we are implementing things. 

**Kelly**: Thanks, appreciate it and thanks for the feedback everyone. 

**james**: We should save it for the EIP IP meeting.

**Hudson**: Actually Kelly where is that posted?

**kelly**: This this EIP it is just under the EIPs.ethereum.Org.

**Hudson**:  The document you just displayed on the shared screen.

**Kelly**:  Okay, that is the EIP actually.

**Hudson**:  Sorry I thought it was like a PDF or something. 

# 5. [EIP-2602: Disable null hash message verification for ecrecover precompile](https://github.com/ethereum/EIPs/pull/2602)

**Hudson**: Okay next up we have a EIP 2602 Disable null hash message verification for ecrecover precompile and that was Wei.

**Wei**: Yes, this is very simple EIP. The background is to have the EC recover precompile and that does signature verification to the curve. We learned last week that the pre-compile that we have is low level and it allows the user to directly pass any hash they want. And it turned out if you pass the new hash which is 000000, it turned out in this case the signature can be forged, so it's not safe to use the easier however in this case at all.
The crypto thing is actually that if you use EC recover with all the power hash functions then the whole thing is safe. With the proper hash function there is nearly zero chance to get the new hash but if the contracts are doing something weird and just happen to have a new hash, then it becomes unsafe. The EIP proposes to disable verification for new hash. (could not capture, t=1:16:00) when the message hash is a new hash. It does the same thing as the EC recover does for the invalid signature. This has nearly zero valid use case for new hash at all. It's actually possible that some contract might have misuse that's because the precompile default parameter is a new hash. If the contract is going to pass messages then they can get into this trap. We actually found one or two contracts on the Gorili testnet that try to valid signature again as a new hash message.  So I think that's entirely unsafe. The EC recover function is a very low level function, it does specify hash but I just think we encourage it to stay by default construct for Ethereum. So disable those unsafe scene. That is the introduction about this EIP.

**Martin**: Sounds good.

**Hudson**: Anybody has comments or questions about this EIP intro? 

**Alex V**:  There exists a trick which could be potentially usable or used by some contracts already. I just was looking for a [link](https://ethresear.ch/t/you-can-kinda-abuse-ecrecover-to-do-ecmul-in-secp256k1-today/2384/17)  for it. So if you just disable using message hash, it can be a common wallet. I think, 
This is up to the implementer. EIP should be posted as security vulnerability and contract developers either should upgrade or put an exclusive requirement. Do not have zero hash and actually want to verify the signature and not use any hacks around it but forbidden it's right now may affect properly working contracts which actually wanted to use this. 

**Tomasz**: I wanted to raise exactly the same thing that Alex mentioned about the existing contracts but if we can confirm that this is not the case and there are no contracts executed now, then maybe it's worth to fix it the way,  Wei  suggests.

**Wei**: Can you explain more, a wild use case of a new hash?

 **Hudson**: Alex is breaking. Would anyone want to speak upon Wei’s question?

**Martin**: Tomasz can you expand on that?

**Tomasz**: Martin, Alex posted to [link](https://ethresear.ch/t/you-can-kinda-abuse-ecrecover-to-do-ecmul-in-secp256k1-today/2384/17) in the chat that mentions one of the use cases that Vitalik was suggesting on Eth research.

**Wei**: I am taking a look. From my understanding this looks to be a way to get a cheaper gas price for EC new operations, I’ll be using the EC recover or something like that from my understanding. 

**AlexV**: It was a trick posted by Vitalik to not get a cheaper operation. I mean you could always write a EC Point multiplication or addition in Solidity contract and then send, yes, it will become expensive. But there was no any form of precompile which allows you to do curves  operations over (?) curve. So this was a clever trick how you could abuse it to get a multiplication function, and the addition function was cheap, you could implement it in Solidity.  I don’t know any solid examples who uses this but since it's no trick maybe someone does . But I don't think there is any way, we can verify that no one does use this trick. It should be considered more precompile vulnerability, not precompile, particular contract vulnerability. Then in principle, say it's a precompile vulnerability.  

**Hudson**: Okay, anybody else have any comments ?

**Pawel**: You can check if it's used by implementing the track and accountant and sync the block trie from the beginning.

**Wei**:  Yeah, I remember this one was actually due to a consensus issue we had on the Open Ethereum master branch. So, the upstream did an update. The ICCP 256 K1 library did an update, the Rust library did an update and I think this new hash message tech and we missed that for a while. During the time, I don’t think we broke the mainnet but we did find one or two contracts on the blockchain in the Gorili testnet.  I still don't know what they are doing or are they just using the trick or is that actually verifying a new hash message.I am not sure. So the thing is, we had a new hash message in the Gorili test net but I don’t think we found it in any mainnet, at least from our knowledge. 

**Hudson**: Anybody else?

# 6. [EIP-2583: Penalty for account trie misses](https://github.com/ethereum/EIPs/pull/2583)

**Hudson**: Next up we have a EIP-2583: Penalty for account trie misses, that's Martin.

**Martin**:  Yes, so I talked about this two weeks ago. And  the idea has been expanded a bit with some alternatives.  And in general, I'm curious to hear that any of the developers have taken a look at this  and are having a thought whether it’s worth pursuing? I personally believe that it most definitely is, **its denial service protection**. So people do you have any opinion on this thing?

**Tomasz**: I was looking at it and it's an interesting step to take in exploration also on the research on stateless clients and it's charging 40 trie axis and weakness generation. So even if in the end it is implemented  in the form it suggested it is definitely worth exploring and even playing and checking what the outcome is. 

**Hudson**: If you just said it's good for stateless Ethereum,  is their coordination being done with the Stateless Ethereum team on this or is this something that wouldn't be applicable.

**Martin**:  Yeah I've discussed it with the stateless context.

**Tomasz**: At the first, I think from Martin’s message on the stateless Ethereum channel, sorry Martin for interrupting. 

**Martin**:  I see it as something that should be implemented as soon as possible on mainnet because there's a pressing need for it whereas for stateless is more of a research project that can be take it one step at a time and I'm not sure, I mean I think there's a pressing need for its and I'm not sure if there's enough time or interest from those group.  I think people working on stateless have  100 problems that they are going to solve eventually and this is maybe priority number 95.

**Hudson**:  Okay, that helps me understand that a lot more, thank you!

**Martin**:  Whereas from my perspective, this is one of the pressing problems on the mainnet right now. 

**Tomasz**: I am definitely in favor of this one, it's a good thing to understand. I just mentioned that this is also a great addition to the stateless Ethereum but obviously they are in the timeline in the research group are totally different. 

**Martin**:  Wei, Open Ethereum, do you guys have any thoughts about this?

**Wei**: Not really, it's not hard for us to implement so well we’re fine.

**Hudson**: Martin, I know last time we talked you didn't want to move to EFI yet if it's something you'd want to try to move to EFI with today or does it need to be cleaned up more?

**Martin**:  It doesn't need to be cleaned up more but I think **it needs to get more input**. The initial proposal has a floor, if you put the penalty above around 700-800, it can be bypassed so there's no point in doing that. Whereas there’s an alternative which changes the size a little bit also makes it possible to set an arbitrary high penalty. There are different downsides because it break backwards compatibility in different ways. I just want some more discussion on that and not necessarily decide on EFI or not, right now.

**Hudson**: That sounds good, anybody else?
Okay, we have about a minute left I think that gives us enough time for Dimitry to do a quick testing update. 


# 7. [Quilt Team's Account Abstraction Announcement](https://github.com/ethereum/pm/issues/164#issuecomment-615260298)

**Hudson**: So if you don't mind James and skip to the Quilt item just because they have to leave in half an hour and once we get rolling on the EFI it'll probably just keep rolling. So, Quilt team just take a minute or two and explain what you guys are doing to get everyone up to speed.

**Will**: Cool, that should be pretty quick.  We included a link to our implementation rationale doc which goes through some of the benefits of a minimum implementation of account extraction.  This is originally [suggested on Eth Magicians forum by Vitalik](https://ethereum-magicians.org/t/implementing-account-abstraction-as-part-of-eth1-x/4020). So we are moving forward on doing implementation on that in Geth, there a couple research items that we still need to figure it out but most of the main questions are already answered for this minimal implementation at least. So we are going to move forward on that and we'll kind of keep you guys up to date the date of that we get everything there and will eventually go through the formal EIP process. A couple things to keep in mind so we've largely, Quilt has largely been working on execution environment in a lot of things under Eth 2 phase two.  We were focusing some of our efforts on this right now is it's a kind of a strong way to iterate on some of those things we want in a long term for this kind of merged Eth1-Eth2 ecosystem. An account abstraction and some of the other things that we went to the doc, SSA and other pieces are like a natural iteration value that can be added right now to kind of get to those steps. There is four of us, will keep you guys up date on what we're doing and yeah I’d say go through that [doc](https://hackmd.io/y7uhNbeuSziYn1bbSXt4ww?both), if you guys has any questions, just ping any of us on the Quilt team. 

**Hudson**: Alright, thanks so much. Anybody have any quick questions about that ?

**James**: This is for getting into account abstractions into Eth1 so like preEth2 implementation?

**Will**: Yeah for now we're focusing on Eth1 and and then in that document we have some discussion on what we do then to begin bridging some of this to Eth 2.

**James**: Oh that's great!

**Will**: Right, yeah first step is done with Eth1. I am very happy to hear that and I'm sure Mariano's going to be happy about it too. 

# 8. Testing updates

**Hudson**: Dimitry if you want to go ahead.

**Dimitry**: Oh yeah, one minute. 

**Hudson**: You’re cutting out Dimitry, we can’t hear you. 

**Dimitry**: (unclear audio) This is an idea, it’s the concept. I can send you a link for discussion. We think to implement it with the Go team. They think they can support this approach, they think tools to produce state transition can be useful and easy to implement on client dev.  So, just try to do it and see how it goes. And I would like to hear feedback from other client developers on what do they think about this approach and how difficult it will be for them to support eventually. I am sending the [link](https://github.com/ethereum/retesteth/issues/88) in chat.

**Hudson**:  Great if you could write that all up in chat cuz you cut out a couple of times. you cut out enough that like rehashing that over text is going to be a great idea.

**Dimitry**: Okay I sent the link to chat, there's a discussion invite to the developers and send some feedback on how difficult it is for them to implement. 
 
**Hudson**: Ok, thanks so much. 
# 9. [EIPIP Survey](https://docs.google.com/forms/d/e/1FAIpQLSeadXscoQgrKznUOAEB_jSzNNFKHWDEFJxKH1LpDsDsC6mXpw/viewform)

**Hudson**: We’re out of time. Do the EIPIP survey please, if you’ve not done so. We really want a good amount of core developers and EIP editors to do it. Also anybody who has ever looked into EIP can do it. I am posting that in Gitter and YouTube chat and probably post it to twitter once again. So, please participate in that if you’ve not already and we will see you in two weeks. 

# 10. [Review previous decisions made and action items (if notes available)](https://github.com/ethereum/pm/blob/master/AllCoreDevs-Meetings/Meeting%2084.md)

Couldn't be discussed.


**James**: **Point of process**, did EIP 2565 go into EFI or is it something that we do next week?

**Hudson**: Next week minimum, because it just got introduced. 

**James**: Alright.

 **Greg**: Hudson, no discussion. I just want people to know that I’ve taken over as Champion for the Prog POW proposal.

**Hudson**: Okay,  that sounds great. You said with Christy or of Christie's proposal ?

**Greg**: With Christy's blessing 

**Hudson**: Okay it cut out. Great we will talk to you all on May 1st at 1400 UTC in 2 weeks. Thanks everyone, goodbye. 

## Next call: April 28, 2020 14:00 UTC. 
	
# Attendees

* Alex Vlasov
* Alex Beregszaszi (axic)
* Ansgar Dietrichs
* Artem Vorotnikov
* Daniel Ellison
* Daniel Weaver
* David Mechler
* Dimitry
* Greg Colvin
* Karim Taam
* Kelly (Supranational)
* Hudson Jameson
* Mariano Conti
* Martin Holst Swende
* Pawel Bylica
* Péter Szilágyi
* Pooja Ranjan
* Rai Ratan Sur
* Robert Drost
* Sean 
* Tim Beiko
* Tomasz Stanczak
* Wei Tang
* Will Villanueva

## Links discussed in call:

* Tim: https://github.com/MadeofTin/EIPs/blob/patch-16/EIPS/eip-2515.md
* Tim: https://github.com/ethereum/rig/blob/master/eip1559/eip1559.ipynb
* Tim: +1 on that. If someone champions it they can come back on the call once they’ve done some progress.
* James: A point of process: We can move it off of the considered for Berlin List, and mark it as “Request for ChampionBut remain as EFI ?
* James: EFI, but Request for Champion makes sense at least for a time. If a champion doesn’t show up then it should expire EFI. I’d propose.
* Kelly: https://eips.ethereum.org/EIPS/eip-2565
* Alex: https://ethresear.ch/t/you-can-kinda-abuse-ecrecover-to-do-ecmul-in-secp256k1-today/2384/17
* https://github.com/ethereum/retesteth/issues/88
