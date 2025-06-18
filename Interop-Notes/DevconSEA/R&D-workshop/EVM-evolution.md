# EVM Evolution Session

**summary**: Discuss current, planned, and potential evolutions to the Ethereum Virtual Machiene
**target audience**: execution devs, EVM toolchain practicioners, and all interested parties
**facilitator**: Danno Ferrin
**note taker**: Alex Beregszaszi

![Choo Choo the EVM train is coming!](https://hackmd.io/_uploads/BkGrs7Vxyx.jpg)

## Reference Material

### The Road Ahead
* EOF 
    * [Mega-EOF spec](https://github.com/ipsilon/eof/blob/main/spec/eof.md) - Non-normative
    * [EIP-7692](https://eips.ethereum.org/EIPS/eip-7692) - Normative
<!--
        * [EIP-663 DUPN/SWAPN](https://eips.ethereum.org/EIPS/eip-663) 
        * [EIP-3540 EOF Format](https://eips.ethereum.org/EIPS/eip-3540)
        * [EIP-3670 Code Validation](https://eips.ethereum.org/EIPS/eip-3670)
        * [EIP-4200 Relative Jumps](https://eips.ethereum.org/EIPS/eip-4200)
        * [EIP-4750 CALLF/RETF](https://eips.ethereum.org/EIPS/eip-4750)
        * [EIP-5450 Stack Validation](https://eips.ethereum.org/EIPS/eip-5450)
        * [EIP-6206 JUMPF](https://eips.ethereum.org/EIPS/eip-6206)
        * [EIP-7069 EXT*CALL](https://eips.ethereum.org/EIPS/eip-7069) 
        * [EIP-7480 DATA section access](https://eips.ethereum.org/EIPS/eip-7480)
        * [EIP-7620 EOFCREATE/RETURNCONTRACT](https://eips.ethereum.org/EIPS/eip-7620) 
        * [EIP-7698 Create Transaction for EOF](https://eips.ethereum.org/EIPS/eip-7698)
-->
### On the Horizon 
 * EVMMAX
     * [EIP-6690 EVM Modular Aritumetic Extensions](https://eips.ethereum.org/EIPS/eip-6690)
 * Legacy -> EOF Integrations
     * \<no pre-read available\>
 * Code Size Increase / Uncapping
### Over the Horizon
* Gas Schedule Flexibility
   * \<no pre-read for L2 schedule adjustment facility\>
   * Multi-dimensional gas
       * [Oil proposal \[2020\]](https://ethereum-magicians.org/t/oil-adding-a-second-fuel-source-to-the-evm-pre-eip/4270) 
* Progressive Precompiles
* Native AA EOF integration [EIP-7701](https://eips.ethereum.org/EIPS/eip-7701)
 * Concurrency
     * [EIP-7519 Atomic Storage Operations SCREDIT and SDEBIT](https://eips.ethereum.org/EIPS/eip-7519)
     * [Queue end-of-block transaciton](https://ethresear.ch/t/queue-end-of-block-transaction-opcode/19621)

## agenda

rough points

* (30 min) The Road Ahead - EOF v1.0
    * Current state
    * Potential changes for Osaka
        * Adding HASCODE / not banning EXTCODE\*
        * Rework EXT\*CALL return codes
        * EOFCREATE Hashing changes
        * Change max stack height in types to "extra stack"
        * Re-order EOFCREATE and EXT\*CALL so they align better
        * Rename RETURNCONTRACT to RETURNCODE
    * Testing overview
        * EEST Tests
        * Code Validation Fuzzing
* (45 min) On The Horizon 
    * (15 min) EVMMAX and specialized math
        * Current spec
        * potential vectorization improvements
    * (15 min) Legacy -> EOF migration strategies
    (How) do we migrate to an EOF only/EOF first?
        1. EOF Parity w/ legacy
        2. Ban legacy deployments
        3. Audit deployed legacy code
            a. "validated" - no ill behavior like dynamic jumps
            b. "remnant" - code that will require special handling
        4. Combine or not
        Many decisions cannot be made until we see what "bad behaviors" remain.  Options include
            * translate legacy to eof
            * create a "v0" eof for "validaed" code, special case "remnant" code for zk proving.
            * Keeping legacy mode forever
    * (15 min) other short term impvements
        * Increase contract size limit / uncapping size limit
    
* (15 min) Over the Horizon
    * Tempurature checks for future L1 and L2 evolutions
        * Gas Schedule
            * L2 flexibility
                * Standard gas schedule JSON file?
            * Multi-variable scheduling
                * compute, storage, etc.
        * Concurrency
            * Atomic Operations
            * Spawning Transactions
        * EOF Metadata
            * Native "storage access list" 
            * Native AA integration
            * Native 4-byte dispatch

## Goals

* The Road Ahead
    * Get everyone up to speed on the status of EOF
    * Allow for input into final round of changes
* On the Horizon
    * Get feedback on proposed designs
* Over the Horizon
    * Tempurature check on new ideas


## Notes

### EOF testing

- There's wrapping of legacy EVM code into EOF in the testing suite for a large number of tests where it can be automatically wrapped.
- Compilers to be used for fuzzing
        - Solar is only a frontend so far, has no codegen
        - For EOF codegen only mainline Solidity exists

### EOF specs

- EIPs are the normative spec now, https://github.com/ipsilon/eof may be lagging behind

### EOF code and data discovery

- An "EOF proxy contract" (i.e. a legacy contract proxying calls/instructions) can be used to circumvent some restrictions
- Code discovery
    - Due to the proxy contracts, code discovery is possible, rendering the removal EXT* a bit moot
    - Allow EXTCODE* or introduce HASCODE
    - HASCODE could be changed to return account type (empty, legacy, EOFv1, account abstraction, etc.)
    - *oting:
        - **Most in favour HASCODE (with returning account type)**
        - None in favour of EXTCODE*
        - Some in favour of "do nothing" (i.e. proxy or code at a known address)
- Data contracts
    - EXTCODE* can be used to acquire it
    - The target contract can have a function returning it
    - Could introduce EXTDATA* instructions

### EOF + AA

7701: Have code section 1 for validation. Main problem: validation MUST be run on TX level and not call level.

How does it work via delegatecall proxy?

- Yoav's suggestion: prior to rollout have an enshrined proxy (similar to how 7702 works)
- Need a standard create2 proxy
- Need a standard eof proxy

(Need to improve this section. It is fuzzy. See the AA breakout for further discussion: https://notes.ethereum.org/@yoav/devcon-sea-l1-aa-session)

### EVMMAX

- SIMD for EVMMAX
    - Code density can be improved.
    - Could execute in parallel.
    - Question: what level of data dependency is in common precompiles? How much can it be parallelized?
    - Proposal: 16 lanes (16 values at the same time)
    - Do SIMD in general in the EVM.
    - Arguments: Hardware SIMD (incl. GPU) unlikely to do montgomery.
- SIMD for EVM
    - Hardware support.
    - Less important use cases.
- EVM model unlikely to change to be more complex on the instruction level, i.e. still one instruction at a time, no threads/parallelization/registers in general.
- Modexp precompile is like swiss cheese.
    - EVMMAX should replace it, but it is more complex as it has unbounded modulus.
- Clobbering (inputs/outputs may overlap): we use an intermediate buffer for the calculation.
- **Another EVMMAX session tomorrow.**

### Legacy -> EOF migration

- Why do this?
    1. EOF makes zk easier
    2. Remove complexity in clients
- EOF parity with legacy
    - Needs TXEOFCREATE
    - Smart wallet transactions must be solved
- Ban legacy deployments
    - Both transaction level creation and CREATE* instructions.
    - Only for contracts deployed after a given demarcation point.
        - Once the point is known, people will deploy breaking contracts for fun.
    - This breaks counterfactual contracts. Maybe an impossible problem?
- Translation
    - Was prototyped in the test suite already
- **Question: Should we do this?**
    - *No clear response.*
- What level of one-time complexity are we willing to endure for client complexity reduction?
    - *No clear answer.*
- Question: Why do we need need to ensure contract semantics dont change?
    - Social contracts. Even selfdestruct is not fully removed. The only thing broken is gas contracts.

### Contract size

- Marius: can't have uncapped limit.
- If uncapped/increasing caps: need TX-level gas limit, not only block-level limits.

### Gas schedule

- There's interest to change, but no plans.
- Changing storage/state costs is way different to changing arithmetic costs.
