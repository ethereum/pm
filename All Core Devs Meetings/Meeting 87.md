# All Core Devs Meeting 87 Notes
### Meeting Date/Time: Friday 15 May 2020, 14:00 UTC
### Meeting Duration: 1.5 hrs
### [Github Agenda](https://github.com/ethereum/pm/issues/169)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=bGgzALuyY3w)
### Moderator: Hudson Jameson
### Notes: Jim Bennett

---

# Summary

## EIP Status

EIP | Status
---|---
EIP-2537, EIP-2315 | `Accepted` Targetting Berlin
EIP-1057, EIP-1803, EIP-1559 | `Accepted`
EIP-2464 | `Last Call`
EIP-1380, EIP-2046,  EIP-2456, EIP-2315, EIP-2541, EIP-2539, EIP-1985, EIP-1702, EIP-1380, EIP-663 | `Eligible for Inclusion`
EIP-1702 | `Eligible for Inclusion` Pending Champion. Not scheduled for Berlin
EIP-663, EIP-2348, UNGAS | Depends on EIP-1702
EIP-1962,  EIP 2456, EIP 2515 | Discussed under `EFI`. Discussion to be continued in EthMagician thread |
EIP-2515 | Discussed under `EFI`. Decision required around needing a Hard Fork

*Note—Removed EIPs included in Muir Glacier.*

## Decisions Made

Decision Item | Description
--|--
**87.1**   | Ephemeral testnet name YOLO (you only live once) to test these Berlin EIPs
**87.1.1** | 2315, 2537

## Actions Needed

Action Item | Description
---|---
**86.1** | Decision required on looking at the contract code for Simple Subroutines.
**86.2** | James to reach out to Alexi for merkalization in Simple Subroutines.
**86.3** | ProgPoW compromise proposal to be decided on (testnet then pocket).
**86.4** | Update EIP bot with Withdrawn
**86.5** | Move EIP-2583 to Withdrawn


---

# Agenda

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:1 updateOnSave:1 -->

- [1. Berlin EIPs - Integration Updates](#1-berlin-eips-integration-updates)   
- [2. Eligible for Inclusion (EFI) EIP Review](#2-eligible-for-inclusion-efi-eip-review)   
- [3. Berlin Timing](#3-berlin-timing)   
- [4. EIP-1057: ProgPoW, a Programmatic Proof-of-Work.](#4-eip-1057-progpow-a-programmatic-proof-of-work)   
- [5. EIP-2565: Repricing of the EIP-198 ModExp precompile. Specifically the open-ethereum benchmarking results per this comment.](#5-eip-2565-repricing-of-the-eip-198-modexp-precompile-specifically-the-open-ethereum-benchmarking-results-per-this-comment)   
- [6. PR to change "hard fork" to "network upgrade" in EIP-1 and common vernacular](#6-pr-to-change-hard-fork-to-network-upgrade-in-eip-1-and-common-vernacular)     
- [7. State tree format conversion with the tree overlay method](#7-state-tree-format-conversion-with-the-tree-overlay-method)   
- [8. EIP-2315: “Simple Subroutines for the EVM” analysis](#8-eip-2315-“simple-subroutines-for-the-evm”-analysis)   
- [9. EIP-1559 implementers' call update](#9-eip-1559-implementers-call-update)   
- [10. EIP-2583: Penalty for account trie misses](#10-eip-2583-penalty-for-account-trie-misses)    
- [11. Testing updates](#11-testing-updates)   
- [12. Review previous decisions made and action items (if notes available)](#12-review-previous-decisions-made-and-action-items-if-notes-available)   


---


# 1. Berlin EIPs - Integration Updates

Video | [5:36](https://youtu.be/MOZ7_0Tb95M?t=336)
-|-

The EIP for changing the difficulty bomb is possible for Berlin, but still needs a lot of work.

## 1.1 EIP-2537: BLS12-381 curve operations

Updates from Besu. Implementation is donne. Only missing contract addresses.

Updates from Geth. The integration with Geth is more or less done. Still quite some work required.

Updates from Open Ethereum. Have not yet started implementations. Awaiting an independent audited verification.

Updates from Nethermind. No updates since last meeting. Has done BLS implentation on Eth2.0.

Update from WASM. WASM implementation of BLS is ready, can be used by any client. Code is quite stable.


## 1.2 EIP-2315: Simple Subroutines for the EVM

Updates from Geth. State tests have been implemented passing Besu and Geth. A new proposal was introduced, walking into a subroutine, and preventing jumping into a subroutine. Running into issues coding preventing jumping across subroutine boundaries.

Updates from Open Ethereum. Subroutines is close to done, there is an open pull request for it, awaiting a final review.

Updates from Nethermind. No updates since last meeting. Awaiting to see the first implementation done and some tests.

It may be premature to decide that it will or will not make it into Berlin. Berlin will be dependent on BLS EIP. Subroutines may or may not make it, making Berlin potentially a one EIP network upgrade.

## Actions

- **86.1**—Decision required on looking at the contract code for Simple Subroutines.
- **86.2**—James to reach out to Alexi for merkalization in Simple Subroutines.

## Decisions

- **86.1**—Berlin will be dependent on BLS EIP. Subroutines may or may not make it, making Berlin potentially a one EIP network upgrade.

# 2. Eligible for Inclusion (EFI) EIP Review

Video | [21:46](https://youtu.be/MOZ7_0Tb95M?t=1306)
-|-

## 2.1 EIP-2515: Difficulty Bomb

No update.

## 2.2 EIP-2046: Reduced gas cost for static calls made to precompiles

No update.

# 3. Berlin Timing

Video | [22:13](https://youtu.be/MOZ7_0Tb95M?t=1333)
-|-

Contingent on EIP-2537.


# 4. EIP-1057: ProgPoW, a Programmatic Proof-of-Work.

Video | [22:32](https://youtu.be/MOZ7_0Tb95M?t=1352)
-|-

Ben Difransico's compromise proposal is to have the code ready and deployed on a testnet, ready incase the security risk it prevents starts to arise.

The `0.93` baseline is in most clients. A `0.94` version includes the Kik fix and addresses Least Authority suggestion for the light evaluation attack. The PR to the if-def-else repo is final. Awaiting for a few more comments to be merged.

Ravencoin is migrating to `0.94` with minor modifications to their mainnet on May 6th.

**Stefan George**: Currently Gnosis is against ProgPoW as it would favor one party over another.

**Artem Vorotnikov**: Open Ethereum would like to see clear community consensus for ProgPoW before it's pushed to mainnet.

**Peter Szilagyi**: ProgPoW is more computationally intensive, from a technical standpoint. ProgPoW blocks would take more time to verify, even if not significant, is a negative. The philisophical viewpoint is another consideration. The Ropsten testnet is more or less dead. Ropsten is kept as a proof of work testnet. If ProgPoW is to be considered at any point, we should relaunch a PoW testnet with ProgPoW. A ProgPoW testnet would indicate to clients if they can create and verify blocks. I don't see us deploying ProgPoW on mainnet anytime soon. Our goal is to keep Ethereum mainnet in one piece. If we want to protect against arbitrary re-orgs by ASICs, ProgPoW should be tested beforehand on a testnet and be ready. We shouldn't switch over until someone starts abusing Ethash.

**Michael Carter** (BBT): Agree with Peter on the creation of PROGPOW Testnet - will coordinate with Andrea and find support to help establish this. Once established, I can help communicate it to the community know how to access and help test.

No decision made for ProgPoW on this call.

Latest discussions on ProgPoW can be seen and can be joined in the IfDefElse repository on the PRs, or the ProgPoW review Gitter channel.

- https://gitter.im/ethereum-cat-herders/ProgPoW-review
- https://ethereum-magicians.org/t/a-progpow-compromise-pre-proposal/4057
- https://github.com/ifdefelse/ProgPOW/pull/52

## Actions

- **86.3**—ProgPoW compromise proposal to be decided on (testnet then pocket).

# 5. EIP-2565: Repricing of the EIP-198 ModExp precompile. Specifically the open-ethereum benchmarking results per this comment.

Video | [41:21](https://youtu.be/MOZ7_0Tb95M?t=2481)
-|-

Parity (Open Ethereum) is on average 2.5-6x slower than the Geth implementation. The simple pricing formula changes would result in certain Parity operations being underpriced in gas. Given Open Ethereum's library, the simple parameter change can't be made.

The options are replacing the underlying library. Benchmarks are pending.

The other option is modifying the gas pricing formula.

Updating the Crate used in Open Ethereum, and implementing the new pricing formula resulted in nothing being underpriced for Parity.

The question for the Open Ethereum team, if an updated library is found for the precompile, would they be open to accepting a pull request? Or just go with the updated pricing formula?

**Artem Vorotnikov**: We should try all the improvements available. And if we still don't approach Geth, we should only then try the pricing formula change in my opinion. If you have any improvements in mind, you're always welcome to hop on our Discord and Github.

**Kelly**: We should be able to come back in two weeks with a recommended library change.

**Artem Vorotnikov**: Once there are benchmarks, we can start merging.

**Peter Szilagyi**: Go is not considered a blazing fast language. I'm curious why the performance gap.

**Martin Holst Swende**: An old comment was that Parity did exponentiation by squaring.

**Kelly**: I don't think it's a Rust performance issue, but the underlying algorithms used by Parity. I'd like to come back in 2 weeks with updates, and then move to `EFI` next meeting.

# 6. PR to change "hard fork" to "network upgrade" in EIP-1 and common vernacular

Video | [51:08](https://youtu.be/MOZ7_0Tb95M?t=3068)
-|-


Over the past few years, the Ethereum Foundation has used the term Network Upgrades over Hard Forks in their blogs. On other networks, hard forks may be dramatic and rare events. Hard forks are also percieved as the result of a contentious upgrade resulting in a chain split. The third reason is for clarity, where people think they'll recieve free coins where it's not the case.

The PR currently changes it in EIP-1. However, if pursuinng this change, it may be worth to do it across the entire EIP repo.

This is a small technical change, but a large political and philisophical one.

**Hudson Jameson**: Would we use hard fork when it is contentious?

**Tim Beiko**: I think that's the way to take it.

**Greg Colvin**: We have the term chain split for that.

**Martin Holst Swende**: It's a hard fork if it's a non-compatible change. It's a soft fork if you restrict, instead of expand, so it's backwards compatible. And then there's a chain-split, which can be caused by a hard-fork.

**Tim Beiko**: We want to separate the normal case of a hard-fork with the exceptional case of a chain-split. My PR was based on how the EF addresses them. I'm not sure what the best way to separate those concepts are.  

**Greg Colvin**: Any upgrade is presented as a PR to the existing code-base. Then the hard-fork picks it up on the network. If things don't go fine, we end up with a chain-split.

**Hudson Jameson**: That's true on a technical level. The EF blog had been using network upgrade as it's a term Zcash had been using. Zcash made it clear to their constituents that it wasn't openly controversial and was not creating free coins. There was a lot of scams going on, so the priority was to make it more clear to the braoder community. It takes a paragraph to three paragraph to define the differences with hard-fork, while with network upgrade, the difference is clear.

**James Hancock**: I was originally in the camp of techinically it's a hard fork. But for someone who doesn't have the technical experience, you have to get a deep level to just explain the concept. While they're the same, socially they're very different. We can invest a lot of time to convince people that hard-fork means not what they think it means, or use terminology that has people naturally come to that conclusion.

**Peter Szilagyi**: I like the change. Everytime we approach a hard fork, everyone asks if they get new coins. So people are misunderstanding it. It might help.

**Pooja Ranjan**: The developers are well aware of the difference between a hard-fork and a chain-split. But the community will use the generalize term. If it's defined in EIP-1 that would be helpful. To reduce confusion, going with network upgrade may be better.

**Peter Szilagyi**: I can see some voices raising concern that we may be trying to hide that a network upgrade is a hard-fork. In EIP-1, we can make it abundantly clear what a network upgrade means. We shouldn't hide that a network upgrade is a hard-fork.

**Michael Carter**: Maybe a quick traceability/matrix document that can be posted somewhere 'official' that is written in English? Create a draft -> go through a review across ACD offline then post final. Rather simple language (agnostic to English rather)

**Tim Beiko**: Would it make sense to add something in EIP-1, and also define that they won't necessarily result in a chain-split. And use network upgrade when we talk of the upgrade itself, like on Meta-EIPs.

**Hudson Jameson**: The final decision may come down to the EIP editors. Alex did ask to bring it up in this call to get opinions from the Core Devs. We can move it to last call if it doesn't see any community dissent.

**Tim Beiko**: Because this is a PR to EIP-1, there's no status associated with it.

**axic**: The discussion is to use different terminology than hard fork, which is relevant to more than EIP-1.

**Tim Beiko**: I'm wondering what the best way to go through in process would be for this.

**axic**: I don't think there's a formal process to changes to EIP-1.

**James Hancock**: It sounds like the Core Devs are leaning to yes for this kind of change. We could have a section in EFI that is for PRs like this.

**Pooja Ranjan**: Should we open a Magician's thread?

**Tim Beiko**: I'll open one as soon as the new PR is live.

**James Hancock**: Is it worth motioning that there is consensus among the Core Devs on this item?

**Hudson Jameson**: I think so.

- https://github.com/ethereum/EIPs/pull/2624
- https://github.com/ethereum/EIPs/pull/2516
- https://ethereum-magicians.org/t/using-network-upgrade-over-hard-fork-in-the-eips-repo/4255

## Decisions

Core Devs agree with network upgrade over hard-fork in documentation.


# 7. State tree format conversion with the tree overlay method

Video | [1:07:08](https://youtu.be/MOZ7_0Tb95M?t=4028)
-|-

Stems from the Eth1.x meeting in Paris. One way is to stop blocks, and once enough time has passed for everyone to be up-to-date, to start minting blocks again with a new root.

Another method was to convert branches into trie one by one. When enough time has elapsed, everyone is assumed to be up to speed on the conversion. Then slowly start merging the trie back a couple hundred accounts at a time. Then drop the extra root, and continue with the binary trie.


**Peter Szilagyi**: One thing unclear to me is the simplified version is in theory, keep using the current trie until a block, then use the binary trie. There's nothing stopping from generating the binary trie three weeks before the hard-fork. If we were to maintain 2 tries, that would be 50-100 milisecond of overhead per block. That wouldn't be significant. I'm not sure why we would create complexity on the protocol level, and ensure the trie is ready by the hard-fork time.

**Guillaume**: When you have a phase, you have a justification to increasing the gas price.

**Peter Szilagyi**: I don't see how gas prices relates to this.

**Guillaume**: You're going to have to write double, no?

**Peter Szilagyi**: Yes.

**Guillaume**: That has to be impacted somewhere.

**Martin Holst Swende**: Block time would increase, incentivizing miners to increase gas prices, or lower the amount of gas consumed.

**Guillaume**: In that case you increase gas prices across the board. Rather than increases gas prices for just store.

**Martin Holst Swende**: But your proposal isn't tied to gas pricing.

**Guillaume**: It's mentioned in the EIP.

**Peter Szilagyi**: For me that seems like an extreme over-complication. I don't see it sufficient for the miners to bump the gas price. It's still a lot safer for the gas prices to be higher for a week, than increasing complexity at the consensus layer where clients can go out of sync.

**Guillaume**: I don't know how long per block it would take. But from what I see, it's quite a lot of calculations. For that period of time, you'd need to implement post-tries.

**Peter Szilagyi**: In Geth we already do a similar thing when we generate snap-shots. Maybe a similar approach can be done, were the switch to binary tries would be 24 hours before the schedule of the hard-fork.

**Guillaume**: That's also the case of my approach. Roughly 24 hours, based on the snapshotter. If you run at the same time, you have the write problem.

**Hudson Jameson**: I want to time-box this. Please finish your last thoughts.

**Peter Szilagyi**: My point is, it's more advantagious to keep the consensus protocol simple, even if client implementation gets more complicated.

**Martin Holst Swende**: I made some proposed changes to Guillaume, to keep things simple by only producing empty blocks, no deletions and no complications like that, only amounting to a couple thousand changes during this period, which can be merged again. For Peter's varient, we just switch over, which may be more difficult for other clients.

**Guillaume**: Further discussions can be done in the PR. There's also a link to the PR to eth.research.

- https://github.com/ethereum/EIPs/pull/2584

# 8. EIP-2315: “Simple Subroutines for the EVM” analysis

Video | [1:18:25](https://youtu.be/MOZ7_0Tb95M?t=4705)
-|-

- https://ethereum-magicians.org/t/eip-2315-simple-subroutines-for-the-evm-analysis/4229

This was discussed in the beginning of the call.

# 9. EIP-1559 implementers' call update

Video | [1:19:24](https://youtu.be/MOZ7_0Tb95M?t=4764)
-|-

- https://twitter.com/TimBeiko/status/1255874207805837313

The EIP has been worked on and off for the past year. The Geth implementation is mostly done. There's a working implementation on Besu, interoperating with Geth. On the call there was a counter proposal.

- https://github.com/ethereum/EIPs/pull/2593

You provide a range of minimum gas to pay, maximum gas, and number of blocks willing to wait. Gas would be increased block by block.

The bulk of the call was comparing the two proposals. Next is an economic analysis, and seeing if they can be combined.

On the client side, a small testnet will be setup.

A final thing that came up was the user UX changes. Metamask may come up with something, and a community bounty may be made for this.

A follow-up call in one month.

# 10. EIP-2583: Penalty for account trie misses

Video | [1:22:25](https://youtu.be/MOZ7_0Tb95M?t=4945)
-|-


- https://github.com/ethereum/EIPs/pull/2583

Can be taken off future agendas. Potentially a better model using gas an oil.

This EIP needs to be moved to Withdrawn.

## Actions

- **86.4**—Update EIP bot with Withdrawn
- **86.5**—Move EIP-2583 to Withdrawn


# 11. Testing updates

Video | [1:23:50](https://youtu.be/MOZ7_0Tb95M?t=5030)
-|-


Nethermind and Besu are almost first citizens. Will be when they can run a consensus test.

It's ethdevops.io.

Working on state transition tool.

Dimitry is working on state tests and blockchain tests.



# 12. Review previous decisions made and action items (if notes available)

Video | [1:25:39](https://youtu.be/MOZ7_0Tb95M?t=5139)
-|-

Issue ran into where decision and action items were inaccurate for previous meetings. A stricter review process is being looked into.

Another thing we want to do is add hyperlinks to the EIPs.

**Tim Beiko**: One thing that might help the Cat Herders is being more prompt updating the EIP status after Core Devs calls. Rather than trying to parse what the rough consensus is.

**Hudson Jameson**: That's good. And there may be other process changes discussed in the ACD gitter, Cat Herders gitter, and EIPIP call. Including explicitly saying a decision has been accepted.

---

# Annex


## Attendance


- Alex (axic)
- Andrea Lanfranchi
- Artem Vorotnikov
- David Mechler
- Edson Ayllon
- Greg Colvin
- Guillaume
- Hudson Jameson
- Kelly
- Michael Carter (BBT)
- Peter Szilagyi
- Pooja Ranjan
- Stefan George
- Tim Beiko
- Tomasz Stanczak


## Next Meeting Date/Time

Friday 15 May 2020, 14:00 UTC
