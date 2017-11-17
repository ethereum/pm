# Ethereum Core Devs Meeting 28 Agenda
### Meeting Date/Time: Friday 11/17/17 at 14:00 UTC
### Meeting Duration 1 hours
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=8S-MEGYq_CI)
### [Reddit thread](https://www.reddit.com/r/ethereum/comments/7dl246/live_ethereum_core_devs_meeting_28_111717/)

# Agenda

1. Testing
2. Byzantium fork review
  a. Group to write EIP for future HF guidelines (Discussion from Devcon)
  b. Move EIPs activated Byzantium to Finalized
3. POA Testnet unification
4. Core team updates.
5. High-level overview of what's planned for Constantinople.

# Notes (Hudson)
Video starts at [7:42](https://youtu.be/8S-MEGYq_CI?t=462)

## [8:35](https://youtu.be/8S-MEGYq_CI?t=515) 1. Testing
Some test cases in the Google spreadsheet were not updated with the ones in the repository so that has started to be corrected.

## [9:44](https://youtu.be/8S-MEGYq_CI?t=584) 2. Byzantium Fork Review

### a. Group to write EIP for future HF guidelines (Discussion from Devcon)

Meeting was held during Devcon3 where we talked about the Byzantium release, issues we had, and how to improve in future hard forks. Some of the ideas discussed last time include hiring a dedicated release manager (or similar title/role), making a cadence for hard forks, and coming up with conditions for delaying a hard fork during network or client issues. For example: a 6 month cadence would allow for 1 month of deciding which EIPs will be in the fork, 2 months for implementation, and 3 months for testing. Having a little bit more structure around hard forks would also cause less confusion about which EIPs are going into the next hard fork. Nick and Martin H.S took notes at the meeting in Cancun and will start to form an EIP we can iteratively work on.

### b. Move EIPs activated Byzantium to Finalized
We are still working on this

## [24:43](https://youtu.be/8S-MEGYq_CI?t=1483) 3. POA Testnet Unification

Piper wants to form a small group of core devs (from Parity, Go, and Casper research team at minimum) to discuss a cross-client POA testnet. We discussed the current POA testnets (Kovan for Parity and Rinkeby for geth). An idea was floated to maybe have the next cross-platform testnet to be based on Casper to help test it.

## [39:49](https://youtu.be/8S-MEGYq_CI?t=2389) 4. Core team updates.

- geth - Felix is finalizing an EIP for the new discovery protocol which will help clients find each other (not necessarily go only, but an interesting development)
- cpp-ethereum - No updates.
- Parity - Changes in team structure. Some devs are not available anymore to work on the Parity Ethereum client. Afri or Marek will start attending the core dev meetings to represent Parity rather than Arkidiy. Major code refactoring and code audits are going on.
- ethereum-js - axic is finishing a proposal for an EWASM testnet that may be completed and running in January 2018.
- ethereumJ - Been working on a database issue that causes a huge memory footprint and slower processing speed. Next release will likely have a new database engine and Snappy compression.
- pyEVM - Byzantium rules are all passing in test. General plan has been developed with the Casper research team for migrating parts of the initial Casper codebase from pyethereum to pyEVM.
- pyethapp - Python3 compatibility.
- KEVM specification - Yoichi is working on this as well as a Casper accountability safety proof.

## [46:38](https://youtu.be/8S-MEGYq_CI?t=2798) 5. High-level overview of what's planned for Constantinople.
EIPs that would enable state size control measures such as dust account clearing are being considered. We need to perform some analysis on what the effects of this would be for the state size. This may be a good time to reduce gas cost for pre-compiles using an EIP. Account abstraction is still tentatively on the roadmap.
Two biggest questions around this are:
1. Do we need to change the nonce scheme in transactions?
2. Would changing the transaction format be useful for account abstraction?
Much of the potential changes to transaction formats need to have multiple parties involved including software and hardware wallets.
Technical details on the above can be viewed in the video.

## [58:25](https://youtu.be/8S-MEGYq_CI?t=3505) Other Stuff

### Ether recovery/rescue options
Currently Parity is taking point on formalizing and will release public proposals, like in the form of EIPs, to attempt to resolve the locked funds issue. Until that happens it will likely not be discussed in a core dev meeting.

# Notes (/u/ledgerwatch) [Located here](https://www.reddit.com/r/ethereum/comments/7dl246/live_ethereum_core_devs_meeting_28_111717/dpz7pea/)

1. Testing

Yoichi: some activity is happening in the repository, but I cannot see anyone who can explain it at the moment, in this meeting

2. Byzantium fork review

Hudson: During Devcon3, there was a core developers meeting, and lots of things were discussed. One of the most discussed was the dedicated role of a release manager. I used to do it in the past, but for Byzantium, I could not dedicate my full attention to it, that is why some of the things got left behind. The idea is to have a release manager as a full time position. Another topic was a cadence of releases. Peter, could you talk about how you are trying to schedule releases in geth?

Peter: generally we are trying to do bi-weekly releases. And the idea is quite simple - whatever makes it to master, gets released. This approach reduced the friction between the developers about when which things get included, compared to making releases every couple of months. The idea that was discussed was perhaps to use the similar process for the hard-forks. Currently, for the hard-fork, everyone has their “pet-EIP”, and then we start to delay the releases because some EIPs are missing.

Hudson: for hard-forks, obviously, it would not be 2-weeks cycle, but rather 6-8 months cycle.

Hard-fork guidelines: Martin will get the notes that he took at Devcon3, and then sent to Nick, and clean it up, to be discussed at the next meeting.

3. Proof of Authority testnet unification.

Peter: Kovan only works with Parity client, Rinkeby only works with geth. There is a demand for a common testnet that is more reliable than Ropsten. The question is: should geth implement Aura (mechanism behind Kovan), should Parity implement Clique (mechanism behind Rinkeby), or should both implement something new?

Casey: Kovan is contract-based, whereas Rinkeby is header-based. New Casper testnet is going to be contract-based. Idea - perhaps new Casper testnet could be this unification?

Vitalik: the properties of the Casper network is: if the attacker has more than 51% hashpower, he can prevent new blocks from being finalized, but he cannot revert the old blocks. And we can secure the PoS part by distributing lots of test Ether between ourselves and running Casper validators.

Piper: would like to form a small working group to work on the unification.

4. Core team updates

Geth team (Peter): The most interesting update is that Felix is finalising EIP proposal for the new discovery protocol.

Parity team changes its structure. Afri, Marek will most likely be point of contact for parity client in the future. Heavy refactoring of the code and auditing.

Casey: EthereumJS - eWASM testnet. Up and running sometime in January?

EthereumJ is looking into switching the database engine to RockDB (because current database engine is getting slow). Implementing snappy compression.

Piper: PyEVM (thinking about the new name for this client) - Byzantium rules passing on the testnet. Some work on light client.

Vitalik: working on lots of small things for Casper and Sharding, like incentivisation in Casper and stateless clients. PyEth-apps upgraded to Python 3 support.

Yoichi: trying KEVM as a specification. Spending some time on Casper accountable safety proofs for the more realistic cases where the validators can change.

5. General idea on what will be included in Constantinopole?

State size control (dust account clearing). Need a sorted list of account by balance, and see what happens if account with the balance smaller than X could be removed from the state.

Make better implementation for elliptic curves precompiles - reduce gas cost for them.

Account abstraction - keep thinking about it more. Whether the txs could be included multiple times (because of the abstraction of the nonce scheme). Account address generation scheme not to require the access to the blockchain state. Is changing transaction format in scope for Constantinopole? Changing tx format could make account abstraction cleaner. Hardware wallets, light clients, myetherwallet need to get involved in this discussion.

6. Ether recovery

It is too early to discuss any ether recovery plans because parity team is still doing some work on it.

## Attendance

Alex Beregszaszi (EWASM/Solidity), Afri Schoedon (Parity), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum/Solidity), GhaS Shee (Unknown), Greg Colvin (EVM), Hudson Jameson (Ethereum Foundation), Martin Holst Swende (geth/security), Mikhail Kalinin (Harmony), Péter Szilágyi (geth), Piper Merriam (pyEVM), Vitalik Buterin (Research & pyethereum), Yoichi Hirai (EVM)
