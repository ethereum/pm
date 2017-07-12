# All Core Devs Meeting 19
### Meeting Date/Time: Friday 6/30/17 at 14:00 UTC
### Meeting Duration 2 hours
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=wLaI7680I4w)
# Agenda

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

# Notes
TODO

## Attendance
Alex Beregszaszi (EWASM), Alex Van de Sande (Mist/Ethereum Wallet), Andrei Maiboroda (cpp-ethereum), Arkadiy Paronyan (Parity), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum/Solidity), Daniel Nagy (SWARM), Dimitry Khokhlov (cpp-ethereum), Hudson Jameson (Ethereum Foundation), Lefteris Karapetsas (Raiden), Martin Holst Swende (geth/security), Matthew Di Ferrante (geth/security), Nick Johnson (geth/SWARM), Péter Szilágyi (geth), Vitalik Buterin (Research & pyethereum), Yoichi Hirai (EVM)
