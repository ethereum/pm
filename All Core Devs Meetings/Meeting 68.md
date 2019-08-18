# Ethereum Core Devs Meeting 68 Notes
### Meeting Date/Time: Thursday 15 August 2019 at 22:00 UTC
### Meeting Duration: 1hr 30mins
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/119)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=08eaI8JjSbw)
### Moderator: Hudson Jameson
### Notes: Brett Robertson
	
----
	
# Summary
	
### DECISIONS MADE
	
**DECISION 68.1:** Move [EIP-2200](https://github.com/ethereum/EIPs/pull/2200) using Wei's version from Tentative Accepted to Accepted for Hardfork: Istanbul 1.

**DECISION 68.2:** Move [EIP-1884](https://eips.ethereum.org/EIPS/eip-1884) from Tentative Accepted to Accepted for Hardfork: Istanbul 1.

**DECISION 68.3:** All Clients are required to have implemented all EIPs for Hardfork: Istanbul 1 by 23 August 2019.

**DECISION 68.4:** The Instanbul 1 TestNet HardFork block number decision will take place at the next All Core Devs Call on the 23rd August 2019 unless decision is made prior via gitter.

**DECISION 68.5:** Approve Alex’s proposal to name the all hardforks going forward according to the devcon cities starting with calling the next hardfork after Istanbul which will be called Berlin from DevCon0 rather than Istanbul 2.


### ACTION ITEM

**ACTION 68.1:** Ethereum Cat Herders to engage with community to make them aware that [EIP-1884](https://eips.ethereum.org/EIPS/eip-1884) is to be implmented and that they should check their contracts encase of any issues.

**ACTION 68.2:** Louis to engage with Martin to ensure that relevant test data is input into the [EIP-2028](https://eips.ethereum.org/EIPS/eip-2028) to assist with giving context to testing.
	
-----

# 1. Istanbul EIPs

## Client implementation updates for Accepted and Tentatively Accepted

**Hudson**: 

### Parity

No one from Parity on the call.

### Nethermind

**Tomasz**: 

**Hardfork: Istanbul 1 - ACCEPTED**

- [EIP-152](https://github.com/ethereum/EIPs/pull/2129): Yet to be implemented. Should be ok.
- [EIP-1108](https://eips.ethereum.org/EIPS/eip-1108): Yet to be implemented. Should be ok but would like to run some benchmarks against their current implementation and see if we have to write any bindings for the libraries.
- [EIP-1344](https://eips.ethereum.org/EIPS/eip-1344): This has been implemented.
- [EIP-2028](https://eips.ethereum.org/EIPS/eip-2028): Yet to be implemented.

**Hardfork: Istanbul 1 - TENTATIVELY ACCEPTED**

[EIP-1884](https://eips.ethereum.org/EIPS/eip-1884): Yet to be implemented.
[EIP-2200](https://github.com/ethereum/EIPs/pull/2200): Yet to be implemented.

Foresee no issues.

- Nethermind's Istanbul 1 Tracker: NethermindEth/nethermind#771

### Geth

**Péter**: 

**Hardfork: Istanbul 1 - ACCEPTED**

- [EIP-152](https://github.com/ethereum/EIPs/pull/2129): Yet to be implemented. Should be ok but we need to confirm if this EIP is now final.
- [EIP-1344](https://eips.ethereum.org/EIPS/eip-1344): This has been implemented.
- [EIP-1108](https://eips.ethereum.org/EIPS/eip-1108): This has been implemented.
- [EIP-2028](https://eips.ethereum.org/EIPS/eip-2028): This has been implemented.

**Hardfork: Istanbul 1 - TENTATIVELY ACCEPTED**

[EIP-1884](https://eips.ethereum.org/EIPS/eip-1884): This has been implemented.
[EIP-2200](https://github.com/ethereum/EIPs/pull/2200): Yet to be implemented. Alexi's implementation resulted in issues as such it has been agreed that we will proceed with Wei's version.

- Geth's Istanbul 1 Tracker: ethereum/go-ethereum#19919

### Parity:

- Parity's Instanbul 1 Tracker:paritytech/parity-ethereum#10770

### Aleth:

- Aleth's Istanbul 1 Tracker: ethereum/aleth#5716

### Patheon: 

- Patheon's Istanbul 1 Tracker: https://pegasys1.atlassian.net/browse/PAN-2756

### Trinity: 

- Trinity's Istanbul 1 Tracker: https://github.com/ethereum/py-evm/milestone/11


## Moving Istanbul EIPs from Tentative to Final

**Hudson**: General concensus that there are no objections from any of the clients for using Wei's version of [EIP-2200](https://github.com/ethereum/EIPs/pull/2200) and moving it to final acceptance for the Istanbul 1.

**DECISION 68.1:** Move [EIP-2200](https://github.com/ethereum/EIPs/pull/2200) using Wei's version from Tentative Accepted to Accepted for Hardfork: Istanbul 1.

**Hudson**: General concensus that there are no objections from any of the clients for [EIP-1884](https://eips.ethereum.org/EIPS/eip-1884) and moving it to final acceptance for Istanbul 1.

**DECISION 68.2:** Move [EIP-1884](https://eips.ethereum.org/EIPS/eip-1884) from Tentative Accepted to Accepted for Hardfork: Istanbul 1.

**ACTION 68.1:** Ethereum Cat Herders to engage with community to make them aware that [EIP-1884](https://eips.ethereum.org/EIPS/eip-1884) is to be implmented and that they should check their contracts encase of any issues.

## Benchmarks for gas repricing EIPs

**Péter**: This relates to Istanbul 2.

**Hudson**: We will not look at this for now as our priority for this call is locking down Istanbul 1.

# 2. Conformance Testing

**Danno**: This is regard to Dimitry's reference tests.

**Hudson**: Dimitry is concerned that alot of the testing rests on his shoulders and that going forward clients or EIP champions should consider doing their own test cases themselves using retesteth. He can then coordinate and create seperate test cases if required.

**Martin**: I have created a few tests and it would be great if the clients could run these tests to ensure they are correct syntactically and also to see if they pass. In this way we can get these tests merged into the official test repository.

**Hudson**: Just want everyone to be aware that there are two resources for testing. 

-There is the [Testing Gitter Channel](https://gitter.im/ethereum/tests) that Dimitry and others are pretty active in.
-There is also the [retesteth wiki](https://github.com/ethereum/retesteth/wiki/Creating-a-State-Test-with-retesteth) for creating state test with retesteth.

**James**: From the last All Core Dev meeting it was decided that the EIP creators/champions should perform the tests. However there is some concern from these parties that even those that are keen to get involved do not understand what needs to be done or how they can do it. So we may need to engage with Dimitry to create a process to allow for this to happen.

**Martin**: This is understandable. One of the first things the EIP champions can do is outline what needs to be tested.

**Danno**: Patheon has just implemented retesteth support with the most recent release. Agree with Dimitry that we should move to something like retesteth so that we can get all the clients working on it.

**Louis**: Can confirm there was some confusion on the process itself. If the Core Devs could lay out a framework of what needs to be done, who is available to assist etc.

**Martin**: This is something that could be managed by a Hard Fork Coordinator.

**Hudson**: That would be great but for now as we don't have a Hard Fork Coordinator then Dimitry will be best placed for this.

**Péter**: Currently all the test cases in the EIPs are blank. It would be really useful if these could be populated even it is just expected inputs and resulting outputs so that when we test we can ensure we are on the right track.

**ACTION 68.2:** Louis to engage with Martin to ensure that relevant test data is input into the [EIP-2028](https://eips.ethereum.org/EIPS/eip-2028) to assist with giving context to testing.

# 3. Testnet Upgrade & Istanbul Next Steps

## Block for September 4th Testnet Fork

**Péter**: As we have only finalised the EIPs and we still do not understand where Parity is with regard to implementing these EIPs I feel we cannot make a decision on what block number should be selected for the Testnet Fork. Previous hardforks allowed for months of testing in the client space before we forked. Allowing only 2 weeks in this fork seems brave.

**Hudson**: Agreed. We will postpone this decision to the next meeting or once we have a better idea of where the clients are with implementing the required EIPs. Suggest that all clients have the EIPs implemented by the next All Core Dev call to finalise a block number.

**DECISION 68.3:** All Clients are required to have implemented all EIPs for Hardfork: Istanbul 1 by 23 August 2019.

**DECISION 68.4:** The Instanbul 1 TestNet HardFork block number decision will take place at the next All Core Devs Call on the 23rd August 2019 unless decision is made prior via gitter.

## Splitting Istanbul into two forks

**Péter**: Istanbul was split into two forks due to there being some EIPs that we wanted to implement but weren't ready now and we did not want to get lost in a completely new seperate fork that would delay their implementation even further. 

**Hudson**: Note there was an [update](https://github.com/ethereum-cat-herders/progpow-audit/) on ProgPoW audit released by the Cat Herders that provides some dates, just for your reference. They are aiming for a final audit completion date of 11 September 2019 - the hardware audit completion date is still to be comfirmed.

# 4. Pooled or Staged Fork Model

**Martin**: The idea is to move away from simply pooling all new EIPs into a Hardfork we instead go for a staged approach where by the EIP champions do the hardyards to get the EIP ready for the Hardfork including engaging with relevant client resources to prepare and test it before it gets presented to the All Core Devs for inclusion into a Hardfork.

**Péter**: So the difference being that we move from the current model of accepting a new EIP before we have implemented it to a model where by the the EIP has already had a cross client implementation and once that is done then it get's proposed into a hardfork.

**Martin**: In this way we move away from the current model where we race against some artificial deadline and instead these things can take the time they take to get implemented.

**Danno**: What I like about this model is that EIPs are accepted when they are ready instead of now where EIPs are accepted and if they fail they get pushed back to the beginning. That way we move them through as they are ready and then when they are ready the All Core Devs can pick it up and then we go.

**James**: My favourite things about this proposal is that every EIP that is not in Istanbul now will now know what they need to do to get their EIP included into future hardforks. And these steps can happen outside of an All Core Dev call. Eliminating alot of the unneccesary waiting around.

**Péter**: It is also worth noting that as these EIPs progress into a ready state does not mean that there will need to be a hardfork. Instead these EIPs can progress into a ready state and get placed into a staging pool so as to be ready for the next Hardfork. In this way Hardforks can take place at expected intervals and there is more control about what goes into the Hardfork without the rush to get it in.

**Martin**: This model allows for multiple individual Hardforks per EIP (and I am not opposed to this) or we can pool the ready EIPs together for pre-scheduled Hardforks. 

**Louis**: As an EIP creator I prefer this model as it allows us to progress with our EIPs in a timely fashion instead of today where we got to rush to meet the required deadline. It is a much better approach as it allows those creating the EIP to know where they stand and when they need to come in and present their project.

**Adrian**: One of the great issues we have currently is that EIPs don't get alot of scrutiny until we are ready to implement them in a hard fork. One of the great things about this approach is that we can enforce the scrutiny requirement when the EIPs get themselves ready for the Accepted status and once accepted people are aware they have now been placed in a queue ready to be implemented in some hardfork in the future.

**Jason**: One thing we need to think about too is if we go with this approach then their will be a lot of individual testing of EIPs rather than bundled testing before release. This could cause issues and we need to think about this.

**Martin**: We could always have specific blockchain tests when we are ready to implement.

**Alex**: The process already exists for EIPs to go into accepted state. That is this work should have occured before they went into final call. However no one enforced this step. My main concern with this process is the uncertainty of how the EIP proposers can capture the attention of the Core Devs earlier on in the process.

**Martin**: The problem with EIPs is that no one really monitors the EIPs and when there is a last call no one really pays attention. Agreed that in order for this to work we will need the clients to accept the proposed EIPs in the early stages and if not all the parties are present at the meeting where the blessing is given to the EIP then this EIP cannot progress. Clients will need to make something of a commitment to say they would accept it.

**Danno**: One of the things the Ethereum Enterprise Alliance does is that they mention the EIPs that are in final call. If we could do a similar thing either at the top or the bottom of the meeting then that could assist clients with knowing what is in final call.

**Martin**: In this case we would need to make sure that every client acknowledges the EIPs in final call and gives them their blessing to progress. Else it does not progress and is stalled or blocked.

**Alex**: My concern here is that this process takes place a lot later than I had envisioned. That is when a person comes up with an EIP idea when are they meant to engage with the clients to find out if this a good idea or bad idea before they spend all the time to build, implement and test this EIP before the final call period?

**Martin**: Yes, I have no solution for that.

**Péter**: My issue with the EIP process is that the whole EIP process is untrackable. One thing that would really help is if we had some sort of visual representation of the progress of these EIPs. This would assist with allowing the various parties to know when they should take a look at an EIP.

**Alex**: The reason this situation exists is that there are only two states: Draft and Accepted state. If we wanted to introduce this new visualisation then we would need to introduce more stages and define what these stages are.

**Péter**: I am not sure I want to go into such a formal process - I will go away and think about it.

**James**: I tried to track what was going on but spent most of my time trying to follow these EIPs.

**Tomasz**: I think if we could create a checklist for the EIP champions so that they would know what they had to achieve for the accepted state. It would also be really beneficial for us to use as a dashboard to monitor progress from a client perspective.

**Alex**: I do think it would be worthwhile having an initial review of fresh EIPs by the All Core Devs before any further work gets done on the EIP so that the EIP champion can know if progressing with this EIP is infact worthwhile. This could be the first step.

**Hudson**: This seems reasonable. We don't need to make a decision today but there appears to be some broad support for this and just requires a little further tweaking.

**Péter**: Discussion are really hard to follow especially when large conversations happen around a subject. A result of the conversation should be pulled out of the discussions to help speed up the process.

**Hudson**: I think there is a feature with the software used by Ethereum Magicians that allows one to get a summary of the discussion. I will look into this further. Or perhaps we can get someone like the hardfork coordinator that can once in a while create an update on all the discussions.

**Péter**: Yes, or perhaps we can put the responsibility back on the EIP Champion. Just so that we can get to the point of the discussions.

# 5. Hard fork naming

From the [note](https://github.com/ethereum/pm/issues/119#issuecomment-520232072) in the agenda.

**Alex**: This is an old discussion thread from back in April, I brought it up again as Istanbul split into two and I thought it might be better to rename it something else other than Istanbul 2. 

**Hudson**: Seems reasonable.

**Martin**: Seems good enough.

**James**: Both Arachnid and I feel from a long conversation on this is that this is a good idea.

**Danno**: I disagree. Dimitry posted and EIP in the open EIP call where he rerecommended we go to using numbers for the names. I think there should be a public name and a private name. Because writing code we need to keep a large mental map of which hardfork came first. Public names are great as they make great conversation and advertising platforms. But when it comes to coding I think keeping it to numbers makes sense.

**Martin**: I agree with you - keeping it seperate. I thought that was Alex's proposal and that it was specific to the public names.

**Hudson**: I like the idea of naming the public names the devcon cities. For numbering the hardforks is there a precedent for this in non-blockchain industry?

**Danno**: It is called semantic versioning and it is going to devolve quickly into a single incrementing number. The first number increments when there is a breaking backwards change which is the very definition of a hardfork. The second one is a minor upgrade which may be seen as a soft fork in bitcoin. The third is bug fixes. I think as most of the changes with be breaking backwards changes the easiest thing to do will be to start at Olympic or Homestead with the idea that every time we update the testnet for a hardfork upgrade we increment by one. And that way it is just a simple count of how many times we wanted to hardfork.

**Tomasz**: The simplest example would be Microsoft Word. They version their things internally but give public names for marketing etc.

**Péter**: The one issue I have with versioning is the testnets have different versioning due to issues experienced at the testnet level. This could result in versions being out of sync and things could get messy.

**James**: Ubuntu uses dates as their versioning.

**Tomaz**: Lets take this offline.

**Hudson**: Absolutely. For Alex’ proposal is anyone opposed to the devcon city naming? 

**General Consensus for proposal**

**DECISION 68.5:** Approve Alex’s proposal to name the all hardforks going forward according to the devcon cities starting with calling the next hardfork after Istanbul which will be called Berlin from DevCon0 rather than Istanbul 2.

# 6. Review previous decisions made and action items
## [Call 67](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2067.md#decisions-made)

Decisions from Meeting 67 reviewed.

# 6. [Working Group Updates](https://en.ethereum.wiki/eth1)

**Hudson**: Eth1.x Finality Gadget working group got restarted and had their first call. I believe that was Alex Stokes who ran that. 

**Danno**: I was on the call and this was more of a organisational meeting and how we move forward.

# 7. Testing Updates

None.

# 8. Client Updates (only if they are posted in the comments below)
a) Geth
b) Parity Ethereum
c) Aleth/eth
d) Trinity/PyEVM
e) EthereumJS
f) EthereumJ/Harmony
g) Pantheon
h) Turbo Geth
i) Nimbus
j) web3j
k) Mana/Exthereum
l) Mantis
m) Nethermind

# 8. EWASM & Research Updates (only if they are posted in the comments below)
 
	
	
# Attendees

* Alex Guchowski
* Alex Beregszaszi
* Adrian Sutton
* Brett Robertson
* Danno Ferrin
* Hudson Jameson
* James Hancock
* Jason Carver
* Louis Guthmann
* Martin Holst Swende
* Martin Lundfall
* Péter Szilágyi
* Tomasz Stanczak

# Date for Next Meeting: August 23rd, 2019 at 14:00 UTC.
