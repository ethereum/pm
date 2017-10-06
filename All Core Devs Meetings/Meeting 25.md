# Ethereum Core Devs Meeting #25
### Meeting Date/Time: Friday 9/22/17 at 14:00 UTC
### Meeting Duration 1.5 hours
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=wLaI7680I4w)
### [Reddit thread](https://www.reddit.com/r/ethereum/comments/72p924/notes_from_ethereum_core_devs_meeting_25_92217/)

# [Agenda](https://github.com/ethereum/pm/issues/23)

**Reminder: Metropolis is now split into 2 hard forks: "Byzantium" first and then "Constantinople".**

1. Metropolis updates/EIPs.
  **a. Any "subtleties" or questions we need to work out.**
          - [EIP #603: Add ECADD and ECMUL precompiles for secp256k1](https://github.com/ethereum/EIPs/issues/603). See [this comment](https://github.com/ethereum/pm/issues/22#issuecomment-326927267) for details and request to add to Constantinople. [Matthew D.]
  **b. Updates to testing.**
        1.  status/statusCode in receipts (eth rpc) [Arkidiy/Martin H.S]
        2. Hive tests update.
        3. Testnet launch update.
  **c. Details and implementations of EIPs.**
        1. Updates from client teams.
            - geth - https://github.com/ethereum/go-ethereum/issues?q=label%3Ametropolis+is%3Aclosed
            - Parity - https://github.com/paritytech/parity/issues/4833
            - cpp-ethereum - https://github.com/ethereum/cpp-ethereum/issues/4050
            - ethereumJ - https://github.com/ethereum/ethereumj/issues/923
            - ethereumJS - https://github.com/ethereumjs/ethereumjs-vm/issues/209
            - yellowpaper -  https://github.com/ethereum/yellowpaper/issues/229
            - pyethapp
            - Other clients
  **d. Review time estimate for testing/release.**

2. [EIP 706: Snappy compression for devp2p](https://github.com/ethereum/EIPs/pull/706) - very simple change yet reduces sync bandwidth by 60-80%. [Peter]
3. [EIP: 152 - BLAKE2b `F` Compression Function Precompile ](https://github.com/ethereum/EIPs/issues/152) [Zooko]
4. [EIP 718: Concurrency and locks for storage](https://github.com/ethereum/pm/issues/23#issuecomment-331381293)
5. [EIP 215: Bitwise shifting](https://github.com/ethereum/pm/issues/23#issuecomment-331443964)
6. [Account abstraction discussion](https://github.com/ethereum/pm/issues/23#issuecomment-331453630) - "I think we should also slowly bring up account abstraction again. How do the toolset providers think about it? Did we find better solutions in the meantime?"
7. ["Some way to reduce the gas costs for an SSTORE if that slot (or the whole contract) is destroyed at the end of the transaction ("ephemeral storage")."](https://github.com/ethereum/pm/issues/23#issuecomment-331454160)

# Notes

## 1. Metropolis updates/EIPs.

### a. Any "subtleties" or questions we need to work out.

  - [4:00](https://youtu.be/gxtftZB7_jA?t=240) [EIP #603: Add ECADD and ECMUL precompiles for secp256k1](https://github.com/ethereum/EIPs/issues/603). See [this comment](https://github.com/ethereum/pm/issues/22#issuecomment-326927267) for details and request to add to Constantinople. [Matthew D.]
    - Resolution: Will re-approach this item once Matthew D. is on the call next time.

### b. Updates to testing.

  1. [5:11](https://youtu.be/gxtftZB7_jA?t=311) status/statusCode in receipts (eth rpc) [Arkidiy/Martin H.S]
    - Resolution: status will be used.
  2. [6:10](https://youtu.be/gxtftZB7_jA?t=370) Hive tests update
    - Update: Going pretty good. geth has a few failures due to how empty accounts are handled, but this shouldn't be a problem in the future.
    - Parity and cpp are doing well on Hive and most of the errors are for small reasons. 
    - The one thing is that difficulty tests (outside of Hive) are lacking, but some of the testing team is working on it. ethereumJ is working on RLP and other tests before they begin Hive integration.
    - There is no work on pyethapp integrating with Hive currently, but there is work ongoing to get the block tests to work with pyethereum.
    - Pre-compile accounts on testnet and mainnet have been filled with at least 1 wei to avoid weird Spurious Dragon account #3 bug.
  3. [10:40](https://youtu.be/gxtftZB7_jA?t=640) Testnet launch update.
    - Byzantium fork on the Ropsten Ethereum testnet was successful.
    - We verified the zk-SNARK of a Zcash transaction on the testnet.
    - There is (or was) an attack on the Ropsten network. The block gas price on Ropsten was pushed down to 50gwi to mitigate the attack and that seems to have helped. The attack seems fairly inconsequential, but shows that Ropsten is a good test-bed for real world attacks.

### c. Details and implementations of EIPs.

1. Implementation Updates
  - **geth** [13:58](https://youtu.be/gxtftZB7_jA?t=838) - [No updates.](https://github.com/ethereum/go-ethereum/issues?q=label%3Ametropolis+is%3Aclosed).
  - **Parity** [14:22](https://youtu.be/gxtftZB7_jA?t=862) - [No major updates](https://github.com/paritytech/parity/issues/4833).
  - **cpp-ethereum** [14:36](https://youtu.be/gxtftZB7_jA?t=876) - [No updates](https://github.com/ethereum/cpp-ethereum/issues/4050).
  - **ethereumJ** [15:21](https://youtu.be/_5Tp_U1jBww?t=882) - [Passing all transition tests in Ropsten so things are good.](https://github.com/ethereum/ethereumj/issues/923).
  - **ethereumJS** [15:50](https://youtu.be/gxtftZB7_jA?t=950) - [Progress moving forward. Rolling out Byzantium changes soon in order to full sync. Passing nearly all of the Byzantium tests](https://github.com/ethereumjs/ethereumjs-vm/issues/209).
  - **yellowpaper** [16:32](https://youtu.be/gxtftZB7_jA?t=992) - [No updates.](https://github.com/ethereum/yellowpaper/issues/229).
  - **pyethapp** - Whoops, forgot to ask pyethapp team.
  - **Swarm** [17:39](https://youtu.be/gxtftZB7_jA?t=1059) - Implementing mounting volumes in Unix and adding Dropbox-like features. Web based file manager is built. Main missing feature is encryption of files on Swarm and that is being actively worked on. http://swarm-gateways.net has more info.

### d. Review time estimate for testing/release of Byzantium.

  - [23:36](https://youtu.be/gxtftZB7_jA?t=1416) Testnet has been running smoothly so far since the fork to Byzantium.
    - We discussed picking block number 4.35mil (Oct. 9th), 4.36mil (Oct. 13th), 4.37mil (Oct. 17th), or 4.4mil (Oct. 27th) for the mainnet fork.
    - Even though block number 4.36mil would be falling on a neat date, it would fall on a Friday so if things go wrong we'd have to work through the weekend. Also, Friday 13th is spooky and has bad luck associated. /s
    - Block number 4.4mil is very close to Devcon so that is not a good date.
    - We need some time to tests the new features and assure that clients stay in sync.
    - Unlike previous hard forks there is not an emergency or attack going on so we can be more conservative on the release date.
    - **The Ethereum mainnet fork for Byzantium will occur at block number 4.37mil (roughly Oct. 17th)** in order to give more time for testing.
    - The fork date/block number may be changed if major issues are found.

## 2. [EIP 706: Snappy compression for devp2p](https://github.com/ethereum/EIPs/pull/706) - "very simple change yet reduces sync bandwidth by 60-80%."

  - [38:44](https://youtu.be/gxtftZB7_jA?t=2324) - EIP discussion on Github has wrapped up.
    - Although there is a small amount of disagreement about implementing Snappy compression at the protocol, rather than a subprotocol level, all parties have agreed to move forward with the EIP because a majority are for it.
    - Reddit comments from /u/alsomahler were discussed and Peter addressed their concerns. [Click here for the Reddit comment](https://www.reddit.com/r/ethereum/comments/6ywatn/notes_from_todays_ethereum_core_developer_meeting/dmqqmcb/).

## 3. [46:52](https://youtu.be/gxtftZB7_jA?t=2812) [EIP: 152 - BLAKE2b `F` Compression Function Precompile ](https://github.com/ethereum/EIPs/issues/152) [Zooko]
  - Zooko wasn't able to make the call, but he wants to propose moving forward with the BLAKE2b EIP to include it as a pre-compile in Ethereum citing it's speed and compactness.
  - He wants to use it to create more efficient zk-SNARKs to make proving times lower. Can help improve things like zero knowledge token transfers and more efficient interactions between the Ethereum and ZCash chains.
  - Can be added in either Constantinople or Serenity.
  - In the call, no one voiced opposition to adding it, but questioned what different primitives would enable what integrations cross chain.
  - Clients still need to look and see how easy/hard it would be to implement BLAKE2b in their client.
  - Hudson will be working with Tjaden (original EIP author) and Jay from the ZCash team to update the EIP to the newest standard.

## 4. [51:20](https://youtu.be/gxtftZB7_jA?t=3080) [EIP 718: Concurrency and locks for storage](https://github.com/ethereum/pm/issues/23#issuecomment-331381293)
  - Anti-reentrency related EIP.
  - Will discuss more in next meeting after investigating it more.

## 5. [55:49](https://youtu.be/gxtftZB7_jA?t=3349) [EIP 215: Bitwise shifting](https://github.com/ethereum/pm/issues/23#issuecomment-331443964)
  - EIP was basically approved in a previous core dev meeting.
  - EIP is now final.
  - Greg will merge it in the EIPs repo.

## 6. [1:00:34](https://youtu.be/gxtftZB7_jA?t=3634) [Account abstraction discussion](https://github.com/ethereum/pm/issues/23#issuecomment-331453630) - "I think we should also slowly bring up account abstraction again. How do the toolset providers think about it? Did we find better solutions in the meantime?"

## 7. [1:01:00](https://youtu.be/gxtftZB7_jA?t=3660) ["Some way to reduce the gas costs for an SSTORE if that slot (or the whole contract) is destroyed at the end of the transaction ("ephemeral storage")."](https://github.com/ethereum/pm/issues/23#issuecomment-331454160)
  - Related to 718 and we can discuss it in future meetings.

## Off Topic:
- [1:02:15](https://youtu.be/gxtftZB7_jA?t=3735) ERC Process: How Does It Work?
  - Hudson, Casey, and Greg discussed what our view of the process is (as editors of the EIPs). We all agree we need to discuss this further and get a more well defined process, but so far ERCs are approved/finalized once the community members who benefit from the ERC and thought leaders come together, agree on an ERC spec, and implement the spec.
  - 2 good examples of this is [ERC-190 - ETHPM](https://github.com/ethereum/EIPs/pull/203) and [ERC-20](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md).
  - We are open to proposals on how to define the process for approving ERCs (you can reach out to Hudson Jameson (/u/Souptacular on Reddit or hudson@ethereum.org) with suggestions.

- [1:06:14](https://youtu.be/gxtftZB7_jA?t=3974) Discussion on the difficulty tests.
  - The testing team will be taking the discussion offline to decide how clients should collaborate on making difficulty tests more flexible.

## Attendance
Alex Beregszaszi (EWASM), Alex Van de Sande (Mist/Ethereum Wallet), Andrei Maiboroda (cpp-ethereum), Anton Nashatyrev (ethereumJ), Arkadiy Paronyan (Parity), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum/Solidity), Daniel Nagy (SWARM), David Knott (Research), Dimitry Khokhlov (cpp-ethereum), Greg Colvin (EVM), Hudson Jameson (Ethereum Foundation), Jared Wasinger (ethereumJS and Testing), Karl Floersch (Research) Lefteris Karapetsas (Raiden), Martin Holst Swende (Security), Matthew English (Testing), Mikhail Kalinin (ethereumJ), Paweł Bylica (cpp-ethereum), Péter Szilágyi (geth), Tim Siwula (Testing), Vitalik Buterin (Research & pyethereum), Yoichi Hirai (EVM)