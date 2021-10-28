# All Core Devs: Meeting 16
## Time: 5/19/2017 14:00PM UTC
## [Audio/Video of Meeting](https://youtu.be/brhanl8T2UY)

### Agenda:
1. [Not in A/V] [ERC-20 Token Standard Finalization](https://github.com/ethereum/EIPs/pull/610) [Fabian, Nick, or Hudson]
- [Point of contention: `throw` vs `return false;`](https://github.com/ethereum/EIPs/issues/20#issuecomment-300260935)
2. Metropolis updates/EIPs.
- **a. Details and implementations of EIPs.**
  - [[0:00](https://youtu.be/brhanl8T2UY)] "Agreeing on gas costs for MODEXP, ECADD, ECMUL, ECPAIRING. For MODEXP specifically, are we going to modify it to somehow incorporate bit length or not?" [Vitalik]
  - [[9:16](https://youtu.be/brhanl8T2UY?t=556)] [Concerns around the REVERT opcode introducing an economic change that may break things and revisiting cost/benefit analysis of the opcode.](https://github.com/ethereum/pm/issues/14#issuecomment-302028124) [Vitalik]
  - [[16:56](https://youtu.be/brhanl8T2UY?t=1016)] "Regarding EIP 96: should the gas price of `BLOCKHASH` already change from the beginning of the Metropolis, or from the block where the behavior of `BLOCKHASH` changes?" More info: https://github.com/ethereum/EIPs/pull/210/files#r117211219 [Yoichi]
  - [[24:34](https://youtu.be/brhanl8T2UY?t=1483)] "Regarding EIP96 (BLOCKHASH contract): should the blockhash-maintainance call at the beginning of each block increment the nonce of `SYSTEM_ACCOUNT`? https://github.com/ethereum/EIPs/pull/210/files#r117260179" [Yoichi]
  - [[26:14](https://youtu.be/brhanl8T2UY?t=1574)] "Regarding EIP98 (med state removal): this should start at (inclusive) METROPOLIS_FORK_BLKNUM instead of one block after that (as written in the EIP).  Pointed out by @gumb0 https://github.com/ethereum/EIPs/issues/98#issuecomment-292222044" [Yoichi]
  - [[26:50](https://youtu.be/brhanl8T2UY?t=1610)] "Regarding EIP 211 (RETURNDATACOPY): the behavior of reading out-of-bounds from the returndata buffer is [under discussion](https://github.com/ethereum/EIPs/pull/211#discussion_r117212647)." [Yoichi]
 - **b. Updates to testing.**
   - [[42:47](https://youtu.be/brhanl8T2UY?t=2567)] [Proposal: "Freeze" EIPs to allow for testing.](https://github.com/ethereum/pm/issues/14#issuecomment-302113189) [Yoichi]
 - **[[47:21](https://youtu.be/brhanl8T2UY?t=2841)] c. Any "subtleties" we need to work out.**
 - **[[50:52](https://youtu.be/brhanl8T2UY?t=3052)] d. Review time estimate for testing/release.**
3. [[1:09:03](https://youtu.be/brhanl8T2UY?t=4143)] [Time permitting] "If we have time (no high priority), I would like to get some feedback about adding functionality that allows dapps to be notified whenever a certain address was touched by a transaction (including internal calls). This information does not necessarily have to be part of the block, but could be an isolated index database." [Christian R.]

# Notes
## 1.  [ERC-20 Token Standard Finalization](https://github.com/ethereum/EIPs/pull/610) [Fabian, Nick, or Hudson]
Everyone in the call was uin agreement that [`throw` was a better solution than `return false;`](https://github.com/ethereum/EIPs/issues/20#issuecomment-300260935) on failed transactions, but it is better that this issue is decided in the EIPs itself as this is an ERC.

## 2. Metropolis updates/EIPs.

### a. Details and implementations of EIPs.**

#### i. "Agreeing on gas costs for MODEXP, ECADD, ECMUL, ECPAIRING. For MODEXP specifically, are we going to modify it to somehow incorporate bit length or not?" [Vitalik]

Need volunteers to write notes.

#### ii. [Concerns around the REVERT opcode introducing an economic change that may break things and revisiting cost/benefit analysis of the opcode.](https://github.com/ethereum/pm/issues/14#issuecomment-302028124) [Vitalik]

Need volunteers to write notes.

#### iii. "Regarding EIP 96: should the gas price of `BLOCKHASH` already change from the beginning of the Metropolis, or from the block where the behavior of `BLOCKHASH` changes?" More info: https://github.com/ethereum/EIPs/pull/210/files#r117211219 [Yoichi]

Need volunteers to write notes.

#### iv. "Regarding EIP96 (BLOCKHASH contract): should the blockhash-maintainance call at the beginning of each block increment the nonce of `SYSTEM_ACCOUNT`? https://github.com/ethereum/EIPs/pull/210/files#r117260179" [Yoichi]

Need volunteers to write notes.

#### v. "Regarding EIP98 (med state removal): this should start at (inclusive) METROPOLIS_FORK_BLKNUM instead of one block after that (as written in the EIP).  Pointed out by @gumb0 https://github.com/ethereum/EIPs/issues/98#issuecomment-292222044" [Yoichi]

Need volunteers to write notes.

#### vi. "Regarding EIP 211 (RETURNDATACOPY): the behavior of reading out-of-bounds from the returndata buffer is [under discussion](https://github.com/ethereum/EIPs/pull/211#discussion_r117212647)." [Yoichi]

Need volunteers to write notes.

### b. Updates to testing.

#### i. [Proposal: "Freeze" EIPs to allow for testing.](https://github.com/ethereum/pm/issues/14#issuecomment-302113189) [Yoichi]

Need volunteers to write notes.

### c. Any "subtleties" we need to work out.

Need volunteers to write notes.

### d. Review time estimate for testing/release.

Need volunteers to write notes.

## 3. [Time permitting] "If we have time (no high priority), I would like to get some feedback about adding functionality that allows dapps to be notified whenever a certain address was touched by a transaction (including internal calls). This information does not necessarily have to be part of the block, but could be an isolated index database." [Christian R.]

Need volunteers to write notes.

## Attendance

Alex Beregszaszi (EWASM), Alex Van de Sande (Mist/Ethereum Wallet), Andrei Maiboroda (cpp-ethereum), Arkadiy Paronyan (Parity), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum/Solidity), Dimitry Khokhlov (cpp-ethereum), Greg Colvin (EVM), Hudson Jameson (Ethereum Foundation), Lefteris Karapetsas (Raiden), Martin Holst Swende (geth/security), Nick Johnson (geth/SWARM), Paweł Bylica (cpp-ethereum), Vitalik Buterin (Research & pyethereum), Yoichi Hirai (EVM)
