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

# Notes
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

## Attendance

Alex Beregszaszi (EWASM/Solidity), Afri Schoedon (Parity), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum/Solidity), GhaS Shee (Unknown), Greg Colvin (EVM), Hudson Jameson (Ethereum Foundation), Martin Holst Swende (geth/security), Mikhail Kalinin (Harmony), Péter Szilágyi (geth), Piper Merriam (pyEVM), Vitalik Buterin (Research & pyethereum), Yoichi Hirai (EVM)
