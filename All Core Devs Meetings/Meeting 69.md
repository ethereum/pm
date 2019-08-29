# Ethereum Core Devs Meeting 69 Notes
### Meeting Date/Time: Friday 23 August 2019 at 14:00 UTC
### Meeting Duration: 1hr 20mins
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/121)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=yO0WdT-J64w)
### Moderator: Hudson Jameson
### Notes: Pooja Ranjan
	
----
	
# Summary
	
## DECISIONS
	

**DECISIONS 69.1**: Block number will be picked after Parity implementation.

**DECISIONS 69.2**: All Clients are required to have **implemented all EIPs** for Hardfork: Istanbul I **by 6th September 2019**.

**DECISIONS 69.3**: **Mainnet HF may be delayed**, not on October 4th. Wait for testnet number then pick date for mainnet HF.

**DECISIONS 69.4**: Going forward **ACD calls will be at regular time (1400 UTC)**. If someone feels that rotating is really valuable then they can step up and say it, either on ACD call or elsewhere.


## ACTION ITEMS

**ACTION 69.1**:  EIP 1884 - Discuss this on ACD gitter and or FEM. Need something formal to be discussed on a technical level about the benefits of it and then needed to be strived on a more abstract level on the future direction and how we should best handle it with consideration that some of dapps could break. We keep an ear open to people who have those concerns within the community.

## SUGGESTIONS

**SUGGESTION 69.1**: **Shadow fork on Ropsten**.

**SUGGESTION 69.2**: Migrating from Ropsten and **have a new testnet network**. If Ropsten never get the ProgPOW and the new network gets the ProgPOW out, that would be one differentiator.
	
-----


**Hudson**: Welcome everyone. This is agenda number 69 and is going to be Istanbul related. Let's go to the clients and see what updates have happened. 

# 1. Istanbul related client updates

## Pantheon

* **Merged**: All EIP merged. 

**Martin**: I put together this [tracker](https://notes.ethereum.org/@holiman/SyT_rGjNr) and also the code side-by-side.

**Hudson**: I just updated the agenda if y'all want to refresh your page and agenda item one now has a link to Martin's tracker so that's really helpful.

## Geth

* **Merged**: All EIP merged. 

**Hudson**: Looks like the Geth team has everything, Peter or Martin do you want to elaborate on that at all?

**Peter**: Not much, we finish implementing EIP. Also, enabled the Istanbul config over Genesis. It would be nice to have multi client thing.

**Martin**: We merged in support Geth for ReTestEth for Istanbul.

## Aleth

* **Merged**: EIP 1108 (alt_bn128 reduction), 1344 (Chain id), 2028 (Calldata gc reduction) are merged.

* **Open**: EIP 1884 (Repricing SLOAD et al), 2200 (Net-metered SSTORE) are still open.

**Hudson**: Nice, the next client is Aleth and the chart that Martin has is accurate as of 24 minutes ago when when gumb0 on the agenda left a [comment](https://github.com/ethereum/pm/issues/121#issuecomment-524321107) about the progress update for Aleth

**Hudson**: The next client would be Parity.

## Parity

* **Merged**: 2028 (Calldata gc reduction)

* **Open**: 1344 (Chain id), 2200 (Net-metered SSTORE)
 
* **Closed**: 1108 (alt_bn128 reduction) 


**Wei**: We've Call data and Gas cost reduction merged. Others are open PR or haven't been implemented. We need time till 6th September to finish the implementation. Not only because we accepted EIPs late but right now we  just happened to be a large code base refactoring and we probably want to merge them first before merging Istanbul EIP.

**Hudson**: All right, understood. 

We already talked about Pantheon and they are reflected in the chart.

## Trinity

* **Merged**: EIP 1108 (alt_bn128 reduction), 2200 (Net-metered SSTORE)	

* **Open**: 1344 (Chain id), 1884 (Repricing SLOAD et al), 2028 (Calldata gc reduction)

**Hudson**: As far as I can tell they still have the Blake F EIP potentially unimplemented, as the call data reduction unimplemented and everything else looks either open or merged.


## Nethermind

**Tomasz**: Everything except blank is merged already and for blank, we're in process and should be ready soon.

**Hudson**: Great! am I missing any clients?



# 2. EIP-1380 Benchmarking

**Hudson**: Okay the next thing I want to discuss are the recent benchmarking. There's one from Martin and there's one from Asic. I'll post the [link](https://github.com/ethereum/pm/issues/121#issuecomment-524325234) to Axic.

**Martin**: The one that I did has nothing to do with Istanbul hardfork.

**Hudson**: Let's skip it and will comeback with more Berlin stuff.
Then it looks like there's some Gas estimation made for the verification zcash headers by axic, it's in a comment.

In short the call cost to compile 385000 gas alone not counting anything else. I could imagine the total cost would be something like 600,000 to 1 million gas. so I think that there're some interesting information about the Blake 2B EIP. Is anyone else have comments on that?

**Martin**:  Well, the one thing that axic has proposed earlier to reduce the gas cost for pre compile and  in relation to that (which I don't recall the number on) this is interesting. Because if we were to do stuff, this number could go up like in order of magnitude.

**Hudson**: Anybody else have comments?



# 3. Decide block number for Istanbul testnet fork?

**Hudson**: Okay, next we have to decide the block number for Istanbul testnet for. It sounds like based on a few clients that still have some implantation to do that we might not be able to make that decision today. But I want to hear everybody's opinions on that and see if this is something that we want to do today or not; because I am open to hear different opinion.

**Martin**: Yeah  was it  6th September?
 
 **Wei**: Yeas,  we need two weeks.
 
 **Tim**: So thats when your release is out. We probably need some buffer after the 6th of September for the testnet, correct?
 
 **Wei**:  Yeah that's just a safe date for us. Like if we rush, we might get it earlier.
 
 **Tim**: But yeah that's the date just by which you feel comfortable having implemented the EIPs not the one by which you feel comfortable hardforking the testnet.
 
 **Wei**: Yeah.
 
**Hudson**: Got it and what's the release cycle for Parity? Is it like just when you want to or is it on like a time schedule?

**Wei**: We can do release just after the implementation. A few days or week buffer would be great.

**Hudson**: Yeah I think that if we have a short meeting next week or we decide on gitter what the number would be. I think doing it in a week would be safe because you would have a better idea of how much more time you need and if it's anything more than a week we can reevaluate but if it's just a week then we can pick the block number and start having clients release. Is that something that we can agree on everyone or does that sounds a little too aggressive?

**Tim**: So I think it's just worth highlighting that if we do this, say that brings us the August 30th where we pick a blocked it'll be a week or two after Parity release, so mid-September and **it seems impossible then the October fork mainnet deadline**, like two weeks of testnet before mainnet seems reckless. So, its worth probably just making explicit that this also means that mainnet hardfork date will slip.

**Wei**: I have one comment related to testnet date, it's related to specification to gas things. I think that we should fix that issue before we actually hardfork mainnet because otherwise if we decide to do something else, we cannot un-fork thing and it may create a lot more complication and actually delay the mainnet further.

**Martin**: What do we solve right now?

**Wei**: Like the gas thing. We might want to rise it so that we don't accidently freeze some contract, right? 

**Martin**: So you would propose that one in combination with a general racing of the gas - from 2300 to something else? 

**Wei**: Yes. As per your analysis, we probably will freeze some contracts if we just apply its results. I think we probably  want  to do something just before we hardfork testnet so  that we really don't do some really complicated things in the future.

**Hudson**: Okay I think I know which issue you're talking about. you're talking about the one where or when we re-price the opcode from 1884 then it might freeze up some contracts that are  dependent on the gas cost being a certain amount and their contracts. Did I get that right so far ?

**Wei**: Yeah.

**Hudson**: And so what happens is, we want to prevent that sort of do.  we don't have to do anything tricky in the future to undo that mistake for stuck contracts. And **the analysis has been performed by Martin and they did find some contracts that would potentially break**. I forgot what the analysis was exactly. Martin can you refresh my memory?

**Martin**: So there is an analysis on GitHub repo of mine. It's hard to join a general conclusions from it because in some cases,  the problem is that you have designated senders, only a couple of senders are allowed to deposit to a certain contract. those senders used Solidity mechanism transfer, which only sounds 2300 with that. Therefore the senders can only send 2300 and the recipient does s sload. A noticeable example was Kyber. In that particular case, an increased gas stipend would work. However there are other similar cases where a fixed amount of gas is used like 119000 for similar call. Other potential things that could break is is if a contract in default function does a  few log operations and also a s load. There could be different ways to solve these problems and I don't really think that there is one solution that would solve it forever case and I don't even think that every case needs to be solved. Some contracts are dead and unused for five hundred days. Other contracts are still used but they have built-in capabilities to upgrade themselves. It would be more work for the operators but it's not impossible.

So, given there is no really self-evident magic bullet to sole it, my personal thought is that we should just go ahead. If there is something which we mess up then that could be fixed in a hardfork following Istanbul.  At that point in time, the Operators of contracts who have been destroyed by this they can contact the all core devs. It makes it easier to figure out what the best solution is that sufficiently solves the actual problematic ones and not every theoretical corner case that exist on the blockchain.

**Hudson**: Okay, I think I got that. Basically if we were to find a solution today, we may find out after the fact that it was not the best solution based on the feedback we get from the people with broken contracts is what I what I kind of interpreted from that.

**Peter**: Not exactly. So there was a proposed solution  but it's really hacky and weird and our suggestion was that it feels weird to add a hacky solution for a case that might not be relevant. The idea was that let's not add hack in now but we know what the hack could be. If we legitimately break something that we didn't know that we're going to break then we can always put in the heck later. but let's go back in before it actually needed.

**Hudson**: Don't we know it's going to break some things though or do you mean break some and people complain.

**Martin**: So, yeah we know it's going to break things, theoretically.  All of those things can break a different way. Some of them can break because of a combination with load and unload those to be sold by making log cheaper. Some other break because they do a lot of s load at the other recipients and those could in some cases be solved just by upgrade  the contract. 

So there are different ways to solve this and not really one. The hacky solution would kind of open us up for a tax optimal and waste proposal but he mentioned earlier he has to raise the gas. It's kind of where I'm staying because that brings us back to issues with re-entrance  and state modifications.

**Wei**: What I really worry is that this could be a potential PR disaster. so the issue is basically, if we broke some contracts and we are asked to unfreeze it, it could have a similar situation like the Parity Multisig. SO, it's like all about subsidiary contract and about to make sure some contracts are unfrozen so it could be like a potential really policy closing. I just worry if we don't fix them right now, in future we may not have a chance for them to add them to function at all.

**Hudson**: That's not a bad point. I would say that, part of what can prevent that is kind of getting ahead of any negative PR that happens by completely explaining the situation and ways that everyone can understand and how this would be a different case in a way that the way the contracts broke this time was not what some would consider an idiot sequence with solidity but a side effect of a needed upgrade that happened at the protocol level and not a higher level. That's how I would explain it but I might be getting that wrong and I would absolutely consult with a lot of people before or pulling something like that out there.

**Wei**: I think rising the gas is a simple operation and we should have most re-entry possibility related to that covered. If you allow 2200 I don't think it would be a big issue, there's obvious solution to it.

**Martin**:  The thing is, currently, theoretical it up to 20  s load, you can do at 2300 gas and if we want that still to be theoretically possible after we reach the 800, that means the gas stipend needs to pump up to 16000. If you have gas at 16000, then obviously you can do re-entrance and state modification.

**Wei**: You can't do re-entrance if any store is below the gas stipend and range would automatically fail after 2200. 

**Martin**: Yeah, we would have to modify 2200 as well. Then all of a sudden you would be unable to do state modification if you have less than  16000 gas. 

There have been a couple suggestions on how to handle this. It would be better if you write down a proposal where you specify some exact numbers. I know the contract library guys have volunteered that if we want to play with some scenarios such as increase in gas stipend and so on or lowering the load cost for another then they can evaluate that against set of affected contracts. So we could work with them to automate analysis of scenarios. But  I have not seen a definite proposal to how we can solve.

**Tomsaz**: Martin say thing that may be controversial but if you're  thinking about it for a moment and think that we can introduce something like we could potentially make a progressive cost but like not too complex but some kind of progressive cost for those operations.

**Martin**: Yeah it's possible that  we could **discuss it on fellowship, ticket on 1884 security repository** - fun tickets with proposal for how to fix it?

**Hudson**: yeah I'd say a combination of the Core dev gitter Channel announcing the analysis and commenting on. I guess just cover all bases, Fellowship of Ethereum Magicians as well as trying to merge information and the security considerations of the EIP. Is that the third one you mentioned, Martin? Or is there a whole another repo?
We could basically store the analysis on repo and then have a discussion on the chat and Fellowship of Ethereum Magicians that seems sufficient for getting the word out amongst the core developers for any proposals for something like this. But I agree with Martin that there needs to be something a little bit more formal proposed about what's going to be the best way if we're going to put some solution in before the hard fork what that solution would be. Any another comments on this? Anybody have an idea or stuff like that ?

**James**: My comment is that this feels like a unique circumstance cuz it's kind of one of the first time this has happened. At least the idea of an intentional change that does have some breaking changes. That also is the promise of what Eth1.x  needed to be observation. So while this one case, I may be thinking about it from solving this exact case as we keep moving forward, this will happen more specially if we get it to state rent. And so that the general case of how to approach this coming from this specific one I think it's worth thinking about.

**Wei**: I just want to  comment, a really easy way to to fix this thing once forever breaking change so we can see. Just an ideas, so you can just do a conversation  in operation 0 and then for operation 1, we move any opcodes related to gas. Make it so that a contract helper cannot make any assumption about the gas cost. ALl those gas issues will not happen for ever and from that version, while we can change the gas cost whatever one want for how many times we want to do future boots.

**Martin**: Yeah but I don't see that being a solution because we still have the non version things right, with low gas it doesn't solve the problem. 

**James**:  My point was it was even outside of gas cost like there's a very large network of soon anonymous, permissionless deployed who knows what; if there isn't, a hey this contract is owned by this person. Just how to handle this situation where it's something we know could happen, how do we proactively say, hey we're thinking about it with the realization that kind of an impossible battle to which everyone in the network. So someone will likely get upset the bit say something.

**Peter**: Adding thought,  I mean realistically, Ethereum is going to be alive for the coming however many years than we cannot expect never ever to break anything. I don't think it will ever be possible to keep indefinitely running contracts that were deployed in Frontier. It would be nice and we should definitely  strive for it. but if we say that it won't ever break anything that might actually be quiet a heavy price to pay.

**Wei**: Actually, why we are breaking stuff because EVM is not actually designed for future app but you can really make some simple change like just removing reference to gas to make EVM good for future friendlier to feature. You can make this so that it's really hard to break stuff too much. Like a really good backward compatibility.  

**Peter**: But you're talking about gas price changes now. So specifically nobody thought that this would be an issue and nobody fixed it. Yes we can upgrade the solution to fix the gas prices  issues but I'm almost certain that next time there will be a completely different class of issues that the again would need something special to fix it.
So I think it's software development that you discover the problem as you go along and you need to figure out what to do with those problems.
I am saying is that if you are willing to pay the price of not breaking anything.

**Wei**: If there is a way to do that, I would definitely  do that, but I think it's just excessive for Ethereum because code is law and you don't want to break it.  

**Martin**: We did back in the Shanghai attacks we intensionally broke the attackers contracts, thats what we did in the Tangerine whistle, Spurious Dragon. Do we want to wait until the next round of Shanghai attacks which targets are cheap s loads before we do it another upgrade of that and at that time intentionally break those attacking contracts.

**Wei**: There is a major difference between some attacking networks and we just fix it than having a future upgrades that breaks some non attacking contracts. These are really two different things. It is still the issue of gas cost. You can fix it in different ways that doesn't break those attacking contracts for eg. makes a contract really expensive to run, so it can't be used as attacking contracts anymore or stuff like that. but I do think that backward compatibility is quite important for Ethereum that I think we should treat it thoughtfully. This is my opinion, but  for this hardfork, the issue is not like over my dead body that if we go with it, I am fine with it. 

**James**: I think it's also important to consider the other side. Not just where a change could break a contract but the change will be benefit to another contract like for example the reducing of gas cost is something that would be great for your swap redeploying based on versioning would be really difficult for them. So there are people who would benefit from having a breaking change happen. And people who would detriment from having the change that happen universally or not version. I think  we have to swallow both pills if we want to do one.

**Hudson**: I guess, James the only thing is, it's not a thing where we're swallowing both pills because what ways  proposing is putting in something that saves the old contracts while reducing the cost; so that's kind of an idea for something that will help with the PR and not make people upset and keep Ethereum's contracts in a state where at least for the moment we can say the code will for the moment run as intended without breaking a contract except for all the other times you've done it.

**Trenton**: The idea has to be implemented in addition to 1884, right? 

**Wei**: We can clarify. I don't think we can get what I said in Istanbul.  So it would require a conversationing and you require another EIP for the subversion of not breaking change. But we'll fix those kind of issues once and for all.

**Hudson**: So you're saying for this issue , we wouldn't be able to cut it for Istanbul so we have a good amount of time for any proposals that come out about ways to fix this, if we decide to fix this at all, is that accurate?

**Wei**: yeah  I'm just saying my concern that I think the current situation should be treated more seriously. We need to make a decision by the rebound, just break those contracts or still want to fix it. I think we probably want to catch more people like outside of the core dev.

**Trenton**: Correct me if I'm wrong but it's not like a nice to have it's more of an existential, the chain will have serious problems if this doesn't change, right? or could in the future?

**Wei**: I don't think this is like existential. It is just nice to have this time. 

**Martin**: No, I also consider it not a nice to have but more important than that.

**Trenton**: Can you expand on why it's a necessary thing, Martin?

**Hudson**: It won't change the decision but yeah I wish I'd like to hear **why it's more necessary than a nice to have** for it like for the reason of if we discuss this with the community how we can frame it ?

**Trenton**: Right because they are just looking at it from their baseline like oh now it's harder to do this thing that I'm doing but in reality it's not a punitive measure when I try to make things more difficult and they need to understand that it has.

**Martin**: Yeah it's simple the case that does the  state grows larger and larger, it becomes more IO intense to look up something, a random key in our state right. SO basically an attacking contract is just spuriously loads random s loads, also will be expensive.  Yeah that's it. 

**Wei**: Well I think the future is like we have larger state. What I am saying is we might just want to fix it,  find some way to fix it before deciding  testnet dates 

**Martin**: So, I consider this to be a band-aid until we get some proper 1x changes that can reduce the state load. I'm hoping that we don't have to race it down but instead have some benefits from 1x 
I totally agree that it would be really nice if we have some really good mechanism that stops the contracts from breaking. I have not seen as such solution that I think is the most ultimate of all of them. There are three or four different things that could be done. Let's continue that discussion and hope we get to something otherwise I would be fine with just trying to solve it post facto.

**Hudson**: We don't have to. There's already the reality that this has to be solved after Istanbul as far as implementing it. So we can discuss it between now and then as this is like an important topic of conversation, however a formal proposal will need to be written in order to have a baseline for a fix that is you know there was something we could actually do that might be a little less hacky or something that would be a little more clear. Is that somewhat what you were saying Martin that we don't need to focus on this, the second, because it's not going to go into Istanbul anyway?

**Martin**: No, I thought Wei meant that we should wait for testnet until we solve this issue. But maybe I misheard him.

**Wei**: Yeah like what I'm saying is this would be a factor to consider when Istanbul 2 has several weeks just to see if they  can come up with something good before the testnet date. Because once its on testnet, it's really hard for other solutions that might be more elegant to be applied on testnet.To clarify, I don't mean to delay testnet or something. This is just purely  for the testnet dates. I would rather be safe than sorry. If testnet has some other issues and got delayed, then the mainnet will be delayed further. 

**Martin**: On the other hand, the testnet is pretty good. it's actually pretty good to roll this out on testnet and see what breaks. I think, obviously a lot of crypto reads Twitter but those who don't might find on the testnets that they are contracts broke, which I'd argue is a pretty good data point.

**Wei**: But we already, it will break some contracts. 

**Martin**: We don't know what contract, we don't know which ones rae still relevent.

**Wei**: It might be a PR issue like if you have a test plan that is entirely new and not on Ropsten but there are a lot of people using Ropsten testnet, so if we accidently break a lot of contracts.

**Hudson**: I think that from a PR perspective the core developers should worry less about that. I mean that's obviously something that you keep in mind but there are people who are communications and PR people within most of our organization  including Parity and in the Ethereum foundation and Pantheon and everywhere. That they can get together and craft a message that is very clear about what the mandate for 1x was and how these things are going to go down now and in the future. So that the cre devs don't have to worry about that and some of them can be deflected, I know. I personally am probably going to write something to the extent of there is a communication breakdown between major dapp developers in the core devs  and part of that is not having a position technically that's a paid position for someone to do that full-time and if I find the best solutions for that. I guess what I'm saying is there is the potential for some bad PR but I don't think it's a show stopper for implementing something that has to save all the contracts and I think there are people equipped to handle that and I know the people from the EF parity and Pantheon who could get together and I think we're already in a chat room who would help with that. So I think that should be less of a concern honestly

**Martin**: Yeah I like to express the counter opinion to Wei's that actually, since we probably will break some contract flows scenarios, it's important to roll it out on testnets as early as possible. So they can investigate how to remediate that situation and check if their upgrades are working or how otherwise they can fix. 

**Hudson**: Yeah I can see that perspective. Are there any final thoughts on this? **What it sounds like the conclusion has come to that it  will need something formal so we can discuss it on a technical level what would be the benefits of it and then we will need to strive on a more abstract level what we want the future direction of what these breaking changes are going to mean and how we should best handle that with the consideration that these dapps some of them being very important to the community could break and making sure that we keep an ear open to people who have those concerns within the community.**  That's somewhat what I got to the conclusion that they would have anything else to add to that, that I kind of didn't go over as far as next steps?
Thanks everybody. I thought this was a really good conversation to have so that we can kind of have expectations set for future upgrades that happened even post Istanbul.



# 4. Conformance testing
 

**Hudson**: Do we have anyone that has an update on testing? I know that there was some there was someone who mentioned that we should definitely have **cross client testing be one of the priorities**. I forgot who mention that but is that something that anyone wants to comment about ?

**Martin**: Dimitry is not on the call. Danno, are you on the call?


**Danno**: Yeah. I've done some work putting together some unit test **ReTestEth framework reference testnet**, to try and get some basis to do some cross client testing. 
* The current ReTestEth does one client at a time. We have to line them up and do them one at a time. Currently I'm debugging a different side. Geth Blake 2F is getting a different state root on Pantheon. But with the tool we can get to the root cause of it. 
* I've written some tests up for some basic self balance and chainID and blake2F and I was going to be working on getting some of the other tests there to make sure that they worked as expected. 
* Currently they're sitting in PR's as part of the Ethereum tests framework. They haven't been merged in the main yet. I think before we merge a test in the main, I think we should have at least two clients who agree on the results.
 
**Martin**: yeah I don't think we need to that careful about the merging because time to time pulling the new test is not gonna optimize the thing.

**Danno**: Same with Pantheon. But even when it's called a mean validation, I think from at least 2 clients, at some point that this is the right number and not something that made up.

**Martin**: Yeah at some point we have to think before we go live.

**Danno**: What's the status of Hive ? I know Pantheon is not on Hive, I'm working on announcing docs to get that. 

**Martin**: Hive is going for a major refactoring. It's going to be pretty big change, where hopefully within the next a week or two; we're going spin up a new machine to put the new version of hive on and then transition from the old one to the new one.
It's obviously the priority to have done when the test the Istanbul tests are done and exported into blockchain tests because thats when Hive can start testing.

**Danno**: Okay Hive doesn't do the differential fuzzing testing yet?

**Martin**: No. Hive is not capable of differential testing. It can't be started until client (in this case Parity and Geth) actually implement Istanbul make it figurable via Genesis.

**Hudson**: Cool, any other testing updates from anybody?

**Martin**: Yeah by the way they're on transaction tests but I've done, right before the reduce call act.  I was just wondering, if anyone has tried that yet?  I'll take that as a "No".

**Danno**: I'm not sure if we have implemented. I haven't been able to dig into the code and  generated, we have stuff referring to transactions tasks. I tried pulling in and  nothing broke but that doesn't mean that I'm sure they were writing them yet. I still need to dig in deeper there.

**Hudson**: anybody else have any comments?
 
 
 
# 5. Review previous decisions made and action items


* [Call 68](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2068.md)

**Hudson**: The last thing we  need to do is go over some of the action items. All the decisions from last meeting are very straightforward so I'm not going to go over them. 

The only one that's is now being changed is that **all clients are required to have them implemented all the EIPs for the hard Fork Istanbul I by** the 23rd of August 2019, that's been pushed back to the **6th of September**.

The **decision for the block number did not happen today**. so we're still discussing that and we can also continue to discuss that via Gitter. 

So those are the two decisions found last week that have just been changed otherwise all the decisions are pretty forward.

**Tim**: Given that we are pushing things back, it's probably worth making it official that **October 4th mainnet hard Fork is probably not going to happen**. I just want to double-check that's what everyone here, because if people are expecting mainnet  hard fork before Devcon, it just seems impossible at this point.  

**Hudson**: I can agree with that. Does anyone else have any comments on the possibility of that? Who thinks that we're going to have to pick another date for the mainnet hard fork?

**Peter**: Yes I think that's pretty obvious. Honestly I would say at least one month after the testnet is forked. 

**Hudson**: I was thinking too.

**Danno**: 3rd week in November?

**Hudson**: Let's **not put a date yet** exactly on it **until we get the testnet number**.

**Peter**:  I'm about to say the same thing.

**Hudson**: Anybody else have comments? 

On the topic of PR for those from Coindesk listening in, we do not have a date for the testnet or the mainnet hardfork  because we're taking care of the fact that we need to be very Mindful and careful and security conscious of the upgrades that we're doing. Thank you. I am not a trained to PR person just throwing that out there. Does anyone else have any other comments that didn't make it on the agenda and the other topics are things they want to say or discuss otherwise I think we're done.

**Martin**: Quick call. **Do people want to start the new Istanbul testnet**?

**Peter**: One thing I think we should do or would be  nice to do is to do **a shadow fork on Ropsten**, I wanted to do this for Constantinople 2. 
Essentially, don't hard-code the fork block number on Ropsten rather just pick one and run a few clients, and a few miners with that block number, that would shadow the real testnet and just see how things behave.

**Danno**: How would we keep that corrupting the main testnet when we change the network id on it?

**Peter**: Honestly, I would just leave them as is. So the two things would be connected and then they would shove incompatible blocks to one another.

**Danno**: Right, Ropsten's got enough issues.

**Martin**: As long as the shadow fork does not actually have the higher difficulty or the mining capacity than the mainnet Ropsten, it shouldn't be the bothersome to the regular Ropsten, Right? 

**Peter**: yeah probably there will be also problem with synchronization because one of the EIPs actually change difficulty or headers. So, **you can't fast sync against the shadow Ropsten**. 

**Danno**: That's a problem we only see all sorts zombie chain from the Constantinople issues when we try and fast sync. That's my concern, I am doing a shadow fork, recruiting more Zombies. If you are committed to take notes down, its fine that some might sink to them.

**Hudson**: Are there any platforms that can simulate a blockchain with traffic? Because I know Whiteblocks said before they have that and that they  open-sourced it but I don't know of anyone who has used it outside of white block people. I was thinking maybe consensus people might have, but I'm not positive.

**Peter**: Well, one of the things that we could try to do this whole Shadow fork thing in a more controlled way is we could spin off of small cluster, just a few machines running maybe one client from each team and instead of connecting them to Ropsten, have them completely firewood off of Ropsten and just to have a transaction relay that the stakes that connects to Ropsten and actually a full Ropsten node and just pushes the transaction into this internal thing. Then we can do whatever we want without actually being afraid of spamming block interrupts them back.

**Danno**: Right. We turn off your discovery and only connected nodes with each other,  that's a good solution I think. 

**Peter**: | would go a bit further. Would startup a few cloud of VMs and firewall them of each other, just to make sure that no client can misbehave.

**Trenton**: I'm pretty sure Whiteblock  could do exactly this. but I'll pass this along to Zac and I'm sure he'd be interested in helping in some way if we can.

**Hudson**: Cool, so we have white block, we have Peter's idea. I like Peter's idea a lot because that seems very controlled in a way that we can quickly identify if something goes wrong without having to seeing how bad Ropsten breaks and having to do analysis on Ropsten itself, am I getting that right?

**Peter**: So I'm not sure I follow the question. **The whole shadow fork idea was specifically not to break Ropsten prematurely but have a cross client testnet that actually have a traffic**. The bridge thing that's more or less to protect Ropsten from this shadow network.


**Hudson**: Got it. Okay do you want to decide to just do that right now, at minimum the shadow Network idea ?

**Martin**: Not the time for something quite a large undertaking for something or somebody to take on.

**Peter**: I am not sure. If we can speak , spinning up some virtual machine and deploying some clients on them. I don't know how much time it takes but I assume, it's not that big of a deal if somebody knows how to do it. I mean if you guys want I can try to hack it on Monday and see if its viable or not.

**Hudson**: yeah that'd be really nice.

**James**: I just got a new computer for my birthday so I can turn my old computer into something two running one of those nodes.

**Hudson**: take it old school we don't need no damn Cloud VM. We'll see what Peter does on Monday. we'll get message back from white block and the yeah happy belated birthday James.
Anybody else have comments before we end the call? When should the next meeting?

I don't think we can pick the block before the 6th, am I right? or is that 6th just when all the implementation will be done so we can have a block slightly before then?

**Peter**: I wouldn't pick a blocked number so I would say that if Parity managers to implement or we have a fair consensus of implementations by next Friday, then may be we can talk on chat . But as long as you don't have the things implemented,  we might as well decide today then.

**Hudson**: I see what you're saying. So, let's wait two weeks, does that sound good? Everyone good with two weeks from now?

**Danno**: That works good because if we could stick with a two-week schedule it deal with the needle of Devcon too.

**Hudson**: Okay and what time is the next meeting going to be?

**Tim**: That would be a  22 UTC, that right?

**Hudson**: It was 22 last week, 14 this week, so we need to do 6 next week.
We need to discuss in the future changing this because we have so little people joining now from all the time shifting.

**Danno**: I kind of agree. It was a good idea but I'm not sure that it's in that positive.

**Tim**: Can we discuss now?

**Hudson**: You know we actually could. Do you want to just have this at the same time in 2 weeks?

**Tim**: So can we say that the same time at 2 weeks and if anyone sort of feel strongly we should keep rotating the calls, then they can make a case for it and then we can start rotating again after that but personally like since we've started doing this it seems there's been like minor benefits and major detriments. One time it was at another time and then they come in a couple hours after and it obviously makes for less productive call. I would personally push to just **have call at regular time and if someone feels that it's really valuable that rotates then they can step up and say it, either on this call or elsewhere.**

**Hudson**: All right let's drop off this thing. Thanks everyone for coming and see you in two weeks at the same time 1400 UTC.

**Peter**: Martin suggested that we should ask whether we want o do a new testnet. I don't want to derail this discussion completely and say that we should do a shadow fork. But, I think people should maybe legitimately consider whether we want to reboot Ropsten maybe after Istanbul. Because Ropsten is kind of big and I don't think it worthwhile to keep bringing that luggage along 

**Danno**: I agree with this. One of the big issues were going to come up with ProgPOW launches as we're going todo a fork transition.

**Peter**: That should be fairly simple. ProgPOW needs empty blocks. You don't need transactions. You can always pin the empty network and see the transition work. 

**Hudson**: Anything else?

**Danno**: Would the idea be to restart Ropsten on the same chain id at 0 or picking a chain ID for a second proof of work chain?

**Peter**: If somebody wants to keep Ropsten alive, I don't see a reason to explicitly murder it.

**Danno**: Eventually the difficulty bomb will get it, if you don't forget it.

**Peter**: yeah 

**Hudson**: That gives people time to transition though. There's some people who rely on Ropsten, not that they should, but they do.

**Peter**: I mean I don't want to explicitly murder Ropsten just if we want to start a new testnet that we can create something  else and eventually people can migrate. We just tell everybody that Ropsten wont receive the forks any more, so transition when you can.

**Danno**: It **would be interesting that Ropsten never got the ProgPOW and the new network got the ProgPOW out, that would be one differentiator**. 

**Hudson**: Oh yeah totally. Okay any other comments?
All right we don't murder testnets, we only make new ones. 

Bye everyone.
# 6. Client Updates 
 None.
 
# 7. EWASM & Research Updates 

None.

 
	
	
# Attendees

* Daniel Ellison
* Danno Ferrin
* Hudson Jameson
* James Hancock
* Jason Carver
* Martin Holst Swende
* Neville Grech
* Péter Szilágyi
* Pooja Ranjan
* Tim Beiko
* Tomasz Stanczak
* Tenton Van Epps
* Wei Tang


# Date for Next Meeting: 6th September 2019, at 1400 UTC.


## Links discussed in call:

* https://notes.ethereum.org/@holiman/SyT_rGjNr the client tracker 
* https://github.com/ethereum/pm/issues/121#issuecomment-524325234
