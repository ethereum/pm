# Model based testing for specs and implementations

**Summary:** Code coverage based testing doesn't necessarily provide good enough coverage of Ethereum protocol components and implementations. We can employ model-based testing to improve test quality according to other coverage criteria. Code-based and model-based testing can be combined (e.g. to test Execution specs).

**Facilitator:** Mikhail Kalinin

**Note Taker:** TBD

**Pre-Reads:**
* Fork choice compliance testing [suite](https://ethresear.ch/t/fork-choice-compliance-test-suites-test-generator/19954) and [methodology](https://hackmd.io/@ericsson49/fork-choice-implementation-vs-spec-testing)
* Validator state testing [proposal](https://hackmd.io/@n0ble/validator_state_testing)

## Agenda

The goal of this session is to present a model based testing approach and the way it can be applied to test spec correctness and implementation compliance for CL and EL, and to facilitate the usage of this approach in Ethereum protocol testing.

The approach has been already applied to [Fork Choice compliance testing](https://ethresear.ch/t/fork-choice-compliance-test-suites-test-generator/19954) and to [Validator state testing](https://hackmd.io/@n0ble/validator_state_testing). It can be applied to other parts of the protocol, like EL state transition (e.g. EVM, including EOF).

To bootstrap the session, we will give an idea of how the approach works and will review two cases, where it has been applied to the Ehtereum protocol (the Fork Choice compliance and the Validator state testing).

Then we plan to collect feedback, faciliate a discussion about applying the approach to Ethereum protocol testing in general and address potential concerns of spec maintainers and client implementors. A particularly interesting application is EVM testing, where the model- and the code-based approaches can be combined (e.g. generate EVM programs using the model-based approach, followed by coverage-based testing of the generated programs).

## Session Summary
* The sesion was opened with a short [presentation](https://hackmd.io/@n0ble/BySKhBCZ1e#/1)
* Then we went through a Validator state testing proposal, including:
    * The general overview of the proposal
    * Validator state model definition in Minizinc language
    * Played a bit with model constraints to generate different set of validator state profiles
    * Test instantiation using generated validator state profiles
* Action items:
    * Finish work on validator state testing
    * Find a place in consensu-specs repo where to put the model in
    * Generate test vectors to test implementations and collect the feedback