# Ethereum Core Devs Meeting 63 Notes
### Meeting Date/Time: Friday, June 21, 2019 14:00 UTC
### Meeting Duration: ~1.5 hrs
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/102)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=Cl5zGk-3Ej4)
### Moderator: Hudson Jameson 

# Summary

### DECISIONS MADE

**Decision 63.1:** EIP-2024 accepted into Istanbul  
**Decision 63.2:** EIP-1702 accepted into Istanbul  
**Decision 63.2:** Shifting time of All Core Dev meeting time by 8 hrs every meeting (from current 9am time) to better accommodate time zones.


### ACTIONS REQUIRED

**ACTION 62.2:** Have an indepth discussion on how EIP-663 can be improved.  

**ACTION 62.3:** Perform a full benchmark for EIP-1108.  

**ACTION 62.4:** Discussion required with Jordi Baylina and Alex Bergszaszi around the options between EIP-1109 and EIP-2046. 

**ACTION 62.5:** James Hancock to update the [Wiki](https://en.ethereum.wiki/roadmap/istanbul) and Meta [EIP-1962](https://eips.ethereum.org/EIPS/eip-1679) with decisions around the EIPs.

**ACTION 62.6:** EIP-1283 requires a new EIP number and a section discussing the difference between the original EIP-1283 which was removed from Constantinople and this new EIP. James will reach out to testing teams to understand 
implementation difficulties. 

**ACTION 62.7:** Engage with Ronan Sandford and Bryant Eisenbach to discuss which EIP; EIP-1344, EIP-1959 or EIP-1965 should be implemented.

**ACTION 62.8:** EIP-1352 needs more work done to answer the questions posed by the All Core Devs.

**ACTION 62.9:** EIP-2045 needs further discussion.  

**ACTION 62.11:** Discussion and inclusion of EIP-1962  

**ACTION 61.1**: [Ganache/spec compliance issue at go-ethereum](https://github.com/ethereum/pm/issues/97#issuecomment-489660359)  

**ACTION 58.1**: Cat Herders to look at updating EIP1. 

# 1. [Review previous decisions made and action items](https://github.com/ethereum/pm/blob/master/AllCoreDevs-Meetings/Meeting%2062.md#summary)
[Timestamp: 3:37](https://youtu.be/Cl5zGk-3Ej4?t=217)

## Actions: 

**ACTION 62.1:** Reach out to the Authors of EIP-615 to discuss the questions around the EIP especially the option of splitting the EIP 
into smaller more digestable components and try make a decision. 
- **Status:** Further discussion didn't happen beyond AMA Gitter discussion. There was some advocacy and pushback. If people want to see further development
they can reach out to Greg. Tabled for now. 

**ACTION 62.2:** Have an indepth discussion on how EIP-663 can be improved.
- **Status:** Axic: No progress made on it. Will lead chat in Core Dev Gitter to gauge support. 

**ACTION 62.3:** Perform a full benchmark for EIP-1108.
- **Status:** Matt: What do we want to see beyond current benchmarking? Will touch base with Antonion and Zach and have better progress next week. 

**ACTION 62.4:** Discussion required with Jordi Baylina and Alex Bergszaszi around the options between EIP-1109 and EIP-2046.
- Jordi: precompiles are expensive, mine aims to reduce that cost. First it tried to reduce cost of static call, but clients suggested it 
was better to implement new opcode. 
- Axic: no discussion with Jordi about this. 
- Jordi: 1109 changed/updated to 2046 to introduce opcode
- Hudson: Link to dependency tree in the Agenda for helpful mapping purposes and hardfork prioritizing 
- Jordi: 2046 changes precompile to opcode and state - you can't do this. Can't reduce gas as much with this which is the point. 
- **Status:** Further discussion will happen on Gitter 

**ACTION 62.5:** James Hancock to update the [Wiki](https://en.ethereum.wiki/roadmap/istanbul) and Meta [EIP-1962](https://eips.ethereum.org/EIPS/eip-1679) with decisions around the EIPs.
- **Status:** Not much need to update beyond soft updates - will keep as a regular touchstone

**ACTION 62.6:** EIP-1283 requires a new EIP number and a section discussing the difference between the original EIP-1283 which was removed from Constantinople and this new EIP. James will reach out to testing teams to understand 
implementation difficulties. 
- **Status:** EIP-1706 and EIP-1283 can probably be combined into a new EIP. James will reach out to testing teams to understand 
implementation difficulties. 

**ACTION 62.7:** Engage with Ronan Sandford and Bryant Eisenbach to discuss which EIP; EIP-1344, EIP-1959 or EIP-1965 should be implemented.
- **Status:** Tabled until next week with absence of Ronan and Bryany

**ACTION 62.8:** EIP-1352 needs more work done to answer the questions posed by the All Core Devs.
- **Status:** ETH Magicians thread supported this. Some edge cases that need to be covered and clarified. Will try to clarify before
next call. 

**ACTION 62.9:** EIP-2045 needs further discussion.
- **Status:** Continued discussion over what is expected of EIPs at deadlines. Further discussion on Gitter and ETH Magicians needed. 

**ACTION 62.10:** EIP-2024 discussion required between James Prestwich, Casey Detrio and Zachary Williamson.
- **Status:** Accepted
** **
**Decision 63.1:** EIP-2024 accepted into Istanbul
** **

**ACTION 62.11:** Discussion and inclusion of EIP-1962
- **Status:** EIP-1962 discussion will happen on ETH Magicians to gauge support and whether it should be included
 
**ACTION 61.1**: [Ganache/spec compliance issue at go-ethereum](https://github.com/ethereum/pm/issues/97#issuecomment-489660359)
- **Status:** Tabled - no one present to discuss

**ACTION 58.1**: Cat Herders to look at updating EIP1. 
- **Status:** Updated after lots of productive discussion. Will as **Action Required** as a touchstone. 

# 2. [EIPs](https://youtu.be/Cl5zGk-3Ej4?t=3298)
A) [EIP 1679: Hardfork Meta: Istanbul](http://eips.ethereum.org/EIPS/eip-1679)  
**Hudson:** Please participate and comment so we can figure this mess out for Istanbul

B) [EIP 1872: Ethereum Network Upgrade Windows](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1872.md)  
**Hudson/Danno:** Reflects decision that next hardfork is likely to be April of 2020 with suggestion for standardizing a third Wednesday
release akin to 'patch Tuesdays'

**Tim:** Reiterating Martin's support for more regular hardforks

**Danno:** There's flexibility for that - potentially releasing every third Wednesday. 

**Hudson:** Tabled for a month for further discussion

C) [EIP 1109: PRECOMPILEDCALL opcode (Remove CALL costs for precompiled contracts)](https://eips.ethereum.org/EIPS/eip-1109)  
**Hudson:** Already covered in **Action Items**

D) [EIP 695 (Felix Thing)](https://github.com/ethereum/pm/issues/102#issuecomment-500835702)  
**Hudson:** Tabled for next time so Felix can be present for discussion

# 3. [EIPs regareding account versioning](https://youtu.be/Cl5zGk-3Ej4?t=3589)  
**Danno:** Some gas costs could open up bugs. Account versioning could help isolate issues.  

**James:** Loudest days for AMAs were during account versioning that 8-9 other EIPs depend on. Favorite is EIP-1702 with some remaining
questions needing clarificaiton. 

**Hudson:** Let's make sure discussion happens so we can make a definitive decision meeting. 

**Danno:** Except for precompiles, every other decision hinges on this decision. 

**Wei:** EIP-1702 seems to be the best option for account versioning. Suits most other EIPs needs. One issue is upgradable contracts - current solution is that it will use slightly more gas which seems acceptable. Another reason for Version 1 is technical depth can be added. If Version 2 is deployed first this will be more difficult.

**Danno:** Version 1 adds the extra field and the absence needs Version 0. Version 2 includes Version 1 and add prefixed bytes to the contract. So Version 1 can be added now and Version 2 could be added in a later hardfork. 

**Wei:** Version 1 is basically the base layer and can be useful by itself. 

**Hudson:** Sounds like consensus on Version 1. Version 1 is accepted into Istanbul. 
** **
**Decision 63.2:** EIP-1702 accepted into Istanbul
** **

# 4. [Working Group Updates](https://youtu.be/Cl5zGk-3Ej4?t=4163)
**Rick:** One main issue is how we're going to test changes like the ones we've discussed. Current testnets don't seem suitable to this. We want smaller more precise testnets - bigger than an individual machine, but smaller than current ones. We need to further discuss future testing environments. Some tests need to be tested seperately before combining, particularly for protocol developers since we're changing the consensus code. Whiteblock does have some good upsides, but the problem is that it's a SaaS platform - it's subscription based. Not sure if incentives are aligned. Does the foundation want to support that? 

**Hudson:** If it's for the EF, there's a strong chance we could get credits for testing. Incentives should be aligned so long as EF isn't picking winnes and losers. 

**Rick:** When you pay for a SaaS platform, are we fostering a dependency or unintentional competition?

**Hudson:** There's a devops team at EF that coordinates with teams specifically for working with and sourcing tools. I see this fitting in well there. 

**Rick:** Again, I'm a big fan of Whiteblock and their resources. Concerning cross-team coordination, as we have patches that touch the same thing or if we change gas fee market, all that research is null so we need to coordinate such communication. 

# 5. [Client Updates](https://youtu.be/Cl5zGk-3Ej4?t=4645)

A) **Pantheon - Danno:** We've had GraphQL shipping in Pantheon for a month from a hackathon.  

# 5. Final Comments:
**Hudson:** Should we change the time for some others to attend the meeting?  

**Danno:** Idea is that there's an 8 hr shift for each meeting so each major timezone only has to wake up in the middle on the night once every month and a half. The rest of the time is reasonable. 

**Guillaume:** Time would be split across a day - Thursday afternoon in Americas, Thursday evening in Europe, Friday morning in Asia)

** **
**Decision 63.3:** Shifting time of All Core Dev meeting time by 8 hrs every meeting (from current 9am time) to better accommodate time zones. 
** **

**Trenton:** Talked with Zach from Whiteblock over Rick's concerns. They're OS and Zach is open to talking about supporting those working on EIPs that might be able to do a complete software or SaaS purchase. 

# Date for Next Meeting:
July 5, 2019 at 06:00 UTC

# Attendees
* Alex Beregszaszi
* Brent Allsop
* Brett Robertson
* Casey Detrio
* Daniel Ellison
* Guillaume
* Hudson Jameson
* James Hancock
* James Prestwich
* Jim
* Jordi Baylina
* JosephC
* Kobi Gurkian
* Matt Garnett
* Matt Luongo
* Michael LaCroix
* Paweł Bylica
* Phil Lucsok 
* Rick Dudley
* Tim Beiko
* Trenton Van Epps
* Wei Tang
* Will Villanueva
