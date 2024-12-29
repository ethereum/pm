# EOF Implementers call 56
Note: This file is copied from [here](https://github.com/ethereum/pm/issues/1128#issuecomment-2302428979)
## Meeting info

**Date**: 2024.08.21

**Agenda**: https://github.com/ethereum/pm/issues/1128

**YouTube Video**: https://www.youtube.com/watch?v=03Dkfpvw4Pc

## Notes

### Client and fuzzing updates

evmone found a bug that fuzzers couldn't find

besu had subcontainer container bugs found via evmon's tests a few weeks ago

Nethermind is re-writing their subcontainer validation to not be recursive

Reth and Geth were not present.

### Spec updates

community strongly wants a EXTCODESIZE/ISCONTRACT solution, Libs may not be happy with legacy "escape hatch" contracts rather than using EIP-165 introspections
- If AA is the reason not to proceed, a clear plan needs to be stated as to how the AA transition is expected to play out.

Delegate call into legacy call rule
- This may break proxies. (EOF proxies, proxying to a legacy contract)
- A detection of EOF vs legacy contract would be useful. EXTCODEHASH would identify EOF
- No opinion about 7702 proxy detection detection, can go with legacy treatment.


### Testing Readiness

With devnet-4 we need to activate on prague alone
- EEST will migrate to just "Prague" for tests,
- EEST will sunset "CancunEIP7692" and "Prague7692" forks
- Will change once 7702 tests are fully merged into tests
- Suddenly 7702 tests will work with EOF

New fixtures release 1.0.8 - Contains Both pragueEIP-7692 and Cancun7692

EOF Container Fuzzing
- EVMONE and Besu

EOF Execution fuzzing
- possibly goevmlab, guido vranken's fuzzer.


### Testing matrix

Devs, please update

Any automation interest?
- Maybe hive/consume?
- Still needs final consume setup in CI
- Consume does not run EOF Validation tests (because engine API is the test interface)
