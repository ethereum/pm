# All Core Devs Meeting 95 Notes
### Meeting Date/Time: Friday 4 Sept 2020, 14:00 UTC
### Meeting Duration: 1.5 hrs
### [Github Agenda](https://github.com/ethereum/pm/issues/203)
### [Audio/Video of the meeting](https://youtu.be/-Jefyrs4f70)
### Moderator: Hudson Jameson
### Notes: Edson Ayllon

---

# Summary

## EIP Status

EIP | Status
--|--
2718, 2929, 2935 | Going into YOLOv2
2930, 2315 | Continue discussion for YOLOv2

## Decisions Made

Decision Item | Decision
-|-
95.1 | Add [EIP 2718](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2718.md): Typed Transaction Envelope to YOLO v2.
95.2 | Add [EIP-2929](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2929.md): Gas cost increases for state access opcodes to YOLO v2.
95.3 | Continue to discuss [EIP-2930](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2930.md): Optional access lists.
95.4 | Continue discussion of [EIP-2315](https://eips.ethereum.org/EIPS/eip-2315): Simple Subroutines for the EVM in Eth Magicians forum.
95.5 | Add [EIP-2935](https://eips.ethereum.org/EIPS/eip-2935): Save historical block hashes in state to YOLO v2.
95.6| [EIP-2711](https://eips.ethereum.org/EIPS/eip-2711): Sponsored, expiring and batch transactions was only discussed today as an overview for the purpose of future discussion and not to be considered for inclusion, EFI, or anything else as of this meeting.
95.7 | Add Account Abstraction item to next ACD meeting agenda. See this comment: https://github.com/ethereum/pm/issues/203#issuecomment-686923605
95.8 | Add Ethereum Cat Herders Survey Results to the next ACD meeting agenda.

---

# Contents
 
- [Contents](#contents)   
- [1. EIP Discussion](#1-eip-discussion)   
   - [1.1 Potentially removing gas refund (see comment).](#11-potentially-removing-gas-refund-see-comment)   
   - [1.2 EIP 2718: Typed Transaction Envelope (general-purpose standard for adding new transaction types).](#12-eip-2718-typed-transaction-envelope-general-purpose-standard-for-adding-new-transaction-types)   
   - [1.3 EIP-2929: Gas cost increases for state access opcodes.](#13-eip-2929-gas-cost-increases-for-state-access-opcodes)   
   - [1.4 EIP-2930: Optional access lists.](#14-eip-2930-optional-access-lists)   
   - [1.4 EIP-2315: Simple Subroutines for the EVM.](#14-eip-2315-simple-subroutines-for-the-evm)   
   - [1.5 General discussion on the idea of combining some of the above EIPs that create a new transaction type, so we just create a single new transaction type that has a whole bunch of the features together.](#15-general-discussion-on-the-idea-of-combining-some-of-the-above-eips-that-create-a-new-transaction-type-so-we-just-create-a-single-new-transaction-type-that-has-a-whole-bunch-of-the-features-together)   
   - [1.6 EIP-2935: Save historical block hashes in state.](#16-eip-2935-save-historical-block-hashes-in-state)   
   - [1.7 EIP-2711: Sponsored, expiring and batch transactions.](#17-eip-2711-sponsored-expiring-and-batch-transactions)   
   - [1.8 EIP-1057 Next Steps.](#18-eip-1057-next-steps)   
- [2. EIP & Upgrades Updates](#2-eip-upgrades-updates)   
   - [2.1 YOLO / YOLOv2 & Berlin state tests update](#21-yolo-yolov2-berlin-state-tests-update)   
   - [2.2 EIP-1559 Update](#22-eip-1559-update)   
   - [2.3 Account abstraction: AA EIP and AA DoS study](#23-account-abstraction-aa-eip-and-aa-dos-study)   

---


# 1. EIP Discussion
## 1.1 Potentially removing gas refund (see comment).

Video | [0:00](https://youtu.be/-Jefyrs4f70)
-|-

Alexey, by observing transactions, noticed it's like an order book. Where people bid for the gas prices. Low bid orders are there to scoop the dips. However, in exchanges you can cancel orders at no cost. But, in Ethereum, you can send another transaction to yourself at a higher gas, or spam the pool so much that it takes it out.

This may be a reason we can't reach high gas prices. As people buy the dip, they go high again.

Looking at Chi token, the magnitude wasn't congruent with it causing the gas prices to rise. Chi tokens only consumed 10% of all gas consumed. We can't blame Chi tokens for sustained high gas prices.


## 1.2 EIP 2718: Typed Transaction Envelope (general-purpose standard for adding new transaction types).

Video | [10:12](https://youtu.be/-Jefyrs4f70?t=612)
-|-

From Micah Zoltou, in draft status right now. It's in EFI right now.

There are no formats defined that defines an access list. This only is a format to provide extensibility in transactions. The access list EIP is 2930.

There is discussion about combining some EIPs into new transaction types, as there is overlap.

This EIP changes transactions to have an outer envelope, and a leading integer that denotes the type of transaction.

Traditionally, we've only had 1 transaction type. But we have a couple EIPs that want to introduce changes to transactions. Rather than guessing what transaction type it is by the elements, there may be errors, we specify the transaction type.

It's an integer with a payload field. How you interpret the payload field is dependent on the initial integer.

This also allows clients to drop transaction types they don't recognize. It may not be used, but it's there as a feature.

Legacy transaction types, current transactions, they'll be wrapped as they are. For all other transaction types, they'll include a transaction number in the signature. This prevents the replay problem.

The signature is included in the payload. Future transaction types can use a different way to sign.

In the Cat Herder's call, it was suggested, when there are a lot of questions in the ACD call, that we can have break out sessions after. This dsicussion will be tabled there.

It may be best to have 2718 not bundled with other EIPs to get it released without much complexity. It may be good for YOLOv2.

There is specification for what to do with pending transactions on the fork block.

## 1.3 EIP-2929: Gas cost increases for state access opcodes.

Video | [28:41](https://youtu.be/-Jefyrs4f70?t=1721)
-|-

Increases the gas cost for first time accesses. This mitigates against DOS attacks and have gas costs more accurately reflect computation time. The blocks that take the longest to process are the IO heavy ones.

Gas costs of average applications would only increase by 2%. Most applications are written very efficiently. It surgically targets making the thing that needs to be expensive.

This EIP may supercede other EIPs people have been trying to push historically.

**Alexey**: This EIP introduces a read list. Before we only had a write list. The correct solution I see is, yes increase the gas cost. But instead, introduce a specialized primitive so we can cache.

**Vitalik**: I see it being less complicated. This uses transaction wide global variables, which are used in refunds, and self destruct. There is value having this out in the fairly short term.

**Alexey**: First of all, is this really important? Do people really do that? If it is, we should introduce a mechanism for that.

**Martin**: Solidity does it every time you make calls. We're not adding another cache layer. We're adding a boolean. Implementation wise, it's not too hard.

**Vitalik**: If you want to get the benefit of not double charging ERC20 tokens, you have to redeploy every ERC20 token.

**Alexey**: My main concern isn't performance. My main concern is complexity.

**Vitalik**: These are things we've already done.

**Martin**: I shared those concerns, that's why I made an implementation.

**Hudson**: I'll table this. Continue on EthMagicians. Or if you want to request a breakout room, reach out to me or Pooja or Edson from the Cat Herders.


## 1.4 EIP-2930: Optional access lists.

Video | [43:29](https://youtu.be/-Jefyrs4f70?t=2609)
-|-

It allows you to prepay higher gas cost for accessesing storage costs and addresses for the first time. This mitigates breaking contracts that rely on fixed gas limits.

The EIP itself is not super complex. If we want to have another transaction type, this is the simplest one to include.

Geth would like to implement this, along with another client. Geth wants it in YOLOv2.

This EIP may be in YOLOv2, but not accepted yet.

For 2718, at first, only the clients need an implementation. As more transaction types are added, contracts may also need compatability.


## 1.4 EIP-2315: Simple Subroutines for the EVM.

Video | [54:33](https://youtu.be/-Jefyrs4f70?t=3273)
-|-

This one is in YOLOv1. Will go over into YOLOv2.

Did write custom fuzzer targeting subroutine, and no issues found.

The last feature, not jumpting into subroutines. Should continue in the Magician's thread.

## 1.5 General discussion on the idea of combining some of the above EIPs that create a new transaction type, so we just create a single new transaction type that has a whole bunch of the features together.

Video | [56:49](https://youtu.be/-Jefyrs4f70?t=3409)
-|-

Skipped for now.


## 1.6 EIP-2935: Save historical block hashes in state.

Video | [57:40](https://youtu.be/-Jefyrs4f70?t=3460)
-|-

You stick the hash of the previous block into a storage slot before processing the current block, keeping a simple and dumb method of ensuring  blocks have a quick merkle path to all historical blocks since the EIP was introduced.

In terms of state size growth, it would add a gain of 1% to the current state growth size.

The benefits are in the category of creating layer 2 protocols.

It's simpler than putting an accumulator in the header.

There are some DeFi projects that would greatly benefit from this.

This would also allow tracking the history without a header chain.

This EIP may go into YOLOv2.

Something to consider for YOLO version, clients have to implement all EIPs going into the testnet, or tney'll be kicked out. So, a lot of these EIPs going into YOLOv2 are very simple. This one is 2 lines of specification.

## 1.7 EIP-2711: Sponsored, expiring and batch transactions.

Video | [1:08:01](https://youtu.be/-Jefyrs4f70?t=4141)
-|-

This was supposed to be the first 2718 transaction. A new transaction type that handles user experiences annoyances in the Dapp space.

Sponsored transactions: Instead of having a single signer, we have 2 signers. The second signer is the one who pays for gas. This is in layer 1, which is much cleaner than solving it in the Dapp layer.


Batch transactions: One or more transactions, atomic in that they make it in the order you specify, with nothing in-between. They are not atomic in that they all fail or they all succeed. Instead of having Dapps that send multiple transactions, one to approve, and the other to commit the action, it's a single transaction.

Also adds optional expiration field, that invalidates a transaction after a specified timestamp. Uniswap has this currently. But, the transactions still exist on chain, so after their expiry in uniswap, it just fails instantly, which leads to large losses of gas.

There's one gas price for the entire batch.

Time boxed until later.


## 1.8 EIP-1057 Next Steps.

Video | [1:19:09](https://youtu.be/-Jefyrs4f70?t=4749)
-|-

Instead of going into decisions, just going into updates.

Andrea, one of the authors, just got out of the hospital, so he's reviewing code just before he went into the hospital. It looks like the kik exploit is nothing to worry about.

It looks like existing exploits will fall out of the network in November, so that's a time to deploy ProgPoW if it will be deployed.


# 2. EIP & Upgrades Updates

Video | [5:29](https://youtu.be/-Jefyrs4f70?t=329)
-|-

A lot of questions about Berlin and timing for Berlin. Why the timing for Berlin hasn't been announced is that it's dependent on YOLOv2. For EIPs that go into YOLOv2, it is possible they go into Berlin, but it doesn't mean they are slated for the Berlin upgrade.

EIPs in YOLOv2 are considered for testnet first, then client integration testing, and that will determine its inclusion.

As for the name, it's not called Berlinv2, as EIPs that are in YOLOv2 may not go into a hardfork at all. Testnets after Berlin may be YOLOv3, or something else. YOLO is meant to show that the testnet will live for a short time.

## 2.1 YOLO / YOLOv2 & Berlin state tests update

Video | [1:20:54](https://youtu.be/-Jefyrs4f70?t=4854)
-|-

Going into YOLOv2:
- 2718
- 2929
- 2935

Continue discussion on:
- 2930
- 2315 (already on YOLOv1)

Continue EFI Discussion
- 2711

2 left to talk about: 2565, 2046. 2565 is moving into final. The other is 2046. 2929 would supercede 2046. 2046 is pending until 2929 is decided on.


## 2.2 EIP-1559 Update

Video | [1:31:32](https://youtu.be/-Jefyrs4f70?t=5492)
-|-

Implementors call last week.

Testnet between Besu and Geth from Vulcanize.

EF is doing some simulations on the EIP. Looking at what happens when there's spikes. Next for having agents outbid each other.

Formal analysis will be done by a game theorist.

Next steps will be to get more client implementations, and have a proof of work testnet.


## 2.3 Account abstraction: AA EIP and AA DoS study

Video | [1:27:26](https://youtu.be/-Jefyrs4f70?t=5246)
-|-

One of the concerns for account abstraction is the DOS vectors and vulnerabilies. Study released on EthResearch.

The goal is to expand the set of conditions transactions have for valid inclusion in the chain.

The use cases are:  Single tenant account transaction. Smart contracts, multisigs, etc.

Too complex and too new to be considered for Berlin.

---

# Annex


## Attendance

- Alex (axic)
- Alex Vlasov
- Ansgar Deitrichs
- Ansgar Deitrichs
- Artem Vorotnikov
- Daniel Ellison
- David Mechier
- David Murdoch
- Edson Ayllon
- Greg Colvin
- Hudson Jameson
- James Hancock
- Jason Carver
- Kelly
- Martin Hoist Swende
- Micah Zoltou
- Pawel Bylica
- Peter Szilagyi
- Piper Merriam
- Pooja Ranjan
- Rai Sur
- Sam Wilson
- Tim Beiko
- Tomasz Stanczak
- Vitalik Buterin
- Will Villanueva
- lightclient


## Next Meeting Date/Time

Friday 18 Sept 2020, 14:00 UTC

## Call Chat


From Edson Ayllon to Everyone: (10:04 AM)

Agenda: https://github.com/ethereum/pm/issues/203

From Micah to Everyone: (10:12 AM)

Essentially "YOLO" is the pre-hardfork integration network?

From Tomasz Stanczak to Everyone: (10:13 AM)

the name YOLO was to suggest users to not expect it to surviveit went sideways :)

From Micah to Everyone: (10:13 AM)

👍So it is the ephemeral integration test network. 👍

From James Hancock to Everyone: (10:14 AM)

Yes, for client integration testing and fuzz testing

From Micah to Everyone: (10:14 AM)

2718 was EFI2711 I don't think was discussed.No mic.I can *find* a mic if it is necessary.Sec.

From Hudson Jameson to Everyone: (10:15 AM)

Yeah find a mic plz

From Tomasz Stanczak to Everyone: (10:16 AM)

We introduce a new EIP-2718 transaction type, with the format rlp([3, [nonce, gasPrice, gasLimit, to, value, data, access_list, senderV, senderR, senderS]]).EIP starts this waywhich is already using iton 2930https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2930.md

From Micah to Everyone: (10:18 AM)

Have mic now, and fixed feedback.

From Tomasz Stanczak to Everyone: (10:22 AM)

you can sign and then extract some of the signed dataas designedmakes sense

From Tomasz Stanczak to Everyone: (10:22 AM)

one is protecting against replay, the other gives hint on serialization format

From Micah to Everyone: (10:26 AM)

👍 I support breakouts. I always feel bad taking time up from ACD calls. 😬

From lightclient to Everyone: (10:26 AM)

also supportbtw i'm working on an impl of 2718, please ping me on discord to coordinate if interested

From Pooja Ranjan to Everyone: (10:27 AM)

sure

From Tomasz Stanczak to Everyone: (10:28 AM)

agreedI am for

From Micah to Everyone: (10:32 AM)

Sounds like James wants it on YOLO v2. 😉

From James Hancock to Everyone: (10:32 AM)

:)

From lightclient to Everyone: (10:32 AM)

IMO, transaction propagation doesn't need to *immediately* transition all txs to the new type -- they just have to be properly encode them in new blocks past the FORK_BLOCK

From James Hancock to Everyone: (10:32 AM)

Happy to have anyone disagree

From James Hancock to Everyone: (10:33 AM)

I just don't want to get held up on what will happen for mainnet at this point, as we can address that on another callas it progresses forward.

From lightclient to Everyone: (10:34 AM)

also, i went searching for the comment from Micah regarding eip-2930 and it not being a good fit for eip-2718, but couldn't find it -- could someone point it to me please?

From Micah to Everyone: (10:39 AM)

@lightclient you are probably thinking of my commentary that we should maybe combine 2930, 2711, and 1559.

From James Hancock to Everyone: (10:40 AM)

My suggestion to that is if we have them in the same integration testnet, you get the optimization of work for the clients without having to bundle the decisions around them.So you don't need to combine the EIPs

From lightclient to Everyone: (10:41 AM)

@micah: ah okay, maybe misheard earlier, but it sounded like there was miscommunication with Martin where he thought you had said 2930 shouldn't be a 2718 tx type

From Micah to Everyone: (10:41 AM)

I don't think I have argued against 2930 as 2718.

From lightclient to Everyone: (10:42 AM)

got it, ty

From Micah to Everyone: (10:43 AM)

@James The problem at the moment is that if we combine them into one testnet, they are currently planned as separate transaction types, but I think (maybe) there is value in having most of them be one new transaction type with several optional fields.

From James Hancock to Everyone: (10:44 AM)

Got it, That is a different discussion than I understood.

From Micah to Everyone: (10:44 AM)

👍

From Hudson Jameson to Everyone: (10:44 AM)

Time boxing this soon.

From Tim Beiko to Everyone: (10:51 AM)

What is 2935?

From Vitalik Buterin to Everyone: (10:51 AM)

https://github.com/ethereum/EIPs/blob/master/EIPS/eip-2935.md

From James Hancock to Everyone: (10:52 AM)

historical block hashes

From Vitalik Buterin to Everyone: (10:52 AM)

Happy to talk about it for a few seconds if people want, it's super simple

From Tomasz Stanczak to Everyone: (10:52 AM)

2929 for sure in

From Tim Beiko to Everyone: (10:52 AM)

How about 2929 in and 2930 on hold?

From Micah to Everyone: (10:52 AM)

Make all blockhashes available, instead of the last 256 (very short version).My 0 votes says 2929 is pretty important, 2930 is "would be cool".

From Tomasz Stanczak to Everyone: (10:53 AM)

2929 is a must

From Tomasz Stanczak to Everyone: (10:53 AM)

2930 I believe there may be a redesign for it and we are not using it yetI think it makes sense to call current transactions 'naked' like a naked burrito without a wrap

From Micah to Everyone: (10:56 AM)

🥗

From Micah to Everyone: (10:56 AM)

I think the clients should be able to build the access list on behalf of the user for 2930?

From Tomasz Stanczak to Everyone: (10:56 AM)

this is also why I think that 'access list' is awkward for the current YOLO - it will be even hard to test

From Micah to Everyone: (10:57 AM)

Hmm, but only if they are doing the signing I guess.That is, the *signer* needs to be able to deal with access lists.So... MetaMask. 😉

From Tomasz Stanczak to Everyone: (10:57 AM)

yes2315 implemented in Nethermind

it is in YOLO

From Tomasz Stanczak to Everyone: (11:00 AM)

do we have the test cases for benchmarking 2565?

From Alex (axic) to Me: (Privately) (11:01 AM)

I know that ignoring the transactiontype field for type=0 for signing is there so they can be upgraded easily, but is it a good idea to exclude the leading byte?Sorry meant to send to everyone :)

From Alex (axic) to Everyone: (11:02 AM)

I know that ignoring the transactiontype field for type=0 for signing is there so they can be upgraded easily, but is it a good idea to exclude the leading byte?

From James Hancock to Everyone: (11:02 AM)

I think there is some for some of the clients

From kelly to Everyone: (11:02 AM)

Tomasz - I can provide the new expected gas costs in the ACD costs for EIP-2565oops in the ACD chat*Micah also had a few suggestions for the EIP before it is finalized and it may be a good idea to put the updated test vector results in there as well

From kelly to Everyone: (11:04 AM)

All test vectors for EIP-2565 are carried over from EIP-198 since EIP-2565 just changes the gas pricing formula

From Tomasz Stanczak to Everyone: (11:04 AM)

we would love to see 2935we have lots of use casesaround DeFi solutions

From Micah to Everyone: (11:05 AM)

I have a project that already is live but is limited to 1 hour instead of infinity hours. :)

From Tomasz Stanczak to Everyone: (11:05 AM)

exactly

From Micah to Everyone: (11:07 AM)

https://github.com/Keydonix/uniswap-oracle/ for an example use case. (trustless price feed via Uniswap)Heh, I think 1559 is less complex than 2929. 😉

From Vitalik Buterin to Everyone: (11:12 AM)

There's complexity of specification and complexity of consequences :)

From Tomasz Stanczak to Everyone: (11:12 AM)

EIP-2046: Reduced gas cost for static calls made to precompiles.cost change only, need benchmarks so need testnet EIP-2315: Simple Subroutines for the EVM. already implemented EIP-2537: Precompile for BLS12-381 curve operations (already in YOLOv1). already implemented EIP-2711: Sponsored, expiring and batch transactions. demanding EIP 2718: Typed Transaction Envelope (general-purpose standard for adding new transaction types). simple and we need it EIP-2565: Repricing of the EIP-198 ModExp precompile. repricing only - worth to have for benchmarks EIP-2929: Gas cost increases for state access opcodes. repricing mainly, critical EIP-2930: Optional access lists. (Nethermind slighlty against for YOLOv2) EIP-2935: Save historical block hashes in state. yes, please (from Nethermind)

From Vitalik Buterin to Everyone: (11:12 AM)

Agree that the new 1559 is quite simple spec-wise

From Tomasz Stanczak to Everyone: (11:13 AM)

2711 is great and needed but 2718 first wouldbe great

From Micah to Everyone: (11:21 AM)

I'll get it for you, one sec.

From lightclient to Everyone: (11:21 AM)

EIP-2803: https://eips.ethereum.org/EIPS/eip-2803

From Micah to Everyone: (11:21 AM)

https://eips.ethereum.org/EIPS/eip-2803 (Rich Transactions)

From Alex Vlasov to Everyone: (11:25 AM)

We are in a state when decision on 2046 can be made without extra dependencies

From Vitalik Buterin to Everyone: (11:27 AM)

Do we need 2046 if 2929 is going in? It de-facto includes the functionality

From Alex Vlasov to Everyone: (11:27 AM)

This one is just simple to implement immediatelly

From Tim Beiko to Everyone: (11:31 AM)

What was the outcome for 2046?

From James Hancock to Everyone: (11:31 AM)

2929 is in yolo, 2046 is in pending

From James Hancock to Everyone: (11:32 AM)

https://github.com/ethereum/eth1.0-specs/projects/1Working from a project board here

From Hudson Jameson to Everyone: (11:34 AM)

Correction 2929 will be in Yolov2, not Yolo.

From James Hancock to Everyone: (11:35 AM)

Yes, thank you hudson

From Hudson Jameson to Everyone: (11:35 AM)

Here are the "Decisions Mae" for the note taker:

From Hudson Jameson to Everyone: (11:35 AM)

Decisions Made:Add EIP 2718: Typed Transaction Envelope to YOLO v2. Add EIP-2929: Gas cost increases for state access opcodes to YOLO v2. Continue to discuss EIP-2930: Optional access lists. Continue discussion of EIP-2315: Simple Subroutines for the EVM in Eth Magicians forum. Add EIP-2935: Save historical block hashes in state to YOLO v2. EIP-2711: Sponsored, expiring and batch transactions was only discussed today as an overview for the purpose of future discussion and not to be considered for inclusion, EFI, or anything else as of this meeting. Add Account Abstraction item to next ACD meeting agenda. See this comment: https://github.com/ethereum/pm/issues/203#issuecomment-686923605 Add Ethereum Cat Herders Survey Results to the next ACD meeting agenda. Note taker: Please hyperlink the EIP URLs to the EIPs referenced in the decisions made section in the notes. You can find them in today's agenda.

From Pooja Ranjan to Everyone: (11:36 AM)

Sure!
