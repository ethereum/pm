Future of EOA/AA Breakout Room #5
--

## Info 
**Date**: June 26 2024, 14:00-15:00 UTC

**Agenda**: https://github.com/ethereum/pm/issues/1081

**Recording**: https://youtu.be/_S01TtA3lao

**Next steps**:
- People are aligned to see [Matt's proposal](https://github.com/ethereum/EIPs/pull/8677) in the next devnet.
- It will be merged in next week or so.
- It is devnet 2 and we will take it from there. will explore more in the next stages.

## Notes

**Nicolas**
To discuss that last update to 7702

Kevin
- The proposal is basically serving the same purpose of revokability in the same way.
- The new ver is also going in the same direction by trying single implementation at a time.
- Our proposal was mimicing what proxies are doing.
- Except migration being more difficult, I don't see the new proposal to be any different. 
- I think we're going into more permanent.

Julian Rachman 
- I am against the permanent approach. I think we talked about this throughout the weeks

Matt/Sam/Ansgar
Ansgar
- couldn't look into proposed change
- conceptually it is somewhat cleaner, and in principle I like it. 
- two different option to activate the delegration target
    
    - add another field to 7702. give a list without authentication. It will make the tx make it active when needed, not permanenetly. 

Sam 
- If we're doing a permanent delegation, why not just make a tx type that deploys code into the EOA

Richard Meissner 
- So the question is if the permanent approach is an acceptable path to approach the revocation topic.
- So far it feels that while now Nethermind is fine with the proposal, other teams that did not have too much of an issue with the revocation, would rather stick to the non-permanent proposal.
 
Julian Rachman 
- So why dont we just push the current 7702 language then?
 
kevin 
- That’s also part of the proposal Ledger made, having an access_list like option a transaction to activate or not the behavior

Richard
- That would still mean only one delegation target at once, right @Ansgar Dietrichs 

@Arik you advocated to allow multiple delegation targets, right?

Richard Meissner 
basically on chain it is said which delegation target can be used, but it will only be used if you specify it in the transaction.

Ansgar 
- Basically the original version of 7702 will be used, but limited to the address (singular) that is set onchain in the account.

kvn 
- Not that we don’t like the permanent approach, it’s just like it feels like it was the kind of things that people tried to avoid during the discussion for EIP-3074 -> EIP-7702


Matt
- In case of Revokation 
    - you have given permanent delegation
- the nice thing about 7702 is that autherization is only valide one time while setting the account.
    - the a/c is delegated to smartcontract wallet
- now that we can write into the account feels like the best thing to happen.
- Let people slowely migrate to smart contract wallet.


Arik 
I think you can just add a small flag to decide if the delegation is single transaction or permanent and it should solve everyone’s issue…
 
Richard Meissner 
should the single tx authorization be reusable?
 
Arik 
No, if you used it and you want to authorize again you would need to do it on a new nonce… cause it increased
 
Ansgar Dietrichs 
yes, I think in every variant of this, I would appreciate a one-time use flag, basically “don’t store this as delegation target at all, just use it for this tx”

Arik 
- Ansgar, I am not sure I understood the mechanism fully - can you write it down?
 
Ansgar Dietrichs 
- right, Richard summarized it well. With the additional asterisk that now by default “turning on” 7702 delegation for an already set target would no longer require any sort of signature by that account at all

yoav 
- Seems like the right trade off to make
 
Hoshiyari
- Using this a malicious EOA would act as a genuine contract for eg; a vault until have enough funds to run away.

I was wondering how the new version can mitigate this actor vector…

Sudeep | Erigon 
- I don’t know if temporary delegation adds anything. Permanent delegation simplifies what 7702 does — which is to set a delegation designation.
Also in temporary delegation wouldn’t you need to have a new authorization (since it’s nonce based) the second time you make a 7702 tx?
 
Richard Meissner 
- yes, that is basically what arik is asking for. It is basically to bring in features like batching
 
Ansgar Dietrichs
- by temporary delegation, do you mean my alternative idea or the proposed one-time use flag Arik just mentioned?
 
Richard Meissner 
- there no long running authorization is required, it is ok to do a per transaction authorization to batch and sponsor


Sam 
- Can you self-destruct in the delegate call target?

Matt thinks
#### Temprorary delegate allocation does not bring us closer tothe smart contract wallet

Arik thinks other wise
- just having the ability to delegate may increase adoption


Sudeep | Erigon 
- I don’t know if temporary delegation adds anything. Permanent delegation simplifies what 7702 does — which is to set a delegation designation.
Also in temporary delegation wouldn’t you need to have a new authorization (since it’s nonce based) the second time you make a 7702 tx?
 
Ansgar Dietrichs 
- right. so in that variant, once the delegation target is set, “turning it on” within a second (or third, or fourth, …) 7702 tx would not require a signature at all. 7702 basically would have 2 lists: one to change 7702 delegation targets, that comes with nonce and sig. and then one for accounts that should have their delegation enabled, without any sigs
 
Arik 
- I think you can just add a small flag to decide if the delegation is single transaction or permanent and it should solve everyone’s issue…
 
Ansgar Dietrichs 
- so one problem with this is frontrunning the one-time use tx (e.g. for griefing the user), if you send it via a public mempool. because the sig doesn’t commit to being used within a specific tx


- temporary delegation
- longterm deleg
- permanent deleg


Ansgar 
- The problem we are trying to solve is Frontrunning.
- I am wondering any good ways to mitigate this as it is not with the protocol.
- Matt proposal may have more context and I think could work. Unsure of any other ways to mitigate it. 


Matt
- using in temp deleg or perm delegation
- if there is a piece of code which has risk then there is no point of having of temporary delegation


Richard Meissner (safe)
- what is the most realistic version to push into the h/f
- what is the complexity as we want to ship with devnet 2
- for me this is the pressing matter that if it is enough to implement 
- there are way more qns around revokability at this time
- consideration of security and revokability are good way to go for us 
- agree to what ansgar says about timeline



Julian Rachman 
- I guess we are using very loose terms here with “permanent”, “temporary”, etc.

Maybe current “permanent” is better said as “persistent” delegation and “temporary” is better said as “expiring” delegation
 
Ansgar Dietrichs 
- I would say “one-time” for those that cannot be used more than once.
And then “optional” for those that are stored, but only active in the initial tx and in future txs that explicitly activate it again
 
Julian Rachman 
- Sure!! Honestly anything away from using “permanent” and “temporary” would be right

lightclient 
- ultimately you can also implement the one-time use with the current proposal
 
lightclient 
- so there is no need to over complicate 7702
 
Ansgar Dietrichs 
- on a more general note, I will say that it really worries me how much the 7702 spec is still in the air, with regard to Pectra timing.

**For context though**, Pectra size is very very large, so full rollout of the fork will probably take quite some time still. Imo the worst timing risk here is that Pectra ends up split into two parts, and that 7702 won’t be ready for the first part, so will end up having to wait an additional 4 months or so.

Ahmad
- suggestion - to preserve old 7702 behaviour, we can add a boolean flag
- the nice thing about this is that once it absorbs the nonce, we gain the implemenattion simplicity from the core dev perspective


Richard Meissner 
@Ahmad Mazen Bitar how do we handle the DoS vector that @Ansgar Dietrichs outlined for this approach?
 
Richard Meissner 
- in the sense that the authorization can be invalidated by malicious parties 

Ahmad
- this approch of adding flagg may satisfy all three concerns with a better implemenation of EIP

Arik 
- Can someone explain why the persistence version is not attackable by this DOS vector?

Ansgar 
- the prob I see is that if you send one time use tx, and is picked up by a bundler of anyone, the tx doesn't make use 


Richard Meissner 
- because if you frontrun the authorization it is available onchain
and therefore it will still be valid in the tx that was frontrun
 
Ivo Georgiev | Ambire 
- Unless im missing something, temporary authorizations would be quite limited in terms of UX

You send one txn to set a delegation, so that you can then benefit from SCA features for one transaction

Sounds like something that will never be used in the wild
 
Richard Meissner 
- for batching and sponsoring this should be sufficient, right?

Ahmad
- it will just validate the tx.

Ansgar
- it will not activate and will not make use of the one time. 

Ahmad
- got it, will think about it. 

Antony Denyer 
- You can basically “unbundle” it?
 
kvn 
- Also, the more options we have, the more complicated the Wallet UX will be… Explaining this AA behavior in ten different ways for X different AA "brands", and making sign  (very powerful) authorizations 10 times, is definitely something that feels very niche to me

Ansgar
- Pectra is very unprecedented 
- 7702 spec should be final very soon otherwise, it will not make it.
- what could happen, that the EIP is split up in two
- if that were to happen, we really need to decide.
- I think we need to make decoision 
    - what recommendation to ACD on what to ship in the next h/f
    - can we ship matt's change. - yes or no
    - I persopnally want to make delegation transparent
    - we should focus on the spec that we want people to use on the upcoming devnet


Ahmad
- EOF tries to look into code & gas introspection
    - I'd try to avoid intrspection of code and account
- If we have the knowledge of one time designation will be consumed by the sender account, then we can authorize 
- unsure if it will work with paymaster
- also if this is a requirement to allow authorization. 

yoav 
- It’s roughly equivalent to SSTORE so we could use the same pricing model (which will change with verkle)
 
Ansgar Dietrichs 
- on a more general note, I will say that it really worries me how much the 7702 spec is still in the air, with regard to Pectra timing.

For context though, Pectra size is very very large, so full rollout of the fork will probably take quite some time still. Imo the worst timing risk here is that Pectra ends up split into two parts, and that 7702 won’t be ready for the first part, so will end up having to wait an additional 4 months or so.
 
Julian Rachman 
- Do you refer to the pre-matt proposal version?

i wish we could have pre-matt’s proposal version but have come around to be ok with matt’s proposal
 
Ivo Georgiev | Ambire 
- Unless im missing something, temporary authorizations would be quite limited in terms of UX

You send one txn to set a delegation, so that you can then benefit from SCA features for one transaction

Sounds like something that will never be used in the wild
 
Ivo Georgiev | Ambire 
- Yes but you send one txn which isn’t sponsored or batched to get 
one that is? Sounds convoluted since many batches will be no more than 2 calls in the first place
The sponsoring is even more convoluted
I’m talking about temporary one time delegations ofc
 
Richard Meissner 
- would this then be like a new param in this EIP, the expected tx.origin?
 
Arik 
- Is it possible to make the “griefing” use case too expensive to be efficient?
 
Ansgar Dietrichs 
- I don’t think restricting to a specific 7702 tx sender would be the right approach, that way it would be incompatible with 4337
 
Ansgar Dietrichs 
- at least with the public 4337 mempool
 
Richard Meissner 
- could be optional xD (this is more a joke)

Matt
- The hard thing is we have too many people with different requirements'

Richard Meissner 
- Do we have a summary on what we align on so far? Or at least 2 options that we have to decide between?

Yoav
- not in favor of temp delegation, if we still want to mitigate the issue raised by Ansgar, it will become possible for 4337 to better use. 

Ansgar
- how will you handle different cases, seems difficult

Yoav
- agreed
- maybe we don't need a temporary delegation.

Sam 
- Unless you're running initcode, you don't get to revert before your code is deployed
 
Richard Meissner 
- Just to understand the emulation: it would still have a delegation set and therefore behave different to an EOA when being called (or being the target of the EXT* methods), right? 
 
kvn 
- I don’t think we answered what would be the behavior of delegated accounts without the authorization in the transaction (having another list like access_list basically was mentioned ?) and in the context of transaction type < 3 ?
 
Sam 
- Wouldn't it be a self-destruct?

Yoav
- if used during a tx, and says now it is becoming validated, it could work.
- It is hard to think of all the scenarios.

Matt
- we can’t use the storage
- the protocol should not touch the user space storage

Kevin
- we kind of changed the opinion on that, but I understand.


Ahmad Mazen Bitar 
- I dont think client teams will go to change this on devnet1. We already finalized devnet 1 spec

lightclient 
- agreed, this would really be for devnet 2

Ansgar Dietrichs 
- what is devnet 2 timing? would we have to decide on the spec to use by next acde?

Nicolas
- let's go for last round of for and against
- dev and researcher thinks this is 

Richard M
- might be helpful to go one more time
- we don't allow temp delegation
- will be dependent on nonce 


Ansgar
- we seem to mostly align with Matt's proposal as the next step
- we can explore my proposal as conceptually the extension of Matt's idea
- my qn- do we have people on the call who strongly oppose matt's or my proposal as matt's extension?

Ivo
- I am **opposing temporary delegation**
- there are various AA cases where it works better
- eg. for batching


Sam 
- If the delegation target is stored in code and you can change your delegation target, then you can mutate your account's code.

Julian Rachman 
- I mean it would be wrong to not say that I do like the flexibility of pre-matt 7702.

BUT I bias towards matt 7702 because we would be WAY worse off having this fall out in the worst case (knock on wood). The ethos for what 7702 is trying to do is still there and we want the ethos to be something we push into Pectra.
 
Richard Meissner 
- I also find the idea of Sam interesting to utilize self destruct to reset delegation. 

Ansgar
- with original 7702, it was also the sace
- my extension of this was conceptually more permanent and advantageous

Richard
- with intrspection, I agree the changes of behaviour. With Proxys we already have a way to look into.
- I like the one time allowing because if it is revert, you have to create a new authorization to reactivate again
- Selfdestruct by itself will be interesting, but unsure if it is going against the isead of deprecating self destruct.

Arik
- I disagree with the statement regarding the batching use case - but it’s probably not worth the discussion here. 2 signatures that run an atomic 2-action code is not the same as 2 signatures that run two separate pieces of code.

But again - this is not the main point in this discussion

Sam
- are we not planning to remove the self destruct even in the same tx 

Ansgar
- as per Vitalik's proposal - yes

### Next steps
Nicolas
- People are aligned to see Matt's proposal in the next devnet
- it is devnet and we will take it from there. 
- will explore more in the next stages.

Matt
- thanks for the feedback
- will try to merge early next week
- if any different idea is emerged may merge by the next ACD 



