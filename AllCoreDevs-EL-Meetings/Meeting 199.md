# Execution Layer Meeting #199
### Meeting Date/Time: Oct 24, 2024, 14:00-15:30 UTC
### Meeting Duration: 1.5 hour 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1177)
### [Video of the meeting](https://youtu.be/3Y8X9_W9ecg)
### Moderator: Tim
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 199.1 | **Pectra Devnet 4 Updates**  Developers launched Pectra Devnet 4 on Friday, October 18, 2024. EF Developer Operations Engineer Barnabas Busa said the following clients are experiencing issues on the new devnet: Erigon, EthereumJS, and Grandine. Pectra Devnet 3 has been shut down. Busa and his team will conduct further tests of clients on Devnet 4 in the coming weeks. Then, developers discussed various specifications changes to Pectra that should be included for Pectra Devnet 5.
| 199.2 | **Pectra Devnet 5 Specifications Changes**  The first were changes to the gas costs for EIP 2537, precompile for BLS12-381 curve operations. For months, developers have been debating the appropriate gas costs to price operations interacting with the BLS curve, a cryptographic signature scheme that will make signature aggregation and zero-knowledge proof generation more cost-effective on Ethereum.A developer on the call with the screen name “Kev” explained that one of the outstanding issues about the EIP related to whether subgroup checks should be included in cost calculations has been resolved. He said due to potential dependencies related to the subgroup checks developers will keep these checks included in cost calculations. He added that he is concerned about the use cases for this EIP in practice among smart contract developers. “Some of [the app developers] have infrastructure that make it pretty hard to switch away from BM 254 to BLS 12-381 so I’m not sure what the use cases for this precompile are,” said Kev.
| 199.3 | **Pectra Devnet 5 Specifications Changes**  Another developer on the call by the name Paweł Bylica said that he does not think that a 2x increase across the board is a good proposal for accurately repricing BLS operations. Bylica recommended restarting the cost analysis from scratch and rebuilding a new “lookup table” for operations. Besu developer Gary Schulte agreed that there were some operations in the EIP that were already overpriced based on his benchmarking analysis so a 2x increase across the board would not be helpful. Developers agreed to redo the cost analysis and prepare final numbers for implementation and testing on Pectra Devnet 5. Beiko recommended using next Monday’s testing call to coordinate with client teams on the status of EIP 2537 repricing efforts.
| 199.4 | **Pectra Devnet 5 Specifications Changes**  ASecondly, Geth developer Felix Lange presented one specification update to EIP 7685, general purpose execution layer requests, and a related change to the Engine API. Most developers on the call were in favor of these changes. However, Lange noted that he expected some pushback on them from consensus layer (CL) client teams as these changes may have an impact on their implementations of the EIP. Beiko said that based on the approval for the changes expressed thus far, they should be added for implementation on Pectra Devnet 5 for now. Busa said that these two have already been included to the required specifications list for Pectra Devnet 5.
| 199.5 | **Pectra Devnet 5 Specifications Changes**  Thirdly, a developer by the screen name “Frangio” shared changes to EIP 7702. He explained, “[EIP] 7702 currently introduces a new type of account that can change its code hash. … This is a strictly new kind of way of changing the code hash, because it can happen even if the code doesn't include self-destruct [and] even if the code doesn't include delegate call. So, it weakens the guarantees that one gets from looking at the code hash of an account. If a contract relies on [the code hash] to trust the way that the account is going to behave, it could be vulnerable, because it's able to temporarily masquerade as a different kind of contract.”
| 199.6 | **Block Gas Limit Increase Debate**  Erigon developer Giulio Rebuffo’s proposal to increase the block gas limit from 30m to 60m gas, Beiko briefly mentioned a comment on this week’s call agenda by Ryan Berckmans, an Ethereum community member and investor. Berckmans has raised several questions related to defining and tracking the minimum bandwidth requirements for operating Ethereum validators. Beiko recommended that developers with thoughts on this matter chime in on the Ethereum Magicians thread.
| 199.7 | **Block Gas Limit Increase Debate**  Rebuffo shared updates on EIP 7790, controlled gas limit increase guidelines, and 7783, add controlled gas target increase strategy. Rebuffo said that implementation work for EIP 7783 has been completed in the Reth, Erigon, and Geth clients. He added that the Nethermind team also plans on implementing EIP 7783. He shared his follow-up proposal to EIP 7783, which is numbered EIP 7790, to double the block gas limit gradually in a linear fashion over the course of 2 years. He said he gathered feedback on this proposal from several client teams and the majority have told him that they foresee no issue with the increase.
| 199.8 | **Block Gas Limit Increase Debate**  Nethermind developer Ben Adams wrote in the Zoom chat that he supports EIP 7790. Geth developer Marius van der Wijden was against the proposal saying the increase to 60m requires further research and testing. Others such as EF Researcher Toni Wahrstätter said developers should not increase the block gas capacity without first limiting the maximum block size through an increase to the cost of call data, as defined in EIP 7623. Geth developer “Lightclient” said that he would like to see progress on EIP 4444, history expiry, before implementation of EIP 7790. Rebuffo pushed back on many of the disagreements about EIP 7790 saying that the increase would be gradual over two years so there would be runway to implement EIP 4444, along with EIP 7623, after the activation of EIP 7790. Rebuffo added that unlike other EIPs aimed at improving scalability, EIP 7790 does not require a hard fork and so it would be easier to implement and coordinate across clients.
| 199.9 | **Revert Error Codes for Contract Calls and November ACD Call Schedule**   Lange presented a case to add official revert error codes for contract calls to the Execution API. Lange said, “We have received this issue multiple times over the year that people have complained there's no standard way to get access to the revert data when accessing contracts using the eth_call, eth_estimategas, or eth_bidaccess operations. We would like to basically introduce the way we've been handling it in Geth as the official one. In Geth we have this error code, error code three, that we use for this purpose. The most important thing is just to have a defined error code and just basically ensure that all the clients behave same way
| 199.10 | **Revert Error Codes for Contract Calls and November ACD Call Schedule**   A few developers on the call expressed their support for Lange’s proposal. Beiko recommended continuing the conversation about it on other channels and moving forward with it assuming there is no further pushback on the matter.Beiko recommended cancelling the ACD call on November 21, as it is scheduled to occur a week after the Ethereum developer conference, Devcon. Support for this recommendation was not unanimous among call participants. Van der Wijden, Busa, and others expressed that they would like to keep the call on the 21.

**Tim**
* We are live. Welcome everyone to ACDE 199. bunch of minor but important Pectra updates today, so we'll catch up on that. But then also on a bunch of different changes to EIP. So hopefully we can close out the subgroup. Check conversation for EIP 2537. had two PRS to 7685 he wanted to discuss. There was a minor change proposed to 7702.
* And then I wanted to do a last check on including 7742. as per the last, ACDC and Gajiender has a small modification for this as well, so you can chat about that, figure out, how that would look. first five spec. and then aside from that, there was this conversation around validator bandwidth that we never quite got to on the last CD. some stuff around the gas limit. and then, the APIs, to. Oh, and yes, the 200 celebration, would,  happen right before Devcon. So, yeah, we can celebrate that at Devcon. to kick us off, I don't know, do we have, Barnabas or Perry to talk about how Devnet 4 is looking? 

**Barnabas**
* Yep. I'm here. So last week, Friday, we have started Devnet four, and we have shut down Devnet three. Since then, we have had a pretty good participation rate. we have a few clients that are still having some issues. hopefully we can get some help on them. So, clients that are known not to be working are currently Aragon and Node JS on the execution layer side. And, grinding seems to be the one that is still struggling with a few clients, but they are now also proposing some blocks, so it seems to be a bit more intermittent. 

**Tim**
* Sweet. anyone from any of those teams want to chime in with some more context? For Ethereum JS. Looking into it. Okay. Any other updates on Devnet 4 for that? Anyone wanted to bring up? 

**Barnabas**
* I have started the bed block, production again this afternoon, only with a single node for now, but we'll grow that into like 3 or 4 different nodes later on. 

**Tim**
* Anything else on the Devnet 4? Oh, Grandin solved some of the issues yet. the other one should be solved soon. Nice. Anything else on the Devnet 4? 

**Barnabas**
* Not from me. 

**Tim**
* Okay. Next step then. BLS. So there's been a lot of conversation around potentially, removing the subgroup checks, splitting out the subgroup checks. over the past week, a couple people have, a couple people have, reached out to, different L2's and other potential users of BLS as well as investigated the libraries, themselves. I don't know if we have. yeah. Does anyone want to give an update on that? I'm either on the side of the community outreach or the actual libraries. 

**Kev**
* I can give an. Yeah. Oh. It's working. Yeah. so on the decision, it seems that we're moving towards, just having the subgroup checks in. one reason was that one of the dependencies, it's pretty hard to see. What. It's pretty hard to get good confidence on what will happen if it's removed. and it's. Yeah, it's pretty hard to read. It seems like from our outreach that the ZK snark folks, at least the ones we reached out to. Aren't sort of like saying we want. This is the best way to say it. some of them have infrastructure, and that makes it pretty hard to switch away from being 254 to BLS 1281. so I'm not sure what the use case is for this. Pre-compiler.
* I mean, there are possible use cases, but it doesn't seem to be like the Zk-snark folks are at the moment. 

**Tim**
* Thanks. Anyone else have context on that? 

**Stokes**
* Yeah, I could add a little bit. essentially, yeah. I think the investigation Kev was talking about was really helpful because it does sound like, what's the dependency?  It's like, not clear what happens if we don't have them. The subgroup checks, so we'll go ahead and keep them in. That gives us like a pretty stable, you know, interface. Now to proceed with like final gas benchmarking. And then separately yeah we can keep thinking about different use cases and reach out to different community members to try to get a sense of like, yeah, the expected use of this thing once it's live. And yeah, that's a thread that can keep running even over the next month or two. But yeah, I think we're unblocked at the moment, which is good. Awesome. 

**Tim**
* And on the benchmarking, I know it's been a couple of weeks since I followed up there, but, my sense is we still didn't have quite, consensus on what the right price for, a subset of the calls should be, like, still correct. 

**Kev**
* I think we do now with the subgroup checks in, I think it was, to just 2X the current cost. 

**Tim**
* So, okay, so like the original proposal of, yeah. Adding a factor of two on, the discount table for those calls. 

**Kev**
* Yeah. I believe everyone was on board with that. 

**Pawel Bylica**
* Yeah, I'm not sure I fully agree with this one, because since it's this original gas cost doesn't fit like the shape of the curve, we think, and we just try to use something that wasn't a good fit in the beginning and like, multiply by two. But, I think we can, like, spend next week to, like, figure it out exactly how this is supposed to work and if the other people will be in favor of the original proposal. I'm also okay. 

**Tim**
* Yeah. I think there's probably value if you want to spend a week or so looking at a better proposal. Yeah, we. And we should, I guess. Yeah. We should ideally have a final merged. In the next week or two so that we're not blocked on that to launch future Devnets. 

**Kev**
* Sorry, what was the issue of the two x? Is it just that it's like not exact enough power? 

**Pawel Bylica**
* No. It feels to me that, we start with some like, I don't know, like lookup table. That wasn't good in the beginning. And we just keep the lookup table by just multiplying everything by two. In the same sense, we can just create a new lookup table that actually fits the the our timings more, more closely. I mean, it's kind of the same amount of benchmarking work. It just it's not like so clear that you multiply by two, but you just put new numbers and maybe it's not even needed and lookup table anymore. And so that's what I mean exactly. 

**Kev**
* Okay, that makes sense. 

**Gary**
* When we were benchmarking in basic against narc, we found that we were using the 150% proposal, not the two x. And we found that even with 150%, the G2 was way overpriced. G2, MSM. So if we two x that I think that's going to get even more overpriced. 

**Kev**
* Oh, that makes sense. Sorry, I thought everyone was sort of in agreement, but yeah, it seems like we need to redo the numbers from scratch then. 

**Tim**
* If we were to do that. yeah. Paul, what's like the timeline that you'd expect here? Is this something that you can benchmark in a week? Do you need client teams assistance? 

**Pawel Bylica**
* Yeah, I don't know. But it feels to me that it's kind of the same amount of work. We just put different numbers in the end into. 

**Tim**
* Well, I guess. Yeah. Like one part I'd want to be sure on is like, what's the what's the flow here where I'm. My sense is when we did the two X proposal, every individual client team ran those benchmarks on their. On their end. so is so I assume here there's like some work of proposing your curve or like a. You know, like a lookup table for, for prices and then, having clients confirm that. Is that correct? 

**Pawel Bylica**
* Yes. I think what what happened is that with two x, like everyone is within the safety margin, right. So the worst case out of all this lookup table numbers, it's fitting like the expectation but. There may be some outliers in the, in the other side like in the other places that makes them, like, maybe too expensive, I don't know. to my understanding, no implementation is is hit by this subgroup. Checks more than plst at least what I get from data I received. So it's a bit it's  more on the north side unless they can fix the performance in the implementation. I think it's a bit more on their side to propose the numbers.
*  If they think like two x it's like great I will accept that. But so I don't think we need to take the pre-assumptions from four years ago when trying to find the the good gas prices. It doesn't save you any work if you just take like this this, Yeah. This, like original work in gas prices from four years ago. We can just put new numbers and and it doesn't make all this process take longer. The longest part is just to do the benchmarks and collect data. 

**Tim**
* Okay. is that something you have the bandwidth to take on and that other teams can assist with? 

**Pawel Bylica**
* I don't know. I need to I mean, I can plot the data if I get one, but I don't think I will be able to benchmark every client, so. 

**Tim**
* Okay. Yeah, I think I. 

**Pawel Bylica**
* Think we need to figure out how to exactly do this right. I'm not that great at this, actually. But if there's no one else who can actually do like similar spreadsheets I did some time ago. 

**Tim**
* So I think maybe what we can do then is we have the testing call on Monday. If all of the client teams can make sure to send someone there to who could help with the BLS benchmarks. And Pavel, if you're able to attend that too, that would be great. And we can yeah, zoom into that discussion on Monday and make sure that we yeah, we have a plan for benchmarking this. 

**Pawel Bylica**
* Okay, I'll try, but I think Monday is quite busy for me, actually. 

**Tim**
* I guess. Yeah. Sorry, Kev. Yeah. 

**Kev**
* So what exactly is needed here in order for us to reach a decision? Is it just, some set of inputs and then we just show what the timings are? because I think a bunch of clients have already done that. 

**Tim**
* Correct? Yeah. So we had the clients do this with the two X proposal. So what we need is what's arguably a better proposal than the two X. And something that I guess is it's more like a granular, like, yeah, a granular repricing per call. and then having the clients rerun the benchmarks on that hardware or sorry, on those numbers. 

**Kev**
* Okay. I see. Yeah. and Pawel, you're saying that the benchmarking process is the hardest part because I think we don't need you to actually do that since you've already done it for everyone. We just need the clients to do that. 

**Tim**
* Okay. Yeah. I think if Pawel can propose a set of numbers, like a lookup table, and then the client teams can benchmark that, we should be good. And so we get. Yeah. So I would suggest like sorting out the details of this. We can use the R&D discord. but then on Monday if we can. Yeah. Check that we have everything sorted. That would be great. And, if you can't make the call directly on Monday. Pawel. If there's a way for you to share, like async, either a proposal or like what's needed for a proposal, that would be. That'd be quite helpful. Okay. Okay. Cool. Anything else on BLS? Okay. Thanks everyone. So yeah, we'll move forward with that. And again, we'll keep the subgroup checks as part of the EIP. next up. Felix had two PRS he wanted to discuss for EIP 7685 is, Felix on the call? 

**Felix**
* Yes, I am. Can you hear. 

**Tim**
* Me? Yes we can. yeah, I just posted your first PR in the chat. excluding the empty requests data in the commitments. 

**Felix**
* Let me just quickly explain. So basically, I am proposing this, because we noticed during the implementation of the devnet four changes that, it's very inconvenient for the LS. To have, empty value of the, the empty value of the request hash depend on which fork is currently active. So, for example, this is, if you initialize a new chain, and add the genesis block, the fork, like the Pectra fork is active, then we need to compute the empty request hash, in the Genesis block and at the with the current devnet 4 definition. This is basically the request hash with three EMT requests this and but in a future fork this might change.
* So basically every time now, it's just going to add a whole bunch of code to the Genesis initialization where we have to figure out like the, the, like, empty request. And then more generally, like there are certain cases where you want to produce blocks just for testing purposes, but there's not going to be any kind of SQL. So it doesn't really it's not really necessary to bother with the requests at all. And then it's like, you know, it's just nicer if you just hard code this empty value there. Like that's the main motivation, honestly. And yeah, that's only possible if it is not dependent on the fork. So this is where the proposal comes from. And I mean the corresponding change in the engine API.
* I only propose it just because we feel like it's much easier if there's a canonical sort of request list that is shared both on the engine API, and it's also used for the commitment.
* Right now we already have this bifurcation of the commitment and the engine API. I personally think it's quite bad. So basically we have to what happens is when we commit compute the commitment, we have to add these type bytes, for the request. 
* But then in the very last minute on the engine API, the typewriters were removed. And so this already means right now that we have two different representations of the request list, one which is only for the commitment and only which is one which is only for the engine API. And so I'm just proposing to make these two the same again by also removing the empty request from the list, which is shared on the engine API, and adding back the type byte. 

**Tim**
* Thank you. And anyone have comments thoughts on this? Okay. Roth is in favor. I know. Thank you. I think approved the changes as well on the PR directly. Ethereum JS is in favor. Does anyone, I guess, disagree with this change or have significant concerns? 

**Felix**
* I'm pretty sure if I had proposed it on the ACDC next week, I would have been some backlash because it does mean that the CLs have to add one more check, which is that they have to now validate that the request items are given in strictly increasing order just to ensure that, for example, because with the Typekit, it again introduces an ambiguity that wasn't there before. However, I do think it's a minimal it has minimal impact, but it does have some impact on the CLs. So maybe someone from the outside. Should speak up. And I mean, I mean, I think it's a minimal impact, but it definitely has an impact on the class as well. 

**Tim**
* Any CLs on the call have strong opinions. Okay, so Loadstar should be okay. Lucas from Teku had already plus one it. So my sense is we can probably go ahead and include these two PRS as part of the Devnet five spec, and aim to get them they're already part of the spec. Awesome. yeah. And aim to get them merged by next week's ACDC. And if there's any CL level issue that comes up, we can address that on next week's call. Um. 

**Felix**
* Yeah. Okay. Thank you. 

**Tim**
* Yeah. Thanks, Felix. Anything else on this topic? 

**Felix**
* Well, not from me. 

# Update EIP-7702: Remove delegation behavior of EXTCODE* EIPs#8969 [21:45](https://youtu.be/3Y8X9_W9ecg?t=1305)
**Tim**
* Okay, I'm moving on then. next up, we had a proposed change for 7702. so I haven't quite followed the conversation on this, but supposedly it was due to some back and forth on Eth magicians. yeah, I don't know. Does anyone have context on this PR, to remove the delegation behavior of Ext-code

**Frangio**
* Just a quick context. So 7702 currently introduces a new type of account that can change its code hash. this is currently somewhat possible if the contract has delegate call. And since, the delegate call changes, you know, only if it uses in the same, transaction as creation. but this is kind of a strictly new kind of way of changing the code hash, because it can happen even if the code doesn't include self-destruct, even if the code doesn't include delegate call. So it weakens the, guarantees that one gets from looking at the code hash of an account.
* If a contract relies on that to, trust the way that the account is going to behave, it could be vulnerable because it's able to sort of temporarily masquerade as a different kind of contract. so it does seem like something that we should look into. we've looked we found a couple of code samples that appear to be affected, but nothing really too serious. But we haven't really done a thorough search, so the proposal here is to, only delegate code execution. So exit code hash. Would an exit code copy would just act on the delegation designator, instead of kind of following the delegation pointer that seems, just sort of more normal in line with what an EVM proxy is. And so it just seems like it would, just be less surprising in terms of the effects on applications. 

**Felix**
* It should be noted that the code hash will still change. All right. Like if you change the delegation, you will have a different code hash anyways. Or is the code hash going to be reported as the hash of the delegation? 

**Frangio**
* Do you mean after this proposed change? 

**Felix**
* Yeah. So, yeah. So I mean, you were saying. 

**Frangio**
* Sorry. Go ahead. 

**Felix**
* So you were saying that basically the point of this is to ensure that account cannot change its code hash, unexpectedly. But I think if we don't do the delegation, we still have to take the hash of the delegation code. Yeah. So that basically means we still have you can still change the code hash of the account with 772

**Frangio**
* Yes. That's right. So, there's a stricter version of this proposal, more conservative, which is to, to do kind of like EOF contracts and just, look at the prefix so it wouldn't change, as you say. Although in this case, if it does change, it would at least not correspond to different code because the delegation designator is not valid code. Right. But it is another option that I would also be open to considering. 

**Felix**
* Yeah, I thought we actually have a proposal in EOF that says any code that starts with 0XF is immediately forbidden from for looking at. Isn't that the case? 

**Frangio**
* From executing zero x? 

**Felix**
* Yeah, but also like, from being introspective. Yeah. 

**Pawel Bylica**
* You cannot look it up. It will just behave as like some sentinel value. So for. 

**Felix**
* So it only returns 0XF basically. Yeah. So maybe that's what we should do for the delegation as well. Just but then it's actually worse because you can't you don't even know it's a delegated account. Basically you don't know anything about the account. And maybe that actually makes the problem worse. 

**Frangio**
* Well in yeah. So Ansgar is saying it's EF00. And in the case of delegated accounts it could be EF01 which is the prefix. So that would allow to to distinguish. But I don't know that that distinction is important. 

**Felix**
* Well I mean the contract could kind of know that it's a delegated account and then like reject interacting with it for example. So that would be the main advantage here. Just being able to detect within the EVM that the delegation is active for this account. And then you could be like, you know, I'm not talking to that account because it's a dedicated one. That's certainly something. But the contract would have to be aware of this concept anyway. So it doesn't apply to the old contracts because they don't know anything about this. It's just that would be a new security pattern that you have to introduce into your very important protocol. Like basically ensure that, yeah, this is just fallout from 7702 adding so much new attack surface, honestly. 

**Daniel**
* Yeah. so just one problem I have with this proposal is that, right now, all the opcodes that interchange that, that interact with code, like the call or exit code has, are completely oblivious of code delegation. They just get the code of the target. If we do this change the delegation is not transparent anymore to the EVM because we need like two ways to retrieve code, one that follows the delegation for calls, and another one like in the proposal code hash and the others that don't. So this breaks a bit. The assumption of 7702 that the EVM in the end, does not have to be aware of it.
* Also in the future when we introduce new opcodes that interactive code, it might be a bit error prone because we have to be careful which of the two ways, in case of 772 we use to to retrieve the code. So that's like my one, my one doubt about this change. 

**Tim**
* Got it. and yeah. Ansgar, do you want to talk about the EOF style behavior? you brought up in the chat. 

**Ansgar**
* No, I'm actually not. Not 100% sure. It could be that, you have, actually returns the kind of zero f hash as the major kind of hash if you try to code, inspect it. I think if that's the case, we should probably revisit this now that we actually reuse the 0XF domain, basically  for other things, things other than EOF. but what I'm saying is it would probably, there would probably be value in having a if we want to just return a magic byte which made like a, like a hash of a magic kind of pre kind of prefix or something. as the response. Now in the 7702 case as well, which I personally think would be just another principled step towards kind of like getting rid of code inspection.
* And then I think we should make sure that it's not the same, kind of magic hash that we use for EOF, because I do think there's value in being able to distinguish those two cases. And they're also conceptually not the same. Right? 

**Tim**
* Yeah. I guess it still feels like there's some discussion to be had on this to actually understand this sort of second order impacts and like, yeah, what it would look like implementing that in the EVM. what's the right way to like, move this conversation forward? is the ETH magician thread sufficient now? Do we want to have a breakout on this in the next week or two? Um. 

**Lightclient**
* I would love to just hear from some more DApp developers. I am weakly in favor of this change. I guess. You know, it's to me it's pretty much okay how it is, but it's also okay to change it. I don't think that this is this is not something I'm super worried about. But if there are more examples that could motivate changing the behavior, like I'm open to hearing them. The ones that I've seen are pretty contrived examples. 

**Tim**
* I think. Guillaume. 

**Guillaume**
* If you're looking for an example, it's not a dev developer example, at least not directly. But when it comes to any stateless gas cost model, if you have to do a jump to a different location, you're going to potentially incur a significant price for opening a new group. and what happens in that case is that some operation that you think is pretty cheap because it's just checking the code hash is going to have a jump to a location, open it and pay maybe, like 1900. Guess like 21,000 extra gas. that could be surprising. that could be. That could be breaking some contracts that expect, Xcode hash to be fairly cheap.
* So, yeah, just for your information, that's going like doing it, the current way is going to have an impact returning a default hash.
* Let's us just go to the current header that we already know about. And that's pretty cheap. So yeah, in terms of gas, this could introduce a very surprising, significant cost in the future. So I'm in favor of this proposal because it would keep the fairly cheap price that we expect. 

**Lightclient**
* Wait, why is it that cheap though? You don't know if it's going to be warm or cold. Right. The account that you're using. 

**Guillaume**
* You're going to call. Right. That's true. But I mean, instead of being warm once or cold once, it's going to be warm and cold twice. Yeah. 

**Lightclient**
* I mean, the same order of magnitude. And people need to be writing contracts to deal with changes in gas costs. Like, we could easily just say in the future that this needs to be twice as expensive. So I don't really see that as that compelling either. 

**Tim**
* Yeah. Frangio I guess. Do you have a sense of whether there would be concerns of using the sort of hard coded, return value like Ansgar was proposing or. Yeah. Do you not have a. Good. 

**Frangio**
* I don't have a super strong opinion, but it. Do you mean like, if there was a way to, tell apart that an account has been delegated. 

**Tim**
* So that, like. Yeah, instead of returning the delegated account, we just returned like a magic byte, like 0XF1, for any. Oh, yeah. 

**Frangio**
* I think that's fine. Okay. Yeah. 

**Tim**
* Yeah, I think I do agree that in the past we would, like we said, we want to move towards less introspection, and that feels like a clean way to move a bit further direction. but, yeah, I don't know. Was there a use case to actually return the delegated or the delegated account? 

**Frangio**
* There are certainly use cases one could come up with, but I think not a critical. 

**Tim**
* Yeah. 

**Frangio**
* Yeah. And nothing that exists already. Yeah. 

**Tim**
* So I think if that's the direction that like this group feels weakly in favor of, then maybe we should modify this PR have a hard coded value, returned and then try to get a last round of feedback from application developers on that before Devnet five. 

**Frangio**
* Cool. That sounds good. I can make the change. 

**Tim**
* Awesome. Thank you very much. yeah. So let's do that. And then, once you have the PR open, just, send us a pain so we can tentatively add it to the Devnet five spec as well. So anything else on this topic? 

# Moving EIP-7742 from CFI to SFI Update EIP-7742: update the required EL headers and the gas fee mechanism EIPs#8994 [35:09](https://youtu.be/3Y8X9_W9ecg?t=2109)
**Tim**
* Okay. And then, next up. So EIP 7742 on the CL call last week. we seem to want to move this to the fork, to separate the blob count from, to have the CL drive the blob count, there. So I guess. And then. Sorry, there was a proposal by Gajinder to change this. he opened the draft PR, for it, so I don't know. Gajinder, do you want to maybe give a bit of context on your draft PR? Yep. 

**Gajinder**
* So, basically, put 7742. what will happen is that CL will send the target and which can basically change theoretically block to block. And so the way this impact the phase, the, this impact how fee is calculated? On EL is that we have basically an excess gas accumulator. And where we calculate where we accumulate the deltas on each block, how much it's below the target or above the target, and then use it to calculate the fee, with the of in a way that so we have an update fraction, which basically makes sure that the factor by which the fees goes up and down, by which basically this, delta. Affects the fees is less than 1.11 to 5, because excess gas by this fraction is exponentiated.
* So, the problem with a dynamic target is that this you can't basically you can't you don't have a constant update for action. So what this EIP does is it normalizes the delta against some some target and then accumulates it. And then there is a normalized update fraction that is used to exponentiate and get the gas cost. So everything else stays the same. But now when you are calculating the excess gas you are basically calculating a normalized excess gas. And so which is basically target which is this target minus gas used by the target times some constant factor. And that, that factor we have chosen arbitrarily. So that factor could be chosen up or down, depending upon how large or small this number to be. 

**Trent**
* Good. Gajinder. Your mic is a little hard to understand. Maybe move a little bit further back. Or, I don't know if you could switch to another mic if possible. If not. Just some feedback. 

**Tim**
* It's not great, but yeah, maybe. Alright. 

**Gajinder**
* So yeah, basically that describes the change. I was almost done. 

**Tim**
* Thanks. Yeah, I think that's that's Yeah. We can somewhat hear you now. anyone have feedback or thoughts on this change? I know it's been. I think the PR was opened. yeah. Just yesterday. So. Any. Yeah. Any comments? Thoughts? 

**Stokes**
* Yeah. So I mean, I think the main thing to do today is just to move this to SFI so that, you know, we have it. there is this question. I think the issue that Gajendra is pointing at is that the, like, base fee adjustment, constant doesn't like it's hard coded essentially for the fact that we have six blobs. And so we'd have to change it eventually anyway. And then this is just now figuring out the right way to make it flexible enough under 7742. So everything works now works nicely. yeah. So I mean, I think we can iterate on that, but then separately, we do want some blob increase impact. Yeah, it sounds like and this is, required. 

**Tim**
* Right. So okay, maybe just to flip the conversation around, does anyone on the L side have a concern with moving 7702 to spectra as it exists today? and then maybe we can take some more time to review Gajendra's proposal in the next week or so. Last call. Okay, so let's move. 7742 to Pectra, and I'll make the change right after the call. We can have an async conversation on the PR, the agenda pull up, and then hopefully resolve this by next week's ACDC. and yeah, Barnabus is asking, if there's any client implementations started for 7742. I guess not much. Oh, Ethereum JS and Lodestar have PRS in the works. basically should be ready by the end of next week. Okay, Prism is in the work. 
* So. Okay. Some clients have started. Um. three. Anything else on 7742?. Okay. And then, Lastly. Devnet five. So we had a couple of PRS today that we decided we're going to add. it seems there's still issues with Devnet four. yeah. Do we want to spend at least another week working on Devnet four and revisit a final Devnet spec Devnet five spec? in the next week or two? Okay. I have a plus one from Barnabas. I think we'll move forward with that. and yeah, I think the only PR we mentioned today that is not tracked there doesn't exist yet is the change to 7702. 
* So as soon as we have that, we can include it to the Devnet 5 spec. Okay. Anything else on Pectra before we move on? 
* Okay. Then next step, I want to touch on the validator bandwidth point that was brought up on the last call, and we didn't quite get to. 
* I don't know is Ryan on this call? If not, I can just share his questions. I'll just post the agenda link in the chat as well. but yeah, quickly. So the first one was giving the giving the emerging importance of validator bandwidth and driving real world disaster contingency planning for the validator set. How do we feel about the existing scope and rigor of bandwidth research? are we doing a great job? Can we close the gap? occurs to him there's at least two different research area. research into internal bandwidth dynamics of the protocols and client implementations, and research into the external bandwidth supply available across the world, and how that's expected to grow and expand and how it changes in different parts of the world and whatnot. and  links an ETH research post with some more like technical versions of this.
* Yeah. Anyone have thoughts comments on this? Okay. If not, yeah. I will point people to the ETH research thread and we can continue there. I know there's already some responses by I believe, some lighthouse folks around, what's happening on the client side? yeah. So we can continue the conversation on ETH research. And next up, Giulio had a proposal for the gas limit EIP that we discussed a couple of weeks ago. yeah. Giulio, do you want to talk about EIP 7790? 

# EIP-7790: Controlled Gas Limit Increase Guidelines [43:35](https://youtu.be/3Y8X9_W9ecg?t=2615)
**Giulio**
* Yeah. So first of all, if possible, I would like to give a little update on 7790 just from an implementation point of view. So right now, I was able to implement it into ref Aragon and Geth. and and in that works I know Nethermind also planned to do an implementation, but I don't know if they actually did it, but I think they did. so this is just an update then regarding 7790. I did some asynchronous coordination amongst clients, and it seems that, I was able to kind of come to a to I think I was able to kind of come to an agreement for, agreement across the clients, across most people at least. on the on the actual guidelines. So so the guidelines I came up with that came up was basically target of 6 million gas over two years. And I took this with Nethermind and they were fine with it. Everyone is fine with it.
* I went to Geth and Peter told me that, there is no reason not to increase it. At least that's what Peter told me. Yes. There was some concerns from business. I haven't heard nothing from RAF yet, but I think Well, I think, but really, I didn't really earn. But, like, at least from a technical point of view, it seems that there is really  no reason not to increase it. I think, at least at least after discussing it, most people agreed at the end of the day. Right. So, yeah, there were some concerns from Besu yesterday, but I hope they are cleared. So I mean, I think we are kind of also ready to kind of at least take a decision here because, I mean, seems that the at least the majority agrees. 
* Maybe, Nethermind can confirm or if Peter is on the call, he can also just confirm. I don't know if he is, but yeah. 

**Guillaume**
* He's not he's presumably not on the call because he's on holiday, but I can like him. We discussed that in a stand up and I confirmed that he he agreed. 

**Giulio**
* Okay, so what about Nethermind, just so that we are sure that you're also on board? Is there something from. Nethermind? 

**Tim**
* There's a comment in the chat from Ben that's saying Nethermind. It's good. 

**Giulio**
* Okay. And okay. And Besu they had some concerns yesterday. I hope they are cleared.  And  Yeah. And what about Ralph. Because I heard nothing from Ralph. If they have an opinion or not. An opinion. 

**Onbjerg**
* Are we talking about including This in Pectra? 

**Giulio**
* No, it's not an hardfork. It's like you can. It's actually you can include it also a bit afterwards. So, like, it's not an artwork like the is not an hardfork. So you don't need to include it in. 

**Tim**
* Right. It's like the default the default behavior that you'd ship with the client, which also doesn't have to be the same across clients. Right. Like Yeah.

**Onbjerg**
* I don't currently have an opinion on this. I don't know who you reach out to, but, I haven't heard anything. 

**Giulio**
* Okay. And. Yeah. So regarding the. Okay, so there are some hands. So who wants to start? 

**Tim**
* Yeah, maybe let's do, lightclient, and then we'll do Enrico. Yeah. 

**Lightclient**
* Yeah. I think my general feeling on this is that we have some work that we need to do around history, and we haven't completed that work, and it feels very weird to sort of skip over the thing that's kind of necessary to just do a very easy change to the protocol and increase the footprint of clients. I would really like to see some progress on fork was made before we talk about increasing the gas limit. I mean. 

**Giulio**
* I mean, yeah, but at the same time regarding history and already kind of talked about it a lot, is that even if you don't commit to it. So first of all, this is a very easy change. Yes. And it can be implemented in less than a day. The testing is really trivial to do. Like it's just tracking a number. So I'm just gonna say that out of the way. And the second. But the other thing is that regarding history growth, if you choose not to do it, you're gonna end up with eating, the four terabyte mark for comfortable study data running in the same amount of time. Pretty much. It doesn't make a difference. So I mean,  if it's just I mean, I don't know you. I know that it's for you. It's just kind of a preference because you feel it's lazy.
*  But from a practical point of view, there is, I think, objectively, no difference whether you do the gas limit increase or not. So yeah. So okay. Anyway. 

**Tim**
* And let's maybe do Enrico and then Ben. 

**Enrico**
* If I'm not mistaken, we send gas limit as a configuration or for the proposer through the MeV boost when we do proposal registration of the builder network. So it's just a comment that if this happens, then this. This interaction must be changed. And this kind of static and the way it works. 

**Giulio**
* Not well, not really well, not really. I mean, after all, you can still suggest it. And if you don't specify, the builder is going to use whatever they have, which is Yeah, exactly. Thank you for that perspective. 

**Enrico**
* Honestly, it was just a comment that says there is an interaction. It's not pure EL thing. there is an interaction with the way CL talked to them builder. And we have to do some consideration there. Yeah. 

**Giulio**
* Yeah yeah. 

**Enrico**
* It's minimal. But it's something that we need to care about. Okay. 

**Tim**
* Yeah thanks, Ben. 

**Barnabas**
* With regards to history. History growth has slowed from blobs because a lot of the data is now going into blobs rather than into core data also the way it increases linearly over two years means the average increase over that entire period would be only 15 million. So that's the impact you've got to think about rather than the end impact. and I hope progress has been made on full force by then. And also that we've been included the core data increase. So I mean, if cold data goes into Lusaka, Lusaka maybe takes six months, say then it's only gone up to 37 million gas by that time. For instance, it's not, you know, it's not a straight shot to, 60 million. And we can also hold it at any time. 

**Giulio**
* Can I also add something really quickly? Because I see some people in the chat says that says that basically, that basically the impact of shipping it is not strong. Well, the thing is that actually, at the beginning I heard way higher numbers from people, not 60 million. At the beginning it was more close to 90. The reason why it's 60 is because we would like first to merge ships before actually making it more significant. But since 60 million is a start, why not? And also it's just a better a better way to increase the gas limit. So yeah, like objectively it's a better way to increase the gas limit. So I don't really. So 60 million comes actually from so 60 million is just it just comes from basically something that clients think they can handle.
* I mean the ones I talked to, that's what they think they can handle quite well. That's where the 60 million comes from. And but if it weren't for some things, it could also be 90. So in reality, in the future it's probably going to go up with the ships being merged. So yeah. Yeah. Anyway. 

**Tim**
* Yeah. Let's do a Stokes and then Marius. 

**Stokes**
* Yeah. I mean, I think you might have just touched on my question, but I do wonder where the 60 million number is coming from. Like, did we just decide to double where we're at now and then go from there? 

**Giulio**
* Yeah, basically kind of. Yes. And we basically first of all, we kind of tried to go for multipliers. I mean, I worked with Nethermind and we first it was we went for multipliers. so the first multiplier was like 90 million, because there was some consensus between Aragon and. Nethermind that 100GB of data was the max they would allow. But then they basically then we basically said no. Okay, wait, but maybe but maybe there are some other things that might get in the way. Maybe we should actually wait for some APIs to be merged. So we actually just say 60 million is actually very conservative. It's very slow increase, it's low impact immediately. But it's. Yeah. And just one thing actually.
* And actually one other thing, I want to just also say some add some more things. So that I am seeing. So the testing I saw somebody talking about testing by testing is for this API trivial. Like it's just tracking a number. Like you basically set a bunch of flags on a dev net and you just see if the number goes up. It's really and it's and it's deterministic. So it's not there is almost no unknowns there. It's just like it's easy to implement. It's easy to test. It's its low effort. And it is. And it's okay. yeah. 

**Stokes**
* I'm not opposed raising the gas limit, but I would want to see like a more rigorous analysis around all of the various considerations before picking a particular number. 

**Giulio**
* Yeah, I think to me it's just what. I mean, we are I mean, I can tell you that, that Aragon can definitely do 60 million. I mean, the number seems to indicate actually quite. Potentially quite. I mean, there are numbers. It is actually based on numbers. Like, it's not like just taking a random just out of multipliers. It's actually based on number. So, then the main reasons is kind of that we put 60 million was because we had doubts about about the whole data and some of because we don't scale very well. That's the TLDR from that perspective. But yes, it is actually, it is, of course, not just taken out of my head and just put it there for fun, right? 

**Stokes**
* Anyway, yeah. And I think just communicating. Yeah. Again, with more data and your analysis and thinking would help, help people get more comfortable with it. 

**Giulio**
* I mean, I wrote some blog posts. I also wrote, like an entire circle. And yeah, you can go check it out. I post it on discord so I can, I can I can share it with you later. 

**Tim**
* Marius. 

**Marius**
* So I think again having two debates at the same time. one debate is, whether we should increase the gas limit and whether we should or maybe we even have three debates whether we should increase the gas limit, whether, or what the what the good gas limit should be. and the other debate is like about the mechanism of increasing the gas limit. And while I agree that we should increase the gas limit, I am not knowledgeable enough about whether I whether 60 million is the a good number to land on. I think there needs to be more research and we made some numbers. But the problem is this a lot of the like worst cases grow exponentially with the amount of gas you have in the block. or at least quadratically with the amount of gas that you have in the block. So, we need to have a lot of, like, we need to really make sure that it works. and the other thing, the mechanism for it, I just don't agree with I don't think we should do these.
* These gradually increases. I think we should do Steps and steps of 1 million or 5 million gas or something. do a step. Decide. Everyone decides that we should do a step. And we will ship the next client version with this step as the default. And most people will update. So the gas limit will be raised gradually to that next step we will see how it works. and then we will, we will make a decision on the next step. I think this automatically like this automatic gradually increase is just, it's it's not great. It would in the case that something happens and this is, 60 million is not the, just doesn't work, and we see it breaking. 
* Then we would need to do, basically an emergency release of all the clients, to vote on the gas limit again, and I don't think that's good. So in my in my opinion, we should do bigger steps and and yeah. Have time to evaluate the impact of these steps. 

**Giulio**
* Yeah. I mean, the gradual increase is just better because you don't need to coordinate, right. Like what you're saying is we do it in steps, but then then you need everyone to upgrade. And it's hard to measure it's objective. Just start to measure right. Doing in little steps also takes time. It takes iteration time. It's inefficient from a management point of view. And also that's and also like and also the 60 million is kind of researched like it's not like as I said before, it is kind of research. Not like I just took it out of my head. I discussed it for like an entire week with with Netermind. So it's not like something I, we just came up with in our sleep, right? There are actual numbers behind it. And and and also 60 million is just over two years is just really small. Like it's just kind of just to start something. Right. And it's easy change. But anyway. Yeah. Anyway. 

**Tim**
* Okay, let's do Guillaume and then, ideally wrap up like again, I think there's, clearly different opinions on this. This is not something we also need like, full consensus on. we, while it would be good to have, like, rough alignment, we can have different teams. we can have different teams, like, test different things on their clients. yeah. Guillaume. 

**Guillaume**
* Yeah. So it's just a remark on the Oracle document, and it's entirely my fault that this got published with this mistake. like Gulio, you asked me, does the proof size increase logarithmically? Which is what your document says. And, the proof does increase logarithmically, but the witness increases linearly. So I think we should actually do some more, you know, dimensioning or whatever. Checking that's doubling the gas doesn't make the witness larger. yeah. I'm sorry for the miscommunication. 

**Tim**
* Okay. anything else that hasn't been, brought up yet? Okay. I think we can continue this conversation. I think,yeah. And again, like, while it would be ideal to get some consensus on this, it's also not something that like requires a hard fork or that core devs effectively control at the end of the day. yeah. okay. Last thing we had on the agenda for today is again from Felix. So adding official revert, error codes, for all of the APIs in, I believe the engine API. Felix. No, it's. 

**Felix**
* A different. 

**Tim**
* So I put up the PR in the chat. Yeah. Do you want to give some context? 

**Felix**
* Yeah. So this came up pretty suddenly. So we have received, this issue multiple times over the years that people have complained that, there is no standard way to get access to the revert data when accessing contracts using the ETH call. ETH estimate gas or ETH bid access list operation. And so, yeah, we would like to, basically introduce our way, the way we've been handling it in Geth as sort of like the official one. So and in Geth we have this like error code three that we use for this purpose. And yeah, I mean, it's I don't know, for us, it's the most important thing just to have a defined error code and just basically ensure that all the clients behave the same way.
* Because right now, in a lot of the client libraries for RPC, you have this, these huge kind of function, with different like matching different behaviors of the APIs, matching on error messages and so on, just to figure out if it's this error and then somehow trying to extract this, this data from the, from the error in some way.
* So yeah, I don't know. I mean, I'm also open to having a different solution, but I mean, for us, it's the easiest to propose the one that we use already. And, yeah, I'm just open to hear, like, what other people think. 

**Ameziane**
* Yeah. I think from Besu's side it makes total sense because this is something I wanted to do recently, basically comparing the results, the outputs from, Geth and Besu on, on each call. And I had this issue because we have, different returns or codes and basically payload. and yeah, it was very hard actually to do the comparison. So, yeah, I am totally in favor of it. Just, I was wondering why we would not have a code that is similar to what we have currently in the engine API. Something you know around -32,000. Currently in Besu we return -32,000, which is basically a server error when we when we have when we have this kind of error. 

**Felix**
* Yeah. So I can answer this. it's a, I think it's kind of a common misunderstanding that JSON RPC error codes must be negative. So basically there is absolutely no need for the error codes to be negative. It's just that the JSON RPC specification, if predefined certain errors and these predefined errors are not taken to like they don't have to be used for everything. But for some reason in Ethereum we have always only used the errors which are predefined by the JSON RPC specification. But in fact they made these negative so that you have the full positive error code range available to to your application, which Ethereum is like. Ethereum is an application of json-rpc, so we have all the positive numbers available for our use. So it's just that we for some reason, only use the error codes that are in that spec, and the error codes that are in the Json-rpc spec are only most of them are for internal use by, the Json-rpc subsystem itself.
* So basically, the most error codes that are defined by the Json-rpc spec are just used to notify the client that their request is malformed in some basic way or something. And then the server error that we used for more things is just it's like the generic error code, like the generic server error in HTTP, you know, like can use it, but it's not descriptive of the actual error. 

**Tim**
* Any other comments on the proposal? Okay. Maybe. Yeah, we can have another couple teams have a look. And if there's no objections, we can move forward with it. But, yeah, we can probably continue this async. Okay. Yeah. Thanks, Felix. last thing I had on the agenda. So on last week's ACDC, we agreed to cancel the All core dev call, during Devcon. I would suggest probably canceling the one after as well as a lot of people tend to travel back or take time after the weekend. We'll have a whole week of people being together. any objections to canceling the call on the 21st, or any strong preference to instead cancel the one like before? Devcon. but right after feels like it's probably the right timing. Okay. No objections. So we'll have ACDE number 200 right before Devcon.. Oh, actually, Barnabas, as opposed to, anyone else in Barnabas? 

**Marius**
* We need to ship.

**Tim**
* Exactly. So I'm keeping the call before Devcon, so we ship before, and then we ship at Devcon. I think it's the right call. and we get the 200 before Devcon. yes. So we have the call on November 7th. Yeah. Of course. so we have ACDC on November 7th. ACDC? Sorry. Yeah, ACDC on November 7th. AcDc on November 14th or no Sorry on November 7th, no. AcDc on 14th, no. AcDc on 21st and then back on the 28th. Yeah. And Marius will be here at 14 UTC. Okay. Marius and Barnabas. Does everyone want to call on the 21st? We can keep the 21st if people feel strongly about that. Okay. Bunch of people want to keep the 21st. my proposal then is we should probably merge the testing call. So we usually have the Monday testing call. that would be on, like, the 20, or.
* Sorry, on the 18th. so keep that together. and have, like, maybe an informal call for whoever's there on the 21st.
* First, but cancel fully the 14th. Um. Okay. And Barnabas might also do the testing call. Great. Anything else people want to discuss before we wrap up?
* Okay. Then I think we can leave it at that. Thanks, everyone. I'll post a summary shortly on the discord, and talk to you all soon. 
* Thanks, everyone. Bye.


-------------------------------------
### Attendees
* Tim
* Pooja Ranjan
* Mikhail Kalinin
* Marius
* Wesley
* Barnabas
* Saulius
* Danno
* Lightclient
* Pari
* Ethan
* Mario
* Tomasz
* Oleg 
* Kasey
* Marek
* Crypdough
* Fabio Di
* Terence
* Andrew
* Roman
* Marcin 
* Pop
* Guilaume
* Protolambda
* Carlbeek
* Mike
* Gajinder
* Stefan
* Hsiao-Wei
* Josh
* Phil Ngo
* Alexey
* Holger Drewes
* Dankrad
* Guillaume
* Proto
* Holder Drewes
* Peter Szilagyi
* Sean
* Micah Zoltu
* Jiri Peinlich
* Marius Van Der Wijden
* Potuz
* Evan Van Ness
* Moody
* Tynes
* Alex Beregszaszi
* Marek Moraczyński
* Justin Florentine
* Ben Edgington
* Lion Dapplion
* Mrabino1
* Barnabas Busa
* Łukasz Rozmej
* Péter Szilágyi
* Danno Ferrin
* Andrew Ashikhmin
* Hdrewes
* Crypdough.eth
* Ameziane Hamlat
* Liam Horne
* Georgios Konstantopoulos
* Mehdi Aouadi
* Bob Summerwill
* Jesse Pollak
* Stefan Bratanov
* Sara Reynolds
* Caspar Schwarz-Schilling
* Ahmad Bitar
* Marcin Sobczak
* Kasey Kirkham
* Sean Anderson
* Saulius Grigaitis
* Ruben
* George Kadianakis
* Dankrad Feist
* Andrei Maiboroda
* Gcolvin
* Ansgar Dietrichs
* Jared Wasinger
* Diego López León
* Daniel Celeda
* Trent
* Mario Vega
* Kamil Chodoła
* Ziogaschr
* Kevaundray
* Antonio Sanso
* Oleg Jakushkin
* Leo
* Nishant Das

-------------------------------------
### Zoom Chat


**Marius:**  
The second century of Ethereum starting soon.

**Tim Beiko:**  
[GitHub Issue 1177](https://github.com/ethereum/pm/issues/1177)  
ACD 2.0

**Gajinder:**  
We (ethereumjs) looking into the issue.

**Saulius:**  
Grandine solved some issues and should solve the rest soon.

**Marek:**  
I think we had benchmarks from three clients: Nethermind, Besu, Geth.

**Justin Traglia:**  
On similar hardware, right?

**Marek:**  
Yes.

**Marc:**  
From Nethermind benchmarks, g2msm seems fine, but g1msm is underpriced.

**Tim Beiko:**  
[GitHub PR EIP 8989](https://github.com/ethereum/EIPs/pull/8989)

**Kev:**  
This is without the 2x?

**Marc:**  
Yes, also depends on if we use concurrency.

**Kev:**  
I think this tracks with Gary Schulte's comment that G2 seems fine, but G1 can be 2x’d/changed for gnark.

**Tim Beiko:**  
Engine API counterpart: [PR 599](https://github.com/ethereum/execution-apis/pull/599)

**Onbjerg:**  
We agree (reth).

**Gajinder:**  
Ethereumjs ok.

**Enrico Del Fante:**  
Yes, Lucas is in favor of it.

**Stokes:**  
I can +1 fwiw.

**Barnabas:**  
Already done :D

**Tim Beiko:**  
[GitHub PR EIP 8969](https://github.com/ethereum/EIPs/pull/8969)

**Jochem-Brouwer:**  
I don't think codehash change is possible since selfdestruct in the same transaction only happens after the transaction. If you do it after, selfdestruct won’t clean up code/storage, just sends balance.

**Ansgar Dietrichs:**  
I personally think it could make sense to have EOF-like behavior.

**Yoav:**  
The point isn’t the codehash itself but that a seemingly immutable contract is actually mutable. Ideally, we should be able to identify a contract as mutable.

**Ansgar Dietrichs:**  
It would help with old contracts that have whitelisted code hashes.

**Barnabas:**  
Should’ve been `0xE0F`—missed opportunity!

**Ansgar Dietrichs:**  
If we make the change, I’d strongly go for the minimal code introspection variant of always returning `keccak(0xEF01)` for accounts with active 7702 delegation.

**Nicolas Consigny:**  
7702 is now the second biggest thread ever on Ethereum magicians. 1559 is first, but 7702 is catching up fast.

**Draganrakita:**  
There’s an EOF proposal for `HASCODE(address)` that would return the type of bytecode an account has.

**Danno Ferrin:**  
It’s an EOF-only opcode as currently `EXTCODE*` isn’t in EOF validated contracts.

**Tim Beiko:**  
[GitHub Issue Comment](https://github.com/ethereum/pm/issues/1177#issuecomment-2405703791)  
[EIP 7790](https://eips.ethereum.org/EIPS/eip-7790)

**Marius:**  
I don't like 7790.

**Toni Wahrstätter:**  
We shouldn’t increase the gas limit before 7623 (increase calldata) or do 7623 at the same time.

**Tim Beiko:**  
Would you prefer a shorter window here? Like, +Xm gas over N months?

**Justin Florentine:**  
I’d need to see network testing—it’s a WAG right now.

**Barnabas:**  
Wouldn’t it make sense to do it at a hardfork given we have a hardfork coming anyway?

**Tim Beiko:**  
My preference is less of an increase and shorter timeline.

**Tomasz Stańczak:**  
It’s a signal to validators, and coupling it with a HF is a stronger signal.

**Stokes:**  
Sure, but we have no idea how this maps to hardware on mainnet today.

**Trent:**  
No considerations for history growth?

**Toni Wahrstätter:**  
This mechanism would slowly increase the limit, making it hard to determine impact after shipping. A prompt increase is better.

**Ansgar Dietrichs:**  
Without 7623, going from 30M to 60M would worsen the worst-case block size from 2MB to 4MB. That seems problematic.

**Ben Adams:**  
Do you not think 7623 will ship in 2 years?

**Stokes:**  
Rather than take the execution risk, we should agree to 7623 and a gas limit raise.

**Justin Florentine:**  
Didn’t we already say we haven’t network tested it?

**Tomasz Stańczak:**  
DeFi has intents; Core Devs have intuition.

**Stokes:**  
We can do better than intuition for a protocol as valuable as Ethereum.

**Tomasz Stańczak:**  
I hope the data and research people will add to the numbers.

**Łukasz Rozmej:**  
We need gas limit social consensus; we don’t want gas limit wars.

**Marius:**  
60M means around 3.5MB blocks, right?

**Tomasz Stańczak:**  
Nethermind shows safety for a while, and some repricings could be suggested over time.

**Kamil Chodoła:**  
We could do a step every X blocks, translating to a range like a 3-5M increase every 3 months, allowing time to stop if needed.

**Justin Florentine:**  
This is close to upload limits for users with poor internet.

**Barnabas:**  
Max gas increase shouldn’t happen together with max blob increase—it would hit home stakers twice. If we increase blobs on Pectra, wait a few months before considering gas.

**Toni Wahrstätter:**  
The upload bandwidth requirements are creeping up from both of these adjustments.

**Marius:**  
Compressed, it can go up to 2.7 MiB max.

**Marek:**  
Through the engine API, for bigger blocks, 7623 is a must.

**Jochem-Brouwer:**  
EthJS supports—this should’ve been introduced earlier.

**Barnabas:**  
Cancel 14, keep 21.

**Lightclient:**  
Keep 21.

**Barnabas:**  
18th testing call will happen on flight wifi.

**Pooja Ranjan:**  
Reacted to “18th testing call will happen on flight wifi” with 🔥
