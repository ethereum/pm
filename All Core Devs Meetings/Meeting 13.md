# All Core Devs: Meeting 13
## Time: 4/7/2017 14:00PM UTC (actually started at 13:00 UTC)
## [Audio/Video of Meeting](https://youtu.be/aGeGvZ5uS8s)

### Agenda:

1. [[2:58-8:49](https://youtu.be/aGeGvZ5uS8s?t=178)/[13:20-19:54](https://youtu.be/aGeGvZ5uS8s?t=800)/[39:38-41:46](https://youtu.be/aGeGvZ5uS8s?t=2378)] Resolution for STATICCALL, PURECALL, REVERT Opcode, & Dynamic Return Discussion
2. [[8:50](https://youtu.be/aGeGvZ5uS8s?t=530)] Update on [EIP 225: Rinkeby and Clique PoA](https://github.com/ethereum/EIPs/issues/225)
3. [[19:55](https://youtu.be/aGeGvZ5uS8s?t=1195)] [EIP 186: Reduce ETH issuance before proof-of-stake](https://github.com/ethereum/EIPs/issues/186).
4. [[41:46](https://youtu.be/aGeGvZ5uS8s?t=2506)] Metropolis testing and client implementation updates.
5. [[56:50](https://youtu.be/aGeGvZ5uS8s?t=3410)] Unplanned topics (transaction propagation issues and potential solutions & making RETURNDATACOPY and CALLDATA to throw in certain situations).

# Notes

## 1. Resolution for STATICCALL, PURECALL, REVERT Opcode, & Dynamic Return Discussion [Core Devs]

Related EIPS: (https://github.com/ethereum/EIPs/pull/214, https://github.com/ethereum/EIPs/pull/195, https://github.com/ethereum/EIPs/pull/207, https://github.com/ethereum/EIPs/pull/211)

The parties interested in coming to a resolution on what EIPs from the list above to include were added to a Skype discussion and have come to the following conclusions:

- Withdraw [EIP 5: Gas Usage for RETURN and CALL*](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-5.md) in favor of [EIP 211](https://github.com/ethereum/EIPs/pull/211).
- Withdraw [EIP 195: PURE_CALL](https://github.com/ethereum/EIPs/pull/195) in favor of other EIPs.
- Include [EIP 214: STATIC_CALL](https://github.com/ethereum/EIPs/pull/214)
- Include [EIP 211: RETURNDATACOPY and RETURNDATASIZE](https://github.com/ethereum/EIPs/pull/211)
https://github.com/ethereum/EIPs/pull/211
- Include [EIP 207: REVERT](https://github.com/ethereum/EIPs/pull/207)

Christian R.: 
It was suggested that we clear the RETURNDATA buffer on the first memory resize ([raised by Gavin in the EIP 211](https://github.com/ethereum/EIPs/pull/211)).

Nick: Not speaking for Gavin, but minimize the max memory consumption and allow for contiguous memory for the entire call stack rather than a separate chunk for each contract. Personally, I think it would be fine if it is designed to erase it after expansion so you can copy RETURNDATA into newly expanded memory.

Christian R: I would like to avoid that because it complicates things, such as the optimizer and static analysis.

[Christian, Nick, and Martin H.S continue to discuss this for the next few minutes.]

[At this point in the call I discover that I started the call 1 hour early because I can't time zone. Doh!]

Arkidiy joins the call and later provides this summary of the concern as well as summaries of concerns in [the EIP comments](https://github.com/ethereum/EIPs/pull/211).

Arkadiy: The concern is that the EIP increases max memory consumption. We have to keep returndata around from the call that you make, but if you expand memory before leaving returndata you will get higher peak memory usage.

Christian suggested having a separate call and discussion outside of all core devs call to talk about the concerns. Those who want to be involved can talk to Christian. [It appears that there is already active discussion on the EIP page as well](https://github.com/ethereum/EIPs/pull/211).

## 2. Update on [EIP 225: Rinkeby and Clique PoA](https://github.com/ethereum/EIPs/issues/225) [Peter]
Next steps: Submit the EIP as a PR to begin process of official approval.
Peter: We've been working on a tool to deploy these Rinqby private networks including a Github authenticated faucet. Still writing some tests, but otherwise mostly done from a Go team perspective. We are aiming to release an "Olympic testnet" version of Rinkeby for initial deployment and can make that implementation more important if it doesn't blow up.

## 3. [EIP 186: Reduce ETH issuance before proof-of-stake](https://github.com/ethereum/EIPs/issues/186) [Hudson]

[Carbonvote link](http://www.carbonvote.com/?p1=1).
[Reddit thread #1](https://www.reddit.com/r/ethereum/comments/5lb684/eip186_to_decrease_eth_issuance_by_3x/).
[Reddit thread #2](https://www.reddit.com/r/ethereum/comments/60c2my/carbonvote_set_up_for_eip186/).

Hudson: Haven't looked into this, but it seems to be getting some community traction so I added it to the agenda.

AVSA: My initial thoughts are that we should not be playing with the issuance or economic policies if things are not very broken. Additionally it would increase the controversy of the upcoming Metropolis hard fork that is currently non-controversial.

Martin H.S: I don't particularly support this, but I am curious at how large the community support is.

We discuss that carbon vote's website is running a poll on it, but we are skeptical about the reach and how it truly represents the community in this instance because this EIP is not widely being contentiously debated or discussed outside of Reddit posts and the EIP itself.

Nick: I generally think it is not a bad idea if it is greater than or equal to the amount they would have received with the ice age because at that point they are not likely to oppose the fork because they will be worse off.

Hudson: This may not even be a question of whether it should go on, but whether it should go in for Metropolis or should be discussed for a different hard fork (in order to avoid making Metro a big deal). Those who deal with economic policy and other related research fields have commented on this primarily, but this week many of them are in Malta at a conference and therefore aren't here to provide comment. I saw Vitalik write somewhere that he would be willing to consider it more seriously with enough community support behind the idea.
What changes would have to happen on the technical end in order for this to go in?

Pawel: Change in code is super simple. My perspective is that this could make a less controversial hard fork a controversial one.

Hudson: So I'm wondering if it is better to implement this based on some possibilities that we aren't sure yet, but face the backlash of a more controversial hardfork and related complications, as well as setting precedence for changing core economic principles on a whim?

Peter: Aren't we already changing core economics by delaying the ice age?

Hudson: True, but this economic change is more of a side affect of preventing the impending block time changes that will affect the network.

AVSA: The ice age was never meant to be taken into prod. People never took it seriously that we wanted to slow the system down to a halt, it is just a mechanism to force a fork. No one believes we want to have a 10 min. block time. Idea was that PoS would be ready by then, but it is not, so the economic policy of the ice age should not really count. My fear is that we are taking something the community doesn't really want and are creating a discussion around it when it isn't truly widely recognized. I could be wrong though.

Martin H.S: I think it's a good thing we are talking about this because it shows that we are looking out for what is being discussed in the community even if we (core devs) aren't following it closely ourselves.

Hudson: Alex, I think that there is a level of legitimate support around this EIP, due to the fact that the EIP was written in Dec. 2016 before the recent price spike and Vlad's blog, which can be considered incentive to change this policy. I think the intentions behind the EIP are good so discussion is good. Like all of these things it comes down to the clients wanting to implement it and seeing how large the community push is for this change.

Alex B: Are we changing the block # for the ice age in Metro?

Peter: Idea was that we add special rules to the difficulty calculation to effectively pause the difficulty between different blocks #s.

We discuss if we are doing 1 or 2 hard forks for Metro/ice age changes. In previous dev meetings, we discussed having 1 HF for metro, so that seems like what we are doing.

We will bring this up next meeting to let some of the researchers, like Yoichi and Vitalik, comment on this.

## 4. Metropolis testing and client implementation updates [Dimitry and Core Devs]

Dimitry gives an overview of how the tests are coming along and what can devs do to help.

Dimitry: To make tests better it would help to have better indication in Github of which EIPs are included in Metropolis. It is hard to follow what is included.

Hudson will work on this by updating the tables on the README page and adding Github labels. We will also incorporate Alex B.'s [EIP 233: Adding Meta EIP for Hard Forks](https://github.com/ethereum/EIPs/pull/233).

Dimitry: As far as implementation, we already did REVERTCALL tests and I've seen some client implement general state tests. If client's submit their general state tests Martin H.S can run the tests on Hive once I convert them into generic blockchain tests. Every client that implements these protocol tests will be tested using Hive. Not every test is converted to Hive yet, but the general state tests are the most updated one. Transaction tests are halfway done. We are now using a branch on the test repository so every change will be in a different branch. [Please review this document I have created and contribute feedback about the test coverage](https://docs.google.com/spreadsheets/d/1xat7UI8GtB4ZGVdlK5_XQSHJZaMThi4SrlcL8XMZb5Q/edit#gid=0).

Hudson: Great. What is the best way to communicate with you to send data?

Dimitry: Gitter and Skype.

### Updates from clients on Metro implementation of EIPs

- Parity: We are almost done. Just waiting on finalization of the pending EIPs.
- cpp-ethereum: We are somewhere in the middle, but don't have exact details on where we are at. It depends on the EIP, some are done and some are getting started.
- Geth: Jeff is handling Metro EIPs, but has been busy recently. It appears that most of the metro EIPs are done.
- pyethereum: We are mostly concerned with getting back to being able to sync to the main chain.

Basically, all EIPs that are going in to metro are finalized, but next meeting we will double check. Many of the EIPs are submitted, but the specs are being tweaked.

## 5. Other topics

### Transaction propagation issues and potential solutions [Peter]

Peter: We have discussed this in the past, but we are trying to sort out how to sort out transaction propagation issues. One of the current issues with transactions are that they have an infinite lifetime. If I create a transaction today, it could be included now or in 10 years. The Bitcoin network was spammed last year and transactions that were sent as part of that spam persisted in the network for 8 months. It would be nice if we could avoid issues like that by saying a transaction has a limited lifetime to propagate cheap transactions easier. Does someone want to do an EIP on this?

Nick: I think this is a great idea. I will write an EIP on this.

[Additional discussion on this is included in the audio, including the breaking of offline signing of transactions.]

### Making RETURNDATACOPY and CALLDATA to throw in certain situations [Nick]

Nick: I discussed this in some chat channels, but wanted to talk about the possibility of making RETURNDATACOPY throw if you attempt to copy beyond the end of RETURNDATA and CALLDATA in Metropolis to throw if a contract requests data beyond the end of the call data, instead of returning 0s. Motivation: Currently we pad it with 0's, but IMO this is us assuming what the user wants. This may help prevent the issues that exchanges had surrounding the Golem ERC20 token exchange implementation flaw (or attack).

Nick has been running some searches on the blockchain for contracts that seem to purposefully read past the end of call data. The only contracts so far that this has been found in is Augur related Serpent contracts due to a compiler optimizations in Serpent.

Discussion continues (see audio) about the balance of potentially breaking contracts that rely on this behavior (and potential EVM consistency and complexity) vs the benefits of making this change. Nick is going to comment on the existing EIP and continue his tests to discuss this issue more in the future.

## Attendance

Alex Beregszaszi (EWASM), Andrei Maiboroda (cpp-ethereum), Arkadiy Paronyan (Parity), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum/Solidity), Dimitry Khokhlov (cpp-ethereum), Frankie Pangilinan (MetaMask), Greg Colvin (EVM), Hudson Jameson (Ethereum Foundation), Konrad Feldmeier (pyethereum), Martin Becze (EWASM/EthereumJS), Martin Holst Swende (geth/security), Paweł Bylica (cpp-ethereum), Péter Szilágyi (geth)
