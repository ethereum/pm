# Ethereum Core Devs Meeting 64 Notes
### Meeting Date/Time: Friday, July 05, 2019 06:00 UTC
### Meeting Duration: ~1h45m
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/107)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=2D_DqJ8jL9Y)
### Moderator: Hudson Jameson 
### Notes: Brett Robertson

# Summary

### DECISIONS MADE

**DECISION 64.1:** Ronan advised that we can drop EIP-1959.

**DECISION 64.2:** Felix to updated the Ganache/spec to resolve [compliance issue](https://github.com/ethereum/pm/issues/97#issuecomment-489660359) so that it resolves as Go Ethereum does.

**DECISION 64.3:** Close ACTION 58.1 as this is now with the Cat Herders.

**DECISION 64.4:** All EIPs are on the chopping block for Istanbul at the next meeting unless there is a reference implementation or the champion can successfully argue one is not needed. EIPs not included in Istanbul are pushed back and can be reintroduced at the next fork.

### NEW ACTIONS

**ACTION 64.1:** Wei and Alexey to discuss retestETH options and how it could be implemented into Parity.

# 1. [Review previous decisions made and action items](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2063.md#summary)
[Timestamp: 3:15 ](https://youtu.be/2D_DqJ8jL9Y?t=195)

## Actions

### CLOSED

**ACTION 58.1**: Cat Herders to look at updating EIP1. 
- **Status:** Closed.

### OPEN

**ACTION 62.2:** Have an indepth discussion on how (EIP-663)[https://eips.ethereum.org/EIPS/eip-663] Unlimited SWAP and DUP instructions can be improved.  

- **Status:** No update.

**ACTION 62.3:** Perform a full benchmark for (EIP-1108)[https://eips.ethereum.org/EIPS/eip-1108] Reduce alt_bn128 precompile gas costs.  
- **Status:** No update.

**ACTION 62.4:** Discussion required with Jordi Baylina and Alex Bergszaszi around the options between [EIP-1109 PRECOMPILEDCALL opcode (Remove CALL costs for precompiled contracts)](https://eips.ethereum.org/EIPS/eip-1109) and [EIP-2046 Reduced gas cost for static calls made to precompiles](https://eips.ethereum.org/EIPS/eip-2046). 

- **Status:** There was discussion in the Magician Forum but no decisions made. 

**ACTION 62.5:** James Hancock to update the [Wiki](https://en.ethereum.wiki/roadmap/istanbul) and Meta [EIP-1679](https://eips.ethereum.org/EIPS/eip-1679) with decisions around the EIPs.

- **Status:** [Spreadsheet](https://docs.google.com/spreadsheets/d/1Mgo7mJ6b6wimUwafsMo1l-b44uec28E_Hq8EQ7YdeEM/edit#gid=0) and Wiki is the most up to date source. EIP-1969 to be updated.

**ACTION 62.6:** [EIP-1283 Net gas metering for SSTORE without dirty maps](https://eips.ethereum.org/EIPS/eip-1283) requires a new EIP number and a section discussing the difference between the original EIP-1283 which was removed from Constantinople and this new EIP. James will reach out to testing teams to understand implementation difficulties. 

[Timestamp: 8:44](https://youtu.be/2D_DqJ8jL9Y?t=524)

- **Status:** EIP-1283 is the first EIP to be disabled. It was disabled in St Petersburg. 
* If we are to re-enable EIP-1283 then [EIP-1706 Disable SSTORE with gasleft lower than call stipend](https://eips.ethereum.org/EIPS/eip-1706) is required as a mitigation. 
* There is still uncertainty about whether a new EIP is required with pros and cons from both sides. 
* Wei proposed Night Gas Metering with Account versioning. 
* Martin is concerned that without it being retroactive that those Dapp users and developers who want it for the existing dapp will miss out. 
* Paweł is a fan of EIP-1706, whilst it looks trivial it is not if you have optimised gas counting. 
* Paweł is also against account versioning as it requires the keeping of multiple EVM specs around all the time. 
* Paweł recommended that both EIP-1286 and EIP-1706 should be joined together to form a new EIP so as to test the implications of these two EIPs together.
* Peter argued that multiple EVMs can cause greater barriers to entry.
* Paweł suggested that if there was another way to implement this without account versioning then that is better. If there was a way of mitigating the security issue that resulted in the St Peterburg fork (other than EIP-1706) then that would also be preferred. 
* To avoid account versioning Paweł would prefer EIP-1706.
* So would Martin Holst Swende.

Benched discussion until Nick Johnson joins on the call.

**ACTION 62.7:** Engage with Ronan Sandford and Bryant Eisenbach to discuss which EIP; EIP-1344, EIP-1959 or EIP-1965 should be implemented.

(Timestamp: 31:46)[https://youtu.be/2D_DqJ8jL9Y?t=1906]

- **Status:** No update, Bryant is unable to attend this call. 
* Ronan suggested we could get rid of EIP-1959 as he fells EIP-1965 is better. 
* Martin prefers EIP-1344 as solution for a pretty generic problem whilst EIP-1965 is alot more complicated for a very niche problem. 
* Peter from a political perspective does not understand why developers would want to implement this EIP if it makes it easier for other people to allow for minority forks of Ethereum.

Tabled until Bryant is on the call.

** **
**Decision 64.1:** Ronan advised that we can drop EIP-1959.
** **

**ACTION 62.8:** [EIP-1352 Specify restricted address range for precompiles/system contracts](https://eips.ethereum.org/EIPS/eip-1352) needs more work done to answer the questions posed by the All Core Devs.

- **Status:** Martin suggested that this EIP makes certain contracts pre-compiles and that complicates things a little as there is uncertainty as to how this should be handled. 
* Continue the discussion in the [magicians forum](https://ethereum-magicians.org/t/eip-1352-specify-restricted-address-range-for-precompiles-system-contracts/1151) regarding the edge cases so that a decision can be made. 

**ACTION 62.9:** [EIP-2045 Particle gas costs for EVM opcodes](https://eips.ethereum.org/EIPS/eip-2045) needs further discussion. 

- **Status:** No update - waiting on Casey to champion it.

**ACTION 62.11:** Discussion and inclusion of [EIP-1962 EC arithmetic and pairings with runtime definitions](https://eips.ethereum.org/EIPS/eip-1962)  

[Timestamp: 47:00](https://youtu.be/2D_DqJ8jL9Y?t=2820)

- **Status:** This takes over from EIP-1829. 
* Alex Vlasov suggested that this EIP is now ready to be implemented. 
* The EIP-1962 implementation is 3,000 lines of safe rust code. 
* The rest of the 7,000 lines is testing. 
* Fuzzing is yet to come. 
* There can be no corruption of memory, it is completely stateless and it cannot panic. 
* Martin feels this it would be optimistic to roll it out for this fork without a parallel implementation and testing of this. 
* Danno confirms that Ethereum is powerful because it has multiple implementations of code. 
* Alex Vlasov confirms he is a team of two and creating a second implementation version is perhaps not possible from themselves. 
* Alex Gluchowski confirms there will be a second implementation for testing in either Python or Sage but not necessarily for a client. * Martin the argument for a single implementation does not hold water, a couple implementations is required.
* One of the reasons this has not been implemented by a Go Developer is because this is hard core cryptography and most developers are not cryptographers. 
* Calling a C method from Go is 20x more expensive than calling a Go method however including C code in Go is doable. 
* Including Rust code into Go is not possible. 
* Alex noted that a precidence has been set previously in Gas metering which also has only one implementation.
* Paweł confirmed that Alex has creaed an EVMC bindings for this EIP so that you can load it as an EVM that supports this single address.
* The full spec is not yet available but it will include a step by step guidance.


Tabled for discussion in the [Magician's forum](https://ethereum-magicians.org/t/generalised-precompile-for-elliptic-curve-arithmetics-and-pairings-working-group/3208/2) and gitter channel.

**ACTION 61.1**: [Ganache/spec compliance issue at go-ethereum](https://github.com/ethereum/pm/issues/97#issuecomment-489660359)  

[Timestamp: 1:03:21](https://youtu.be/2D_DqJ8jL9Y?t=3801)

- **Status:** Felix's last comment in the issue comments suggests that there needs to be a change in the spec to return the quantity as Geth does. 
* Peter confirmed that if you interpret these as numbers then you are allowed to have 0 if you interpret them as binary then you want even number of hex characters. Ganache follows the Spec whilst Go Ethereum suggests that these were numbers orginally cryptographically speaking.

** **
**Decision 64.2:** Felix to updated the Ganache/spec to resolve [compliance issue](https://github.com/ethereum/go-ethereum/issues/18152) so that it resolves as Go Ethereum does.
** **


# 2. EIPs
[Timestamp: 1:08:16](https://youtu.be/2D_DqJ8jL9Y?t=4096)

## [EIP-2028 Transaction data gas cost reduction](http://eips.ethereum.org/EIPS/eip-2028): 

* Louis explains that EIP-2028 is a reduction of call data gas costs.
* They released a test plan with Whiteblock to gather more simulation data on the 4th July 2019.
* They are hoping to see the affect of increasing the actual blocksize on the network as there is currently very limited data around this.
* They wish to hear back from people regarding the simulation plan as well as any concerns around the EIP.
* Eli explains that essentially the code is pretty simple reducing the gas cost from 68 to something smaller (estimate 4x).
* Tomasz notes that this change is a the transaction level not the contract level so it will not touch accounts and will not therefore need account versioning. 
* Paweł confirms that it does not effect the EVM.
* Alexey also advises that it would be incorrect to call it call data reduction because it only affects the gas costs of the transaction that originates not from the construct but from the external account because within the contract calls there is no charge only the data that is included into the blocks and made it to the frontier of the EVM - this is what changes. 
* This EIP is the reduction of the call of transaction data not the call data. 
* Louis confirms that the only impact is the increase of block size.
* Peter expressed some concern that the size of the data my impact on the size of the block to increase it to 0.5MB.
* He explained he had 2 issues: 1. The chain growth, how fast would the chain grow compared to the size of blocks currently. 
* Louis explained that the average size of block is 25kb. When discussing chain growth we need to understand are we talking about a full node or archive node? 
* In the case of this EIP by increasing the transmission size we actually reduce the state growth. 
* Archive nodes would grow faster than full nodes. 
* The storage of a block is roughly 30% whilst the current data in the block represents roughly 3% so increasing it by 4 would only take half of the storage.
* Peter then continues and notes the other important thing to consider is transaction propagation. Go Ethereum has a limit of 24kb in size for transactions with propagators 25. 
* Louis notes this is not a consensus rule and we could push a patch to Go Ethereum.
* Peter notes that whilst it is not a consensus rule unless all the clients have the sae limits when it reachs a client that does not have this same limit it will filter out these transactions which affects propagation.
* Whilst limits can be raised we need to be aware of the possibility of a denial of service and from a network transaction bandwidth perspective, transaction propagation can take up a lot more bandwidth.
* Louis agrees with this prognosis and confirms this is the reason for the simulations with whiteblock. 
* Note also since the update of Parity there is now a very weak correlation between block size and uncle rate on existing blocks. 
* Louis notes in general use the block size is between 25kb and 35kb.
* Peter notes that his concern is not general use case but that someone could DoS the network with large blocksizes. 
* Louis agrees that this is also their main concern. 
* 0 bytes is priced at 4 bytes. Louis remains unclear as to why there is a price difference between 0 byte and non 0 byte.
* Eli thanks Peter for his feedback, this is exactly why they want to do the simulations. 
* They will be sharing the data from simulations as soon as they have them. 
* There is a concern that gas costs and call data are already way to high which causes other problems such as all the data goes to storage - doing this may result in a more secure system but this needs to be reviewed.
* Work will progress very cautiously.

Hudson: To follow the progress and contribute join the [magicians forum](https://ethereum-magicians.org/t/eip-2028-calldata-gas-cost-reduction/3280).

## DevOps discussion

* James advises that at the last core devs call from the discussion between Rick and himself around [EIP-1559 Fee market change for ETH 1.0 chain](https://eips.ethereum.org/EIPS/eip-1559) and that we were in talks with a group that was also looking to do tests for EIPs and perhaps the devops that Ethereum has can be extended to some of these groups - this is the group. 
* Hudson confirmed from last discussion he had introduced the idea with the EF DevOps team to maybe have foundation resources to help test for EIPs. Whether that be server time, different nodes getting spun up, things like that. 
* Initial conversations were good but nothing concrete there yet.

a) [EIP 2124: Fork identifier for chain compatibility checks](https://github.com/ethereum/pm/issues/107#issuecomment-508164964):

No time for discussion.

b) [EIP 1962 Update](https://github.com/matter-labs/eip1962/)  

No time for discussion.

c) [EIP 1679: Hardfork Meta: Istanbul](http://eips.ethereum.org/EIPS/eip-1679)

No time for discussion.

# 3. [Working Group Updates](https://eth.wiki/eth1)  

No time for discussion.

# 4. Testing Updates
[Timestamp: 1:23:42 ](https://youtu.be/2D_DqJ8jL9Y?t=5022)

* Dimitry advised that Geth is now support retestETH. 
* It is possible to generate tests for EIP implementations with the Geth Client. 
* Geth could now generate performance tests and statetests. 
* A workshop is planned for August in Berlin for test teams and people working on testing implementations for EIPs. 

* Martin has also floated an idea in the all core dev channel and the testing channel and it now exists in a form of a [Pull Request](https://github.com/ethereum/go-ethereum/pull/19743) in Go-Ethereum but has not been merged yet.  
* The ability to run statetests where we have the basefork and the particular EIP/s. 
* That is where the fork is for example Constantinople plus EIP number/s. 
* This could make it easier to get tests ready early on. 

# 5. Any other business
[Timestamp: 1:25:30](https://youtu.be/2D_DqJ8jL9Y?t=5130)

## State rents proposals for Istanbul [(Comment)](https://github.com/ethereum/pm/issues/107#issuecomment-507810235)

* Alexey confirmed that he had written 5 EIPs but did not believe he would have enough time to meet them all before Istanbul in October.
* He has completed the implementation for only one, [EIP-2027 State Rent C - Net contract size accounting](https://eips.ethereum.org/EIPS/eip-2027) which introduces storage size accounting. 
* This however currently is in conflict with current implementation of account versioning which is basically adding another field into the account.
* The account field is the fifth field and so is the storage field. So it needs to be reworked. 
* With current state I don't think it will be. 
* Istanbul became the focal point for anything to change in Ethereum. 
* Istanbul was meant to be, from discussions at DevCon4, for emergency measures to stop the chain from dieing - this is no longer the case.
* So it is now unrealistic that progress will be done in State Rent because of conflicting issues.
* So the answer is no it will not be implemented in Istanbul.

* Wei did advise that with regard to account fields, Parity did an update and should now be compatible with any other account fields. 

* Alexey confirmed that the other significant work required is to produce a specification and provide data around the Status client and the Senior Status client which remains Alexey's focus.

## Timeframes for Ethereum 1.x
[Timestamp: 1:31:12](https://youtu.be/2D_DqJ8jL9Y?t=5472)

* Tomasz wanted to confirm if it is now unlikely to get Ethereum 1.x in 18 months or is it still on track for 18 months?
* Alexey it all depends on how Ethereum 1.x evolves. 
* If we go back to the orginal idea and reduce the changes to the minimalistic set then it is possible to achieve 18 months.
* It also depends on testing. 
* At this stage we are still waiting to see what happens with Istanbul first before a timeframe can be determined.
* Hudson confirmed that this has grown larger than previously envisaged. It includes process changes, what EIPs going in between now and Ethereum 2.0 and mitigation efforts.
* Martin suggests we need to start rejecting more suggested EIPs and stop tabling discussions for later. 
* James notes that there are only 10 EIPs that have Reference Implementations out of the 34 currently proposed EIPs.
* Danno advises that the original soft deadline for client implementations is next week. So next call could work if we decide to make the final decision to chop EIPs.
* Hudson questioned if people still buy into the schedule?
* Alexey would like to increase the number forks per year but make the forks smaller.
* Danno confirmed this could work if we define which issues go into which fork.
* Hudson confirms that we can decide today that only those EIPs accepted at the next meeting with go into Istanbul. The rest will be pushed back.
* Danno seconds this.

* Alex Vlasov questioned what was meant by a "complete" Reference implementation.
* Martin: Reference implementation is an implementation in a client which show other node implementors how do we integrate this, what parts need to be touched. Basically a full embedding of the EIP inside of a Node.
* Alexey advised that a reference implementation is the implementation that can generate the conformance tests. 
* Previously we only had Aleth now we also have Geth.
* Hudson wanted to know if there was a way we could get the retestETH into Parity?
* Wei confirmed that this is not possible as they have issues implementing testing using RPC... 
* Dimitry advised that RPC may not be the best protocol and Alexey may have some ideas around this using devp2p or libp2p.

** **
ACTION 64.1: Wei and Alexey to discuss retestETH options and how it could be implemented into Parity.
** ** 

* James suggested making Hybrid decision at the next meeting. That is those EIPs that don't have a reference implementation, unless they can justify the reason behind not having one at the next call, will not be implemented in Istanbul. 
* Alex Beregszaszi confirmed that some EIPs may not need a reference implementation. 
* Tomasz agreed that some EIPs on the list are very simple and just need discussion.
* James agreed that this would also work. 
* Hudson confirmed that all EIPs are up on chopping block if no reference implementation is present, with exception to those where the champion is able to get agreement that one is not needed at the next meeting.

** **
**DECISION 64.4:** All EIPs are on the chopping block for Istanbul at the next meeting unless there is a reference implementation or the champion can successfully argue one is not needed. EIPs not included in Istanbul are pushed back and can be reintroduced at the next fork.
** **

## Next Hard Forks 

* Danno suggested it would be worth discussing if their is time in the next meeting what the forks would look like after Istanbul. 
H*Hudson agreed if there was time otherwise it may be worth bring it up in the magicians forum.

## Apologies regarding Agenda
[Timestamp: 1:44:00](https://youtu.be/2D_DqJ8jL9Y?t=6240)

Hudson apologised that it was not possible to review everything in the agenda.

### [EIP-2124: Fork identifier for chain compatibility checks](https://github.com/ethereum/pm/issues/107#issuecomment-508164964):

* Hudson suggested people please review and comment on this EIP so that we can give a Yes or No next call.
* Peter advised that this EIP does not touch concensus and does not even enable anything yet on the network. 
* If anyone sees any obvious issue with it please write it down. 

# Date for Next Meeting:
Thursday July 18, 2019 at 22:00 UTC

# Attendees

* Hudson Jameson
* James Hancock
* Adrian Sutton
* Alex Beregszaszi
* Alex Gluchowski
* Alex Vlasov
* Alexy Akhunov
* Brett Allsop
* Brett Robertson
* Danno Ferrin
* Greg Colvin
* Jacek Sieka
* Jim Bennett
* Jules
* Martin Holste Swende
* Paweł Bylica
* Péter Szilágyi
* Louis Guthmann
* Ronan
* Tim Beiko
* Wei Tang
