# All Core Devs: Meeting 14
## Time: 4/21/2017 14:00PM UTC
## [Audio/Video of Meeting](https://youtu.be/PGi0vBxDPHY)

### Agenda:

1. [[0:12](https://youtu.be/PGi0vBxDPHY?t=12)] [EIP 186: Reduce ETH issuance before proof-of-stake](https://github.com/ethereum/EIPs/issues/186). ([Carbonvote link](http://www.carbonvote.com/?p1=1), [Reddit thread #1](https://www.reddit.com/r/ethereum/comments/5lb684/eip186_to_decrease_eth_issuance_by_3x/), [Reddit thread #2](https://www.reddit.com/r/ethereum/comments/60c2my/carbonvote_set_up_for_eip186/)) [Core Devs]

2. [[5:14](https://youtu.be/PGi0vBxDPHY?t=314)] About [EIP 86 (a.k.a EIP-208)](https://github.com/ethereum/EIPs/pull/208), there is a difference between the EIP pull-request and the implementations. Which should be fixed? Also, some EIPS (212, 213, and 96) are not specific enough to form specs yet. Who can update those? [Yoichi]
3. [[20:56](https://youtu.be/PGi0vBxDPHY)] [EIP 98: removing medstate from receipts](https://github.com/ethereum/EIPs/pull/98) - go & cpp implemented option 2, Parity seems to have went with option 1 [Andrei]

4. [[25:35](https://youtu.be/PGi0vBxDPHY?t=1535)] Metropolis updates - specifically an update on where each client is at in implementation and an update on the tests. Some accepted EIPs are not yet specific enough to form a protocol consensus. What is the next action by whom?

5. [[38:52](https://youtu.be/PGi0vBxDPHY?t=2331)] [EIP 599: 'Valid until block' field for transactions](https://github.com/ethereum/EIPs/pull/599) [Nick]

# Notes
### Thank you to http://www.etherworld.co/ for the detailed transcript.

## 1. EIP 186: Reduce ETH issuance before proof-of-stake [Core Devs]

Hudson: Vitalik, what's your view on EIP 186?

Vitalik: I think anything over 2.5 is safe enough but going beyond that will introduce some risks for just safety stand points.

Hudson: What would you say about the need they put it in the Metropolis? Is that what they want at this point or is that something that should be addressed for a different hardfork or not at all?

Vitalik: The reward is going to come down anyway once we start the PoS switch. Practically speaking the difference between cutting it down to like even to take the bottom end 2.5 and just pushing it all the way back up to 5 and in terms of Metropolis, it’s going to be something like 2-3 million Ether.

Hudson: It sounds like it's not something that is more important or applicable for Metropolis.

Vitalik: It's not that important or applicable either way, though on the other hand that given network going to be mucking around with mining rewards anyway because we will be delaying the ice age. I don't see any extreme case in either direction, I guess.

Hudson: Yeah, I am thinking the same way. In most cases, I feel like the status quo for when that happen within hardforks that I've seen is that when it’s not that strong in either direction and there are no people who is going to be championing the idea that it probably should just remain in discussion overall or be delayed for different thing. Does anyone else in the room has any different perspective or any other opinion?

Martin: I am just saying, keep the uncontroversial hardfork as uncontroversial as possible.

Hudson: Yeah, I would tend to agree with that. Next agenda item is one Yoichi brought up - EIP 86; which is talking about the instructions. He was saying that there are discrepancies between the EIP poll request as written and the implementation across clients. Yoichi, do you want to expand on that a little bit?


## 2. About EIP86 (a.k.a EIP-208), there is a difference between the EIP pull-request and the implementations. Which should be fixed? [Yoichi]

Yoichi: Yes, this EIP is about account abstraction and as part of that specification point 3 talks about changing the way it calculates the address of new contracts. The interesting thing is it only talks about create, transactions but not create instructions. So, when the EVM hits the create instructions, it creates something but it’s not the create instruction. So, there is some ambiguity if this EIP changes both create transaction and the create instruction or it does just change the create transaction and we keep the create instruction as it is? Literally the EIP text looks like it changes only the create transactions not instructions but other implementations I saw, I kind of agreed on changing both, specially the create instructions. So, I need some clarification, which way we are following?

Dimitri: Due to the fact that we also add a new creation opcode in this proposal than this means that the old creation opcode retains its semantics.        	

Yoichi: So... Yes, Christian made one argument to form an auction and that’s why I chose the same in the yellow paper pre-requisite. But that's a different argument may be its a good EIP without keep create instructions as it is because when we change that we might break some existing contracts. I kind of need clarification here.   

Dimitri: Create transaction is an external interface to Ethereum.

Martin: Lets introduce a level above a new create opcode.

Yoichi: Yes... so, this same EIP talks about creating a new kind of create instruction where different sources can deploy the same code on the different addresses. It's called create PY2SH or something.  So yes, this is the new instruction.

Martin: So, the intention that EIP seems to be that create states does not pause before.

Yoichi: correct

Martin: And someone who would champion the case why create would change?

Vitalik: Basically, the idea in general is that we want it to be possible and very easy to have addresses that are very specifically bounced to one particular piece of code. So, the people can either send money or send tokens to do other things at those addresses before the accounts get created. The problem with the current contract creation approach is that because the address only depends on the sender and the nonce, the actual contents of all the addresses are under the full controls of the sender because the sender gets to put whatever they want to into the contract code and it’s still the same address either way. So, this EIP would make addresses code dependent and actually allow you to create contract where the address for those contracts do depends just on what the users code is. One user story for example, let say I have no money, and I want to start receiving money and I also do not want to have the account that use regular ETH just say. I may want to directly have a multi-sig or I may want to directly have something which is linked to lamppost signature and whatever else. What I would do is I would privately kind of simulate the creation of the contract, privately like figure out what the address would be with that piece of code. Then I would give people that address and people can send money to that address and when there is enough money in the address, you could create the contract and pay out of that money as a fee going to the miner.

Yoichi: That’s where it can go with the extend of the concern the contract both, so this kind of doesn't answer the specific question that if the create instruction will change.

Vitalik: There are two ways to create contract, one of them is external and other one is with create opcode. So, part of the EIP accounts the scheme for addresses that get created externally gets changed. But as far as the create opcode, I think there are two main reasons to change that.
•	One of them is consistencies.
•	Other is that the scheme works even if contracts are creating other contracts and not just the mechanism from the outside.

Yuichi: I got the clarification now and I think that this EIP prerequisite text can be improved but I don’t think that the original implementation needs change. I am happy about this.

Martin:  Just to clarify Yuichi, do these implementations, these pull requests change the create instructions or do they add a new create instructions?

Vitalik: They add a new create instructions and the old one is retained.

Yuichi: They do both.

Martin: So, the old one is retained?

Vitalik: Yes.

Yuichi: The old one is there but the old one creates accounts in different positions after Metropolis.

Vitalik: No, the old create opcode should still create accounts at the same positions.  

Yuichi: Oh! In the same position? Ok, I misunderstood you. In that case, the cpp-ethereum   pre-requisite should be updated and the priority implementation should change.

Hudson: The opcode gets a new name but the same number. Did I say it correctly?

Martin: No that’s not correct. The old create is still the old create. You create the P2SH, different creation address. Correct me if I am wrong Vitalik.

Vitalik: The behavior of the old opcode is unchanged and the new created opcode has equivalent functionality except with different address.

Yuichi: I get that the old create instruction will not change its behavior, then I agree with comments on mainly cpp prerequisite.

Martin: What happens with the address of a contract, if it is self-destructed later?
 
Vitalik: Then you can create another contract on the same address with this opcode.

Arkadiy: Just for clarification, after Metropolis there will be three ways an address for new contract is generated.
1.	Create transactions: generates an address from the code hash
2.	Create opcode generated by ROP concatenating sender and nonce
3.	A new create instructions to generate it from.

Vitalik: Yes.

Arkadiy: A use case when the account receives some balance and only after that a contract is created for that address. A create instruction doesn't check if an account exists, just check for the code.

Vitalik: Yes

Hudson: Yoichi had another comment about what's the next action on some of the excepted EIP that are not yet specific enough to form a protocol consensus?

Yoichi: There are certain accepted EIPs and I assume that we are seeking to implement those for Metropolis but some of these have missing numbers.
•	For elliptic curve thing, we don't have the gas prices yet.
•	For blockhead abstraction thing, we don't have the gitter code

Vitalik: Christian has come up with some of the possibilities of gas prices but the reason why we didn't set thing in stones yet because we wanted to get benchmarks on the parity version and the go version and see how long it takes before we make a final decision.

Hudson: So, it's accepted but then we can tweak that at the end as the stuff goes.

Vitalik: If we need to do it just for testing purposes then we could agree to some temporary gas price now but then if it is just for testing then lets all make it zero.

Yuichi: No problem.

Hudson: The pairing check and the group addition on elliptic curve are things that sounds like will come with time when we can put values in. The thing with gitter code on EIP 96 is something the is the same case or can be answered?

Vitalik: For EIP 96, I can provide one version of the gitter code.

Yoichi: Points withdrawn.

## 3. [EIP 98: removing medstate from receipts](https://github.com/ethereum/EIPs/pull/98) - go & cpp implemented option 2, Parity seems to have went with option 1 [Andrei]

Hudson: EIP 98 seems to have difference in implementation between go and cpp version, Andrei would you like to comment?

Vitalik: EIP 98 is the one which removes the intermediate state correct?

Hudson: Yes.

Andrei: There are two options in EIP specifications
1.	Removing the root hash altogether from their RLP structure
2.	Replacement with zero hash
Looking at the code I noticed that parity seems to modify RLP structure and go just replace it with zero hash. So, we should come to some agreement here.

Arkadiy: We should just remove it completely because it seems more cleaner and ready to deploy it , so we prefer to keep it that way.

Andrei: I agree that removing is better.

Felix: I agree with removing.

Hudson: About blockchain and state root change; EIP 96 (86). Powel asked about keeping the addresses at precompiled contract continuous, why are we jumping from contract 10 contracts to 20?

Vitalik: My reasoning for making them separate is because these addresses for EIP 96 is not actually a real precompile; it’s just a prenode regular contract with a piece of prenode regular code that happens to have a privilege status in the protocol.

Arkadiy: In EIP 96, the contract is inserted into the state when the transition happens and it changes the state root, so it’s not a precompile.

Vitalik: Yes

## 4. Metropolis testing and client implementation updates [Dimitry and Core Devs]

Hudson: Metropolis testing update

Dimitry: Test fields will be prefixed by 0x. All the tests will be in this new format now on, I am working on it. Yan is implementing new changes on create instruction.

Hudson: Any help that you need from the core developers for testing of EIPs for Metropolis?

Dimitri: A file on Google Docs keeping updates to that file with test cases that are already implemented are marked in green. To do list and status of other tasks are available. It is a task in progress.

Hudson: Metropolis Clients implementations. I think they are still with PR with the checklist of what’s been implemented. Any comments, questions or showstoppers that you want to discuss?

Nick: The last I heard from Jeff, he was more or less done. I don't have more details if it’s done 100% or not.

Hudson: Looking at the PR it looks like it’s more or less done, so it should be fine for this call. That’s Go, now do Parity.  

Arkadiy: On Parity, we are mostly done, just one EIP that needs to be implemented on the return data.

Hudson: Ok great. Berlin team got dropped off.  Jan, do you have updates on clients you worked on?

Jan: There is no active development on ruby-ethereumnow, and I and my team is working on pyethereum. We are also working on adding DEVP2P and NAT functionality to the client so you can run a Py node from home local network. We are adding concurrent synchronizing to DEVP2P of the py node. So basically, we are trying to fix Py node so that it can keep up with other implementations like geth. Then I think we can start to implement Metropolis features.

Vitalik: I started implementing some Metropolis features in pyethereum. The revert opcode is passing all the tests, there is implementation of EIP 86 although it is old so it may not be fully compliant with all the related stuff that we agreed on but that will be very easy to change once the test is there. EIP 96 and EIP 98 are theoretically implemented back when I was doing some experimentations for Casper, but it may be reparametrized a little bit. There are still couple of EIP those aren't done, so static calls are not done on them either.

Hudson: Ok, sounds great. Thank you for update on that. We've Berlin team back, so we can have update on C++ and Martin if you would like to update on JS?

Andrei: We are half the way through, three EIPs are still not started, three are implemented and merged. So we are in progress.

Hudson: Great. Is Martin there?

Martin: Ethereum JS is a work in progress; team hasn't done any Metropolis related stuff so far except for one. That’s the update for past two weeks.

Hudson: Any other outstanding questions?

Vitalik: I don’t think there are any outstanding questions now.

Hudson: Nick wanted to bring up EIP 599 and discuss, but before that any more update on Metropolis timeline. Right now we have a goal of end of June, can we set up dates on implementing stuff on testnet?

Vitalik: I personally feel there is still too much uncertainty to get on a hard date right now. I prefer that we make commitments just to get stuff running and passing tests with medium – high priority. Once it gets more clear and get all closer towards it then we can agree to a date.

Hudson: Sounds good to me.

Vitalik: Just from ice age standpoint, difficulty continues to go up that continues to make a later launch of Metropolis more tolerable by at least a couple of weeks. If we get out the fork by June 25, 2017 and hash power stays as it is now then block time will not go above 19s.

## 5. [EIP 599: 'Valid until block' field for transactions](https://github.com/ethereum/EIPs/pull/599) [Nick]

Hudson: Nick, you want to talk about EIP 599?

Nick: This is a proposal to add a 'transaction time to lose' field to transactional pay. The goal here is that currently managing transactional polls so there is no good way to expire out the old transaction and that means that attackers can potentially cause a lot more trouble in a DAO s point of view than they should be able to and they can spam a transaction and as long as a transaction remains valid and his balance in the account and we have no way to evict theses spam transactions from executing them. If you think they would evict themselves then the chances are they would just be reload back from another node that doesn't sends its node transactions. What I am suggesting is adding an optional field which specifies that the transaction must be mined before they stay in block. And any transaction whose block number is before the current block number is discarded as it may not be relied and any transactions whose include before block number is too far in the future should be treated as hostile and generally not relied.  The idea is in addition to make DAO attack harder also allows people to publish transaction they now believe be executed quickly or not at all good for operations. The existing transactions will still be fine with this proposal. Nodes must accept the blocks that contains transactions with fa future time stamps or with block numbers and with no block numbers, they would generally try to avoid relying them. 	

Hudson: It is under handling transactions issue category. In this EIP, you want this to happen in Metropolis or something that would work now and when we would want to implement it?

Nick: I think its reasonably straight forward so optimistically it would be nice to implement this in Metropolis but that depends on what the team thinks of its implementations.

Spectacular: That’s great. Anyone with other idea or thoughts on complexity for its implementation?

Vitalik:  Yes, as far as implementation complexity goes, I would have preference to go around how EIP 86 does.

Hudson: Any other comments from any other devs?

Jan:  I think these changes are also good for Dapp developers for the apps because there is a problem for system that when you send a transaction, you are not sure when will your transaction be included in the blockchain and until you see your first transaction on the chain, you don't know, if you should send another transaction or just wait. With such a change, I think you only need to wait for a certain amount of time and that's very useful. 	

Hudson: Cool … good comment. For implementation, a hardfork is required. Any other comment?

Yoichi: I feel we should do the transaction field simplification thing proposed by Vitalik.

Hudson: So, that would be just instead of adding a field every time you want to add functionality but just doing a field you can put wherever you want and have some standards around that.	

Vitalik: Yes. There are two ways of abstracting this
1.	We do it inside of my suggestion for changing transaction formats. And the benefit there is just the basically makes it easier for us as protocol developers to change transaction formats in the future.
2.	Don't bother for now, but instead we make maximum block number field part of EIP 86 transaction and recommend people to add a checker for max block number in the validation code.  	

Nick: I will read Vitalik's EIP 232 and update my proposal accordingly for the next meeting.

Vitalik: Another thing, if we have enough time, we can be a bit more conservative and to take an extra month to do security audits and other things.

Nick: Yes, I am generally onboard with extra cautious approach and on the other hand I do think that we have enough potential to deal with the issue here.

Hudson: We may have more information by next meeting about the changes you have made will help start making some decision on timing of implementation since it seems like it’s been excepted so far.

Nick: Sounds good.

Hudson: Anyone would like to add anything.

Vitalik: Not right now.

Hudson: Ok Great. Thank you everybody. Keep up with the EIPs, especially keeping them updated and getting the specs validated so that we can start shoring up the implementation on the testing on them.

## Attendance

Alex Beregszaszi (EWASM), Alex Leverington (Golem), Alex Van de Sande (Mist/Ethereum Wallet), Andrei Maiboroda (cpp-ethereum), Arkadiy Paronyan (Parity), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum/Solidity), Dimitry Khokhlov (cpp-ethereum), Felix Lange(geth), Hudson Jameson (Ethereum Foundation), Jake Gillberg, Jan Xie (ruby-ethereum & pyethereum), Lefteris Karapetsas (Raiden), Martin Becze (EWASM/EthereumJS), Martin Holst Swende (geth/security), Nick Johnson (geth/SWARM), Vitalik Buterin (Research & pyethereum), Yoichi Hirai (EVM)
