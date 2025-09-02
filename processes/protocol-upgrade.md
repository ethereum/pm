# Ethereum Protocol Upgrade Process

## Abstract
This document specifies a checklist and incident response process for Ethereum protocol upgrades. It outlines procedures for managing upgrades across devnets, testnets, and mainnet, including security reviews, fork preparations, testing protocols, and communication strategies. This document aims to standardize the upgrade process to further increase network security and stability.

## Motivation
Ethereum has regular protocol upgrades that introduce performance, security and functionality enhancements to the protocol. Given the inherent complexity of these upgrades and the involvement of multiple teams and systems, a standardized approach reduces the likelihood of upgrades going wrong or a subpar incident response. This document addresses the need for a clear, systematic framework to manage the upgrade process efficiently, mitigate risks, and facilitate rapid incident response when necessary.

## Timelines

### General
- Upgrades must not be scheduled for major holidays or events.
- Bundling the mainnet upgrade with other upgrades should not be done.
- If multiple testnet upgrades are scheduled in advance, each testnet upgrade but must be at least 10 days apart, ideally aiming for two weeks between upgrades.
- In the event that multiple testnet upgrades are scheduled, and the first a testnet upgrade is not deemed a success, the next testnet upgrade is automatically cancelled. The next testnet must not be rescheduled until the first incident has been resolved, at which point the earliest point in time is 14 days from the All Core Devs (ACD) call it was agreed to proceed.
- Upgrades must not take place until at least clients representing 90% of the active weight pass all [consensus](https://github.com/ethereum/consensus-specs/) and [execution](https://github.com/ethereum/execution-spec-tests) tests, and are stable.
- An assessment must be done in ACD to assess if infrastructure external to the protocol is required to be upgraded for the upgrade to move forward.
- In the event that the upgrade fails, an incident retrospective must take place to understand what went wrong and how it can be proved or strongly inferred that it won't happen on the next testnet.
- ACD can, if needed, override parts of this document. For example in the event of a contentious fork where a client with more than 10% of mainnet validators could otherwise hold up the process.

### EIPs
- An assessment must be done if any EIPs and their client implementations should undergo an external review.
- SFI requirements in [EIP-7723](https://eips.ethereum.org/EIPS/eip-7723#scheduled-for-inclusion) must have been followed to for example ensure test vectors are covered.
- A date for last inclusion of Ethereum Improvement Proposals (EIPs) in the upgrade must be set.
- In the event that an included EIP has a significant issue that requires a change to the EIP, additional testing, a security assessment and an agreement on ACD must be done before the upgrade process continues.

### Devnets
- Devnets are expected to experience issues, are short lived, and a new one should be launched when relevant. Given their short lived nature, they are considered out of scope of this process.

### Testnets
- There must be a 14 day period between client releases being ready, and the first testnet going live.
    - This is to provide time for internal security reviews, inclusion of upgrade specific code in the bug bounty program, and potential external security reviews.

### Mainnet
- The upgrade must have gone through at least two testnets.
- Mainnet upgrade less than 30 days after the final testnet has been verified to have been successfully upgraded. This is to ensure enough time has been given to test and spot potential issues before going live on mainnet and to allow for downstream projects to plan their upgrades. L2s need time to produce DAO proposals, organize their own upgrades, etc.

## Verifying & Reviewing
### Internal Reviews
- A channel on the Eth R&D Discord must be setup for each EIP in the upgrade, to ensure coordination between client devs, test engineers and security researchers working on each EIP.
- Each EIP that has been assigned CFI should be considered to have one or more core developer per team assigned.
- Each EIP that has been assigned SFI should have one or more core developer per team assigned.
    - Test objectives:
        - Verify that the EIP is implemented according to specifications and pass tests.
    - Security objectives:
        - Verify the security of the EIP itself.
        - Verify that the EIP is implemented according to specifications.
        - Continually review the client implementation of the EIP from a security point of view.
- Notify responsible parties of potential issues, i.e., client team in the case of a client issue, and follow up.

### External Reviews
- Historically, when smart contract code has been written an external audit has been triggered, but other areas may also warrant an external audit.
- In the event that an external review is deemed appropriate, a Request for Proposal (RFP) should be used to gather proposals from various providers.
- Any findings must be notified and signed off by the party responsible for fixing the finding (i.e., client team in the case of a client vulnerability).

### Informing Ecosystem
- After testing, internal and external reviews have been completed, a blog post should be published describing the process and any findings.

### Include new code base in bug bounty
#### Ethereum Foundation Bug Bounty Program
- Upgrade specific code should be included in the bug bounty program as soon as client releases are ready for the first testnet upgrade.

####  Bug Bounty Competition
- A bug bounty competition may be run to crowdsource finding issues, but not prior to:
    - Internal reviews are completed.
    - External reviews are completed (in the event they are taking place).
    - Client teams have released their testnets releases.
- The Bug Bounty Competition must end no later than three weeks prior to the mainnet upgrade, to ensure coordination efforts for potential client releases can be done in time.


## Upgrade Validation
### Devnets
- Targeted tests must be done for each EIP to confirm functionality, with documented results.
- Interoperability across clients within the devnet must be verified.
- A generation of high volumes of transactions, edge-case operations, and network partitions to see how clients handle unexpected loads or network splits must be done.
- Tests covering periods of non-finality should be done.

### Testnets
- Verification that all clients remain in consensus through the upgrade must be done.
- Running targeted tests must be done for each EIP to confirm functionality, with documented results.
- Monitoring of logs and metrics from all clients must be done.
- Closely monitoring finalization, validator participation and block production post-fork for at least 32 epochs must be done before success may be defined.
- A continued expanded monitoring for 48 hours must be done after the upgrade, to ensure stability under normal usage.

### Mainnet
- Follow the same procedures as testnets.

## Incident Response Plan
### Role Assignment
- Each upgrade must have an Incident Response team with:
  - Client Team Coordinators (one per client team): Main Point of Contact for the client team, ensures client teams diagnose and resolves client bugs.
  - DevOps Coordinator: Ensures infrastructure and debugging is done.
  - Testing Coordinator: Ensures testing is done.
  - Communication Coordinator: Ensures core devs receive relevant updates, and that community communication is done.
  - Security Coordinator: Ensures security coordination is done.
- Who holds these roles for the specific upgrade should be decided on ACD, and each role must have a dedicated person assigned to it, including a backup which must take over if necessary.
    - An assessment must be done around the most suitable backup. This could for example be having a backup in a different time zone, or a backup in a separate organization or team.
- These roles are not expected to do everything on their own, but are responsible to ensure the responsibilities are being done during an incident, or to transfer responsibilities to someone else if they can no longer fulfil their duties.
- The roles should share their phone numbers through the Incident Response team group on Signal.
- The roles must be on-call for 48 hours after the activation of the upgrade, in the event that the upgrade fails after being initially classified as a success.
- If there is an incident, it is the responsibility of the Incident Response team to ensure that the incident is resolved as soon as possible and that their responsibilities are successfully executed.

### Client Team Coordinators
- Ensures progress/issues are shared in real-time in the `default communication` channel.
- Ensures information is forwarded to their respective teams or users.

### DevOps Coordinator
- Ensures network metrics (e.g., block production, finalization rate, node health) are being monitored.
- Ensures infrastructure issues are triaged.
- Ensures anomalies are communicated to the default communication channel.

### Testing Coordinator
- Ensures testing efforts are taking place if issues are found during the upgrade.

### Communication Coordinator
- Creates a `$fork-$network-incident_response_team` group on Signal.
- Ensures updates are posted on the `status website` as the upgrade happens (activation, finalization, any issues).
- Ensures distribution of emergency updates or patches are done if needed.
- Ensures an emergency core devs meeting is called if necessary.
- Ensures that if there is an incident, community updates are provided at least every 120 minutes.
- Ensures that after the upgrade is complete, a post-fork summary is published.

### Security Coordinator
- Ensures security procedures are followed if a vulnerability is discovered around the upgrade.
- Ensures coordination is done with external researchers and bounty reporters for findings.
- Ensures a severity of the incident is defined.

### Escalation Procedures
- Utilize the ```#$fork-$network-upgrade``` Eth R&D channel on Discord (default communication channel).
    - This channel has permissions so anyone can read, but only core devs can write.
- In the event there is a necessity for sensitive information sharing, a member of the Incident Response team should facilitate setting up a secure communication channel.

### Incident Severity Levels
- Low: Minor bugs, no immediate risk. Fix included in next planned release.
- Medium: Possible node crashes or partial network degradation. Out-of-band fix.
- High: Critical consensus flaw, chain halt, or security exploit. All-hands emergency response.

### Decision-Making Framework
- For high-severity issues (e.g., chain split, finality failure), the Incident Response team is responsible to ensure appropriate steps are taken to resolve the incident as soon as possible.
- Decisions made outside of the default communication channel should be documented.


## Templates
* These templates should be added to the ```$fork-pm.md``` file for each upgrade, e.g., https://github.com/ethereum/pm/blob/master/Pectra/pectra-pm.md

```markdown
# Holesky Upgrade & Incident Response Team Plan

## Upgrade Information
- **Upgrade Date:**

## Upgrade / Incident Response team

### Client Team Coordinators 
| Client Team | Primary | Backup |
|-------------|---------------------|--------------------|
| Besu | [Name] | [Name] |
| Erigon | [Name] | [Name] |
| Geth | [Name] | [Name] |
| Grandine | [Name] | [Name] |
| Lighthouse | [Name] | [Name] |
| Lodestar | [Name] | [Name] |
| Nimbus | [Name] | [Name] |
| Nethermind | [Name] | [Name] |
| Prysm | [Name] | [Name] |
| Reth | [Name] | [Name] |
| Teku | [Name] | [Name] |

### Coordinators
| Role | Primary | Backup |
|------|---------|----------------------------|
| DevOps Coordinator | [Name] | [Name] |
| Testing Coordinator | [Name] | [Name] |
| Communication Coodinator | [Name] | [Name] |
| Security Coordinator | [Name] | [Name] |

## Communication Channels
- **Primary Communication:** Discord `#$fork-upgrade` (Eth R&D)
- **Status Updates:** `status page`

## Upgrade Verification post upgrade
- [ ] EIP-XXXX
    - [ ] Test Case 1
    - [ ] Test Case 2
    - [ ] ...
- [ ] All clients remained in consensus throughout the upgrade
- [ ] Chain finalized
- [ ] Validator participation and block production (monitored for at least 32 epochs)
- [ ] Verified stability of the network for 48 hours after upgrade.
```

```markdown
# Sepolia Upgrade & Incident Response Team Plan

## Upgrade Information
- **Upgrade Date:**

## Upgrade / Incident Response team

### Client Team Coordinators 
| Client Team | Primary | Backup |
|-------------|---------------------|--------------------|
| Besu | [Name] | [Name] |
| Erigon | [Name] | [Name] |
| Geth | [Name] | [Name] |
| Grandine | [Name] | [Name] |
| Lighthouse | [Name] | [Name] |
| Lodestar | [Name] | [Name] |
| Nimbus | [Name] | [Name] |
| Nethermind | [Name] | [Name] |
| Prysm | [Name] | [Name] |
| Reth | [Name] | [Name] |
| Teku | [Name] | [Name] |

### Coordinators
| Role | Primary | Backup |
|------|---------|----------------------------|
| DevOps Coordinator | [Name] | [Name] |
| Testing Coordinator | [Name] | [Name] |
| Communication Coodinator | [Name] | [Name] |
| Security Coordinator | [Name] | [Name] |

## Communication Channels
- **Primary Communication:** Discord `#$fork-upgrade` (Eth R&D)
- **Status Updates:** `status page`

## Upgrade Verification post upgrade
- [ ] EIP-XXXX
    - [ ] Test Case 1
    - [ ] Test Case 2
    - [ ] ...
- [ ] All clients remained in consensus throughout the upgrade
- [ ] Chain finalized
- [ ] Validator participation and block production (monitored for at least 32 epochs)
- [ ] Verified stability of the network for 48 hours after upgrade.
```

```markdown
# Hoodi Upgrade & Incident Response Team Plan

## Upgrade Information
- **Upgrade Date:**

## Upgrade / Incident Response team

### Client Team Coordinators 
| Client Team | Primary | Backup |
|-------------|---------------------|--------------------|
| Besu | [Name] | [Name] |
| Erigon | [Name] | [Name] |
| Geth | [Name] | [Name] |
| Grandine | [Name] | [Name] |
| Lighthouse | [Name] | [Name] |
| Lodestar | [Name] | [Name] |
| Nimbus | [Name] | [Name] |
| Nethermind | [Name] | [Name] |
| Prysm | [Name] | [Name] |
| Reth | [Name] | [Name] |
| Teku | [Name] | [Name] |

### Coordinators
| Role | Primary | Backup |
|------|---------|----------------------------|
| DevOps Coordinator | [Name] | [Name] |
| Testing Coordinator | [Name] | [Name] |
| Communication Coodinator | [Name] | [Name] |
| Security Coordinator | [Name] | [Name] |

## Communication Channels
- **Primary Communication:** Discord `#$fork-upgrade` (Eth R&D)
- **Status Updates:** `status page`

## Upgrade Verification post upgrade
- [ ] EIP-XXXX
    - [ ] Test Case 1
    - [ ] Test Case 2
    - [ ] ...
- [ ] All clients remained in consensus throughout the upgrade
- [ ] Chain finalized
- [ ] Validator participation and block production (monitored for at least 32 epochs)
- [ ] Verified stability of the network for 48 hours after upgrade.
```

```markdown
# Mainnet Upgrade & Incident Response Team Plan

## Upgrade Information
- **Upgrade Date:**

## Upgrade / Incident Response team

### Client Team Coordinators 
| Client Team | Primary | Backup |
|-------------|---------------------|--------------------|
| Besu | [Name] | [Name] |
| Erigon | [Name] | [Name] |
| Geth | [Name] | [Name] |
| Grandine | [Name] | [Name] |
| Lighthouse | [Name] | [Name] |
| Lodestar | [Name] | [Name] |
| Nimbus | [Name] | [Name] |
| Nethermind | [Name] | [Name] |
| Prysm | [Name] | [Name] |
| Reth | [Name] | [Name] |
| Teku | [Name] | [Name] |

### Coordinators
| Role | Primary | Backup |
|------|---------|----------------------------|
| DevOps Coordinator | [Name] | [Name] |
| Testing Coordinator | [Name] | [Name] |
| Communication Coodinator | [Name] | [Name] |
| Security Coordinator | [Name] | [Name] |

## Communication Channels
- **Primary Communication:** Discord `#$fork-upgrade` (Eth R&D)
- **Status Updates:** `status page`

## Upgrade Verification post upgrade
- [ ] EIP-XXXX
    - [ ] Test Case 1
    - [ ] Test Case 2
    - [ ] ...
- [ ] All clients remained in consensus throughout the upgrade
- [ ] Chain finalized
- [ ] Validator participation and block production (monitored for at least 32 epochs)
- [ ] Verified stability of the network for 48 hours after upgrade.
```
