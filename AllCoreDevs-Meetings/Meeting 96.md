# All Core Devs Meeting 96 Notes
### Meeting Date/Time: Friday, September 18 2020, 14:00 UTC
### Meeting Duration: 1:32 hrs
### [GitHub Agenda](https://github.com/ethereum/pm/issues/206)
### [Audio/Video of the meeting](https://youtu.be/HUUxwyoxU7k)
### Moderator: Hudson Jameson (Tim Beiko for EIP-1057)
### Notes: William Schwab

---

# Summary 

## EIP Status
EIP | Status
--|--

- 1057: to be merged into clients, testnet to be launched
- 2315: original marked for inclusion in YOLOv2, modified to be slated for YOLOv3
- 2357: marked for inclusion in YOLOv2
- 2359: not to be included in YOLOv2
- 2929: marked for inclusion in YOLOv2

## Decisions Made

Decision Item | Description
--|--

- **96.1**: Breakout room meeting for Monday to proceed as planned, in the future the following expectaitons will be used: discussions that would potentially take too much time of the ACD call will be forwarded to async comms such as Magicians, if over the cycle of one ACD call this is insufficient, a breakout room will be suggested and organized if there is sufficient demand.
- **96.2**: Clients to merge ProgPoW, but client teams and EF will not take responsibility for launching a testnet for ProgPoW. A ProgPoW testnet should be launched, however, perhaps launching with Ethash and migrating to ProgPoW
- **96.3**: BLS12-377 (EIP-2539) will not be considered for inclusion in YOLOv2 or Berlin in order to not set a precedent and/or delay, but can be brought up later
- **96.4**: Original EIP-2315 proposal to be included in YOLOv2, modified proposal (including restrictions for jumping in subroutines) to be considered for YOLOv3


## Actions Required

Action Item | Description
--|--

- **93.1**: Cat Herders to coordinate participants of breakout room meetings, handle coordination and invitation
- **93.2**: Clients to test and merge ProgPoW capabilities
- **93.3**: A ProgPoW testnet should be launched (but client teams/EF will not be responsible for this launch)


---

# Agenda

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 bullets:1 updateOnSave:1 -->
- [1. EIP & Upgrades Updates](#1-eip-upgrades-updates)
    - [1a. YOLO/YOLOv2 & Berlin state tests update](#1a-yolo-yolov2-berlin-state-tests-update)
    - [1b. Breakout room feedback](#1b-breakout-room-feedback)
- [2. EIP Discussion](#2-eip-discussion)
    - [2a. EIP-1057 next steps](#2a-eip-1057-next-steps)
    - [2b. BLS12-381 curve operations & BLS12-377 curve operations](#2b-bls12-381-curve-operations-bls12-377-curve-operations)
    - [2c. Account Abstraction Update](2c-account-abstraction-update)
    - [2d. EIP-2929: Gas cost increases for state access opcodes](2d-eip-2929-gas-cost-increases-for-state-access-opcodes)
    - [2e. EVM384 update](2e-evm384-update)
    - [2f. EIP-2315: Simple Subroutines for the EVM](2f-eip-2315-simple-subroutines-for-the-evm)
- [3. EIP-1559 Update](#3-eip-1559-update)

# 1. EIP & Upgrades Updates

Video | [3:45](https://youtu.be/HUUxwyoxU7k?t=225)
-|-

**note**: EIP-1057 was put first - the order of the notes reflects the order of the agenda

# 1a. YOLO/YOLOv2 & Berlin state tests update

Video | [34:55](https://youtu.be/HUUxwyoxU7k?t=2095)
-|-

**note**: this item was discussed through the three EIPs on the agenda relevant to YOLO:
* [2b. BLS12-381 curve operations & BLS12-377 curve operations](#2b-bls12-381-curve-operations-bls12-377-curve-operations)
* [2d. EIP-2929: Gas cost increases for state access opcodes](2d-eip-2929-gas-cost-increases-for-state-access-opcodes)
* [2f. EIP-2315: Simple Subroutines for the EVM](2f-eip-2315-simple-subroutines-for-the-evm)

# 1b. Breakout room feedback

Video | [1:08:28](https://youtu.be/HUUxwyoxU7k?t=4109)
-|-

**Hudson Jameson**: we tried breakout rooms in the Discord along with some calls. There was some confusion about the purpose. **Hudson** asks **Pooja Ranjan** to talk to this.

**Pooja Ranjan**: there were 2 meetings since the last ACD meeting on the consecutive Mondays (1400 UTC). The goals was to get consensus from client developers on proposals discussed, and to discuss the results in the next meeting. Both meetings were focused on YOLOv2, summaries in ethereum/PM repo. The proposal to have the rooms was discussed in the last ACD, general consensus was once a week, one or two proposals, and on a by-need basis. The meetings in general can do with only 6-10 people from the 6 clients, the author, and other parties implementing are welcome.

It's important to get representation from the clients. You don't need to keep track, we'll publish in the channel when it's going to happen. There will also be a calendar invite, for those willing to share email, please DM on Discord.

**Hudson**: I had been under the impression not every client needed representation, only those with some opinion about the proposal.

**Pooja**: Better to have the clients there in order to get their opinion on any way the proposal is modified. **Hudson** asks for general opinion about whether all clients should attend. **James Hancock** does not want it to turn into ACD part II, and wants it to be conversations that don't need to be in ACD. **Hudson** proposes that **Pooja**, **Hudson**, and **James Hancock** shouldn't be the ones dictating what gets a breakout room, but rather core devs themselves should be deciding.

**Micah Zoltu**: If in ACD someone has a strong opinion, they should show up to argue their point. If it's only the author, no progress is made. **Peter Szilyagi** doesn't like the idea of an additional meeting, **Hudson** asks if there's a change that could be made to the format to make it better, **Peter** clarifies that if **Martin Holst Swende** wants to argue against an EIP, and he'l argue against all of them since he's security, then he has all this extra work, **Hudson** agrees to this concern, **James Hancock** says that attendance should therefore not be compulsory, though adds in deference to **Micah** that there will have to be acceptance if the core antagonsists to a proposal can't or don't attend. **Micah** asks at least to clarify beforehand if people won't come in order to help everybody's schedule by knowing who is attending. 

**James Hancock**: It's at least good for the organizers (such as **Pooja** and **James Hancock**) to point out if a conversation is stretching that it can go to breakout rooms, and then allowing the participants to decide, and if they agree, to schedule for them. This increases the chance of them actually happening, and can save longer conversations from taking over an ACD call.

**Hudson**: another suggestion is leveraging the asynchronous communications like the Magicians more. There needs to be options in between no action and forcing, otherwise there will be ossification.

**Pooja**: The problem with asynchronous comms is that they can cause delays, and cannot come to quicker decisions.

**James Hancock** gives the example of EIP-2315 as a good potential breakout about what needs to be done, but doesn't think it should be done this time, just an example, but doubts could be ironed out then reported to ACD.

**Hudson**: I think a good in between is that the breakout room is available whenever, won't be about a specific topic unless requested. First push should be for asynchronous comms like the Magicians and ACD chat or whatever, if that doesn't work after a single ACD call, then the ieda of breakout room should be floated. There is a tradeoff, but for important decisions, the rooms are important.

**James Hancock**: the focus should be getting consensus, not making decisions. Decisions will remain on ACD. **Hudson** asks for last comments, **Pooja** asks if a meeting for next Monday is still on, clarifies that it was slated for YOLOv2, **Hudson** asks what still needs to be discussed, **Pooja** cites EIP-2935, which has fallen aside due ot absence of a champion, **hudson** asks for general opinion.

**James Hancock** thinks a breakout call would be good since there were points which can't be addressed in the current call. **Hudson** proposes going forward with the Monday call, then implementing the new set of expectations afterwards. There seems to be consensus on this. **James Hancock** clarifies that the Cat Herders will take the role of figuring out who needs to be there, and contacting. **Hudson** agrees.

**Decisions**:
- **96.1**: Breakout room meeting for Monday to proceed as planned, in the future the following expectaitons will be used: discussions that would potentially take too much time of the ACD call will be forwarded to async comms such as Magicians, if over the cycle of one ACD call this is insufficient, a breakout room will be suggested and organized if there is sufficient demand.

**Actions Required**:
- **96.1**: Cat Herders to coordinate participants of breakout room meetings, handle coordination and invitation

# 2. EIP Discussion

Video | [26:53](https://youtu.be/Riu-PqrJVH4?t=1613)
-|-

**note**: the order in the notes does **not** follow the chronological order in the call, but rather the order of the agenda - the timestamps by each item can be used to construct what order they were discussed in


# 2a. EIP-1057 next steps

Video | [4:18](https://youtu.be/HUUxwyoxU7k?t=258)
-|-

**Tim Beiko** moderates this part of the conversation instead of **Hudson Jameson**, as per request. Tim asks **Greg Colvin** to summarize current status.

**Greg Colvin**: submitted May 2018, tentatively accepted after ~7 months of review, then many people got angry (about it), software and hardware audits performed, decided to put it in, published numbered decisions to do so, followed by another outcry, including on All Core Devs where non-regular members heckled. At the end of the call, the previous decision was reversed. In discussion since it has been unclear what happened, but it seems that people are more or less happy with Ben DiFrancesco's compromise. Goals for today: either a publishable decision that will not be reversed without serious discussion to go with this compromise (brought at the top of the PR, will be removed when a decision is reached, as it isn't meant for the EIP).

ProgPoW is a Proof-of-Work algorithm meant to replace Ethash. Ethash was designed to be ASIC-resistant, but isn't, and ProgPoW should it make it very difficult to make ASICs stronger than GPUs, and by now we have every reason to believe that it should. We do not propose immidiate deployment or hard fork, the compromise Ben recommended is full implementation and testing across clients, which is already true for many of them. It should be deployed to a testnet to keep the possibility and threat of deployment open. We can and should keep an eye of what is happening on the network, and switch to ProgPoW if necessary, and the hope is that those in the business of making ASICs can take note and decide if it is worth it for them to make them.

**Martin Holst Swende**: Curious about the kik exploit and if there were changes to the spec?

**Greg**: While there is a way to completely mitigate the possibility of the issue, after months of inspection we concluded that it would be practically impossible to implement. You need a homemade ASIC which can brute force a table inside a block time, modify headers that can't be modified, and more. Andrea Lafranchi has more details, but we don't think it's worth it to fix. The spec has only been changed to move this down into the security section, just in case someday we think someone has found a way to make this exploit more possible.

There was also an exploit which the software audit found, which is also an Ethash vulnerability. It is not practical to attack Ethash with now, maybe a few years down the line. It wasn't clear that it is possible to exploit on ProgPoW, so we're not putting it into the current proposal, though it is discussed in the security section. (Clarifies questions from **James Hancock**, both have the vuln, though Ethash has it as more of a risk than ProgPoW, though it's still not practical to attack ethash with.)

**Martin**: Does the current implementation need to be changed?

**Greg**: No.

**Martin**: If we move forward with the compromise, the current goal would be to merge it, and activate the ? (**notetaker's note: unclear in recording (~15:25), I would guess 'testnet' from context). **Greg** confirms. **Martin** confirms that this is a small technical burden.

**Greg**: I am not proposing this as a delay, I am proposing we remain serious about ASICs not becoming a threat to the network. Community feelings are not as important as the security of the network. **James** asks for confirmation that the decision here is to deploy to testnet, **Greg** confirms, adding that it should be in a way that it can be deployed to mainnet if necessary.

**Tim Beiko** asks for integration status from client teams. (Something about a comment about **Nethermind** from **Micah Zoltu**, but it isn't visible.)

**Tomasz Stanczak (Nethermind)**: doesn't look like a lot of work.
**Tim (Besu)**: some work, but not starting from scratch
**Dragen Rakita (Open Ethereum)**: merged a year and a half ago, unaware of current status, would assume it needs a little work. **Peter Szilyagi** mentions that he thought he saw them announce that Open Ethereum would no longer maintain or ProgPoW work. **Dragen** agrees that it should be looked in to.

**James Hancock**: probably doesn't make sense to deploy to YOLO

**Tim**: also need to ask if it should be bundled with anything else, or kept stand-alone.

**Peter Szilyagi**: Ropsten is getting too huge to use, everyone is using Rinkeby or Goerli, could make it a replacement for Ropsten. No loss in having a testnet which isn't Ethash.

**James**: would a ProgPoW testnet, would we want it inside Muir Glacier, or should it wait for Berlin.

**Tomasz**: release testnet now, don't bind it to main.

**Peter** suggests deploying with Ethash and switching over to ProgPoW, **James** concurs, says that if so it should definitely be inside Muir Glacier.

**Micah Zoltu**: I think Ropsten isn't getting used because it's always under attack, not because of size.

**Peter**: probably both. **James** agrees.

**Tim**: what is stopping this from happening? **Peter** since ProgPoW isn't merged in the clients, and there should be a bit more testing. **Martin** code should be merged, bindings to activate should be exposed.

**Tim**: is **Martin**'s proposal a way to do this with minimal involvement if client teams don't want to be involved. **Martin** agrees, adds that the EF runs a number of nodes, and that they usually require big machines, but if this testnet isn't about full blocks, and there won't be many devs building on it, it should have a low overhead. Either way, the proposal isn't for the EF to run the testnet. **Tim** makes sure **Greg** agrees with this.  **Greg** agrees with **Martin**'s technical proposal, and agrees that the proposal does not include providing or paying people to keep the testnet running.

**Vitalik** asks to move forward within the next couple of minutes. **Greg** stresses the importance, asks for a published decision.

**note**: **Greg Colvin** placed the following text in the chat:

_DECISION:_
* _This proposal is not being proposed for deployment in any planned hardfork._
* _This proposal should be fully implemented and tested across major clients._
* _Clients implementing this Proposal should be deployed and maintained on a testnet._
**end note**

**Tim** restates that the client teams will not take on the responsibility of deploying or maintaining the testnet. **Greg** says this is his intent. **Martin** consents for Geth, **Peter** concurs. **James** restates that the code will be merged into clients for activation on testnets (not mainnet). **Peter** says that if testnet lasts for however long, clients can implement defaults for the testnet.

**Greg Colvin**: to state clearly, client teams are agreeing to merge ProgPoW code in a way that it can be activated on mainnet, but will not be activated at this time. **Tim** agrees, but wants to stress that there is no target block for mainnet to switch, even if the code exists.

**Tim**: **Andrea Lafranchi** asked in chat what grade of trust a non-official testnet has to the All Core Devs. There is some confsion to the intent, **James** says he isn't aware of any differentiation, which has general consensus, **Martin** concurs with some technical details.

(**notetaker's note**: due to the amount of emphasis placed by **Greg Colvin** on a published decision, I would like to state clearly that the general consensus on the call was in favor of the decisions below. **James Hancock** confirms this at [34:30](https://youtu.be/HUUxwyoxU7k?t=2070).)

**Decisions**:
- **96.2**: clients to merge ProgPoW, but client teams and EF will not take responsibility for launching a testnet for ProgPoW. A ProgPoW testnet should be launched, however, perhaps launching with Ethash and migrating to ProgPoW


**Actions Required**:
- **96.2**: clients to test and merge ProgPoW capabilities
- **96.3**: a ProgPoW testnet should be launched (but client teams/EF will not be responsible for this launch)

# 2b. BLS12-381 curve operations & BLS12-377 curve operations

Video | [36:20](https://youtu.be/HUUxwyoxU7k?t=2180)
-|-

(Some conversation between **James Hancock** and **Hudson Jameson** about ordering)

**James Prestwich**: At Celo planning for hard fork, which includes a number of Berlin inclusions, including EIP-2357 (BLS381) and EIP-2359. The last time this came up in an ACD call, the decision was for EIP-2537 due to applications for ETH2, and to shelve the others until a concrete usecase. Celo would like to consider the other (EIP-2359) for inclusion since Celo uses it throughout, also have ancillary benefits for 1-layer recursive zkps, and to Aztec and other zero knowledge projects. Celo will include both EIPs, and would be happy to contribute the research upstream.

**Hudson** clarifies that the only precompile currently being considered for inclusion is BLS12-381 (EIP-2537). **James Prestwich** confirms, and confirms that **James Prestwich** would like to contribute code for both EIPs since they will be implementing both.

**James Prestwich**: Since these precompiles are almost the same, we feel like it would not be much work to also include EIP-2539 as well, and will be willing to contribute much of the work, and would love to see it considered for YOLOv2 or even Berlin. **Martin Holst Swende** objects.

**Martin**: It's not reasonable to roll it out now for YOLOv2, and throwing out new precompiles because they share the same form... they need to be tested from the ground up before considered mature.

**James Prestwich**: We've deployed a Rust version in the wild, and will be fuzz testing.

**Hudson** asks **James Hancock** for his opinion. **James Hancock** asks **Martin** how much fuzz testing will help for these concerns.

**Peter Szilyagi**: Original BLS curves were fuzz tested for weeks and months, and Martin and Marius came along and found a number of vulnerabilities, including in the assembly. Fuzz testing is not enough. 

**Alex Vlasov**: Firstly, the change in the curves is ?, so the current code base can take 20 lines of code and make it for the new curve. Also, while it is true that there was a bug in the assembly which I didn't catch in Go, the rest of the problems were not in the part in the control of client developers, and there was never an error in math implementation found, just in the integration of the codebase and some constants for some clients. So this doesn't inflate the complexity. Fuzz testing should be used as a black box by the client developers.

**Peter**: The point was that there is always room for error, and it requires testing by people that have been doing this for the five years. You might be right, it might just be a few constants, but I don't know now what the affect on the assembly will be. You very well may be right that there will be no change, but we need to be sure.

**Alex Vlasov**: But we need to define what is well tested.

**James Prestwich**: Since it's so similar in implementation, and just has a few parameter changes, **Martin**, would you consider it if we brought it up to the same testing and integration standards as the existing curve. **Martin** says he would not, and references putting a lid on Berlin if it's going to happen anytime soon. **Hudson** concurs with this point, and states his opinion that it should not be included this far into the planning for Berlin.

**alex Vlasov** asks about timeframe for Berlin, **James Hancock** says this would be a long conversation, and concurs on not adding to Berlin, also concurs more testing necessary until the new curve is deemed secure, but says that if the extra research speeds deployment for Berlin since it will add research on both curves, that it should be considered.

**James Prestwich** clarifies that they want to help with testing and integration for EIP-2537 (BLS381), and that as a result, testing and integration for EIP-2539 (BLS377) should be trivial. Also states that he does not want to push back Berlin, rather would hope to help with testing and get this integrated in the same timeframe.

**James Hancock**: would this help enable a faster timeframe for saying EIP-2537 (BLS377) is ready for mainnet? **Hudson** asks if EIP-2539 inclusion is a precondition for helping, **James Pretwich** says that it is not, rather part of Celo calculating their own hard fork schedule, and contributing upstream to Geth and Open Ethereum.

**Hudson**: Based on the Geth team's concerns, EIP-2539 will not be considered for inclusion today, though may certainly be brought back up in the future. **James Prestwich** asks if there was a concrete decision to stop taking requests for Berlin, and specifies that they're interested in figuring how best to interact with ACD on these points. **Hudson** says it's a sliding scale, and depends on an EIP-by-EIP basis, and that communication with the Core Devs is probably the best. **Hudson** adds that he doesn't have a more specific answer, and that the nature of decentralization is bit messy on decision-making.

**Alex Vlasov** asks for a standard on how much something should be tested, **Hudson** says in his opinion standards would help, but is contingent on the opinion of those doing the tests. In addition, standards can be proposed, but acceptance is contingent on the implementers. **Alex Vlasov** asks for taking the current processes on BLS, and maybe using them to try and create something of a standard.

**James Hancock**: wants to know how much testing will be sufficient for the BLS precompile.

**Alex Vlasov**: there are 3 parts: the historical from 1962, results will be consistent if implemented properly, for a more specific curve like 381 you can use specific linraries, but want good case testing first that valid inputs get the same result, then go to negative inputs, which also depend on binary interface, then implementation into clients. **James Hancock** clarifies that he would like the client developers' opinions, and says that one of the difficulties in trying to come up with a date for Berlin stems from not understanding how much time is needed for this.

**Hudson**: this won't be solved today, so we'll move on.

**Decisions**:
- **96.3**: BLS12-377 (EIP-2539) will not be considered for inclusion in YOLOv2 or Berlin in order to not set a precedent and/or delay, but can be brought up later

# 2c. Account Abstraction Update

Video | [1:22:50](https://youtu.be/HUUxwyoxU7k?t=4972)
-|-

**Sam Wilson**: Vitalik and the Quilt team have put out an explainer and made an EIP, and want to ask what the next steps are for inclusion, also looking for feedback. 

**Ansgar Dietrichs** also points out that the important difference between this EIP and other EIPs were bringing consensus changes to a minimum - a new tx type, and a nonce opcode that might even be written out, and a peg. The idea is that mempools have strict rules about txs, and can therefore start with very restricted use cases, then later can add or extend mempool rules without further changes. Wants to hear feedback and concerns.

**Hudson Jameson** agrees that core devs will review and feedback. **Ansgar** says that there are 2 Magicians threads, so some care needs to be taken to find the right one, and there is an account abstraction channel in the Eth R&D Discord.

# 2d. EIP-2929: Gas cost increases for state access opcodes

Video | [59:30](https://youtu.be/HUUxwyoxU7k?t=3570)
-|-

**Alex Vlasov** had a question about this which was resolved in chat. **James Hancock** agrees that if the issue has been resolved, that the call will move on.

# 2e. EVM384 update

Video | [1:26:22](https://youtu.be/HUUxwyoxU7k?t=5182)
-|-

**Alex (axic)**: Over the past 4 weeks (mainly **Paul** and **Jared**) we had three different versions of the opcodes and a Yul implementation, and we have advanced on both fronts, thought Yul might not be the most optimal, thought Huff might be better, and also had ideas how to improve opcde bottlenecks. The major bottleneck is in the number of stack items each requires. Shared a doc, the most important implementation is the last (v7) which has one item, and packs memory off of that item. This has the least changes to EVM, and has all the speed benefits. In terms of Huff vs. Yul as an example, in one case the Huff version was 40% more efficient, which seems to be a good indication to focus on Huff. Compared to 4 weeks ago in Yul we were at 18ms, with Huff and v7 we are at 5.5ms (and against a native code of 4.3 in this case). This gives a good indication that we are on the right track for performance, and we think the v7 design is unlikely to change in any major way, and would like to encourage writing a pairing operation, and encourage looking at the Huff code for a proper implementation. Once a pairing implementation is written, we can make a final decision if this is a solution, but the numbers suggest that it's promising.


# 2f. EIP-2315: Simple Subroutines for the EVM

Video | [1:00:10](https://youtu.be/HUUxwyoxU7k?t=3610)
-|-

**Hudson Jameson** mentions that **Greg Colvin** had an issue regarding which version would be used, **Greg** proposes moving to the Magicians thread in interests of time. The basic idea was if the proposal to prevent jumping in and out of subroutines should be included, states personal inclination in favor.

**Vitalik Buterin**: has anyone thought about interactions between 2315 and code merkelization?

**James Hancock**: Yes, it was part of **Axic**'s suggestion, and also looked at by **Alexey**. To my memory we said that we would do the jump stopping features, but that **Greg** was against. **Greg** agrees that there are concerns. **Martin** agrees ("more or less") that this was the general sentiment. Wanted to check if implemented if it would break contracts, dumped contract code and checked it, had a lot of false positives, though there were some contracts being used as storage, called by delegatecall, then dumped into memory, a couple may be disrupted. Did not quite finish analysis, since it wasn't pursued. **James Hancock** asks if it's included in YOLO if that work could be integrated. **Martin** doubts it's ready to be merged into YOLOv2.

**Greg**: what we're running now is ready to go, and no one has any issues.

**James Hancock**: so the changes are a bit complex, probably more work than necessary for YOLOv2, but now if **Greg** agrees that the changes should go through, then can we say this is the new consensus?

**Greg**: There was one PR merged, than the other is complex, and I had some ascetic concerns, and it's on the table. **Martin** mentions **Pawel Bylica** and **Alex (axic)** as the experts.

**Alex (axic)**: If the question is if I'm still in favor of the restriciton, the answer is yes.

**Pawel Bylica** confirms his support of the changes too, but adds that he hasn't been keeping track of the conversation, and would need to update himself on the status. **Martin** says it was implemented in Open Ethereum, but adds that it adds overhead for jumping, and makes the EVM more complex. Thinks it's fine based on benchmarking, but says there's a lot to do to implement in other clients.

**James Hancock**: let's keep original in YOLOv2, and the modified version for YOLOv3. **Martin** concurs, **James Hancock** states this as the general consensus, **Greg** agrees.

**Decisions**
- **96.4**: original EIP-2315 proposal to be included in YOLOv2, modified proposal (including restrictions for jumping in subroutines) to be considered for YOLOv3


# 3. EIP-1559 Update

Video | [1:30:02](https://youtu.be/HUUxwyoxU7k?t=5402)
-|-

**Tim Beiko**: To get the latest, there's a Discord channel, calls, and I update on Twitter. The latest is to try to see what core developers perceive as the major risks. The last update was 6 months ago, then the biggest concern was dealing with blocks twice the size even for a short time, we've been working on this. The next thing to address in addition to building testnets, is seeing if there are any other objections, and figuring out when the next time to bring it to ACD is - what do poeple want to see?

In interests of time, **Hudson Jameson** and **Tim** agree to make this the first item of the next call, **Hudson** recommends ACD chat for answers until then, **Tim** said they tried that but didn't get response, **Hudson** encourages participation.


## Attendees
- Adria Massanet
- Alex (axic)
- Alex Vlasov
- Alexey Akhunov
- Andrea Lafranchi
- Ansgar Dietrichs
- Daniel Ellison
- Danny Ryan
- Dimitry (tests)
- Dragan Rakita
- Georgios Konstantopoulos
- Greg Colvin
- Hudson Jameson
- James Hancock
- James Prestwich
- kelly
- lightclient
- Martin Holst Swende
- Micah Zoltu
- Pawel Bylica
- Peter Szilagyi
- Pooja Ranjan
- Rai Sur
- Sam Wilson
- Tim Beiko
- Tomasz Stanczak
- Vitalik Buterin
- Will Villanueva

## Next Meeting Date/Time

Friday, Oct 2 2020, 14:00 UTC

