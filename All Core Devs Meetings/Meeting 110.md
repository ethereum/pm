# All Core Devs Meeting 110
### Meeting Date/Time: April 16th, 2021, 14:00 UTC
### Meeting Duration: 90 mins
### [GitHub Agenda](https://github.com/ethereum/pm/issues/293)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=-H8UpqarZ1Y)
### Moderator: Tim Beiko
### Notes: Joel Cahill

## Decisions Made
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
| **1**   | 3198: BASEFEE opcode being included in London | [1:19:53](https://youtu.be/-H8UpqarZ1Y?t=4793) |     
| **2**   |Newly planned dev call next week |  [1:35:03](https://youtu.be/-H8UpqarZ1Y?t=5703) |  
 
 
## Berlin Updates

**Tim Beiko**
[8:00](https://youtu.be/-H8UpqarZ1Y?t=482)

* Berlin happened yesterday, there was an issue with open Ethereum

**Karim Agha**

* Bug in the way open Ethereum implemented 2029, gas cost calculation was incorrect
* Thanked everyone from other client teams and community for help with identifying and fixing, pushed a fix to 3.2.3
* They will publish a written postmortem for the community with conclusions and findings next week

**Martin Holst Swende**

* Passing and reference case both failed to find the error, only way he can think to find this error is if the hive chain config had been identical to the main chain config with the only difference being the numbers, but otherwise its hard to figure out a process to better avoid this kind of thing.
* To debug things when they happen, its good to have tools that enable a node to forcibly import and trace a non-canonical block that was previously rejected

**Karim**

* Create a working group to define a set of integration tests so that all clients can talk to each other through a language agnostic API, and having a staging environment to swap clients before releasing and a certification process before marking a client ready for a fork, so that if something like this happens it can be a test case for all clients

**Tim**

* How is that similar/different than what we have with Hive?

**Karim**

* Not familiar with Hive

**Martin**

* [Hive](https://hivetests.ethdevops.io/)  - It takes 4 clients, executes states tests on the clients – start the client, import the blocks, rlp, checks if the latest block after import is expected to be, eth protocol, graphql.
* What you are describing sounds like something that can be done in Hive, although I am not sure if you were talking more specifically about debug analysis or testing in general

**Karim**

* More about testing in general. Each client has its own set of tests, and rather combine all tests to one repository

**Martin**

* Yeah, that’s basically what Hive does. Feel free to reach out off chat for any help

**Tomasz**

* Whichever environments we define will always end up having some inconsistent configurations vs mainnet, so what they did with an issue with a config file was add internal nethermind specific tests for the config file formats and they have added that for all the configs files they have used, but it’s hard to do something like this for all the clients because there is always going to be something client specific

**James Hancock**

* Not idea for bugs/issues to pop up during a hardfork, but more importantly the issue was handled respectfully and responsibly and is something to admire about the group and its resiliency, and congrats to open Ethereum team for how they handled it. Dragan echoed this sentiment

**Tim**

* Should we have hive run with mainnet configs? Should we look at this or take a next step on it?

**Martin**

* Its more a note for self in future to try to make the hive specs more closely aligned to mainnet specs

**Dragan**

* Bug fixed, recommend using Open Ethereum version 3.2.4

**Tomasz**

* Could we put effort into setting up part of Hive to test encoding of all the types of dev p2p messages. We currently only test in hive in the synchronization test, but we could do every single message separately for encoding decoding for each client.

**Martin**

* Unsure if it is fully tested in Hive yet, but if not, it should be added, and the goal is to have all the network packets tested in Hive.

**Lightclient in chat:**

* It would be nice to have more effort into a standard tracing format because different clients use different formats, and it can be hard to find the divergence in outputs

**Tim**

* Something to investigate more offline
 
## Updates for London
[33:10](https://youtu.be/-H8UpqarZ1Y?t=1990)

**Marek**

* From nethermind team: We are ready with our client and are in sync with London devnet.

**Tim**

* What is the next best step here? JSON RPC handling? Previous calls we talked about potentially having another devnet once 1559 was fully implemented and spec’d out? What do we think the next step should be?

**Lightclient**

* Are the RPC changes fully defined now? My understanding is most things will continue to be optional fields, the one question was how to bring the effect of gas price to the transaction object, and either have effective gas price as an element or just replace gas price with it.

**Tomasz**

* It would be reasonable to suggest some dates in July for testnets, or even start in June and set July date for London and let everyone work against those dates and have cleared planning for when everything needs to be implemented.

**Lightclient**

* Why not do that and continue working towards these EIPs to see if they can be implemented by then

## EIP 3403

**Tim**
[38:10](https://youtu.be/-H8UpqarZ1Y?t=2290)

* EIP 3403, which is disabling the refunds, has been discussed as needing to go along with EIP 1559 for security reasons, is that still the case, and should we bring it in now so that people know they need to implement it?
 
**William**

* If we believe miners will push an infinite gas limit, then it will not matter if the elasticity is 2x or 4x. If this is a major security concern, we should revisit the hardcap, though I would recommend a much higher limit than the original proposal. On the other hand, if we assume miners want to prevent each other from submitting DOS blocks, the base fee would be more secure with a possibility of 4x vs 2x.

**Tomasz**

* Miners are showing great care for network security and are using MEV now which is offsetting potential losses from 1559. We heard threats from miners they would pick up aggressive actions against the chain, but we have not seen this behavior from miners.

**Martin**

* I’m in favor of EIP 3403, not sure if it is a security requirement for 1559 but thinks it probably is.

**Micah**

* Is gas pricing for storage based on long term state growth cost, or just the read/write to disk cost?

**Vitalik**

* The cost of a s load was intended to represent the short-term operation cost, the cost of an s store was intended to represent the combination of short-term operation cost and the growth in storage for an archive node.

**William**

* I agree the long term was the major component of s store, and for that reason we should consider keeping the stipend to incentivize in good behavior and design. 3 protocol engineers concurred in the Ethereum additions forum that this proposal punishes state cleanup, and therefore make state cleanup worse.

**Tim**

* Should we think through this stuff async before the next call before deciding since there is a lot to consider? Take 2 weeks to think before coming to a decision.

**Martin**

* Sounds like this could be a contentious thing, debate in an offline forum is nice but it does not look like it will be resolved where everyone agrees, and we will have to make a call at some point.

**Artem**

* What we are seeing is the gas token businessman who does not want to see their old business model turned to garbage, but we should not pay attention to it and proceed as planned

**Matin**

* I agree

**Ansgar**

* I tend to agree with what was just said, if we do not come to a decision today what does it mean for the devnet, does it make sense to include it in the devnet for London with 1559 before the more optional EIPs

**Vitalik**

* Just want to remind that whatever choice is made on 3403 is not inherently permanent because the state expiry roadmap which will be one of the top priorities after the merge, which will reform state into a structure where state being removed won’t be a concept that exists, so the cost of making the wrong choice for 3403 isn’t that large.

**James**

* We’ve discussed some these same ideas in previous calls and going through permutations of the same ideas won’t get us anywhere helpful, and Id rather go ahead with it from the perspective of the design isn’t working as intended. We should go with putting it in for devnet and London, and revisit if needed after implementation and the fork.

**Tomasz**

* We’re generally in favor, just not for London

**Tim**

* Turbo geth and geth are strongly in favor for

**James**

* Piper has said strongly in favor for in previous conversations

**Dragan**

* Open Ethereum in favor of EIP 3403, maybe plan for London but if something happens delay is okay

**James**

* Micah’s point that we can include it in the devnet and not have it apart of London

**Martin Koppelmann**

* Do not have a strong opinion, but from smart contract developer point of view, developing/auditing/bug bounty for contracts takes a long time, so he expects to see more and more contracts that are making heavy use of deleting unnecessary storage

**Martin Swende**

* Do not want to overstress contract developers are not developing correctly, more its issue of various gas tokens that use the state as a battery to charge up and get back later on

**Gary Schulte**

* If we include it in dev net but not London, are we not opening the door to another bls precompile type of consensus issue?

**Artem**

* If we are not aiming for London, then this EIP will be effectively buried. We must aim for London.

**Tomasz**

* This is why we need clear timeline with the merge and EIP upgrades. If EIPs are not included in London, it could be 6-9 months before next opportunity for them to be implemented.

**Danno**

* We should step back and see if there is not a compromise to be made. What if we just apply the refund to the account and have the total gas used on the block always go up, and never be a benefit from refunds. This can in some uses reduce it from heavy defi operations, but at the same time preserve the market for the utility the contracts have for refunds.

**Vitalik**

*  I've thought about things like that a bit, and I think the challenge is making refunds anything other than anything globally scoped introduces more complexity and edge cases that would have to be tested, so it would complexify and bloat the whole thing significantly.

**Rai**

* Do gas futures with the introduction of base fee help with there being less of this battery usage of the state? Or is it equivalent in some sense with just as much state claimed?

**William**

* The motivation for using gas tokens is to increase the throughput during congestion, so if you use them in that context then the futures market won’t help you.

**James**

* Tomasz plan works if Shanghai is an EIP fork and happens in the fall, followed by the merge. But if Shanghai is the merge and not an EIP fork in the fall, then we should expand the scope of London. And I am okay with either of those plans, but we should decide on one

**Vitalik**

* There is also the 3rd track of being willing to wait a year for EIPs because none of them are that critical, and the Ethereum ecosystem has been willing to wait a year for an EIP for pretty much all its history.

**Artem**

* We shouldn’t focus on the merge too much because there isn’t a lot of concrete or finalized on how things will look. We should introduce one hard fork between London and the merge, and if we want to stagger EIPs for London that is fine.

**Ansgar**

* Timeline: With London being in July because of the difficulty bomb in August, the community sentiment seems to be merge as soon as possible, so the community might not support a merge delay to prioritize EIP hardfork before it.

**Tomasz**

* Adding more EIPs to London can cause a delay to the merge

**Tim**

* Main challenge with the merge is there is a lot of work to specify it, core devs need to spend attention on it and spec it out

**Micah**

* Last week we talked about getting a rough estimate on the difficult of the proposed EIPs, did we ever get that made? I feel like that is a significant component here

**Tim**

* Two things worth considering here, whats the expected amount of work to implement something, and would it be the end of the world if we waited a year to have it?
* Is there anything from this list: EIP-3403 #277, EIP-3198 #270, EIP-3074 #260, EIP-2537 #269, EIP-2677 #271 that would be the end of world if we waited a year?

**Lightclient**

* Unless it is a security issue I don’t think its ever the end of the world, but I would like to say 3074 users are spending about 25million a month of token approvals, and 3074 will reduce that by at least 30%, so it was save end users millions of dollars per month in extra gas fees. Which is only a small aspect of 3074, so we should not push it out a year

**Tim**

* We’ve talked about 3403, 3198 the base fee op code being the smallest amount of work, 3074 being pushed out by the community. The 2537 (bls recompile) and 2677 (capping the size of init code) haven’t had as much advocacy for them.

**Martin**

* Doesn’t see 2677 as something that needs to be done right now

**James Prestwich**

* 2537 has been ready to go since yolo v1 with no issues so there is not really an update from him

**Danno**

* I would like bls in the next plan if possible, I see utility in it

**Tim**

* Hypothetical timelines for London, say latest possible date we can have it is August 1st, that means we want to have last of the test net fork 3-4 weeks before then by early July, so if we want to have 1st of test net a month before then, so when do we need client versions out? So in 2 months from now we need client releases out with full support for London.

**Tomasz**

* Question to Open Ethereum team is how much is left to be worked on 1559 implementation

**Dusan**

* Our implementation is 90% finished, we are in a sync with dev net. We have additional work on RPC implements, improvements on transaction pool. But for consensus part of the implementation, we are good.

**Tim**

* Did you also implenet the basefee opcode? That is the smallest amount of work to be implemented. Do you have any issue implementing that for London?

**Dusan**

* No, we can do it.

**Tim**

* Can we agree to bring it into London? (basefee opcode)
* **DECISION 1:** Okay, basefee’s will be in London [1:19:53](https://youtu.be/-H8UpqarZ1Y?t=4793)
* What’s next best step about 3403, 3074, 2537, 2677?

**James**

* It might make sense for 2537 to be a part of the merge as well

**Micah**

* I would love to see Open Ethereum’s rough time estimates for each of the EIPs, because historically they have been a little slower implementing the changes because they are a newer team taking on an existing codebase, which is difficult. I suspect in the end they will be the decision maker on what can be included regarding difficulty and timing. This can be done async.

**Tim**

* That will be valuable, and I can follow up with each of the client teams over the next 2 weeks and chat about these things.

## EIP 2935

**Tomasz**

* I believe we can skip the discussion for now. Lets put it after London.

## EIP 3436

**Danno**

* What I propose to clique, can clique only, is a few specific block choice rules that go on when you see two equally valuable heads. Of course, the first rule is to pick the blockchain head with the highest total difficulty. The second rule is to pick the one that is the shortest. The third rule is you decide based on who is either closest to intern or furthest, it doesn’t really matter as long as everyone picks on the same side. And fourth, is to take the hash of the block, convert it to a uint 256, and pick the block with the lowest number. This should prevent all chain halts at this point. Encourage people to go to the Ethereum additions thread for feedback.

**Tomasz**

* Strong support of what Danno is suggested.

***Zoom audio cuts out during Peter Szilagyi’s, and Danno’s response from 1:30:45 – 1:33:45***

**Tim**

* Timeline for London: If we want to aim for mid-July, we need a client release for fork by May 15th, and the next call in 2 weeks will be right before then so we absolutely need to make a call about the EIPs on the next call. Thoughts about a call off schedule next week to discuss the EIPs? Or do them async?
* **DECISION 2:** Ill organize a sync call next week and follow up with the different client teams about effort/time/value ratio for various EIPs, and we can discuss that next call. [1:35:03](https://youtu.be/-H8UpqarZ1Y?t=5703)
 
##EIP 3074

**Sam Wilson**

* Our second 3074 testnet is going with geth and working on our Open Ethereum implementation

**Lightclient**

* We have been getting an audit to look at the specification as well as do analysis on how it will impact contracts that already are on mainnet. We have gotten a couple proposals and are optimistic about the people doing the audits and the timeline can be completed by the end of May. I think our team is committed, along with other premier teams, to funding or providing developers to make 3074 happen for London, with the goal to minimize the amount of work current client teams need to do. 

**Tim**

* Are people opposed to putting 3074 into a dev net before the results of the audit? It seems like the audit will come in after everything will have to be done. We cannot wait for it to come into, digest it, then implement. We might have to implement it, then rip it out if the audit shows a severe issue.

**Micah**

* Tricky part with 3074 is going to be getting everyone on board with it. Most are skeptical at first, and the tricky part will be getting the mindshare with every core developer to convince them that it is okay.

**Tim**

* The goal of the audit is in part to show that its safe and alleviate/satisfy some concerns.

**Ansgar**

* This EIP has the potential to make a big difference on the application side, so if there is some chance to include 3074 we should try to take it, assuming the concerns are alleviated in time.

**Tim**

* To wrap this up, I will talk to client teams specifically about 3074 and get an idea if we can technically/time wise include this with London, assuming audit is good.

**James**

* This fits into the if we had a fork in the Fall it would fit in easily, but to get it into July could be cutting it close. But having it push back to mid next year would severely impact usability, so it fits into the not wanting to wait a year but is tough to get into July.

**Lightclient**

*  We have talked to a few dozen of the most prevalent defi eth UX tool teams, pretty much every single one of them is positive on it and will be raising money to show they are serious about it.

-------------------------------------------
## Attendees
- Tomasz Stancsak (Nethermind)
- Tim Beiko
- Jochen
- Rai
- Micah Zoltu
- Karim Agha
- Trenton Van Epps
- hexzorro
- Dusan
- lightclient
- Mikhail Kalinin
- William Morriss
- James Hancock
- Pooja Ranjan
- Ansgar Dietrichs
- Paul D
- Gary Schulte
- Marek M
- Mojtaba Tefagh
- James Prestwich
- Kev
- Alex Vlasov
- John
- Martin Holst Swende
- Danno Ferrin
- Peter Szilagyi
- Tukasz Rozmej
- Sajida Zouarhi
- Vitalik
- Dragan Rakita
---------------------------------------
## Next Meeting
April 23, 2021
