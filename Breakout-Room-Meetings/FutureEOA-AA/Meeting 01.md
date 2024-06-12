# Future EOA/AA Breakout Room #1

Note: This file is copied from [here](https://notes.ethereum.org/QT9e9r6NRdSOjWRBzA3JLA)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/962

**Date & Time**: Feb 28, 2024, 14:00-15:00 UTC

**Recording**: https://youtube.com/live/FfEZdTFAz4E

### Relevant links

- Call agenda and [recording](https://www.youtube.com/watch?v=FfEZdTFAz4E)
- [Execution Layer Meeting #182](https://www.youtube.com/watch?v=4ioJwNPe6RU) which had a lot of AA discussion as well
- [ERC-4337 - Account Abstraction Using Alt Mempool](https://eips.ethereum.org/EIPS/eip-4337)
- [ERC-7562 - Account Abstraction Validation Scope Rules](https://eips.ethereum.org/EIPS/eip-7562)
- [RIP-7560 - Native Account Abstraction](https://github.com/ethereum/RIPs/blob/master/RIPS/rip-7560.md)
- [EIP-3074 - AUTH and AUTHCALL opcodes](https://eips.ethereum.org/EIPS/eip-3074)
- [EIP-5003 - Insert Code into EOAs with AUTHUSURP](https://eips.ethereum.org/EIPS/eip-5003)
- [EIP-5806 - Delegate transaction](https://eips.ethereum.org/EIPS/eip-5806)
- [EIP-2938 - Account Abstraction](https://eips.ethereum.org/EIPS/eip-2938)
- [EIP-7377 - Migration Transaction](https://eips.ethereum.org/EIPS/eip-7377)
- [EIP-7553 - Separated Payer Transaction](https://github.com/ethereum/EIPs/pull/7949)

### Call summary
Everyone wants AA, but there are many unanswered questions so far:

- What is the desired AA endgoal? Which proposal is best in the trade-off space?
- Should we be improving EOAs? If so, how do we do it safely with AA endgoal in mind?
- Should L1 pave the way to L2s (in terms of standard) or should standards be implemented/tested/adopted on L2s before enshrinment on L1?
- How much bandwidth do we have for a big upgrade vs. a smaller incremental step towards AA in Prague? What are the immediate steps?

Main desires from AA endgoal:

- Basic security mechanisms: Key rotation/revocation
- Quantum resistance
- UX improvements: Gas sponsorship, batching, signature aggregation

### Intro
We are planning the next hard fork (Prague) and there’s been many proposals around AA, so now we want to explore the scope of various proposals, and see how much bandwidth we got towards inclusion of AA of some form in next fork

The biggest challenge is getting everybody to agree on what the right plan is. We need wallet devs, app developpers, etc. to chime in since they will be the ones using new account capabilities. They’re the ones most in touch with users doing transactions and the UX flow etc.

What are the direction we want? Must-haves (short/medium term)? Get rough consensus, look into existing proposals, potentially new proposals, that might go into the next hard fork. Then we can see if we can be ambitious for long term past forks.

## Context
### From lightclient
We all want AA, trying to find the ways to get there as the endgoal. We have various options available: “True AA” (or “Native protocol AA”), ERC4337, enshrinment via 7560, etc. It doesn’t feel like it’s currently in a place to be enshrined in the near future. Mainly because it changes a lot of the flow of transactions.

It’s clear that the changes should be inside the transaction rather than the protocol. We can look into something different, e.g. EIP2938 is simpler, but doesnt address the desires of AA from people: No easy paymaster, no reoccurring payments, it’s too simple and limited compared to 7560.

No clear path yet towards AA enshrinement. We want to think about how to provide that primitive to users. Also ask if we should provide that to users. Given desires for AA specifically with paymasters, not sure if we should enshrine that type of logic into the protocol.

To support paymasters you need to have validation of different frames of execution, send payment to paymaster, etc. It feels like the more specific we get into specific workflows and uses-cases, the more “generality” we lose from the protocol

Other part of the discussion is how to improve EOAs, but there’s also questions about whether we should do this at all. Two proposals: 3074 makes EOAs better and potentially compatible with 4337. (See [yoav’s post comparing 3074 and 4337](https://notes.ethereum.org/@yoav/eip-3074-erc-4337-synergy)). 3074 gives execution abstract, UX benefits that users wants. But doesn’t change how you validator transaction. So no true mechanisms for recovering/rotating keys. Security concerns around 3074: Will people migrate, or stay on plain EOAs? Further enshrining EOAs or ECDSA?

5806 is also proposed and picked up steam, makes EOAs better. Some concern that it turns into the next EIP2930 (Access List Transactions). We could come up with some solution that get people to move off to EOA and then have EOA sitting around forever. Maybe we should go that direction in the near term as it does provide value in the near term. EIP3074 shines a little more, maintaining the op code is easier long term. But EIP5806 is very safe and simple, doesnt change much the intuition around transaction flow/validation.

**Big question**: Should we be improving EOAs?

We havent really found the path to whatever end state we want, a reasonsable compromise might be to support 7377 which allows EOAs to upgrade to smart contract wallets (one-time code migration) if people will have SC wallets in the future it improves the EOA experience, since today’s users have the ability to migrate without sending every single asset. Minimizes the risk by doing something simpler. Still many questions to answer

### From Vitalik
In every other branch of Ethereum protocol R&D, there’s been big change over the past 5 years. 5 years ago things were very blue sky, a lot of holding out for the possibility of future discoveries. But now every part of the eth roadmap there’s a mindset that we actually have spent a lot of time exploring and we need to settle on something and build toward this (ex. state trie -> clear consensus on verkle trie and stark friendly upgrade in the future, PoS -> SSF roadmap, DA scaling -> roadmap is clear, L2 scaling, etc.)

But in the wallet space today, we’re at the point where we are in the position to make that mentality shift, but it feels like we haven’t quite yet made that shift. Now is exactly the right time that we should make it. There are a few properties of accounts in the Ethereum long term game that we generally understand are just necessary security properties. Like ability to make key changes, revoking old keys, things that are considered basic in traditional cybersecurity. EOAs don’t currently support that. Eventually, Quantum Computers could can kill EOAs as we know them today, we’ll have to see if we want to keep ECDSA or switch, etc.

Some more UX side things like batching, sponsorship, and signature aggregation, we know what proposals satisfy all of these good and how they look like. Basically figuring out the next step is very difficult if we don't understand what long-term goal we want. We have to figure out what the initial steps are and at the same time figure out if in the short term, we can have both an existing 4337 and EOA ecosystem, can we improve them in watch steps instead of having two branches and end up deprecating one of them.

Spending some time thinking back to front and get consensus. Another big thing is having a clear answer consensus on Is Ethereum L1 meant to be friendly to users, or just rollups/L2s? Either are valid visions, but there are other consequences. Like is it worth canceling EOF, canceling TSTORE, etc. L1 being L2-exclusive has consequences, we generally want L1 that continues to be friendly to users even if the bulk of txs is happening on L2. If that’s the case then that’s something we need to accept and internalize that whatever the long term account solution is, it’s something that L1 is going to be a part of. So that’s the context for where the need to get ourselves aligned on some of these goals.

Regarding ERC4337, a common question is “what in all of this stuff, does 4337 by itself not satisfy?” Main answers:

- **Inclusion lists compatibility** - The argument is that it’s pointless to include ILs in the standard until we actually have them on L1. But some endgame IL design is ultimately going to exist
- **Gas cost issues**. Verkle trie gas cost design will solve a lot of that.
- **Bundler/relayer are not quantum resistant**. Doesn't make 4337 impossible. You can still work around it but it’s annoying
- **TSTORE behaves differently for calls and transactions**. In between L1 transactions tstorage gets cleared, but between 4337 calls it doesn’t, so it’s a different behaviour that devs have to kind in mind
- **Extra complexity to developers**. Important to think about. One of those places where it’s important to think about an endgame that reunifies the structures we’ve been creating in the short term.

## Discussion
### Sponsorship and batching
Arik argues that it’s the most important feature, as it unlocks vastly better UX for “onboarding the next billion users” by not having them need to acquire the gas token first. It’s definitely important on the short term, not just long term. Should be the first priority in whatever plan we come up with. Batching is another good UX improvement (e.g. no longer need to approve and then swap in two different transactions)

Tim: If we did either of those things, do they block us in the future endgame? Will be back ourselves in a corner if something is great and adopted on L2 but can't be enshrined on L1 because of decisions made today.

Vitalik: On the convert to SC side, it feels like the sort of thing that’s not forward incompatible with other proposals because once you have a SC wallet with a self-upgrade functionality, so you can upgrade it to any other SC wallet in the future anyway

## Account migration / Improving EOAs
EIP-7377 allows a one-time migration from an EOA to any type of smart contract wallet (including 4337). Lightclient raises the point that it might be confusing to users for cross-chain applications and similar purposes that the EOA’s private key might still be useful in the future to deploy the same SC wallet on another chain at the same address.

Alex Jupiter: Could we solve that on the wallet side? Potentially reduce the burden of hardforking. Make it the responsibility of the wallet to move all assets etc.

Vitalik: It gets talked about, but in practice it’s even harder because there’s so many applications that people forget they participated in.

Tim: The cost can also be a problem. For example having 50$ of 20 different tokens, the gas cost on L1 quickly becomes prohibitive to make all the transfers.

---

After a possible migration scheme, do we still want to support plain EOAs forever? e.g. what if I forget about Ethereum for 4 years, is my EOA still valid, can I still do stuff with it?

Vitalik: We’d have to make an opcode that initializes an account at an address based on the hash of a public key who’s code is a standardized thing that accepts ECDSA from that account’s key. Like the big thing to keep in mind there is always going to be a SC wallet design that is able to create equivalent functionalities to what EOAs do. We can arguably force conversion from EOA to SC with equivalent functionalities.

### Test on L2s first
ERC4337 is currently gaining adoption, especially on L2s. Is it worth testing out what enshrinement looks like on L2s and then potentially bring that to L1’s core protocol?

Ansgar: the question is will we be able to actually introduce meaningful changes EIPs to L2s if they’re not supported by L1s or any of the layer 1 clients. For example, Geth wouldn't support an enshrined 4337 unless it comes to mainnet (too much code to change and maintain that’s not directly relevant to L1). So the idea of L2s first is a somewhat restricted path. L1 sets the default to L2s so do we want to change L1 specifically to influence L2s for better UX on L2s? Have to embrace that L1 is the settlement layer. Most users will be priced out from L1 anyway. Focusing on powerusers on L1 doesn't make sense. The main reason to think about it is to guide Layer 2s.

Vitalik: There’s a challenge with L1 being almost compatible but not quite. Expect wallets to want to provide as many functionalities on as many chains as possible, and L1 is realistically gonna be one of them for a long time, so if wallets have to write custom code for L1 just to serve a few powerusers then it’s a significant burden on them. Big part of the reason why saying either we’re supporting L1 as a user-friendly chain, or we’re deciding that L1 is not for users and fully embracing that.

### Big vs small changes
Tim: As Matt said, we’re in this impasse where either we lean into these larger AA overhauls (enshrine 4337 or 2938 and what not, can be separate conversation in more depth). If we only focus on that, this means that the status quo remains the same on L1 for the next year or so, which might be fine but people will complain and say we do nothing for users. But alternatively, we go with the smallest incremental improvements we can make on L1, do those now while the broader AA roadmap gets fleshed out, and be mindful of compatibility with that to avoid backing ourselves into a corner.

Andrew: I agree, but a smaller EIP like 5806 doesn’t conflict with any bigger AA proposals, there will be a new legacy transaction type but so what? Doesn’t matter we’ll have some legacy stuff anyway.

Matt: 5806 specifically doesn't support AA, goes into a different branch (delegation), and really only addresses the third most useful thing, not worth enshrining in protocol forever.

Andrew: Maybe not specifically that one but we can consider a small EIP for sponsored transactions. But 5806 is simple to implement, it doesn't introduce incompatibility, and brings a benefit to users

Matt: I would rather enshrine 3074 with the requirement that the message is only valid for the current nonce of the account, so you’re signing a blank check forever. That for me would be a better feature towards improving EOA



