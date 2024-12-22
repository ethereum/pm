# EOF implementers call 55

Note: this file is copied from [here](https://github.com/ethereum/pm/issues/1115#issuecomment-2273805574) 

## Meeting info

Date: 2024.7.24

Agenda: https://github.com/ethereum/pm/issues/1115 

YouTube video: https://youtu.be/OaNJOoaeNNY

## Notes

### Client updates

Discussed EOF container validation

some discussion about testing

### Compiler

need to finalize solidity PR (depends on an evmone release w/ EOF)

### Spec

Contract Detection
- Contracts can either disable safetransferfrom, or call out to another contract with legacy features to get the "isContract" question answered.
- "do nothing" is the most undoable, as we can add ISCONTRACT later. But we cannot do the return code changes.
- do nothing / fix later has momentum

Tracing changes
- There was discussion of process
- PC is zero to section
- Maybe shorter names for section
- Danno will write up a new EIP as a red herring, rather than modify 3155
- goEVM lab wants nomemory and nostack options (maybe just top of stack). Make this the default?

### Testing

Instead of Kurtosis we can use EEST consume
- Kurtosis's main gain is it's a full client setup
- EOF calls to the system contract would be valuable in Kurtosis. Withdrawals/deposts/other pectra calls
- Not valuable at the moment

Run every test via consume

EEST could produce Assertoors

Testing blindspots
- Need to update the checklist
- Quantify the testing progress for next ACDE
- Make sure all EIPs tests are in the testing checklist

Devnet
- We want fuzzing ready
- Do we need to be 100% for devnet?
  - Client should pass fuzzing
  - Clients should pass reference tests at 100% (EESTs and Ethereum/tests and evmone)
  - 7702 will be dominating devnet testing
- Reth and Besu can join a devnet today (configuration wise)
  - Need updates from Geth, Nethermind, EthJS, Erigon
