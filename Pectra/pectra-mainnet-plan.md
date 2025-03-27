# Mainnet Upgrade & Incident Response Team Plan

## Upgrade Information

***Tentative, to be confirmed on [ACDC#154](https://github.com/ethereum/pm/issues/1399)***

| Epoch | Start Slot | UTC (+00:00) | Moscow (+03:00) | Los Angeles (-07:00) | New York (-04:00) | Brisbane (+10:00) 
 | -- | -- | -- | -- | -- | -- | -- 
| 362496 | 11599872 | 2025-04-30 14:14:47 | 2025-04-30 17:14:47 | 2025-04-30 07:14:47 | 2025-04-30 10:14:47 | 2025-05-01 00:14:47 

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
| Communication Coodinator | Tim Beiko | [Name] |
| Security Coordinator | [Name] | [Name] |

## Communication Channels
- **Primary Communication:** `#pectra-upgrade` (Eth R&D Discord)
    - Channel to be created ~24h before the upgrade and archived once upgrade has successfully activated. 
- **Status Updates:** `#announcements` (Eth R&D Discord)

## Upgrade Verification post upgrade
- [ ] All clients remained in consensus throughout the upgrade
- [ ] Chain finalized
- [ ] Validator participation and block production (monitored for at least 32 epochs)
- [ ] Verified stability of the network for 48 hours after upgrade.

## [TODO] EIP-specific test cases on Ethereum mainnet 
- [ ] EIP-XXXX
    - [ ] Test Case 1
    - [ ] Test Case 2
    - [ ] ...
