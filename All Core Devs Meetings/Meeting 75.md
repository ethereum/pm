# Ethereum All Core Devs Call 75 Notes
	
### Meeting Date/Time: Thursday October 24, 2019 at [14:00 GMT](http://www.timebie.com/std/gmt.php?q=14)
### Meeting Duration: 1:30 min
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/138)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=3qZFiETlDtk)

#### Moderator: Hudson Jameson
#### Scribe: Brett Robertson

** ** 

## Agenda

- 1 Istanbul Adoption and [Call for Assistanc](https://github.com/ethereum/pm/issues/138#issuecomment-554228944)
- 2 Berlin updates
- 3 Harmony/ethereumJ
- 4 Testing updates
- 5 [Eligibility for Inclusion (EFI) EIP Review](https://github.com/ethereum/EIPs/pull/2378)
  - [EIP-2348: Validated EVM Contracts](https://github.com/ethereum/EIPs/pull/2348)
  - [EIP 1803: Rename opcodes for clarity](https://eips.ethereum.org/EIPS/eip-1803)
- 6 EIPIP (EIP Improvement Proposal) Meeting
- 7 Review previous decisions made and action items
  - [Call 74](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2074.md)
- 8 Client Updates
  - b Parity Ethereum
  - c Aleth/eth
- 9 Research Updates

** ** 

## EIP Status 
| EIP | Status |
|-------|----------|
| EIP-1679 | `Accepted & Final` |
| EIP-152 | `Accepted & Final` |
| EIP-1108 | `Accepted & Final` |
| EIP-1344 | `Accepted & Final` |
| EIP-1884 | `Accepted & Final` |
| EIP-2028 | `Accepted & Final` |
| EIP-2200 | `Accepted & Final` |
| EIP-1702 | `Eligible for Inclusion` Pending Champion. Not accepted into Berlin |
| EIP-663 | May not be ready. Currently depends on EIP-1702 |
| EIP-1962 | Requires more Specification. Contact Champion |
| EIP-1380 | `Eligible for Inclusion` |
| EIP-1985 | Decision required around needing a Hard Fork |
| EIP-2046 | `Eligible for Inclusion` |
| EIP-1985 | `Eligible for Inclusion` |
| EIP-1559 | `Eligible for Inclusion` |


## Decisions
| EIP | Status |
|-------|----------|
| EIP-2348 | `First Call`, not yet `Eligible for Inclusion` |
| EIP-1803 | `Eligible for Inclusion` & `Last Call` |

** ** 

## 1. Istanbul Adoption and [Call for Assistance](https://github.com/ethereum/pm/issues/138#issuecomment-554228944)
Video: [04:10](https://youtu.be/3qZFiETlDtk?t=250)

**Phil Lucsok:** Parity has released [v2.5.10](https://github.com/paritytech/parity-ethereum/releases/tag/v2.5.10
) for there client in preparation for Istanbul. 

**Martin:** Geth has released [v1.9.7](https://geth.ethereum.org/downloads/#). 

**Danno:** Nethermind has released [v1.1.8](http://downloads.nethermind.io/). 

**All users are encouraged to update their client to the current release to ensure they are ready for Istanbul on the 4th December 2019, Block # 9,069,000.**

**Hudson:** James posted a call for assistance on the (Ethernodes Website)(https://www.ethernodes.org/istanbul) to reach out to the mining pools, infrastructure providers and exchanges to ensure they are updated to the latest version of their client. 

At this moment only Etherchain has confirmed that it has updated. The Cat Herders and others are going to reach out to them. 

**James Hancock:** I am actively working on this. If there is anyone who can assist with connecting with parties please reach out to me. Otherwise, the ethernodes sight is great for collating the progress with regards to adoption of the upgrade code and will be a valuable tool going forward with future forks.

## 2. Berlin 
Video: [7:23](https://youtu.be/3qZFiETlDtk?t=443)

Nothing to update.

## 3. Harmony/EthereumJ
Video: [7:50](https://youtu.be/3qZFiETlDtk?t=470)

**Mikhail Kalinin:** Harmony/EthereumJ will no longer be maintained. Reason being is that we are focused on Ethereum 2.0 and don't have the capacity to do both.

## 4. Testing Updates
Video: [09:08](https://youtu.be/3qZFiETlDtk?t=548)

**Hudson:** See [comment from Andrei](https://github.com/ethereum/pm/issues/138#issuecomment-554345398).

**Martin:** Geth already supports this. If anyone wants to make test cases for a particular EIP then you can make those test cases without the hardfork being defined. You can instead base it on any previous hard fork plus your EIP number and activate it for test cases. It is a nice tool.

## 5. Eligibility for Inclusion (EFI) EIP Review
Video: [10:43](https://youtu.be/3qZFiETlDtk?t=643)

### [EIP-2348: Validated EVM Contracts](https://github.com/ethereum/EIPs/pull/2348)
Video: [10:55](https://youtu.be/3qZFiETlDtk?t=655)

**Danno:** This EIP is a conglomerate of several EIPs that have been floating around for a while. The purpose of this EIP is to build a foundation primarily for multi-byte EVM instructions. There is evidence that adding multi-byte code right now will break some executions. There are four basic features that we are combining into this EIP:

1. To use the EIP-1702 structure to ensure all other options in this EIP are eligible for use.
2. Use headers in the EVM options. It is essential that we should allow code to opt in to a new versioning scheme. This allows people to use old versions of Solidity to compile their mainnet code. It is more sustainable to combine the header and one of the opcodes from the EIP-615 which is the ‘BEGINDATA’ opcode. 
3. Fix invalid opcodes - by putting a wrapper around the EVM code we are saying that this is the only code that is executable and validate that code.
4. When you deploy a contract there is a validation step to ensure each code point is actually a valid code point. If opcodes do not exist then that opcode is rejected. In the future that opcode may exists as a single or multi-byte opcode but we just don’t know that now. In this case the EVM would evaluate the opcode against the known opcode list and reject it. While we are at it we are adding in an option to do static jump validation. 

We don’t have to push all of these, we can always take things out and add them to another version.

**Martin:** Please explain your main motivation around multi-byte opcodes?

**Danno:** We need to validate the contracts before they go onto the chain. We need a mechanism that will ensure all the opcodes in the stream will be valid opcodes. That will need to go with the opt in. If we don’t validate them then people can put in an unused opcode and the very next byte can be jump destination operation. The way the EVM works now you can jump over all the invalid code. So the byte that they have before the jumpdest becomes a multibyte code. When you interpret it you are not meant to jump into the destination just like you are not meant to jump into the middle of a pushin operation. 

**Martin:** So you are suggesting that someone could introduce a contract that behaves differently after the initial byte code.

**Danno:** Right. We are in an environment where someone can introduce a contract that breaks down barriers. 

**Martin:** So what happens with init code in this case?

**Danno:** So that is an open question. What should we do with that header code? One of the things is get the EVM when they recognise it to discard it and move the PC to PC=0 at byte 5 in the stream. Another option is that we can discard it and make PC=4 the beginning of the operation at the start of the stream. And another option is to make it a multibyte no-op operation. These three options could be used to ensure this header does not accidently get executed. 

I would like to mention that when you use CREATE2 you will need to use the Header in the CREATE2 wrapper as well. So whatever they load into the memory will also need that.

The reason I am concerned about PC=0 and the index lighting up is you can still get at the header with the ext code copy operation and that is why I am not liking the idea of P=0 being the fourth index of the stream.

I  am happy with any of these options but my favourite is to turn the header into a multibyte no-op.

**Martin:** I would disagree for the [reasons posted](https://github.com/ethereum/EIPs/pull/2348#issuecomment-554296846) on the EIP. 

init code is very cheap to execute. If we need to do a validation up front that is fairly cheap. If however we do it your way then we will need to do two passes and a lot more flipping. 

**Danno:** Why would we need to do two passes? 

**Martin:** Because in order to ensure a statis jump is legal you need to have the full jump destination set. The jump may be going forward no only backwards.

**Danno:** Right so you will keep two sets. One where you are jumping to and one where you have it. You  collect those once and you compare and if there are differences you reject. But the list could conceivably be 2MB if the code is 2MB so there could be a jump operation for a future operation and that could present a problem. 

**Martin:** Yes, I think it could be attackable if it works like that. So the only way around that is to not allow validated code in init code. And then there is no deploy time, only run time. 

**Danno:** Is it only the jump validation that requires multiple flips? I am intending for this to be a one pass validation including existing validations.

**Martin:** I am not sure you can do it in one pass. Maybe you can but it will present memory problems and this is how Geth was attacked a few years ago. 

**Danno:** Ok, that is good feedback - I was not aware of the attack. I will read through the comment. 

**Martin:** I am not sure you need to pull it out but I don’t think you should have validation of the init code. 

**Danno:** Ok, I will take that under advice when I do the prototype and see how messy it gets. 

**Wei:** From the Ethereum Magicians [forum](https://ethereum-magicians.org/t/eip-2348-validated-evm-contracts/3756/3). I believe this is a solved issue. I think this can be done using an extension and account versioning which in my opinion is much nicer than the code prefix. 

**Danno:** How would we get that code prefix into the account versioning? What are the current mechanisms or would we need to introduce a new mechanism where it says I want to be subject to validation?

 **Wei:** EIP-1702 account versioning has two extensions. These two extensions are not enabled by EIP-1702 only. But there are two specifications that allow multiple versions of contracts to be deployed. There is one for `CREATE` and `CREATE2` opcodes - there is an extension for that. And another one is for contract creation transactions. I therefore think EIP-1702  covers this part of the motivation and I still think there is a much nicer solution. The main reason is that the multibyte instructions are more complicated than we previously thought. There is also some discussion in EIP-615 where we discussed why code prefix may not be a good idea.

**Danno:**  The reason I did not go with the extra field in the account creation and in the opcodes is because that presents a tooling problem. We would therefore also need to upgrade all the tooling to support this as well. I guess we will require them to do the headers and the wrappers but I was trying to get as minimal a footprint into here. And so adding new fields, engineering wise felt unnecessary when we have existing solutions.

**Martin:** One problem with the code prefixing  is the day before this hard fork hits we start deploying a lots of new contracts with this code prefix and the day after once the EVM starts executing my code prefixed contracts that I deployed the day before it will treat it like a validated contract but it is not. Therefore how should it behave when I do a jump into a data section. Clearing then the EVM will not do the jumpdest analysis in runtime.

**Danno:**  That is why it is combined with account versioning. Before account versioning is turned on you can deploy all these old contracts without account versioning. When account versioning is turned on when you deploy a contract and you have version 1 on the contract - that is when it will deploy the contract. So all these old contracts that have that header will never be evaluated. That is why I will be using both of these facilities to make sure for that situation. 

 **Wei:** If you combined code prefix with EIP-1702 then you will have two layers of conversioning… which is unnecessary. I understand the ecosystem tooling concern but if we use EIP-1702 there may be less tool breakage as we only need a change in the contract creation and not the EVM bytecode layout. 

**Danno:** So if we do the transaction then we will need to have the compiler, the client code and the EVM where as if we do the account versioning and the wrapper, we take out the deployment stuff and we just need the compiler and the EVM. I will note this into that these are some of the concerns. But either way we need to get there to allow for these multibyte instructions and a solution to enable validation.

**Piper:** Maybe the thing to do here is to compile a list of objections and dig into the history of why people have objected to code prefixes so that we can build up a small knowledge base to figure out solutions that resolve these objections. 

 **Wei:** For reference, EIP-1702 includes a background as to why the code prefix is not a good idea and why it does not work.

**James Hancock:** I would second Piper’s suggestion the the EIP should have a place that lists all the blockers so that we can see why this EIP is currently not moving forward.

**Hudson:** Perhaps notes at the top of the Ethereum Magicians thread.

**Wei:** Agree, keeping the discussion in the discussion link in the EIP will be sufficient.

** **
** DECISION 75.1:** EIP-2348 is still in progress and is not yet eligible for inclusion.
** ** 

### [EIP 1803: Rename opcodes for clarity](https://eips.ethereum.org/EIPS/eip-1803)
Video: [24:15](https://youtu.be/3qZFiETlDtk?t=1455)

**Martin Lundfall:** I believe this EIP is non-controversial. Just wanted to discuss this whilst it should not require a hard fork I feel some EIPs don’t get discussed if they don’t need a fork.

What this will affect is the infrastructure around testing and coherency how opcodes are named. The main reason I want to make this change is to rename `SHA3 (0x20)` to `KECCAK256`. Since this has not been done in solidity already and is really confusing. I think the other naming suggestions are good too. 

This is Alex’s proposal but he is not hear and I just wanted to discuss it.

**Martin:** We can easily make this change but does this name change affect the debugging tools being used?

**Martin Lundfall:** Yes, exactly - that is why I want to discuss it and correctly syncronise this change. 

**Wei:** I think it is quite nice. I am happy to have this implemented.

**Martin Lundfall:** It may be worth synchronizing this with a hard fork so that why people are updating their tooling they can make this change at the same time.

**Piper:** I am happy to get onboard with this one as well and suggest with provisionally allow it whilst we wait to hear from people who know can advise if this would break some tool.

**Martin:** I would prefer it to be separate to a hard fork encase of the hard fork not going to plan and the tools now do not work either. A change in a low activity period would be preferred. 

**Hudson:** Martin if you could revive the [Magicians thread](https://ethereum-magicians.org/t/eip-1803-rename-opcodes-for-clarity/3345) and get people to comment there about how this change may impact their tools? And based on feedback come back to the Core Dev call to make the final call.

** **
** DECISION 75.2:** EIP-1803 is eligible for inclusion and in moved to last call.
** ** 


## 6. EIPIP (EIP Improvement Proposal) Meeting
Video: [55:38](https://youtu.be/3qZFiETlDtk?t=3338)

**Hudson:** A few people from the Ethereum Foundation, Ethereum Cat Herders and Ethereum Magicians are gonna hold a meeting next week to discuss improving the EIP process. That will include all aspects, including the requirements to get EIP editors, how we can recruit EIP editors, redoing EIP-1, how to make the process clear to outsiders. Next week’s meeting will be the first one and then we will decide if we want to have more meetings after that. 

If you are interested in attending contact myself at hudson@ethereum.org. 

I may create a Gitter or Telegram group.

**Hudson:** This is a new meeting to improve the EIP process.
 
## 7. Review previous decisions made and action items
- [Call 74](https://github.com/ethereum/pm/blob/master/All%20Core%20Devs%20Meetings/Meeting%2074.md)
Video: [56:44](https://youtu.be/3qZFiETlDtk?t=3404)

No further review required.

## 8. Client Updates

None 
 
## 9. Research Updates 

None

## 10. Any Other Business

General discussion around the Ice Age and calculating when it will occur. Vitalik wrote a script and Lane cleaned it up. It is a fairly manual process and James Hancock is working on it.

## Attendance

- Alex Beregszaszi
- Brett Robertson
- Daniel Ellison
- Dimitry
- Danno Ferrin
- Hudson Jameson
- James Hancock
- Mikhail Kalinin
- Martin Holst Swende
- Martin Lundfall
- Peter Szilagyi
- Phil Lucsok
- Piper Merriam
- Pooja Ranjan
- Tim Beiko 
- Trenton van Epps
- Wei Tang
