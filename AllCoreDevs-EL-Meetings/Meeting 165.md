# Execution Layer Meeting 165 <!-- omit in toc --> 

### Meeting Date/Time: July 6, 2023 at 14:00 UTC <!-- omit in toc --> 

### Meeting Duration: 60 Mins <!-- omit in toc --> 

### [GitHub Agenda](https://github.com/ethereum/pm/issues/815) <!-- omit in toc --> 

### [Video of the Meeting](https://www.youtube.com/watch?v=Voavkk8Es5E) <!-- omit in toc --> 

#### Moderator: Danny Ryan <!-- omit in toc --> 

#### Notes : Avishek Kumar <!-- omit in toc --> 

—------------------------------------------------------------------------

## [SSZ Impact Analysis](https://docs.google.com/document/d/1p-1VvOGwI5GHkwaGMzJYDL7Affofm6rVLa6cvnmoqGI/edit)


**Danny** [1:19](https://www.youtube.com/watch?v=Voavkk8Es5E&t=79s): Hey Everyone! This is All Core Devs Execution Layer Meeting 165. This is issue 815. We can keep moving anyway this is issue 815 on the PM repo and I am subbing in for Tim Beiko, today. All right, it looks like we have somebody from Dedaub? Okay so the first thing up is we do have an SSZ impact analysis uh that was done by dedaub if you all want to take it away. You can screen share.


**Neville Grech** [2:17](https://www.youtube.com/watch?v=Voavkk8Es5E&t=137s):  Sure thanks Danny, let me just share my screen. All right, thank you for hosting this meeting and inviting me here. So over the past three weeks we've conducted another study that has to do with the migration of the RLP format to SSZ of some MPT commitments which are stored in the receipts and transaction route respectively. So this is obviously your work with some of my colleagues. One of them is at this meeting as well. Yeah so what was the original scope of the study so the issue with you know making changes to execution layer data structures in the block header is that so there's some protocols that might actually be using these and Performing proofs on top of these. So these two EIPs so that's 6466 and 6404 are you know migrating the encoding from this from RLP to SSZ. Now what is the impact of such a change on these protocols? We've tried two different approaches for completeness. So in one approach we've analysed all smart contracts deployed on Ethereum. So we have a data set for that on the contract Library. So the static analysis and the other approach employed Dynamic analysis. So we actually looked at the transaction behaviour and tried to determine whether there were smart contracts that are actually doing, you know, verifying proofs over these data structures. So we already had an idea that perhaps you know the centralised Bridges might be doing this sort of thing. But you know over our you know over like a couple of years ago we also saw like you know historical blockchain events oracles and other weird stuff that cannot be discounted. So we found you know and examined these projects and tried to determine what is the provenance of this RLP encoded data. Is it coming from Layer2? Is it coming from layer 1 itself ? Now note that you know in this meeting we're deciding whether to you know make changes to layer 1 but not Layer 2. So if you know layer 2 changes then it shouldn't affect I mean it shouldn't affect you know decisions that are being made on layer 1. Yeah and then of course there's you know other things like for instance is some of the data being relayed via centralised Keepers and things like that so you know if there's some element of centralization through which some of these data is being passed through then perhaps even if you know the changes are being made you know the centralised systems can be upgraded.  Okay and of course all of this study has been done on you know recently used or high balance or part of non-protocol contracts. Now if we determine that the protocol was affected we explore upgradeability options. Okay so to get into a bit more detail about the effect of the changes so here's the ethereum block header here's some of the fields. There's three routes there. There's a state route which is a root Hash a global State also coded using a Mercury transactions routes and receipts root. Again these are roots of Miracle trees containing transactions and receipts respectively. So 6466 is changing the encoding of the transactions from RLP to SSZ and in case of the receipts as well so this will obviously make a a big difference to the to the hashes that are going to be calculated so if there was some smart contract which is actually re-verifying these than those will will actually be broken. So throughout these three weeks we've determined that actually there are three protocols that will be affected by this so one of them is layerZero and in this case layerZero is also being used by zkBridge in some way. So you know both of these Protocols are affected. You know specifically that one of the light nodes is being used and it's going to be affected. In the case of Telepathy which is doing very complicated things that is also going to be affected. Now in all three of these protocols we've also found out that there are upgradability options and in all cases only EIP 6466. So the receipts route had an impact. Now the estimated impact is subjective but so for instance you know the subjectivity comes from the fact that you know how we can determine whether the protocol is easy to upgrade. We're not exactly sure how easy it is but you know we've seen that for instance if they're using um you know certain software engineering patterns we know that they're upgradable. And how often is the protocol used and then you know especially on the more complicated protocols there's you know alternative configurations and some configurations the protocol is affected and some it isn't? Now most importantly, before we started the study we already had an idea that perhaps you know some of these decentralised Bridges like an optimism or polygon there is a possibility of them being affected and indeed you know these Bridges were being flagged up time and time again. In our analysis because they were doing proofs of RLP encoded commitments and in actual facts these are not being affected. I mean these were out of scope because in both cases for instance polygon and optimism. The data was coming from Layer 2 and being verified on Layer 1 okay. 


**Danny** [9:59](https://www.youtube.com/watch?v=Voavkk8Es5E&t=599s): Do we know when data goes from Layer 1 into Layer 2? Are they utilising the Layer 1 commitments Or is that a blind spot?


**Neville Grech** [10:13](https://www.youtube.com/watch?v=Voavkk8Es5E&t=613s):  So what we did is we looked at the protocols that were deployed on Ethereum. But then most of these larger protocols would have similar contracts on other chains. So when we found that they were actually doing the you know verifying these kinds of proofs on Layer 1 from Layer 2 data. We also checked on the other chains whether a symmetric thing is also happening.


**Danny** [10:46](https://www.youtube.com/watch?v=Voavkk8Es5E&t=646s):  Right.


**Neville Grech** [10:47](https://www.youtube.com/watch?v=Voavkk8Es5E&t=647s):  And in this case we didn't find that that was happening but say for instance in the case of Layer0 we did find that it was happening.


**Danny** [10:54](https://www.youtube.com/watch?v=Voavkk8Es5E&t=654s): Okay, thank you.


**Neville Grech** [10:56](https://www.youtube.com/watch?v=Voavkk8Es5E&t=656s): Okay so I'll go into the two different approaches we used so we used the **static program analysis** and we were very literally trying to find just by analysing smart contract byte code just to be fully complete. Whether the byte code we're implementing you know  RLP decoders and using that say for instance in Miracle tree proofs. Now it looked a bit daunting at first but we actually did manage to mechanise an analysis for identifying these, And the main Insight from this is that all of these RLP libraries if they want to you know decode RLP correctly they need to actually contain some constants. Such as the ones that I'm selecting here because these are actually needed because you need to do comparisons or you need to subtract these constants to get for instance length fields and things like that. So what we did is we try to see whether there are patterns such as for instance you know the variable is being compared to a constant in either direction and things like that so you know in multiple different ways. And it turns out that you know this analysis yielded quite a few contracts and you know I'd say most of them were they weren't actually false positive indeed you know having you know combination of those constants being used in Expressions such as comparison expressions and then using that to you know decide which part of the loop to execute and things like that. It was basically an RLP decoder. Now one other thing we did is because Ethereum bytecode is you know doesn't have variables. What we did is that the analysis was performed on a lifted version of the bytecode. So in contract Library we  have this constant data set of decoded smart contracts and sorry decompiled smart contracts and they're be compiled up to various levels and one of those levels is three address code which is very faithful to the original semantics of the bytecode but it contains variables instead of you know stack operations. And so once you have that and it is easier to know, perform comparisons. You know looking at certain patterns in the code okay and of course you know there's other things you need to do. So the compiler generates a lot of code which needs to be optimised and things like that. And you know we had analysis passes to de-optimize some of the codes. It's you know, it wasn't work which was conducted for this but it is a data set that we're constantly analysing you know for security vulnerabilities and things like that. Okay so we've also tried the second approach to find you know affected contracts and the reason why we wanted to try two different approaches is so that we can get kind of like more confidence out of the you know data sets and you know be sure that you know each approach has its own blind spot but you know we combine two approaches together uh you get better results. So via Dynamic analysis what we actually tried to find is identify contracts, specifically some functions within those contracts that received RLP encoded data as part of their call data. It's part of their arguments now. How do you do that reliably in order not to get a lot of false positives, not to because what's special about RLP encoded data? And we will see in the next slide. Assuming that the RLP encoded data is of type bytes then because of the way API Encoding works. So in API Encoding you'd have the first four bytes being the selector and then you've got chunks of 32 bytes being individual arguments. Now when you have something of type bytes apart from having a pointer to where the bytes start. Right before the actual data in that byte array starts. So I'm putting my cursor here right before you have a length you have the actual length of the you know the the array in the next 32 byte and chunk and so on. And it also happens to be the case that RLP encoded data also contains a length field and it's you now frankly encoded because you've got the first byte to give you the left.  Yeah so the first byte is actually the length of the length and then you've got the actual length here of course there's like differences here but you know if you go through you know as we did like all the call data over a million blocks and you check for heuristics like this. We ended up getting a pretty good data set of around a thousand smart contracts that were actually doing RLP, RLP decoding. Now there was also a source of false positives in this data set because there are many contracts you know such as for instance unismol flash swap or things like that that just relay the call data from one contract to another without actually interpreting it and so what we did there is we actually assessed for every smart contract for every pump public function that it implements  the number of times it actually is receiving RLP encoded data in its argument. So if it was receiving more than RLP encoded data on more than 10% of the time that it was being invoked then we put it in the data set to be inspected later. So then what we did is we combined these two data sets. And we found out that it's mostly the same contracts that were being flagged and we inspected the most popular contracts out of these out of these data sets and a lot of contracts and big protocols were flagged you know as I said before you know like like polygon and optimism a bit torrent and you know many other protocols. And then obviously there were false positives as well but I'm just saying you know like um contracts or protocols that are decoding are RLP encoded data. But most of  them we found out by painstakingly going through each one of these contracts you know one by one trying to understand the protocol. There was always some reason why this particle would be unaffected. And these are the three reasons. So one of the reasons was that the protocol didn't really do MPT proofs over this RLP encoded data even though the data was RLP encoded. You know such as the case of for instance when you have flash loan contracts or things like that which relay um call data arguments. So the second case which is the most popular case is that a contract was actually doing you know proofs but the provenance of this data was coming from Layer2  Chains or other side-chains and then when we looked at the same protocol again on other chains we didn't find asymmetric relationship there. And then finally the protocols we're doing you know proofs over MPT commitment but they were unrelated to in-scope imps the EIPs. Such as for instance you know the state route or custom data structures that were being created from centralised systems. And so you know this wouldn't be these wouldn't be affected. Yeah so the important unaffected protocols that we found so these are unaffected were Polygon Bridge, Optimism and Bittorrent Bridge. So, Bittorrent Bridge was mostly used between Torrent I believe and Ethereum and you know we didn't find a symmetric path where you know like the implementation on the opposite chain so the chain to which they were bridging to. What's doing it like similar proofs as was happening on Ethereum. Interestingly, there was another protocol called telepathy which we marked as being affected but in many cases it was being flagged up as doing RLP encoded you know proof commitment checks but these were on the storage route. But then there was part of that protocol doing that on the receipts route as well. Don't say something? Okay all right, so yeah, I mean these are the affected protocols so I'm going to give an example here on LayerZero, this did exactly here on LayerZero which is validating one of the proofs and the data is streaming from receipts routes. In the second case zkBridge was integrated into Layer Zero as an oracle. And you know in some cases we found that it was being configured with the ultra right node in Layer zero so that's also affected and in telepathy that was more complex. 


**Other Person** [22:36](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1356s): Yeah indeed and yes I was one of the collaborators that worked on this report with Neviel and indeed telepathy was a very different based on the other bridges in the sense that it actually uses consensus layer data but it turns out that they depend historical summaries field on the historical Summers buffer which contains commitments from execution layer and which of course right now are a function of a seeds root so when this changes uh they will also be affected because they assume the data in the execution layer blocks are assessing a RLP encoded so changing battery will affect the
smart contract ?


**Neville Grech** [22:33](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1413s):  So yeah and of course it was also being flagged up for things that were unrelated as well okay so in conclusion you know just just from you know what we found out we think that the impact is overall it is moderate but in all three cases we found you know upgradeability possibilities. Now I gotta stress that RLP Encoding on and then you know like reproving MPT commitments happens a lot on chain and it's actually took quite quite a bit of time to go through and filter out you know cases where this was going to be affected versus not? Most instances were indeed unaffected in all three cases that we found in layerZero for instance. The default inclusion Library can be upgraded and zkBridge you know with Layer Zero fixes this then it's going to fix zkBridge but you know they can also Implement their own proof validator which might add some technical debt and again in telepathy they can also upgrade the inclusion proof logic. So thank you. Do you have any questions and also you can find the full report I'll share with you on the chat and also this presentation as well. 


**Danny** [25:10](https://www.youtube.com/watch?v=Voavkk8Es5E&t=656s): Awesome thank you. I have a quick question: given your tools analysis and some of the kind of heavy filtering you had to do to remove what we think are false positives, what are the chances we miss something? What's the confidence level on completeness here?


**Neville Grech** [25:31](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1531s):  Yeah, so the reason why we did two different approaches is in order to maximise this now if you want to be even more rigorous than this. And theoretically you would have to go through every single chain that we know about and repeat this on all the different chains. Now the problem with that is that you know you will flag similar contracts but they will not be exactly the same perhaps and so again you have to do a lot of inspections of all of these contracts. We did a little bit of this so specifically we looked at a sample of so we ran one of the dynamic analysis which was easier to run on multiple chains. We ran this on a sample of BSC data and we run a sample on Phantom data as well. But essentially I mean what what was happening is that these  protocols were deploying uh you know similar contracts on on different chains of if you find a contract which is doing that on Ethereum you're more you're most likely going to find the same contract doing it on other chains and it's probably the case that there weren't protocols bridges that were being developed for other chains with no similar symmetric contracts on Ethereum.


**Danny** [27:09](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1629s): Got it, any  other questions?


**Lukasz Rozmej** [27:28](https://www.youtube.com/watch?v=Voavkk8Es5E&t1648s):  Yes if we're talking about other chains and coordination right because this is not a blocker for us or anything do you have the tools for this analysis available for them?


**Neville Grech** [27:42](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1662s): Yeah so part part of the tool chain is open source but you know another part is closed source so you know we can you know give you accounts for instance on one of the tools we have internally called Watchdog and some of the analysis can be repeated. Again so  on the other on the other chains we're limited but on the Ethereum Chain we're we fully support that. 


**Lukasz Rozmej** [28:09](https://www.youtube.com/watch?v=Voavkk8Es5E&t1689s): And second question so if I understand the conclusions the conclusions are there are no blockers but it needs a bit of coordination when doing this upgrade with all affected parties.


**Neville Grech** [28:23](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1703s):  Yeah I would go with these three affected parties I think Layer zero already knows I mean they've read the or some of the developers have read this already and then you know the other two we can contact them as well. And I guess you know the news will spread as well. We'll also put this up on our Twitter account. You know, maybe we can do the same thing on some of your accounts, but  I don't think we'll find completely different protocols that will be similar to what these Protocols are doing.  


**Danny** [29:19](https://www.youtube.com/watch?v=Voavkk8Es5E&t1759s): Great thank you for any other questions? Okay I appreciate it we dropped the link in the chat for the full report check it out. Obviously this isn't something we're making a decision on today but this is really good information to help us make decisions in the future. There were a lot of discussion points in the chat. Is anybody want to surface anything for this discussion now? 


## Dancun Updates


**Danny** [30:00](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1800s): Okay great thank you for the detailed analysis next up are just general Dancun, Dancun updates any test net updates that we want to relay or other updates relevant for today.


**Paritosh** [20:19](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1819s): Yeah we have devnet7 up and running since last Friday and just the test now it's been finalised. We've also submitted a bunch of blobs to it and triggered at least one or two issues in the test map. I think some of them have already been patched and some are still open. There's an issue tracker so please refer to that for more details. And besides that once we have all the patches put in we're gonna just continue spamming the network to see how we'd perform with the three six blobs being full all the time so far we've headed for short durations of time but we haven't had it for a longer duration of time. And there's a message from Justin from the security team about a deposit processing issue. If someone from Techo could have a look that would be great or I think Techno and prism could have a look that would be great. 


**Danny** [31:17](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1877s):  What layer of the stack are we seeing were the couple of issues is networking consensus.


**Paritosh** [31:27](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1887s):   I'd say it was networking issues. I think Mario's has a lot more information on that and if you want to expand on that election.


**MauriusVanDerWijden** [31:37](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1897s): Yeah so Geth had an issue with European coding of the transactions on the on the networking layers so transactions weren't relayed correctly the that was fixed now so it's that was the only thing like it like transactions between guest nodes were relayed but not with the others and the others implemented this correctly so.


**Paritosh** [32:15](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1935s):  I think there was also an issue with the message size right with the two long messages being requested.


**MauriusVanDerWijden** [32:21](https://www.youtube.com/watch?v=Voavkk8Es5E&t=1941s):  Yeah but this is not really something that we can change on our end. Basically we can just say hey give us give us messages give us these messages and the someone on the other side has to respond. There was an issue in Geth where we would we would not tell the other nodes the correct size of the messages but I don't think anyone is really like has implemented this part where we really use EIP 60 like the new EIP 6068 mechanism to say to filter messages and say okay we now want block messages or we only want messages that are smaller than X so yeah that's something that still needs to be implemented. I think some clients might even still send blob messages over each other's protocol versions. I think especially ethereum JS because they don't have EIP 6068 yet so either they are not sending any block transactions or they're using EIP 6066 which is not good.


**Danny** [34:03](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2043s): Okay thanks for the updates. Any other Cancun updates.


**Alexy** [34:10](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2050s): Yeah another mindfulness issue would you almost have a fixed as an image we'll deploy it soon. It is connected to the message size which was mentioned right. So let's fix themselves away.


**Marcin Sobczak** [34:36](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2076s): Yes, we have a mechanism of limiting the size of transactions which we are handing but we had a bug in calculating size like length of block transactions and it's already fixed and will be merged in a few minutes. And probably images for Devnet7 will be updated today as well.


**Paritosh** [35:04](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2103s):  Assuming that all the fixes are in and devnet7 is relatively stable. Do we then start planning would you guys prefer that we start playing the next one with all the other EIPs or should we continue just keeping in devnet 7 Up and stressing it more. I'm not sure which approach we're gonna take right now.


**Danny** [35:28](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2128s): I know on the consensus layer at least a couple of teams have voiced the desire to move towards the full feature set for the next test net. But in terms of the timeline if we want to stress devnet7 and there's some some iterative pure 4844 updates that people want to do then you know that that makes sense. So preference for when we move to do so but I don't know if there's a Time preference for when we move.


**MauriusVanDerWijden** [35:59](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2159s):   So we don't have 4788 yet in the code and I think at least one or two other EIP’s. I would rather use this time to  stress test Devnet 7 and in parallel work on work on getting those other things in and not wait with the stress testing until the next devnet.


**Paritosh** [36:33](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2193s):  How about we add all the tests required for the next devnet onto Hive so that anyone who's ready can already start testing and making sure I have the screen. And in the meantime we keep Devnet7 around at the stress test 787. That'd be a good doesn't block any one approach.


**MauriusVanDerWijden** [36:53](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2213s):  Sounds good to me. 


**Danny** [36:54](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2214s): Yeah I think so. We don't need to be setting the date for the next test snap but allowing clients to be in the position to move there. Mario?


**Mario Vega** [37:06](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2226s):  Yeah do you mean with the Hive test do you mean the EPIP tests or the for example the dev peer-to-peer issues tests or both of them.


**Danny** [37:22](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2242s): Yeah because ultimately both starting with consensus and then moving to w2p makes sense unless you think otherwise.


**Mario Vega** [37:31](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2251s): Yeah we are still working on having all the atheists. I think in the next couple of weeks we should have them already for testing.  Yeah sure and I believe the EIP's are going to be a domain.


**Danny** [37:44](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2264s): we kind of consensus rather than the P2P test in terms of the workload on your end contrary to 4844.


**Mario Vega** [38:00](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2280s): Yeah definitely I think foreign was like a one-off because of the different transaction formats that we used in the header versus the peer-to-peer so that's not gonna be an issue for the other areas yeah.


**Danny** [38:26](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2306s):  Yeah so Barnabas just to Echo that obviously unless major issues are found with devnet7 and pure for before testing the intention is that the next devnet would be full featured for Dancun. But we're not  setting a timeline for that test net. We're gonna allow people to develop the full feature set while stress testing Devnet7.


**Paritosh** [38:55](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2335s):  I'm talking about issues with 24/36 we only had three six for a short curation. So I think it's too early to make a call on either one.


**Danny** [39:14](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2354s):  Cool and we can call on Monday 4844 call. We can spend some time talking about if there's networking stuff the surface looks like Nimbus is having issues but we don't we don't really have Clarity on if on our small test net three sixes changing the impact but we will continue to bring that up either on the call 4844 on Monday if we have time I mean if we have information or on existence clear call next week. And Barnabas just for your information the latest consensus layer spec release and test does have the full feature set on the consensus layer so if you're building the spec for that devnet you can point to whatever the latest releases.


**Barnabas Busa** [40:04](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2404s):  Great. Thanks. 


**Danny** [40:17](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2213s): Okay other Dancun discussion points? 


## `shouldOverrideBuilder` flag for Cancun -- [Scope shouldOverrideBuilder flag for Cancun execution-apis#425](https://github.com/ethereum/execution-apis/pull/425)


**Danny** [40:40](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2440s): Moving on there's an item from Snake Island myself that should override Builder flag and being introduced into the engine API. This was discussed something since their call last week and uh General consensus that getting this flag in the engine API is high priority for them and very easy because it can be introduced. And always sets a policy execution Layer and a no op if they feel like a consensus Layer, so you can kind of introduce the flag and then add feature functionality to it over time. But Mikhail can you give us the information on this and what people are thinking.


**Mikhail Kalinin** [41:24](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2484s):  Okay so I'll just quickly go give the context on this flag and then the discussion on whether it glued it into Cancun. So should a ride Builder flag and the proposal is to add this flag to the get payroll response is basically true or false. This is the way the EL to communicate to see all that there is some censorship is happening in the network and CL should make its own decision about that. So the way the way it's supposed to work so yeah we'll have some heuristics and to find the evidence of censorship transactions censorship in the network and according to this heuristics made a decision and returned this back with the build payload so we if we were client diversity for implementing this heuristics. So they're completely unspecified for this reason and also if EL does not implement any of the heuristics it should always return false. So yeah as the instead it should be in all and also consists their client should may also ignore this track even if it is sad the truth so it's completely free process for both parties and consensus they may use other sources of this to feed it into their decision-making process about censorship. So the main reason why this flag should be returned by EL is that EL has information like mem-pool and the re-work which is a pretty big chunk of data that it does not want to expose why any API and it doesn't make sense to be exposed. So that's the way it is supposed to work. And getting back to Cancun so we want to include this into Cancun as Danny’s said the sale clients are on board with that and considering that the engineering complexity it's really low. And also we have a prototype in Geth of those heuristics viruses that can give more details on that, considering that the complexity is low and the utility is quite high of that flag. So the proposal is to make it into that's basically it. Lukasz?


**Lukasz Rozmej** [43:59](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2213s):  So my question might be premature. Maybe Mario's should come first but the question is what's the status of research of this heuristics and are there like many of them proposed are there are they in any way like stacked on historical data right. Against historical data and my question stems from actually client diversity so think that a client would implement this in a way that would plug a lot of false positives right and then stakers might be discouraged to this client because they would get lower rewards. So it may affect like uh this kind of things too so hence my question?


**Danny**  [44:58](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2698s):  I suppose in theory that is possible you know if you always if you had a client that always said true and you could never write that and CL listened to the EL you know in the extreme obviously you would have lower words. That said, I know there are discussions of a number of simple heuristics. For example transactions sitting in the mem-pool for X time that certainly could have been included profitably in a block where you know these end up looking pretty deterministic. But I also you know this is primarily to elevate the EL to have a voice in you know the fallback functionality um you know and there's any number of reasons even Beyond censorship that you might perform such fallbacks but are there any are there any write-ups or deeper discussions of potential heuristics here I know potos has thought about them.

**MauriusVanDerWijden** [46:07](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2767s): So I have not really thought about it. I just implemented this very simple heuristic: if a transaction has been reorg'd at least two or three times then we suspect that someone is censoring it. This is just the first heuristic that I today thought about. So it's not not back tested it's not really yeah it's just something to prove that it's actually possible to implement this and show that it's very easy to implement those heuristics. Lukasz.

**Lukasz Rozmej** [47:02](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2822s): So okay let's say someone reorg'd transactions three times you  have this like you you managed to find this out and so for how long do you return this lag.

**MauriusVanDerWijden** [47:18](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2838s): Forever afterwards.

**Lukasz Rozmej** [47:21](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2841s):  Okay that's probably also not optimal. 

**MauriusVanDerWijden** [47:25](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2845s): No as I said this is very much a draft of this concept it's just to make sure that this concept kind of works.

**Danny** [47:36](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2856s): Yeah I mean and and defining optimality is certainly up to the client right like if you have any heuristics go off you can flip a coin ways if you are concerned about that to delay those concerns go on sir.

**Lukasz Rozmej** [47:58](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2878s): Good idea from Ben that if we have empty blocks fairly empty blocks that could take transactions from the transaction pool but didn't right so someone is trying to uh like tensorably block space in general not certain transactions good idea for a heuristic.

**Danny** [48:18](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2898s):  Yeah I mean I guess the way I think about it is primarily this the EL has a lot of information that gives a way for the EL to give an opinion to voice something about that information. And because it's very wide open then you know you know you have the faculty to decide when and if to voice that oh yes.

**Lukasz Rozmej** [48:42](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2922s): I'm totally agreeing with the concept right the concept is great and we should implement it ASAP and it's very simple because we can right now just returned false for some time just wanted to highlight that this opens quite a not trivial problems that may have better or worse solutions that in my opinion need some res maybe needs could be helpful to have some research on that's what I meant agree.

**Ahmed Bitar** [49:21](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2961s): One thing that I noticed also about the code I'm not entirely sure about it but I was thinking that if someone posts a  transaction with a bit of a low fee or a low  priority fee and that's the reason why it's not included with the current approach that Marius has this might flag as censoring when it's actually not.

**MauriusVanDerWijden** [49:48](https://www.youtube.com/watch?v=Voavkk8Es5E&t=2988s): No it's like this only tracks if a block gets like if a block gets react out and like we see three blocks in a row getting reoped out and they mean they contain the same transaction then we suspect someone is doing.

**Ahmed Bitar** [50:10](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3010s): So we're talking about only reorging not being included.  

**MauriusVanDerWijden** [50:15](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3015s):  Yes the heuristic that I implemented yes. 

**Danny** [50:26](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3026s): So the main question here is anyone opposed to getting this into the engine API spec. It is a single Boolean flag in one method other than implementing the engine API. You don't have to do anything immediately um this would probably be slated for that full feature devnet that we're talking about called devnet. Xeon opposed that we have support from the consensus layer teams Mars right now we do not have the API’s for the engine API. The engine API is more of an implementation detail around the outer consensus spec but I'm not sure if there was .Dankrad?

**Dankrad Feist** [51:17](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3077s): What are we going to do with this flag when we have it? 


**Danny** [51:23](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3083s): In the event that the execution layer says true the consensus layer can decide to fall back to local building instead of that booster any sort of X outer block building.

**Dankrad Feist** [51:36](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3096s):  Oh but sorry that's that doesn't mean okay so but then marius's approach of detecting it doesn't make sense because he is detecting it using reorg blocks right.

**Danny** [51:49](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3109s):  Right so implementation that okay all right go ahead we can debate we can debate that right because if the attacker has the ability to reorg then they're going to just reorg it again. We can debate the technique, yeah.

**Dankrad Feist** [52:03](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3123s):  I mean yeah so like I mean I think like such a flag only makes sense if you can detect an attack and you have a remedy for that attack like yeah if like we can if we can detect block Builders are not including it then that flag might be interesting. But if like we're detecting something completely different and extrapolating from that censorship is going on then it doesn't make sense to like affect this part of like I don't know the two that don't seem to be.	

**Danny** [52:30](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3150s): There are many other heuristics that do not involve reworks you're right there is a Nuance.

**Dankrad Feist** [52:35](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3155s):  All right but I'm simply saying like I mean it definitely has to be one of those like otherwise it doesn't make sense to me.

**Danny** [52:46](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3166s):  Agreed. I think the most obvious ones are monitoring them pool and with respect to what was included in the main chain and that does not have to do with reorgs and can allow for something there might be.


**Dankrad Feist** [53:02](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3182s):  In that case you have to make a judgement about the tips but I think you can say if transactions with lower tips are getting included then you could like to say a censoring attack is probably going on.


**Danny** [53:25](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3205s):  But I do think we and I agree that there are techniques that are valuable here and relatively simple.


**MauriusVanDerWijden** [53:38](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3218s):  And this also I think this heuristic was kind of naturally grown and in the beginning it was just just a log output if we have this if we see this case so basically just an indicator that the censorship is going on and for that one the heuristic was fine. I agree that um for falling back to local block building this heuristic is not really on doesn't say anything. So yeah as I said the heuristic was something that was thought up in like five minutes just to see that the concept works. 


**Mikhail Kalinin** [54:33](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3273s):  So yeah thanks a lot for the discussion. Recapping if there are no, if there is no opposition on the call if anyone listened to us and has an opposition to this tiny change please express it in the EIP or sorry in the PR. I will be aiming to merge this on next Monday so that's the plan.


## Bounded 4788 storage to be merged -- [Update EIP-4788: Bound precompile storage EIPs#7178](https://github.com/ethereum/EIPs/pull/7178)


**Danny** [55:09](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3309s):  Great, thank you Mikhail. Okay next up 4788 bounded storage has been merged Alex do you have anything you want to discuss here. 


**Alex Stokes** [55:29](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3329s): Not really I mainly just calling it out we've kind of had a little bit of back and forth on the design and the PR that was merged is kind of the last or sort of you know the product of all those conversations so basically it's storing blockers from the beacon chain and the storage is now bounded using like two ring buffers and yeah I'll just point you to the PR. If you want to see the details a few people have implemented it and said good things. So sounds like this is the 4844 EIP right now.

**Danny** [56:05](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3365s): Thank you great and this had no impact on the consensus layers right.

**Alex Stokes** [56:13](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3373s): Yeah that's been handled other places there's 4844 engine API so that's all set and then yeah all this was really doing was just changing some of the implementation details of the actual pre-compile but otherwise same basic idea.

**Danny** [56:30](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3390s):  Yeah great, any questions for Alex? Thank you. That's all we have on the agenda for today are there any other discussion points or announcements concerns at this point. Okay thank you everyone I believe Tim will be back for the next version of this call in two weeks talk to you all very soon.


**Pooja Ranjan** [57:11](https://www.youtube.com/watch?v=Voavkk8Es5E&t=3431s):  Thank you! 


—-------------------------------------------------------------------------------------------------------

# Attendees

* Danny
* Record Bot
* MariusVanDerWijden
* Pooja Ranjan
* Justin Florentine
* Ben Adams
* Damian
* Danno Ferrin
* Lightclient
* Marekm
* Neville Grech
* William Schwab
* Ben Edgington
* Mikhail Kalinin
* Alexy (@flcl42)
* Mario Vega
* Paritosh
* La Donna Higgins
* Georgios Konstantopoulos
* Roman Krasiuk
* Ahmad Bitar
* Ameziane Hamlat
* James He
* Stokes
* Enrico Del Fante
* Sifis Lagouvardos
* Lukasz Rozmej
* Ansgar Dietrichs
* Barnabas Busa
* Dan (Danceratopz)
* Andrew Ashikhmin
* Radoslaw Zagorowicz
* Marcin Sobczak
* Alexy Shekhirin
* Stefan Bratanov
* Gajinder
* Mike Kim
* Karim T.
* Mehdi Aouadi

—------------------------------------------------------------------------------------------------

### Next Meeting Date/Time: Thursday 20 July 2023 at 14:00 UTC
