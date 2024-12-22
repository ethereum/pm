---
title: Untitled

---

# EOF implementers call 57

Note: this file is copied from [here](https://github.com/ethereum/pm/issues/1138#issuecomment-2329428927) 

## Meeting info

Date: 2024.09.04

Agenda: https://github.com/ethereum/pm/issues/1138 

YouTube video: https://youtu.be/7wFucExQb7U

## Notes

clients and compilers - no non-test updates

switch to prague

mario discussed 7702/EOF testing features in EEST https://github.com/ethereum/execution-spec-tests/blob/eip-7702-devnet-3/tests/prague/eip7702_set_code_tx/test_set_code_txs.py

Fuzzing - no new updates

Discussed converting EOF format tests into format tests.

- Init containers need extra work, either double wrapping or need to declare deployed container format. Issues include appending data
- For automated testing we will move to assuming the container is deployed, and in cases where that isn't going to work we need to notate the tests with expected outputs

New release of legacy tests - invalid tests have been removed, or fixed, or moved to EEST. No new coverage -- all new coverage comes in EEST.

### ISCONTRACT

Legacy solidity will not easily be able to determine if it's EOF or Legacy, so the code may fail compiling to EOF. Old contracts will need new versions or alternates for EOF.

Most libraries depending on assembly would need to change for EOF anyway (any use of JUMP, CALL*, EXCODE* for example)

May be best solved in solidity? conditional compilation or new is_contract primitive? existing solidity PR Detect EVM version? existing solidity pr

Example: OpenZeppelin, Solady, Tycho do deep code interactions and have taken up to a year to implement.

Need to do outreach to the AA team, as they expressed concern on ACD that this may be problematic. (Piotr to reach out)


What is Erigon's status?
- Unknown status.


More on nethermind's status

- 7702 is in a different branch from EOF. 7702 will land in Nethermind master first.
- Will target prague in EOF branch
- Running published EEST fixtures.

New fixtures will be published this week. Need to fix an EEST bug relating to EXT*CALL opcodes.