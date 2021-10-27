# Ethereum Core Devs Meeting #24
### Meeting Date/Time: Friday 9/8/17 at 14:00 UTC
### Meeting Duration 1.5 hours
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=_5Tp_U1jBww)
### [Reddit thread](https://www.reddit.com/r/ethereum/comments/6ywatn/notes_from_todays_ethereum_core_developer_meeting/)

# [Agenda](https://github.com/ethereum/pm/issues/22)

**Reminder: Metropolis is now split into 2 hard forks: "Byzantium" first and then "Constantinople".**

1. Metropolis updates/EIPs.
  **a. Any "subtleties" or questions we need to work out.**
          - [EIP96 = PR210](https://github.com/ethereum/EIPs/pull/210/files#r133664542) contains three different hex code for the BLOCKHASH contract, but there should be at most two (runtime code and initcode). [Yoichi]
          - [EIP #603: Add ECADD and ECMUL precompiles for secp256k1](https://github.com/ethereum/EIPs/issues/603). See [this comment](https://github.com/ethereum/pm/issues/22#issuecomment-326927267) for details and request to add to Constantinople. [Matthew D.]
  **b. Updates to testing.**
  **c. Details and implementations of EIPs.**
        1. Updates from client teams.
            - geth - https://github.com/ethereum/go-ethereum/issues?q=label%3Ametropolis+is%3Aclosed
            - Parity - https://github.com/paritytech/parity/issues/4833
            - cpp-ethereum - https://github.com/ethereum/cpp-ethereum/issues/4050
            - ethereumJ - https://github.com/ethereum/ethereumj/issues/923
            - ethereumJS
            - yellowpaper -  https://github.com/ethereum/yellowpaper/issues/229
            - pyethapp
            - Other clients
        2. Determining gas prices for new opcodes & pre-compiles [Martin HS/Arkadiy]
  **d. Review time estimate for testing/release.**

2. [EIP 706: Snappy compression for devp2p](https://github.com/ethereum/EIPs/pull/706) - very simple change yet reduces sync bandwidth by 60-80%. [Peter]

# Notes

## 1. Metropolis updates/EIPs.

### a. Any "subtleties" or questions we need to work out.

  - [0:36](https://youtu.be/_5Tp_U1jBww?t=36) Topic: [EIP96 = PR210](https://github.com/ethereum/EIPs/pull/210/files#r133664542) contains three different hex code for the BLOCKHASH contract, but there should be at most two (runtime code and initcode).
    - Resolution: Figured out on the call. Issue resolved.
  - [3:48](https://youtu.be/_5Tp_U1jBww?t=228) [EIP #603: Add ECADD and ECMUL precompiles for secp256k1](https://github.com/ethereum/EIPs/issues/603). See [this comment](https://github.com/ethereum/pm/issues/22#issuecomment-326927267) for details and request to add to Constantinople.
      - Resolution: Sounds like a good idea. Easy to add to all clients. Needs more feedback on the EIP PR and for editors to make sure it is correctly written. The change would be added to Constantinople if it is accepted. We will discuss official acceptance in future meetings.

### b. Updates to testing.


  - [9:23](https://youtu.be/_5Tp_U1jBww?t=563) On Hive multi-client cross-compatibility testing we are seeing better numbers wrt passing tests. geth has < 10 failing tests. cpp-ethereum has 700 errors, but because we cannot locally reproduce them there may be another unrelated issue causing it to fail. Many people pointed out mistakes in tests this week and that helped a lot. Parity is 

### c. Details and implementations of EIPs.

1. Implementation Updates
  - **geth** [12:01](https://youtu.be/_5Tp_U1jBww?t=721) - [Basically done besides some testing. peter spots a cat around [12:38](https://youtu.be/_5Tp_U1jBww)](https://github.com/ethereum/go-ethereum/issues?q=label%3Ametropolis+is%3Aclosed).
  - **Parity** [12:41](https://youtu.be/_5Tp_U1jBww?t=761) - [Basically done besides some state tests failing and implementing blockchain tests. Should be ready in 2-3 days. Parity team will work with Martin H.S to resolve issue of Parity not working in hive. Arkidiy is sending branch information to Martin.](https://github.com/paritytech/parity/issues/4833).
  - **cpp-ethereum** [13:38](https://youtu.be/_5Tp_U1jBww?t=818) - [Progress made. Several minor fixes occurred.](https://github.com/ethereum/cpp-ethereum/issues/4050).
  - **ethereumJ** [14:42](https://youtu.be/_5Tp_U1jBww?t=882) - [Implemented all EIPs. Passing all blockchain, state, and transition tests, but still needs to implement/update compatibility with the new test format and with Hive.](https://github.com/ethereum/ethereumj/issues/923).
  - **ethereumJS** [16:10](https://youtu.be/_5Tp_U1jBww?t=970) - As of this morning the elleptic pairing pre-compiles have been merged and all of the state tests are passing. About a dozen tests to debug. Expect to be passing blockchain tests soon.
  - **yellowpaper** [16:58](https://youtu.be/_5Tp_U1jBww?t=1018) - [Needs to add EIP 649, pointed out by /u/5chdn.](https://github.com/ethereum/yellowpaper/issues/229).
  - **pyethapp** [17:29](https://youtu.be/_5Tp_U1jBww?t=1049) No progress since last core dev call.
  - **Other clients** [17:40](https://youtu.be/_5Tp_U1jBww?t=1060) - No others in attendance. Afaik Ruby is deprecated and Haskell client (ethereumH) may no longer be actively maintained, not sure.

2. Determining gas prices for new opcodes & pre-compiles. 

  - [17:55](https://youtu.be/_5Tp_U1jBww?t=1075) Meeting occurred earlier in the week to discuss gas prices for Metropolis. Gas price benchmarks are complete and we are ready to confirm the suggestions created based on analysis of the benchmarks. This is will be discussed further in Gitter chat. More technical details discussed in the call.
  - [23:00](https://www.youtube.com/watch?v=_5Tp_U1jBww&t=1380s) Cat plays with squeaky mouse toy.

### d. Review time estimate for testing/release of Byzantium.

  - [24:27](https://youtu.be/_5Tp_U1jBww?t=1467) The testing team has determined that we are at a place where we can launch the testnet within two weeks, pending the resolution of the Hive consensus issues in CPP we are currently having.
  - Projected block times for mainnet:
    - 30 second block times on September 22nd
    - 39 seconds October 22nd
  - We set a target date for the Ropsten testnet hard fork for 10 days from now - September 18th. 
    - If testnet variables remain as they are now, that block number will likely be block number 1.7 million on Ropsten.
    - We will pick a block time that is around September 18th. This block number will be decided at 14:00 UTC Wednesday September 13th in the core developers chat.
    - We are picking the block number 5 days from now so we can account for difficulty adjustments on testnet that may occur between now and then. This allows us to pick a more accurate block number and adjust for mining changes on testnet.
    - These dates can be changed if we determine that we need more time for testing or major issues are found.
  - A mainnet fork block number will be decided around or after the testnet hard fork launches.
    - The testnet will run for at least 3 weeks, which would put a tentative main net hard fork date at October 9th.
    - These dates are very unofficial and can be changed if we determine that we need more time for testing or major issues are found. October 9th is a tentative date assuming that the testnet fork goes smoothly and no major issues are found.

## 2. [EIP 706: Snappy compression for devp2p](https://github.com/ethereum/EIPs/pull/706) - "very simple change yet reduces sync bandwidth by 60-80%."

  - [41:06](https://youtu.be/_5Tp_U1jBww?t=2466) [Active EIP PR discussion on-going](https://github.com/ethereum/EIPs/pull/706). Most clients are in favor of implementing this change besides Parity.
  - Arkidiy from Parity [suggests that this be made as an optional subprotocol](https://github.com/ethereum/EIPs/pull/706#issuecomment-328123598).
  - [Peter responds to Arkidiy](https://github.com/ethereum/EIPs/pull/706#issuecomment-328132190).
  - We will bring up this item in future core dev meetings. This change would affect the Ethereum network layer and not require a hard fork, just client agreement.

## Attendance