# All Core Devs: Meeting 10
## Time: 2/10/2017 14:00PM UTC (Date shifted due to EdCon)
## [Audio of Meeting](https://youtu.be/huYl7eOlKJE)

### Agenda:
1. New EIP GitHub process and cleanup. [Facilitator: Hudson]
2. Come to final agreement on [EIP 196: zk-SNARK precompiles](https://github.com/ethereum/EIPs/issues/196) [Facilitator: Christian]
3. Update on EIP for precompiles for elliptic curve point addition, elliptic curve scalar multiplication and pairing [Facilitator: Christian]
4. Metropolis and associated EIPs. [Facilitator: Vitalik/Christian]
* [EIP 5/8: Gas costs for return values](https://github.com/ethereum/EIPs/issues/8) [Facilitator: Christian]
* [EIP 86: Proposed initial abstraction changes for Metropolis](https://github.com/ethereum/EIPs/issues/86)  [Facilitator: Vitalik]
* [EIP 96: putting block hashes and state roots into the state](https://github.com/ethereum/EIPs/issues/98)  [Facilitator: Vitalik]
* [EIP 100: uncle mining incentive fix](https://github.com/ethereum/EIPs/issues/100)  [Facilitator: Vitalik]  
* EIPs [196](https://github.com/ethereum/EIPs/issues/196) & [197](https://github.com/ethereum/EIPs/issues/197): pairings [Facilitator: Christian/Vitalik]
* [EIP 198: bigint arithmetic](https://github.com/ethereum/EIPs/pull/198)  [Facilitator: Vitalik]
* ethereum/EIPs#206: Revert OPCODE and  ethereum/EIPs#207: Encoding of revert OPCODE [Facilitator: Vitalik]
5. STATIC_CALL: ethereum/EIPs#116 follow-up. [Facilitator: Christian]

# Notes

IN PROGRESS

1: pairing precompile: Gas still to be determined after we have some implementations, probably linear in the number of pairings

2: EC operations: Also, gas still to be determined, multiplication similiar to EXP

3: 5/8: compromise proposal (needed to make proposal B backwards compatible): new rules only if the return size is 2^256-1
Nick: seems complicated, what about adding “returndatasize” and “returndatacopy” similar to “calldatasize” and “calldatacopy” that can access return data even if return area size was specified as zero

4: 86 (account abstraction):

## Attendance

TODO
