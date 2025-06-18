# EEST & EELS (STEEL 🦾)

**Summary:** 

Our aim is to facilitate the discussion around EL client consensus testing using EEST (execution-spec-tests) during fork development, alongside a future EIP spec implementation and testing process utilizing EELS (execution-specs).

By the end of this workshop, all EL client teams will have a unified understanding of the past, present & future testing landscape, and have an idea of the future EIP spec implementation process within EELS.

**Facilitator:** Spencer (**EEST**) & Peter (**EELS**)

**Note Taker:** Dan

**Pre-Reads (optional):** 
- EEST - https://github.com/ethereum/execution-spec-tests
- EELS - https://github.com/ethereum/execution-specs

**Slides:** https://notes.ethereum.org/@spencer-tb/devcon-sea-eest-eels-presentation

## Agenda

### Split Presentation from EEST & EELS: 10-20 mins

#### EEST: 10-15 mins

- Overview of the testing team and the purpose of EEST, combining with EELS to form STEEL.
- Brief framework deepdive and improvements within EEST, outlining new CLI.
- Outline of the past vs. current vs. future testing landscape:
    - Remove confusion around fill-ing, it doesn't mean you are the passing tests.
    - What tests releases and simulators should I be running as an EL client?
    - Plans for `ethereum/tests`, aiming for a full port over to EEST by EOF. 
    - Hiveview/hive changes with regards to EEST:
        - migration from `hive eth/pyspec` -> `hive eth/eest/consume-engine`
        - migration from `hive eth/consensus` -> `hive eth/eest/consume-rlp`
- Define hard test passing requirements for entering devnets, passing both `consume direct/engine` tests?
    - If `consume engine` is a hard requirement, should EL clients write a binary to run blockchain engine fixtures locally? Fast feedback on engine api tests?

#### EELS: 5-10 mins

- Why EEST are switching to EELS as the main t8n tool for test filling:
    - Should clients maintain or deprecate there existing t8n tool implementation?
- Future EIP spec implementation process in EELS:
    - EIPs only CFI'd if they have a spec implementation in EELS and basic tests in EEST?



### Disscusion & Open Questions: 45-60 mins

## Testing (EEST) Feedback Form

If you use EEST or interact with the testing team, we would appreciate your honest feedback, even if it’s just a few words. Please keep it critical and harsh.

**Feedback link:** https://vaultform.com/surveys/a3864ac5-1e0e-4b71-a019-d508b80a2316/

Here are some questions to get your 🧠 flowing:

- How can we make it easier for you to work with our tests?
- Do you like the current EEST release process? How could we improve it?
- What has been your biggest testing challenge this past year?
- What has been the main source of confusion with EEST?
- Do you rely on `hiveview`? How often do you use it?

## Notes & Action Items 

N/A

