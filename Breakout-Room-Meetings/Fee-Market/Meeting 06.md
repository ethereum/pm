# EIP-1559 Implementers' Call 6 Notes <!-- omit in toc -->

### Meeting Date/Time: Thursday, Nov 5th, 14:00 UTC <!-- omit in toc -->

### Meeting Duration: 1 hr <!-- omit in toc -->

### [GitHub Agenda](https://github.com/ethereum/pm/issues/215) <!-- omit in toc -->

### Audio/Video of the meeting: [Part 1](https://www.youtube.com/watch?v=LgvUnCdMXQg), [Part 2](https://www.youtube.com/watch?v=oa4r8m-a2yM) <!-- omit in toc -->

### Moderator: Tim Beiko <!-- omit in toc -->

### Notes: Edson Ayllon <!-- omit in toc -->

---


# Contents <!-- omit in toc -->

- [Summary](#summary)
  - [Actions Required](#actions-required)
- [1. Status updates from implementers and researchers](#1-status-updates-from-implementers-and-researchers)
  - [1.1 Testnets](#11-testnets)
    - [Client updates on PoA testnet](#client-updates-on-poa-testnet)
      - [Nethermind](#nethermind)
      - [Besu](#besu)
      - [Geth](#geth)
    - [Next steps for testnets](#next-steps-for-testnets)
    - [Actions](#actions)
  - [1.2 Demo - 1559 Toolbox](#12-demo---1559-toolbox)
  - [1.3 Simulations - Floating escalator notebook](#13-simulations---floating-escalator-notebook)
- [2. EIP-2718 - Now part of YOLOv3, likely for Berlin, do we update 1559 to require it?](#2-eip-2718---now-part-of-yolov3-likely-for-berlin-do-we-update-1559-to-require-it)
  - [Actions](#actions-1)
- [3. Mainnet readiness checklist review](#3-mainnet-readiness-checklist-review)
  - [Actions](#actions-2)
- [Annex](#annex)
  - [Attendance](#attendance)
  - [Next Meeting Date/Time](#next-meeting-datetime)
 
---



# Summary


## Actions Required

Action Item | Decision
-|-
**6.1** | Finish POA testnet
**6.2** | Create a testnet from a fork of mainnet
**6.3** | Add 2718 after mainnet large state fork.
**6.4** | Have every client what they do for replace by fee, for eviction, for accepting gossip of transaction, and transaction sorting.
---


# 1. Status updates from implementers and researchers
## 1.1 Testnets



### Client updates on PoA testnet

Video | [0:00](https://youtu.be/LgvUnCdMXQg)
-|-

#### Nethermind

- Fully synced with validating blocks
- Some problem with filling the blocks
- Issue with synchronization was very small, all fine.
- Will include a new employee working exclusively on 1559

#### Besu

- Nothing new on core Ethereum client, other than RPC endpoint
- Working on tooling, will discuss later

#### Geth

- Completed Geth code to align with latest version of EIP
- Test synchronization Geth to Geth, Geth to Besu, working on Geth to Nethermind, on a local network. Suggestions to test on testnet instead of local.

### Next steps for testnets

Video | [18:29](https://youtu.be/LgvUnCdMXQg?t=1109)
-|-

Questions to consider. How much more time should we spend on POA testnet? And should we look into proof of work in parallel? What's the next step?

First item - Should we also implement 2718? 

**Rick Dudley**: Large state? The blocks being bigger?

**Tim Beiko**: We'd like to test 1559 on a state comparable to mainnet to see performance impacts. 

**Tomasz Stanczak**: Questions on suggesting 2 pools. We already have just one pool only. 

**Rick Dudley**: Yes, moving to one pool was the last major change we made. It's already done.

**Rick Dudley**: Sorry, misunderstanding. Also, how would 1559 affect state? It seems independent.

**Abdelhamid Bakhta**: People are already worried about the actual state as the base goes up. Because of block elasticity, people are worried of the negative impact it could have.

**Tomasz Stanczak**: What's the difference between existing state and 1559? The state is only growing 10% faster, but it's only temporary. 

**Micah Zoltu**: The fear is a superlinear issue with gas per block, and a single block that's twice as big when interacting with large state network like mainnet could have superlinear costs. 

**Tim Beiko**: That's the concern. If we can at least run a testnet with 100 million accounts and 100 million storage slots, we can see if anything is much worse, where the blocks are much bigger. 

**Micah Zoltu**: Another alternative is forking off of mainnet, set the block gas limit to 40 million, fill a bunch of blocks, and see if anything crashes. 

**Tomasz Stanczak**: Maybe instead of faking this network, maybe lets just fork mainnet. We can use any accounts we want.

**Abdelhamid Bakhta**: It would be harder to have accounts with large values of ETH.

**Tim Beiko**: That would be part of the hardfork.

**Micah Zoltu**: You can disable signature checking as part of the hardfork.

**Tomasz Stanczak**: There's nothing like signature checking, it's just an abstraction of the address. So this is much harder.

**Micah Zoltu**: Treat the R value of the address.

**Tomasz Stanczak**: Maybe, but then the transaction format is different.

**Tim Beiko**: Maybe instead, have a list of whales in the hardfork. And set the mining difficulty to 0. 

**Micah Zoltu**: In general, I think forking mainnet in test will be useful in many situations. I think it may be to formalize it, maybe adding a config file, so others can do it. 

**Tomasz Stanczak**: We can share the Nethermind chainspec for such a chain, and people can sync to it. Anyone that has mainnet Eth can switch and start signing transactions.

**Rick Dudley**: Hard hat claims to do this. I'll share a link in the Discord.

**Tim Beiko**: Do we want a smaller PoW testnet in between? Or should we go to forking mainnet?

**Tomasz Stanczak**: Let's go to mainnet.

**Tim Beiko**: If we get a lot of bugs, maybe we can try something smaller. 

**Tomasz Stanczak**: I feel it'll be very useful in the future for testing new EIPs. 

**Tim Beiko**: Should we implement 2718 before we fork mainnet? Should the fork of mainnet be a new version of the 1559 spec?

**Tomasz Stanczak**: I prefer not to.

**Tim Beiko**: So go to mainnet immediately. After we see it works for mainnet, then add 2718. 

**Tomasz Stanczak**: It won't be a big time difference. I just don't want to wait to have 2718 to have the fork of mainnet. 

**Micah Zoltu**: Let me know when you're ready to do 2718, and I'll update 1559 with it. I don't want to have the EIP out of sync with what's live. 

**Tim Beiko**: Let's do that. Let's finish the POA fork we have. Share the information. And then fork with multiple clients from mainnet. And then after that, assuming everything goes smoothly, we can add 2718 on top, and have we'll already have this mainnet size testnet. 



### Actions

- **6.1**—Finish POA testnet
- **6.2**—Create a testnet from a fork of mainnet


## 1.2 Demo - 1559 Toolbox

Video | [10:57](https://youtu.be/LgvUnCdMXQg?t=657)
-|-

This EIP introduces breaking changes in UX. This impacts wallet providers and block explorers. 

Tooling may allow these users to interact with the testnet, and validate the implementation.

Tooling includes standard components with REST API. These submit transactions using legacy style with the new format. This may be changed again once typed transaction is launched. 

The API to submit transactions. And the API to retrieve the base fee. This will be a stand-alone HTTP service.

Additionally, built a web interface, that will allow users to test it. It does not work with web3 providers, only takes private keys. Will whitelist only private keys at genesis. Users can choose from a list of accounts loaded at genesis. 

The UI provides some links to the specification and the block explorer to the testnet. 

Also started to write a Wiki guide to join the testnet. Will need the genesis file and configuration file from Nethermind and Geth.

Demo showed with legacy transactions that will be converted. Switching to 1559, 2 new fields, and gas price not available anymore. The miner bribe and the fee cap. 

Will provide links in the Discord channel.

## 1.3 Simulations - Floating escalator notebook

Video | [4:01](https://youtu.be/LgvUnCdMXQg?t=241)
-|-

Notebook looks at combination of 1559 and escalator. Users can employ an incremental bid strategy, to increase their bids over time. 

In a previous notebook showed when demand is increasing quickly, users have incentive to have strategy to beat each other, which is seen in the current live fee price auction. 

Traditionally, users who send with a low fee can request a higher fee by resending the transaction. The escalator model bakes that strategy into the core protocol, where the user specifies a low transaction fee, and specifies how high he's will to escalate it. It will increase bewteen these two bounds. 

In 1559, you get a default entry price. Combining them, we start the bids at what the base fee would be. 

The notebook looks at two strategies. 

In the first, the base fee is increasing because demand is increasing. Alice is in more of a hurry than Bob. Originally it tracks the base fee. But over time, each individual escalates at their rate. 

The notebook looks at the mechanism within game theory. 

Two strategies:
1.  High cost for high speed
2. Don't care how fast the transaction is, but willing to wait 10 blocks. So the fee escalates until it's included in block 10. 

On the roadmap is looking for an equilibrium. 


# 2. EIP-2718 - Now part of YOLOv3, likely for Berlin, do we update 1559 to require it?

Video | [18:29](https://youtu.be/LgvUnCdMXQg?t=1109)
-|-

**Tim Beiko**: We should wait until it's scheduled for a hardfork. Not do work for it to be pulled out.

**Micah Zoltu**: I believe it will go out with the next new transaction type. If it's not 2930, then 1559 is a good candidate. The impression I have is, no one wants to add a new transaction type without it.

**Tim Beiko**: My concern is, it feels like it's not a blocker to add 2718 support. There's no huge rush to do it as well.

**Micah Zoltu**: It's something that needs to be done before 1559 launches. If we wait to do it later, then the clients will need to change it later. 

**Tim Beiko**: My hunch is, Open Ethereum won't implement anything until it's scheduled for mainnet. I'm not against implementing 2718.

**Rick Dudley**: I'd like to implement 2718 sooner rather than later. I don't know what the total roadmap. I know, there is a push to go to 1 transaction type, and remove 2 pools. Any testing?

**Tim Beiko**: I think 2718 is the last major spec change. Then testing proof of work, and dealing with a large state. In terms of big changes, 2718 will be the last one. 

Decision was to update 1559 after mainnet size testnet was made and tested.

## Actions

- **6.4**—Add 2718 after mainnet large state fork.


# 3. Mainnet readiness checklist review

Video | [32:09](https://youtu.be/LgvUnCdMXQg?t=1929)
-|-

Nethermind did hire someone. Cannot 100% confirm. Will be notified when to update that.

DoS risks are separate from the EIP itself.

Transaction encoding decoding, will wait until 2718.

Replaced by fee not fully hashed out. 

New format transactions will be prioritized. The new format incentive is to get a refund on fee cap. But, the intention is to tell clients to insert the new format first.

The push to 1559 may rely on wallet providers updating to 1559, and users without out-of-date wallets migrating to wallets with 1559. 

The advantage a 1559 wallet has over a legacy transaction may be 0 in terms of discount, if the legacy transaction is able to correctly price a transaction to their needs. However, the amount of engineering required to do that calculation is large. And under a 1559 wallet implementation, that calculation is trivial. The advantage is convenience to achieve cheaper transactions. 

Additionally, 1559, from the wallet provider's perspective, improves the user experience for their users in some conditions. An example Micah provided was with congestion, all Coinbase Wallet users had their transactions stuck, as they couldn't set their own gas prices. 1559 would offer a solution to that. 1559 causes pending transactions to be increasingly rare, when 6 blocks in a row are double full.

The transaction pool sorting can't be enforced in consensus without major changes to the spec. We don't neccessarily have to have a solution on that now.

However, with replace by fee, having a safe cononical formula all clients use may be preferred. 

There was one replace by fee formula made that was decent already. Something will be written up, and client teams will give feedback. 

The pool sorting mechanism may introduce some security concerns. May be worth fleshing out. It may go wrong if we don't at least describe it. 

Something to consider is evicting transactions. Where there may be a case where a transaction is evicted, that after fluctuations in base fee, would become valid. The argument against that, is not using the network as a personal transaction queue. It reduces the gossip of the network. 

May be best not to add another EIP until we're settled with some best practices. 

Testing, reference consensus tests, not there yet, as 2718 change not done.

Community testing starting. Will keep improving on it.

The public testnet is planned as a fork of mainnnet. 

One way to address the testnet is to aggressively restart the chain. There should be a process to finding the new chain. Can start with the 1559 Discord.

Nethermind is using 1559 as part of a client's network. Filecoin and Celo also have implemented 1559 in their networks. 

Vitalik put together some slides on 1559. 

Community outreach will continue with wallets and exchanges. 

## Actions

- **6.5**—Have every client what they do for replace by fee, for eviction, for accepting gossip of transaction, and transaction sorting.

---

# Annex


## Attendance

- Abdulhamid Bakhta
- Baranbe Monnot
- Micah Zoltu
- Rick Dudley
- Tim Beiko
- Tomasz Stanczak

## Next Meeting Date/Time

Thur. December 3, 2020, 1400 UTC.
