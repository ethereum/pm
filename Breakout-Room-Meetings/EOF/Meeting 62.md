# EOF implementers call 62

Note: this file is copied from [here](https://github.com/ethereum/pm/issues/1192#issuecomment-2504249197) 

## Meeting info

Date: 2024.11.27

Agenda: https://github.com/ethereum/pm/issues/1192 

YouTube video: https://youtu.be/yzYUWpa-1QM

## Notes

### Testing Update

How to handle State tests with invalid EOF?
- state tests - reject test if any EOF is invalid
- Block tests - only an issue in genesis? Abort if EOF in genesis is invalid.
- Imported blocks - presume valid as create TXes are how they are added, so invalid EOF should result in an failed transactions.
- Extends to 7702 - 0xEF01 validation?


EOFWrap Tests
- ports over legacy tests into EOF if it ports, stopgap for full testing
- feat(tests): port ethereum/tests test cases (tracking issue) execution-spec-tests#972 will ultimately port all old tests

### Client and Compiler Updates

No client Updates, mostly focused on petctra

Solidity working on EOF as an experimental feature
- eof: Support functions (CALLF, RETF, JUMPF) solidity#15550
- eof: Implement stack height calculation solidity#15555
- EOF: Implement ext*calls solidity#15559

### Spec Updates

Compiler Metadata Section
- Kaan from Sourcify Team
- Current practice is to just append
- would want a separate metadata section in EOF.
  - Unreachable by code (a good thing)
  - contains the CBOR data solidity produces
- Current status of appended to data and behind constructor fields makes it hard to find
- Experimental Solidity EOF handling is to put CBOR metadata at the beginning of the data section.
- Would insulate code/data indexes from variable CBOR sizes, such as if experimental flags are logged.
- Next step is an EIP


### Brief discussion on header section numbers

EOFCREATE hash - ipsilon/eof#162 (comment)

danno wants a "0xef01" hash added

Solidity has concerns about the genericness, would prefer container index

Bad salt management could prohibit multiple deployments

Should hash include auxdata, not just code data?

possible issues with cross-chain deployment. The more mandatory data makes same address contracts difficult.

note: some people don't like metadata has in CREATE2, would compiler metadata be excluded from address derivation?

Are there security implications? Would the "code hash" guarantees be forgotten about? Could compilers compensate?

Please add comments to the thread.
