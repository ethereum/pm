# Ethereum Core Devs Meeting #23
### Meeting Date/Time: Friday 8/25/17 at 14:00 UTC
### Meeting Duration 1.5 hours
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=PQjeAZyL2_w)
### [Reddit thread](https://www.reddit.com/r/ethereum/comments/6w29zk/metropolis_and_other_updates_from_todays_core_dev/)

# [Agenda](https://github.com/ethereum/pm/issues/21)

**Reminder: Metropolis is now split into 2 hard forks: "Byzantium" first and then "Constantinople".**

1. Metropolis updates/EIPs.
  **a. Any "subtleties" or questions we need to work out.**
      - JSON RPC updates needed by the receipt status change EIP. [Peter]
      - [EIP 649: Metropolis Difficulty Bomb Delay and Issuance Reduction](https://github.com/ethereum/EIPs/pull/669): Community concerns need to be addressed [Hudson]
  **b. Updates to testing.**
  **c. Details and implementations of EIPs.**
        1. Updates from client teams.
            - geth - https://github.com/ethereum/go-ethereum/issues?q=label%3Ametropolis+is%3Aclosed
            - Parity - https://github.com/paritytech/parity/issues/4833
            - cpp-ethereum - https://github.com/ethereum/cpp-ethereum/issues/4050
            - ethereumJ
            - yellowpaper -  https://github.com/ethereum/yellowpaper/issues/229
            - pyethapp
            - Other clients
        2. Determining gas prices for new opcodes & pre-compiles [Martin HS/Arkadiy]
  **d. Review time estimate for testing/release.**

# Notes
### Reminder: Metropolis is now split into 2 hard forks: "Byzantium" first and then "Constantinople".

### Ice Age Updates

Block times:

- 23 seconds now (block #4200000)
- 30 seconds on Sept. 22nd (block #4300000)
- 39 seconds on Oct. 27th (block #4400000)

### EIP 649 Discussion

[EIP 649: Metropolis Difficulty Bomb Delay and Issuance Reductio discussion](https://github.com/ethereum/EIPs/pull/669).

- /u/kybarnet kindly joined the call ([starting at 9:29](https://youtu.be/PQjeAZyL2_w?t=569)) to discuss the issuance reduction and to argue for a further reduction.
- There are others in the community, notably /u/DeviateFish_, who argue that there should be no issuance reduction, but unfortunately they were unable to join the call.
- The conclusion we came to in the call was to keep the issuance reduction for the Byzantium hard fork to 3 ETH in accordance with [EIP 649](https://github.com/ethereum/EIPs/pull/669).
- It is unfortunate that certain parties in the discussion ([particularly TheCryptoMines](https://github.com/ethereum/pm/issues/21#issuecomment-324893807)) felt left out and I want to find ways in the future to include everyone in the conversation around EIPs and network changes.
- I address this specifically at [1:04:43](https://youtu.be/PQjeAZyL2_w?t=3883) and Martin H.S provides good commentary at the end of the discussion.
- It should be noted that changes like this can be reversed or modified in future hard forks with enough community and developer consensus.
- Other posts and opinions from /u/DeviateFish_ and TheCryptoMines can be found [here](https://github.com/ethereum/pm/issues/21).

### Metropolis Testing

- The testing team has grown significantly from 3 people to 7 people ([starts at 37:05](https://youtu.be/PQjeAZyL2_w?t=2225)).
- Big shout out to Dimitry, Casey D., Yoichi, Martin H.S, Tim S., Jared W., Matthew E. who have contributed to the testing efforts!
- Testing is proceeding more smoothly and major clients, including Parity and geth, have implemented most or all of the EIPs that are going into Byzantium.
- /u/cdetrio created an awesome tool for running state tests on multiple clients ([starts at 40:41](https://youtu.be/PQjeAZyL2_w?t=2441))
- Tim S. (Testing), Arkidiy (Parity), and Martin H.S (Testing) will be working to get the opcode benchmarks necessary to complete gas cost analysis prior to launching Byzantium on the testnet.

### Launching the First Part of Metropolis: Byzantium ([starts at 56:36](https://youtu.be/PQjeAZyL2_w?t=3396))

- Within the next 7-10 days we should have benchmarks for gas costs completed.
- Once the gas costs benchmarks are finalized and the clients complete implementation of the [Byzantium EIPs](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-609.md), we will launch a hard fork on the Ropsten testnet that would run for 2-4 weeks.
- Ropsten is hard to sync, so we will look into finding creative ways for people to more easily sync Ropsten. Example: Use lightsync, fastsync, or warpsync, depending on client.
- Block number for the mainnet hard fork will be decided soonish. Ballpark block numbers are : block 4.3 million on Sept. 22nd and worst case is block 4.4 million Oct. 27th, so the hardfork will likely be between those two times. We are aiming for sometime late September.

### Clients represented in the meeting

- geth (Go)
- Parity (Rust)
- cpp-ethereum (C++)
- pyethapp (Python)
- ethereumJS (Javascript)
- ethereumJ (Java)

## Attendance