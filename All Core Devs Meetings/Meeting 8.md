# All Core Devs: Meeting 8
## Time: 10/28/2016 1:00PM UTC

### Agenda:
  1. Upcoming HF to clear out state + potentially other changes.
  - Clearing out state
    - [EIP 158](https://github.com/ethereum/EIPs/issues/158) by (@vbuterin)
    - [EIP 161](https://github.com/ethereum/EIPs/issues/161) by (@gavofyork)
  - EXP Cost Increase
    - [EIP 160](https://github.com/ethereum/EIPs/issues/160) by (@vbuterin)
  - Replay attack protection
    - Do we want it in the upcoming HF, Metropolis, or not at all?
    - [EIP 134](https://github.com/ethereum/EIPs/issues/134) by @aakilfernandes
    - [EIP 155](https://github.com/ethereum/EIPs/issues/155) by @vbuterin
    - [EIP 166](https://github.com/ethereum/EIPs/issues/166) by @vbuterin
  - Block number of HF.
  
  2. EIP/ERC GitHub Organization
  - Improvement Discussion
    - [EIP 148](https://github.com/ethereum/EIPs/issues/148) by @axic

# Notes
## 1. Upcoming HF to clear out state + potentially other changes.
### Clearing out state
EIP 158 and 161 are now equivalent, after changes were made to 158. 161 will be implemented. Test cases are located here (feel free to add more)(https://etherpad.net/p/EIP158). Currently we have the state bloat because there are many empty accounts. The hard fork will change the database encoding of empty accounts so that they are not present at all anymore, but the encoding only affects accounts that are "touched" by transactions. After the hard fork the Ethereum Foundation will fund the transaction(s) neccessary to clear the empty accounts.
### EXP Cost Increase
It was discussed whether a 5x increase in cost was enough. Benchmarks indicated that EXP is 4-8 times underpriced. It was decided that a 5x increase is sufficient for now and it may be increased in the Metropolis hard fork after more analysis. There are ongoing efforts to work on better benchmarking tools which will help determine future OPCODE pricing changes.
### Replay attack protection
Three proposals discussed:
   1. EIP 134 (include a blockhash in an RLP field of each tx)
   2. EIP 155 (inlude a `CHAIN_ID` as a factor in the `v` value of the EDCSA signature scheme and in the tx hash)
   3. EIP 166 (include a `CHAIN_ID` in the high-order bits of the tx nonce)
   
In deciding which replay protection scheme to adopt, the trade-offs between these three proposals were discussed. EIP 134 was rejected because it adds 32 bytes of data to each transaction. Both EIP 150 and EIP 166 were agreed to be equally simple in their implementation complexity, but EIP 166 (which was already provisionally [implemented in geth](https://github.com/ethereum/go-ethereum/pull/3179/commits/53510dd70af80dc9d14cd219ddcdd559f8bf7f10)) requires an additional byte of data for each transaction, whereas EIP155 does not add any data to transactions. On the other hand, EIP155 modifies ECDSA signature inputs, and one concern with modifying signature inputs is that when Hardware Security Modules (HSMs) are used for signing transactions, HSM firmware may need to be updated for those transactions to be replay protected. Since EIP 166 does not modify signature inputs, it can be argued that EIP 166 is a "cleaner" separation of concerns. And while the increased data usage of EIP 166 could be remedied with a compression scheme, in the interest of practicality, minimal data usage, and avoiding further postponement of replay protection, core developers' indicated there was a preference for adopting EIP 155 in the upcoming hard fork.

### Block number of HF.
Block number for hard fork will be decided on Monday.

## 2. EIP/ERC GitHub Organization
###Improvement Discussion
Hudson will clean up the EIPs and continue dialog about what to change in the repo.

## Non-agenda
Future meetings will start being held twice monthly in order to process EIPs more quickly. We will likely have a set time/date (such as every other Monday) to prevent the added complexity of using Doodle's to ask a bunch of people what time works best for them.

## Attendance
Alex Beregszaszi (Solidity), Alex Van de Sande (Mist/Ethereum Wallet), Anton Nashatyrev (ethereumJ), Casey Detrio (Volunteer), Christian Reitwiessner (cpp-ethereum), Dan Finlay (MetaMask), Dimitry Khokhlov (cpp-ethereum), Felix Lange (geth), Greg Colvin (EVM), Hudson Jameson (Ethereum Foundation), Jan Xie (ethereum-ruby & pyethereum), Jeffrey Wilcke (geth), Martin Becze (Research), Péter Szilágyi (geth), Vitalik Buterin (Research & pyethereum)
