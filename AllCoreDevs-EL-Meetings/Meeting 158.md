# Execution Layer Meeting #158
### Meeting Date/Time: Mar 30, 2023, 14:00-15:30 UTC
### Meeting Duration: 1hour 30 minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/744)
### [Video of the meeting](https://youtu.be/RQ2WtyevRXE)
### Moderator: Tim Bieko
### Notes: Alen (Santhosh)

| Decision Item | Description                                                              | 
| ------------- | ------------------------------------------------------------------------ | 
| 158.1 | **Shanghai Incoming** On Tuesday, March 28, the Ethereum Foundation (EF) published a [blog post](https://blog.ethereum.org/2023/03/28/shapella-mainnet-announcement) announcing the forthcoming activation of Shanghai on mainnet Ethereum. Shanghai contains one major code change, enabling staked ETH withdrawals from the Beacon Chain. The upgrade will go live on April 12 at 6:27pm (ET). All Ethereum node operators are encouraged to upgrade their software to the latest client versions, which are all linked in the EF’s blog post.
| 158.2 | **Mega EOF** EOF is a bundle of code changes that target upgrades to the Ethereum Virtual Machine (EVM). The EVM is the execution environment through which smart contract code and user transactions are compiled and deployed on-chain. Beregszaszi explained that the EOF changes proposed last December have undergone significant edits to address feedback from other core developers and clients teams. 
| 158.3 | **Deprecating Self-Destruct** Based on the proposal, developers agreed to consider the EIP for inclusion in Etheruem’s Cancun upgrade. Beiko recommended that the authors of the EIP conduct a more thorough survey of Ethereum stakeholders and the dapp ecosystem to ensure that the code changes does not break or negatively impact existing smart contracts.
| 158.4 | **Exposing the Beacon State Root in the EVM** Ethereum Foundation researcher Alex Stokes, then shared a few paths forward for implementing EIP 4788, which seeks to expose the state of the Ethereum CL, also called the Beacon Chain, in the EVM and make the state accessible to smart contract applications by the protocol without the need for third-party oracles or other trusted intermediaries
| 158.5 | **Builder Override Flag** The Engine API dictates communication between Ethereum EL and CL nodes. Notably, client teams can implement the changes asynchronously without a hard fork. The change adds a new Boolean field called “should override builder” that the EL can use to indicate to the CL node that it should consider falling back on local block production instead of relying on a third-party builder. This field is useful in the event that the EL node notices peculiar transaction activity that indicate some kind of censorship within blocks produced by a third-party builder. CL nodes can override the flag but at the very least, node operators will be notified of potential censoring behavior on-chain and be able to act accordingly. Nethermind (EL) client team is currently working on a prototype for implementing the proposed changes to the Engine API. Kalinin encouraged other EL client teams to also take a look at the specifications and consider prototyping the override flag.

**Tim Beiko**
## Intro [1:51](https://youtu.be/RQ2WtyevRXE?t=110)
* Okay, welcome everyone to ACDE #158. couple things today, quickly we'll go over Shanghai and, and, and that, which is a plan in the next, two weeks. but then most of the call, we got some big updates on pretty much, all the largest, potential EIP for Cancun. So we can, go over those and if there's anything else people wanna bring up, we can do that at the end. 
* I guess to start, so we announced, Shapella earlier this week. I linked the blog post in, in the agenda. I can put it here in the chat as well. and, I think Argon is the only client, for whom the version has changed since the original announcement. so if you, had originally downloaded version 2.41, you now need to change the 2.42. Otherwise, everything that was originally listed is still valid. Anyone from any client teams or testing or whatnot have any updates or, or, thoughts they wanna share on the, the announcement or their client release? 

## Shanghai Updates | Announcement [3.11](https://youtu.be/RQ2WtyevRXE?t=191)
**Terence**
* Prsym is thinking about another minor release, probably sometime less week to fix some, API RPC issue. This is, this is our, slightly optional if, unless you're like a, operator, you are pulling, this api, then you probably don't need to update. But yeah. Anyway, watch out for our announcement. 

**Tim Beiko**
* Okay. Anyone else? 

**Marius**
* Yeah, we started doing some, EVM first for Shanghai. and, I have not looked at the results yet, but, I'm currently doing it with, Geth, Besu and Nethermind, and I'm going to add Argon and, Nimbus EL to it as well. 

**Tim Beiko**
* Cool. Anyone else have anything you wanna share about, releases or upgrades? 

**Pari**
* We have the last shadow for our plan for next week. it'll go through the transition either Tuesday or Wednesday. And the idea is that relays are up and running then, and we can test the transition with relays. if someone wants to test, release their planning to have in the next couple of weeks, let me know. Otherwise, I'm just gonna use the recommended releases. 

**Tim Beiko**
* Got it. anything else? 

**Phil Ngo**
* Loadstar has, 1.7 0.1 out. it's a minor update for people using Gorley, for testing with Loadstar. we may also do a minor bump with a fix for our BLS pool, but that's it. Keep an eye out for that. 

**Tim Beiko**
* Okay. But the 1.7 is still, is still correct if people just want to keep that correct? 

**Phil Ngo**
* Correct. Yeah, they'll still work. 

**Tim Beiko**
* Okay. Anything else? 

**Pooja Ranjan*
* Maybe a small reminder, related to the EIPs. So now Shapella upgrade is in public testnet, and obviously we do have the mainnet, date announced. So ideally we should have all the proposals, which are going to be deployed on mainnet in the last call. So this reminder is for the authors, for proposals 3855, 3860, and 4895. 
* Please go ahead and create a pull request to move the proposal to the last call ending on April 12th. Yeah, please reach out, to ECH. You want us to create a pull request and you are okay. Approving, otherwise, yeah, do let us know if there is anything we can do. Okay. 

**Tim Beiko**
* Okay. Anything else? If not, just as a reminder. So the fork is scheduled for April 12th at, 10:27 PM UTC. That's EPOCH 194048. so please upgrade your node before that. And for all the validators, we have a withdrawals f FAQ that's linked in the announcement, that you should check out, to make sure you're properly ready, for withdrawals. 
* And then, similarly, Alex, you made a small update to the withdrawals EIPs for 4895, just to add the actual timestamp of the fork into the EIP. Anything else to add on on that? 

**Stokes (Alex)**
* No, that was it. It was just TBD, and so I just put in the, mainnet timestamp. 


## Cancun Updates [7.40](https://youtu.be/RQ2WtyevRXE?t=460)
**Tim Beiko**
* Anything else on, Shapella? Okay. so for, Cancun, we have updates on EOF self-destruct, the Beacon State route and, the engine API. So we can go through each of those. signed with EOF, last week or this week, there was, the mega EOF endgame spec that was put together. I don't know, Alex Pav, did either of you want to give, context on that and kind of share the latest on EOF? 

**Alex**
* Yeah, absolutely. you can hear me correctly, right? 

**Tim Beiko**
Yeah, yeah, Yeah. 

**Alex**
* So just like a bit of background, with EOF, we had a, a fairly stable version, you know, last December. And then we had, this, this proposal, to avoid code, in inspection introspection. And they also potentially, avoid like gas inspection capabilities. and so basically we have worked since then. the work mostly started at to redesign EOF in order to, to support these, requirements. and also meanwhile a number, number of, smaller requirements arose. and so basically over the, the past like two months, we have been working on, flashing out these questions. And, we took the unified spec, which, many of you may be familiar with. and we made, the changes to the unified spec, in order to support these requirements. 
* I also have like a, a guest, with the diff between the two, and the diff actually isn't that big. I think it's around like 200 lines. just to show that, you know, this may look like a lot of, features or a lot of new things compared to last time, but actually the diff isn't, that significant. I think the, the biggest, so the requirements we had is to avoid code inspection, and I think we successfully accomplished, the supporting that requirement. what that means is that creation has to change significantly. 
* And it also means that we want to remove, operations like, you know, code copy and code copy. and we figured out a way you had to deal with code copy, especially, for the direction of going from legacy accounts to EOF accounts. it's describing the document what should happen in that case. 
and beyond that, the create instructions and the create transactions are the, the biggest changes. 
* So what we came up with is, actually not that far away from the, initial proposals back in, I think end of December or early January. I would say it's a refined version of that. we have two, create instructions. the first one is create three, which takes a index for a sub EOF container. And this sub EOF container would be, part of the, the creator contract. And the sub EOF container is the runtime piece. 
* So this create trans instruction, can be deployed, time validated that it has, you know, a correct, payload for the runtime. and that is described how, the creation process works. It's not really, any different to how it works in legacy. the main important difference is that we only have create two style, creation, which uses a code hash and we don't really have, a need for a announce. 
* And then the create for instruction is a bit more interesting because with this CREA tree, you can imagine that, somehow, this runtime payload has to, I mean this in IT code has to enter the system. and there we have two options. 
* We can, either create a specific create transaction, or we can, introduce this create four instruction, which, works a bit differently. so what we do is, instead of having a specific create transaction, we only, extend the, the basic transaction format. And in fact, we, we only want to extend the 4844 transaction format with the new field, which is a list of containers. 
* And this list of init containers can only be inspected through the create four instruction. So the create four instruction either, takes the, the index, and this init container list, or it could take, this is the, the only question we haven't settled on yet. It could take the hash, off an entry. 
* And that's the only way to inspect this data. and, and at runtime this, data is validated to be, for EOF, and then the creation process is the same as, as it is in create treee. So that's the only difference between the two. there's also an interesting, side effect of this. 
* We could have, basically a creator contract or even a creator pre-compiled, but when I say pre-compiled here, it's, it's, it's actually not, it doesn't need to be written in, as a pre-com compiled. It only means that having this EVM coded, known address, there's an example, what such a creator contract would look like at the end of the document. 
* And it basically, would take the index, of this init code list in the transaction, and some additional data, as the input would perform the creation and return the address. the interesting effect here is that if we do have such a creator contract, and then instead of having a create transaction, one can just send a regular transaction to this creator contract in order to deploy code. 
* And then the rest of the, the additions is, instead of the return instruction returning the, the payload, we have a return contract, because that only, that only re has an auxiliary data, which is appended, to the runtime payload. 
* The only reason we, we need this, append option is, to, to support, this feature of, of solidity, of immutables. this feature in Solidity is, basically you have two options today on the, on on legacy code had to, access data. You could just create storage slots, or if you don't wanna spend all the, all that gas on loads, you can use this immutable feature in, in solidity, which basically translates into, a pending constant data and creation time, and then code copying, those data directions instead of S load. 
* So return contract, is not returning the entire payload. It is only returning a payload, which is appended, to the,runtime container. So that is the only piece which can be inspected.
* And since we don't have code copy or code copy, if we do wanna support this immutable feature, we need a way to inspect, the data section. and for that we have a number of instructions, such as data size, data copy, and data load. and there's a, one specific instruction called data load NM, which instead of taking a stack item for the offset in the data section, it takes it as an immutable, as an immediate.
* And the, the main benefit of this is, this basically replaces, this could be used, instead of, pushing constants in solidity, you could just, date a load from the data section, where, the content is something like an immutable. So this piece is really just an optimization, this data load and instruction. but the other instructions would be needed to, you know, perform this feature set, the number of other, like smaller changes. 
* But I think this would be the, I think the, the important ones. and maybe I would close out with, saying that every other question, which, was an open question during, you know, earlier discussions in December and January and anything which, has been, brought up by the community has been addressed, at this specification. and then the lastly, beyond the specification, we have a implementation of each of these features in a EVM-1, and we are in the process of creating, state test, for them. Yeah, sorry, this was a super lonb, thank you. This didn't expect. 

**Tim Beiko**
* Yeah. Does anyone have thoughts, questions? 

**Andrew**
* Yeah, I think it, it's great. but,  I worry that if we try to deliver it in Cancun, it just, it's too big a change. so I would definitely want to have it in prod, but I just think I'm going, is stretching it. 

**Tim Beiko**
* Got it. Thanks. Any other thoughts? Either on like, the spec itself or like overall timing? Okay. I guess, where's the best, 

**Danno Ferrin**
* I Have A question, please. What are the design decisions calls for adding a field into the transaction? I'm interested to solicit, the opinions of the other core devs of their appetite for that edition. Does it feel good, feel bad? Great. Awesome. You know, some sort of a signal as if whether or not this is the right direction, they would expect a transaction like this to move in. 

**Tim Beiko**
* Oh, sorry, I lost audio for a sec, Daniel. I don't know if anyone answered to you. 

**Danno Ferrin**
* No one answered, no one raised hands. So there's no concerns with, adding an extra field into one of the new transaction objects to handle the new create, approach. 

**Marius**
* I do have concerns one concern is that I didn't really fully understand, the proposal yet, so I cannot really comment on it. So, like not raising concerns right now doesn't mean that I might not have concerns in the future. So we shouldn't take like, not saying anything as, as no concerns by default. 

**Danno Ferrin**
* That's fair. so, but I do wanna bring that to people's attention to please read it, and not just wait until two weeks before we're supposed to ship it on the test net 

**Tim Beiko**
* Yeah, and there's some comments in the chat about, basically verkle being another thing we wanna do, you know, after, after Cancun.  and, and, obviously, you know, if we push EOF out of Cancun and, you know, potentially do it in the fork after, you know, that also means we might push something like verkl out of the fork after and do it in the fork after that. potentially we could do them together. 
* But, you know, that risks, being a lot of big changes at once. yeah, I guess where's the best place? Clearly, like, I think teams probably need some time to look into this more and, and kind of digest it. Where's the best place to share feedback, comments, questions? 

**Danno Ferrin**
* There is an EVM channel in the Ethereum Discord. everyone who's implementing it is there. We also have an EVM implementer's call, on the Wednesdays that are not EL So it's the day before the consensus call, calling into that call. It's about the same time. just on the day before is an excellent time to come in and drill down with your questions and seek understanding. 

**Tim Beiko**
* Okay. Alex? 

**Alex**
* Yeah. So generally we had, a number of different options had to, to split up, because you may remember in, in January,  I said that I felt like, you know, doing all of this at once, maybe quite big. I tend to think now that the change set isn't actually that big as I expected, in January. that being said, it is possible  to break it up, by skipping some of the create features, and rolling out, you know, like for example, skipping create four, or skipping giving create three and having, a intermediate separate legacy create UF code. we did review these, these options and they are feasible. 
* So it would be possible to also launch this in two pieces. but if we, if we postpone all of these, I would still favor that we introduce at least the transaction field, to get a bit 4844, and just, you know, it would be a field which cannot be really used, but you would still pay the gas for it, because that way we can avoid like the qualification of, new transaction types. 

**Tim Beiko**
* Any thoughts on that? Okay. so I guess let's, oh, sorry. Ansgar?

**Ansgar**
* Yeah, Yeah, just Bearably wanted to say that my, my intuition would be that if we end up not bundling full EOF with 4844 I'm not very opinionated on the specifics. Can we have some small pins already in that 4844? 
* But what I would say is that probably it would be better to then just give EOF its own fork afterwards, in between, like be before the work with fork and just try to make it like a quick follow fa because if we keep basically trying to bundle it with another big change, but then we keep prioritizing the other big change over EOF, we'll just keep pushing it. So I feel like if we don't end up combining it with 4844, it should really get its own and fork afterwards. 

**Tim Beiko**
* Got it. I think in, in theory, I also agree, but I one risk like, well, I don't know if it's a risk, but like there will be other stuff that people want to do at the same time as this EOF forks. So we're just saying like, you know, the next fork is EOF and maybe there's not like CL changes that come in at the same time, but I think, you know, there is some overhead to like having these forks.
* We can try to keep it minimal and, and, you know, not have too many other things, but, we don't, we don't sort of get a fork between EOF and, or between like, you know, Cancun and Prague for, for free, right? Like, it just means we prioritize EOF before whatever we would've done next, which is, which is fine, but yeah, it, like, I think realistically you end up with, like, there will be other things that will be included along that and you know, it's another like, I don't know, three at least if not 4, 5, 6 months, to put out a fark generally. but yeah. Yeah. Yeah. So, so basically, yeah, EOF would be the big thing of that work. Yeah. Lucas? 

**Lukasz**
* Yes, so we were actually discussing it internally in Nethermind. And, what looks sensible to us is, not doing EOF in Cancun, but doing schedule another fork for that. that would, the, like, the driving force of the fork will be EOF. so that was like, that, that looks sensible to us, right? And then on the next fork, 
* For example, if the vertical trees will be going in, that would be for the vertical trees or, or something else. But, I think, those two things are big enough to the, to themselves that they, if we want want to do them, they should occupy like most of the fork, if we want to do them fairly soon after Cancun. 

**Tim Beiko**
* Got it. Thanks. Guillaume? 

**Guillaume*
* Yeah, I'm missing the part where, EOF is more advanced than vertical and therefore should be scheduled first. I really don't see, I mean, maybe I get the wrong impression, but, yeah, I don't wanna push verkle again when it's way more ready than other things. 
* I mean, if EOF needs more time, I don't see the point delaying verkle is, what I'm saying. And what  I'd like to understand why this is not obvious to everybody here. 

**Tim Beiko**
* So there's a comment about EOFF being much more ready than Verkle. Does it make sense that maybe, I don't know if on this call you have it, you're ready, or maybe on the next call give a proper update on verkle trees so that people can understand where, where it's at? 

**Guillaume*
* Sure, I can do that. Yeah, I mean, I can't even do that now if you want. 

**Tim Beiko**
* Okay. Can we, can we wrap up EOF first and then we can Yeah, we can definitely do verkle today as well, but, just wanna make sure we wrap up EOF 

**Guillaume*
* Yeah. No, but I mean, if you, if you, if you have an agenda, let's do it next time. No problem. 

**Tim Beiko**
* Yeah. Okay. Yeah. Yeah. So yeah, if there's, if there's time today, let's do it today, but we can do it next time for sure. Yeah. Angar. 

**Ansgar**
* Yeah. I don't wanna say anything about whether workload emphasis is ready, but what I would say is that actually it seems like bundling them would really not make sense, right? Because they're both very heavy, el side changes. So, I feel like if we are bundling something, then it should be EOF side and, 4844 for Cancun, but if that doesn't happen, we should definitely have them in separate folks, because that would just be a big mess, in, in my, in my opinion. 

**Tim Beiko**
* Cool. Andrew? Yes. 

**Tim Beiko**0
* Yeah. I'd like, to say like, I am totally for verkle, but, I suspect that, that, that actually switching to verkle, it's a huge, massive change on the EL side and, it will take other teams, a lot of time to be, in terms of the engineering to be ready for the verkle, so I kind of urge everybody to start looking at verkle and, doing the necessary engineering work, and it took, argon like years to change the data model. 
* So  it's, big and long change. So I'm just thinking that realist.  I'd, I'd love to be wrong, but I think realistically it'll take a lot of time just on the engineering front to be ready to switch to verkle. 

**Tim Beiko**
* Got it. Okay. So let's make sure to cover, if we have time today, we can do more verkle. but otherwise, next call, let's make sure to go over it and, and get like an update from Guilme and, and the different kind teams. any other thoughts on EOF specifically? 

## EIP-6780 [29.48](https://youtu.be/RQ2WtyevRXE?t=1788)
**Tim Beiko**
* Okay, in that case, next up we also have an update on self-destruct. so, Vitalik and Dankard have put together a spec, for the, basically self-destruct, but allow, allow it if it's called in the same, transaction as a contract creation, which addresses a bunch of the, edge cases we, we've discussed previously. yeah. Dan, do either of you want to give an update on that? dank, do you completely breaking up? 

**Dankard**
* Sure. 

**Tim Beiko**
Oh, Yeah, we can't hear you super well. 

**Dankard**
* Is this better? 

**Tim Beiko**
* Yeah, much better. 

**Dankard**
* Okay. So, so basically it's a, it's a new version of, deactivating SELFDESTRUCT.  we've had a few iterations. So this one, what it does is it's, it mostly works just like, the complete, deactivation, which just, makes it basically only send all the funds, except, in the case, where it's called in the same transaction where a contract was created in which it, in which case it will clear all the, all the storage and everything about the contract. So like, it'll be from EVM side point of view, actually, at least it'll behave exactly, like the current self destruct, you cannot detect that there was, any contracted product address. And, so the reason why, yeah, we suggested this is that at least for one of the examples we know that has like at least some amount of TVL in it, which is the sign finance contract that would solve their problem. 
* Because what they basically do is they use self distract to limit who can call that contract, basically have a contract that anyone can pull, but, because it only lasts, at that address for the duration of transaction and the sense of destroyed, if nobody else can actually call it. so it's basically using this pattern for access control and, and yeah, so that, that kind of functionality would be, unaffected by this change. yeah. 
* And the reason for this that, yeah, basical, well, we have had the different versions and, all of them, we ran into like either a security problem, which is the one where we don't hear the storage, which, was suggested previously. 
or like, the other possibility would be of course to have like fully functional self construct where we contract versioning, by having this column. and, I think that would be, from what I've heard, significantly more complex to implement. I think we had to go at it. and basically it, it, at least for forget, it seems to reach no solution that hopefully doesn't break. 

**Tim Beiko**
* Thank you. okay. There's a first question in the chat, and then we can do Andrew, but, there's a question from Daniel about, if there's pending storage rights in the destructive contract, will those storage right be persisted as part of the contract? Finalization? 

**Dankard**
* Sorry, what is the pending storage? Right? 

**Danno Ferrin**
* So if you're doing a self-destructed, a contract that exists, and before you did a self-destruct, you wrote to one of the storage slots, do those storage slots get committed before the contract is marked as self-destructed? 

**Dankard**
* No. Like the, the storage will be empty. So like, what the client will have to do is have to track all the rights that the contract does, and if it does gets up distracted in that transaction, then the rights will not actually,

**Danno Ferrin**
* This is the case where it's not the same transaction where it's an existing contract and they, in the logic inter code write some stuff as Storage.

**Dankard**
* Ah, okay. I would assume that in that case, because at least the way it's specified right now,

**Danno Ferrin**
* It's, it's not clear the winds testified right now, that, 

**Dankard**
* I would say it is, but we can, if we can happily add another bullet point to clarify this detail, Right, by the way, is fine. 

**Danno Ferrin**
* I just think it should be clarified. Yeah. 

**Dankard**
* Okay. Sure. Yeah, feel free to like add a bullet point on that. 

**Tim Beiko**
* Cool. Andrew

**Andrew*
* Yeah, I think, this, this version, it, hits, the sweet spot be between, reducing complexity and, not breaking too many things. So, I think it's, yeah, it's a great option and, I would, see it for Cancun. 

**Tim Beiko**
* Got it. And do we know,  on your second point about not breaking, too many things, does anyone know, like, if, and what would break based on this? I know we've done a bunch of analyses, but I don't know if we've had one where like we specifically look at like, you know, how much, like, what would potentially break from this. So i will take this as no.

**Guillaume**
* Oh, if, I'm only aware of two contracts that would be broken by just a simple, removal of self destruct and this fixes the, their, so their their problem. So if, yeah, we need to, we need a new analysis to make sure it, this solution fixes it all. But as far as I can tell it's the good enough solution, no one else has, come up saying, this is not good enough for me so far. 

**Tim Beiko**
* Okay. So, and there were two people at least who asked about making this CF5. I feel like what might make sense is to actually make this CF5 for Cancun, to sort of signal that it's happening and then in parallel to that's to, you know, run like, like a more thorough, scan on the chain, you know, with this, potentially with like, you know, a prototype client implementation and, and, and try to analyze, yeah, if anything breaks, that, you know, we did not expect. 
* But I think just yeah, to signal that this is happening to the community and that if somebody's application or contract is affected by it, you know, they might reach out. yeah, I think CFI will will help with that. Does anyone disagree with that? 
* Okay. so I'll make that change, after the, the call. so yeah, the EIP number is 6780. If you wanna review this. And if you are listening and are potentially affected by this, please have a look, to make sure that, yeah, you can raise, you can raise an issue, yeah with us. Anything else on self-destruct? Okay. next up, Alex, you wanted to talk about, making, giving access to the consensus layer state route on the EVM. you wrote, little doc, giving some context, but please, walk us through it. 

## EIP-4788 (context) [38.07](https://youtu.be/RQ2WtyevRXE?t=2287)
**Stokes(Alex)**
* Sure. Yeah. So the doc, Tim dropped in the chat is here and basically is like, you know, just a written form of what I'm about to say, but essentially, I just wanted to get some opinions on a path forward for verifying, SSZ proofs. So there's like kind of two big pieces to this, and the first piece is having some accumulator from the consesus layer in the execution layer. 
* So the way we usually think about this is having like the state route or the block route for each blocker state, you know, have some op code or something that exposes that into the EVM, and then you have this thing that you can make proofs against. that's generally the approach of EIP 4788. yeah, so the thing is though, there's one other thing which is that the way SSZ works is that you basically have these things called generalized indices, and basically they're just like pointers into this whole like verkle tree structure that you need. 
* The problem is that they theoretically can change. And so now the question is like, you know, how do users of the system deal with that change? you know, the straightforward answer is like, the protocol gives them nothing and they just have some governance. But, you know, if you're like a staking pool using this stuff, that's not ideal. Cuz now you need some like governance answer to like, change this technical thing. And, you know, one other option that gets around this is just having say a pre-compile for these things, that could be updated, you know, as we need it to be. 
* And then essentially it becomes, you know, you can imagine there's like immutable, you know, contracts using this stuff because, you know, they just have the changing state behind the pre-compile. 
So, I think for now my question is first, you know, does anyone have any takes on this problem? And like in particular, you know, does it make sense to maybe add a new pre-compile for this generalized index thing? we can instead, so the, so the way we have it right now is with the EIP 4788 that would expose the root and then you could imagine a different preop pile for this generalized index accessor, let's call it. 
* The question is like, do we want to have two print compiles for this? We could imagine in fusing them and just help like a generic SSZ proof verification thing that does it all. or yeah, maybe some other option. So yeah, I wanted to bring this, to the floor and I wonder if anyone has any thoughts on that? 

**Tim Beiko**
* Anyone? Dankrad

**Dankrad**
* Yeah, I would generally before, having some way of getting generalized indexes inside the protocol just to, avoid the upgrade problem. but yeah, I mean it's, it's not gonna be there, there's not gonna be a super elegant solution because it also changes, right? So you, the, the pre-compile will at least have to also take fork versions and I dunno what else to like know for each specific state with how to interpret it. 

**Tim Beiko**
* Okay. Any other thoughts? 

**Stokes(Alex)**
* Yeah, I'll take this for now as just, evidence that no one has any particular preference. And, yeah, sometime later, maybe the next All core dev or the one after that, I'll have some updates for 4788 and maybe I'll also have another EIP for some pre compile here for generalizing. 

## Add getPayloadV3 with builder override flag execution-apis#395 [42.34](https://youtu.be/RQ2WtyevRXE?t=2554)
**Tim Beiko**
* Cool. And sounds good. Next up, Mikhail, you wanted to talk about Add getPayloadV3 with builder override flag

**Mikhail**
* Yeah, thanks. so the,if I understand correctly, during one of the previous calls, there was a, an rough consensus to have this, feature of builder override flag. And, there was an agreement that we want to implement, aristic on the EL side, and it will suggest CL to, switch to local execution,  to block, obtain from local execution engine, rather than like go into builders and get a block from there if we see some censorship is happening. 
* So, I mean, like there is a rough consensus that we want this feature and, this, proposal is in the field of, when do we want it to be implemented? So this, this, particular proposal, creates like a separate document and, makes it in a way that, makes the specification in a way that, it can be implemented separately, from the next work, so right after Shanghai, for instance. yeah, and the main question here is that is, if, there is, any anyone from EL client, teams, who wants to really work on it right after Shanghai and, before Cancun, then  it does make sense to spec it out separately. 
* And, yeah, do it this way. If, yeah, when I'm talking like work on this, I, it implies that, really work on heuristics and really make this feature, enabled not only change the format of the response of the get payload, to, and, step out, this for the next update with the real heuristics. so, and the other option is that nobody wants to, is willing to work on, on it before, say, before cancun. 
* Then it would make sense to not do it separately and just spec it out as a part of, like, cancun, specification. So that's the kind of main question. And this, this, this proposal, suggests that, right, we will do it right high before cancun. I just wanted to bring this to everyone's attention and, if there any opinions right now, so from, your client developers, mostly Great to hear them. 

**Stokes (Alex)**
* I think it'd be nice to have this functionality, the reasons you gave, and if it's as simple as just adding this extra bullying field, that should be pretty straightforward. And yeah, that being said, we don't want to, I think block Shanghai for that change. So pulling it out into like a separate stream makes a lot of sense. 

**Mikhail**
* Yeah, but probably, sorry, go ahead. 

**Tim Beiko**
* I was just gonna ask, is this something that all the clients need to have implemented at the same time? I assume not, right? 

**Mikhail**
* Like No, it's not really. So we can do it really in uncoordinated fashion. Yeah. But if nobody will really implement heuristics, for a censorship that bots has outlined or maybe some else algorithms, before Cancun, yeah, it doesn't make sense, you know, to spec it out like separately. 
* Yeah, I mean, like Prysim and we'll do it. I I, I'm pretty sure about, we need some EL clients, to kind of say that yes, we are willing to work on it as soon as possible and then it makes sense. 

**Potuz**
* I mean, like to To To, wait, wait, I missed the, I missed the beginning. So why do we need the CLS to do anything? I mean, for the cls the change is absolutely trivial, right? We either accept the recommendation or we don't. 

**Mikhail**
* Yep. 

**Potuz**
* So for us it's just a one liner. And for the ELs well, it depends on how much of our heuristics they want to add. 

**Stokes (Alex)**
* I mean, it's probably more than just one line, but either way, you know, one thing you could do is work with like, say Geth, if you wanna write, go and like prototype it out, just like the idea, you know? 

**Tim Beiko**5
* Yeah. So already Marius put out a couple of prs, with, with a proof of concept for one of the two heuristics, which is, forking, fork sensor ship. So, and it doesn't seem to be such a large, such a large line count that list. 

**Lukasz**
* Yeah, I would have to look into like who does what and who can potentially help here. But, I think nethermind can also do it. And like I mentioned on some other call, I'm like a bit, not sure about like coming up with proper heuristics, but I see that there are some, some already. 

**Marius**
* So, I actually think that the EL desks coming up with their own heuristics is really good, because we don't really want everyone to, like if, I don't know if the heuristic can be attacked, we don't want everyone to stop, doing meth stuff, at the same time. So I think if we all come up with our own mechanisms, then,  it's kind of client diversity improvement. 

**Potuz*
* I laid out, two or three, heuristics that seem very simple in the, in the, in the issuer, in the PR, which is just, tell us if transactions are being reorged consistently, if blocks are being invalid when they include particular transactions, or if transactions are being delayed consistently.
*  It'd be nice if someone comes up with something better to add it to that PR or to add it to that description. I can't think of more that I would like to see. and all of them seem to be easily implementable. I'm actually willing to write the prs if the ELs are, go ahead and, and put up, the boolean in the Geth payload. I can actually try to help  write some PRs for something else. 

**Lukasz**
* The Nethermind, we'll pick it up and we'll prototype something. 

**Mikhail**
* Cool. It, it would be great if, if like we can't, yeah, we can definitely come decide something right, right away right here on the call. So it would be great if just the outline will look into it and then we come to some consensus that one or two teams are willing to work on it, with, for Cancun and have, have enough capacity to do that. 
* So in, in one of the next calls. So yeah, doing some prototyping may, may really help to answer this question, whether it's difficult or not. 

**Tim Beiko**
* And I guess, yeah, if we can have one client at least show that, like on the EL side, they could implement something before Cancun, then it makes sense to spec it independently of the fork. But then if no one sort of has the bandwidth, maybe we bundle it with Cancun. Is that what you're saying? 

**Mikhail**
* Yeah, exactly. Exactly that. 

**Tim Beiko**
* Okay. 

**Potuz**
* Are we talking about specking, the actual heuristics or just the specification is gonna be just include the boolean? 

**Mikhail**
* I'm talking about, the specification includes the boolean because if, if, it doesn't make sense, to just add boolean to the specification if no one will really effectively use it. 

**Potuz**
* Oh, I see. So you want this consensus that someone will write some, some non-trivial heuristic and that's gonna be good enough to specify the boolean. what's gonna be specified is only the boolean, right? 

**Mikhail**
* Yeah, definitely. I mean, like, I, I'm trying to understand whether it makes sense to specify this boolean separately from Cancun. 

**Potuz**
* That, that makes a lot of sense to me. Thanks. 

**Tim Beiko**
* Yeah. Does anyone disagree with that? Okay. So yeah, let's do that. obviously we can keep this PR open. And, yeah, as we, as we have more, EL clients, implement things, you know, if that happens before Cancun, we can just, merge it in and otherwise we'll add it as part of the Cancun specs. okay. so that got us through all the stuff we had on the agenda today. 


## Verkle Discussion [52.38](https://youtu.be/RQ2WtyevRXE?t=3158)
**Tim Beiko**
* We can discuss Verkle in more depth, depth, Guillaume if you're, if you wanna give an update now? 

**Guillaume*
* Sure. yeah, so I mean, Verkle's been, going along fine. There's been two testnet that were produced. one of them is called Beverly Hills. and this one is closer to what, well, hopefully Prague would be, which is, just using a Verkle tree without producing the proofs. So of this, on this type of network, you don't need to have any work for, like on the CL side. 
* So that would be, that would be a, for, that would not require any, any change on the, on the CL side. And then there's another net, testnet called Castlin, which, this one uses, like adds the proofs to the, to the execution payload or execution data. so this one is also working Nethermind has just joined the two, the two testnets, last week. I mean the, the last one was today, but, Castine was today, but, the Valley Hills was, last week or two weeks ago. And, yeah, there's been some progress in the performance as well. 
* I think we're only currently 40% slower than, than regular MPT And, yeah, we still have a few things in the pipe, so I'm not saying it's ready to ship in Cancun. but I still get the impression, at least the spec, has been stable. transition is, okay. Still an open question, but, yeah, like  I don't really wanna share stuff about the transition cuz it's, it's improving greatly. 
* I'm Ingrid strides at the moment. so  I hope to share something about this soon, but I don't see why, it would not be ready for another, like, for the next fork, after Cancun, excuse me. 
* Simply because, yeah, I think like most of the questions have been answered over the last two years, and it's just a matter of, implementing. So I understand that for Argon database model is a bit more complicated. But I would say the, the real problem is that people don't look into it. but Nethermind has implemented it in, in less than a year. So I think at this point it's, it's quite clear. 
* It's, it's looking realistic to be shipped in Prague and, and yeah, I don't know if there are questions about the, the current status, but overall, I think it's, it's getting close to ready. 

**Lukasz**
* I have seven questions already. 

**Tim Beiko**
* Amazing. Go ahead. 

**Lukasz**
* Okay. So, have you tested the implementations against reorgs, Against reorgs rs? 

**Guillaume**
* Yes. 

**Lukasz**
* Okay. JSON RPC, does, it does have any degradation in like EH call, things like that, Right? 

**Guillaume**
* So, okay. Jason RPC hasn't been tested. 

**Lukasz**
* Okay. have you tested mainnet ,like blocks? 

**Guillaume**
* Yes. 

**Lukasz**
* Have you managed to do a mainnet shadow work? 

**Guillaume**
* Right. So this is, the problem, I mean, but when you are doing a mainnet shadow for, you're pretty close to the end. it's, yeah. Okay. When you, there's a new decision that has been, okay, there's a new design that has just been decided yesterday. So no, it hasn't been done, but it will be done this month. 

**Lukasz**
* Sorry, multiple client transitions. so we'll be good to have more than one client doing the transition, right. generating things on the transitional reasons fine. Just, just have one client do that. 

**Guillaume**
* No, no, no. Yeah, we should have that, agree. Yeah. 

**Lukasz**
* Okay. That, that will take long time. So it's good to like maybe work on it earlier in parallel, but just, just highlighting problems. And last one, and that is a big one, snap sync for verkle trees. 

**Guillaume**
* No, yeah, there wouldn't be any snap sync for verkle trees. Yeah. It would be a verkle sync. 

**Lukasz**
* Okay. Would it perform compared to Snap sync? 

**Guillaume**
* I mean, yeah. I mean, presumably better, but yes, we don't know until we, we have tried it. Yeah. 

**Lukasz**
* Okay. So quite a few, question marks, right? 

**Guillaume**
* So, No, I, okay. Yes, I'm not, I said it's not ready. I agree. It's getting closer to being ready. I said it's definitely not ready, like it can be shipped in Cancun

**Lukasz**
* No, don't worry. I'm probing. I'm probing where we are, right on the decision when to ship it. Right. And, yeah, I still think it's far away. it's a lot closer than it was like so few months ago, and so, yeah, I'm reluctant to, rush it right until those, questions are, we have answers and we are happy with those answers. So for those questions. 

**Guillaume**
* Fair enough. at the same time, I think that doesn't change what I said. the spec is stable, so it should definitely get more interest than it does now. People should look at it. That's the point. Yeah. 

**Lukasz**
* Yeah. Fine. I'm just a bit, you know, cautious that that's what I want to Say. 

**Guillaume**
* Okay. Fair enough. I think there was five questions. 

**Tim Beiko**
* Oh, you, you want more There? I, I count, I counted six, questions in My notes. Andrew, you have your head up as well? 

**Andrew**
* Yeah, I just, I'd like to clarify, like for Argon as at least my understanding is that it's easiest, for Argon. So, I'm not worried about Aragon implementing Verkle trees. I'm worried about other clients because how I see it like, I don't understand how you can do it without moving to the data model with unhatched keys. maybe I'm wrong, but I just don't get it. And it's the last time when I spoke, spoke to Peter, the Geth is not moving to Geth is still using he keys. So I just don't, maybe Marius can comment. 
* I just don't understand how Gath is going to implement vocal choice with you. They're not moving to Unhatched keys, So you need to rehash. So where, where do you get pre images from? Or you don't need pre images? 

**Guillaume**
* Well, I mean, yes, you need to distribute the pre images, but what happens is, we're looking at a solution where only a smaller number of notes, I mean, talk to Julio about it. He, he has worked on that topic. the, the idea is that, some nodes that do have the pre images typically. Node that do have the pre images, typically arrogant, will share the converter database with other node. 

**Andrew**
* Yeah. that's fine. But, it's still like, yeah. Again,  my point is that for Argon, it is easy, but, other, other clients should, be happy with this, with this plan. 

**Lukasz**
* Yeah. To comment on that,  I really, like, I know that you can verify it and it's verifiable, et cetera, but I like have, an unease on, on this topic too. Right. So I somewhat agree, but this is like,  maybe just, just a feeling that is wrong, but I'm, I'm unease about it as to, get the state from one node, for example. But, how verifiable is that? How easy verifiable is that? 

**Guillaume**
* Well, I mean, that would be very easily verifiable. You just have to check if your data can be reconstructed. but yeah, no, if I, I agree with you that this is not, the my favorite, method, either, sorry, either, but that does, that seems the, the simplest at this point, although I might change my tune in, just a couple days. yeah. I'm actually lost, I lost the point of your question. Could you repeat your question? 

**Lukasz**
* Sorry, was it really a question? Just was a comment more so, Okay. 

**Tim Beiko**
* Yeah. That's relying on Argon only the distribute at the database is, yeah. 

**Andrew*
* What I was also thinking, is that we can have a, a special small, sub protocol for, for just pre images. we, and, we can implement it  argon, and then our other clients can just, just, get, the pre-images they want. but it's we need to test that. 

**Guillaume**
* Sure. just to address another comment, I like so far, the best implementation we have is with Argon. I never said it was only going to be Argon that would do this. It makes sense that everybody tests, like everybody tries to produce the same, the same image and needs to, to verify that, that it matches. 

**Lukasz**
* So Nethermind  is in the process of, reworking at state db, and we have actually two streams, one, like more, more proven to, to, to work and one very, very, experimental. So I think we would be after we, if we managed to ship it and we can ship it this year, question when this year, we might be able to do that migration more easily. 
* But yeah, this is still an open question. we also, this more experimental layout, it's also done in this way that then later could be, with lot of changes applied to, Verkle trees. So, it's called pubarchive. The one is interested and it's, direct storage of the Patricia verkle tree on the disc using the, mapped number mapped files in a way. So, there are some good docs being produced by Shemon, so if someone wants to check it out, I encourage. 

**Tim Beiko**
* Thank you. Any other questions, thoughts on Verkle trees? Okay. I know Guillaume you said not to ask about this, but I'll try anyways, but I'm curious if, even if you don't have a full spec yet about the transition, like if you can share just a bit about your thinking about that and the, maybe like the trade offs and, and, yeah, just because we have plenty of time now to talk about our Verkle, so it's probably worth going over as as much of it as we can. 

**Guillaume** 
* Yeah, sure. I mean, once again, I'm about like we're, we're having some results start coming in that, might make us change our plans. but so the idea is that indeed, because so far the translation was taking so much time, you have to rehash everything, that, I mean, except Argon, that you have to do it offline, like you need some powerful machines to do it. And, from our benchmarks so far, to be updated soon, it takes about, yeah, 18 hours in, the case of, of Argon, and much longer for Geth to produce, to produce a conversion that then is sent all over the, like to all the, all the clients on the network and well more exactly, all the clients on the network download it, and they start replaying blocks on top of this conversion and catch up with the, with the MPT head. 
* And they have to do this before a given four block. And at the four block, the mpt, is no longer dated as jettison. And, the verkle, state becomes the, the official state. so yeah, that's roughly the plan so far. we are having some, yeah, okay. Now I don't really want to talk about this yet because, it sounds too good to be true. but yeah, the idea is that we would somehow be able to ensure that everybody, is able to do their conversion themselves. but currently with, with all confirmed benchmarks, this is not realistic. So we need to help, like the, some very powerful nodes need to help less powerful nodes to do the transition. 

**Tim Beiko**
* Got it. So, and, and, okay. And so at least, I guess the, the thing I was worried about this, the earlier specs of verkle trees required like, the network to stop producing blocks for a while or, or something like that, but with this spec, you would not have this issue, correct? Like you, obviously you need to figure out the way to do it efficiently, but you're, you're sort of swapping in the background from the verkle, the, the verkle Patricia try to the verkle try, when the fork happens, but yes. 

**Guillaume** 
* Okay.  Got It. Yeah, it has never really been, seriously considered. It's, was more meant like a joke. Maybe there was a joke that was too catchy, but, yeah. 

**Tim Beiko**
* Yeah. But yeah, yeah, it wasn't clear that there was a, an easy way to do it without downtime basically. And so I just wanted to make it clear that, there is, or wouldn't necessarily call it easy, but there is a way to do it. 

**Guillaume** 
* Yep. 

**Tim Beiko**
 *Cool. Any other questions? Oh, there's, okay, there's a questions about do zkEVM Evms make verkle tries redundant and the, yeah, I don't know. Do you wanna take that? 

**Guillaume** 
* I don't know. zkEVM is closer to a connection. My understanding is that yes, zkEVM, the long term, plan is to get rid of, like to replace verkle trees with, with a zkEVM, like construct. I don't think, it will be made completely redundant because some of the choices we have are specifically designed to be zkEVM friendly. but yeah, that's just my understanding. I don't have, yeah, should be able to answer that better. 

**Dankard**
* Can you hear me now? Kind of so yes, like a full zkEVM that can in a decentralized inner fashion, prove in like, say a second that a block is correct would indeed make verkle trees like not necessary, but I think we are quite a few years from that. I'm willing to be proven wrong, but that is my current assumption that yes, like, I mean ZzkEVM are coming, but like they still have much higher latencies. 
* They also have massive prove costs. So I kind of have my doubts that they would currently Geth say a majority from the score, like say, oh, it's okay to just rely on them, to know whether L one blocks are valid. So, so far I think you still need zkEVM. 

**Tim Beiko**
* Got it. Any other questions on verkle trees? Okay. any, anything else anyone wanted to bring up? Okay, well, yeah, then I guess we can wrap up. So, we'll move the self destruct EIP to CFI. and I think, yeah, if in the next couple weeks people can review the stuff around EOF, the, the 4788 and the other, beacon State proposals, and look at SSZ as well, we can continue those conversations, on the next call. 
* And the next call, I believe will be right after Shapella. So, yeah, last time, I guess this is a time for users to upgrade and, we'll go over how the fork on the next, next one of these. yeah, guess we can wrap up. Thanks everyone and see you on the CL call next week. 
Thank you!

-------------------------------------

## Zoom Chat Highlights
**Tim Beiko:** couple of things today. Quickly. You'll go over Shanghai and and and that which is a plan in the next 2 weeks. But then most of the call we've got some big updates on pretty much all the largest potential eips for cancun. So we can. 

**Pari:** We have the last shadow for plan for next week. It'll go through the transition either Tuesday or Wednesday, and the ideas that release are up and running there, and we can test the transition with relays. 

**Pari:** If someone wants to test the least they're planning to have in the next couple of weeks, let me know otherwise. I'm just going to use the recommended uses.

**Phil Ngo:** Load Star has a 1.7 point 1 out. It's a minor update for people using Gly.

**Phil Ngo:** for testing with loadstar. We may also do a minor bump with a fix for our Bls Pool, but that's it.

**Tim Beiko:** Okay. But the 1.7 not always still is still correct. If people just want to keep that correct.

**Danno Ferrin:** What are the design decisions calls for adding a field into the transaction. I'm. Interested to solicit, the opinions of the other core devs of their appetite for that addition is, it's feel good, feel bad, great awesome, you know, some sort of a signal, as if whether or not this is the right direction, they would expect, a transaction like this to move in.

**Tim Beiko:** if we push Eo F out of cancun, and you know potentially do it in the fork after you know, that also means we might push something like Merkel out of the forecast, or do it in the forecast for that. Potentially, we could do them together. But you know that's risks

**Tim Beiko:** you know there is some overhead to like having these forks. We can try to keep it minimal, and and you know not have too many other things. But we don't. We don't sort of get a fork between Eo f, and or between, like you know, cancun and pride for for free right, like it just means we prioritize. Ef, before whatever we would have done next, which is, which is fine.


-------------------------------------
### Attendees
* Tim Beiko
* Danny Ryan
* Pooja Ranjan
* Mikhail Kalinin
* Marius
* Wesley
* Barnabas
* Saulius
* Danno
* Lightclient
* Pari
* Ethan
* Mario
* Tomasz
* Oleg 
* Kasey
* Marek
* Crypdough
* Fabio Di
* Terence
* Andrew
* Roman
* Marcin 
* Pop
* Guilaume
* Protolambda
* Carlbeek
* Mike
* Gajinder
* Stefan
* Hsiao-Wei
* Josh
* Phil Ngo
* Alexey
* Holger Drewes
* Dankrad
* Guillaume
* Proto
* Holder Drewes
* Stokes
* Peter Szilagyi
* Sean
* Micah Zoltu
* Jiri Peinlich
* Marius Van Der Wijden
* Potuz
* Evan Van Ness
* Moody
* Tynes
* Alex Beregszaszi
* Marek Moraczyński
* Justin Florentine
* Ben Edgington
* Lion Dapplion
* Mrabino1
* Barnabas Busa
* Łukasz Rozmej
* Péter Szilágyi
* Danno Ferrin
* Andrew Ashikhmin
* Hdrewes
* Crypdough.eth
* Ameziane Hamlat
* Liam Horne
* Georgios Konstantopoulos
* Mehdi Aouadi
* Bob Summerwill
* Jesse Pollak
* Stefan Bratanov
* Sara Reynolds
* Caspar Schwarz-Schilling
* Ahmad Bitar
* Marcin Sobczak
* Kasey Kirkham
* Sean Anderson
* Saulius Grigaitis
* Ruben
* George Kadianakis
* Dankrad Feist
* Andrei Maiboroda
* Gcolvin
* Ansgar Dietrichs
* Jared Wasinger
* Diego López León
* Daniel Celeda
* Trent
* Mario Vega
* Kamil Chodoła
* Ziogaschr
* Kevaundray
* Antonio Sanso
* Oleg Jakushkin
* Leo
* Nishant Das
* Pote
* Sam
* Tomasz K. Stanczak
* Matt Nelson
* Gary Schulte
* Rory Arredondo

-------------------------------------

## Next Meeting
April 13, 2023, 14:00-15:30 UTC



