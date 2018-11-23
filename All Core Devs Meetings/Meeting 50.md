# Ethereum Core Devs Meeting 50 Notes
### Meeting Date/Time: Fri, November 23, 2018 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/62)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=wfxvCEhglTM)

# Agenda

1. Discussion about openness and roadmap discussions in Prague
1. Testing update
1. Client updates
1. Research updates
1. Constantinople, testnet hard forks
1. Goerli update
1. ProgPoW update

Call starts at [[5:55](https://youtu.be/wfxvCEhglTM?t=355)]

# Discussion about openness and roadmap discussions in Prague
NOTE: I didn't take thorough notes in this section yet as I was dealing with some audio/streaming issues. Will try to improve the notes later, but please feel free to submit a PR to contribute!

- Alexey
    - I can't cognitively communicate with the entire community
    - Nothing new happened here, we've been working on EIPs for ages
    - Are we discouraging people to go to Magicians? This isn't true
- Afri
    - Out of 250 people at EthMagicians in Prague only 2-3 identified as core developers
- Hudson: [missed this]
- Greg
    - The notes were public and looked published to me
    - Four meetings over the course of several days do not look "ad hoc" to meet
    - Who was invited? There was no notice even on core devs
    - We are a public project, and we cannot have private conversations
    - It doesn't look like an ad hoc meeting; make a recording or a transcript
    - We must get comfortable with working in public; if you don't want to, find another project to work on
- Hudson
    - We want a channel for core devs to communicate without inviting the media
    - It means people don't speak up about their actual intentions
- Peter
    - As a developer I feel that I cannot say things openly without Coindesk misinterpreting everything I say and taking it out of context
    - Then instead of having open discussions, people start withholding their opinions because they are afraid of the media backlash
    - Maybe that's something we need to learn to live with as Greg says
    - But it's a problem that people are afraid to speak their minds
- Afri
    - The solution is Chatham House rule, don't attribute to specific people
- Alexey
    - I need to get caught up, cannot do this in public, need to be able to ask dumb questions in smaller group
    - Then produce high quality EIPs later
- Peter
    - Could have been discussed during EthMagicians?
        - Yes, better opportunity
        - But I hate it when a conference turns into a two week event
        - I couldn't make EthMagicians
- Fred
    - I don't personally understand the purpose of the EthMagicians meetup, I thought it was more political than technical
- Lane
    - The conversations started ad hoc and in a small group
    - The point of DevCon is to facilitate "watercooler" conversations, not all of which should be open or recorded
    - We all agree that small, sidebar conversations with e.g. two or four people do not need to be "open", recorded, livestreamed, etc.
    - But it's unclear where the line is
    - What happens when you're in the moment and the scope and attendees set has expanded?
- Alex
    - First couple of gatherings were ad hoc
    - People opened up a lot
    - Many of these folks are not familiar with EthMagicians
- Hudson
    - I disagree with Greg that everything that can be open always has to be open
    - It's detrimental and means that people won't be open
    - Working groups can be private
- Greg: You can, you just have to consider what will happen
    - There were four meetings
    - It doesn't look ad hoc
    - 15+ people per meeting
    - Looks like an organized series of meetings
    - Someone should record on their phone and make a transcript if it becomes an important meeting, even if it wasn't intended to be
- Fred
    - I disagree it was important, I don't think it was important at all
    - These conversations happen all the time at Parity and on the geth team
- Peter
    - I agree with Fred, it wasn't an important meeting
    - We were trying to figure out who needs to collaborate to come up with a proposal
    - E.g. how do we collect data on the state trie size
- Hudson
    - I said to every working group member, hey, how's your working group going?
    - "I'm having reservations on how open the meeting on the 30th should be, we said we wanted it to be private, but I think maybe it should be more open. Here are some options..." notes taken, published, livestreamed, etc.
    - Some potential for meeting and notes to be more open but we didn't have time to work this out
    - For the meeting on the 30th, does this need to be somewhat closed?
- Alexey
    - I'm okay with releasing whatever we've got
    - What I want to avoid:
        - There are certain things in the material that might start a "witch hunt" e.g. gastoken, charts about which contracts consume storage - goal is to NOT blame certain developers of contracts that consume a lot of storage
        - If someone reads this doc they might think "OMG, Ethereum is doomed" - I don't want this to happen either. We have to present it in such a way that it's not just a problem statement, it's also a solution.
    - I'm happy to release it but I'm not even comfortable that all the data is correct
    - "I have more data but only comfortable to release these data because I've double checked and I'm sure they're correct" - someone may suffer from releasing bad data
- Hudson: How do we handle the call on the 30th?
    - Presentations of the working groups
    - Data points we can use to write Eth 1.x EIPs
    - Greg: What do the people doing the presentations want to do?
    - Hudson: Mostly wanted it closed, since not sure of their research as Alexey mentioned, or think that sooner or later the topics will come up with the all core devs chat
    - Could start a thread on EthMagicians forum instead
    - I'll put meeting link in AllCoreDevs channel but won't record or livestream it
        - Media not invited; I'll kick people out who are not core devs
    - Further interaction should happen on EthMagicians forum
- Alexey
    - I personally would say what I think anyway
    - I'm not personally bothered by open- or closedness
    - But I'm trying to protect others who are bothered
    - I don't belong to any of these big organizations that are invested in future of Ethereum
    - So I can say whatever I want
    - But I have to be very careful about working with other people
- Hudson
    - Working group leads should post a thread on EthMagicians, or forum of their choosing to discuss their findings
    - Call will be open only to core devs invited via AllCoreDevs channel
    - Notes will be taken, don't have to be made public
    - Call not livestreamed or recorded
- Greg, Afri: sounds very strange
    - Greg: Once there are meetings across groups, it shouldn't be secret
    - Press will report whatever they can find, it won't be complete or accurate
- Alexey: If no one else is arguing for it to be closed, let's make it open
- Peter: I can speak my mind more easily if I know there's no recording, no press
- Afri
    - If you make it private you must make sure it's announced so that people who aren't invited at least have a chance to ask to be included
    - If you take notes, you can't keep them secret, this is open source software and protocol, we have a disenfranchised community and we are trying to keep them involved and cannot argue that our governance is decentralized if meetings are unannounced and private and notes not shared
    - Private meetings are fine but announce them and share notes
    - They can be unattributed
- Hudson
    - Core devs invited
    - It's hard to define
    - But if you're not considered one by a majority of people present
    - Or haven't been to other meetings
- Fred
    - Meetings and work just happen
    - Especially at conferences
    - You just start talking about something
    - How do we proactively plan for each meeting with proper disclosure?
- Afri
    - If you agree ahead of time on a time and take notes and decide you can't invite everyone, that's different
    - Than just an ad hoc conversation
- Lane
    - We agree that true ad hoc, sidebar conversations don't need to be announced and recorded
    - And on the other side of that line, if there are e.g. 25 people in the room and it's planned for, that's different
    - I'm confused where the line is, it's very subjective
- Hudson
    - For my purposes definition of core devs is working on low-level projects
    - There is a grey area including teams such as Infura working on low-level RPC
    - For now, meeting on 30th is not closed but may be closed to anyone but core devs
    - Notes may or may not be released
- Lane: I don't think anyone would complain if we take/share notes that aren't attributed

# Testing update
- [Martin update](https://github.com/ethereum/pm/issues/62#issuecomment-441173179)
    - Two evm fuzzers are (still) running. No new issues found in the last couple of weeks.
    - One testcase found by fuzzing has now been added to the tests-repo. It affected geth and ethereumJ (at least), and concerned EXTCODEHASH in a fairly complex edgcase scenario.
    - Hive is currently down for maintenance, I have some hopes that we'll get it working again during the day. Hive has been moved into the ethereum org (https://github.com/ethereum/hive/), and a new geth-team member @FrankSzendzielarz have been working on improving it further, with a test-suite for p2p networking as well as support for more advanced multi-cllient test suites.
- Adrian Sutton
    - Good progress being made on EXTCODEHASH tests, awful lot of green on the board
    - Some tests still coming, hopefully we can fill them in in the coming week or two

# Client updates
- Parity (Fred)
    - No major update
- Geth (Peter)
    - Tiny performance update
    - Playing around with caching
    - Full sync up to 15% faster, 30% faster block processing after sync
    - Disk I/O reduced almost to zero during normal block processing after you're in sync
    - Martin found nasty bug we had for a year, affected only if you ran with insane cache allowances, may or may not have influenced pruning efforts
    - Pruning algo implemented since summer, some corner cases we didn't manage to find cause for, this bug may have been causing it
    - Will pick up pruning effort again and see if it works as it should
- Harmony (Mikhail)
    - Released EthereumJ/Harmony with fixes related to Ropsten Const. HF
    - Spun up a couple of nodes to participate in Stureby testnet, used to test cross-client transitions to Const.
    - Haven't spent too much time on Eth 2.0 spec
- EthereumJS (Alex)
    - Holger released new version of VM with full Const. support
    - Last release of solc comes with support for Const. opcodes
    - Once Remix and other frameworks pick up both of these then end users and devs will be able to test Const. changes outside of chains as well
- Aleth (Pawel)
    - No update
- Nimbus (Jacek)
    - Focusing on Eth 2.0 stuff for now, no other updates
- Nethereum (not present)
- Pantheon (Adrian)
    - Thanks to everyone who gave us a great reception since our release
    - 0.8.2 release with some fixes to issues folks reported
    - Gorli and Stureby testnets very useful in getting things working
    - All on track for Const.
- Trinity (not present)
- Mana (Exthereum)
    - Progress good, near complete syncup
    - Working on warp sync, PoW, performance
    - Target Q1 2019 for early full client
- Tomasz ([which client?])
    - Participate in testnets
- Hudson: progress tracker moved to wiki
    - Fully filled out
    - https://github.com/ethereum/pm/wiki/Constantinople-Progress-Tracker
- Ewasm (Alex)
    - Testnet launched at DevCon
    - Community call last Thurs., showing demo of running a client and interacting with testnet (deploying contract)
    - All of this is documented
    - https://youtu.be/vj6o6UCfyIY

# Research updates
- No update, no one present

# Stureby testnet and Const. HF testing
- Afri update
    - Martin proposed it this week in AllCoreDevs channel
    - To have a PoW testnet to redo the Const. HF
    - I created chainspec for Parity, relaxed HF schedule a bit
    - We are at block [?] now, on Mon or Tue. at block 40k we will activate the fork
- Peter
    - I've been out of the loop on this new "fork net"
    - During Ropsten HF, clients started to behave strangely when heaviest chain was non-forked chain
    - If we want to do a fork test, one interesting data test would be to have a miner not fork and continue to produce blocks - and be more powerful than fork miners - could surface interesting corner cases
- Adrian
    - Sheer weight of peers on other chain could cause you to slow down a lot
    - Have many peers you need to go through
    - We have some improvements we plan to make about more directly checking bad blocks
    - That scale is missing from Stureby and probably won't be there
    - How do we simulate that in terms of peers, tx, and data?
- Peter
    - Way back when we did DAO hardfork we had an explicit rule during fork that extra header data fields explicitly set so that fast/warp/light syncing cannot end up on wrong chain
    - Haven't done these protective measures since then since we don't consider these forks contentious
    - But might be interesting to test this to ensure the network separates cleanly, otherwise we'll always have these weird problems if something goes wrong
- Afri
    - You can run a Byzantium miner
    - On mainnet we don't _expect_ it to be contentious i.e. don't expect major mining pools to mine old chain
    - On Stureby we have reassurance that fork runs smoothly under perfect conditions
    - We just want to redo the fork since it didn't go well on Ropsten
- Name [comes from Stockholm](https://en.wikipedia.org/wiki/Stureby)
- Afri: We should discuss block number
    - For Parity, okay to discuss next meeting
    - Peter: Geth will do two more releases, one Monday, one on Dec. 10 so we can discuss on next call
    - Hudson: Let's continue conversation on Gitter
    - Afri put some [suggested block numbers](https://github.com/ethereum/pm/issues/62#issuecomment-438601027) into agenda

# Goerli update
- Afri
    - Thanks to everyone who contributed
    - We are still in pre-testnet phase, so it might break anytime and all testnet ether would be burned when we restart it
    - Four clients connected, geth, pantheon, nethermind with full support, parity clique implementation still experimental and some features missing but it's syncing
    - I'm surprised how stable it is
    - Launched a one-way bridge this week so people can burn testnet eth on other testnets to bridge to Goerli, testnet-to-testnet bridge faucet
    - Just [announced some bounties](https://dev.to/5chdn/the-grli-testnet-initiative-bounties-announcement-3gp) for open tasks we want to work on in a blog post

# ProgPoW update
- Pawel update
    - Specification and reference impl. are versioned now, currently v9.1
    - Mine and Martin's impl. are on this point
    - Parity's impl. may be one change behind but not significant difference
    - We have four more or less in sync current impl.
        - Geth
        - Parity
        - C++
        - OpenCLO/Kuda (ProgPoW team)
    - We need some kind of announcement from authors of ProgPoW that they believe this is the final spec
    - Then we can consider have a separate testnet to check it on a running blockchain
- Adrian: Has spec been licensed? GPL? Not useful to us as Apache-licensed client
    - Pawel: This was pointed out to team at DevCon; they used a lot of ethminer code, GPL licensed
    - Not sure if they are working on a resolution or how it affects using the spec
- Peter: Problem isn't GPL code/reference impl., it's, is there a spec stating you can use algos in non-GPL code?
- Pawel: Not sure
    - Spec has code snippets taken from their impl., it was done within ethminer, may or may not make it a bit more complicated
    - Haven't seen spec for some time, haven't paid attention to mention of licensing or use
    - Can check and comment later
    - But I'm not very good at licensing so would be good to have a second pair of eyes
    - Adrian: Clean licensing would be very helpful
    - One guy from ethminer prepared alternate spec similar to ethhash spec, mostly python code snippets, was posted on EthMagicians
    - I can provide language bindings to C/C++, separate Apache license, if someone doesn't want to implement it from scratch
    - Lane: Can someone in ConsenSys help look at the license question?
    - Adrian: we'll look into it.
    - Some additional links
        - The spec (README) and reference implementation: https://github.com/ifdefelse/ProgPOW
        - My implementation (C++), if you need language bindings let me know: https://github.com/chfast/ethash
        - Alternative spec: https://github.com/MariusVanDerWijden/progpowWiki/blob/master/ProgPoW.md
EthereumStratum/2.0.0 draft: ethereum/EIPs#1571
    - and [some benchmarks](https://gitter.im/ethereum/AllCoreDevs?at=5bf81b01ed6bcf1ef84b00e6)

# Attendees
- Hudson
- Fredrik Harryson
- Adrian Sutton
- Pawel
- Afri
- Alexey Akhunov
- Andrew Gross
- Mikhail Kalanin (EF/harmony)
- Geoff Hayes
- Daniel Ellison
- Jacek Sieka
- Adam Schmideg
- Greg Colvin
- Jared Wasinger
- Peter Szilagy
- agyt (?)
- Alex Beregszaszi
- Tomasz S
