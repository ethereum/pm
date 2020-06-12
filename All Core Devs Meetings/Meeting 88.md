# All Core Devs Meeting 88 Notes
### Meeting Date/Time: Friday, May 29 2020, 14:00 UTC
### Meeting Duration: 1:13 hrs
### [GitHub Agenda](https://github.com/ethereum/pm/issues/172)
### [Audio/Video of the meeting](https://youtube.com/watch?v=UJ1jK73rKdk)
### Moderator: Hudson Jameson
### Notes: William Schwab

---

# Summary

## EIP Status

EIP | Status
2315, 2537 | Accepted for Berlin and YOLOv1 testnet
2565 | EFI, proposed for Berlin, currently not included in YOLO
2046, 2666 | Under Discussion

## Decisions Made

Decision Item | Description
--|--
**88.1** | State tests for YOLO-v1 should be regenerated under that name (and should not carry the Berlin name)
**88.2** | Opcode change proposal to be implemented

## Actions Required

Action Item | Description
--|--
**88.1** | James Hancock to continue to update the Berlin and YOLO EIPs, including commit hashes
**88.2** | Ephemeral testnet EIP to be merged
**88.3** | James Hancock to follow up with Open Ethereum, Axic, and Martin to discuss EIP-2315 after this call
**88.4** | Axic to make a PR to update opcodes for EIP-2315
**88.5** | James Hancock to coordinate with Axic and interested parties about a precompile gas cost changes call
**88.6** | kelly to continue working with Open Ethereum on EIP-2565

---

# Agenda

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 bullets:1 updateOnSave:1 -->
- [1. Berlin EIPs - Integration Updates](#1-berlin-eips-integration-update)
    - [1a. EIP-2315: Simple Subroutines for the EVM](#1a-eip-2315-simple-subroutines-for-the-evm)
    - [1b. EIP-2537: BLS12-381 Curve Operations](#1b-eip-2537-bls12-381-curve-operations)
- [2. Eligible for Inclusion (EFI) EIP Review](#2-eligible-for-inclusion-efi-eip-review))
- [3. EIP 2666: Repricing of Precompiles and Keccak256 Function](#3-eip-2666-repricing-of-precompiles-and-keccak256-function)
- [4. EIP 1559 Update](#4-eip-1559-update)
- [5. EIP: Limit Size of initcode](#5-eip-limit-size-of-initcode)
- [6. Berlin Timing](#6-berlin-timing)
- [7. EIPIP Working Group/Survey](#7-eipip-working-group-survey)
- [8. Testing Updates](#8-testing-updates)
- [9. Review Previous Decisions and Action Items](#9-review-previous-decisions-and-action-items)

# 1. Berlin EIPs - Integration Updates

Video | [3:50](https://youtu.be/UJ1jK73rKdk?t=230)
-|-

**James Hancock**: As a part of standardizing the EIP and network upgrade processes, we will include integration testing using ephemeral testnets as part of the upgrade process in order to assure multi-client compatibility. This is not a statement about including specific EIPs on mainnet. Community should understand that these ephemeral nets are not for deploying code, but for client testing. They will be nuked.

Current spec for an ephemeral testnet (called YOLO) include EIP 2537 (BLS precompile). EIP 2315 is working towards being specified. EIP 2565(1) will not be included due to feedback from the Open Ethereum team. 'Not included' means only that once there is a specification that makes sense, that the ephemeral testnet can be redeployed. Again, none of these statements represent any commitment to deploying on mainnet.

The process for adopting this ephemeral testnet (YOLO-v1) is being tracked on [the EIP page for the creation of YOLO](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2657.md).

**Martin Holst Swende**: The specification should include that state tests should also run under the name YOLO-v1, whereas they seem to be named Berlin currently. This can circumvent issues of miscommunication arising from the name Berlin appearing in the tests, which can lead to the mistaken impression that clients are Berlin-ready when they are not.

## Decisions
- **88.1**-State tests for YOLO-v1 should be regenerated under that name (and should not carry the Berlin name)

# 1a. EIP-2315: Simple Subroutines for the EVM
Video | [13:27](https://youtu.be/UJ1jK73rKdk?t=807)
-|-

**Martin Holst Swende**: The original EIP 2315 has been modified. There is a PR submitted chanigng the gas prices. Feeling of general consensus. Has not heard form Open Ethereum, Besu has already integrated. The other question is whether or not to implement the subroutine restrictions suggested by Axic, which is still under discussion. Possible agreement of using non-restricted subroutines for the testnet. If given a go-ahead, will merge.

**David Mechler (Open Ethereum)**: Will evaluate after call. PR already made reflecting some changes to EIP 2315, another will be needed.

**James Hancock**: The state in which EIP 2315 goes in to the YOLO testnet does not reflect the state in which it may go into mainnet, but is rather a convenience in implementation that might help us better understand in which state it should go into mainnet, if at all.

**Alex (axic)**: There is another change proposal for different opcodes from those appearing in the EIp that was brought up about a month ago to use a linear opcode space so that the opcode means the actual byte, and the instruction is what the byte is doing, but seems to have quieted down. Should those proposals be reflected in YOLO?

**Martin Holst Swende**: Proposal makes sense, but does not need to be included in YOLO.

Discussion about the necessity of such an implementation between Peter Szilagyi and Alex (axic).

**Alex (axic)**: Questions nature of testnet: is it only for client implementation and trying to break it, or also for users to test out functionality?

**Peter Szilagyi**: No one is stopping users from trying it out.

**Martin Holst Swende**: If someone makes an experimental compiler and then it changes, it could make a mess, though.

**Peter Szilagyi**: Doesn't see the actual bytecodes as a sticking point, and asks that if there is even a slight reason to change the opcodes, why not implement change now already?

**Hudson Jameson**: Couldn't these changes be merged at the same time as changes already discussed?

**Martin Holst Swende**: Agrees, though it would take a bit of work.

**Alex (axic)**: Agrees.

## Decisions
- **88.2**-Opcode change proposal to be implemented

## Action Items
- **88.1**-James Hancock to continue to update the Berlin and YOLO EIPs, including commit hashes
- **88.2**-Ephemeral testnet EIP to be merged
- **88.3**-James Hancock to follow up with Open Ethereum, Axic, and Martin to discuss EIP-2315 after this call
- **88.4**-Axic to make a PR to update opcodes for EIP-2315

# 1b. EIP-2537: BLS12-381 Curve Operations
Video | [22:15](https://youtu.be/UJ1jK73rKdk?t=1335)
-|-

**Peter Szilagyi (Geth)**: The Geth PR with the precompiled code in it is 'hanging in the air'. Serious testing and fuzzing has begun. Many potential issues, concerns, and bugs have arisen. There are issues in the assembly code, some communication has happened, iteration has occurred, which has resulted in completely new assembly code being merged four days ago (with the old assembly code being deleted), making it unviable to properly implement in time.

**Alex Vlasov**: Recommends using the pure Go implementation, which also fits in the gas window. If having assembly is a problem, the assembly code can be removed.

**Peter Szilagyi**: The problem isn't in assembly being used per se, rather that the PR was not properly tested. A fork cannot be rushed into if the spec has not been properly refined.

**Martin Holst Swende (Geth)**: Having both versions was good, because it allowed for differential fuzzing. (More details on the state of fuzzing this spec.) Fuzz testing the clients against each other in a differential mode is a couple of weeks of work. Also need to replecate benchmarking, and that the Go and assembly implementations fit in the gas schedules. Theoretically something could still be merged in testnet, but skeptical of going live with anything in the near-term future.

**Alex Vlasov**: Mentions that there have been new accomplishments in allowing differential fuzzing. Details about the original testing on the assembly version. If assembly is cut, performance would not be an issue, and could focus on getting one implementation ready.

**Martin Holst Swende**: Still estimates that actual implementation-readiness is weeks away. Some discussion with Alex Vlasov about the nature of the fuzzing tests.

**James Hancock**: Is there anything that can be defined in terms of including this EIP in YOLO?

Some conversation between Hudson, James, Peter, Martin. No tentative date reached for inclusion in YOLO.

**Artem Vorotnikov (Open Ethereum)**: Currently focusing on the PR by Alex, which is under review, and expected to be merged soon.

**Rai (Besu)**: PR has already been merged.

**Tomasz Stanczak (Nethermind)**: Should be working on this over the weekned, with intent to test and merge, though not promising. Will check if possible with current codebase, or if there are new operations only possible with Alex's PR. Intends to write C# wrapper, and to provide code to Geth in order to work on fuzzing together.

**Jason Carver (Trinity)**: Work in progress, no major update.

EthereumJS not present.

# 2. Eligible for Inclusion (EFI) EIP Review
Video | [38:23](https://youtu.be/UJ1jK73rKdk?t=2302)
-|-

## 2.1 EIP-2046: Reduced Gas Cost for Static Calls Made to Precompiles

Related to EIP-2666.

**Alex Vlasov**: Long technical description, including status of EIP-2666. Also asked if views 2666 as superseding 2046, and spoke to that.

**Alex (axic)**: Still interested in 2046, talked about potential ways forward. Probably needs a dedicated call, All Core Devs does not seem to be the right venue for discussing precompile repricing.

## Action Items
- **88.5**-James Hancock to coordinate with Axic and interested parties about a precompile gas cost changes call

## 2.2 EIP 2565

(Will not go into YOLOv1.)

**kelly**: Decided on implementing pricing formula in order to not need to change the Open Ethereum libraries. Artem has implemented a draft PR, kelly is in the process of updating the EIP. Once this is done, it can be shared with the Geth team, and a PR can be formed.

## Action Items
- **88.6**-kelly to continue working with Open Ethereum on EIP-2565

# 3. EIP 2666: Repricing of Precompiles and Keccak256 Function
Video | n/a
-|-

Was included in the discussion on EIP-2046 above.

# 4. EIP 1559 Update
Video | [48:45](https://youtu.be/UJ1jK73rKdk?t=2925)
-|-

**Abdelhamid Bakhta**: Talks about results of EIP-1559 call, has a new PR to remove part of the spec. Discussions about best settings for implementation testing. Also more technical details. 

Call has been uploaded to the Ethereum Foundation YouTube. Dan Finlay has mockups for those wishing to educate themselves more on the subject.

# 5. EIP: Limit Size of initcode
Video | [52:09](https://youtu.be/UJ1jK73rKdk?t=3129)
-|-

**Martin Holst Swende**: Speaking for a group of people who want to limit the size of initcode, reasoning being that it can be used to attack jump analysis (and has been used to do so), and also a possible future motivation if restricted subroutines are introduced, which would make it more complicated for clients to guard themselves from such attacks.

# 6. Berlin Timing
Video | [55:00](https://youtu.be/UJ1jK73rKdk?t=3300)
-|-

No update (focus is on YOLO)

# 7. EIPIP Working Group/Survey
Video | [55:20](https://youtu.be/UJ1jK73rKdk?t=3320)
-|-

**Edson Ayllon**: Descibes goals of EIPIP (trying to make positive change to EIP process). Describes survey about EIP process. Poll also had ability to reflect current values of community. Main findings seem to be that people want structure, legitimacy, and focus on the technical aspects. Barrier to entry should be low, barrier to approval should be high, but the process should be transparent and fair. Roadmap forward centers around improving decision making, clarity, and increasing capacity, and will most likely be addressed in that order. Currently discussing decision making.

Results of the survey have been published to the Etherem Cat Herders' Medium.

# 8. Testing Updates
Video | [59:08](https://youtu.be/UJ1jK73rKdk?t=3548)
-|-

No updates

# 9. Review Previous Decisions and Action Items
Video | [59:30](https://youtu.be/UJ1jK73rKdk?t=3570)
-|-

Some discussion about how to signal that an EIP is going into an ephemral testnet happened at the end of this section.

**Decisions**:
- 87.1 EIPs 2315 and 2537 to be accepted into Berlin
- 87.2 YOLO to be created as an ephemeral testnet
    - 87.2.1 EIPs 2315 and 2537 to be implemented in YOLO
- 87.3 Updates on EIP-2046 appear in this call, can be called resolved
- 87.4 Outstanding spec issues in EIP-2315 resolved in this call
- 87.5 Precompile to be listed by early next week by Alex Vlasov in order to finalize

**Actions Required**:
- 87.1 Decision required on Simple Subroutine contract code - Resolved in meeting
- 86.2 (from two meetings ago) James to contact Alexi for merkalization for Simple Subroutines - Completed
- 86.3 ProgPoW testnet - Ongoing
- 87.4 Update EIP bot with Withdrawn - Ongoing
- 87.5 Move EIP-2583 to Withdrawn - Ongoing
- 87.6 James Hancock to review EFI EIP and accept existing PRs - Completed
- 87.7 Alex (axic) to review Berlin EIP and accept existing PRs - Completed


## Attendees
- Abdelhamid Bakhta
- Alex (axic)
- Alex Vlasov
- Artem Vorotnikov
- David Mechler
- Edson Ayllon
- Hudson Jameson
- James Hancock
- Jason Carver
- Karim Taam
- kelly
- Martin Holst Swende
- Peter Szilagyi
- Pooja Ranjan
- Rai
- Tomasz Stanczak
- Wei Tang

## Next Meeting Date/Time

Friday, Jun 12 2020, 14:00 UTC
