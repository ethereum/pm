# Execution Layer Meeting #195
### Meeting Date/Time: Aug 29, 2024, 14:00-15:30 UTC
#### Meeting Duration: 77 min 
#### [GitHub Agenda](https://github.com/ethereum/pm/issues/1142) | [Video of the meeting](https://youtube.com/live/HJ9WxAOwTTA)
#### Moderator: Tim Beiko
#### Notes: June 

| S No | Agenda | Summary |
| -------- | -------- | -------- |
| 195.1 | **Pectra Updates** | Devnet-2 and Devnet-3 updates
| 195.2 | **EIP-7702 Updates** | Update [EIPs#8832](https://github.com/ethereum/EIPs/pull/8832)
| 195.3 | **EIP-7702 Updates** | Update [EIPs#8835](https://github.com/ethereum/EIPs/pull/8835)
| 195.4 | **EIP-7702 Updates** | Update [EIPs#8833](https://github.com/ethereum/EIPs/pull/8835)
| 195.5 | **EOF** | [EXTCODESIZE and DELEGATECALL issues](https://hackmd.io/@frangio/S1VvatXiR)
| 195.6 | **EOF** | Devnet updates
| 195.7 | **EIP-7251 Updates** | [Consensus-specs#3882](https://github.com/ethereum/consensus-specs/pull/3882)
| 195.8 | **Engine: unify request objects** | [execution-apis#565](https://github.com/ethereum/execution-apis/pull/565)
| 195.9 | **Pectra EIP proposals** | [EIP-7623](https://eips.ethereum.org/EIPS/eip-7623)
| 195.10| **Pectra EIP proposals** | [EIP-7742](https://eips.ethereum.org/EIPS/eip-7742)
| 195.11| **Pectra EIP proposals** | [Raising the blob reserve price](https://github.com/ethereum/EIPs/pull/8849); [Ethereum Magicians forum](https://ethereum-magicians.org/t/eip-7762-increase-min-base-fee-per-blob-gas/20949)
 
#### Introduction
**Tim**: Okay, we are live. Welcome everyone to ACDE#195. I'll put the agenda in the chat here there is a bunch of stuff to go over today: updates on the devnets, lots of specifc updates or proposed changes for 7702, one issue that was brought up around excode size and delegate call, and then getting some updates on the devnets there and then lastly there were two more proposals for changes related to the stuff that's already in pectra so one for EIP-7251 and then one for the engine API.

Assuming we get through all of this, there there is three proposals that we have on the agenda. The first is 7623, which we CFI'd for pectra already increasing the call data cost in certain cases. The second is 7742 which is about having the blob count only set on the CL side; we discussed this last week on the CL call. And then lastly, there is a pre-EIP idea around raising the reserve price for blobs. So hopefully we have time to get through all of this.

Maybe to kick us off, Barnabus or Pari, do either of you want to give us an update on the current state of devnet-2 and what the plans are for devnet-3?
<br>
<br>

-------------------------------------
### 195.1 | Pectra Updates ([2:50](https://www.youtube.com/live/HJ9WxAOwTTA?si=Q6RpLK4xTwUNwCPt&t=170))
**Parithosh**: The current state of devnet-2 is pretty much still on the interrupt channel; we haven't been able to recover the network. There was a Geth bug last week that's since been patched, but that has led to atleast one or two other bugs: one in Prysm and the other one in Teku. If someone from the teams there, maybe they can briefly go through what the bugs are? Or if they are still active? Atleast the Prysm one, they said they were able to narrow it down, but I think the Teku one might still be actively under triaging. Either way, we haven't been able to get the network back up and running, but at this stage I think we're just going to leave it at this level and figure out what the bugs are. We're waiting on client teams to pass all the tests before we can launch the next network, devnet-3. 
<br>There was a spec test release yesterday by Mario. I think if Mario is there, maybe he can quickly speak about the spec test?

**Mario**: There's not much to talk about; there are a couple of interesting test cases there, which I think should be clarifications in the EIP. If no one else is working on it, I will try to make a PR to the EIP to make these clarifications, but other than that I think it is just 7702-focused release. 
<br> I think the release is passing because we filled the test with them; Reth yesterday sent a message that they were passing on our EVM, but they have to port it to Reth. The rest of the teams, I think, are working on it, but if you guys have any updates, it would be nice to know. 

**Parithosh**: I think Oliver mentioned that they've done it and they have a branch ready for us to use. We are waiting on client teams to pass the spec test and then once they're ready we're ready to launch the network--that's the current status.
**Tim**: Got it, we won't relaunch devnet-2, we'll just launch devnet-3 once we have confidence that all the new test suites are passing.

**Paritosh**: Exactly because most of the issues that were triggered in the devnet-2 were 7702-related so there was no real reason to fix it.

**Tim**: In terms of the spec changes for devnet-3, I saw there's a doc, but are there any other notable additions? 

**Parithosh**: The only big change is 7702 and on the CL side we've done a few changes with the consolidation bug, etc. But as far as the CL side is concerned, those changes were decided weeks ago and nothing has changed there. On the EL side, we've switched to pinning to a specific spec-tech telease version. I will update right now to whatever Mario released last night, but essentially if you're passing spec test, you're probably ok. 

**Tim**: Any other updates, questions concerns about devnet-2 or path toward devnet-3?

|| **Chat**
- Richard Meissner: 7212 is not considered at all for devnet-3, right?

**Tim**: No, 7212 is not considered for devnet-3.

**Tim**: I assume, once we get all the teams passing spec test, we'll launch devnet hopefully in next week or so. Is that realistic? Is there a team that thinks, say by next Thursday, they could not be ready to launch devnet-3?

**Tim**: Okay, sweet. Let's continue chatting on this as we fix the bugs on Discord, but thanks a lot Pari and thanks everyone for the work on all the implementation.
<br>
<br>

-------------------------------------
### 195.2 | EIP-7702 Updates: [EIPs#8832](https://github.com/ethereum/EIPs/pull/8832) ([7:05](https://www.youtube.com/live/HJ9WxAOwTTA?si=5O-aFCjgYuDYRxuO&t=425))

**Tim**: Okay next up, 7702. So we have three open PRs on it that I want to make sure we discuss and then potentially make a call on, including in devnet-3, if we decide to.
The first is around behavior in self-destruct in 7702 by Sudeep. Do you want to give some context on your PR?

**Sudeep**: That is just a clarification being included in the EIP and the execution spec test is already following that behavior, where we restrict the self-destruct of EOAs; so just a clarification being added and I think there's a general acceptance to it.

**Tim**: The execution test that Mario just shared, the last version which is already in devnet-3 followed this behavior, correct?

**Sudeep**: Yeah.

**Tim**: Any questions, comments on this?

**Tim**: Maybe we should just have it in the list for clarity; I don't think it's part of the devnet-3 specs, so I would just add this one as well to make it clear, especially if it's already in the tests.
<br>
<br>

-------------------------------------
### 195.3 | EIP-7702 Updates: [EIPs#8835](https://github.com/ethereum/EIPs/pull/8835) ([8:40](https://www.youtube.com/live/HJ9WxAOwTTA?si=J4F1LTJf77gt_Tf_&t=520))

**Tim**: Ok next up, Etan had two PRs. He is unfortunately not on the call, I'll go with the first one which was about changing the signature domain for 7702, so using 0x1a instead of 0x05. Basically in his post he explains that this would allow future transactions types to use 0x05 and then if we ever get past 0x18 we already have some issues because 0x19 is already allocated. I don't know if anyone's reviewed this or has strong opinions. lightclient commented that he was indifferent but generally in favor. Anyone else have thoughts on this?

|| **Chat** 
- Peter Miller: It seems very sensible

**Tim**: I guess if we did do this, do we want to do this for devnet-3? It's a pretty small change but I assume it affects a lot of different parts of the code base.

|| **Chat**
- lightclient: I think we should wait to do this

**Tim**: Okay there's one comment about waiting. Daniel?

**Daniel**: I wanted to say the same. The change in the account base I assume for everybody is very small because it's just changing a constant, but we have to change all the spec tests because all the signatures are changing; so I don't know how much work this would be. 

**Mario**: It shouldn't be that hard; they should be dynamically updated once we update this one constant. It should be one line. But yes, the filling process, it takes an hour. That would be the longest wait I think.

**Tim**: So would people agree that we should do this change but plan it for devnet-4, is that reasonable?

|| **Chat**
 - Jochem-brouwer: 1 hour to fill
 - Barnabus: I wouldn't extend the scope
 - Stokes: Medium agree
 - Barnabus: We have plenty of other future devnets where this could be added to
 - lightclient: Would like to look a little more into sig prefixes ppl are using across the ecosystem, but I assume it's okay

**Tim**: Ok, lightclient says he wants to look a little more into the prefixes, but generally assumes it's ok. In that case, let's not do it for devnet-3 but let's leave the PR open a bit more for people to review in the next week or two and  when we're scoping devnet-4 we can formally add this in. If there's any concerns people can debate this on the PR.

|| **Chat**
 - Oliver (Reth): We're indifferent to the change but would like to not do it for devnet-3
 - Mario: devnet-4 sounds more reasonable though
   
<br>
<br>

-------------------------------------
### 195.4 | EIP-7702 Updates: [EIPs#8833](https://github.com/ethereum/EIPs/pull/8835) ([11:45](https://www.youtube.com/live/HJ9WxAOwTTA?si=cs4PHgcOuzfG1OJS&t=705))

**Tim**: And then last 7702 PR, this one was by Dragan, which wanted to restrict the chain ID to either valid existing chain IDs or zero. Dragan, are you on the call?

**Dragan**: In general, currently we are having that check inside EVM, I want to move that check outside EVM and for it to be validation of the sectionability. We already have some checks on the signature and this would be one additional check on chain ID. It would make any authorization list that has authorization with chain ID that's different from current chain ID or zero be 'invalid'. 

**Tim**: Any concerns or objections with the general proposal? If not, one question I have is, are there some cases where testing this could be more complicated? 

**Dragan**: There will be need for some test just to cover this case, which is why I would like to do it after devnet-3. But this is a very localized and small change to be honest. There are some tests -- I think Mario would be better to say this-- but there are some tests that are covering different chain IDs inside the authorization list, those need to be changed, and one or two tests need to be added to check this case.

**Mario**: Yeah i agree, while it seems easy enough to test, I wouldn't include this in devnet-3 because it needs additional testing. Should be small enough though.

|| **Chat**
 - lightclient: I don't think we should make the validity of the tx based on the validity of the auth list
 - lightclient: We already have auth validations right, for instance nonce is uint64

**Tim**: There is a comment by lightclient saying that we shouldn't make the validity of the tx dependent on the validity of the auth list, but maybe there, one question I'd have is that previously we just cared that this was a 256 bit integer, we already have some restrictions on this. [To lightclient] I don't know if you have access to a mic, but it might be good to just expand that a little bit.

**lightclient**: I think in general constraining the inputs based on a data type integer is different from constraining the input based on chain data, fork configuration data. So, I don't feel like we should be combining the fork data into this kind of serialization logic of the op list.

**Tim**: Got it. 

**Peter**: Yeah there's a difference between things that are invalid because they can't be deserialized and authorizations that could be deserialized but then aren't valid as authorizations. If someone on Ethereum gives you an authorization with chain ID 3, you could deserialize it, but it's not a valid authorization. It doesn't authorize anything.

**Dragan**: This is very similar to what we're doing with transaction signatures. Basically, make it invalid if S is more than half of the field and if the V is not in correct format. So it's not different from having those checks.

**Tim**: Right, but those checks are based on data types otr data constraints, less than domain types-- is that correct? I assume the signature data is formatted the same across all the chains and we want to check that it's a valid format, but that's different than checking that it's a valid signature on this chain, for example.

**Dragan**: Authorization lists enables us to have those checks on EVM. For the signature on the transaction level, that was not the case, that's why we have option to make those checks inside EVM but what I'm arguing is that we shouldn't do that. We should do it when we are deserializing the lp and making those checks before. To not have invalid data inside the authorization list, not just invalid but data that we can check easily that we know is not going to pass.

|| **Chat**
 - lightclient: I don't think we should make the validity of the tx based on the validity of the auth list
 -- Yoav: Definitely. As long as the sending EOA can pay for it, the transaction is valid. Otherwise, we get a new DoS vector - N transaction using the same authorization, which can be invalidated in O(1)
   - Thanks, that's a better way of saying it  
 - lightclient: We already have auth validations right, for instance nonce is uint64

**Tim**: Does anyone else have strong opinions on this? 
<br> Yoav has a chat comment saying that otherwise if we do this change, there's a potential DoS vector where we have N transactions using the same authorization, which can be invalidated in O(1). Yoav, do you want to maybe expand on what you see as the issue here?

**Yoav**: Just acknowledge what lightclient wrote about not making the validity of the transactions dependent on the validity of authorizations, because as long as the EAO that's in the transaction can pay for it, the transaction is valid. It should be included even if the authroizations themselves are invalid because otherwise you could have a DoS vector where you send a large number of transactions, all of them using a certain authorization, and then you can invalidate the authorization with a single transaction and cause many transactions to become invalid after propogated. So the validity of the transaction should only depend descending EAO, not the authorizations. It's okay for authorizations to fail, the transaction is still valid. I think that is what lightclient meant.

**Dragan**: Just want to address the DoS claim-- I don't think that is valid because even when you receive the section you still need to do recovery of it to check the section work, to do recovery; it's a lot bigger than just iterating on authorizations list.

**Yoav**: I mean the authorization can become invalid because it is nonce dependent, right? If you send 1000 transactions and all of them have the authorization and after the nonce gets incremented, all of the transactions except one becomes invalid.

**Dragan**: That's true, but what we are talking about now only for chain ID not about nonce and not about if the sign is valid or not valid. We're talking about chain ID.

**Yoav**: That's fine, about chain ID that's fine. I thought that what lightclient meant was about the validity in general and I think the validity should not depend on the validitiy of authorizations. These authorizations just won't work but the transactions will still go through, does that make sense?

**Dragan**: Yes, but that is not what we're talking about now. We are talking just about chain IDs.

**lightclient**: I don't understand what the difference is. I thougth that we were talking about the validity of the transaction.

**Peter**: As I understand it, what we're talking about here is at some point we have to check that the chain ID of the authorization is valid. I.e. it's either the current chain ID or it's 0, so it's valid on any chain. The question is: should that check happen before accepting the transaction-- if the authorization of the chain ID is invalid the entire transaction is non-includable-- or should it happen after the transaction is accepted so the transaction is included in the chain and I assume it then immediately fails because the authorization is invalid? My feeling on this is it probably doesn't matter because transactions that include, you know, if you have a transaction for chain A that includes an authorization for chain B, that transaction is trivially malformed under some trivial static check that doesn't require you to know anything. It's obviously wrong so anyone who signed such a transaction has already screwed up really badly and I'm expecting that it will basically be impossible to create these sorts of transactions using any sort of standard tooling. It's not a mistake that people are goin gto make in reality. On the other hand, the check is so trivially cheap if we say reject the entire transaction if the authorization is invalid. 

The only concern I would have which would lean me against this us that currently all of the checks you have to do to make sure that the authorization is valid are completely chain agnostic. Either the RLP bytes you get given are an encoding of an authorization object or they're not encoding of an authorization object and the only check you have to do is you decode it with the RLP and if your RLP decoder throws you an error then it's invalid. Whereas, what this does is it makes the validity of the authorization makes the authorization invalid depend on the chain ID of the current chain. It adds a little complexity whereas we're going to check the entire authorization any in a minute after we've accepted the transaction.

|| **Chat**
 - lightclient: clients are free to drop these txs in txpool if they like
 - lightclient: it should happen after, that's what Yoav was also saying
 - ansgar: this seems like a pretty detailed question, not sure it warrants acd discussion
 - - tim: Yes, assuming there's no clear consensus now, I'd ove this async, given it only would be included in devnet-4 or later
 - lightclient: I don't think it's that cheap. It requires us to actually analyze the auth list
 - frangio: you could see the chainid check as 'chain agnostic' if it's just checking for coherence with the 7702 tx's own chain id?

**Tim**: Ok, I think clearly there's a bit more thinking to be done here. Because this is not going to be added to devnet-3 it's probably fine to move this conversation async, so there's a PR there. In the next ACD we can follow up on it, if it's not merged or closed by then. 

<br>

-------------------------------------
### 195.5 and 195.6 | **EOF** ([24:45](https://www.youtube.com/live/HJ9WxAOwTTA?si=DDvLrRoZ_70lwrgw&t=1485))

**Tim**: EOF, Francisco Giordano (Frangio) put together this doc with some concerns for EOF, especially with how it behaves with regards to token transfers for NFTs. Do you want to take a minute to maybe walk through your doc and what the concerns are. I know it's been discussed a bit on the Discord in the past couple days as well.

**Frangio**: First, as a preface, I'm very excited about EOF improvements to static analysis and code generation, so I feel like that's important context. I think these are just improvements to make. So, I do have these concerns that come from the application layer. ERC 721 and ERC 1155 are the two major NFT stanfards and essentially they need an IS_CONTRACT operation because of some behavior that they have on transfers. So when a token is transferred to an account, if the receiver is a contract, it has to explicitly declare that it supports receiving this token by implementing a call back and the token transfer will invoke this call back and expect some special value in return. This is only done for contracts so if the receiver does not have any code, it's assumed to be an EOA and the token is transferred without calling any call backs. So the purpose of this check is to prevent the loss of tokens which are transferred to contracts that can't handle them. This is an error that happens a lot, so it's kind of debatable: does it belong in the EVM or not? The fact is that these two ERCs, which are final, already specified they require this operation so what that means is that in EOF, which does not have EXTCODESIZE or EXTCODEHASH, it is not possible to implement this. The current proposal is to work around that by dispatching to a legacy contract as a sort of escape hatch to get EXTCODESIZE. This is possible, this works, but it is a bit of a hurdle for library authors because now they have to hardcode this address in the code that they ship to users. We as an ecosystem have to make sure that those addresses are widely deployed and available everywhere, which in itself is it's own issue because there's no 100% reliable way to get deterministic addresses across all chains. There's also the problem of development chains on users' local computers which also have to have that, so it's a big issue. In my opinion that needs to be addressed just in EOF. the fact that it can be worked around in this way so easily, and also that these two main standards require that, so it is going to be used widely. This sort of escape hatch mechanism, to me just says, why don't we just enable these up codes EXTCODESIZE or EXTCODEHASH in EOS and just fix that so that all of this work around is not required.

The other issue that I describe in the notes here is regarding delegate call. So EOF contracts cannot delegate calls into legacy contracts. This, in my opinion, realistically cause some contract bricking situations that could become a new parody wallet situation where a proxy that is working perfectly is accidentally upgraded from an EOF contract to a legacy contract and then it becomes unusable, completely frozen. It will require some sort of, well, or no recovery at all would be possible. It's not really clear why this limtation is in place; I think it's about avoiding things that are not supposed to happen with an EOF contract, for example related to self-destruct. Recently, there was a proposal for 7702 to change the behavior of self-destruct in that context, there's now a discussion to apply it in EOF as well and to lift this restriction to allow delegate calling into legacy contracts that would prevent this situation.

But, this is sort of related to the previous issue because if we had EXTCODEHASH we could implement at least a check to prevent the situation in the code itself to see if the target that we would be delegate calling into is EOF or not by using EXTCODEHASH behaviors, which just allows you to detect that. These are the two issues that sort of related to EXTCODESIZE and EXTCODEHASH and delegate call is it's own discussion. We've been talking about this in the EOF implementer's call but so far no change has been made and we're sort of heading toward the status quo. I think it would be better to make a deliberate decision with convincing arguments as to why choose one thing or the other. I'm happy to hear any opinions.

**Danno**: So, we've got a couple restraints working with EOF to get it to ship. One of them is there was feedback given from multiple people in ACD that we should strip absolutely everything that is not absolutely necessary to ship it, and we come back in future releases and add those features in. So any feature that did not involve breaking something that could be added additively in the future hard fork is something we made conscious decision not to put in to reduce the scope and the testing impact of EOF. This is one of them, how to detect a contract, we can add that with IS_CONTRACT, or unlocking the old op codes in a future fork. There's also a coupleof other features: TXCREATE, which allows us to create new EOF objects arbitrarily from transactions, was also removed; as well as consideration for EXTDATACOPY, which allows us to copy data from other EOF contracts. Those were pulled becasue those can easily be added in the next hard fork; we can add those op codes in without breaking you away, without invalidating any other contracts. So that's been our guiding northstar for EOFv1 for what goes in and what goes out. While this issue with building 721 or 1155 contracts in EOF, it does kind of prevent it right now from following the specs, but it doesn't break anything outside of EOF. You can continue to write these contracts in legacy and we can add these op codes in the next hard fork and then you can start writing them in EOF. So that's been our philosophy of why we chose the status quo, but if we get feedback from ACD that it's important to fix now then we'll work harder on the consensus as the EOF implementers call to get it released. But my overriding concern is ACD already concerned about the size of this release as it is.

**Tim**: I guess maybe in that case, assuming we did add those more features in a future version, if something did get bricked through some weird update like we were just talking about, is that something where then exposing that functionality in EOF allows you to make the same calls you make in legacy VM and therefore sore of unbrick the contract?

**Danno**: So that's the case with the delegate call limitation. We already put that in, mostly it was around self-destruct, but generally it's around any feature / operation we ban inside of EOF. Self-destruct is the most easy one to demonstrate but when it comes to the other op codes that we're banning in EOF, as Frangio pointed out, you can just do a regular non-delegate call to get EXTCODECOPY and pass it in as return data. So a lot of those have non-delegate call solutions, I think only the self-destruct and the side effects are what is impacted by it and we didn't want to propose changes to self-destruct. But with 7702 that cat's out of the bag. 

You can write you proxy contract to do the EOF detection via those jumper calls if you feel it's important to have your proxy in EOF, but I think until we get these features, you shouldn't write a proxy in EOF. Those will come down the line and we'll get those addressed.

|| **Chat**
 - Ansgar: To make what Danno just said extra clear: it's much better have EOF start overly restrictive, because it is always possible to add (back) functionality in later forks. In contract, to ever remove functionality, we would need a new EOF version. But of course, if we already know we want to add something later, might be better to have it now, otherwise the early EOF contracts can't use it.
 - Hadrien (OZ): This feels like << we are going to ship something and we don't care if devs are not going to use it, they'll use the next version >> Personally not a fan of that
 - Ansgar: yes, it's a bit unfortunate, it's caused by EOF being sequeezed into this fork, so we can't give it all the room it should ideally get
 - stokes: Can we move it to the next fork? And give it the room it deserves?
 - Danno: Not with verkle in the same fork, too big
 - Ansgar: "EOF next fork" is a meme
 - lightclient: peer das this fork is a meme

**Frangio**: I feel like there's a significant difference between something like TXCREATE, which is an actually new thing, versus something like EXTCODESIZE where it's not a difference from legacy contracts. In my view, we're making all this effort to shape EOF now. While removing stuff is good, it's also good to make it useful and ensure adoption so that all of this effort pays off. My concern si that with these limitations, it's going to really harm this adoption in language and libraries and we're not going to really kind of reap the benefits. So in the direction of like reducing it as much as possible, the simplest possible fix would be to just enable EXTCODESIZE and I think that would be a much better situation for EOF to get adopted.

**Ben**: Probably CODEHASH also because then you can actually detect it's an EOF contract, specifically. Whereas you can't do that with CODESIZE alone. CS would say, 'oh it's two bytes,' but that doesn't tell you it's EOF two bytes-- if you're worried about proxies detection.

|| **Chat**
 - Ansgar: What is the case against adding 'IS_CONTRACT' and 'EXTCODETYPE' now? seems like they are minimal complexity features
 - Tim: We can add it in gradually. eg. ship EOF as-is in the next devnets, and see what the diff is to add mores
 - Ansgar: Hadrien has a point though. Do we want all the smart contract devs to move over or not?
 - Tim: Right, but if testing scope if the concern, maybe it makes sense to gradually extend EOF across more devnets once we see a version that's stable
 - Ansgar: yes, but then we should ideally still already have a decision about eventual scope
 - Yoav: One reason to avoid IS_CONTRACT is the way contract checks are currently abused by certain contracts, which delays AA adoption. Long term we prefer not to have different flows for EOA and AA.

**Danno**: So one of the things that we're developing in the EOF implementers-- we don't have the PR out yet-- but we're contemplating an IS_CONTRACT op code. One of the design options is to have it return 01 or 012. 0 for EOA, 1 for legacy, and 2 for EOF. So in one op code, we solve both of these problems. But still there are other design issues we want to make sure we're covering space and not pulling back on some of our commitment to remove code introspection because if we just blindly turn on the EXTCODEHASH, EXTCODESIZE, EXTCODECOPY--well we probably don't need copy but I mean if we're removing the other EXT codes there's going to be a lot of pressure to say 'well why don't you just do code copy' and all of a sudden we're needing to keep all the old byte code or atleast metadata about the byte code as was originally implemented, which is going to make things difficult for ZK systems because they need to keep extra data. There's already issues around that anyway with calculating the addresses. So we're discussing this in our chats and I mean if it was as simple as just flipping an op code or implementing one other thing, I'd be more willing to push the rest of the implementers to a solution, but I think one of the big issues is we don't have the exact solution that's going to solve all of our commitments and fixing in a subsequent fork gives us the space that we need to make sure that we're doing the right thing not necesarily the time-forced thing.

As far as, if we're shipping something that devs can't use-- 90% of contracts never need to know that you're calling an EOF or an EOA. The exception is the 1155s and the 721s. But if you're calling Uniswap, the callbacks work. A lot of the contracts and smart contract use cases that go with this, these features are not essential and their not breaking. We're covering 80-90% of the people who could use it. You could deploy Uniswap today and not have any of this concern.

**Tim**: So I guess maybe one related thing to think about--how far along EOF is now and what the difference is to add these features and over what timeline--there's clearly a design space to explore here whereas we've been exploring the rest of the design space for quite some time now. So I don't know if Danno is the right person to give this update, but in terms of EOF devnets, where we are now, how stable are the impleemntations, and then what do you think it would take to add these op codes?

**Danno**: The big issue for the op codes, aside from coming to consensus on what the correct solution is, is we need to write tests for them. That is a couple of days to write the tests, then all clients would need to implement the codes and conform to the tests. As far as devnet-4 readiness, we're at least two weeks out. The clients aren't 100% on tests right now. Every client has at least one test that their failing. Some of them it's because some of the specs have been changing underneath it a bit and they had implemented it to a spec that was correct a year ago. Plus the work on 7702 is taking a lot of the engineers time right now; things are getting basically designed on the fly and it's taking a lot of their time to reimplement these changes. 

As far as readiness, we can be ready for when devnet-4 ships. Adding the op code would push us back probably about a week for devnet-4, at least.

|| **Chat**
 - Marius: 2% of contracts is like 1.2 million contracts :D
 - Jochem-brouwer: BTW we also need EOF <-> 7702 tests since these interact somewhat
 - Frangio: uniswap itself uses ERC-155

**Tim**: Okay. My sense is that given EOF is already such a huge huge change, I would lean toward integrating the version that we're already testing throroughly as a first version in devnets before we add anything more. Then potentially in parallel, start targetting an EOF extension that we could potentially add in devnet-5, if devnet-4 goes smoothly. My biggest fear here is that this is already such a massive massive change and that if we try to just add everything now and constantly keep changing the spec, we don't get to a point where clients have a stable implementation of the current spec that we can test.

It does seem like we don't necessarily need to make a decision on this now but ideally before we ship we should have taken the right decision here. Does that make sense to people? Any objections or concerns with that?

In that case, what's the best place to continue the conversation around the specific issues? I know that people have been using the EVM channel, that seems right, and I assume there's another EOF implementers call if not next week then the week after.

**Danno**: Yes, the EOF implementer calls are opposite weeks of ACD calls, so it'll be Wednesday. I'd like the Ipsilon team to get that draft out as soon as they think it's ready, preferably as soon as possible, so we can have a discussion on what their ideas are for how we can address that. I do like the idea of doing devnet-4 with what we have right now and then contemplating whether we add this in Pectra or whether it becomes a Fusaka target.

**Tim**: That sounds good. Any other concerns, comments, about EOF or the specific change?

|| **Chat**
 - Dragan: I would consider including IS_CONTRACT after devnet-4

<br>

-------------------------------------
### 195.7 | **[EIP-7251](https://github.com/ethereum/consensus-specs/pull/3882) Updates** ([42:50](https://www.youtube.com/live/HJ9WxAOwTTA?si=FzKXFLzw5YteAJYf&t=2570))

**Tim**: Moving on we have a proposed change, a CL change, to fix the correlation penalties that Mikhail put together and he just wanted to get a last call on people reviewing this. I don't think Mikhail is on the call today, but if anyone else has comments or contexts they want to share about this, please do.

**stokes**: I can, a little bit. It's kind of fixed as an edge case with the penalties on the CL around slashing under the max ev change. If CL team could just take a look at the PR and approve ideally, that would be great. It should be in a pretty good place, so the ask is just for CL team to take a look.

**Tim**: Is this something we would merge into devnet-3 ro devnet-4?

**stokes**: It will land in the CL specs when it's ready and then from there we can just see which devnet is ready. It doesn't really matter; this isn't something we're going to hit in testing at least in devnet-3 or 4.

**Tim**: Okay sounds good. Let's try to get this reviewed async and merged before next week's call.



-------------------------------------
### 195.8 | **[Engine: unify request objects](https://github.com/ethereum/execution-apis/pull/565)** ([44:29](https://www.youtube.com/live/HJ9WxAOwTTA?si=8dji7WZkXBQlCSqf&t=2669))

**Tim**: Next up we have a proposal by lightclient to unify request objects in the engine API. There's been a fair bit of discussion on it with the last comments coming after the start of this call, right at the start of this call. Lightclient, do you want to give some context on this and if others after that want to chime in, that'd be great. 

If not, as I understand, it is that the current design requires clients to be aware of the fork schedule through the engine API and this design would, I believe, remove that requirement. But there was a recent comment that came right at the start of this call saying that it seems like the EL actually needs to be aware regardless because of some old methods.

Any comments, thoughts? If no, we can also continue the discussion on the PR and potentially give people another week to review it.


-------------------------------------
### 195.9, 195.10, 195.11 | **Pectra EIP proposals** ([46:15](https://www.youtube.com/live/HJ9WxAOwTTA?si=3ZyVWly8LqRA9Ylm&t=2775))

**Tim**: So Pectra EIPs. We have 7623, which was proposed a while back and then subsequently, CFI'd. Toni wanted to ask about including this in the hard fork. Similarly Alex had an EIP to decouple the blob count between the EL and the CL. Lastly, Max has a proposal to update the blob reserve gas price. It is probably worth going over each of these in more detail, but I wanted to flag that it does seem like we have a fair amount of small proposals that people still want to put in the fork. There's other that we've discussed in previous calls like 7212, for example. So if making decisions we should make them in context with the others--none of these are the only thing we potentially want to add as a small addition to Pectra. 

#### [EIP-7623](https://eips.ethereum.org/EIPS/eip-7623) ([47:30](https://www.youtube.com/live/HJ9WxAOwTTA?si=0wJb23LJ-EjBJgLv&t=2850))

**Tim**: Toni, you are on the call, do you want to give a bit of context for 7623? 

**Toni**: As a reminder, EIP 7623 proposed to increase the call data cost for call data heavy transactions. The main motivation to do so is to reduce the size of the EL payload because already today we see certain big blocks--and with 'big' we're talking 400 kilobytes-- that receive way less attestations and are then more often reorg-ed. Also, today the mean block size is around 100 kilobyte plus blobs, but the maximum size is 3.5 megabytes, so 100 kilobytes versus 3.5 megabytes. As you can see this is super volatile and by increasing the call data cost we can basically reduce it. Also, I think the EIP is in a good position now because we have blobs, all the rollups are using blobs already, so no on relies on using call data for data storage on chain. As Tim said, the EIP is considered for inclusion and I would propose that we include it in devnet-4. The EIP itself is super small, the EL specs are done, and I think Mario started implementing it in Geth? Would love the hear what the core devs think about it.

|| **Chat**
 - Ansgar: 7623 to me is addressing an active network vulnerability-- a calldata cost increase in some form should very importantly be in the fork.
 - +1s everyone
 - Ansgar: and just to point out, a big block attack would most severely impact solo stakers on low bandwidth connections
 - Ansgar: 7623 is somewhat opinionated about the exact economic mechanism. I personally like it, but if it ends up being controversial, alternatively we could just ship a 'dumb' calldata cost increase.
 - Tim: IIRC that's what lightclient preferred

**Tim**: There are comments saying that they see the EIP as addressing a vulnerability. I assume this is the fact that we can have these huge heavy blocks on the network and then a +1 from Nethermind for this EIP. Any other thoughts, comments? Lots of +1s [in the chat] for the EIP.

Before we make a call about this, it's probably worth going over the two other proposals to see how much support they have. If this is the one people feel strongest about...we can decide to include it and figure that out. Before we make that decision, Alex do you want to talk about 7742?


#### [EIP-7742](https://eips.ethereum.org/EIPS/eip-7742) ([50:10](https://www.youtube.com/live/HJ9WxAOwTTA?si=2P5oiADnoiUast_7&t=3010))

**stokes**: I think most people have seen this EIP in some sense already. So today, how it works, is there's a target value for the blobs that we want in the protocol and a maximum value and right now these parameters are specified both on the CL and EL. One thing this does is it couples together the development of both these layers and makes it little more inflexible to change target or max, whatever we want. The EIP proposes to uncouple these constants betweek the EL and CL and essentially have the CL drive the values and then provide them in the necessary way to the EL. 

We've gone through a few rounds of feedback, at least more on the CL side of things, and I think the things are ready to go, meaning the EIP engine API changes and the CL specs. There was really good support from the CL call last week and I'd like to hear what EL devs think. 

**Tim**: Any thoughts on 7742?

|| **Chat**
 - Barnabus: Is this a trivial change from the EL clients?
 - Oliver: +1 from Reth, makes sense. Don't feel strongly about including it in Pectra or not
 - Barnabus: we ideally want this in peerdas-devnet-3

**stokes**: I guess one other comment is that it support peerdas and just generally the blob mechanics and so we could imagine coupling this with peerdas and can decide when peerdas ultimately lands. [In response to Barnabus] It would be a little messy to have a separate peerdas spec, but...

**Barnabus**: No, we would have one spec and just point to that basically. I'm not sure about the correct order, what we would do, like Pectra devnet-4 would come first, or peerdas-devnet-3? We are currently still waiting for peerdas-devnet-2, for client teams to finish the implementation. once that's somewhat stable then we can add some additional scope to the peerdas testing, which would also be the time when peerdas would rebase on top of Electra. At that point, it would be very nice if we could play around with a different number of blobs, different targets and values, and just experiment how it would like in peerdas. All we would need is a single EL to implemenet this and then we could use that for testing, and then every other EL could implement this later or whether we decide to include in Pectra or not.

|| **Chat**
 - Dragan: Would leave decision making for at least next ACDE call, so people can have time to digest and make their statements.
 - Tim: Yeah, I'm inclined to agree. Doesn't seem like any of these decisions need to be made now. And I can make sure to polish the list of proposals (e.g. we can CFI 7742, but perhaps also a list less formal proposals like the EOF changes.

**Tim**: So does there's a comment in the chat from Dragan; I feel like that's the right way to go about this so that we can at least list out all of the potential additions. Some of them are like formal EIPs. For 7742, I'm not sure if we've CFI'd, but it seems like it probably makes sense to CFI that for the fork given the relatively strong support, but then in addition to that, potentially list out the less formalized proposals like the EOF changes and potentially what we're about to talk about. Would that make sense to people or does anyone feel like there needs to be a decision now? Does anyone object to CFI-ing 7742 so we can have it there alongside everything else: 7212 R1 curve, inclusion list EIP, 7623, 7742. I can put together a list of other proposals that aren't quite formalized and people can review that and ideally even share their thoughts prior to the next call.

#### [Raising the blob reserve price](https://github.com/ethereum/EIPs/pull/8849) ([55:50](https://www.youtube.com/live/HJ9WxAOwTTA?si=WsY4OGC8Uelibklh&t=3350))

**Tim**: Last on the agenda, Max wanted to talk about raising the reserve price for blobs.

**Max**: This change would be a one line difference; the reserve price is actually already implemented, it just hasn't been set other than at 1 gwei. So it's a one line diff just changing that constant to be a value that I proposed. The value was chosen so that the cost of a blob would be pegged to around the cost of a simple transfer, so 21k gas at a 1 gwei base fee, which comes out to around 5 cents USD per blob at today's prices. The goal of the change is not to raise revenue. Even if we had three blobs per block, it would be something like less than 400k a year in total cost if we saturated all blobs. But the goal is really to have the reserve price be at a point where when blobs do enter price discovery, they do so faster than they do right now. Right now, it would take basically 32 minutes to get from 1 gwei to this level of reasonable 5c per blob because of the way that the updating rules work. Right now you have to traverse all these orders of magnitude of fees to get to the right spot and it just takes a long time to do that with the updating rule. This would be a one line change that addresses that. 

The reason we might want to do this is that there's some chaotic stuff that happens when blobs enter price discovery where there's a lot of weirdness that goes on on the fee markets that we've seen a few times when they do enter price discovery. 

**Ansgar**: I just wanted to say that the reason why the parameter is in the specs right now, but not set, was just that we weren't sure it's worth the complexity and initially we just assumed that blobs would only really go through price discovery once, relatively shortly after shipping 4844, and then we would stay above some sort of minimum price from then on out. It turns out that was not the case. It takes a little bit longer to basically hit that adoption level and so we might actually go through that phase several times. We've already done that a few times in the past when demand spiked and so I personally think it makes a lot of sense and particularly that Max's specific proposal seems very sensible to me. It's actually important that we hit the right trade off and that we don't set it too high because the point specifically is not to raise revenue or price gouge or anything. It's really just to shorten the time to sensitivity. I think the proposal as-is is already ideal and if it was put into a full EIP, I would support it.

**Ben**: I have not double checked Max's math, I'm trusting it, 100 blocks to go from 1 gwei seems like an extraordinary load on the validations for unresponsivenet to get to a price that's pretty low anyway, so I think it makes a lot of sense.

**Max**: That would be at full load and actually there's a bunch of weirdness that happens. Usually these price spikes happen around when other activity on the chain is high, when there's trading going on, the builders don't want to include the blobs so it actually takes even longer than that because they're periodically producing blocks without any blobs so it's even longer than that. That's kind of the best case scenario.

**Tim**: Any other thoughts, questions, or comments about the proposal? 

**Peter**: Someone mentioned that blobs are not being included for efficiency reasons related to trading; is there any concern that we might not get price discovery because people are so reluctant to include blobs that they're just not being included above the target rate anyway? That might suggest that we want to do something more sophisticated than just this proposal. 

**Toni**: I don't think that's the case, because at some point rollups will just pay more and more and at some point the builder will have incentive to include them no matter how big the blobs are.

**Max**: I agree, the priority fees will start to escalate. There have been some changes in the builder API endpoints that allow more efficient fee market and allow you to basically replace your bid with one with a higher priority fee without having to rebroadcast the blob. Before, you had to rebroadcast the blob and in order to prevent DoS attacks on the network you had to increase the fee by 100%, so there have been some positive changes in that direction on the builder front. Besides, I think a change like that would probably be too big for Petra--any change that's more in the fundamental structure--whereas this is a one line change to a parameter. 

**Tim**: I think for this specific proposal its clearly worth drafting an EIP and considering it along with the other changes we we're just discussing. Max, do you have the bandwidth to do that in the next week or so?

**Max**: Yes, I'll have it ready by the end of the week.

####([1:02:38](https://www.youtube.com/live/HJ9WxAOwTTA?si=wBvUnL1Oo0vCBJ68&t=3758))

**Tim**: One thing related to 7623 that I wanted to bring up [from the chat]. Ansgar said it might be worth considering just the raw call data increase if that's simpler than 7623. I don't know if anyone wants to draft an EIP for that as well for us to consider, or if Toni has thoughts about if we were to just do a simple one line change instead of 7623? What would that look like?

**Toni**: You could basically look up the EIP first version. It started exactly like that by just 4x-ing the call data cost for nonzero and zero bytes. The main problem back then was that the community was saying that this is a bigger change because it impacts tooling. Not like in EIP-7623, where 99% of the transactions would be unaffected, but with a dump increase you touch basically every transaction. This was the main rationale for doing it in a more complex way, by having the advantage to not touch every transaction.

There is a follow up proposal by Vitalik to do it multidimensional, which we might want to do in the next years, so I would see 7623 more as the quick fix that is a little bit more sophisticated than the dump increase but also far away from multidimensional gas pricing.

**Tim**: Got it, thanks. In that case, we can have people review 7623 and if people think it's too complicated, we can cross that bridge when we get there.




-------------------------------------
### Attendees
* Tim
* Stokes
* Pooja Ranjan
* Ben Adams
* Mark Mackey
* Hadrien Croubois
* Oliver (Reth)
* latterjed
* Lucas
* Trent
* lightclient
* Danno Ferrin
* Justin Florentine
* Ansgar
* Peter Miller
* Jochem-brouwer
* Parithosh
* Ben Edginton
* Łukasz Rozmej
* Ignacio
* Guillaume
* Enrico
* Mario Vega
* Andrew Ashikhmin
* Max Resnick
* Justin Traglia
* Daniel Lehrner
* Toni Wahrstaetter
* Alex Forshtat
* scorbajio
* terence
* Carl Beekhuizen
* frangio
* Shruti Gandhi
* Katya Riazantseva
* Roman
* potuz
* Manu
* Barnabus
* Phil Ngo
* marcus
* Karim
* Sudeep
* James He
* Echo
* MarekM
* Ameziane Hamlat
* Somnath
* Yiannis
* Tanishq
* yoav
* dragan rakita
