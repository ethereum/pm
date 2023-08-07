# Execution Layer Meeting 167 
### Meeting Date/Time: Aug 3, 2023, 14:00-15:30 UTC
### Meeting Duration: 1:32:44
### [GitHub Agenda](https://github.com/ethereum/pm/issues/836)
### [Video](https://www.youtube.com/watch?v=X46mbG8N5XM) 
### Moderator: Tim Bieko 
### Notes: Metago 


# AGENDA

# Dencun Updates

## [Update EIP-4788: set nonce of beacon root history address to nonzero EIPs#7431]( https://github.com/ethereum/EIPs/pull/7431) 

## [@holiman EthMag 4788 comment]( https://ethereum-magicians.org/t/eip-4788-beacon-root-in-evm/8281/35) 

## [Update EIP-4788: Mention genesis block with no existing beacon block root case EIPs#7445](https://github.com/ethereum/EIPs/pull/7445) 

**Tim**
Okay, hello everyone welcome to ACDE167. So a couple of Devcun spec updates / clarifications today. Then there are some questions around some engine API prs for the devnet8 and then we had two people with new EIPs they wanted to present and to wrap up, Guillaume and Josh have a big Verkle update to share, sort of what they've been doing over the past couple months. But yeah I guess to start, there were three pr /comments for 4788, and I guess yeah Martin you put up the first, so do you want to give some context on that? 
This is PR 7431. I think as I wanted on the call.

**Martin**
Hello can you hear me?

**Tim**
Yes yes we can.

**Martin**
Right so about 4788, first of all I made a suggestion, let me see if I have that PM somewhere here, just so I remember what it was about. 

**Tim**
It's so the first one was like the history storage address right it has Mount zero so 

**Martin**
First of all we discovered this problem that due to the definition of empty, the bigger root stateful pre-compiled storage was wiped at the end of every block because emptiness does not require an empty storage route, the definition of emptiness does not care about what the source looks like, so that's kind of wonky and I proposed one fix for that which would be to set the nonce. 

If the nonce when we set storage check the nonce. If the nonce is zero then set it to one. That's kind of a neat way to solve it. Yeah then why we were kind of investigating that, some other people got their eyes on 4788 and there was the question raised that we should turn it into not being a pre-compiler at all. Is that something we want to discuss now or is it something we should postpone to a later point?

**Danny**
I think the question about the first the conditional…

**Tim**
Yeah let's do the first yeah and then we can discuss the precompile. 

**Danny**
Yeah is there should this actually be conditional and if so should there be tests where it's already non-zero before the fourth like it's nine?

**Martin**
And so though it, on mainnet we will only ever have it be zero once, and then it will forever always after be one. Testnets that people might spin up they can set it to whatever they want. I mean it wouldn't be, it's a very simple thing to get right. Yeah I just learned about it and if we get it wrong it might screw someone up on some very strange private network. 

**Danny**
Okay but there should be probably a test case where it's non-zero and stays non-zero. 
 
**Martin**
Yes yes sure.

**Tim**
Okay, I do think yeah so the question of do we want to even make this a bigger ? is something we should discuss now because if we want to make this decision it feels already pretty late to make like a significant change so yeah Martin do you want to share 

**Martin**
Yeah give it give a little heads up for them, perhaps, publish on the caller someone else who can give it their thoughts about why they don't want set for picking parts but first of all then I think the question was raised long time ago by ? At that point in time the EIP looked very different and then the EIP evolved and now we're at the point where the whole of the pre-compile could just be replaced with a regular contract and the only magic that will be needed from the like client consensus point of view would be that we that the system makes a call to it that start the block processing. The EIP already today contains pseudo code that says what this pre-compile is supposed to do and now all of us client implementers have taken it and implemented that in our respective languages.

Did it go and other people will implement it in other languages. I noticed yesterday when I was comparing them that our implementation was not according to spec. That would have been a consensus issue and we need to write tests about that yada yada. If we instead of taking the pseudo code and put it into solidity, it wouldn't have mattered if for consensus from a consensus point of view, it wouldn't have mattered if there was one such type of error because from the client developer's point of view it would all have been an opaque black box. We would just call it once on the block processing but it fixed amount of gas hope that it does its thing correctly and for consumers point of view that people who write contracts that actually want to use this beacon route, it does not matter much at all for them whether it's a pre-compile or whether it's regular contract. 

The tangible difference I guess is that if it's a pre-compile, we can decide arbitrarily that hey the gas should be 4200 or whatever. If it's a contract it's going to be a you know a little bit of change, it's going to be a few more opcodes for the logic and it depends on a bit on you know how we how they so it's going to be a bit less round number, but otherwise no difference. I think that going with the regular contract increases the security. I mean it decreases the complexity of implementation. So it lessens the risk of a consensus split and in a separate way I think decoupling pre-compiles from and not having stateful pre-compiles makes easier for plug-in architectures such as Aragon and even one but I'm sure someone else can talk about that more than I can so that's it for me. 

**Tim**
Got it thanks. Lucas you have your hand up?

**Lucas**
So if I understood correctly that would be at the end of the block. We will call this kind of special transaction that would update the contract?

**Martin**
As the best currently is specified to do it in the beginning of his book okay from the beginning of his book we would call this special transaction that would update the contract.
**Martin**
Yes.

**Danny**
So it's more of a special call rather than actual physical transaction in the block route?

**Martin**
Yes I mean it's semantically it's a transaction.

**Lucas**
Yeah it's a transaction so yeah

**Martin**
But it doesn't it doesn't admit any receipt yeah and things like that so it's just 

**Lucas**
Okay give me a second 

**Martin**
Wait but that's already I just wanted to mention that's already part of the currently regardless of you know it becomes a free compiler because not 

**Lucas**
And what about gas metering of this transaction? Its I guess

**Martin**
So I suggested when I just suggested like we could then change the that which would just set the gas to like 100,000. Its not going to be near that because it's going to do proof to store it is

**Lucas**
But this gas wouldn't be counted for blockers in any way?

**Martin**
No.

**Lucas**
Okay.

**Martin**
And that's the same I mean there's no difference between the current where the eth works and the and then what I propose because this system call goes outside of a gas.

**Lucas**
Okay so just FYI this sounds very familiar to what Aura consensus introduced as system transactions, this is basically the same thing.

**Martin**
Yeah.

**Lucas**
It's implemented currently in Nethermind, Aragon and I know that Guillaume is working on gas implementation of this thing to work similar to support this, makes sense, we will be we have been using that for years now so it's so it makes sense from the coupling perspective. I totally agree it has its own drawbacks because now there's something like shadowy going on that updates the state but it's not visible but it's similar as it would be implemented in the code so generally I don't disagree makes some sense just a bit funny that we are porting this potentially to the original Ethereum

**Martin**
I think from myself actually it's not that funny I mean of course but I think the original source for this is EIP 210 which Vitalik proposed back in 2017 or 18. 

**Lucas**
This exact mechanics for block hashes so is it before my time yeah makes sense and it's fairly easy to implement from our site so and some clients have already similar mechanisms so it's doable fairly easy.

**Tim**
Pawel, you have your hand up?

**Pawel**
Yes can you hear me?

**Tim**
Yes.

**Pawel**
Okay so like one comment, like what was said about the like technicalities how the system covers I think there's also like special address where the call comes from so that's the way it will to identify that the system is calling contract from inside the contract. I'm sure this our I think is similar but yeah it's interesting that it's kind of converged the similar design. So like comment from my side as a kind of EVM maintainer, it's also like simplifies stuff on the testing and implementation because otherwise you need some special data structure like somehow to transfer this data, what the pre-compile would have to answer to users so we need to have this data somewhere and either you need to get it from some API or whatever right? 

And the same for testing if you consider like we have a JSON structured tests, you need to extend this JSON format to also somehow encode this data the pre-compile might be asked for. If all goes to state and yeah if all of that goes to state by a regular call then there's not really need to do anything and yeah the second comment, I will just repeat is that we kind of translated the pseudocode from the spec into EVM bytecode, so I think that's much easier to consume by the implementers as well. 

**Tim**
When you say the pseudocode from the spec you mean the current spec?

**Pawel**
Yeah I mean like that would be kind of replaced with the like EVM something, I mean probably we need to use high level but in the end the bytecode only matters that has to be deployed, and I think it will be even less complex than the current pseudo code because pseudo for example has to handle like ndms and conversion between different like types and whatever and when you specified with the EVM inputs and EVM op codes it's already kind of…

**Tim**
Sorry what did you say Martin? 

**Martin**
Yeah well all the so the pseudocode a lot of view into bigger and then conversion but when I moved it over to solidity all of that just fell away it was no need to worry about it, it was a bit fun so yeah they like and the code it turned out in my eyes simpler than the pseudo code.

**Tim**
Got it. Danny?

**Danny**
Yeah I think this is a very fine direction. I just want to understand at this point the process what the security and kind of overhead of the process would be right, like do if this were written today we have bytecode, how do we get comfortable with the bytecode?  We need to have a test suite which runs independent of say The Hive Etc and we probably want a handful of probably EVM experts to be doing review. You know when we did something like this for the deposit contract we also formally verified the thing granted the deposit  contract handles capital, whereas this would not, so I don't know if that's requisite but you know the just the process of doing this is not the process of doing Hive and tests and things, so like we have to like define what the process is and how long it's going to take and what the overhead. 

**Alex**
One thing on that is if we deploy it and it breaks we'd have to wait till the next hard fork to redeploy something so it's not like there's zero cost. 

**Danny**
Yeah so I mean since it's like instead of a consensus split you get a broken up code.

**Alex**
Sure yeah.

**Martin**
You don't actually get a broken up code because there's no old code for…

**Danny**
Sorry you get a broken system facility that people use 

**Alex**
Like the feature breaks yeah, like people want the feature and so if we deploy something in the ? then it was a feature.

**Martin**
Yes. 

**Danny**
And that's the difference between you you're taking either consensus split or you're taking a potential broken thing. 

**Martin**
Yeah and me as a clientele I know what I pick but sure I understand your concern. 

**Danny**
Arguably it should be easier to get it right once.

**Martin**
Yeah on or this is also a very actual simple contract it does not have a lot of state, it does not have a lot of paths and as you point out it does not handle a huge amounts of money the way the deposit contract does. Yeah I don't know where to how we should but we should yeah what process we need to follow for this. I'm open to suggestions.

**Tim**
I guess Alex I know you've talked to a lot of the potential users of this do you think from their perspective it matters?

**Alex**
No. I mean I think some of them have started working against the current EIP but this is a pretty small change and like to be clear I think this makes a lot of sense so. Right well like the address would change but yeah otherwise it's pretty much the same, yeah and then my bigger thing with this is just, like you know if we want to keep this in Deneb then we need to figure out the testing security or less informal verification story ASAP. 

**Danny**
I guess fortunately we could get a bytecode that works into testnets very quickly but at the simultaneously we need to be doing kind of a rigorous testing and analysis and review of that bytecode so we're not blocked on like switching to this very quickly but we simultaneously need to be doing a verification of it.

**Martin**
Yeah and then so I mentioned this but I don't think I mention it here today but what we could do then is we could deploy it, could create two we could deploy it across all networks with the deploy it on mainnets long before Dencun and anyone who wants to can audit it and test it and check it on mainnet and then what happens in Cancun is just that we start to we bless it we start invoking it by the system.

**Lucas**
One more comment on system transactions from me that I remember when implementing them there all the gas related things like there are some gas checks, like subscribing the value for the gas, for example or refunding it was a a bit problematic to implement it correctly that it wasn't that easy it's easy to make a consensus error implementing that.

**Danny**
And something real quick on what you said Martin. I had assumed incorrectly that you just intended at the fork for a bytecode that exists kind of written into the EIP to be deployed at a certain address. You're saying instead to just manually deploy?

**Martin**
Yes and I'm saying that what happens in Cancun, the fork is just that we start invoking an address and I hope that everything is in place and I mean we don't really care if there's anything there listening but we're doing both here.

**Danny**
Why not have the fork deploy the bytecode and not have a manual dependency? I mean I guess obviously additional complexity but then you know that it's like self-contained and it works independent of human activity. 

**Martin**
I just think it would be nice to remove it from the EIP and not have it be part of the consensus 

**Danny**
Right. I guess the EIP just has a dependency on a ? 

**Martin**
Yes. 

**Danny**
Before X human must deploy with energy 

**Martin**
If you're on a network and no one has deployed it then you won't have the feature. If you decide to deploy it, it will start functioning because the system will you know the next if you do deploy it on the system then the system calls will start functioning.

**Danny**
Yeah I understand that I but some of the like you know what happens to the failed system call that isn't doing the right you know right so I might put someone must deploy before and then sidestep those questions.

**Tim**
Ignacio?

**Ignacio**
Yeah I was just wondering because the only thing that would require me in general I think it's a good idea the only thing would run me a little bit is kind of potential Cancun delay so just be curious in my mind it's mostly the system transaction not so much that the contract code itself because we could basically have audits and everything running in parallel as long as they finish by the time of that folk they're basically good and but with the system call obviously another method something implemented that could probably be adapted more or less as is but it just maybe would be nice to get some sort of feeling for how confident the other clients would be that this would not add significant timeline delays in terms of testing or bad and everything, we just said that's like the one big unknown for me.

**Tim**
Yeah I agree. Is there yeah do the client teams want to share maybe like how they think this would affect their Cancun development?

**Martin**
 I talked a lot would someone else wanna go?

**Tim**
Well I guess just to confirm, do you feel like this would meaningfully change the developments timelines for Cancun?

**Martin**
Yes I do. Okay it will yeah it will remove some complexity to remove one of the pre compiles, yeah I don't think it's going to be a problem time wise to improve this.

**Tim**
Got it. Yeah.

**Martin**
…from Besu…

** **
I think when we talked about this earlier we um we talked about this ahead of some of the certainly the head of the contract option so it's not something we really have any consensus on right now. Personally I think that sticking with the pre-compile option is going to be better self-contained and easier to reason about in terms of delivery but it's not a strongly held opinion. 

**Tim**
Nethermind?

**Lucas**
So for us we can definitely deliver it. There are some quotes around cost economics for this call and like EIP 158 for the system address, things like that that's other guys would have to accommodate too. I think Aragon also implemented that already so they should be fine.

**Andrew**
Yes we have an implementation for system transactions or a system transactions used for analysis chain so we can implement this one, especially I think the bulk of the work will be in formalizing system transactions and ideally we should get it this like there should be no discrepancy between Ethereum mainnet and gnosis channel like horror stuff that would be perfect.

**Tim**
Okay and so it seems like Danny and Alex would rather have the deploy of the contract part of the EIP, they sort of keep it all self-contained, so part of the hard fork activation. If we went that route, does that significantly like make things more complex because then the hard forks logic needs to include the contract deployment?

**Danny**

I also just worried in testing like in Hive and in testnets and stuff it…

**Tim**
Right 

**Danny**
So we yeah for example even if we're doing like Deneb and post Dencun testnets in the future like now we have to figure out is that bytecode deployed at Genesis who's deploying like it just it seems to bring like a whole thing to have to think about in any testnet in the future 

**Martin**
So there's still it adds one quote though and it's the same quirk as with this nonce thing and that's why I maneuvered around that by doing it the check every time however so if we do the quote is if we configure that Cancun happens at zero, block zero,  and there is nothing there into Genesis then we create block one, so it's just, do we then deploy the thing before processing, yeah it becomes a bit of we need to do it correctly when we do the deploy it's block zero.

**Danny**
Right but if it's if it's part of the EIP investigation it can be you know at fork block which is block zero at, before you're doing anything you essentially deploy by code and then it's self-contained and we never have to think about it you know, once you get the logic right once.

**Martin**
Yeah and what if there's code there?

**Danny**
Well you put it at an address that is essentially reserved like a pre-compile, but it doesn't have to be a pre-compile, it could be any address.

**Paritosh**
Will we be able to use the same logic by using for the deposit contract on testnets? We currently just hard code what the storage code needs to be at an address we decide and this is in the Genesis JSON.

**Danny**
Yeah so you would have if we do the manual kind of thing then it looks it's going to look like the deposit contract and it's just going to be something that needs to be baked into tools rather than something that's baked into consensus logic.

**Paritosh**
Got it at least from a testing perspective this is super easy because we've basically set it up says that everything inherits Genesis from this one tool. I know Hive is different and antithesis is different, but yeah I'd let Mario speak for Hive of course, but for testnets it should be a super easy change.

**Mario**
Yeah I guess if they decline, somehow makes it so that the code appears automatically at the allocation before starting tests that would be very helpful for testing because otherwise we have to hardcode it into every single test somehow before starting, and I mean for this, the main issue would be the Ethereum tests and type of testing where we do some pre-allocation, so we have to be yeah, pretty hardcode the code before each test, but if the client itself does it at the hard fork, and the code appears where it has to be, that will be very helpful indeed for testing.

**Danny**
Also and yeah also Apollo's point that kind of if we deploy to the same address everywhere it has a certain implication on tooling if it's deployed ad hoc depending on network then it has a different application on tooling, like you kind of have to like the tools that want to use this the libraries that want to use this have to be configured per network whereas the other they're just kind of configured singularly. 

**Martin**
Yeah I can go with either I don't really have strong opinions about this.

**Tim**
So I guess there's anyone still feel strongly in favor of the pre-compile it seems like we've like slowly shifted to how we do the normal contract rather than like defending the pre-compile but is there anyone that thinks that we should stick with the pre compile?

I know Besu mentioned they have like a weak preference but aside from Besu?

**Lightclient**
Did we agree on how to trigger the contract?

**Danny**
From the system standpoint?

**Lightclient**
Yeah like does this account against block gas does this is this a transaction does it come from something instead of a Terran transaction hash?

**Martin**
It comes from a special system matters it does not count towards the block gas and it there it does not emit any receipt. I think that's 

**Lightclient**
Okay and so is that is that call have it that function have a conditional like assert must be from system address and then otherwise it fails or is it

**Martin**
So in the implementation that I wrote yes and there I wrote two well in digital system Addison ?path and one which actually uses poor bytes it's easier nicer for addressing, you know better ux, We’ll decide I guess in the coming days and what which one we prefer. Okay thanks for posting it just yeah.

**Tim**
So yeah in terms of getting to like a final decision on this, it seems like there's it's probably worth like discussing offline a bit to like work through the details of the spec, but at the same time it'd be nice to not cause huge delays over this, like do we think it's realistic to get to the call, the CL call I guess do you think it's realistic to either have a decision, and people agree like by Monday on the testing call or the CL call next week I think if we need longer than like a week to agree on this, it's probably a sign that it's yeah it's too long.

Okay Alex says decide by Monday. Does anyone think that's unrealistic that by Monday we can't have a okay and so oh yeah please. 

**Danny**
I was gonna say if we wanted to move on a definite without 4788 which is not the current discussion, we need to think about how that impacts the consensus layer or tests and release and stuff so I prefer to try to just get it sorted.

**Tim**
Okay and so the things we need to figure out by Monday are one do we put this as part of the hard fork flow or do we have a manual deploy and two what contract we want at the very least to start with, this is a bit more of a reversible decision but it would be good to align on, yeah the deployment flow and the deployment flow, our preferred contract and I guess to also have at least the pr to the EIP with the proposed changes? 

**Danny**
Yep yeah 

**Tim**
Okay and is there a channel that should we just use like allcore devs or interop to discuss this just so everyone sort of goes to the same spot I don't think we had the channel quite for this EIP

**Alex**
We've been talking in testing in EVM testing let's see sorry execution layer testing.

**Tim**
Okay so that's yeah let's keep using that then so the testing channel yeah we have many testing channels but okay so under the execution layer category, the testing channel okay yeah.

**Alex**
So maybe we can summarize a bit. 

**Tim**
Yeah. 

**Alex**
So we're gonna need the nonce thing no matter what right? So we can go ahead and merge that EIP?

**Tim**
So this is Martin Source pr right it's the one that?

**Alex**
Oh sorry.

**Martin**
Exactly it becomes moot.

**Alex**
Well you could still deploy this in some way could like delete it right?

**Martin**
Right but then as if there's non-enthy code it's not considered empty right yeah

**Paritosh**
For devnet 8, do we want to start with devnet 8 with the current version, with the pre-compile or do we want to wait until the new csis address is called beanie.

**Alex**
Yeah I think we would try to wait.

**Paritosh**
Okay.

**Alex**
So yeah I mean unless someone else wants to I can make it pass and update in the EIP like today and or tomorrow so I think by Monday it'll like at least look clear what to do and then separately there's you know the testing log in front but I think we can have the actual functionality pretty quickly but I just want to understand what we're all agreeing to so if we're sure about the code thing then we don't need 7431 and then yeah I can update the EIP with this my good approach.

**Martin**
Sounds good I can work with you on that.

**Alex**
Very great and one other thing there was another PR through this EIP to handle the Genesis case which I think most people saw but I just wanted to call it out oh yeah. Yeah the one that Tim put in chat yeah and then otherwise I think that's it unfortunately okay.

**Tim**
And then yeah it so for devnet 8 it seems like we also agreed to wait until these changes are done to deploy the devnet rather than deploy with the current version and like change it. Does that make sense to everyone? Okay. Okay anything else on 4788? 

## [Update EIP-6780: Add clarifications to EIP-6780 EIPs#7308]( https://github.com/ethereum/EIPs/pull/7308) [43:08]( https://www.youtube.com/live/X46mbG8N5XM?feature=share&t=2586) 

Okay next up, so their last call we discussed the exception slash edge cases to the self-destruct EIP and so after checking with the L2s, there's no L2 that breaks based on the change so I believe optimism is the only one that uses the burn but they call it inside of a contract creation transaction, so they're like unaffected, it still works under the New Logic yeah and Danno was there more that you wanted to hot to cover beside this?

**Danno**
No I just want to do last call if anybody knows of any other change that we need to look at I looked at the ones off of l2b like you said optimism is the only one that uses the burn the other ones either just use exactly what's in or they blow up, on they don't implement self-destruct or they revert on self-destruct. Polygon zkm changed it to send all but that brings them out of EVM compliance so I'm not too terribly worried about accommodating them based on the spec because they're already moved off the spec. 

**Tim**
Got it. Any other thoughts comments on this? Okay so yeah so we go I guess we can merge your clarifications to the EIP Danno yeah anything else on self-destruct?

**Danno**
I think that's it.

**Tim**
Cool okay yeah and Mario says that all the tests are implemented with the clarifications from that pr already. Okay anything else on the EIPs themselves for Dencun otherwise there's some engine API stuff but on the EIPs themselves any other comments thoughts concerns? 

## [Devnet 8 spec]( https://notes.ethereum.org/@ethpandaops/dencun-devnet-8) [45:10]( https://www.youtube.com/live/X46mbG8N5XM?feature=share&t=2710) 

### Unmerged Engine API PRs

#### [Add blobGasUsed and blobGasPrice to receipts for 4844 txs execution-apis#398]( https://github.com/ethereum/execution-apis/pull/398) 
### [Clarify Cancun payloads handling by earlier APIs; reorder checks execution-apis#426](https://github.com/ethereum/execution-apis/pull/426) 
### [Rename "data gas" to "blob gas" execution-apis#451]( https://github.com/ethereum/execution-apis/pull/451) 

Okay so Andrew, there were three engine API prs that you mentioned were not merged and we were not sure if we wanted them in devnet 8 or not, so they're in the agenda but the first one is adding block gas used and block gas price that it receives for 444 transactions, second one is 426 which clarifies the Cancun payload Delaney and then the third is just a rename of data gas The Blob gas. They're currently all listed in the spec but they're not merged. I guess given especially we have this extra delay or a short delay due to the pre-compile change, does anyone see a reason to like exclude any of those three from the devnet? Because it would potentially delay things or introduce logics that we don't want to test quite yet? If not then I think we should okay so we should keep them on and I don't know if there's any specific blocker to merging any of them. 

It looks like there's been some approval on the first, there's some discussion on the second and the third looks approved as well. So yeah maybe if by Monday we can try to have a look at those get them mostly merged, and if there's any discussion left on either of those three prs, we can discuss it on the testing call Monday. Does that make sense? 

**Andrew**
I think I just maybe if you have time we can discuss the second one. I think it makes sense and I think we discussed it a few times, but I don't remember whether there is still opposition to it or not. We can postpone it, but if we can agree now to merge it that would be great. I mean 2426 yeah like to my mind it makes sense.

**Tim**
Yeah it doesn't seem like there's any opposition on the pr, yeah the only one that still seems to have discussion is like their receipts pr but the two other ones seem yeah, the two other ones we should just merge. On the receipts, yeah on the receipts, there was like a comment by Peter that's just, I guess made obsolete by the previous naming change, but is there any other reason not to merge that? Or do people feel like we need more discussion? 

Okay it's already implemented in Besu. Okay so yeah let's merge the last two for sure and then yeah it seems like there's support for the first one as well but if maybe if like some of the implementers just wanna give it a thumbs up we can get it merged as well so all three merged by Monday?

**Andrew**
Yeah I think all three make sense.

**Tim**
Cool and then Mara says Hive can be updated to reflect the changes from 426 today. Yeah awesome. Anything else then on devnet 8 or engine API specs?

**Gajinder**
I think there is one small change that we still need to do regarding fork choice update. Basically we in the Endian API specs we haven't clearly mentioned that Cancun or words you should only call fork choice update 3. I mean on new payload V3 we already made it made a one-to-one correspondence of these versions with regard to the hard forks but I think we haven't specified on fork choice update so I think that we should also get in and close it out.

**Tim**
So there's no PR for this yet correct?

**Andrew**
But isn't it covered by 426? I think it says that it has a fork choice update.

**Tim**
Sorry so does this used to 

**Andrew**
Do we need to use a fork choice update 2 or with 3 for Cancun V3 only I mean we decided that Cancun hours will make sure that the hard fork and the versions will match because it makes for an easy validation on the inside and I think there is we haven't really updated for new payload V3 but we didn't basically update the same for fork choice V3 and there is no EIP ad but I can drop in something I mean it should be pretty easy to drop in right so it should be do I going to do it on top of like on top of four to six or as part or it will are going to update for 426 I think we can update photos explorations.

**Tim**
Okay cool okay so then let's merge the receipts pr and the renaming basically as soon as we can and we can make that change in 426 to require the call to V3. Does that make sense to people? Okay anything else on anything else on the test net or sorry yeah devnet 8th or then EIPs or specs in general?

**Pari**
Oh yeah Mario so yeah I just wanted to comment that we have The Hive branch that is ready to test all the changes up to now before deep recompile changes that we're going to make this weekend but if clients want to test I share the branch in the interop channel and you should be able to run the execution clients with this and that's up to this point in time yeah, if you have any questions or help me into wrong do you have tested just let me know. 

## Large Validator Testnet Results [53:25]( https://www.youtube.com/live/X46mbG8N5XM?feature=share&t=3205) 

**Tim**
Awesome okay moving on, so Pari, you wanted to share some updates based on the large validator test that you ran. 

**Paritosh**
Yeah so over the last couple of days we've been running some big validator tests, so we've been attempting to have a testnet up with 2.1 million validators and roughly 420 nodes. We tried once with machines that we're using on other testnets so those were four core 16 gig machines and that hit memory and CPU limits almost immediately, and in order to save some time we went really overkill so we went to 16 core 32 gig machines, and we've done a split such that each node has roughly 5000 keys, and we're mostly mirroring what you see on mainnet. So Prism, Lighthouse, Nethermind account for roughly 1 million validators, so about half, slightly over half, and you can have a look at some initial impressions here, the last run had a regenesis about an hour ago and we're still not able to finalize, we're still noticing issues with late blocks or with duties not being performed in time, and we definitely appreciate help in triaging everything. 

And the whole purpose of this is we want to be able to launch the host key test net which would be roughly one and a half million validators but we don't know if the current paradigm supports such a large network so we wanted to go with a 2.1 million validator testnet, and see if we need to make emergency changes or not.

**Tim**
Got it. Thank you. Any comments, thoughts by client teams, or others? Okay.

**Danny**
We can touch on it again next week. 

**Barnabus**
This will not be online for a week by the way. We don't plan to run this for a very long time because they are quite expensive to us so you'd like to get as many people as well on them as soon as possible.

**Danny**
Yeah I don't mean to delay consideration but even if the testnet's down, this is a conversation we should continue next week.

## EIP Discussion [56:13](https://www.youtube.com/watch?v=X46mbG8N5XM) 

### [EIP 5806](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-5806.md)
### [EIP 7377](https://eips.ethereum.org/EIPS/eip-7377) 

**Tim**
Okay next up so there were two EIPs that people wanted to briefly present today so the first one was from Hadrien, 5806. I don't know if you are on the call.

**Hadrien**
Yes hello?

**Tim**
Oh hey!

**Hadrien**
Yes so yeah do you want me to present it or?

**Tim**
I guess do you want to give maybe if you want to give like a minute or two background yeah on it and if there's any questions that you'd like answered yeah this is a good time.

**Hadrien**
So all of you know that account abstraction is a big topic right now and this pr is not really about the context abstraction, so this EIP is not really a company but it falls into the same scope of thinking of what EOA will become and what accounts per user will become, and my intuition and what I understand from all of the discussion I've seen particular in HTC is that EOAs are here to stay because you will still need them to start transaction an operation like that and currently EOAs are very limited in what they can do because they can basically just send transactions there.

Are any transaction types you can produce blobs that kind of things but it's pretty limited and there are a lot of ideas of what EOAs will become. I think they will stay here in the network and I think it's interesting to provide them with more capability, while not starting to build something too complex and too difficult. And there is already a behavior that I think is really interesting. 

It's a delegate called Behavior and just this proposal is about yeah, let's just allow EOAs that are just accounts they don't have code but there are accounts like smart contracts to do a delegate for, and that opens a lot of possibilities while we're using mechanisms that are already present in the EVM that are already pretty well understood. So the possibilities include being able to do multiple to batch operations that would be ? 45. It's also allows a new way to execute I create to by calling by delegate called a contract that does create tools and it will also allow EOA to emit events which might be useful for social operations like advertising data under your accounts that can be easily recovered by Observers. 

**Tim**
Yeah does anyone have any comments questions thoughts about this? Okay let's start with Guillaume. 

**Guillaume**
Yeah, quick question because you say there would be two calls from EOA and I get the point. Would it be possible to get it to send it from, yeah no actually it's a system idea, but from a non-EOA account or at least to transfer it to a non-EOA account, and what I'm thinking here, is could we somehow hijack this system to recover some funds that were locked in the contract that would be, that was locked basically, that was destroyed or incapacitated for some reason.

**Hadrien** 
So to emit such a transaction, you would need the private key that when hashed, correspond to this address, so if it's a contract that was deployed using Create or Create two, that would not be possible. Also there are current proposals that I think are going to be discussed later in this call, about being able to create code in place of a new way to do a migration to account abstraction. 

Those transactions would not be able to happen because you cannot, since there is an EIP somewhere in remember the name that enforces that you cannot emit a transaction, if there is code at the address. So I mean the current ecosystem means that this could only be done for addresses that don't have code and that never had code basically. 

**Guillaume**
Yeah no, I understand that I'm just wondering if it would be possible to somehow extend it this way, but yeah I don't see it working either so okay never mind thanks

**Tim**
Ansgar?

**Ansgar**
Yeah I just wanted to say that my just initial impression would be that while I'm generally sympathetic with the idea trying to make EOAs more powerful, it seems like in the past when this came up like for example it's one of the people who fought for EIP 3074 quite a while two years ago, on this call, without success, and I think generally the skepticism was that executing code, basically that allows things like multiple transactions from one account, within one transactions, just is a pretty high security risk because then one single transaction can empty out all the accounts and whatnot, so I think all the reasons that made us not go with 3074 also apply here unfortunately. 

Also specifically I think in the context of delegate calls from a new EOA, there were some additional concerns around just executing code in the context of an account basically what the implications are for storage usage, and all these kind of things, so it seems like this would basically be a more contentious version of 3074. 

Yeah for these reasons also specifically because there are now some other proposals to completely migrate away from EOAs, even at basically from the requirement of using them for entry points of transactions, it seems like this is probably not the way to go, but I could be convinced with basically, but I feel like this is not as simple of a using existing logic of the EVM as it was presented, so I think it would be pretty extensive change, and with a lot of implications, and would require a lot of basically justification. 

**Hadrien**
Yeah if I can just say two things here, one is about yes, we are preparing for pass to towards migration. I still believe that the migration while it's very useful has also some downside like you are committing to a specific code that you cannot change later. Some people I believe will stay with EOAs, so I think it's still valuable to accommodate that and about 3074 is a very big difference here and what makes this less powerful but also I believe more secure than 3074 is here all the replay protection and the signature is built into the transaction by itself. It's not an independent system if you sign a transaction like this, it's only good for one transaction, it's not something that is going to be used in the future if you sign 3074 there was a risk that you should sign for a contract that is malicious or buggy, it could exploit you.

Here like we're using the replay protection currently built in the system. It's safer. Now for sure if someone signed a transaction like this that is malicious, they can do a lot, but so is true of any other like more normal kind of transactions, like if you have the private you have controller versus the accounts that's basically

**Tim**
Danno?

**Danno**
So this is a bit more of a meta commentary about 5806 and 7377 and it seems like we're trying to get into accidental design of a good account abstraction system, and before we do that I think we need to pause and consider, is this really the best way to get the account abstraction system that Ethereum needs. I mean these are you know interesting solutions, they open up interesting design space, but I think we should step back and think if we served better by deliberate design towards account abstraction. 

So that's my concern with these going forward is we might be left with some albatrosses when we go to real account attraction system. These also might be the right solutions I mean I don't know that's just my concern.

**Hadrien**
Here one point I made in the document that maybe I haven't made very clear in this clearly, I don't think this is a solution track on abstraction I think it's just providing useful mechanism for EOA, and this is definitely not an alternative to the other account abstraction proposals.

**Danno**
My concern there is that it could cause design constraints on the other proposals if they now have to account for delegate calls and EOAs and EOAs having storage now. 

Maybe it's the right solution, maybe that's what they need at the end. I don't know but I think we should make sure that we put the big rocks in first before we fill in small rocks.

**Tim**
Martin?

**Martin**
Yeah just something that Oscar and now also Danno kind of mentioned. I think this should be raised in the security considerations on this e the fact that a user might invoke some mod to think or whatever contract it stores some things into the storage area or the EOA, and then later on the user unwittingly might invoke some other delegate call thing, which also interacts with the storage area on the EOA, and users can, you know, invoke things in strange orders, and be towards the slots may interfere in ways that are not intended.

The same problem would exist in contracts except that contracts are usually written more, I mean, not as haphazards as the way end users do things. So I think that's just, we raise a point on the security considerations. That's just my feedback. 

**Hadrien**
Yes I completely agree with that.

**Tim**
Okay thank you. So there's the eth magician thread. I think we can continue the conversation there and then the Discord. Yeah just to be mindful of time. I have to move on to the next one. Thanks Hadrien, for coming and presenting this. 

**Hadrien**
All right thank you thank you for having me.

**Tim**
Of course. And next up I believe lightclient had an EIP as well that you wanted to discuss it.

**Lightclient**
Yeah I wanted to introduce the EIP 7377 which was kind of mentioned briefly in the discussion in the last one but I wanted to explain the functionality. Very simply what it allows is it allows for an externally owned account to submit a transaction, which creates a one-time code deployment to their account, and the specifics are, you know something that we can debate on The Magician's forum, maybe on Discord. There's some ideas here that I think are kind of interesting, like instead of deploying code and running a knit code we actually have the user submit a address which the code will be copied from. I'm taking advantage of the fact that we usually store only the code hash as an associate in association with the account. These are just things to try and make it as cheap as possible for users to migrate their EOA to a smart contract wallet and I wanted to mention that I think there's a lot of demand for things in the protocol layer to improve ux. 

I mean here we're talking about two different ux improvement proposals and over the last couple years, ERC 4337 has taken a lot of growth, and seen a lot of deployments on many chains outside of just Ethereum L1, and this EIP is something that I think really helps 4337 and any other kind of account abstraction proposals that we might have whether it's in protocol, or you know some sort of application level one, because a drawback for users is if they want to use an account of abstraction mechanism, whether it's in protocol or out of protocol, they have to deploy a new smart contract wallet and move all their assets over. 

So this EIP is really trying to address that issue by making it simple for users to just start using smart contract wallets, by submitting a single transaction upgrading their existing address to the smart contract world. Yep that's the general proposal. Happy to answer any questions hear any feedback thanks.

**Tim**
Thank you any thoughts questions comments? Okay oh yeah okay please.

**Yoav**
I just wanted to add that indeed we are seeing a lot of demand. This is one of the most commonly asked question with the 4337 users and there was quite a big ecosystem for 4337 at this point so it's very often people ask about migrating an existing account. So I'm not very opinionated on how we should do the migration, but we should have some form of migration, so my main thing I think about is whether the right way to do it is a through a transaction type of an OP code but either way it would be good to have a migration path. 

**Martin**
Yeah yeah I just can mention quick because I read through this Heap a couple of days ago and and I had to get the clarification from lightclient on this specific point. So after this migration there is code on the account and the transaction which where the sender has code is an invalid transaction. So I just wanted to point that out but after you do this upgrade there can never be a transaction from that account again, unless self-destruct still exist, and in self-destructs I guess.

**Yoav**
Yeah that is actually that's actually a feature not a bug I think, because if you migrated your account, one of the primary use cases for account abstraction is that you can rotate the keys so if you change the key of the account you don't want it to ever transact again with the old ecdsa key. 

**Martin**
Yeah I just wanted to lift it up so 

**Yoav**
Yeah yeah you're 100 percent right.

**Tim**
Ansgar?

**Ansgar**
Yeah if you wanted to say that I think maybe similar to the comment of the last EIP that I think the direction is a fruitful one because simulator we should probably migrate or completely overturned a world but I think this EIP is mostly used for as like a concrete proposal so we can start debating this and not something that we would just do in the very short term because it has very far-reaching implications, so basically this is more of a set an ambitious goal and then start debating with how we how we get there kind of thing, let's schedule this for the next time in my opinion. 

## [Verkle Trie Update](https://verkle.info/) [1:13:22]( https://www.youtube.com/live/X46mbG8N5XM?feature=share&t=4402) 

**Tim**
Got it. Yeah I think with that we're probably good to wrap this up for now, unless there's any final urgent comments on either of the EIPs okay. 

Then last up we have Guillaume and Josh to give an update on the work that's been done on Verkle Tries. 

**Joshua**
Let me share my screen. Okay, let me know if anyone cannot see my screen. 

**Tim**
I can see and hear you.

**Joshua**
Okay perfect cool thank you. So in the interest of time I will go through some portions of this fairly quickly so we can get to what we believe to be the meat of it here. Most of this presentation will be kept fairly high level but please feel free to flag anything of course that you would want to see more of a deep dive on and we would also love to encourage anyone to join the discussion on upcoming Verkle implementers calls, where we can dive deeper, and we can also of course future ACDs as well. 

So quick overview or quick agenda in the past five or six months, we have hit a number of big milestones that we are excited about so we will give an overview of that, but of course there are a number of milestones remaining. And we would love to bring more people in who would like to contribute to any of these remaining milestones. Which brings us to questions answered and questions remaining. 

These are questions or general areas we think we have solved, or have a very clear path to solving in the near future, as well as questions still remaining and will require a bit more exploration. The overlay method, although most of this will be high level, we will do a very quick mini deep dive into the overlay method, goal is to bring people up to speed here quickly, the design and implementation of the migration has perhaps unsurprisingly downstream effects, and will impact some of our remaining open questions here. And then finally next steps, how we will begin to answer some of these, yet to be answered questions. 

Hopefully by getting more people into the discussions as well. I will go through this, very quickly, quick reminder on why we are doing all this in the first place, won't spend much time here. I think most people on this call are likely familiar with this but state is growing, this growth is unbounded permanent even today, you likely need a two terabyte SSD to run a node, but in a future where we have stateless, it is possible that this could be something like one gigabyte or less.

And making it easy for anyone to run a full node is a very good thing. So the key to unlocking stateless is small proofs, which just happens to be something that Verkle gives us. So with Verkle, thanks to the much smaller proof size, no extra state is needed to validate a block, you can do it with what the block gives you, also a node here we are going for a weak statelessness, which means block builders will still need to store the full state. We can share more at a later date or if we have time on why we believe that to be the best path or you can read a write-up that Dankrad has created here that I've linked to my notes.

So diving into where we have actually done over the past six months, as I mentioned it's quite a lot, a number of notable milestones have been hit on the performance front, thanks to Ignacio and others. The overhead of Verkle is much lower, current benchmarks at 20 percent, compared to Merkel when we've replaying blocks. The overlay method so this again is the solution for the Merkel to Verkle migration. We have gotten to us a place on the trade-off where there are no longer trade-offs like two X ing designs. Disk space which is a huge win and we have again validated the initial strategy and created a working proof of concept.
Multiple clients have made great progress likewise on the snap sync front. Lastly we are currently targeting our first shadow fork for later this month. Client updates, if you'd like to see a full list please visit Verkle.info. Also as a quick side note Verkle.info is a resource where we point people to who are looking to get up to speed on Verkle. In general find the latest documentation and just see the current status of things. But on the client updates front, again just a very quick sampling here, Nethermind and Ethereum JS both making progress on stateless which is exciting. Besu has a small group working on making sure that Verkle will play nice with Bonsai and Lighthouse and Lighthouse is deployed to mainnet and Lodestar will soon be joining.

Okay so with that I will hand it over to you, Guillaume.

**Guillaume**
Thank you. I need you to try to unshare your screen so that I can share mine. But yeah so we noticed that there was a lot of misunderstanding about our current state, like this current state of development of Verkle. And usually it comes with not being aware of what the current state of the transition proposal is, so I'm going to present some slides actually presented at HCC, I will in the interest of keeping it short, I will go over it fairly shortly. I'm going to select the right window, there's too many of them. Let's see, can you see my screen?

**Tim**
Yes.

**Guillaume**
Okay excellent so yeah so if something is not clear just, I'll direct you to this to this talk I did that at HCC, otherwise feel free to ping me. So yeah so the principle is pretty simple. The idea is that just before at the end of like at the last block before the fork, we have the MPT and we have all the internal nodes that are represented by those things in red. All the blue squares are the values that were written to the state before the fork and we have this green arrow that represents an iterator that is going to sweep over the state over a series of blocks. 

So at the beginning of the first block of the of the fork you start with an empty Verkle tree that is really that written right that is writable, and the mpg like I said becomes read-only. And so as you execute the block, values get written too so they are represented by a purple square, which means personal squares are values that get written to the state after the fork. So here first value got written into the tree, and at the end of the block, a number of values, so in this case two get moved, actually they don't get moved, they get copied from the Merkel tree to the Verkle tree.

And so if you're looking for data that is currently represented by a pink square and that data is currently not present in the Verkle tree but it is present in the MPT, you first go to the to the Verkle tree, and if you don't find the value there you go search it through the Merkle tree. So that's basically the principle. Each block more values get copied into the Verkle tree, some values that were there before get overwritten, and when the lpt the last block with the MPT gets finalized, you can delete all the internal nodes, so you already free up some space, and as things continue, once the whole state has been converted, you can delete the MPT because all the values that were present then have either been overwritten, or have been just copied.

So just to finish on this story, the reason why we're trying to get people to look at this a bit closer is because time is of the essence. If we decide to convert 1000 leaves at per block at a rate at like and assuming that the payload, the total amount of data that needs to be transferred is one billion leaves, it will take six months. So one billion leaves to be clear is an estimate of what the size of the tree will be in a year.

If it's ten thousand leaves, it's 15 days, so of course those numbers are an estimate of if we perform this fork in the next year. If we do it later it will be more so even with 10K with 10000 leaves, it can be more than 15 days. So yeah, just to be clear, we have answered some questions or at least we're pretty close to we have definitely answered the design where sometimes finalizing the details but most of it is clear.

We have good performance, we understand how we're going to migrate, we have, I mean, we Nethermind has a prototype of snap sync with Rocco. Now the question is how do we distribute the pre-images because we need to rehash the whole tree, which is where the the problem lies. We still have some questions about the gas schedule, how to update it during the transition. And yes basically we need a lot of testing, RPC or not.

So yeah what we're going to work on in the next month is basically the shadow fork validating the snap sync, relaunching a testnet, and hopefully we can get more clients to join us in that effort, so there's a call, the Verkle implementer call and the channel Verkle trie migration that you can join. The next Verkle implementer is called if I'm not mistaken, is next Tuesday. And so two hours before ACD, like the time at which ACD starts I think. And so if you want to be invited, let us know, let Josh know ,and otherwise yes, we are always interested in the deploying more application, more contracts to the testnet to stress it out, and there's also currently the two big discussions are how we are going to distribute the pre-images and the gas cost during the transition. And yeah I think that was the last slide. Yep so that's pretty much it.

**Tim**
Thank you Andrew. You have your hand up and then Danno has a question in the chat as well.

**Andrew**
Yeah so for pre-images we can just introduce a new methods to the eth protocol or like a new protocol and Aragon can serve them, because as you know Aragon knows are all full archive notes and we have all the pre-images.

**Tim**
 Jim Joshua, thoughts?

**Guillaume**
So sure yeah I was just thinking of something smart to say after that, but yeah we'd love to basically that's yeah if we can experiment with Eric and distributing the pre-images, like create a protocol that would be a great start a great starting point.

**Andrew**
Right yeah so I think we will try to find out a developer but you say it makes our job easy if somebody like just maybe pens the protocol like, something like an extra capability, like Snap is it or whatever, but it's a minor point yeah we can do it.

**Guillaume**
Yeah so I think that would be the topic of conversation on the next Vic and then we can do exactly that.

**Tim**
Danno has a question. What will state proof look like during the overlay period? Verkle only and all reads get moved over, or is it rights only improves…

**Guillaume**
Yeah, I missed some of that. 

**Tim**
…commented in the chat

**Dankrad**
…there are no state proofs…I mean state proofs are separate from…Verkle Trie just change the commitment that state proof become possible. So like while the changes in in progress, state proof would still be large so it wouldn't make sense to introduce them.

**Danno**
Well there already exists the need to get proof that will return a large proof from the Merkle tree. How would that transition, I guess, is my question would there just be nobody can do proofs until the transition's over? I don't think that's a good solution.

**Dankrad**
I thought you meant block witnesses by that. Okay sorry.

**Guillaume**
So yeah, I mean my understanding so far was that there would be no proof. We definitely know MPG proof, except you would have to, you could still get the MPT proof it's just that the MPT doesn't get inserted anymore, so they would be a bit less value in this. We could just provide proofs for the Verkle tree itself, during the transition.

**Dankrad**
I mean I think like it depends how on like how much this is used at the moment, but there are definitely ways to have state proofs during that time. So basically the complete state proof would be a worker proof and if it does not exist in the Verkle tree, then you would provide a proof for the MPT at the same place.

**Danno**
So I don't think we can design in this call, but that seems like something needs to be discussed in the tooling discussions and roll out.

**Dankrad**
I'm simply saying it's possible to do it.

**Tim**
Any other questions comments? 

There's a question here about the JSON RPC from Mario in the chat. 

**Guillaume**
I'm having some issues with the chat, so if you could read

**Tim**
Should we introduce eth get Verkle proof that returns empty until the tree node makes it into the Verkle tree?

**Guillaume**
We could do this for sure the question is it going to be useful but yeah that would be possible to do that.

**Tim**
Any final questions? How is the Shapella rebase coming? H

**Guillaume**
It's painful. I just created a PR today but yeah I need some input from Gary because we have this new like storage system or database system in geth that I need to integrate with so yeah I would say it's go it's happening.

**Tim**
Nice. Okay any final questions before we wrap up? Sweet. Well thank you everyone talk to you all on the next CL call next week.

**Everyone**
Thank you.

Call ends.

## Attendees

* Tim Beiko
* Danny
* Ignacio
* lightclient
* Ben Edgington
* Mario Havel
* Danno Ferrin
* Gajinder
* Mario Vega
* Pooja Ranjan
* Gabriel (EthJS)
* Jamie Lokier
* Tanishq
* Ameziane.hamlat
* Phil Ngo
* Justin Traglia
* Draganrakita
* Andrew Ashikhmin
* Alex Stokes
* Terence
* Guillaume
* Ayman
* Saulius Grigaitis
* Carlbeek
* Spencer-tb
* Mark (ethDreamer)
* NC
* Nico Flaig
* Roman Krasiuk
* Joshua Rudolf
* Dankrad Feist
* Kasey
* MH Spende
* Marcin Sobczak
* James He
* Sean
* Pawel Bylica
* Danno
* Hadrien
* Ansgar
* Yoav
* Kasey
* Carlbeek
* Gcolvin
* Tanishq
* Sasawebup
* Jared Wasinger
* Jochem
