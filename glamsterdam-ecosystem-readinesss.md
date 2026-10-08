# Glamsterdam Validator & Operator Readiness Checklist

Tracking ecosystem readiness for validator operations and infrastructure changes introduced by [EIP-7732 (ePBS)](https://eips.ethereum.org/EIPS/eip-7732) as part of the Glamsterdam network upgrade.

This checklist is intended for validator operators, staking providers, validator client teams, and infrastructure projects.

## How to Participate

Projects are encouraged to submit a Pull Request (PR) to update their readiness status.

1. Add your project to the relevant table.
2. Update your testing status.
3. Link to a release, test report, GitHub issue, or documentation.
4. Include any known blockers or operational concerns.
5. Submit a PR to the [ethereum/pm](https://github.com/ethereum/pm) repository.

Projects can update their entries as testing progresses.

### Status Legend

- ⭕ Not Started
- 🛠️ In Progress
- 🧪 Testing
- ✅ Ready
- ⚠️ Blocked
- ➖ Not Applicable

**Note:** Readiness is self-reported by participating projects.
A "Ready" status does not constitute an official certification or guarantee of mainnet readiness.

---

## 1. Validator & Staking Infrastructure Readiness

Projects should assess the following areas relevant to their operations.

| Readiness Area | Description |
| --- | --- |
| Client Compatibility | Compatible CL, EL, and validator client versions |
| PTC Duties | Correct assignment and timely submission of Payload Timeliness Committee attestations |
| Payload Availability | Correct reporting of payload presence and blob data availability |
| Block Proposal | Support for ePBS builder selection, payload reveal, and self-build |
| Attestation & Fork Choice | Correct validator behavior under the new ePBS validation flow |
| Failure Recovery | Handling missing or delayed payloads, builder failures, and client restarts |
| Monitoring | Visibility into PTC duties, payload failures, and missed validator duties |
| Performance | Infrastructure capacity, bandwidth, latency, and validator performance |

Projects do not need to test every area. Report the areas relevant to your services and identify any gaps or blockers.

---

## 2. Validator Operators & Staking Providers

| Project | Service / Infrastructure | Client Stack | Network Tested | Status | Evidence / Release | Blockers / Notes | Additional Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Your Project | Validator Operator | CL / EL / VC | Devnet / Testnet | ⭕ | Link | - | - |

---

## 3. Validator Client & Infrastructure Providers

| Project | Category | EIP-7732 Changes Tested | Network Tested | Status | Evidence / Release | Blockers / Notes | Additional Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Your Project | Validator Client / Monitoring / Signing / Infrastructure | PTC / Proposal / Monitoring | Devnet / Testnet | ⭕ | Link | - | - |

---

## 4. Builder & Relay Infrastructure

| Project | Category | EIP-7732 Changes Tested | Network Tested | Status | Evidence / Release | Blockers / Notes | Additional Comments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Your Project | Builder / Relay | Builder Registration / Bidding / Payload Reveal | Devnet / Testnet | ⭕ | Link | - | - |

---

## 5. Known Issues & Mainnet Blockers

Use this section for issues affecting multiple operators or requiring coordination with client and testing teams.

| Project | Issue / Concern | Severity | Tracking Link | Status |
| --- | --- | --- | --- | --- |
| - | - | - | - | - |

Severity: Critical / High / Medium / Low

Please link technical issues to the relevant client, specification, or testing repository whenever possible.

---

## 6. Additional Operator Feedback

Projects are encouraged to share feedback on:

- New operational requirements introduced by EIP-7732.
- Additional monitoring, metrics, or alerting needs.
- Unexpected validator behavior or missed duties.
- Infrastructure performance or resource requirements.
- Missing documentation, APIs, or tooling.
- Potential mainnet readiness blockers.

Feedback can be submitted through a PR or linked GitHub issue.

---

## References

- [EIP-7732: Enshrined Proposer-Builder Separation](https://eips.ethereum.org/EIPS/eip-7732)
- [Ethereum Consensus Specifications](https://github.com/ethereum/consensus-specs)
- [Ethereum Beacon APIs](https://github.com/ethereum/beacon-APIs)
- [Ethereum PM Repository](https://github.com/ethereum/pm)

---

*Maintained collaboratively by Ethereum ecosystem contributors. Project readiness information is provided by participating teams.*


