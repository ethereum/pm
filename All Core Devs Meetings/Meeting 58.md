# Ethereum Core Devs Meeting 58 Notes
### Meeting Date/Time: Friday, March 29, 2019 14:00 UTC
### Meeting Duration:  ~1 hour
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/89)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=v8Psbo8zY4Y)
### Moderator: Hudson Jameson

# Summary

### DECISIONS MADE

**DECISION 58.1** The [ProgPoW Carbon Vote](http://www.progpowcarbonvote.com/) signal will be shutting down in 13 days from today. Everyone that wishes to vote will need to do so before this date and ensure they leave their ETH in the address they voted from until after block number 7504000, as per [Lane's tweet](https://twitter.com/lrettig/status/1111652965331415040).

**DECISION 58.2** Going forward Clients will not provide generic verbal updates in the meeting but should provide an update in the comments in the agenda. If there are any questions or anything specific to discuss a space will be left to do so.

**DECISION 58.3** Going forward Reseach will not provide generic verbal updates but should provide an update in the comments in the agenda. If there are any questions or anything specific to discuss a space will be left to do so.

### ACTIONS REQUIRED

**ACTION 58.1** Cat Herders to look at updating EIP1, see [here](ethereum-cat-herders/PM#19).

**ACTION 58.2** Review the proposed solutions for Roadmaps in the [Ethereum Magicians](https://ethereum-magicians.org/t/more-frequent-smaller-hardforks-vs-less-frequent-larger-ones/2929) forum to decide if going forward the Core Devs adopts smaller hardforks rather than larger hardforks.

**ACTION 58.3** Vitalik to format the currently proposed [EIP-1559](ethereum/EIPs#1559) so that it is correctly presented.

**ACTION 58.4** Lane to provide a block number for when the [ProgPoW Carbon Vote](http://www.progpowcarbonvote.com/) will be shutdown.

**ACTION 58.5** Discuss if ProgPoW should continue to be implemented if the Technical Audit is not funded in [Ethereum Magicians](https://ethereum-magicians.org/tags/progpow) or [here](https://ethereum-magicians.org/t/what-has-to-be-done-to-get-progpow-on-ethereum/1361) or [here](https://ethereum-magicians.org/t/motion-to-not-include-progpow-without-audit/3027).

**ACTION 58.6** Clients should provide updates for future Core Dev Calls in the comments of the agenda and request an update to the agenda if they wish to discuss anything specific. 

**ACTION 58.7** Research should provide updates for future Core Dev Calls in the comments of the agenda and request an update to the agenda if they wish to discuss anything specific. 

**ACTION 58.8** Alexey to create a Beacon Chain Finality Gadget initiative working group and find someone to lead it, for context please see discussion in [Ethereum Magicians](https://ethereum-magicians.org/t/eth2-in-eth1-light-clients/2880).


# 1. [Roadmap](https://en.ethereum.wiki/roadmap/istanbul)

**Hudson:** We have tentative dates for the roadmap. For example, 17 May is the deadline for EIP proposal for Istanbul and the 19th July is the deadline for major client implementations.

**Alexey:** There is a discussion in the Ethereum Magicians regarding having multiple smaller forks or one larger grouped Hardforks.

**Martin:** Larger Hardforks requires more testing. Might be easier if the Hardforks are smaller or spread out.

**Dmitry:** Better to have smaller hardforks.

**Alexey:** What is the reason behind this?

**Dmitry:** The biggest reason is the time it takes to create the json test cases.

**Alexey:** Perhaps we should help train EIP proposers to create json tests for their EIPs?

**Boris:** Agree - we need to improve the number of people doing testing.

**Martin:** This is happening under the Python wing with Piper.

**Lane:** There has been a parallel Ethereum Magicians thread on improving the quality of EIP authors.

**Martin:** If it is easy to write a test no problem. But if it is a lot harder then that is different story.

**Alexey:** If the proposer creates a set of tests and are reviewed by the testing team and passed back to the EIP proposer for improvement then that may work?

**Hudson:** We would perhaps need to change EIP1 and this needs to be upgrade regardless for things like what it means to have something rejected and accepted. What happens with ERCs? 

**Boris:** Could be handled in the EIP233 - the Hard Fork Meta.

**Lane:** Let's make the updating of EIP1 a Cat Herder Task? 

**Boris:** Tim has spoken about this and so yes it is happening.

** **
**ACTION 58.1** Cat Herders to look at updating EIP1, see [here](ethereum-cat-herders/PM#19).
** **


**Lane:** Question around 17 May deadline? Do the EIPs need to be fully formed or can they be placeholders?

**Alexey:** If we introduced a pipeline of EIPs then we will not have rushing in of EIPs. If the hardfork timelines are shorter then that may also help without rushing it in. 3 months is less stressful than knowing if you miss this hardfork you will have a 9 month delay before you will get it in. Therefore, in this way placeholder EIPs in hardforks should not be included, instead they should be more fully formed.

**Boris:** Agreed. Will add to EIP 233 to include a proposal section.

**Martin:** We should change the process to be EIP centric rather than Hardfork centric. 

**Boris:** Agreed.

**Pooja:** We are proposing a seperate EIP managing process for Hardfork specifically. 

**Hudson:** If we have smaller forks then Martin's proposal for EIP centric is better. If it remains for larger hardforks then Pooja's suggestion works. 


** **
**ACTION 58.2** Review the proposed solutions for Roadmaps in the [Ethereum Magicians](https://ethereum-magicians.org/t/more-frequent-smaller-hardforks-vs-less-frequent-larger-ones/2929) forum to decide if going forward the Core Devs adopts smaller hardforks rather than larger hardforks.
** **


# 2. EIPs

## 2.1 [EIP 1599 - Fee Market Change for Eth 1.0 Chain](https://ethereum-magicians.org/t/eip-1559-fee-market-change-for-eth-1-0-chain/2783)

**Hudson:**  Vitalik is not here to discuss this.


** **
**ACTION 58.3** Vitalik to format the currently proposed [EIP-1559](ethereum/EIPs#1559) so that it is correctly presented.
** **


## 2.2 [Ethereum Network Upgrade Windows](https://github.com/shemnon/EIPs/blob/4e3069b4f9a30a639b142151dc6295f634712786/EIPS/eip-network_upgrade_windows.md)

**Danno:** Suggests quarterly dates for hardforks and the dates proposed miss most holidays. Three types of upgrades: Roadmap, Priority, Critical. 

**Alexey:** Support it as it provides certainty for certain groups.

**Pawel:** I am not sure about this until we have seen our current process run through smoothly.

**Danno:** We need some certainty if we go for a quarterly process. There is a an Ethereum Magicians thread. 

**Lane:** Just to confirm what Pawel is saying, we should stick with the plans that we have now and move to the quarterly after this.

**Danno:** My proposal works with Istanbul's current proposed date.

## 2.3 [EIP - Opcode repricing for trie-size-dependent opcodes](https://github.com/holiman/EIPs/blob/reprice/EIPS/eip-1884.md)

**Martin:** This focuses on trying to make operations that have deteriated over time and put them back in balance again. The ones I am specifically looking at are `SLOAD` and `BALANCE`. There are two versions to this EIP. In both of them they increase `SLOAD` by a factor of 4 from `200` to `800` and the `BALANCE` would be repriced from `400` to `700` gas.

Version B would introduce an opcode called `SELFBALANCE` which would be priced very cheaply as `GasFastStep` at `5` gas.

There is something that can be done to make all opcodes more equivalent but that is not a concern for this EIP.

Would be great to have some feedback on this before it is finalised.

# 3. Working Group Updates

**Hudson:** There is a very [detailed update](https://github.com/ethereum/pm/issues/89#issuecomment-477954769) in the bottom of the agenda provided by Alexey.

**Alexey:** Yesterday I published the stateless client prototype so esentially collecting data on how big these block proofs would be, identify the next steps and to ensure that the next steps are to lower the bandwidth requirement by using some more statefulness or to use Starks.

I would like some feedback on is something that came up some time ago, "Probablistic Estimation of Contract Sizes". Esentially one of the issues found in the State Rent and is now in the syncing protocols is to trying to figure out the size of the contract. How many items does the contract storage have. For state rent proposal the idea was to introduce it into the state over two stages using two hard forks. Having thought about it sometime ago I realised that you could estimate, no precisely but approximately, the size of the contract by using the hash function Keccak256 has some kind of random oracle property and I will probably publish it in a couple of days.

From section 4 in my update, if we could bring forward change J (fixed prepayment for contract storage) this would be the requirement to increase the block size limit as it would stop the acceleration of state growth. I am hoping that this change could be brought forward to one of the first hardforks so that we could do the harmless block gas limit increase earlier.

From section 6 in my update, I am looking to do some more work on linear storage to integrate with the eWASM engine but I am waiting to hear back from eWASM before I launch in.

## 3.5 [Istanbul & ETH1x Roadmap Planning Meeting - April 17th & 18th in Berlin](https://ethereum-magicians.org/t/istanbul-eth1x-roadmap-planning-meeting-april-17th-18th-in-berlin/2899)

**Boris:** Confirmed for Full Node. Thank you Gnosis for hosting. We are looking to use the live meeting to discuss EIPs. A ton are related to precompiles. We can use this forum to discuss what a more continuous EIP process looks like. 25 people have confirmed.

**Lane:** Confirm there with be a remote stream for those who cannot make it?

**Boris:** Yes there will be.

**Alexey:** Encourage Geth and Parity clients to attend this meetup.

**Lane:** If we do adopt a quarterly hardfork process then we can plan events like this well in advance.

**Guillaume:** Where can I find the proposed EIPs for the hardfork?

**Boris:** We are keeping the [roadmap](https://en.ethereum.wiki/roadmap/istanbul) in ethereum wiki up to date. Ideally this will move to github so that you can track a feed.


# 4. ProgPoW Audit Update & Carbonvote Being Taken Down

**Hudson**: Won't discuss ProgPoW but will give an update.

**Lane:** Carbon Vote will be shutdown in 13 days time, I will hardcode that to a specific block number and will publish the block number. The ETH needs to be in the account up to and including the final block.



** **
**ACTION 58.4** Lane to provide a block number for when the [ProgPoW Carbon Vote](http://www.progpowcarbonvote.com/) will be shutdown.
** **

** **
**DECISION 58.1** The [ProgPoW Carbon Vote](http://www.progpowcarbonvote.com/) signal will be shutting down in 13 days from today. Everyone that wishes to vote will need to do so before this date and ensure they leave their ETH in the address they voted from until after block number 7504000, as per [Lane's tweet](https://twitter.com/lrettig/status/1111652965331415040).
** **


**Hudson:** The funding of the [ProgPoW Technical Audit](https://gitcoin.co/grants/82/official-progpow-technical-audit-funding) is not going as well as hoped. We will continue to seek funds and will provide further details next time. 

**Greg:** Is this audit a show stopper?

**Hudson:** If we cannot fund the Technical Audit then Core Devs will need to decide whether to go ahead with ProgPoW without a Technical Audit.

**Danny:** It is reasonable to accept that we can make a final decision as more information becomes available.

**Ameen:** Will ProgPoW be implemented if the Audit is not funded?

**Hudson:** We cannot answer that question at this time.

**Hudson**: Let's continue to discuss this in Ethereum Magicians.


** **
**ACTION 58.5** Discuss if ProgPoW should continue to be implemented if the Technical Audit is not funded in [Ethereum Magicians](https://ethereum-magicians.org/tags/progpow) or [here](https://ethereum-magicians.org/t/what-has-to-be-done-to-get-progpow-on-ethereum/1361) or [here](https://ethereum-magicians.org/t/motion-to-not-include-progpow-without-audit/3027).
** **



# 5. Testing Updates

**Dimitry:** I have completed my retested application on blockchain test. So now we could run all of the blockchain tests including the general state tests in a blockchain form on any client that supports RPC interface which was describe on the testnet wiki page. I also have instructions to use docker build so that you can run it on your client if you support this interface.

Also, I have been thinking, similar to us using fixed EIP numbers, we could use fixed fork numbers to identify hard forks. I have proposed [EIP-1848](https://github.com/ethereum/EIPs/pull/1848) to standardise the naming of forks. It is assists massively with discussion, testing and code and avoids confusion if forks change due to unforseen circumstances for example the recent Constantinople and St Petersburg releases.

# 6 . Client Updates 

**Hudson:** Are these client updates useful? 

**Fredrik:** I personally am not sure what to report here.

**Danno:** Client updates gives an attendance reports. 


** **
**DECISION 58.2** Going forward Clients will not provide generic verbal updates in the meeting but should provide an update in the comments in the agenda. If there are any questions or anything specific to discuss a space will be left to do so.
** **

** **
**ACTION 58.6** Clients should provide updates for future Core Dev Calls in the comments of the agenda and request an update to the agenda if they wish to discuss anything specific. 
** **



# 7. EWASM & Research Updates 

**Hudson:** Who feels we need research updates?

**Danny:** Having space for them seems reasonable.

**Lane:** Provide text updates as comments in the agenda and then only discuss questions. Saves time.


** **
**DECISION 58.2** Going forward Researchers will not provide generic verbal updates in the meeting but should provide an update in the comments in the agenda. If there are any questions or anything specific to discuss a space will be left to do so.
** **

** **
**ACTION 58.7** Research should provide updates for future Core Dev Calls in the comments of the agenda and request an update to the agenda if they wish to discuss anything specific. 
** **

**Hudson:** Do we have any research updates?

**Alexey:** I know most research updates relate to Ethereum 2.0 but I want to create a new working group within Ethereum 1.x with a goal of creating proposal where the Beacon Chain is being used as the Finality Gadget. Not sure who will lead it.
Danny: I would be keen to be part of it, this is a key initiative and appears to be something people want.


** **
**ACTION 58.8** Alexey to create a Beacon Chain Finality Gadget initiative working group and find someone to lead it, for context please see discussion in [Ethereum Magicians](https://ethereum-magicians.org/t/eth2-in-eth1-light-clients/2880).
** **


**Hudson**: Any Ethereum 2.0 research updates?

**Danny:** Phase 1 dsicussion is currently very active whilst Phase 2 is still emerging, the design space in Phase 2 is pretty large so we need to narrow things down. Many of the Ethereum 2.0 Beacon Chain clients are getting Testnet data so we expect to see some exciting stuff in the next couple of weeks.

**David:** We had a Beta release last week that introduced a new algorythm for gas estimation that is very accurate down to 1 gas even for [EIP-1014](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1014.md) opcodes and it does not use binary search so it only requires one pass through the transaction outcodes to get the esimation. We call it "Gas Exactimation". We are planning on writing a detailed blog post on the algorithm and how it works. We believe it is something that alot of other clients could make use of for performance reasons. More info can be found [here](https://github.com/ethereum/pm/issues/89#issuecomment-478030037).

# 8. Other Business

**Pawel:** We are preparing to implement this new discovery protocol for devp2p, what I understand geth already have. It is an ongoing effort and if you would like to comment or change out minds, let us know.

**Hudson:** Will not be on the call next week. Will find another moderator for the next meeting probably from the Cat Herders.

# Date for next meeting
April 12, 2019 at 14:00 UTC

# Attendees
* Alexey Akhunov (Ethereum)
* Ameen Soleimani (SpankChain)
* Borris Mann (Fellowship of Ethereum Magicians)
* Brett Robertson (Ethereum Cat Herders)
* Brooklyn Zelenka (SPADE)
* Charles St Louis (Ethereum Cat Herders)
* Daniel Ellison (ConsenSys)
* Dankrad Feist (Ethereum 2.0)
* Danno Ferrin (Pantheon)
* Danny Ryan (Ethereum 2.0)
* David Murdoch (Ethereum/eWASM)
* Dimitry Khoklov (Ethereum)
* Eric Kellstrand (Pantheon)
* Felix Lange (Geth)
* Fredrik Harrysson (Parity)
* Greg Colvin (Fellowship of Ethereum Magicians)
* Guillaume Ballet (Ethereum)
* Hudson Jameson (Ethereum)
* Ivaylo (Web3Labs)
* Jacek Sieka (Nimbus)
* Jason Carver (Trinity/PyEVM)
* JosephC 
* Lane Rettig (Ethereum)
* Meredith Baxter (Pantheon)
* Martin Holst (Ethereum)
* Mikhail Kalinin (EthereumJ/Harmony)
* Mikerah (Ethereum 2.0)
* Pooja Ranjan (Ethereum Cat Herders)
* Tim Beiko (Pantheon)
* Trenton Van Epps 

