# All Core Devs Meeting 107
### Meeting Date/Time: Friday, March 5th, 2021 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Agenda](https://github.com/ethereum/pm#acd-107-march-5-2021)
### [Video of the meeting](https://youtu.be/xWfR-WxjmYg?t=127)
### Moderator: Hudson Jameson
### Notes: Shane Lightowler


## Decisions Made
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
| **1**   | EIP-2315 will be removed from the Berlin scope | [32:42](https://youtu.be/xWfR-WxjmYg?t=1962) |     
| **2**   | Consensus to keep Berlin [test dates](https://github.com/ethereum/pm/issues/248#issuecomment-782106181) the same | [51:12](https://youtu.be/xWfR-WxjmYg?t=3072) | 
| **3**   | EIP-1559 and difficulty bomb delay (EIP-3238) confirmed ok to go into the London upgrade for July. All client teams are comfortable with the timeline. | [1:16:09](https://youtu.be/xWfR-WxjmYg?t=4569)  | 

# Berlin Updates

**Hudson Jameson**: 

* Welcome everyone to All Core Devs meeting #107. 
* Tim Beiko will be stepping into the moderator role from next ACD metting. 
* Hudson to continue attending as back up or netutral party.
* Berlin updates, starting with EIP-2315 (huge topic past week).

## Discussion on removing EIP-2315 from Berlin scope

**Lightclient**

* Opened the [proposal to remove EIP-2315](https://github.com/ethereum/pm/issues/263) from Berlin 3 days ago.
* Didn't open this due to any particular agenda, but does not think it is very useful.
* Seems good on the surface but doesn't address what it claims to. Claims it will bring more efficient contracts to mainnet. Solidity shows the gain is minimal. There are things we could do instead. 2315 claims to improve static analysis. It doesn't change what we have today in a big way but increases complexity in code.
* People who oppose removing it seem to be saying that due to not wanting to remove EIPs at the last moment.
* We shouldn't be adding EIPs to mainnet that aren't of use.

**Hudson**

* Re: objections that it is not desirable/could be an attack vector to be pulling EIPs from an upgrade at the 11th hour, how we ended up here, process improvements for the future - these are not going to be the focus of this call. Consensus is however that the process is broken and needs to be looked at.
* What are others' thoughts re: Berlin?

**Peter Szilagyi**

* There seemed to be consensus yesterday that 2315 should stay. Has this changed?

**Hudson**

* Yes

**Tim Beiko**

* Vyper team came out and said 2315 would be useful as a stepping stone to a complete overhaul of the EVM.
* This is unlikely to happen, 2315 may not even be the right stepping stone.
* 2315 may not be very valuable for Vyper in the end.

**Danny Ryan**

* 2315 is not an appropriate stepping stone.

**Vitalik Buterin**

* Even if there is a good stepping stone we should take a step back, evaluate the roadmap and revisit this at a future time.

**Tim**

* Nobody is taking on that revaluation right now. It's unclear why are we doing this? 

**Hudson**

* Decision is for client devs.

**Chris Reitwiessner**

* 2315 doesnt clearly state its goal - it can't be evaluated whether it achieves its goal.
* Participated in modifying the EIP. Goal is to ease static analysis. We ended up disallowing flowing into it.
* Current PoV is that we should allow flowing into it.
* This isn't really negative for Solidity but it does add EVM / debuggers / tools / analysis complexity.
* This fundamentally changes the control flow of EVM programs. Is very difficult to modify.

**Danny**

* Notes that Martin, one of the co-authors, doesn't see 2315 as a stepping stone. It adds technical debt.

[14:34](https://youtu.be/xWfR-WxjmYg?t=874)

**James Hancock**

* More Martin... even if we remove 2315 in the next hard fork, we still have to have it in code, to process for the blocks that it was enabled for, even if it is disabled in future.

**Leonardo Alt**

* 2315 is not very useful as a stepping stone.

**Hudson**

* Keeping in mind that Open Ethereum has a release candidate with 2315 included. Nethermind has a release (with or without block numbers) with it included also.

**Nethermind**

* We'd still need to do a release anyway.

**Tomasz Stanszak**

* Switching 2315 on/off is no problem as is config switch, user configuarable.
* If Vyper are syaing they don't need it, we would prefer not to include 2315.

**Dragan Rakita**

* Same view as Tomasz... if there's no benefit we should remove 2315. It's an easy flag to flip on/off for us.

**Rai Sur**

* We'd need to do another release to take out 2315.
* Abstaining from a view on whether to do so.

[18:08](https://youtu.be/xWfR-WxjmYg?t=1088)

**Peter**

* Have already done a major release but didn't include the Berlin block numbers due to this issue not being closed.
* If decision is to remove 2315 we'd need to do this Monday. Were planning a release today but would need to ensure sufficient time to make the change. It's doable.
* Personal view (not GETH's) - accepting the majority view (assuming we agree no benefit to the change), but not in favour of what has gone down here. Thought the topic was closed. If I had authored an EIP that gets pulled at the last minute in this manner, would question whether or not to remain in this ecosystem.

**Hudson** 

* Share the concern. This does not set a very good precedent.
* Consensus seems to leaning towards removal of 2315.
* Adds tech debt for little to no benefit.
* Assumptions were made based on a benefits case laid out in previous meetings that do not seem to hold now.
* We can do a lot to ensure this doesn't happen again in future.
* Any other views?

**Danno Ferrin**

* Agrees with Peter. Has downstream community consequences. Community willingness to contribute is at risk.
* We are in a position of needing to choose between two awful choices.

**Tomasz**

* Asked over 6 months ago - why arent there clear use cases for 2315?
* Due diligence of consulting the users of the feature has not happened.

**Micah Zoltu**

* Concern isnt so much that this is against process, more so that there hasn't been enough time to properly consider the merits (or not) of the removal.
* As distributed teams it is a challenge to be able to gain input from the right individuals at the last minute.

**Artem Vorotnikov**

* Accepting EIPs isn't about giving badges of honour. It's about improving the protocol.
* We've dodged a bullet here.
* ACD/EIP process is broken. There's nothing inherently bad about u-turning if we decide we don't need the EIP, albeit at last minute.

**Chris**

* History of the EIP is that it has always been in dispute (over the definition)
* Removing 2315 sets a bad precedent and prevents participation.
* There have always been concerns over the EIP. We shouldn't ignore concerns as this discourgaes participation.

**Lightclient**

* Agree with Artem and Chris.
* 2315 would not be accepted given the current sentiment if we'd been discussing this earlier.
* The focus should be on making the protocol the best that it can be. 2315 does not improve the protocal.

**James**

* Feelsbadman.
* [The issue should be added](https://github.com/ethereum/pm/issues/263) to these notes to ensure it can be tracked in future.
* We should commit to coming back to this in 6 weeks to improve the process.

**Tim**

* Praise for Lightclient for raising the issue.
* Lets wait until we have a bit more distance from the issue before we start the discussions on process improvement.

**Hudson**

* Plans to have individuals from the ecosystem acting as liasons to relevtant stakeholders re: EIPs.

**Vitalik**

* We need a better way to get feedback for incoming EIPs at an earlier stage.
* Eg removing of refunds EIPs.
* Need to make it easy for ideas to fail fast. Curious for ideas on how to improve communication.
* Has been posting ideas/EIPs to Reddit to encourage feedback.

**Tim**

* Tim and Hudson picking this up. Hope to announce on next ACD call.
* We need to be more proactive on getting feedback earlier.

[32:41](https://youtu.be/xWfR-WxjmYg?t=1961)

**Hudson**

`Decision #3 is to remove EIP-2315 from Berlin.`

* 2315 is able to be brought back if a new champion were to do so.

**Peter**

* Removing an EIP in this way is uncharted territory due to us not having a test suite with 2315 removed. Risk of consensus fault increases astronomically. Concerns that the client teams will not have time to adequately test.

**Tomasz**

* We haven't got a testnet with 2315 included.

**Peter**

* Yolo v3 doesn't contain test transactions and Yolo v2 was focussed on BLS. Everyone already assumed that this was already working and tested.

**Danno**

* Tests have already been run against the state prior to the withdrawal of 2315. We've verified it works.

**Hudson**

* There's no strong veto against removing 2315.
* We can move on to Berlin timing.

## Berlin timing

[38:16](https://youtu.be/xWfR-WxjmYg?t=2296)

**Tim**

* Ropsten scheduled to fork 10 March.
* All clients needs to release (for 2315 testing) and blog post going out re: Berlin. Seems hard to do in 5 days. Thoughts on schedule?
* Would prefer to move Ropsten back one week. Keep other testnet [dates unchanged](https://github.com/ethereum/pm/issues/248#issuecomment-782106181) the same. Not a strong opinion though. Would need a new block number.

**Hudson**

* Agrees with Tim.

**Peter**

* Doesn't mind postponing Ropsten, but doesn't think forking two testnets simultaneously. Can we do Ropsten 1-2 days prior to Goerli instead of same time? Ropsten Tuesday 16 March?

**Artem**

* Should we push everything back a week (not just Ropsten)?
* What if 2315 is not the only contentious change?

Peter, James and Hudson all strongly against pushing everything back.

**Hudson**

* There doesn't seem to be any questions over any of the other changes?

**Tim**

* Is confident these provide value to users.  

**Afri**

* Would like to keep all dates, including Ropsten, the same.
* We should fork Ropsten asap as a very early testnet.
* We'd need to ensure the correct chain/Ropsten is being mined with someone standing by.

**Danno**

* Ropsten is going to fork no matter what due to zombie miners. Would be good to get more hash power on the new fork.
* Strong preference not to touch the mainnet block number.
* If we want to remove 2315 this late, we need to be prepared to go to extreme lengths to keep the schedule on track. Community impacts could be severe if we push back mainnet.

**James**

* Summarising release candidates - Open Ethereum today/next day, Nethermind Sunday, GETH Monday.
* Afri's plan could work if the same is true for Besu.
* Preference to change test dates as little as possible.

**Tim**

* Ideally we'd want all of the client teams mining Ropsten.
* This way we'd know all teams are paying close attention.

**Micah**

* We could use Nicehash for this?

**Peter**

* We should ensure every client has a miner so that there is consensus between all parties.

**Hudson**

* EF could help here.

**Peter**

* Agrees with Tim. All clients should run their own miner.

Besu, Nethermind (with James' help), Open Ethereum - all confirmed to mine.

[51:12](https://youtu.be/xWfR-WxjmYg?t=3072)

**Hudson**

* Consensus to keep all Berlin dates the same.
* Extra vigilance on the day with all client teams having their own Ropsten nodes, on the correct chain.

`Decision #2 - London test dates to remain as is.`

**Peter**

* Lightclient already updated tests? Can the open PR be merged so that others can pull the updated repo to help with testing.

**Hudson**

* James to help Lightclient get this merged. See if Dimitri can help.

##Berlin announcement

[53:27](https://youtu.be/xWfR-WxjmYg?t=3207)

* Hudson, Pooja, James, Tim, Trent and others working on a Berlin announcement blog post.
* This to be posted to various sources including blog.ethereum.org, mycryptos blog, Status, Nimbus, Gitcoin blogs etc.
* To be published as soon as the client teams release (next week).

# London EIPs

## EIP-1559 - Fee Market Change

[56:41](https://youtu.be/xWfR-WxjmYg?t=3401)

* Tim has linked to the [1559 proposal](https://github.com/ethereum/pm/issues/254) and gives an overview of the technical review and development.

**Tim**

* EIP-1559 is in a good place now. Ready to be included in an upgrade.
* Some work to do - eg update JSON RPC stacks and reference tests.
* [Economic analysis done](https://timroughgarden.org/papers/eip1559.pdf) by Tim Roughgarden.
* Performance testing completed. Everything fine.
* If we are to include this in London, we need to come to a decision sooner rather than later - it's quite a big change. It would be 'the big thing' in London.

**Peter**

* If we proceed with 1559 we should also cover removal of refunds (EIP-3298)/rework of refunds at the same time.

**Tim**

* Which refund proposals should we be referencing? (there are a few)

**Vitalik**

* Not in favour of any phasing out approaches. Has different ideas on how to deal with this. Looking to formalise into an EIP soon. We need more time to review and agree this.
* We can agree on this within 2 weeks.

**Peter**

* There may be a time when both refunds and EIP-1559 are active.
* This is fine as long as in the long term block times stablise.

**Vitalik**

* Gas prices are very high, users are suffering, milions $$ being spent on fees daily.
* In favour of moderate gas limit increase and ensuring that this can happen safely. (less variance is good)

**William Morris**

* Mentioned in Discord - issue with fork choice. Concerned that 1559 does not provide elasticity. Doesn't think 4x is an issue.

**Peter**

* Currently it is possible to create super heavy blocks.
* Even a 10x increase would stop the network.

**Hudson**

* Seems to be consensus to proceed with 1559.
* Miners concerns were heard in [last week's 1559 community call](https://www.youtube.com/watch?v=EdXhL6VR0mU&ab_channel=EthereumCatHerders). Many miners not in favour due to reduction in mining fees.
* Community / Majority seem to be in favour.

**James**

* Ice age delay needs to happen at the same time (around July), so all client teams need to be ready to deliver both.

**Tim**

* Yes, we have March/April to implement and test the EIPs going into London. Testnets in June.

**Hudson**

* Any others concerns re: 1559 in London?

**Tomasz**

* Could we do a separate upgrade release for 1559, with any dependant EIPs to avoid undue delays?
* Should we consider putting any additional EIPs in next upgrade (Shanghai) while we progress London?

**Tim**

* Difficulty bomb delay must be packaged with 1559 as miners could elect not to upgrade otherwise. They could still do this even if the difficulty bomb is pushed back but this would be more work as they'd need to fork a client.

**Artem**

* It's not hard to fork a client...

**Tim**

* True, but to distribute the forked client and to communicate the change out would be difficult.

**Tomasz**

* Agrees with Tim. We should package the two.

**James**

* Agrees with Tomasz. We should minimise what goes into London and use Shanghai for other items.

**Micah**

* Agrees that 1559 and difficulty bomb delay should be packaged together.
* Not comfortable that we are using the delay as a way to coerce others to choose the same fork as us. We should leave this to users to decide.
* Fork-based governance is all about freedom of choice. We shouldnt make it hard to disagree with us.

**Peter**

* Point of difficulty bomb IS to force people in a certain direction so we shouldnt shy away from that.

**Tomasz**

* Difficulty bomb inherent qulaity: When a group of miners want to execute a fork, they also promise to the fork users that they will be capable of removing the difficulty bomb.

**Dragan**

* Agrees that difficulty bomb should be packaged with 1559.

[1:16:09](https://youtu.be/xWfR-WxjmYg?t=4569) 

**Hudson**

* Does anyone oppose EIP-1559 going into London?
No objections. 
* Does anyone oppose EIP-3238 difficulty bomb delay happening?
No objections.
* Does anyone oppose the two changes going into London together?
No objections.

**Peter**

* We shouldn't make it easy to fork Ethereum (due to speculators).

**James and Hudson**

* Are all clients ok with the 3 month window to deliver London?

No objections.

`Decision #3: 1559 and difficulty bomb delay to be included in London targetting July timeline proposed.`

**Tim**

* We should set up Yolo v4 for this as soon as client implementations are ready.
* Any opposition to include EIP-3198 (adds opcode that returns base fee) with 1559 as well in London?

**Vitalik**

* Agrees with Tim re: 3198, will re-write reasoning for this.

**Hudson**

* Let's discuss 3198 in ACD Discord and next ACD call.

**Peter**

* Alexey should be brought into that discussion.

# Gas refund EIPs

[1:25:24](https://youtu.be/xWfR-WxjmYg?t=5124)

**William**

* Strongest motivation for removing refunds is limited capacity. We should be well below that... 1/4 capacity.
* Sceptical that 10x would stop the network.
* Supports increasing the gas limit and 1559/gas target.
* In favour of EIP-3322 in this area.

**Hudson**

* No time for rebuttals on this - post rebuttals in the [agenda topic](https://github.com/ethereum/pm/issues/258) for EIP-3300.
* William is on Eth R&D Discord for questions/rebuttals.
* Goodbye all, thanks for having me do this last few years. Let's all get excited for Tim taking this over. He is going to do a great job. Thank you all, we've another meeting in two weeks on March 19th at 1400 UTC.```

-------------------------------------------
## Attendees
- Hudson Jameson
- Lightclient
- Peter Szilagyi (GETH)
- Tim Beiko
- Danny Ryan
- Vitalik Buterin
- Chris Reitwiessner (Solidity)
- James Hancock
- Leonardo Alt
- Tomasz Stanczak (Nethermind)
- Dragan Rakita (Open Ethereum)
- Rai Sur (Besu)
- Danno Ferrin
- Micah Zoltu
- Afri Schoedin
- Artem Vorotnikov
- William Morris

---------------------------------------
## Next Meeting
March 19th, 2021 @ 1400 UTC




