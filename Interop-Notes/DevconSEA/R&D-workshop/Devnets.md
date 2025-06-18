# Devnets and tooling 

With ambitious fork plans, devnets and tooling are starting to come in the critical path. This session will discuss what tooling we still need to build, changes we need to make to our devnet approach and potential custom devnets we should be building (e.g one for non-finality) 

**Facilitator:** Parithosh Jayanthi
**Note Taker:** Sam Calder-Mason

**Notes**: https://notes.ethereum.org/@ethpandaops/devnets-and-tooling-devcon-notes

**Pre-Reads:** 
- https://ethpandaops.io/posts/kurtosis-deep-dive/

**Slides:** 

## Agenda 
1. Pectra devnet feedback:
    i. What tooling would have helped speed up the process?
    ii. Did the strategy of spec sheets with EEST and Spec tests releases help?
    iii. What tests do you think we MUST do before mainnet?
2. Retrospective and feedback on current devnet approach:
    i. Can teams handle the current number of devnets?
    ii. Could we handle increased load by having an EOF devnet too?
    iii. Feedback on the approach to split pectra/peerdas early on for devnets, was this as useful as perceived?
3. What custom devnets should we have?
    i. Non-finality devnet
    ii. Long range sync testing devnet?
    
4. Peerdas devnet feedback:
    i. What kind of devnets would you like to see going forward? 
    ii. What kind of tests on those devnets do you want to see? 

5. EOF/Fulu devnet planning:
    i. What kind of devnets would you like to see going forward?

6. Q&A or discussion space

## Notes & Action Items 

## Infrastructure & Tools

### Log Aggregation
- **Action Items**:
  - EthPandaOps to publicize their Loki instance and empower everyone with log aggregation ability for devnets
  - Lighthouse team to contribute example queries

### Snapshotter
- Interest expressed in mainnet snapshots

### Assertoor
- **Action Items**:
  - Add special withdrawal credentials point to system contract
  - Improve documentation
  - Enable client teams to write their own tests
  - Implement system to convert downstream discovered issues into Kurtosis/Assertoor tests after fixes

### Kurtosis-chaos
- **Action Items**:
  - Create documentation for Kubernetes in Docker setup
  - Implement NTP server failure test

## Testing Framework

### Spec Tests
- **Issue**: Early Pectra devnets faced issues due to skipping pre-devnet test requirements
- **Discussion**:
  - Marius: Against strict gating of devnets behind passing tests
  - Pari: Proposed short-lived hive instance per devnet
- **Action Item**: Define clear testing requirements pre-devnet participation. Status quo may be sufficient

### EEST
- **Issue**: Client incompatibility support currently limited. Potentially out of scope.
- **Action Item**: Unsure on paths forward, investigate expanding client incompatibility support

### Transaction Pool Testing
 - Basic propagation tests exist in Assertoor and are being run
 - Different EL rules across implementations
     - Not defined since its hard to break in adversarial case
- **Action Items**:
  - Implement comprehensive transaction propagation testing
  - Create tests for n-node setup with propagation and inclusion verification
  - Consider EEST integration

## Documentation

### Devnet Specifications
- PandaOps team has been creating and maintaining a devnet summary document for each devnet iteration, containing links to spec versions and changes between devnets.
- **Improvements Needed**:
  - Better publicity for existing documents
  - Simplify URL structure for assertoor tests/playbooks for discoverability
- **Action Items**: 
    - PandaOps to improve document visibility
    - Create separate documentation for compatible EL/CL versions
## Mainnet Pectra Requirements

- **Action Items**:
  - Implement transaction pool tests (7702 implications)
  - Create tests for same-block deposits/withdrawals/consolidations
  - Expand pectra-FAQ document
  - Test 7702 authentication with large-scale delegations
  - Resolve MEV workflows before devnet-5
  - Test delegation scenarios

### Pectra-Devnet-5
- Discussions around implementing restriction of 1 blob per transaction before increasing blob count

### RBuilder
- **Action Item**: Develop timing games simulation module for devnets

## Custom Devnets

### Non-Finality Testing
- **Requirements**:
  - 1-month unfinalization period
  - Continuous operation
  - Test new aggregation system for attestation packing
- **Action Item**: Implement non-finality devnet learning from Goerli experience

### Long Range Sync Testing
- **Action Item**: Establish dedicated long-range sync testing devnet

### Peerdas Development
- **Issues**:
  - Limited developer presence in discussion, DAS session happening at same time
  - Column storage validation needed. Clients might advertise they are storing certain columns, but no way to easily check.
- **Action Items**:
  - Complete PandaOps validation tool
  - Integrate with Kurtosis

## General Devnet discussion
- Current devnet quantity is appropriate
- Separate devnets were preferred and worked well over a consolidated mega-devnet for Pectra/Peerdas/EOF