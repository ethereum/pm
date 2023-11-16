# Execution Layer Meeting 174 [2023-11-09]

### Meeting Date/Time: Nov 9, 2023, 14:00-15:30 UTC
### Meeting Duration: 40 Mins
### Moderator: Tim Beiko
### [GitHub Agenda](https://github.com/ethereum/pm/issues/895)

### [Audio Video of the Meeting](https://www.youtube.com/watch?v=TQ2XEvMzvFg) 


### SUMMARY




| Item | Descritption |
| ---------------- | ------------ |
|   1          |       **Goerli Shadow Fork** went well, but was on a relatively small number of nodes. Next steps are to get a devnet running with the last spec changes, and after that we'll do a larger Goerli Shadow Fork, and then start doing mainnet ones to have at least one smaller and one larger one done before actually forking mainet.       |
|       2.     |We agreed to add the **Single RPC method for blob gas price** (eth_blobGasPrice) and to add the blob pricing info to eth_feeHistory as described here https://github.com/ethereum/execution-apis/pull/486|
|3. |   Conversations about **EIP-7545 and precompiles** in general, no action taken for now.|
| 4.  | We agreed to **keep both next week's ACDC and ACDE** the week after, but cancel the testing call next Monday. For teams who aren't able to send anyone to the call, please post an async update on the call agenda prior to it |




## Dencun Updates
  
**Tim Beiko** [02:23](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=143s): Welcome everyone to ACDE number #174. So we'll cover Dencun today. Some updates on the Goerli Fork, Client updates. There's also some RPC discussion that people wanted to bring up. And then aside from that Guillaume has a Verkle EIP to discuss. And then given its Devconnect next week and US Thanksgiving after that. It makes sense to figure out which calls we want to have in the next couple weeks and whether we want to cancel. So any of them? I guess, to start on the Goerli Shadow Fork. Pari, I believe you shared this analysis. Do you want to give us a quick walk through how things went? 

## Goerli Shadow Fork

**Paritosh** [3:18](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=198s): Yeah, so we had a Goerli Shadow fork earlier this week. We basically synced up all the nodes to Goerli heads. Then started a new Beacon chain and forked off a small section of the nodes. So roughly 21 nodes. And afterwards we set the Dencun Forks. So we had we enabled Dencun on Goerli. Since then we've been running Xatu to collect all the metrics so blob arrival times Etc. And the analysis is shared there. I think there's nothing insane that pops out there's a couple of like regular spikes. We're still not 100% sure why? But besides that block processing times. And gossip times look really low but that's also kind of expected considering it's a really small Network. The main takeaway or the thing that we're yet to properly analyze is the amount of time it takes to build payloads Etc doesn't look very high. So we're still getting organic transaction gossip from Goerli. So the question is just is there anything else we should be trying on this network before we delete it? 


**Tim Beiko** [4:32](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=272s): Thanks anyone have anything they would like to see on the Shadow Fork. 


**Danny** [4:37](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=277s): Yeah I mean my intuition is given, we're doing the CL networking rework. And given that so far things look stable and you know it's a good test that we probably have what we need. And we're probably going to want to run another one and potentially after we run another one another one at scale but after we have the rework on the consensus layer.

**Tim Beiko** [5:00](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=300s): Right this is basically our Baseline before that change comes in.

**Danny** [5:05](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=305s): Yeah so I mean as a baseline it sounds like it worked. I don't personally see.  More stuff to do right now.


**Tim Beiko** [5:11](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=311s): So I guess for the next ones. Do we see value in having it and on Goerli again? Would we want to go straight to mainnet for the next Shadow Fork? Yeah the teams have an opinion about that for devops.

**Paritosh** [5:36](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=336s): I think mainly we prefer continuing Goerli Shadow Fork because it's relatively most of the upgrade changes we're going to notice up here peer to peer Layer and renting more nodes that can support the goerli network is cheaper than renting more nodes for mainnet. We're definitely going to do a mainnet Shadow Fork before we do the official main net for but the question is just do we do that earlier or later.

**Tim Beiko** [6:01](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=361s): Okay in that case I think yeah it probably makes sense to do goerli again as the first one. And if there's no issues then move to mainnet.


**Danny** [6:12](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=372s): And yeah I'd be an advocate for that doing a large Goerli after doing a small Goerli then doing a small mainnet, doing a large mainnet but again after we're pass another couple of Devnets with the fix or at least one.


**Tim Beiko** [6:28](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=388): Yeah I agree. I would do at least one devet with the final spec changes before we do another Shadow Fork. Does anyone see the need to do another Shadow Fork before that.

**Danny** [7:03](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=423s): Yeah I should just barring unless devops is just trying to strength and devops tooling. I wouldn't continue to do them now. 


**Paritosh** [7:14](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=434s): They used to testing in proud we’re fine.

**Tim Beiko** [7:20](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=440s): Nice. Okay anything else on the shadow fork? 

## Add eth_gasPrices; add blobs to eth_feeHistory execution-apis#486

Okay if not so the second thing on the agenda, so there was a PR to add the Blob gas price to eth_feeHistory. And then in the comments there was a proposal to also have a single RPC method that returns all of the gas price related values but maybe. Alexey, do you want to start walking us through your PR and then we can discuss the alternative proposal that was posted in it. 

## Proposal: RPC method to retrieve all of eth_getBlock, eth_gasPrice, eth_maxPriorityFeePerGas, and eth_blobGasPrice

**Alexey** [8:03](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=483s): Yeah, let me try to present. So let's try to start from a very brief description. What is blob gas and why do we need API for it? So blob gas is like I guess in  addition to regular one, which is used for blobs and is relevant for blob transactions now. And to understand how much, what price maximum price for blob gas is needed to, we mentioned in the transaction. We need to provide some kind of estimation. To include this data after all in to block transaction. Specifically the fill from Blob gas. To do this we can query it through a new endpoint. There are two variations initially is gasPrices was provided and form of this point it's a pretty simple method that returns several various regular gas which can be used like a regular gas cap or the transaction blobGas and maxPriority which can be set as a tip for transaction which started working from EIP #1559 and a simpler version of it. If we just return blobGasPrice and it can be used when posting when sending blob transactions. I have no strong preference. I thought that the first approach could be more optimal, because we return this data based on the same structures like Blobs and it could be one method because usually all these values are queried together. But after all we can do just a batched call which can be done quite simply. And my work too another update is for history in addition to regular gas ratio and baseFee per such kind of gas. We could add the same for blob gas. And other fields do not need any change because they like report are about prosthetic. That's an update would like to propose and happy to hear feedback. 


**Tim Beiko** [12:36](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=756s): So thank you. Does anyone have thoughts preferences on the various options.

**Alexey** [12:52](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=772s): I would post the link with the examples and description.


**Tim Beiko** [13:11](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=791s): Okay so there's a question about whether this already exists in GraphQL. Does anyone
Know?

**Devconnect** [13:26](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=806s): Pretty unlikely it does not. 


**Tim Beiko** [13:28](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=808s): Okay.

**Devconnect** [13:33](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=813s): I mean I shared some thoughts on the PR but I generally would prefer to have eth_blobgasPrice because that sort of follows the pattern that we currently have. And unless there's like a strong reason to do the gasPrices. So I was hoping someone might make an argument for that but as it is, we don't really need to return gasPrice. As far as I know because that's kind of a legacy value we really just need the max_Priority fee and the base fee. And now the Blob gas price. So I would prefer to have it as a separate method and just expect people to batch the RPC request.


**Tim Beiko** [14:26](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=866s): Got it and I know, so there were some comments on the agenda in the Discord now for having a single call. Does anyone want to make the case for why batching them in a or why combining them in a single call is better? If not it feels like we should at the very least add blob gas price that seems kind of like a no-brainer. It also seems like a no-brainer to update eth_fee history that also include the data there. How do people feel about merging those two and then if the bundled method maybe doesn't have to be part of the spec. But if clients want to offer it they obviously can just add extra RPC’s. But that at least on the JSON RPC spec we'd have a single method for ETH blob gas price. We'd have the blob values as part of fee history. And then the rest is sort of an optional thing clients can do.  Oh and there's an argument that clients should not do stuff that's not in the specs which unfortunately we can't control what clients do. But I guess, does anyone disagree with merging the single blob gas price method and the changes to fee history. And not having the combined one and worst case we can also always do the combine one later if there's enough demand for it.


**Devconnect** [16:18](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=978s): I'm not sure if there is any L2 people or someone who is working with ethers who wanted to chime in since they're the people who are using I guess not. We can try and follow up with those folks, but yeah we'll move with the one method and update in Fee history.

**Tim Beiko** [16:54](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1014s): Okay, anything else on that? Okay if not anything else on Dencun at all that wasn't included on the agenda. 

Okay then next up, Guillaume, you wanted to discuss Verkle proof verification precompile?


## Add EIP: Verkle proof verification precompile EIPs#7926
 

**Guillaume** [17:27](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1047s): Yep. So I mean it's more like, I was trying to bring people's attention to it. So it comes froum a conversation I had with some people from openZeppelin at first and then other people afterwards. Let me see if I can share my screen. Yeah should Work. So it's really about collecting input. The idea is simple. It's because verkle entails a lot of complex math updating a lot of tools. The idea that came up would be to use a pro verification pre compiles. So offer a pre-compile. So for example Bridges or I forgot the word for L2s but L2 Bridges let's call them or even application developer could verify verkle proofs. So that they don't have to wait for all the libraries like opens Zeppelin like Foundry to get up to speed and like get up to speed and Implement that in in solidity so it's just about adding a simple pre-compile So currently I suggested 0x21 uas an address. But yeah of course that can be changed. And the idea is that it receives a chunk of memory that starts with a version bite. And then where where the proof data can be found. Sorry, actually so it first receives a version bite and then a location memory where the proof data can be found along with its size. And also the state root of the tree that the proof is proven against and what the pre-compiled does. So it's upgradeable if we want to move on to different proof system. But if version is zero we use the the standard polynomial commitment scheme, suggested like polynomial commitment scheme based multi proof that was suggested by Dankrad. And otherwise we return one if the proof verifies and zero otherwise and there's also like the EIP also describe gas costs. So I think the model is not really complete. For example, I realize it's missing some data to actually verifying the IP’s approve but that will be updated. But the general idea is you have this constant Point cost that corresponds to every time you need decentralised  commitment. So it's paid for each commitment to get that gas decentralised and then you need to evaluate the Polynomial at some opening point. So you also pay that for each opening you have to do. Yeah there's not much more to that. I mean clearly it's something that needs a lot more input. So that's why I want to bring your attention to it. Of course if there are questions I'm happy to answer but it's more like a call for Code pseudo to pay attention to that. 


**Tim Beiko** [21:00](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1260s): There's a hand up by Devconnect Berlin.

**Devconnect Berlin** [21:06](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1266s): Yeah! Hello, this curve is over bandersnatch or sorry like this approving scheme would be over bandersnatch the curve?

**Guillaume** [21:14](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1274s): Benderwagon.

**Devconnect Berlin** [21:16](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1276s):
Benderwagon. Okay so I guess my question is how it relates to the BLS12 curve and if there's any interplay between those set of precompiles and this 
One.

**Guillaume** [21:27](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1287s): How does it relate, I mean I forgot which of the two Fields is the one from BLS but otherwise it's my understanding is that it's a completely different curve. I'm not an easy elliptic curve expert but my understanding is that they are different. And so you could potentially, I guess use that precompile that BLS pre-compile but you would have to reimplement all the proving yourself all the commitment. Sorry, the multi proof proving yourself. So, that means that every application developer would have to reimplement that and the goal of this contract is to save some time.


**Devconnect** [22:18](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1338s): Right. So we just have pre- compiles for both then because that's something I'd like to do for the next hard Fork is the BLS12 -381 curve. But, it sounds like they're almost similar but not quite exact. 


**Guillaume** [22:33](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1353s):  So they are completely different curve?


**Dankrad Feist** [22:35](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1355s): Yeah so no this the BLS precompile cannot verify the verkle proofs. We could add a bandersnatch precompile. I think that would actually also make sense probably. I think my preference is actually to have a state verification pre- compile. And the reason is that when we change the state in the future we could make it Backward Compatible. So that smart contracts can be built that verify a part of the state. And you can just upgrade the state commitment and the smart contract could be completely the same. And would so it could be an immutable smart contract. And I think that would be preferable rather than having to have lots of smart contracts upgrade. If we do need to change the state commitment in the future again. 



**Tim Beiko** [23:50](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1430s): Got it. Danno you had your hand up yeah.


**Danno Ferrin** [23:54](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1434s): Yeah. This might be a controversial take on this but I think one of the great things about #4788 as a pre-compile is that, there is EVM code that says this is the pre-compile. This is the canonical answer. So this kind of goes against some of the idea that you know why wait for open Zeppelin to implement this in solidity. What if all pre-compile is going forward that the canonical form is a
form of solidity or Viper or fee or whatever. And that defines it in modulo gas. You know we're going to have to change a gas schedule on that. And that the clients could do a pre-compile that would optimize that but would truly be a pre-compile at that point there would be an uncompiled version that is the Canonical this is a reference implementation. This is the correct state. It would solve a lot of problems in devs who aren't you know PHD’s in cryptography trying to. Get the small little details of these curves correct when they don't necessarily have a large set of test cases to run against.


**Tim Beiko** [24:58](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1498s): And so the implication here is you can Implement any of them in solidity basically.


**Danno Ferrin** [25:06](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1506s): Right and early on when you don't have when you're work doing the next hard work the client you just slide that precompile slide. The EVM in and then when you optimize it you come check if you got some local code it'll always be correct.

**Dankrad Feist** [25:19](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1519s): So this curve specifically will be used for verkle trees anyway, right. So all clients will need I mean we have already created libraries for that. So I mean I think like currently the general position is that client tests never touch the cryptography themselves. Well unless they are really comfortable with it. And that we have readymade libraries and that's already the case for verkle in this case. 

**Danno Ferrin** [25:47](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1547s): So yeah verkle does kind of change this argument a bit since it's gonna have to be part of the client. But I think it's just an idea I want to put out there for like cryptography not necessary. I was commenting on this. but

**Dankrad Feist** [25:55](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1555s): The idea is good particular EIP.


**Tim Beiko** [26:01](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1561s): This is a bit off topic but could we do that for BLS or because I remember like the whole debates around EVM Max were to allow us to build BLS on a one but.


**Danno Ferrin** [26:15](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1575s): I know the Epsilon team at one hackathon did through EVM Max the existing precompilers. I don't know if they moved on to BLS12 and using EVM Max. Right.

**Tim Beiko** [26:28](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1588s): Got it. Okay and I assume I guess back to just the original EIP. I assume there's an ETH magicians link people can raise issues there but were there any other questions about the EIP.


**Devconnect** [26:52](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1612s): Are there specific implementations you can point to of this like the multi proof PCS.


**Guillaume** [26:59](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1619s): The multi proof PCS itself. Yes they are there's, I mean one of them is go verkle the other one is there's a python implementation reference implementation in fact by dankrad. And there's a rust one I think. Oh yeah there might be a nethermind one to a C sharp one by nethermind. But yeah there's no there's no implementation of a pre-compile itself. But it's going to be easy to couple together if that's what you need.


**Devconnect** [27:30](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1650s): Yeah just curious maybe toss links to those repos and the ETH magician stand.

**Guillaume** [27:37](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1657s): Sure.


**Tim Beiko** [27:41](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1661s): Cool. Anything else on the precompile. Okay, there's a comment around saying they've started implementing BLS at EVMMax and after Devconnect we'll know if it's possible. Anything else people wanted to chat about. I had the call scheduled but there's anything more substantive we can get to that first. If not, next week there's Devconnect. 

## ACDC during Devconnect, US Thanksgiving

So next week we should have had a testing call on Monday and ACDC on Thursday. The people want to keep either of those. Yeah does anyone feel like there's value in having them or should we wait until either the week after just as it heads up that'll be American Thanksgiving on the Thursday.

**Danny** [28:54](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1734s): I was thinking if we don't do the consensus layer call. I might ping on that Thursday the Discord and just ask for like a quick written update from the consensus layer teams on getting through the networking changes. And surface any issues that maybe have arise or unknowns at that point and we could do a similar thing the week after on like Wednesday if we don't do the Thanksgiving call US Thanksgiving call. 


**Tim Beiko** [29:20](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1760s): We could also have the call on a Wednesday you know if we want to have one the week after and not skip two weeks in a row. 


**Danny** [29:28](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1768s): Well and I guess one of the main things that will come up in that time period is if there are open issues or questions related to this update. So I'm also okay like doing the Ping a couple times and then scheduling an ad hot call if we need it.

**Tim Beiko** [29:49](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1789s): Okay that works for me does anyone have oh Ben?


**Ben Edington** [29:56](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1796s): Yeah just interested in signalling. So just delving back into into history when we were planning the capella and the dencun upgrades. We committed, we broke the on pass about delivering both together by committing to doing #4844 as a fast follow on to capella with withrawal. We're talking about June /July time which is amusing in ambitious in Retrospect. But I'm concerned about the Optics you know these week here and week there add up to delay over time. We've seen it time and time again. And I know everyone is working super hard on delivering deneb cancun but because I'm inside the process but from outside the process you know cancelling two core Dev calls in a row doesn't the Optics. Don't look great to me and I'm starting to see things hotting up again on the need to deliver this thing. So that would be my case for keeping the Calls. Obviously there's no point if nobody's going to be here but I think generally that should be our default approach.

**Tim Beiko** [31:12](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1872s): Yeah I'm also, I have less of a strong opinion on the devconnect one just because there will be a lot of people there even though there may be a bit less than expected. I do like the idea of having your written update though from client teams. So that we can still get a status update and I'm happy to keep. I'm not American. So I'm happy to do the one on US Thanksgiving, the week after that. And or to move it to or to move it to like Wednesday if that means more people show up. So either of those is fine for me. Yeah and maybe I don't know maybe we can get teams to chime in on the Discord. If they have a preference but yeah I agree like skipping two might not be ideal. So we can maybe do next week's async get an update from teams and then figure out the best day for the week after that. Do people think that make sense? Okay I'll post something in the Discord get some more feedback from client teams. Oh now there's more and more support for having the calls. Okay I'm fine either way. I don't know Danny, do you want to do a quick call next week?  


**Danny** [32:53](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1973s): I don't mind, I'm comfortable either way. I might not live stream it given my remote capabilities and setup. I might even take the call from a phone but. 

**Tim Beiko** [33:12](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=1992s): I think we can probably find someone to live stream it. Yeah Okay then let's keep both calls I guess. Okay let's default to this let's keep both calls. If people if like a whole team cannot make a call and share a written update on the agenda and we can kind of point it out at least on the call but there will be a call. And we'll try our best to live stream it but worst case we'll just upload the zoom recording later. And yeah if you're team can't make it just share an update.

**Danno** [33:50](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=2030s): When I toss up the agenda I'll make a comment too. If you can attend to share it, update in the agenda. 



**Tim Beiko** [34:01](https://www.youtube.com/watch?v=TQ2XEvMzvFg&t=2041s): Sweet anything else? Oh and I guess maybe the only one I just wanted to check do we want the testing call Monday as well or do we I especially given these All core Devss have become shorter. I would lean towards cancelling next Monday's testing call though and just having ACDC next Thursday ACDE the Thursday after that and then whichever next I think the next testing call was scheduled for the Monday after that one. So November 27th but I think having just one syn call next week is probably sufficient. Does anyone think we should have the testing call as well on Monday? 

Okay cool. So let's do that, we'll add a note in the agenda and we'll share something in the Discord. Thank you Ben for pushing us to stay on track anything else anyone wanted to discuss. Okay well thanks everyone I will see you all at or most of you at devconnect next week. And then we'll see everyone on ACDC whether you're at devconnect or not next Thursday talk to you all soon. Thanks bye.

# Attendees

* Tim Beiko
* Guillaume
* FLCL
* Ben Edgington
* Paritosh
* Danno Ferrin
* Echo
* Devconnect Berlin
* Justin Traglia
* Pooja Ranjan
* Daniel Lehmer
* Gajinder
* Damian
* Piotr
* Matt Nelson
* Fabio Di Fabio
* Enrico Del Fante
* Hsiao-Wei Wang
* Stefan Bratanov
* Ayman
* Tukasz Rozmej
* Tomasz Stariczak
* Danny
* Dankrad Feist
* Roberto B
* Mehdi Aouadi
* Marcin Sobczak
* Mario Vega
* Denis Kolodin
* Ameziane Hamlat
* Andrew Ashikhmin
* Gabriel Fukushima
* Trent
* Spencer -tb

### Next meeting [ 23rd November, 14:00-15:30 UTC]


