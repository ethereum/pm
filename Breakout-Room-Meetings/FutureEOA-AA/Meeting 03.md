Future of EOA/AA Breakout Room #3
--

## info
**Date**: May 29 2024, 14:00-15:00 UTC

**Agenda**: https://github.com/ethereum/pm/issues/1053

**Recording**: https://youtu.be/0vHHhZgrJ58

**Links shared in chat**:
* notes at the Berlin workshop by Ansgar: https://notes.ethereum.org/@ansgar/aa-meeting-berlin
* proxy pattern idea by Matt Garnett to discuss https://gist.github.com/lightclient/7742e84fde4962f32928c6177eda7523

## Next steps
- next call - 1 week from now, then bi-weekly
- start working on best practices

By next call we hope to 
- explore different specs & changes by Vitalik
- ERC Proxy [Richard & Ansgar]
- getting progress on best practice document [Ansgar]


## Agenda

Tim: Since the last meeting, PR on EIP7702 and the Berlin talk are the two main things. 
Hopefully, we can discuss and get next steps.

Matt: PR is based on different convo in Berlin and at different places.
In Berlin, we talked about some restrictions with wallet devs over there.

#### Takeaways from Berlin
- will not have a flag to persist the code, because of open question of EOA
- need to do more research on storage allowances

#### Issues
- storage key collision between..., added 7610
- Replay protection

Ansgar:
In Berlin , different dimensions and open questions were discussed.

- How do you specify the target
  - specify the address and not the code
- Decision is that launching something that is already having flag is not right
- other than storage, the other big thing was to start working on a wallet guidence
- how should this be supported by Ledger brought different questions and concerns, thus warrented for a guideline



### Pectra 7702 spec

#### [Update EIP-7702: refine based on discussions](https://github.com/ethereum/EIPs/pull/8561)

Ansgar Dietrichs 
I really think this PR should be merged instead of being the perpetual catch-all for all changes to the EIP. I keep meeting ppl that only see the main EIP and are unaware of any of these changes.


### AA Berlin Workshop Summary
#### Open questions:
##### **Replay Protection**

Ankur Dubey 
Just to confirm, for replay protection has it been decided that both nonce and chain_id will be optional, by setting it to 0?
 
Julian Rachman 
And then nonce would be set to null
 
Daniel Lehrner (Besu) 
Yes, just one correction: nonce must be null, not 0 to be optional. Because nonce 0 is a valid value.


##### **Storage Restrictions**
Yoav:
@lightclient @Ansgar Dietrichs  update re storage. I talked to the solidity team and they started looking into supporting storage layout remapping. Just got off a call with them and they're on it. If we agree on a standard for storage bases, it can be made safe without sstore restrictions.

Basically resolving this old issue:
https://github.com/ethereum/solidity/issues/597#issuecomment-1537533170

- whether to make it safe

Felix:
- it is usually unsafe to sign conflicting code, the safe side will be to allow only one proxy
- it will allow contract development system to develop the idea of storage system as it is fairly new


Konrad
- have a modular account with ref implementation, may send a PR
- Based on the PR it is pretty minimal effort
Pr for context: https://github.com/erc7579/erc7579-implementation/pull/29

Richard Meissner 
I tend to disagree @Konrad. I.e. with Safe the implementation effort is little, but migrating users is a huge effort. Also auditing this and performing formal verification with external storage increases complexity.

Ahmad
- specifying a proxy and only allowing single contract


Felix
- the difference is that changing destinantion of the proxy
- if want to switch from one to another wallet type, initially you'd point the proxy and when want to point to another wallet
- with authorization approach, you'd be allowed to sign by anyone and run code in the context of account. Will be more risky as it is not an onchain action to designate which code to be run.

Richard Meissner 
It is possible, but definitly way more effort than when we can directly use existing contracts. (Note: I do not see this as a blocker, just a comment on compexity)
 
Ansgar Dietrichs 
I will say, if we think the “only one authorized implementation at a time, with changes requiring onchain actions” pattern is desirable, we should think about a more fundamental change to 7702 instead of just enshrining a specific proxy as target

Ahmad: 
- it does not make sense to restrict the design

Richard Meissner 
I tend to disagree @Konrad. I.e. with Safe the implementation effort is little, but migrating users is a huge effort. Also auditing this and performing formal verification with external storage increases complexity.
 
Richard Meissner 
As said it is not a blocker, but we have to consider our existing users. Maintaining multiple contract versions is not really efficient over a longer time

Konrad 
Could this be determined at runtime (ie having a flag that determines whether  to use contract storage or external storage)? That way it’d only be one codebase

Ansgar Dietrichs 
I agree with felix to some extent: there is some risk that given pectra might be relatively soon, that we don’t have enough time to fully figure out best practices. in an ideal world then wallets would wait before adopting 7702, but competitive pressures might make this infeasible
 
thogard 
Could use a diamond storage pattern with address(this).codehash as the storage salt?
But I agree w/ yoav - sequential storage would be a nightmare

Ahmad: 
- I will not prevent SSTORE

Tim
- So the SSTORE will act like what TSTORE does

Ahmad
- Yes

Yoav
- We don't want it to work like TSTORE
- say, setting a threshold for an implementation and the threshold increases. We should not change the semantic

Richard Meissner 
Agree with @Yoav I.e. for a normal Safe you could replay txs as the nonce is in storage that would be reset

Ansgar
- External storage may be the better way

Richard: 
One point for the external storage pattern was, that keystore related pattern are going in a similar direction

Ankur
- Allow the user to specify the additional contract storage address
- if the user want to switch to another application, it switch to another storage code


Dan Finlay 
I thought part of the 7702 motivation was reusing existing code, so making a big difference in the behavior or implementation of these account extensions would seem like it compromises the benefits over 3074.
 
Dan Finlay 
I’ll note 3074 avoided storage issues.
 
Richard Meissner 
That is because 3074 acts like an external storage holder, right?
 
Dan Finlay 
right
 
Richard Meissner 
But agree that with allowing storage it would provide more benefits 

Dan Finlay 
the invoker initiates the message on behalf of the user

Ansgar Dietrichs 
I think it is pretty binary: either there are no changes, or it requires rewrite anyway

elim 
Using existing code as-is would be the dream. But if it requires minimal modifications, imo it's still better than an entirely different architecture as required by 3074. Since the 7702 modified wallets can still be used as-is for native aa.

Dror
- How much external storage change the implementation to EOA


Ansgar Dietrichs 
I also strongly disagree with implicit tstore behavior. if behavior is not identical, making it explicit breaking instead of implicit unexpected behavior is much preferable
 
Ansgar Dietrichs 
storage contract defined in tx would not be forward compatible with later permanent transitions, no? unless we would then store that storage contract location in the verkle node and have this difference of former-EOA contracts forever?

Ansgar Dietrichs 
I don’t think we can make final decisions on storage today. more important to figure out how we can get to making decisions on this over the next month or so
 
thogard 
One pattern would be to SSTORE / SLOADs point at keccak(actual slot, codehash) for EOAs, but that runs into the same nonce replay issue unless the nonces are stored externally.

Richard Meissner 
the "disadnavtage" with this would be that we have to touch existing opcode behaviour
 
Yoav 
I held the same opinion until solidity agreed to add namespaced storage 

lightclient 
allowing storage isn’t going to block migration
 
Yoav 
With that, it becomes easier to have a standard that all accounts should use

Matt:
Even if we have store, we see migration
- same thing discussion 
- Solidity is able to suggest storage
- if it is okay at the protocol level, then it is good
- Allowing SSTORE to work as it is supposed to work in a normal contract


**Tim**: Let's move forward with Storage and keep discussing. 

Matt
- in 7702 it is possible to delegate to code offchain and is natural. 
- It is more likely a situation where user will end up
- One way is to have a proxy contract that is allowed
 
Sachin Tomar 
If we allow storage in EOA, won’t this result in storage conflict when EOA uses different implementations in different txns?
 
Dan Finlay 
And risks the bundler including the wrong 7702 account, changing the behavior of the op
 
Felix 
This is why I suggested to only allow a specific proxy, because then you'd at least be able to perform explicit transitions between the implementations.
 
Dan Finlay 
Yeah, “just allowing a specific proxy” may not solve storage conflict, but does solve this important issue.

##### **Proxy Pattern**


https://gist.github.com/lightclient/7742e84fde4962f32928c6177eda7523

Matt
- Matt thinks this addresses the issue of Offchain delegation of 7702


elim 
Not necessarily the proxy code, but rather the implementation slot right?
 
Ansgar Dietrichs 
I don’t dislike one proxy contract, but I would be very reluctant to enshrine it in the protocol. better to enforce via wallet whitelisting imo
 
Ansgar Dietrichs 
also means that every tx is more expensive now, as it always has that additional delegatecall hop

Dan Finlay 
I disagree; a user with srps in two wallets could get in hazardous situations easily here

Dan
- there can be conflicting 7702 message floating around
- I think this is about ensuring the user about safety

**SRP means Secret Recovery Phrase**

Ansgar
- open to the idea, but look more into fundamentally change 7702

Matt
- what problem is being addressed?
 - (explained at 40 mins)

Andrew
- extend the account scheme  with verkle?

Gary Schulte 
Agreed re:verkle, but presumably we don’t want to wait for Osaka for AA
 
Julian Rachman 
So would this proxy be a built-in proxy?
 
Julian Rachman 
Built into the protocol

vub 
**A few random ideas:**
1. Let the code of ADDRESS + 1 represent an EOA's "backup code", and have 7702 just temporarily flip on the backup codes of the listed accounts
 
2. Add an EOF version for "this account's 7702-code is at address X"

Ansgar Dietrichs 
can’t do this before eof in pectra is certain


Daniel Lehrner (Besu) 
An enshrined proxy could cause problems with L2 compatibility. Not all L2s are on the same hard fork as main net
 
lightclient 
the proxy would not use new ops

elim 
Why does it need to be a proxy? We just need to record on-chain somehow who the account is delegating to. So this can just be an agreed upon storage slot. 7702 auth'ed implementations can just "promise" to verify this slot.
Can bypass the extra delegatecall



Matt
- Merge the PR without the storage restriction
- and we go from there
- the client team will implement
- the wallet team want less permissive system and we will get to know where we land

Vub - agrees


Andrew
- Noun nonce and zero nonce

#### **Tim: Move forward with the PR to add in Devnet 1**
- will be discussed in ACD meeting 

Ivo @ Ambire 
My 2c is that no storage restriction is amazing. Huge flexibility for wallet teams, no need to enshrine a contract, 

And the storage conflicts are a separate issue that always existed. Yes, 7702 makes it easier for it to accidentally happen but this is up to wallet devs to prevent (make implementations that use unique slots)

Eilas
- Noob question also that i didn’t get an answer for, why is there a keccak in the spec of the new tx type for 7702?
It hinders ZK-EVMs

Vitalik
- it is broader issue
- can be a part of the broader move


Matt agrees with Vitalik.


Ahmad
- the wallet developers gather and agree on max flexibility


Tim
+1 on ERC proxy, if we could have a draft for next week’s call that’d be great