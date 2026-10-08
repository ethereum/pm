# Glamsterdam Validator & Operator Readiness Checklist

Tracking ecosystem readiness for validator operations and infrastructure changes introduced by [EIP-7732 (ePBS)](https://eips.ethereum.org/EIPS/eip-7732) as part of the Glamsterdam network upgrade.

This checklist is intended for validator operators, staking providers, validator client teams, infrastructure providers, and institutional participants.

## How to Participate

Projects are encouraged to submit a Pull Request (PR) to update their readiness status.

1. Add or update one row for your project in the relevant table.
2. Update your testing/readiness status.
3. Link to a release, test report, GitHub issue, PR, or documentation where available.
4. Include any known blockers or operational concerns.
5. Use **Additional Comments** for other observations, dependencies, or feedback.
6. Submit a PR to the [ethereum/pm](https://github.com/ethereum/pm) repository.
Projects can update their entries as testing progresses.

There is no separate questionnaire to complete. Projects can update their entries as testing progresses.

### Status Legend

- ⭕ Not Started
- 🛠️ In Progress
- 🧪 Testing
- ✅ Ready
- ⚠️ Blocked
- ➖ Not Applicable

> **Note**: Participation in this checklist is voluntary, and readiness information is self-reported by participating projects. Reported statuses have not been independently verified by Ethereum client developers. A "Ready" status reflects the project's own assessment and does not constitute an official certification or guarantee of mainnet readiness by Ethereum Clients.

---

## EIP-7732: Validator & Operator Readiness

Projects should assess the areas relevant to their operations.

| Readiness Area | What to Check |
| --- | --- |
| **Client Compatibility** | Compatible CL, EL, and validator client versions |
| **PTC Duties** | Correct assignment and timely submission of Payload Timeliness Committee (PTC) attestations |
| **Payload Availability** | Correct handling/reporting of payload timeliness and required data availability |
| **Block Proposal** | Correct handling of the ePBS proposal flow, including builder and self-build paths |
| **Attestation & Fork Choice** | Correct validator behavior under the new ePBS validation and fork-choice flow |
| **Failure & Recovery** | Handling of missing/delayed payloads, builder failures, network disruption, and client restarts |
| **Monitoring & Alerting** | Visibility into PTC duties, missed/late duties, payload failures, and proposal issues |
| **Performance** | CPU, memory, bandwidth, latency, and missed-duty impact |
| **Key Management / Signing** | Compatibility with remote signers, HSMs, custody, and existing validator key-management infrastructure |
| **Failover** | Backup validator infrastructure, failover, and disaster-recovery setups continue to operate correctly |
| **Operational Changes** | Required changes to configuration, runbooks, on-call procedures, or infrastructure |
| **External Dependencies** | Dependencies on builders, relays, signers, cloud providers, custody/key-management systems, or other third parties |
| **Penalty / Slashing Considerations** | Any new failure modes or penalty/slashing exposure identified during testing |

> Projects do not need to test/report every area. Report the areas relevant to your services and identify any gaps or blockers.

## Validator Operators & Staking Providers

| Project | Service / Infrastructure | Client Stack | Network Tested | Status | Evidence / Release | Blockers / Notes | Additional Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Your Project | Validator Operator | CL / EL / VC | Devnet / Testnet | ⭕ | Link | - | - |

## Validator Client & Infrastructure Providers

For projects providing validator software, remote signing, monitoring, staking infrastructure, key management, or related services.

| Project | Category | EIP-7732 Changes Tested | Network Tested | Status | Evidence / Release | Blockers / Notes | Additional Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Your Project | Validator Client / Monitoring / Signing / Infrastructure | PTC / Proposal / Monitoring | Devnet / Testnet | ⭕ | Link | - | - |

## Builder & Relay Infrastructure

For builders, relays, and other block-production infrastructure affected by the transition to ePBS.

| Project | Category | EIP-7732 Changes Tested | Network Tested | Status | Evidence / Release | Blockers / Notes | Additional Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Your Project | Builder / Relay | Bidding / Payload Reveal / Block Production | Devnet / Testnet | ⭕ | Link | - | - |

## Known Issues & Mainnet Blockers

Use this section for issues affecting multiple operators or requiring coordination with client and testing teams.

| Project | Issue / Concern | Severity | Tracking Link | Status |
| --- | --- | --- | --- | --- |
| - | - | - | - | - |

**Severity:** Critical / High / Medium / Low

Please link technical issues to the relevant client, specification, or testing repository whenever possible.

## Additional Operator Feedback

Projects are encouraged to highlight:

- New operational requirements introduced by EIP-7732.
- Monitoring, metrics, or alerting gaps.
- Unexpected validator behavior or missed duties.
- Infrastructure performance or resource requirements.
- Key management, remote signer, or HSM compatibility concerns.
- Failover or high-availability concerns.
- New penalty or slashing risks observed during testing.
- Dependencies on external infrastructure or service providers.
- Missing documentation, APIs, or tooling.
- Potential mainnet readiness blockers.

Feedback can be included in **Additional Comments** or linked to a GitHub issue, PR, test report, or other public documentation.

---

## References

- [EIP-7732: Enshrined Proposer-Builder Separation](https://eips.ethereum.org/EIPS/eip-7732)
- [Ethereum Consensus Specifications](https://github.com/ethereum/consensus-specs)
- [Ethereum Beacon APIs](https://github.com/ethereum/beacon-APIs)
- [Ethereum PM Repository](https://github.com/ethereum/pm)

---

*Maintained collaboratively by Ethereum ecosystem contributors. Project readiness information is provided by participating teams.*


