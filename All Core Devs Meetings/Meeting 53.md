# Ethereum Core Devs Meeting 53 Notes

## Meeting Date/Time: Friday, January 18, 2018 14:00 UTC
## Meeting Duration: 98 minutes

## [GitHub Agenda Page](https://github.com/ethereum/pm/issues/70)
## [Audio/Video of the meeting](https://www.youtube.com/watch?v=45mrrVrw4x8)

## [Proposed Agenda](https://github.com/ethereum/pm/issues/70)

- Constantinople postponement
- Difficulty bomb update
- How to mitigate the SSTORE net gas metering security issue
- How and when to redo the hard fork
- Post-mortem: how did this happen? how do we prevent it from happening again?

## Meeting Summary (Key Points and Decisions)
  - Hard Fork Update: The first hard fork will be the original “Constantinople” which will include all planned EIPs.
The second fork will be to disable EIP-1283. This was decided because the full Constantinople upgrade including EIP-1283 is running on testnets. This way testnets can just do the second fork and then continue to operate.
Both forks will be triggered on the same block on the Ethereum mainnet (block 7.28 million) which should occur on February 27th.
- [Post Mortem of Constantinople Postponement](https://medium.com/ethereum-cat-herders/a-post-mortem-report-the-constantinople-ethereum-hard-fork-postponement-dd780d7ae63d)
- ProgPow 
  - There has been a lot of community feedback and a lot more testing. The Gangnam testnet has quite a few clients on it now thats getting some good hash rates.
  - Discovered an AMD compiler bug, so every once and a while when we generate these random programs, the AMD compiler just completely miscompiles it. Trying to find the root cause of this and trying and mitigate this issue and go ahead. 
  - Other feedback is that there are a number of parameters that tune ProgPow how much compute, how much memory it uses and the tuning that we set turn out to be too harsh for AMD, a little too compute heavy for some AMD hardware. Recommended to tune it down by 10 % of the compute workload. This doesn’t effect  any AMD hardware, same with the Nvidia hardware we’ve tested it on. It does help some of the AMD hardware out there in the ecosystem to keep the playing field fairly leveled. 
- PoS finality gadget 
  - The protocol is being designed so that the beacon chain will be as useable as a finality gadget for the PoW if people want to. This would basically give the same security that the original kind of pre beacon chain hybrid Casper FFG was going to give.
  - Don't expect this within 6 months. Adding the finality gadget from the beacon chain won't happen in the initial launch. We  would want to see stability on the beach chain first and then an increased security over there before.
  - Food for thought: if Ethereum would ever switch over to some ASIC friendly PoW algorithm. 
  - Hardware choice discussion and issues with distribution and economies of scale. 
- Ideas for improving the decision making process 
  - Cat Herders looking into and evaluating to see if there is a better forum and decision process for that.

Roadmap
- - a) Constantinople - what next?
- - b) ProgPoW Hardfork Decision
- - c) Istanbul Hardfork Roadmap
- - d) Outlook: PoS finality gadget on PoW chain (Serenity)
- Testing Updates (time allowing)
- Client Updates (time allowing)
- - a) Geth
- - b) Parity Ethereum
- - c) Aleth/eth
- - d) Trinity/PyEVM
- - e) EthereumJS
- - f) EthereumJ/Harmony
- - g) Pantheon
- - h) Turbo Geth
- - i) Nimbus
- - j) Mana/Exthereum
- Research Updates (time allowing)
- Working Group Updates (time allowing)
- - a) State Rent
- - b) EWasm
- - c) Pruning/Sync
- - d) Simulation

Participants: 

- Hudson Jameson (Host) 
- Charles St.Louis 
- Alexey Akhunov 
- Yoav Weiss
- AC
- Afri Schoedon 
- Alex
- Alex Beregszaszi (axic) 
- Andrea Lanfranchi 
- Ben Burns 
- Chainsecurity ( ) 
- Daniel Ellison (Consensys) 
- Danno Ferrin 
- Danny Ryan
- David Murdoch 
- Dimitry Khoklov
- Evan Sultanik (Trail of bits) 
- FJL (felix) 
- Fredrik Harrysson 
- Guillaume Ballet
- Hacktar 
- Hubert (Chainsecurity) 
- Jay Welsh 
- Josselin Feist 
- Karalabe (Peter) 
- Lane Rettig 
- Martin Holst Swende 
- Meredith Baxter 
- Mikhail Kalinin 
- Miss If 
- Mr Else 
- Mr DEF
- Neville Grech 
- Pawel Bylica 
- Ptsankov
- Stefan Edwards (ToB) 
- Vitalik 
- Wei Tang 
- Yoav Weiss 


The beginning of the meeting: 

## Constantinople Postponement

Hudson - Hello everyone and welcome to episode 53 of the Core Devs Sauga. I’m feeling tired today. 

Hudson - The first topic of discussion for today is The Constantinople Postponement 

Lane - I think you aren’t the only one who is tired today. There were some engineers that pulled all nights to make it possible so I think we should first all express gratitude to all those people. 

Hudson - I agree. Thanks, everyone who chipped in to help with the postponement, the people who were involved with the decision and everybody who reached out to all the exchanges and miners and major stakeholders to help delay the fork

Hudson - First topic of discussion regarding the postponement is the Difficulty bomb update and someone told me that the next time the difficulty bomb is going to update is at block [7,100,000] (https://amberdata.io/blocks/7100000).



Lane - Yeah, Hudson, I can jump in on this one. Just as a recap, I think that we spoke about this back in November. I did some analysis of this using a script that Vitalik wrote for the previous one and had the help of 3-4 other awesome people. The short version of the story is the difficulty bomb has already started to tick and I believe if you look at the block times we had one visible tick up so far above the current difficulty level. 

We were originally predicting that block times would reach 30 seconds in May.

So two important points: 
Since that point in time, the hash power has declined by around 20%. This means we would hit 30 second block times closer to the end of April. 
While it took 6 months for that to happen in 201, it going to happen faster this time because we at an overall much higher network hash power than we were last time. So, we still have a few months but its ticking.



Hudson - Okay, sounds great. Thanks, Lane. Does anyone have any comments on that or are we going to get to the part where we talk about when the next hard fork should be. Okay...so I think everyone knows the reason for why the fork was delayed. So we have been talking about how to mitigate or whether on not to even include the EIP in the redo hard fork. Let’s go ahead and talk about that.

We had a report from TrailofBits and ChainSecurity on some potential mitigation efforts and there is also a top page on ETH magicians that has some ideas and recommendations there. I also know that Martin and Nick have been talking about it. 

So, let’s see if Nick is online. I doubt it because it is really late for where he is…

Lane - It’s 2 am, he said he would not make it for today. 

Hudson - Okay then, could Chainsecurity go over a quick overview of what their recommendation is or just an overview of what they found.

Chainsecurity:

Quick recap what was found, the gas changes discussed especially on one of the EIPs can have an impact on previous reentrancy safe smart contracts. During the search, we discovered multiple cases with most not holding significant vlaue luckily but still deployed smart contracts that would have been attackable with reentrancy attacks after the EIP change. 

Do you want to go over the recommendations? 

Trail of Bits/Josselin F - There were 6 propositions on ETH Magicians that we reviewed as fast as possible. The first solution we recommend is to simply drop the EIP 1283. Otherwise, there is another option that is a bit better than that. Should I go over all these propositions now? 

Hudson - You don’t have to go over them all but going over the most recommended would be good. 


Trail of Bits/Josselin F - Yes, the solution is to keep gas cost that is already implemented but implement the EIP using another system. Execution is the exact same cost but it will be cheaper to use. 

Chain security - What proposal number was that? 

Trail of Bits/Josselin F - It was number 5. There was one thing that wasn’t clear in it. It was to increase the cost of writing to 5000 gas. So, it was not clear that this should be for all the data storage. That’s why in the report, we kind of created a slight version in this proposal where instead of changing the gas cost to 5000 we recommend to just use a gas cost that was pre-EIP. To keep the same gas cost computation but you change the mechanism of the storage in the case of data storage. 

Hudson - Posted the links to Eth Magicians proposals:

1. https://ethereum-magicians.org/t/immutables-invariants-and-upgradability/2440  
2. https://ethereum-magicians.org/t/remediations-for-eip-1283-reentrancy-bug/2434/

Chain security please introduce yourself. 

Chainsecuity/Matias - My name is Matias, I worked on the medium post and work on the operational side of the business here.

Hudson - Wonderful. Josselin, you are from Trail of Bits. Does anyone have comments or questions about what was just said? 


Martin S - I think its going to be a long discussion if we go into details about all of this. My preferred approach is to not include the EIP form this hard fork. If anyone has a different idea for an approach, please say it. I would suggest to only decide here how exactly they can implement it. Otherwise, we just exclude it. 

Danny - Even if we decided on updating it today, would the testing and reconfiguration of the fork with code changes be reasonable in the context of getting this out for the difficulty bomb. 

Martin S - If we make any modifications to it that would add a lot of test complexity. If we drop it, that's a lot less testing 

Danny - In the emergency call, we had a tentative consensus to leave it out.


Hudson - Yeah, we should talk about whether or not to include it rather that what the right decision is. Any other comments? 

Alexey - Agree. Simplest way is to exclude it. The #7 proposition was to reduce the desired effect of the EIP because of the cap. That exists for the funds. So, its not the exact replication of the semantics. Its slightly less, so less powerful to change.  

Hudson - Anyone else have comments? 

Yoav - About the comments on the #1 proposal. I dont see how it breaks anything we desire to have when it preserves the original intention of the EIP including its benefits and doesn't break any scenario that’s lacking. So can you please elaborate on this…

FJL - Something about the proposition #1 now which is adding a condition that causes it to revert if less than 2300 gas remains. 

Yoav -  Yes because even before the EIP it would cause a revert anyway so it doesn't change that behavior and when you do have enough gas you do get the benefit. Then you dont have to deal with complexities (ie: refund limit). So, its essentially a one-liner fix. So why do we need anything more complex than that? 

FJL - People are thinking about options that exist. Its not straight forward because adding this particular condition is weird. Its elegant but there is a lot of other things that could be done. We all want to reach a conclusion where the proposition thats accepted is not super ugly.

Chainsecurity - When we investigated this we also found that several smart contracts out there had higher gas limits, pass on to other calls, which makes it also depend on which version of the solc compiler was used at that time. So those existing contracts may still be attackable and additionally, it would enshrine into the sematics of Ethereum. That being the workarounds that happened because of the way people used it for some time. Lets say in 5 years, when people ask about the codes today, and they say why does this yellow paper version 5 have this case of “if < 2300 gas do that” which is what we would have to carry along...

Yoav - Yeah. Keeping a log of the reasons behind such decisions is essential anyway because then maybe the whole problem could have been prevented. If we think about why exactly we had the limits in the first place, we should remember this regardless of the decision choice but if we change the gas limit we also need to think of another gas limit. This will affect miners etc…

Alexey - To answer your question, if we make a thought experiment and move ourselves to a situation prior to this. Lets say we are deciding whether to include this EIP a couple months ago and somebody said we knew about this vulnerability and one of the propositions was to add this check about 2300 gas. Would we accept this workaround? Probably not. So why do it now? We don't need to rescue the main chain from this so we are basically by not doing Constantinople, we brought ourselves back to the situation where we want to be so we can have the freedom to make this messy change or not. 

Danny- Makes sense. 

Lane - I want to second what Danny said before. Let’s focus on how to move forward with Constantinople and if we should include the EIP or not. Does anyone strongly oppose to moving forward without the EIP? 

Danny - Let’s get consensus on that. 

FJL - I think its a useful EIP and if we keep the discussion time-based it would be good to talk about how we can change this EIP so it can still be included. Im opposed to moving forward without it. If we take it out, the HF will be less of an improvement. 

Lane - Why is that a problem? 

FJL - HF’s don’t happen every week. We dont have a lot of chances for upgrades. The next one will be what, 6 months from now?

Lane - Good point. Maybe we cant answer that first question without answering the second. I think Afri can speak to the timeline as he tentatively proposed October which isnt far. 

FJL - Mhm, yeah. Maybe you are right. In any case, maybe people feel like if we can come up with a solid fix to this EIP in 2 weeks and its clear to everyone that its a good fix, that it may still be possible to include it. 

Afri - I would say no because if we change this EIP, we have to change its implementation and tests. This means we may want to test it on a testnet first and we cant do that in a couple of weeks. 

Martin - I agree . A modified implementation would take months of time for testing. Dropping it, we can do that quickly and moving forward as is, we could do that too if the analysis had shown that we are certain no contract is affected. But, we aren’t there yet. 

Alex B - Would a scenario be realistic where the EIP is not included but the hard fork is made within a few weeks and then 3 months after that a properly designed version of the EIP is launched? 

Peter - I think if we postpone this and take it out of the hard fork and want to add it back at some point, then it has to wait until the next hard fork. Im opposed to doing emergency hard forks just to get this feature back in 

Afri - I couldn't agree more. So now we need to go get a fixed HF schedule that means we have at least 2 hard forks a year scheduled, which is 2 more than we had last year, so whats wrong with waiting another half year? I dont think we should have hard forks every 3 months. It's too big of an overhead for the client developers. 

Alex B - October is not half a year from now. 

Peter - That's not what we debated. 9 months seems to be a reasonable amount of time to get features in and to test it. So by doing one in 3 months, we are breaking everything we talked about from before. 

Chain security - Perhaps not. So how many months before a hard fork do we need to agree on all EIPs ito include? How long would be the review/test phase and so on…

Hudson - Afri had a scheduled timeline for that stuff I believe. 

Afri - Yeah, Im working it out. What I was proposing was before we discussed ProgPow and before we had this incident. I was proposing a timeline for subsequent hard forks. So after a hard fork like Constantinople, I want to schedule another hard fork 9 months after it, which means we have another 3-5 months before the hard fork then the client teams have 1-2 months to implement and then test the hard fork before the scheduled date. 

Chainsecurity - Understood, thank you. It might be interesting to add a specific time to test and try to break it and see if Ropsten does diverge. 

Hudson - Yeah, there is another conversation about what to do with future hard forks and EIP inclusions and what security measures to take. Martin has been looking at that from an audibility perspective.

Chainsecurity - Asking because of the timeline and implications of it. 

Afri - No, what I am suggesting are deadlines. For example, we cannot have the testnet hard fork within 2 months because we need 2 months on a stable testnet and then another 6 weeks for releases to be posted for the users. Thats the proposition, doesnt mean nothing can happen in parallel. 

Hudson - So, Felix has your opinion shifted in any way from what we just discussed? As far as potential deadlines go and how long until the next planned hard fork would be. 

FJL - I just feel Im way less professional that all of you are when it comes to making changes. If you guys feel its best to be conservative with time, its fine with me. Its safer this way. 

Hudson - Is there anyone else opposed to taking out the EIP and having a hard fork in 2-6 weeks? We also need to figure out if that’s the case, how long until the next hard fork. Afri, have you looked at that? 

Afri - How much time do we need to prepare another hard fork without this EIP? 6 weeks is optimal to push releases fro the clients and do testing. Any other opinions from testing teams?

Lane- Peter had an interesting proposition for what to call this and how to update mainet relative to the testnets

Ben B- If it helps the decision (truffle) we are close to have a verse of ganache that has the GP removed for testing

Martin- I am curious if Dimitry is on the dall. How long would it take to modify & regenerate the tests?

Dimitry- If we remove, we need to regenerate the tests for the client

Martin- Are we talking about a couple of days? 

Dimitry- yeah a couple days. TO make sure all clients are updated publicly. 1 week.

Martin- Couple days for tests, then client devs can use those tests to verify their own clients and after that there will be live tests

Peter - I propose an alternative. This would change the hard fork because we remove EIP from it and regenerate every test as if it did not exist and remove from clients, the problem is Ropsten and Rinkeby already forked over. If we wipe it, we break all networks that already have this feature. This will kill Ropsten and Rinkeby.

Proposal→ instead of removing, we define a second hard fork that only removes this code. So even clients would have testnet capabilities. So leave it and then fork it and then have another hard fork that disables this code path. These two hard forks would trigger out the same block number. This allows for a clean upgrade and cleanly disables the EIP without rolling back. This will just take a couple of new tests.

Alexy- I would add that later on when we reset all the testnests then we simply remove the code

FJL- You would need to be able to reprocess the time between
Alexy- It would only apply for testnets so if we reset all testnets because too big, we simply remove it.

Peter- Need to reach out to the community to make sure no ones private network gets broken

Afri- A few enabled it, including Kovan

Martin- If we go with Peter’s idea, would this affect the test process?

Dimitry- Please clarify what this means again

Peter- We define 2 hard forks, one of them is Constantinople and the second is fixed up with the disabled feature and they would trigger on the same block.

Dimitry- What’s the difference? If they are happening on the same block

Peter- We don’t want to kill all testnets that have already upgraded. With two hard forks, those who already upgraded can have a second hard fork in order downgrade

Alexy- Saves time for fork prep and can get Ropsten alive quicker

Dimitry- Tests would look the same

ChainSecurity- Unless we have some client feedback that is using Ropsten in a semi-productive manner. We need to be careful. Don’t want to underestimate the time needed to verify if it works off of an empty testnet

Afri - From Parity’s perspective, Peter’s suggestion makers perfect sense (good fix for PoA’s)

Peter - Doesn’t matter how we go forward with mainnet but if we want to move forward with Rinkeby and Ropsten then Parity and Geth needs to implement another hard fork anyway.

Dimitry - If the Constantinople block # is the exact same for mainnet it doesn’t make a difference but for testnets you could use different block numbers to help the transition

Martin - From the testing perspective, there is not need if we are tied for time to have test cases for EIP 1283. 

[Ideas for names]  

Dimitry - Do we have names for these forks?

Peter - Constantinople was defined with these features and if we create a new name fork that disables this then we retain the same name. For Geth, we have named forks so Rinkeby Constantinople would be different. 

Alexey - Call in ConstantinNOPE 

Peter - The name should make sense for mainnet, something meaningful 

Chainsecurity - Consider how the public would view it. Consistency is good 

Lane - Where did previous forks names come from?

Hudson - Martin made them while we were goofing off

Lane - So what we call it and what goes into the code doesn’t need to be the same.

Afri - Lets not focus on names here. The community should do this in the future, on ETH Trader. 

(Block number decision) 

Hudson - I like Peter’s fork idea. Anyone opposed? Peter’s idea it is! So these forks will happen at the same block number in approx 6 weeks?

Vitalik - Can we calculate it right now? What is it now? 

Lane - 7,087,616

(Calculations with conisdersation of difficulty bomb) 

Vitalik - Should be around blocked 7.3 million. Past that would be inconvenient for people.

Lane - I will run simulations with the difficulty bomb

Vitalik - We need to see what block number it would be because right now block times are increased by 9% from the ice age. 6 weeks would be 2 more steps away form ice age which would push times to 21 seconds. If we do 3 weeks, then we could avoid a big step like that.

Hudson - 3 weeks is too soon. We need more tests and more client coding. 

Lane - Dimitry said he only needed a week or two. What about 4 weeks?

Danny - Presumably we need to deploy Constantinople to one or two testnets first.

Vitalik - So between 7.25 and 7.3 million

Hudson - 6 weeks is best. Anyone opposed?

Peter - Quick memo - Ropsten is independent of this. So with 2 different hard forks we can update Ropsten and testnets whenever.

Danny - This is a hard fork so we should update it 

Hudson - Lets decide the name and block number on the chat. Roughly 6 weeks from now and stick with the convention of quad zeroes. 

---

## Post Mortem

Hudson - So how do we prevent this from happening in the future? Id like to bring in Charles St.Louis to talk about the post mortem being created. Charles is with the Ethereum Cat Herders and he was around for the entire time of the incident. He took some good notes and during and after the decision process and the Cat herders are working on a post mortem. 

Lane - We haven’t introduced the Cat Herders yet. Introduce us! 

Hudson - We have a group set up to help out with coordination and PM work. How would you describe it Lane?

Lane- An initiative to improve PM over the ecosystem and improve inter-team comms. I’d add that this team has people with many years of real work project management experience and this is something the community has been lacking. I think we will see some exciting things from them. 

Hudson - Afri will be the hard fork release coordinator and working with some cat herders to help him organize. Charles, want to talk about the document?

Charles - Yes! I created a doc to highlight the decision process for the postponement. I pretty much just walked through the whole process (on Gitter/emergency call) and structured it into steps. I’ll like the doc in the chat. It mainly goes over the steps of the process: 
1. Identify the threat 
2. Factors involved in deciding to postpone or not
3. Emergency Call with Ethereum Stakeholders
4. Decision Window for aborting network upgrades 
5. Emergency Security testing analysis/scanning 
6. Proactive and Retroactive Actions for the postponement: 
7. Do we feel confident that we can get every stakeholder notified?
8. The Decision
9. How to best communicate the decisions to everyone (comms, blogs, social, yelling, etc..) 
10. Deciding to remove the EIP or fix it? 
11. Rescheduling the fork

I put it in the doc in chat for comments and put my email there as well. 

Hudson - Anyone else working on a post mortem?

Peter - I dont but I want to bring up something discussed after Byzantium as we had a similar situation. Where we had a similar situation where we had to do many last minute releases. The fuzzer found bugs. We talked about it a while ago but we talked about having an on chain oracle to pull the plug on a hard fork. We dont talk about this because its a pain point but we need to. Do we want this?

Danno - What about instead of a centralized kill switch, each client maintained there own decision and coordinate it but only respect their own kill switch contract.

Peter - That would be messier and its the same level of centralization. If you had a contract with clients having the same vote..then the majority can postpone the fork. That’s the cleanest. 

Lane - Parity’s already has an auto upgrade feature and its opt-in. Opt- in is best. 

Ben Burns - Its important to state the intent, which is to make the decision whether or not to go along with hard fork. Automated switches may not be acceptable. 

Peter - Problem is Geth also had upgrade oracles where it bumped number in smart contract and started logging messages to the console that there is a new version or something. The issue is people dont check their logs all the time. 

Ben Burns - If clients were implementing a config. Option, that makes perfect sense that the clients are able to still watch but can opt. Out of it consciously. Point is, its not really a centralization mechanism if there is a conscious decision going on 

Peter - Agree. The client would signal to the user that there is a decision and ask if they want to opt-out. Is it viable for nodes to signal? Anyway, I brough this up because its not a simple solution and if we can solve it well, it would be welcomed and in the long term we need to address this. 

Ben Burns - Last thing, I want to clarify that opt-in would be an ahead of time thing. 99.99% scenario to opt-in to what the group's consensus is if im running a node. So Id be happy to flip the flag in my config. Ahead of time or flip it back. Puts the diligence on me.

Peter - Agree. Opt-in is preferred.

Hudson - Let’s iterate on those ideas later. 

Lane - On a side note, I re-ran the simulation. It looks like we hit 30 second block times at the end of April (April 17-27). So if we want 6 weeks from now, we want to target the end of February so that puts us at block 7.3 million. 

Vitalik - March 2nd is more than 6 weeks, maybe block 7.28 million?

Lane - So Feb 26-28th.

Afri - 27th because its midweek

Lane - I’ll figure out the block number. Its going to be harder to pick a day given the difficulty bomb changes. 

Peter - Wednesday is good on the 27th because even if there is a 2 day delay, its still a workday. 

Hudson - Anything else we need to talk about with respect to Constantinople? We’ll be naming the 2nd hard fork in the chat and Afri said Eth Trader could name it. Afri, for the road map planning, is there any other questions or points you had for Constantinople?

Afri - No. 

Hudson - Next topic if ProgPow. 

---
## ProgPow 

Hudson - We have Mr Else, Mr Def and Ms IF here which is awesome. Before we go into the hard fork chat, we tentatively decided that last meeting but the community has had some feedback since then. Have any of you responded to the feedback yet? Any updates or comments from you three? Also, let’s re-discuss ProgPow here. Please start out with your updates...

Mr Else - In the past two weeks, there has been a lot of community feedback and a lot more testing. The Gangnam testnet has quite a few clients on it now thats getting some good hash rates. One interesting thing that came up was that we have discovered an AMD compiler bug, so every once and a while when we generate these random programs, the AMD compiler just completely miscompiles it. The AMD hardware will give bogus answers for an entire period. The next period when you get a new random program, it compiles it correctly. Our team is enaged along with some of the miner developers with some AMD engineers to try and and root cause this an try and mitigate this issue and go ahead. 

Some other feedback we got is that, there are a number of parameters that tune ProgPow how much compute, how much memory it uses and the tuning that we set turn out to be too harsh for AMD, a little to compute heavy for some AmD hardware. We recommend to tune it down by 10 % of the compute workload. This doesnt doesn’t effect  any AMD hardware, same with the Nvidia hardware we’ve tested it on. It does help some of the AMD hardware out there in the ecosystem to keep the playing field fairly leveled. 

I think thats the only major updates.

Hudson - Does anyone have any comments or questions? 

Dann0 - What’s the preferred channel to give this feedback?

Mr Else - Eth minor dev channle has become an unofficial channel. We will start our own gitter channel. 

Danno - Whats the authoritative specificiaiton locations too? Bc there is one on the EIP, there is one on if def else. The test case is out of date on the if def else 

Mr. Else - Oh, it should be up to date. I’ll make sure it gets fixed if it isnt. 

Danno - I have many questions like this so a formal channel would be great. 

Mr Else - A gitter for IF Def Else will be best and Ill start that tirght now. 

Hudson - wonderful, any other comments or quesitons? I think the biggest comm feedback lately was that this decsion was rushed and not enough time for discussion and the biggest concern was that the AMD video cards are effected.  So I’m glad ya’ll are fixing that with AMD. GOod work there. Any other proposals to change this tentative decision? Bc as of now we are going forward with it. 

Martin S - Yeah I have some comments. Been some discussion about progpow claimed features and there is a question that is is following those claims which is a very technical discussion. The other idscussion about these claims, the ASIC resistance relies on the assumption that we dont want ASIC on the network and if it is worth striving for. I personally assumed that is what we should aim for, bc that was an early goal of eth hash but it appears that this is not a tech issue but a poltical issue. Should we strive for ASIC resistance and if we should, how much pain are we willing to go through and is progpow the best way to reach that? I believe so btu willing to hear other points..


Mr Def - I’m coming from the perspective that we eventually want to end up off of proof of work entirely and that's one of the motivations for developing this. If that is not the direction we are going in I think some of this discussion becomes less interesting. Assuming we want to move to a system that we are not going to be doing PoW, I think the most empirically stable system that has been the status quo that you can observe from the last two weeks, after the initial tentative consideration of the progressive proof of work what it motivates those possessing hardware on either side, being the existing the status quo (GPU) or with those who are making or having made ASICs. How that motivates the convo, from taking not productive angels, if you will. I think that is just the exact negatively that we are trying to avoid. I think the problem we want to help with is to minimize the economic incentive alignment of the particular hardware holders or hardware ecosystem to the development of the network as a whole. I think its important to preserve the independence and the ability to have the ETH core devs continue making progress in tech and advancements in the network and it's unfortunate if the network hash and security model becomes unaligned to a particular type of system or specific set of owners or miners. That said, there are even problems with the status quo. With AMD and Nvidia, there also may not be enough particular brands or makers of the existing of the GPU ASICs for the network and we may have particular economics misalignments there. Given that, I think the existing status quo also already has the least “evil” approach bc it is the most distributed hardware compared to any other ASIC available or even FPJs. In terms of the economies of scale, in the ASIC economy and distrbuted. It is aligned to a wide and massive distribution availability. Its the fairest for availability and price. That was the starting point for the development and rationale for working on this. Beyond that, I don't think the goal is to try an win for one particular hardware or another bc I don't think hardware should win in the end. I can understand that this may be an unpopular opinion or a negative thing for current hardware users/ ecosystems. I just hope we can contribute to the independence of Ethereum development. 

Hudson - Okay, thanks for that. Anyone else have comments or questions? 

Alexey - I have more of a statement. Overall, I don’t know how people perceive these meetings in terms of making major decisions I would like to say that I am abstaining from making a decsiion and so my silence should not be couldn’t as a for or against statement. I don’t think this call is where we should make this decision. I’m not as informed or aligned with any of the ASIC or non ASIC sides as some people may have suggested because of my activity in terms of discussing it, My point of view is that I have taken on the taste of developing and designed one of the parts of ETH 1.x which is the state rent and I do understand that more hard forks we do have planned, the harder it will be for us and me personally it will be to get this job done. Therefore, this explains my interest in the issue. Otherwise, I'm not interestedin arguing with miners or ASIC manufacturers. I also want to say that although some people say if you don't like the HF you don't have to do it but this isn't the best advice bc it depends on the entities that fund the development. Whoever does the fork, the EF possesses the ether on both sides of the fork and whatever they choose to do with that then its determined the chances of any of the forks winning. This is why I think we need to rethink the decisions processes.

MR. Def - I’d like to also jump in and back that point up. In principle, I also agree with less forks. Just an observation I think more forks is not just hard for devs but also causes discussion and churn. Anyway, to the extent that there is many much earlier threads saying that if a PoS could be implemented in the short term, we should go to that. I agree with that and if ProgPow is only going to be in effect for a month or two before everything else is ready in PoS, then there is kind of no point and an extra fork is not a good thing. With that being said, if the dev team of the folks meeting here   that there is a longer more arbitrary amount of time to get PoS working, then I think one of the mechanisms that is built into ProgPow is in effect basically a bunch of microscopic forks that are not hard forks. Its actually the evolution of the algorithm or the changing of the random math and the recompilation is basically changing the mining algo in currently a 50 block step, maybe we can change it to a shorter time. What would people do to do a basic resistant forks. That is the mechanism that underlies ProgPow, it helps to eliminate the need for algo forking for the mining algorithm. It maintains it and we just do a bunch of continuous forks all the time in a predictable and well understood manner. 

### PoS finality gadget 

Hudson - With regards to that, the next thing, if we have time to discuss, was going to be the PoS finality gadget on the PoW chain. Danny or Vitalik, do ya’ll have any word on how fast things are coming alone or timelines?


Vitalik - One thing that is relevant is that we are designing the protocol so that the beacon chain will be as useable as a finality gadget for the PoW if people want to. This would basically give the same security is that the original kind of pre beacon chain hybrid Casper FFG was going to give. That’s something that’ll be out and not focusing on timelines before sharing and before state executions. So that would basically mean that if that happens everyone is listening to the PoS system pro finality and if enough people are participating that its actually secure then a 51% attack on the proof of work will basically be able to censor but it will not be able to revert anything finalized. 

Peter - Are we not talking about the 6-month timeline? 

Vitalik - Yeah, no realistically we don't expect this within 6 months
 
Danny - Adding the finality gadget from the beacon chain won't happen in the initial launch. We would want to see stability on the beach chain first and then an increased security over there before.

Vitalik - Part of the beacon chain code immediately its just no one would immediately listen to it. 

Danny - Correct but the follow distance that the beginning would also be very long so we would also want to reduce the follow distance. 

Vitalik - Yeah, that’s true 

Mr. Def - Vitalik, Id like to ask your in terms of the sensor and not the reversal comment. If you have persistent censorship for some percent of the blocks being censored, censoring a certain type of operation would the chain have to basically be less effective at that point and cause a crisis anyway if there is censorship.

Vitalik - If there is a censorship 51% attack and if the attacker is persistent, so the attacker doesn’t just go away on their own after the attack after one or two days or whatever then basically if we can only do (if we know they have ASICs) we could change the algorithm to cancel their ASICs but if it is a 51% attack that is run based on GPU hardware then we would really have no choice but to scramble as quickly as possible to some kind of Pos. 

Danny - Or just change the algorithm entirely

Alexey - there is another avenue, I’ve been about it and researching the ways to best avoid this situation regardless of what kind of miners we have. I read a thread in the BTC reddit who runs a mining farm in the US, he proposed to modify the fork choice rule (in that case for Bitcoin cash) but in our case it could be in Ethereum 1.0 so that in the lone term it could converge to converge to the same fork choice rule but in short term it could favour the blocks that are not censoring or the blocks that arent trying to revert. So even if the attacks didnt have ASICs, they would still be beatable if the network agrees that the attacker is still censoring because they could compare the transaction pool with the blocks and they can figure whether the censorship is really going on. 

Vitalik - That works okay if the goal is to prevent short term 51% attacks but if you try and turn banning censorship into a fork choice rule components then thats starts to become scary because an attacker network splitting attacks where they can censor just enough so that half the network thinks its not fine and at that point the attacker can start reeking a large amount of havoc. So I would recommend not trying to go in that direction. The only version of that situation that I would find secure is probably something based combining the 99% fault tolerance consensus approach which requires telling clients and all the nodes in the network to be online with PoW in some way. This could be possible but properly researching it and spec’ing it would take a large amount of time 

Mr. Def - I want to jump back to an earlier point about GPU vs. ASIC 51% attack. Ethereum is currently resistant by the virtue of it being the biggest coin/consumer on the GPU type of ASIC and in any case or any sort of hardware specific algo or an algo that can be made optimized for a specific type of hardware. Only the biggest work consumer that consumes the most of that hardware is ever protected. So by changing that algo to another algo, whatever hardware affinity it has, the algo selection would only be protected by a 51% attack if the algo selected was the biggest work consumer on that new type of hardware and if you forked to a new algo that requires a new hardware to be made, first of all, that algo would most likely be mined on something programmable. Perhaps FPJs, so if it was originally attackable it would still be attackable on programmable hardware. If it was forking to some sort of optimized ASIC algo, then you immediately run into a distribution problem where the first to produce gains economies of scale and leverage and also limits the ability to scale hardware. Distributing hardware means shipping it somewhere, so this is a narrowing path that can become dangerous. 

Vitalik - Sure, yeah.

Peter - So that’s food for thought. If Ethereum would ever switch over to some ASIC friendly PoW algo, for example, an elegant solution would be to announce “Hey, one year from now or two years from now we are going to use this ASIC friendly algo” This gives everyone time to sort these problems out. 

Mr. DEF - Yeah, I’d like to speak about that a little bit. I think another person in the community has talked about economies of scale and it's an important point that we all understand. The same person referred to the manipulation in terms of partnerships in hardware manufacturing in China and both of these problems are very, very real.  So economies of scale obviously, means first in you have the advantage to leverage additional profits from the initial sale. So whoever is most efficient, basically has a pricing advantage and a manufacturing advantage for whatever initial partnerships they have started. We are all familiar with the first-mover advantage. In terms of production in Asia ecosystem, once you have established money making path these relationships become very well cemented.  So even if they have equal technology or equal efficient ASIC, the natural evolution of the production economy is you have a dominant producer, a second competitor, and all the others fall terribly far behind. This goes for any product out there. The consolidation occurs very early on and especially for narrow demand and very specific purpose demand. You end up with a very tight alignment of economic incentives to preserve one particular path. Furthermore, you have manufacturers that always end up with a technological advantage either in the ability to optimize for complexity or in being able to drive to a lower process node faster or economies of scale advantage. Its always going to be the case. In a hardware ecosystem, you cant pick your poison, all of t the choices are poison. 

Hudson - Okay, so we have to wrap up this call in a minute or two. But feel free to wrap up your final thought right there. 

Mr. DEF - Okay so, Im pushing for the status quo. If you have an ecosystem that you already know is distributed it is the enemy you know. Its already stabilized and dealing with all these damages and difficulties of a hardware ecosystem and ameliorating that because those incentives arent aligned to trying to manipulate the Ethereum chain. They are trying to win a different market. 

---
### Ideas for improving the decision making process 

Hudson - Cool, thanks for that comment. There is one more thing I wanted to mention before we sign off. Alexey mentioned earlier that this is not the best forum for decision for ProgPow and I actually agree with that. I don't know of a better forum but  that is something that the Cat Herders said they want to try look at and evaluate and see if there is a better forum and decision process for that. If anyone has any better ideas please feel free to put that in the AllCoreDevs call. That would be very helpful. Also, the people who arent commenting on the call on the ProgPow decision or tentative decison is because they haven't formed an opinion or its out of their wheelhouse as far as this hardware stuff goes. I think that its kind of important to keep in mind that we will need to continue this dissucuion in the future. I don’t know if it will fit into the next core devs call or not but we’ll try. I do want to thank IF DEF and ElSE for coming on and providing their perspective and answering questions. Do we have any final comments to just wrap things up? Do we have any other comments, I know we are over time but if anyone had anything they wanted to say now is the time. 

### Final Comments 

Afri - Sorry Hudson, I’m jumping back here but wouldn’t it be nice if we could agree on a block number for Constantinople today. 

Hudson - Yeah, Lane put some numbers in the Gitter. 

Lane - Yeah, I'm proposing 7.28 Million. The simulation changes slightly depending on two variables which are the network hash power which could change between now and then as well as the current block time. We did some sensitivity analysis and it looks like 7.28 million gets us pretty close to the target. We can go with that as a tentative number for now and once all the clients are updated we can reevaluate in like two weeks.

FJL - Why not do the thing that was suggested a while ago and base the fork off of the block timestamp. That would be even more helpful 

Afri - I can tell you because its a lot of change to do to the clients and its a lot to do in a couple of weeks

Peter - There are also some weird corner cases that could happen after the fork. Where it could cause a post fork problem where a block might have some weird uncle blocks with weird time stamps. So validation gets really messy. 

Hudson - I’m good with the block that Lane just suggested. Anyone opposed? 

Peter - Can we also figure out the block for Ropsten then. Maybe a couple weeks before that?

Hudson - Yeah, let's decide that in the core devs chat unless you have numbers ready or a suggestion 

Peter - Nope, let's do it there

Hudson - Okay, so we are over time now and we want to respect everyones time. Thanks everybody and we will talk to everyone on the next call. Thanks, everyone, bye! 

/End Meeting
