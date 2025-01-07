# EOF implementers call 59

Note: this file is copied from [here](https://github.com/ethereum/pm/issues/1162#issuecomment-2388989786) 

## Meeting info

Date: 2024.10.02

Agenda: https://github.com/ethereum/pm/issues/1162 

YouTube video: https://youtu.be/TjZv8DMZka4

## Notes

Current release tests (EOF on top of prague) are broken
- Besu had a 7702 bug, all non-7702 tests are fine.
- Next release will be released after devnet 4 is released
- PR reviews are mostly caught up
- Testing focus is on devnet 4 for the next week

Compiler
- Vyper create from blueprint needs a re-work for EOF.
- Create form EXT Contract would have helped.
- Cannot blueprint off of any contract in EOF like you could in legacy
- A factory deployer would be good, delegate call into a contract that EOF creates. As opposed to an initcode only contract


Osaka Migration
- Clients need to target Osaka for EOF activation
- Tests need to target Osaka, including moving tests in source tree
- We have 6 more months to reifine the spec
- We can look into HASCODE
- We can reconsider EXT*CALL return code numbers
- cleanup: EOFCREATE stack order
- cleanup: Remove hashing of container in EOFCREATE
-cleanup: Rename RETURNCONTRACT to RETURNCODE

### Open questions

Implications of gas introspection: regarding a gas to eth EIP.
