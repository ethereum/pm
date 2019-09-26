# Ethereum Core Devs Meeting 71 Notes
### Meeting Date/Time: Friday 20 September 2019 at 14:00 UTC
### Meeting Duration: 1.5 hrs scheduled, 1 hour actual
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/125)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=OjJd2G0pmeM)
### Moderator: Hudson Jameson
### Notes: Jim Bennett

----

# Previous Decisions

**DECISION 70.1**: ~~Leave Blake 2 as Blake2b, keeping it fixed to 12 rounds.~~
Revised at the end of the call -- Update the EIP to reflect the precompile addressing a superset of BLAKE2b, leave the `rounds` parameter as-is in the EIP, further discuss the inclusion of an `m_len` parameter with client implementers on Gitter.

**DECISION 70.2**: The fork of the Ropsten Testnet is set for the 2nd October 2019 and block that corresponds closest to that date will be selected.


## ACTION ITEMS

**ACTION 71.1**:  David Palm will talk to Wei Tang to see if 2200 should be self-contained.

**ACTION 70.2**: Ethereum Cat Herders to create a communication that describes all changes and highlights the concerns around EIP-1884 and provide it back to the All Core Devs for review before it is put out to the community. This document will be released when every client has completed the Istanbul updates and has a block number.

-----
## AGENDA

## 1. [Istanbul related client updates](https://notes.ethereum.org/@holiman/SyT_rGjNr)
[Timestamp - 04:37](https://youtu.be/6m0So81_j2Q?t=277)

### Geth

**Martin**:

- Released new version of Geth to testnets on 9/19. Discovered an issue concerning miners and fixed it on 9/20.

## Nethermind

**Tomasz**

- Not many changes since last time. Merged. Updated the dock numbers. Completing tests for an announcement before Istanbul - so far, tests are all green.

## Trinity

**Piper**
- All Istanbul features completed.

## Aleth

**Pawel**

Not everything is finished yet. Working on Blake2 (EIP 2024) now. Release not yet scheduled.

## Besu

**Pawel**

Will do the 1.2.4 release on 9/23, and it will be the first release under the Besu name.

## Parity

**David**

Merged all Istanbul EIP changes. Will probably release on 9/23 or 9/24.

**Hudson**

Reviewed Action Item 70.2. Picked block numbers for Istanbul:
Ropsten - 6485846 - October 2
Gorli - 1561651 - October 30
Rinkeby - 5435345 - November
Kovan - 1411141 - December

Blake2b EIP update:

**Alex**

Discussed EIP 2200 re: gas metering. Most complex EIP that isn't merged yet. Blake2bf is merged. Discussed net gas metering for SSTORE - 4 or 5 comments on PR were left unaddressed.

**Martin**
Closed about 2300 tests in the EIP. The first step is what differentiates 2200 from 1283.

**Alex**
Asked if GO Ethereum is used to generate the new test cases.

**Martin**[https://youtu.be/OjJd2G0pmeM?t=1047]
Yes. Using GETH to generate initial consensus tests. Geth is highly consistent with Parity in over 7 million test cases. Aside from that, 10,000 test case were exported. Found a hit on Besu that added flaws for 2200. Some clients are using less than and others are using less than/equal to. There are test cases to cover these conditions.

**Alex**
Asked if it would be a good next step to make sure that the EIP accurately reflects what GO Ethereum is doing. Martin agreed.

**Alex**
Discussed the two major things people are confused about: 1. Awhile ago, it was agreed that 2200 should be self-contained, but some sections still refer to other sections. 2. Compared to 1283, the biggest change was to reflect the SLOAD cache change. The cache change isn't reflected in the appendix and some other parts.

**Hudson**
Hudson asked David to talk to Wei to see if 2200 should be self-contained. David agreed to do so.

**Alex**
None of the EIPs apart from the chain ID are in the final state. Covered the process of moving EIPs to final state as defined by EIP 1. They should move through this last oral process first and then they can be adopted. Asked for people to agree on this call for some of them to be moved to final. Proposed that the EIPs 152, 1884, and 1108 be moved to final.

**Hudson**
All agreed to put all EIPs into last call until 9/24 and then move into final after that.

For EIP 1344, there is an update on how the opcode returns a 256-bit value, and Parity and Trinity might be affected by this.

**Martin**
The only case this would ever blow up is if someone had a private chain where they set the chain ID to some silly large number.

**Matt**(https://youtu.be/OjJd2G0pmeM?t=1643)
Said he just wanted a quick summary to address nomenclature, and that the issues were addressed.

## 2. Testing Updates

**Martin**
Some of the consensus tests have been made, but there has also been change in the test format. Geth, Parity are having some problems with them. We're done fuzzing, and he wrote a bit about it in the PM. There are also updates happening regarding the libfuzzer. Hoping to have it up over the weekend or early next week. Got a new server for Hive. Conducting Nethermind testing and fizz testing as well to implement better standard JSON trace output. From a fuzzing perspective, satisfied so far.

**Trent (Whiteblock)**
Whiteblock is hosting multiclient testnets as a step before doing a public testnet. What we're doing with the Whiteblock Genesis Platform is what we're doing with Eth2. Can also run specific contracts to make sure they're going to work, specifically in the case of 1884. After gathering and analyzing data, we can run different testnets iteratively.

**Martin**
Asked if those testnets are bootstrapped from an existing testnet.

**Trent**
Said he thinks they're going to be clean. The way it's been done in the past is that there's a genesis file that instructs what sort of information to start with.  

**Martin**
Asked what the difference is between this and just launching a public testnet.

**Trent**
It's meant to be a lightweight, iterative system that can be started up and torn down quickly without a lot of coordination from other people.

**Tomasz**
When they set up an Istanbul testnet yesterday with the chain spec of the AllCoreDevs that created 5000 empty blocks, they had to coordinate with many others. So the Whiteblock system will be good if it doesn't require that kind of coordination.  

**Trent**
The Whiteblock product allows you to preload wallets and set up accounts beforehand. They're to abstract away the process of kickstarting to a YAML file. Very similar to puppeth, but "puppeth on steroids." In the future, it will be a user-friendly web UI to run test cases with all the backend taken care of. It also intorduces adversarial conditions - i.e. pump up the latency and still see if things will come to consensus.

**Martin**
Said that he hoped he could get the Geth node on Tomasz's recently started testnet by the end of the week.

**Tomasz**
Noted that on Genesis, Whiteblock previously only had support for Parity and Geth and asked if these things are set up for Istanbul for all remaining clients.

**Trent**
Right now, they also have support for Pantheon and Besu, so they have enough support for a multiclient testnet. They do have to update to the Istanbul spec, but that shouldn't be too difficult.

**Tomasz**
Asked if they would have support for Trinity, Aleth, and Nethermind.

**Trent**
Whiteblock currently doesn't have those, but ideally they would support all Eth1x clients.

**Hudson**
Said to reach out to Trent if there are any additional questions - usually, it would be Zack, but he's getting ready for his wedding.

## 4. ["Ethereum Roadmap 2020: A Community Discussion" @ Devcon5](https://docs.google.com/document/d/1pD9RxQcgI4hBoOWGWlVwg4JqNS19_YIUnr3HsftHtE8/edit?usp=sharing)

**Hudson**
This year at Devcon, there's not going to be a Day 0,1,2, and 3; it's going to be Day 1, Day 2, Day 3, and Day 4.

For Day 1, there's not going to be a mainstage with speakers on it. It's going to be divided by partitions, where there are going to be different workshops, seminars, and groups held.

This Ethereum Roadmap 2020 Community Discussion is going to be on the 8th from 1-5 in the convention room that has a 200-person capacity. It's going to talk about the the technical roadmaps for Eth1 and Eth2 and the transition from Eth1 to Eth2. The link above has the format and the schedule. It ends with working groups, and it starts with the  overview and the Eth1 roadmap. Hudson is doing a talk on Eth1x, so he will probably be the point on the Eth1 roadmap unless he gets pulled into something and he has to find someone else.

There is a link to the [full schedule](https://docs.google.com/document/d/1jy3l0bnKXC6AZdyFVBne4go9oe58bTZmMdUGb4Dj8bs/edit#) of community sessions on October 8th under "Schedule." If you want to help with this, please participate and join in. Jamie Pitts is one of the organizers, and so is Annette. Maria Polla is the MC.

## 5. [Both ProgPoW Audits Released](https://medium.com/ethereum-cat-herders/progpow-audits-released-ed4973ebe073)
Both ProgPoW audits were released right after the last CoreDev meeting. There is a [blogpost from the Cat Herders](https://medium.com/ethereum-cat-herders/progpow-audits-released-ed4973ebe073) that discusses everything about the release.

## 6. Review previous decisions made and action items

**DECISION 70.1**: ~~Leave Blake 2 as Blake2b, keeping it fixed to 12 rounds.~~ Alex was going to talk to the EIP 152 champions to discuss the concerns, so Hudson thought some of this might have changed, but it was left as is.

**DECISION 70.2**: The fork of the Ropsten Testnet is set for the 2nd October 2019 and block that corresponds closest to that date will be selected. This has happened.

**ACTION 70.2**: Ethereum Cat Herders to create a communication that describes all changes and highlights the concerns around EIP-1884 and provide it back to the All Core Devs for review before it is put out to the community. Once we have it so we're ready to take comments on it, it will be put in the All Core Dev channel and make sure everything's good.

**Hudson**
EthereumJS has a release version 4.1.0. of the VM with full-featured Istanbul support, even though it is still labeled as beta.

## 7. Any other items

**Bob**
One thing to note on ProgPoW, in terms of the EIPs tagged for Berlin, there's been a sweep of things forward such that ProgPoW is currently tentatively accepted hinging upon the security audits.

**Hudson**
The security audits haven't been fully investigated by anyone in the Core Devs that have come to him, but he also hasn't heard anyone bring up anything groundbreaking about the audits that would be a showstopper.

**James**
The list of tentatives was more accepted for Berlin. The "tentatively accepted" was for this first fork. That's where the word "tentative" came from.

**Danno**
Regarding investigating the audits, from the hardware audit, there isn't anything unique to ProgPoW. Each hash has the same vulnerabilities. There's one question in the Least Authority audit:  Suggestion One concerning putting padding at the end of the Keccak hash. Reached out to @ifdefelse on Twitter, and they replied that they are confident that they don't need it. It's mostly there to provide uniqueness, and they stated that in the context of what they're doing with repeated use of it, it doesn't really have any security impact, which satisfied Danno's concern.

**Hudson**
He is collecting community sentiment on that. This is not a Cat Herders thing; this is just Hudson collecting arguments and laying them out. There are a lot of loud people, or at least a group of loud people - it's hard to tell which - that don't want ProgPoW anymore due to some political stuff, as well as a few arguments that are technical. He is collecting them and has over 55 Twitter and Reddit links.

ETC recently had some drama over ProgPoW, which spearheaded part of the sentiment collection.

**Danno**
With that list, it will be useful to identify ones that are new since February or March versus those that are repeats of the same arguments.

**Hudson**
Scott Lewis put together a good Trello board.

**Trent**
Asked Danno about the Keccak modifications - could the authors write up a public address of the audit concerns?

**Danno**
The extent of the interaction was the Twitter exchange. It has been copied into the ProgPoW review room. It is in the log, and Danno can post it again, and he agreed to send Hudson the link.

**Trent**
Would the Core Devs on this call consider integrating ProgPoW but not actually implementing it?

**Hudson**
Until we re-approach the entire issue, that probably can't be answered because it's already in accepted state, so from a process perspective, no.

**Martin**
ProgPoW 0.9.2. has already been merged into Parity and will be merged into Geth.   

**Trent**
It's a broader issue than the technical implementation. It's a more nuanced conversation about the transition fro Eth1 to Eth2 and how ProgPoW could be a dissuasion to interrupt the deposit contract, keeping it in our back pocket to be used later if necessary. It's already being intergrated into clients, but the alternative is to keep it integrated but not activated until such a time as its very much needed.

**Hudson**
It's too early for the alternative, and the previous screaming about it has died down. We're now collecting sentiment about it.

**Trent**
The disconnect is that the Core Devs are approaching it technically, and a lot of the outside concerns are political. It would help to have both sides understand each other better if the Core Devs responded to some of those political ideas.

**Martin**
The problem is if we keep ProgPoW in our back pocket and something happens where we need to activate it, that switch cannot be done in a day or an hour. It can be done over maybe two weeks.

And once the decision has been made to do that, all the existing miners will know they're going to be kicked out, and they're going to do whatever they want with the chain, because their investment is going to be worthless. They can do the continual rollout of new chains during the two weeks while the switch is being made, and the actual value of Ether is going to plummet during those attacks.

Eventually, if we manage to do the switch to ProgPoW, we may discover that there is no mining forum that is able and ready to pick up and switch over to actually mine Ether at full scale. They're doing other things. They've moved on. The only ones willing to mine Ether if the value plummets will be pump and dump gangs, and shenanigans will happen. So keeping it in our back pocket is not something that is going to play out well.

**Danno**
Some of the political discussion has been attacks on the AllCoreDevs, who are not burying their heads in the sand, but they are not engaging in the political process because they don't see the constructive nature of what's been going on.

**James**
This question does a disservice to the Cat Herders who, nine months ago, did much of this process already and, at that time, they were thinking about those political things and explicitly discussed them on the AllCoreDevs calls.

**Trent**
Wanted to give a bit of context as to why people were bringing this up again and have their voices heard. Just trying to bridge the different parties into understanding a little bit better.

**Hudson**
There is new political drama. He will do the new sentiment collection. Please keep it civil. If people are loud and angry, it will be hard to take them seriously.

**Trent**
In the side chat, Bob and Matt have both said that ProgPoW being introduced would be likely to cause a chain split. No idea how serious this is, but he's heard it enough times that it's worth mentioning.

**Danno**
That's an argument that the numbers didn't support when we did a miner poll. With 70% participation, they were 100% in support of it. Not a single miner took the time to do a negative vote. If there were a single miner that took the time to put a negative vote in, he would put more weight on that argument.

**Tim**
Checked yesterday, and there's still a decent amount of miners signaling yes on ProgPoW. Not sure what the percentage is, but the miners who were voting yes have not removed those votes.

**Bob**
The controversy is not necessarily on the mining side but on the user side. If there was a chain split, it would be an ETC-style one of user rebellion and then mining building up to support that.

**Danno**
Earlier this year, that was almost a user rebellion in favor of ProgPoW.

**Hudson**
Yes, that almost happened, and that one actually had code behind it. Hudson will mention it in his sentiment collection if he sees any brew attempts or plans or preparations for a chain split. Forking is one of the great things about blockchain, because if you don't agree with something, you can leave.

We do try to keep politics out of the CoreDevs calls. It is inevitable sometimes, and most of us have addressed that fact.

Martin had mentioned that Geth is on 0.9.3, but Hudson thinks it is on 0.9.2. Martin said it might be. Danno said it's easy; it's just a few parameter changes.

Discussion about whether or not we are meeting in two weeks. People agreed to meet, with Tim running the agenda. We can change our minds if there's not much on the agenda.


# Attendees

* Brent Allsop
* Alex Beregszaszi
* Bob Summerwill
* Daniel Ellison
* Danno Ferrin (Besu-Hyperledger)
* David Palm (Parity)
* James Hancock
* Jim Bennett
* Martin Holst (Geth)
* Matt Luongo
* Pawel Bylica (Aleth)
* Piper Merriam (Trinity)
* Tim Beiko
* Tomasz Stanczak (Nethermind)
* Trent (Whiteblock)

# Date for Next Meeting: 4th October 2019, at 1400 UTC.
