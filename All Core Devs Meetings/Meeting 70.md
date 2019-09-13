# Ethereum Core Devs Meeting 70 Notes
### Meeting Date/Time: Friday 06 September 2019 at 14:00 UTC
### Meeting Duration: 1:30hrs
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/123)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=6m0So81_j2Q)
### Moderator: Hudson Jameson
### Notes: Brett Robertson
	
----
	
# Summary
	
## DECISIONS
	

**DECISION 70.1**: Leave Blake 2 as Blake2b, keeping it fixed to 12 rounds.

**DECISION 70.2**: The fork of the Ropsten Testnet is set for the 2nd October 2019 and block that corresponds closest to that date will be selected.

**DECISION 70.3**: 

**DECISION 70.4**: 

## ACTION ITEMS

**ACTION 70.1**:  Alex Beregszaszi and EIP-152 Champions to discuss the Alex’s concerns around Blake2b after the Core Dev Call.

**ACTION 70.2**: Ethereum Cat Herders to create a communication that highlights the concerns around EIP-1884 and provide it back to the All Core Devs for review before it is put out to the community.

-----

## 1. [Istanbul related client updates](https://notes.ethereum.org/@holiman/SyT_rGjNr)
[Timestamp - 04:37](https://youtu.be/6m0So81_j2Q?t=277)

### Pantheon

- All Merged.

### Geth

- All Merged. 

## Trinity

**Jason**: 
- There is an issue. It is working but it is too slow. 

## Parity

**Wei**: 
- We are going to wait to discuss Blake F before we hit the merge button.

**Martin**: 
- I have added Genesis activation support to the Istanbul tracker. This is important for testing. Please can everyone look to include this in their clients.

## Aleth

No one available to speak on Aleth.

## Nethermind

**Tomasz**: We are all ready and are just waiting on the tests.

## 3. [“Patch proposals” for Istanbul](https://github.com/ethereum/pm/issues/123#issuecomment-528506546) 
[Timestamp:7:44 ](https://youtu.be/6m0So81_j2Q?t=464)

### Blake2

**Alex**: 
- There appears to be some confusion because the EIP uses different names. 
- Initially it was called a Blake2b precompile then it became a Blake2f function. Then it turned into a Blake2bf function and all of these terms are used interchangeably. 
- But it turns out that the EIP right now only focuses on Blake2b specific configuration of Blake 2 and Blake2b specifies the rounds to be 12 - which is fixed. 
- The configuration of Blake2b has 12 rounds, it has a specific initialization vector, a specific set of round constants and a specific buffer size.
- The EIP even though it specifies the F function it is an F function specific to Blake2b.
- In the end I don’t see the round argument as it has it already set at 12.

**Jason**: 
- Should we reduce the round thereby reducing the bytes and is there usefulness in the F function if it is set to 12 rounds? I don’t know how this will work but those with familiarity are saying they want the functionality to change the rounds.

**Alex**: 
- The confusion is that if you have a fully flexible F function then you would need the number of rounds, the initialisation vector and the parameters which the current EIP does not have. If you want to only support Blake2b then the EIP is fine. If you want to change the rounds then you won’t have Blake2b any more and Blake 2 configuration. There just does not seem to have any reason to keep the rounds parameter if don’t introduce the other parameters to Blake 2.

- Some background; 
- Blake 2 itself is a flexible hashing framework, it has a configuration part.
- Blake2b and Blake 2S are specific configurations of the Blake2 hashing framework.
- If you change any of these parameters you will get a different hash.

**Hudson**: 
- Having looked at the EIP as of 17 days ago the people who reviewed this said that it is good to go. Sounds like they only want Blake2b. Is this accurate? 

**Louis**: 
- From Starkware’s perspective we will not be able to use the precompile as it is way too expenisve compared to Keccak.
- But at some point if we could use Blake2x that would be useful for us because we don’t need an output of 256 but we need an output of 180 and being able to make changes to the hashsize would be useful to us in the long run.
- Basically as it currently is it is unusable but if there was an option for a more generic option in the future that would be useful.
- Also, from Alex perspective would Blake 2S be as secure as Blake2b and could we use this?

**Alex**: No.

**Louis**: 
- It that case to avoid delays we should just leave it as Blake2b and simply rename it to Blake2b.

**Hudson**: 
- Making it generic would certainly delay things.

**Martin**: 
- From a testing perspective, formatting it or dropping the rounds would not be a big issue for testing, we simply need to modify the test vectors a bit.
- If however we were to add something or make it generic then we would need to invent new test cases.

**Tomasz**: We agree just remove the F function and call it Blake2b. The changing of rounds does not seem worth have the F function. It complicates it. We can always add a new one later.

**Jason**: 
- Key reasons for flexibility as listed by Zooko include:
- Blake 2 Key
- Blake 2 X
- The ability to change things in the ZCash protocol.

**Hudson**: 
- It may be worth noting that in the future people may want that extra flexibility but we cannot guarantee that we will create another precompile. 
- But that will have to be after Istanbul.

** **
**DECISION 70.1**: EIP-152 is specific to Blake2b, that is it is fixed to 12 rounds.
** **

**James**: 
- In terms of history of this EIP, we spoke with Zooko and a few of the ZCash guys. We did not have a ton of resources for implementing something that has the hash function and then if there were any needs going forward we could implement them as required.

**Alex**: 
- The tfields are the offset counters, .a.k.a. the bytes already pushed into the hashing function. I am happy to keep things as it is as long as we properly explain that this is 128 bits because this is Blake2b. 
- The second thing is the length field for the message which is a gas optimisation in the EVM. The last block has to be zero pedit. To avoid issues it would be much easier if we could supply the length field for the message.

** **
**ACTION 70.1**:  Alex Beregszaszi and EIP-152 Champions to discuss the Alex’s concerns around Blake2b after the Core Dev Call.
** **

### EXTCODECOPY

**Martin**: 
- I don’t see an issue with this for now.

**Wei**: 
- We should not do any more major changes to the EIPs. It will only cause further delays.
- We need to avoid backward incompatibility changes in the future.
- We need to improved the EIP management procedure, with the growth of the community, we could potentially implement an backward incompatibility change that would create some sort of attack vector.

**Tomasz**: 
- Last call Wei raised an important issue around EIP-1884. 
- I agree the change is very important to introduce for the reason’s stated by Martin. 
- We need to ensure the that person raising security concerns does not feel the pressure from the community to ignore them and simply merge.
- EIP-1884 will cause issues with Aragon and other contracts and we need to ensure that these issues are addressed for most parties before the implementation of EIP-1884 in Istanbul.
- I have seen a list of contracts that could be affected and the list is long. I also don’t believe all the owners of contracts is tracking this. It is speculation but it remains a concern.
- I would like to discuss a proposed change to EIP-1884 that introduces a counter that treats the for 2,300 gas on stipend differently. I see this as non-invasive in terms of the way it affects the performance and memory requirements of the clients.
- I would like to discuss this as I don’t believe enough people read the proposal and I believe it solves the problem without risks. Taking the fact that 9,000 gas is required for any value calls avoiding the attack vectors leaving the SLOAD under priced.
- So we can raise the price of SLOAD and at the same time secure, for the time being, all the contracts affected.

**Hudson**: To be clear this would need to be prepared for Istanbul in order to be effective.

**Tomasz**: 
- Whilst I agree I am not keen on making changes to EIPs so late in the game I feel this change provides an easy solution to a problem that affects big contracts like Aragon.
- I believe without implementing this change we lose trust within the Ethereum, that we can implement EIPs that we knowingly breaks contracts.

**Martin**: 
- In my view the proposal is overly complex, convoluted and not properly analysed.
- I would think it would be very optimistic to squeeze this change in for Istanbul.
- I also believe that if we post-pone fixing it we will make a better job of it.

**Hudson**: 
- If we make a commitment now to fix any contracts, including time locked contracts, then this is a commitment we are making before anything breaks. 
- I believe with the right amount of PR behind this it will be ok.

**Martin**: Caveat that if a contract simply needs to upgrade then that path should be followed. If however some Ether is stuck in a contract then we will assist with fixing it.

** **
**ACTION 70.2**: Ethereum Cat Herders to create a communication that highlights the concerns around EIP-1884 and provide it back to the All Core Devs for review before it is put out to the community.
** **

**Tomasz**: I would like everyone to properly review the proposed change to fix EIP-1884. If every reviews it and they agree that they will still want to go ahead with EIP-1884 then I am happy to go with the consensus.











## 4. Decide block number for Istanbul testnet/mainnet
[Timestamp 53:57]( https://youtu.be/6m0So81_j2Q?t=3237)

**E.G.**: 
- Suggest we set block number for Testnet fork first before we look to set the block number for the Mainnet fork. 
- If we have a period of stability then we can set the Mainnet fork.

**Hudson**: Today we will therefore select a testnet block number.

**Martin**: Assumption that all clients can release their next update by end of next week.

**E.G.**: Would suggest a 2 weeks from last update.

**Tim**: Be conscious that if we leave it too long then we could hit DevCon.

**Martin**: Perhaps 2nd October we could fork the testnets?

**Tomasz**: 
- Perhaps we should stagger the changes, starting with Rinkeby which is only produced by GETH so there will not be any consensus issues. 
- Followed by Ropsten which has only two miners.
- The continue with Goerli which has 4 different clients creating blocks.

**Hudson**: It is a good idea but we would need to ask the teams running Rinkeby and Goerli perhaps at the next call.

** **
**DECISION 70.2**: The fork of the Ropsten Testnet is set for the 2nd October 2019 and block that corresponds closest to that date will be selected.
** **

## 6. [ProgPow Audit](https://github.com/ethereum-cat-herders/progpow-audit/blob/master/Least%20Authority%20-%20ProgPow%20Algorithm%20Initial%20Audit%20Report.pdf)
 [Timestamp 1:04:10](https://youtu.be/6m0So81_j2Q?t=3850)

**Hudson**:  
- The ProgPoW report from Least Authority was released mid-week this week.
- This is an opportunity to hear for the Core Devs to hear from the Least Authority Team and ask questions.
- There is also an email that you can [email](progpow-audit@leastauthority.com) if you would prefer to send questions that way.

**Liz**: On the call we have Hind, Ram  & Jan on the call & Mirco listening in.

**Hind**: I was the project manager on the ProgPoW audit.

**Ram**: I do security audits for Least Authority.

**Keks**: I am Jan, I am also doing security audits.

**Liz**: Mirco will send through messages via slack.

**Liz**: There is a good summary in the report. This is the initial report and based on the feedback we get we will take that into account for the final report.

**Liz**: 
- The summary, in general on a high level it reaches it’s design goals and it is reasonable in terms of meeting its economic effect. 
- We did find one particular potential attack that we outline in the report. Members of our team can get into more detail if you wish to get into those details now.
- We also had some recommendations of things that can be done so that ProgPoW can continue to work in the future as intended.
- We also gave some feedback on what we recommend the community does moving forward.
- There is a lot of speculation of what can happen in terms of hardware advancements in the future. 

**Jan**: 
- Just a run through the suggestions:

**Suggestion 1: Scrutinize the custom Keccak Function**
- ProgPoW uses a modified Keccak Function.
- It is not clear if this is a proper hash function.
- However, whilst the rounds are reduced individually, it is used very often and chained, so there is not a lot going on which is why we say it achieves it’s intended design goals.
- But this remains a source of unclarity. 

**Danno**: Is this specific to the padding of the Keccak Function?

**Jan**: 
- That is one part, but I understand that the padding should not be necessary as it will always be the same size. 
- But is it is a medication and it would be nice to have people who are deep into hash functions have a look at it.

**Danno**: Does the current Ethash do the same non-padding?

**Jan**: As far as I am aware it includes the padding.

**Pawel**: That is correct.

**Suggestion 2: Address the light-evaluation method mining attack**

- This is specific to the situation where you have stages where you have the c, then you compute the hash, then you compute the DAG and in the DAG you adjust for lookups in the mining.
- The cache now days is small enough or it is getting small enough to fit on an ASIC or as ASICs grow, or you can put more SRAM on an ASIC, it is either now or soon, it should be feasible to put enough SRAM on an ASIC to hold the entire cache.
- And with a little more computational method do the mining from the cache.
- It means that you don’t have the memory bottleneck anymore, which is where the security is currently anchored on Ethash and ProgPoW, or at least ProgPoW in part.
- We are not sure what the situation is now. We verified this information from Bob and some other sources and they suggested the same.

**Hudson**: For clarification, Bob Rao is doing a very extensive hardware audit for ProgPoW. This is addition to the Least Authority Audit that looked at both Hardware and Software with a specific focus on software.

**Jan**: Just for clarification on Suggestion 2. The same attack would work on Ethash.

**Martin**: Is this reliant on very fast memory? And, is it available now and very expensive or available soon? 

**Jan**: If you have memory on the same chip then you reduce access speed enormously and this would be the cause of the potential attack. But we are unaware if such a thing exists and if it does not then it might soon.

**Hudson**: Bob’s audit suggests that this is more about future hardware, but his audit should answer a lot more of the questions and speculations.

**Liz**: This would also be far more energy efficient. There is a suggestion to mitigate this that it may be worth changing the constant dataset parents to 512 or something like that.

**Martin**: Were these suggestions and recommendations discussed with the ProgPoW team?

**Jan**: No we did not.

**Liz**:
- If it would be a good thing to do then now would be the time to do it between the initial and final report.
- These two suggestions remain the most in depth whilst the other suggestions are more over all suggestions.

**Greg**: Is Recommendation 2 a show stopper for ProgPoW or can this be overcome?

**Jan**: 
- The suggestion is to increase the constant dataset parents from 256 to 512. This constant suggests how much data has to be read for an item in the DAG to be computed.
- This would make both the light way verification, we don’t have the entire DAG, slower and also mining slower.
- Increasing it should be sufficient.
- I cannot comment if this will resolve the issues for 10 or 20 years but there is leverage to tackle this.

**Liz**: Our conclusion is that it does not change ProgPoW’s ability to do what it was designed to do and do this change value should be ok.

**Jan**: Note, Ethash has the same problem.

**Liz**: 

**Suggestion 3: Create additional documentation.**

- There were some key details that we felt were missing as well as improving the documentation in general to help people key on eye on these potential issues in the future.
- There are a couple of areas where more documentation could be added. 

**Suggestion 4: Explore a formal model of ASIC resistance.**

- If mining continues to be a growing industry then a more look into this would be useful.
- Coming up with better benchmarks for ASIC and formal models.

**James**: What is meant by formal in this case?

**Jan**: 
- It is not formal logic necessarily but more like a sound mathematical model or something that you can reason about. 
- Currently, we it comes to ASIC resistance it is just theory and it would be nice to have something that was reliable. 

**Suggestion 5: Monitor hardware industry advancements.**

- Whilst this sounds obvious, we just wanted to make sure that this was documented so that people were kept aware of hardware advancements that could pose a threat to ProgPoW in the future.
- Also we want to highlight other incentives for hardware to advance outside of Proof of Work.
- Specialised hardware of the future is hard to predict but there are certain signs and incentives that we should be aware of and how they could potentially impact on ProgPoW in the future.

## 5. Review previous decisions made and action items
•	[Call 69](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2069.md)

# 6. Client Updates 

None.
 
# 7. EWASM & Research Updates 

None.

## 8. Overtime discussion on Blake2b
[Timestamp 1:25:49]( https://youtu.be/6m0So81_j2Q?t=5149)

-	Notes were not taken of this discussion as it was held as a separate discussion to the All Core Dev Call but if you would like to listen to the discussion please click on the timestamped link above.
	
# Attendees

* Alex Beregszaszi
* Daniel Ellison
* Danno Ferrin
* E.G. Galano
* Greg Colvin
* Guillaume
* Hind Kurhan (Least Authority)
* Hudson Jameson
* James Hancock
* Jan Winklemann (Least Authority)
* Jason Carver
* Liz Steininger (Least Authority)
* Louis Guthmann
* Martin Holst Swende
* Pawel Bylica
* Ramakrishnan Muthukrishnan (Least Authority)
* Tim Beiko
* Tomasz Stanczak
* Trenton Van Epps
* Wei Tang

# Date for Next Meeting: 20th September 2019, at 1400 UTC.
