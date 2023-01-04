# All Core Devs Meeting 108
### Meeting Date/Time: Friday, March 19th, 2021 14:00 UTC
### Meeting Duration: 1 hour 30 min
### [Agenda](https://github.com/ethereum/pm#acd-108-meeting-info)
### [Video of the meeting](https://youtu.be/AclPXsRlgSc)
### Moderator: Tim Beiko
### Notes: Pedro Rivera


## Decisions Made
| Decision Item | Description | Video ref |
| ------------- | ----------- | --------- |
| **108.1**   | EIP-3322 rejected for London. | [42:33](https://youtu.be/AclPXsRlgSc?t=2553) |     
| **108.2**   | EIP-3368 rejected for London. | [1:13:45](https://youtu.be/AclPXsRlgSc?t=4425) | 
| **108.3**   | EIP-3382 will not go alongside EIP-1559 in London | [1:22:01](https://youtu.be/AclPXsRlgSc?t=4921)  | 

## Action Items
| Action Item | Description |
| ------------| ----------- |
| **108.1**   | Promote Rinkeby access lists to community. |
| **108.2**   | Clear up the argument that EIP-1559 needs EIP-3403 alongside for security reasons. |
| **108.3**   | Create an official EIP for EIP-3403 |
| **108.4**   | Formalize The Merge spec for ETH1 clients |

## Berlin Updates - Ropsten/Goerli Forks

### Discussion on Besu Ropsten consensus issue, post-mortems and tests for feature non-inclusion [(1:30)](https://youtu.be/AclPXsRlgSc?t=90)

* **Rai** explained their client stopped importing on Ropsten by mistake because they hadn't fully removed all the references to BLS12. In relation to that, he brought two questions:
1. Is there an expectation for clients to make post-mortem write-ups for *testnet* consensus issues?
  
   **Martin Holst** says he totally would write if his client experienced a consensus issue.  **Hancock** thinks each client Team should assess whether it's valuable for them or others to have a write-up. **Dragan** also thinks it depends on the type of consensus issue.
In general, the group agrees they are good to have, but there was no outspoken commitment. 

2. Tests for non-inclusion - when should we have them? (there wasn't one for BLS12)

   **Micah Zoltu** and others highlight it's a tricky one because the set of things that are not in are infinite  (i.e. where to draw the line?). 

   **Dianno Ferrin** and **Tomasz Stanczak** both suggest some form of back-testing. Specifically, **Tomasz Stanczak** says it's possible to compare test results between latest pre-compile (where it was removed) against the previous. If the former uses no gas, then it can be considered removed. Then he adds that any opcode that has been switched on or off, we can detect (there are tests for it), but anything outside like networking and transaction formats is harder. **Martin Holst** points out doing so may not achieve the intended coverage. So, **James Hancock** suggests to make a note that every time an EIP is taken out, an individual conversation should take place to assess the need for no-inclusion tests.

* Adding to Ropsten issues, **Dragan Rakita** says they (Open Ethereum) only found a bug related to Rust versions, which got fixed.

### Goerli validation and discussion about triggered features [(11:10)](https://youtu.be/AclPXsRlgSc?t=670)

* Goerli validators did good. Nethermind didn't see any problems. 
* **Danny** asks whether we have we triggered at least a version of all the features in one of the testnets. At least **Nethermind** didn't do so. It would be hard work to run the "standard testsuite" on them because there is a lot of work to setup the state in the way we would want for the test. So, **Tomasz** ideates there could be a set of tests that don't validate a specific outcome, only exercises every feature that we can think of, which could be run on all clients with the pass criterion being that all of them behave the same. However, **Martin Holst** doubts the worthiness of deploying synthetics tests on Ropsten/Rinkeby if they can be done on other YOLO testnets. **Tim Beiko** concludes the value in that case is in the amount of time the testnets are available for use.
* **Micah Zoltu** brings up the concern that Ropsten is the only net where we test PoW before mainnet. **Tomasz** thinks there is no huge need in this case, unless something substantial like difficulty changed in London. There is general agreement that there it isn't highly concerning. 

### Rinkeby and getting community to know access lists [(17:24)](https://youtu.be/AclPXsRlgSc?t=1044)

* **Tim Beiko** asks whether something can be done in advance for Rinkeby. **Tomasz** recommends advertising with the community, show how access lists work and encourage them to try them. Prepare people to understand what tooling they can use and how to change them. **Micah** doubts anyone is interested in access lists, but **Tomasz** says everyone could be interested because of the involved gas savings. **Vitalik** confirms most people do benefit from gas savings even if only a little. He also adds access lists enable database accesses in parallel which potentially increases scaling.

## Proposals related to [Included London EIPs](https://github.com/ethereum/eth1.0-specs/blob/master/network-upgrades/london.md#included-eips)

### Gas Refunds Alternatives

#### EIP-3403 - Partial Removal of Refunds [(23:00)](https://youtu.be/AclPXsRlgSc?t=1380)
* **Vitalik** explains his proposed EIP-3403. He favors it over EIP-3298, which was very as barebones and had some concerns around it. EIP-3403 doesn't have those concerns and still meets two key goals of 3298. First, it preserves the invariance that the amount of gas for execution has to be bounded by the block gas limit. Second,  it renders gas tokens useless since you can't use storage as a battery anymore.

#### EIP-3322 - Efficient Gas Storage [(25:40)](https://youtu.be/AclPXsRlgSc?t=1540)
* **William Morris** presents EIP-3322. One of his main arguments in favor for it is reduction of state bloat. **Piper** objects to that, saying that removing incentives to clear the state isn't a problem because we're looking at an expiring cold state; we're not currently looking for a mechanism that reduces state bloat. **Vitalik** adds that soon having incentives to clear storage will become in fact useless (not just superfluous).
* **Martin Holst** and **Danno Ferrin** think it's totally out of scope for London. **Geth** and **Nethermind** also argue the change is more complex than it appears. Several Devs agree it isn't realistic to implement for London.
* **Beiko** asks if anyone would potentially consider it for Shanghai.  Some devs such as **Artem Vorotnikov**, **Danno Ferrin** and **OpenEthereum** suggest it shouldn't even be considered at all. 

#### Client-side thoughts between EIP-3403 and EIP-3298 [(44:00)](https://youtu.be/AclPXsRlgSc?t=2640)
* Earlier, **Artem Vorotnikov** argues EIP-3298 is the simplest, most straight-forward. Therefore, he suggests going with it. **Dragan Rakita** concurs. However, at another point in the meeting, **Martin Holst** argues that EIP-3403 is not much more complex to implement than EIP-3298. **Tomasz** thinks the only benefit of going for 3298 is it removes gas refunds entirely, making future implementations simpler, but admits it can be done later if needed. It is then noted that EIP-3403 does not prevent us from doing EIP-3322 in the future, as it is forward compatible with everything. In general EIP-3403 gets more acceptance.

#### Bringing 3403 into London [(46:00)](https://youtu.be/AclPXsRlgSc?t=2760)
* **Micah** says he is for the EIP but really doubts it's necessary in London, given that 1559 can go perfectly fine without 3403. **Martin** argues that not including 3403 could incur a security issue related to increases in block processing time with refunds enabled. **Micah** points out that the argument has been brought up many times and is fuzzy, requests a more elaborate explanation. He argues that we're not currently constrained by block processing time (unless it's average BPT). **Martin** will work on explaining the argument better.
* The consensus seems to tilt towards getting EIP-3403 to CFI (Consider For Inclusion). **Ansgar** then proposes it should be default for inclusion in London unless it's proved not to be a security concern. **Tomasz** recommends rather defaulting it to not included, but promising to workout the security concern question. **Beiko** thinks whether it's default in or out doesn't make a big difference over the next two weeks, proposes everyone think through the EIP and making a decision about that on the next call. Finally, **Micah** underscores it must first be made an actual an EIP, as it's currently just an idea without a draft. Then be reviewed, before getting into CFI. 
* **Vitalik** reminds that an open question is also what number the refund will be set to.

### EIP-3198 - BASE FEE Opcode #270 [(55:45)](https://youtu.be/AclPXsRlgSc?t=3345)
* **Tomasz** thinks it's simple enough, but not critical for London
* **Ansgar** is concerned that after London and Shanghai the next feature fork would come in a 24 month horizon, but it'd be nice to have this opcode before then. **Beiko**, asks to come back to it later in the agenda when we discuss Scope.
	
### Michael Carter explains EIP-3368 (increase block rewards to 3 ETH, with 2 Year Decay to 1 ETH) [(58:40)](https://youtu.be/AclPXsRlgSc?t=3520)
* **Michael** starts off with an apology about tension and language used in the 1559 discussions. Then he explains the EIP is meant to address existential risks to the network. He is concerned about security and Ethereum dominance in the event of price fall and (mining) yield reduction. He acknowledges his EIP seems like "printer goes BRRR" at first sight, but wants to make sure all measures for security are considered up until the merge. He is open to discussing offline other possible measures such as MESS (Modified Exponential Subjective Scoring). Lastly, he admits that with the rescheduling  of the merge event to an earlier date it may not make sense to bring such a change forward. 
* **Michael, Tomasz, Vlasov, Beiko, Hancock, Danny** exchange thoughts with the main message that (1) it's important to have the discussion (2) it is better to avoid playing with issuance, which could back-fire (3) it's an unlikely event (4) it is important to have something in the back-pocket if it does happen. (5) There is a much simpler and readier alternative, which is just changing the reward without decay.
* **Beiko** finally concludes that there aren't Devs advocating EIP-3368 to go into London as is. 
	
### EIP-3382 - Hardcoded Block Gas Limit #281 [(1:14:40)](https://youtu.be/AclPXsRlgSc?t=4480)
* EIP-1559 may incentivize miners to grow the block size, which they currently control. **LightClient** pushes EIP-3382 to remove their ability to raise or lower the gas limit, hardcoding it to 12.5M. **Tomasz** stands strongly opposed, arguing that historically there has been a good behavior from miners, and that it balances power between Devs and Miners. **Vitalik** echoes Tomasz, adding that there is also not a huge economic incentive to deliberately grow the gas limit. A few others generally agree. **Danny** suggests keeping it in the back pocket.
* Seemingly opposed to the rejection, **Hancock** says we should go for a kind of gas limit but maybe not for London, and have the limit set by those who understand the nuances of state growth the best. **Tomasz** responded that, with the next few hardforks all reserved, there will never be a chance to increase the hard cap if it's fixed. 
* **Beiko** notes that this change could also be done in a soft-fork without miner support if ever needed. Finally, asks for consensus, and draws the conclusion that EIP-3382 shouldn't be included alongside 1559 in London.

## Network Upgrade Timing & Scope [(1:22:30)](https://youtu.be/AclPXsRlgSc?t=4950)
#### London #245
* **Beiko** summarizes the dilemma around inclusion of EIPs in different hard-forks and the scheduling of The Merge, underscoring in general it's accepted we want to keep London lean, since EIP-1559 is complex enough on its own.
* **Tomasz** suggests lean London for July and Shanghai shortly after in October to include the minor EIPs. Then, possibly do The Merge in January with Cancún. However, **Danny, Mikhail** and **Ansgar** share the similar opinion that The Merge and the PoS promise is way more important and should take precedence over any of the minor EIPs. 
* **Ansgar** mentions that, from his understanding, one of the main roadblocks to merge is ETH1 client attention, so shifting to that gets us to merge earlier agrees to commit to Shanghai for merge. This brings **Micah** to ask whether we have a spec for ETH1 clients to go implement, because if we don't let's not even discuss The Merge. **Mikhail** says currently they only have the spec as a PoC and they're working on the spec. 
* **Beiko** draws brief conclusions for the meeting. For London we haven't committed to include anything beyond EIP-1559 and the EIP-3238 difficulty bomb pushback.  Got to clear up in the next call the scope of London/Shanghai and the timing of The Merge
* **Danny** lastly shares there will be discussions about The Merge taking place bi-weekly on Thursdays (next one on April 1st). He invites an engineer from each team to join.

-------------------------------------------
## Attendees
- Afri Schoedin
- Alex Vlasov
- Ansgar Dietrichs
- Danno Ferrin
- Danny Ryan
- Dragan Rakita (Open Ethereum)
- James Hancock
- Lightclient
- MariusVanDerWijden
- Martin Holst Swende
- Micah Zoltu
- Michael Carter (BitsBeTrippin)
- Mikhail Kalinin
- Rai Sur (Besu)
- Tim Beiko
- Tomasz Stanczak (Nethermind)
- Vitalik Buterin
- William Morris

---------------------------------------
## Next Meeting
April 2nd, 2021 @ 1400 UTC



