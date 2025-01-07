Future of EOA/AA Breakout Room #6
--

## Info
**Date**: July 31 2024, 14:00-15:00 UTC

**Agenda**: https://github.com/ethereum/pm/issues/1118

**Recording**: https://www.youtube.com/watch?v=Oct83bBp3Z8

**Summary/Next steps**:
- Migration off the table for EIP-7702. Could be proposed as a separate EIP.
- Not enough support for storage change, should be looked as a separate proposal.
- Keep EIP-7702 as slim as possible to include in Pectra, include the [PR](https://github.com/ethereum/EIPs/pull/8775) in latest specs.

**Links**: 
* [Update EIP-7702: Proxy the storage of a delegation to its unique deleterminstic keys](https://github.com/ethereum/EIPs/pull/8762)
* [[EIP-7702] The Rubber Stamp-ening](https://hackmd.io/@otim/BkUQJ5RdA)
* [`CODERESET` for EIP 7702](https://hackmd.io/@S9AwbucvTS6GYodLz-G1SQ/S102UtTwA)


(Notes+zoom chat)

Nicolas: Initiated the call.
- Going to discuss the latest change requests and hopefully by the end of this call we have some decisions for ACD call. 
- Lightclient give us a quick update

Vitalik: In a state with couple of proposed changes
- it keeps increasing based on ongoing discussion. There is a strong desire to get to a point where we decide on Finality on spec.
- About a week ago, Vitalik suggested breakout to discuss different ideas around.
- And discuss the proposal to replace the current design
- Ideas
    - Code reset opcode
    - adjusting the storage opcode
    - and more 
- We can talk about the underline philosophy

Ankit+1
- we wrote the document on code reset
- it is at the last mile and making suggested changes
- A workshop posted by wallet connect folks
- Ephimeral vs non-ephimeral
- Shared the screen to share the [doc](https://hackmd.io/@S9AwbucvTS6GYodLz-G1SQ/S102UtTwA)
- Discussing mitigations doesn't feel very strong at this point
- Focusing on suggested changes make more sense

Ansgar Dietrichs (Jul 31, 2024, 10:05 AM)
to push back on Vitalik a bit, to me it feels like there are simply still remaining open questions, I don’t have high confidence that we are in a good place to pick the final shape of the EIP yet

Ahmad Bitar (Jul 31, 2024, 10:07 AM)
I disagree, I feel like the EIP in its current shape is actually enough and covers most of the concerns.
It does feel that the remaining concerns can be mitigated by certain patterns or actions

Ansgar Dietrichs (Jul 31, 2024, 10:08 AM)
I think I said that on the last call, but CODERESET seems like the wrong direction to me. we decided early on in the process that 7702 was not supposed to ship with permanent upgrade capabilities, and this idea would introduce such permanent upgrades through the backdoor

Ansgar Dietrichs (Jul 31, 2024, 10:09 AM)
although I will admit that the additional capabilities look nice. but it should be its own separate EIP then, not piggybacking off of this one that has a very different focus

Ansgar: 
- looks like interesting feature but I am opposed for it to be in 7702 because the proposed change we considered this initally out of scope.
- it can be good feature to have in the future but no reason to combine this with 7702

Ankit+1: I agree, this is a deviation if the EIP isn't intended to acheive the goal.

Arik:
- the entire idea with 3074 moving on to 7702 is to align a lot of things which were not aligened with EOA, will be addressed.
- As soon as we have those capabilities with 7702, we would be building smarter wallet and contracts to allow the better UX experience be widely adapted.
- want to raise as the question is the ability to build code or save the code for future txs. 


Vitalik: 
- unless in a way Self Destruct already work

Arik (Jul 31, 2024, 10:12 AM)
What if the CODERESET is added alone, just as a way to make a cheap/1-time delegation? Without making the change that disallows EOA transactions?
 
Julian Rachman (Jul 31, 2024, 10:14 AM)
You still have unlocked functionality even if the pk is the master key. I believe safe asked for more concrete reasonings from wallet providers
 
Sachin Tomar (Jul 31, 2024, 10:14 AM)
“the delegation designation can be revoked at anytime signing and sending a EIP-7702 authorization to a new target with the account's current nonce”
Can this new target be ZERO_ADDRESS to remove the code from an EOA?

Elias Tazartes (Jul 31, 2024, 10:16 AM)
we are designing an EIP that is scheduled for inclusion, it feels a bit bad no? how much sunk cost can we bear as a governance body
 
Arik (Jul 31, 2024, 10:17 AM)
Sorry Derek didn’t see you were earlier 🙏
 
Ivo Georgiev | Ambire (Jul 31, 2024, 10:17 AM)
There’s very little use case for one txn delegation, if not none. 

Gas sponsorships are pointless because you need an eoa txn first, same goes for batching

So I can’t imagine any useful one transaction delegation use case


Darek (Wallet Connect)
- I agree with many people including Arik
- I talked to a bunch of wallets, Trust is a special case but other than that adoption of 7702, ephimeral case for 7702 makes it easier migration path to wallet
- In favor of 7702 in its current form

Ahmad
- Designation delegation fixed most of the problems, but received comments that some wallet dont like that. 
- there is always a spec which is going to be the best for most but won't work for some.
- Code reset is not the way to go because it provided the ability inside EVM and not the wallet
- in the last discossion, ansgar mentioned of DOS vector, may want to touch on that.


Arik (Jul 31, 2024, 10:19 AM)
reduced risk = functionality
 
Ansgar Dietrichs (Jul 31, 2024, 10:20 AM)
which exact version does ephemeral storage refer to?
 
vub (Jul 31, 2024, 10:19 AM)
Do we need a new opcode for CODERESET, or is this a small tweak to the functionality of SELFDESTRUCT?
 
Julian Rachman (Jul 31, 2024, 10:20 AM)
a flag be added to the 7702 transaction’s `authorization_list` that would designate it as ephemeral, clearing the code hash at the end of the execution

Nicolas:
- any strong opinion on this?

David(Trust Wallet)
- Code reset will be useful
- batch sponsorship will be done by 7702, but many wallets need to handle key mgmt. 
- beside institutional functionality, we want to unlock some validation related features.


persistnace doesn't has to be in EOA's own storage
 
Ahmad Bitar (Jul 31, 2024, 10:22 AM)
7702 is not supposed to be the EIP to fix it all
 
Sachin Tomar (Jul 31, 2024, 10:14 AM)
“the delegation designation can be revoked at anytime signing and sending a EIP-7702 authorization to a new target with the account's current nonce”
Can this new target be ZERO_ADDRESS to remove the code from an EOA?
 
Ronny Panford (Jul 31, 2024, 10:23 AM)
I guess the concern is not allowing the signing key to ultimately reset the account at any time be it by pointing to ZERO_ADDRESS or null bytes. To help create credible smart accounts. Thats why CODERESET only in the contract code, is what I understand, but this opens new gate ways of concern todetermine malicious use of CODERESET. But I agree crafting this solution might be too late for 7702.

Ankit+1: 
- EOA can move contracts away
- A question is to whom we want to delegate what job
- one concern - why making pvt key available to root user
- we need to educate the user
- Even the wallet don't understand the current spec, it will be difficult to expect from the users. 
- Educating user the users will be useful
- Over 99% tx on mainnet do not have TVL


lightclient (Jul 31, 2024, 10:24 AM)
you were never supposed to get security of smart contract wallets
 
derek (Jul 31, 2024, 10:24 AM)
@Derek could you type out here again why some wallets you talked to felt that 7702 in its current form wouldn’t be widely adopted?  I didn’t completely catch your point
 
Ahmad Bitar (Jul 31, 2024, 10:24 AM)
7702 was not aimed to fix this

Ahmad Bitar (Jul 31, 2024, 10:24 AM)
7702 was not aimed to fix this
 
lightclient (Jul 31, 2024, 10:24 AM)
where have you been the past year?
 
Julian Rachman (Jul 31, 2024, 10:24 AM)
Does that really create a new account though? It is just an eoa with smart functionality
 
Sudeep | Erigon (Jul 31, 2024, 10:24 AM)
I think the feedback from wallet teams was the opposite some time back — an account should be able to act as both EOA and SCA — so that the apps which EOA interact with continue working; and then SCA based functionalities/dapps can be optionally interacted with (and slowly transitioned to).
 
gajinder (Jul 31, 2024, 10:18 AM)
ephemeral storage takes away none of the functionality and reduces complexity
 
Ansgar Dietrichs (Jul 31, 2024, 10:25 AM)
ah. then I would just ban storage within 7702 accounts completely, instead of turning it ephemeral. but we discussed this a few months ago - the feeling was that it would be better to have decisions mirror the 4337 situation

Ansgar Dietrichs (Jul 31, 2024, 10:25 AM)
so rather keep storage enabled, because changing implementations is already a problem that the 4337 ecosystem has to solve. otherwise we end up with 2 separate tech stacks again
 
gajinder (Jul 31, 2024, 10:26 AM)
or this PR: https://github.com/ethereum/EIPs/pull/8762
 
Francisco (Jul 31, 2024, 10:26 AM)
7702 is not migration, education should start by avoiding that term
 
Ivo Georgiev | Ambire (Jul 31, 2024, 10:26 AM)
Also please let’s not forget the signature complications from the concept of converting EOAs to real smart accounts
 
ankitchiplunkar (Jul 31, 2024, 10:27 AM)
https://hackmd.io/-V7ywDDZRDKrXMRRkulOpQ?view

Matt:
- ENS is at risk
- I took a random token and found that at risk
- I think ENS with billion dollars is at risk and I won't do that to put it on risk 

Aniket+1
- there are two tokens are at risk

Jochem (EthJS) (Jul 31, 2024, 10:28 AM)
What is the ENS risk? Someone has a description of this problem?
 
Ahmad Bitar (Jul 31, 2024, 10:29 AM)
the idea is that, if the EOA key is leaked somehow, then the assets are still secure if the migration to sca is final
but looking at ENS token for example, you find this to be un true
 
lightclient (Jul 31, 2024, 10:29 AM)
ENS doesn’t support 1271 so a EOA pk can spend the funds even if EOA is migrated
 
Sudeep | Erigon (Jul 31, 2024, 10:24 AM)
I think the feedback from wallet teams was the opposite some time back — an account should be able to act as both EOA and SCA — so that the apps which EOA interact with continue working; and then SCA based functionalities/dapps can be optionally interacted with (and slowly transitioned to).
 
Ahmed Al-Balaghi (Jul 31, 2024, 10:29 AM)
“wallets don’t like eoa retaining root access” is def over exaggerated < why do you think so?


Aniket+1: 
- shared screen to discuss alternate proposals
- with one proposal if user leak their pvt key 


Matt
- there sare so many thing wrong with this comparision
- when people migrate to smart contract wallet, they expect Smart contract wallet to secure their fund.
- A true smart contract wallet will be in position to secure them
- It will be difficult to educate every retail users about the security consideration.


Julian Rachman (Jul 31, 2024, 10:31 AM)
That is a reallllly binary questioning
 
derek (Jul 31, 2024, 10:31 AM)
I don’t think anyone is disputing that by permanently migrating the EOA, the impact of leaking the key gets lower.  But that’s not considering all the other factors
 
Ansgar Dietrichs (Jul 31, 2024, 10:31 AM)
my personal 7702 wish list:
make it fully ephemeral: store delegation target, but turned off by default. 7702 txs manually enable delegation for a list of addresses
change code read behavior to not return delegation target code
(maybe) add initcode behavior, running at the beginning of a 7702 tx with separate gas limit
 
Derek (Jul 31, 2024, 10:31 AM)
SCA based functionalities/dapps

what exactly is that? `atomic batch transactions` and `dapp sponsored` / `erc20 paid` transactions?
 
Ivo Georgiev | Ambire (Jul 31, 2024, 10:32 AM)
There’s more signature risk than just permits IMHO. Just taking any dapp login as an example that doesn’t support 1271

there are even dapps which support 1271 but verify ecrecover first or as a fallback 🤷‍♂️

Matt
- Let's simplify this for end users.
- the point of 7702 is not to migrate EOA 

Aniket+1: 
- our intent was to add some features to enhance the present proposal

Yoav
- concerned about EOA migration
- I like the change form protocol perspective.
- It has some security considration
- what the change does is alternating the account between EOA or smart wallet. Never both at any point of time.
- we need to decide one of the proposed change and write it to the security consideration

Darek
- two points
    - every one is aligned with the risk of migrating EOA
        - it cant be done perfectly.
        - there is no EOA migration proposal that address all risks
    - people actually want to keep their EOA
        - if people have to try out the features of smart contract, there is alternate ways to try
        - that depends on the smart contract 
- the third point is that we probably we can all agree that the most important thing is to ship this in Pectra
- or a slightly better proposal in the next upgrade. I prefer the Pectra.

Pedro
- Nicely put.
- From my take, the current solution put account in an ambigous state
- we have the ability to revet back to EOA. 

lightclient (Jul 31, 2024, 10:40 AM)
we should move to the next topics, CODERESET isn’t going to be support by 7702 in pectra and there are other things ppl want to discuss
 
Derek (Jul 31, 2024, 10:31 AM)
SCA based functionalities/dapps

what exactly is that? `atomic batch transactions` and `dapp sponsored` / `erc20 paid` transactions?
 
Sudeep | Erigon (Jul 31, 2024, 10:40 AM)
yes
 
greg (Jul 31, 2024, 10:37 AM)
Does the current impl of 7702 have sstore
 
greg (Jul 31, 2024, 10:42 AM)
Unless we want collisions you technically need it

Yoav
- there are user's perspective and protocol perspective

Pedro
- the pvt key should be secondary in this migration

Ahmad Bitar (Jul 31, 2024, 10:43 AM)
it is a "delegation" and not "migration"
 
Agus (Jul 31, 2024, 10:43 AM)
I don't think it's such a UX problem. Smart contract wallets are mostly presented as multisigs, so it can always be displayed as if the wallet has "one more key" that is not revocable
 
Julian Rachman (Jul 31, 2024, 10:43 AM)
The vm and wallet interface lines are blurring......
 
greg (Jul 31, 2024, 10:37 AM)
Does the current impl of 7702 have sstore
 
Ansgar Dietrichs (Jul 31, 2024, 10:43 AM)
the same is true for changing smart account implementations today.

Pedro
- In theory it sounds good, but may not be in practical ways.

Matt
- until we are able to do it in a nice way, we can do it at the protocol level
- there are other problems to be considered, but we need to focus on what it adds

Darekn (Wallet Connect)
- Billion of dollars at risk - I still have to lose my pvt key for those funds to be at risk

Matt
- Risk can not be fixed with 7702
- we are just doing that EOA's can do execution txs. 

pedrogomes (Jul 31, 2024, 10:46 AM)
I would disagree simply because we the current proposal is halfway-migration but we are just renaming it to delegation
 
Ansgar Dietrichs (Jul 31, 2024, 10:46 AM)
I am open to reopening the permanent upgrade conversation - but then we have to be okay with 7702 very possibly missing Pectra
 
Ahmad Bitar (Jul 31, 2024, 10:47 AM)
i am not. if we want to open the permanent upgrade conversation, it can be in a totally different EIP than this one
 
lightclient (Jul 31, 2024, 10:47 AM)
ephemeral setting doesn’t match with 4337


Darek
- one wallet start using and another one doesn't then users may have issues.
- I suggest to keep it simpler for wallets.

Vitalik:
- it feels to me that chances of getting consensus in time for pectra is Zero
- if we do 7702 (as is), it is still compatible for us to do migration latter
- so I think, for questions we get consesnus around but basically ask questions for full account migration (kick the can down solution) is not do that now, and continue to be open as long as some people care about it.
- May in long term people figure out how to do that. 
- Does 7702 as is solve all the problems, if no then see if that can be updated with a new EIP in future?

Matt
- It make sense
- I am not against EOA migration, but against this with 7702

Ahmad Bitar (Jul 31, 2024, 10:51 AM)
always depending on pay masters and bundlers to include my transactions is not something i want to do. I like the ability to use them without being forced to use them
 
derek (Jul 31, 2024, 10:48 AM)
Why don’t we tackle permanent EOA migration in a separate EIP?  As long as we are aligned that 7702 in its current form is a big value add, and is NOT incompatible with future EOA migration proposals, why don’t we move ahead with it for Pectra and tackle EOA migration in a separate proposal?

As Ansgar said before, a permanent migration proposal completely changes the *character* of 7702 and should be considered a separate EIP
 
derek (Jul 31, 2024, 10:51 AM)
The very reason why no EOA migration proposal has gained any traction, while 7702 did, is because 7702 is not attempting to do EOA migration… so trying to add EOA migration back to 7702 seems like a backwards move to me
 
Stephane (Jul 31, 2024, 10:51 AM)
Is that the reason?

Agus
- we rae discussing many dapps and tokens
- dapps may have to consider this fully in order to prevent vulnaribility
- At some point every single wallet will be smart contract wallet.

Aniket+1
- it's a good idea to separate out the migration concerns
- i think things to consider are the side effects
- i know some people will be disappointed that they are waiting on support for the migration

I can only see power users wanting EOAs
 
Ansgar Dietrichs (Jul 31, 2024, 10:53 AM)
side note: I still like the idea of exploring modifying ecrecover to check if there is code in the account associated with the recovered address, and throw if so. not sure if good idea, but worth exploring for full migration
 
Ansgar Dietrichs (Jul 31, 2024, 10:55 AM)
for 3074, we even considered a variant where instead of throwing, ecrecover could call into the smart account to have it check the “signature” instead
 
Ahmad Bitar (Jul 31, 2024, 10:53 AM)
So, we want to force users to migrate to sca by making sure the EOA experience is bad. I hate this argument 👎
 


Greg
- The fundamental thing to remember it took long to discuss 3074
- we're not going to get everything
- get as slim as lean as we can to hold this to make EOA a little ahead of the curve and in the next year see what i sthe best way to move this forward.

Agus (Jul 31, 2024, 10:56 AM)
we wouldn't be forcing users to migrate tho, we would be forcing dapp devs to account for smart contract wallets, the other way around
 
Ahmad Bitar (Jul 31, 2024, 10:57 AM)
They have to, because they will want to support delegated accounts
delegated accounts will have the exact same features that SCAs will have beside security
 
pedrogomes (Jul 31, 2024, 10:58 AM)
Delegated accounts is not a strong enough reason because they can still act as EOAs
 
gajinder (Jul 31, 2024, 10:57 AM)
+1 with greg, we should just push for completion of 7702 rather than radically change it

Eric
- pragmatic usage of 7702 - I'd love to see modification that would make it cheaper


lightclient (Jul 31, 2024, 10:58 AM)
**let’s take migration off the table once and for all**
 
lightclient (Jul 31, 2024, 10:58 AM)
**should be a separate proposal**

Greg
- where 7702 sits is not the dream but at least it gets the job done

Yoav
- in future if we discuss we should have only one thing in
- since we are not using this form of mitigation. It should be mentioned in the Security consideration for the awareness of clients.

Ansgar
open questions from authors pov
1. Exact ephimeral nature of delegation
    - you turn it off default
    - to me it feels safer to keep it off (default)in case of attacks
2. Code accesses
    - to me seems very dangerous
    - never be able to access the code to the delegation target
3. Init code
    - In the past it wasn't considered
    - it seems reasonable to potentially have init code in

frangio (Jul 31, 2024, 11:04 AM)
is limiting to one transaction in mempool a problem eg. for UX?
 
lightclient (Jul 31, 2024, 11:06 AM)
i don’t see why it would since the user would most likely be using a relayer if they’ve upgraded their account
but even if not, if they are self-relaying their account supports batching so no need for multiple txs pending
 
lightclient (Jul 31, 2024, 11:07 AM)
if you run the initcode first, how do you determine how much gas was used to charge that user via a paymaster?


Ahmad
- response to Ansgar's 3 points
- I don't see the first as a concern
- for 2nd - I agree with Ansgar
- for 3rd - I know initializing the smart contract in current form is ugly but having init code may complicate it.

Dror
- Regarding init code - the minimal we should add a very stron security consideration to the EIP. 
- you must have a set of signature or you are vulnerable 
- it is a call data at the begining and not the init code


gajinder (Jul 31, 2024, 11:09 AM)
can we also discuss : https://github.com/ethereum/EIPs/pull/8762 for storage colllision resolution
 
Ansgar Dietrichs (Jul 31, 2024, 11:09 AM)
might be some confusion on what I meant with “ephemeral”.

my question here was basically:
user sets delegation target in tx A.
in tx B, someone calls into their account. does the code run or not? (i.e. does it behave like an EOA or a smart account)

Ahmad Bitar (Jul 31, 2024, 11:10 AM)
smart account
unless A resets the delegation
 
Jochem (EthJS) (Jul 31, 2024, 11:10 AM)
Frontrun could be mitigated by adding ORIGIN to the authority lists: https://github.com/ethereum/EIPs/pull/8763 (but this depends upon the situation)

lightclient (Jul 31, 2024, 11:10 AM)
this isn’t needed, just use a sig from the account
 
Jochem (EthJS) (Jul 31, 2024, 11:11 AM)
So in that case you can ensure that a specific ORIGIN will send your tx and other EOAs cannot "steal" / frontrun your tx by either replacing another code, or setting code before your tx and performing arbitrary code execution (assuming that the delegated contract has no entry guards to check callers)

Ansgar Dietrichs (Jul 31, 2024, 11:12 AM)
the idea would be that all 4337 bundles would be 7702 txs in the future

Jochem (EthJS) (Jul 31, 2024, 11:10 AM)
Frontrun could be mitigated by adding ORIGIN to the authority lists: https://github.com/ethereum/EIPs/pull/8763 (but this depends upon the situation)
 
gajinder (Jul 31, 2024, 11:14 AM)
this is wallet side providing security post delegation, above Jochem's is user side, both are different
 
Ahmad Bitar (Jul 31, 2024, 11:14 AM)
Yeah, i was saying someone can copy the delegation from previous 7702 tx and include in a new one. if the nonce is still valid or the delegation had no nonce, then the problem is not solved. thus, i am not seeing how the ephemeral idea fixes this
 
lightclient (Jul 31, 2024, 11:15 AM)
to be clear it isn’t really initcode?
it’s calldata into the account they’re proposing?

Yoav
- I'd prefer call data
- but init code more consistent

Matt:  what is the flow

Yoav  
- You set the code that allow to work atomatically 

Wallet developers agrees to keep it simple

Dror 
- I understand the complexities to add any such data. 

Matt
- No problem adding security considertaion

Ansgar Dietrichs (Jul 31, 2024, 11:22 AM)
only a wallet could make the mistake of whitelisting a non-7702 contract
 
Ivo Georgiev | Ambire (Jul 31, 2024, 11:22 AM)
We’ve worked around the initialization issue and we don’t use a setup function so that’s what makes things easier for us

I could be misunderstanding this a bit but still two implementations is not a big sacrifice in our case
 
Arik (Jul 31, 2024, 11:22 AM)
It would be useful to be able to use the most proven smart contract wallet in the space…
 
frangio (Jul 31, 2024, 11:22 AM)
regarding gas metering for init calldata why wouldn't the user just specify an exact amount of gas and pay for that
 
Arik (Jul 31, 2024, 11:22 AM)
But feels like we need Safe on the call for this

lightclient (Jul 31, 2024, 11:23 AM)
i think ppl want to discuss storage

Gajinder
- I have put up a [PR](https://github.com/ethereum/EIPs/pull/8762/files) 
- it is also compliant to the verkle implementation
- this will solve the problem of conflict
- I think it is worth to include

Matt
- not with 7702
- it may restrict some of the changes for EOA and smart contract wallet
- this is not a protocol problem but a implementation problem

Ansgar Dietrichs (Jul 31, 2024, 11:24 AM)
I don’t love collision avoidance solutions that are specific to 7702, because the long-term future of smart accounts will not be 7702-based
 
Yoav (Jul 31, 2024, 11:25 AM)
I agree, we should have the same solution for both account types.


Gajinder
- want to hear other opinions

Ahmad
- since we have whitelist of designations
- Ahmad Bitar (Jul 31, 2024, 11:27 AM)
we can have the user clear the storage from the old wallet using the old wallet interface before migrating to the new one if aconflict could arise

Matt:
- **not enough support for storage change, should be looked as a separate proposal**

Vitalik
- the bars for changes in 7702 is difficult to get out from and will be considered as separate EIPs
- it feels like, in general there is no consensus on status quo (have to hear again)
- we are not rubberstamping 7702 as is but pretty close and is progress


Eric
- everybody feels that the next iteration will be in next 2 years
- will be nice to have some space in future forks

We still dont have proper tests. clients forked a lot in devnet-1 because of 7702 transactions
 
Matthew Smith (Jul 31, 2024, 11:28 AM)
matt's proposal is extremely well thought out. just a few minor points to clear up. let's ship it
 
Ansgar Dietrichs (Jul 31, 2024, 11:29 AM)
I still feel very strongly about code reads. I think the current spec is a clear mistake there, and would really like to see changes
 
Ansgar Dietrichs (Jul 31, 2024, 11:30 AM)
all my other proposed changes are more preferences, where I am happy to stick with the current spec instead.
 
Ahmad Bitar (Jul 31, 2024, 11:30 AM)
Agree

Ahmad
- Code read
- in EOF we usually try to avoid any code read, copy exit code, hash exit code, size. Basically it's Code introspection and here it does not make sense to me to allow code introspection into the EOA's delegated account. 
- My preference will be to have these specific code return the normal thing that they'd usually return for an EOA and we can simply add that to the EIP?
- what matt and other client implementers think of this?


Yoav
- one argument against is there are already contract that make it deliberate to not communicate anything related to account abstraction but to only serve EOAs. 

Ahmad
- so we can keep it for non-EOF

Yoav
- yes

Ahmad
- make sense to me

Ansgar Dietrichs (Jul 31, 2024, 11:32 AM)
there are 4 options imo:
behave like an EOA
return the raw code, i.e. the delegation format
behave EOF-like, return “0xEF”
current spec, return delegation target code

andrei (Jul 31, 2024, 11:33 AM)
current spec + allow to delegate to EOF only

Ahmad Bitar (Jul 31, 2024, 11:34 AM)
I actually like that
 
lightclient (Jul 31, 2024, 11:34 AM)
i think we should let pectra get a bit farther down the line, but yeah in a few months would be down to also do this
 
dror (Jul 31, 2024, 11:34 AM)
re: initcode: 
Without initcode, we're not allowed to use existing deployed contract code, and t should be mentioned in the EIP's security consideration

Specifically, we can't use a contract code that relies on storage initialization, since any "setup" function is not protected by the "authorizer" signature (unless it performs "require address(this)==ecrecover(something)"

E.g. In the current design, signing an "authority" to use Safe's masterCopy as your account makes this transaction front-runnable, and someone could frontrun with a different setup and take over the account.

The same goes for any existing contract code, including any ERC4337 modular framework.

Arik (Jul 31, 2024, 11:36 AM)
I do think it’s something that is unfortunate - there is a lot of value with using “lindy” smart contracts…
 
Ansgar Dietrichs (Jul 31, 2024, 11:36 AM)
I think most people already left, we should not discuss this now
(even though I tend to agree with dror on this)

Ansgar
- I wrote the alternative options in chat

Yoav
- do you see anyone using this method?

Ansgar
- it is unpleasent that we have to make these assumptions
- I am talking conseptually it doens't see the right thing to do


Yoav
- we should spend some time looking into it


Dror
- Observation regarding Initialization code - you can only allow monolithinc account that requires set up

Matt
- you can modify
- just set up master controller 

Frangio
- Code will be reenabled 
- a discussion to be had and make a decision

Nico
- keep it as small as possible in pectra
- future improvements in separate EIPs.


