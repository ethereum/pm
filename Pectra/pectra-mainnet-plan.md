# Mainnet Upgrade & Incident Response Team Plan

## Upgrade Information

| Epoch | Start Slot | Unix | UTC (+00:00) | Moscow (+03:00) | Los Angeles (-07:00) | New York (-04:00) | Brisbane (+10:00) 
 | -- | -- | -- | -- | -- | -- | -- | -- 
|  364032 | 11649024 | 1746612311 | 2025-05-07 10:05:11 | 2025-05-07 13:05:11 | 2025-05-07 03:05:11 | 2025-05-07 06:05:11 | 2025-05-07 20:05:11 | 2025-05-07 20:05:11

## Upgrade / Incident Response team

### Client Team Coordinators 
| Client Team | Primary | Backup |
|-------------|---------------------|--------------------|
| Besu | [Name] | [Name] |
| Erigon | Somnath Banerjee | Andrew Ashikhmin |
| Geth | [Name] | [Name] |
| Grandine | [Name] | [Name] |
| Lighthouse | [Name] | [Name] |
| Lodestar | Phil Ngo | Nico Flaig |
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
