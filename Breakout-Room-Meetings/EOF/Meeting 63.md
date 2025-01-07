# EOF implementers call 63

Note: this file is copied from [here](https://github.com/ethereum/pm/issues/1205#issuecomment-2533055543) 

## Meeting info

Date: 2024.12.17

Agenda: https://github.com/ethereum/pm/issues/1205 

YouTube video: https://youtu.be/2Z5YPfOnb74

## Notes


### Tracing:

Updated EIP-7756

- PC=0 is always the first byte of the container
- Number and HexNumber are interchangable
- OpCode now defaults to hex
- gas members now default to number


reth and evmone will need to adjust to PC=0, geth, besu, and nethermind have already adjusted

#### Fuzzing:

branch with WIP fuzzing tool shemnon/eof-fuzz
 - Needs a patch to goevmlab to work - Non-osaka EOF changes holiman/goevmlab#179

Corpus is the single test set of reference tests

4 mutators currently (more to come)
- Add PUSH0/POP
- Replace PUSH value with in-test address
- Replace PUSH value with "magic" number (mostly 2^x and friends)
- Replace PUSH with random bytes (biased to shorter strings)



Found 3 bugs so far
- Besu 32/64 bug in EOFCREATE
- Geth DATACOPY overflow
- Nethermind EXT*CALL gas costing issues

plan is to write more fuzzers to bring it on par with FuzzyVM, but for EOF.
