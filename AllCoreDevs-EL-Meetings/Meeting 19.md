# All Core Devs Meeting 19
### Meeting Date/Time: Friday 6/30/17 at 14:00 UTC
### Meeting Duration 2 hours
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=wLaI7680I4w)
### [Reddit thread](https://www.reddit.com/r/ethereum/comments/6kaetr/live_stream_ethereum_core_developer_meeting/)

# [Agenda](https://github.com/ethereum/pm/issues/17)

# Notes

## [Brickoliciousness summary on YouTube comments](https://www.youtube.com/watch?v=wLaI7680I4w&lc=z12evpdw1uv2e5q3v22bttj42sbksplrg04)

There is a lot of technical insight and status updates during this meeting, most of them are not useful information for anyone other than the actual developers (unless you are really nerdy, or malicious). However there are two rather insightful points on the agenda that i will share with you.

They have discovered several issues (or concerns) related to the implementation of EIP #208 (formerly EIP #86) - Which is related to Abstraction of transaction origin and signatures.
 
Contract addresses cannot be computed (or rather guaranteed) without a live blockchain.
Problem with calculation. Can calculate the final address, but cannot calculate the ownership for sure.
Problem where circumstances can result in the same contract addresses. You can actually lose ownership if you do not explicitly state in the contract that you own it.
Problem where an exploit could allow a miner to execute a transaction 10 times.
 
There is suggestions to solve most of these issues, some are however imperfect, and would still apply to transaction where the sender is null. //Not sure how common that is?
 
The problems are considered to be severe if not taken care of, and culminates in a discussion about (just skipped 40mins of updates): “if the problems related to EIP #86 is not handled, do we then have to push the release of metropolis?”
 
If these problems are not handled, they are seriously considering to split the release of Metroplis into two hard forks - "In software engineering, a project fork happens when developers take a copy of source code from one software package and start independent development on it, creating a distinct and separate piece of software" (from wikipedia). //Hard forking the project would be a hassle to say the least, and it would mean that the release (currently) scheduled for september would not include all the features promised.
 
This however all depends on the progress on EIP-86 within the next two weeks, most people seem cheerful about the schedule, but if the open issues - explained above - remain unsolved, some features will most likely miss the deadline. 

[00:00](https://www.youtube.com/watch?v=wLaI7680I4w&t=0s) - [33:40](https://www.youtube.com/watch?v=wLaI7680I4w&t=2020s)  Talk about issues with a switch from EIP #86 to #208, where there are some messy issues that needs taken care of, possible exploits, with execution of transaction multiple times. Problem where circumstances can result in the same contract addresses; You can actually lose ownership if you do not explicitly state in the contract that you own it. //problem would be malicious miners
 
[33:40](https://www.youtube.com/watch?v=wLaI7680I4w&t=2020s) - [35:44](https://www.youtube.com/watch?v=wLaI7680I4w&t=2144s) EIP #86 Transaction origin. His name was Jeff, and he was not there.
 
[35:45](https://www.youtube.com/watch?v=wLaI7680I4w&t=2145s) - [38:00](https://www.youtube.com/watch?v=wLaI7680I4w&t=2280s) How to handle the up and coming difficulty bomb - implement an if sentence (if metropolis) that delays the issue. Will be added to EIP #86.
 
[38:00](https://www.youtube.com/watch?v=wLaI7680I4w&t=2280s) - [48:00](https://www.youtube.com/watch?v=wLaI7680I4w&t=2880s) Random selection of updates.
 
[48:15](https://www.youtube.com/watch?v=wLaI7680I4w&t=2895s) - [54:30](https://www.youtube.com/watch?v=wLaI7680I4w&t=3270s)  Determining gas prices for new opcodes & pre-compiles, also ([49:49](https://www.youtube.com/watch?v=wLaI7680I4w&t=2989s) Daniels mic is initially pretty bad. //That is honestly an understatement)
 
[54:39](https://www.youtube.com/watch?v=wLaI7680I4w&t=3279s) - [58:00](https://www.youtube.com/watch?v=wLaI7680I4w&t=3480s) Time estimates for testing for different EIP’s that clients can run, and what is ready to be released. Conclusion about the middle of august. Release for metropolis is thereforeideally september:
 
[58:45](https://www.youtube.com/watch?v=wLaI7680I4w&t=3525s) - [1:11:00](https://www.youtube.com/watch?v=wLaI7680I4w&t=4260s) Discussion about hard forking metropolis ([1:10:16](https://www.youtube.com/watch?v=wLaI7680I4w&t=4216s) Summary of the hard fork discussion)
 
[1:11:00](https://www.youtube.com/watch?v=wLaI7680I4w&t=4260s) Discussion about the block gas limit increase.

[1:17:00](https://www.youtube.com/watch?v=wLaI7680I4w&t=4620s) - [1:29:00](https://www.youtube.com/watch?v=wLaI7680I4w&t=5340s) EIP 186: Reduce ETH issuance before proof-of-stake - discussing how to keep the block reward pr. Sec the same after switch to the proof of stake. Should you set the issuance rate to dollar prices? ([1:21:28](https://www.youtube.com/watch?v=wLaI7680I4w&t=4888s) Question about extreme scenario: about proof of stake)
 
[1:29:00](https://www.youtube.com/watch?v=wLaI7680I4w&t=5340s) - [1:50:31](https://www.youtube.com/watch?v=wLaI7680I4w&t=6631s) discussion about information regarding transaction fails, and minor structural changes.﻿

## My notes:

1. Metropolis updates/EIPs.

  **a. Any "subtleties" or questions we need to work out.**
  
  [[4:14](https://youtu.be/wLaI7680I4w?t=253)] 1. [EIP 86/208: Abstraction of transaction origin and signature](https://github.com/ethereum/EIPs/pull/208) - Contract addresses cannot any more be computed (or rather guaranteed) without a live blockchain, and even then we have no guarantee that a deployed code is ours (or that it remains ours in the face of reorgs). [Peter]

  [[]()] 2. [EIP 86/208: Abstraction of transaction origin and signature](https://github.com/ethereum/EIPs/pull/208) - Discuss the comment here https://github.com/ethereum/EIPs/pull/208#issuecomment-311985691 and further refined by https://github.com/ethereum/EIPs/pull/208#issuecomment-312029135 [Peter]
        
  [[]()] 3. [EIP 86/208: Abstraction of transaction origin and signature: Atomicity over an ECDSA's accounts operations](https://github.com/ethereum/EIPs/pull/208#issuecomment-307681408) [Jeff Coleman]
        
  [[34:10](https://youtu.be/wLaI7680I4w?t=2050)] 4. [Metropolis Difficulty Bomb EIP](https://github.com/ethereum/EIPs/issues/649) [Everyone]
        
**b. Updates to testing.**
- [[37:45](https://youtu.be/wLaI7680I4w?t=2265)] Documentation and other updates

**c. Details and implementations of EIPs.**
  
- [[41:44](https://youtu.be/wLaI7680I4w?t=2504)] Updates from client teams.
    - geth - https://github.com/ethereum/go-ethereum/pull/14337
    - Parity - https://github.com/paritytech/parity/issues/4833
    - cpp-ethereum - https://github.com/ethereum/cpp-ethereum/issues/4050
    - yellowpaper -  https://github.com/ethereum/yellowpaper/issues/229
    - pyethapp
    - Other clients
    
**d. [[48:16](https://youtu.be/wLaI7680I4w?t=2896)] Review time estimate for testing/release.**

[[]()] 2. [Block gas limit increase update](https://www.reddit.com/r/ethereum/comments/6k769r/ethpool_ethermine_are_now_targeting_a_block_gas/) [Hudson]

[[1:16:34](https://youtu.be/wLaI7680I4w?t=4594)] 3. [EIP 186: Reduce ETH issuance before proof-of-stake](https://github.com/ethereum/EIPs/issues/186) [[Vitalik/Avsa/Nick have comments](https://github.com/ethereum/pm/issues/17#issuecomment-312063219)]

## Attendance
Alex Beregszaszi (EWASM), Alex Van de Sande (Mist/Ethereum Wallet), Andrei Maiboroda (cpp-ethereum), Arkadiy Paronyan (Parity), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum/Solidity), Daniel Nagy (SWARM), Dimitry Khokhlov (cpp-ethereum), Hudson Jameson (Ethereum Foundation), Lefteris Karapetsas (Raiden), Martin Holst Swende (geth/security), Matthew Di Ferrante (geth/security), Nick Johnson (geth/SWARM), Péter Szilágyi (geth), Vitalik Buterin (Research & pyethereum), Yoichi Hirai (EVM)
