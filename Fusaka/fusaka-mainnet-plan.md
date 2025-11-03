# Mainnet Upgrade & Incident Response Team Plan

## Upgrade Information

| Epoch | Start Slot | Unix | UTC (+00:00) | Moscow (+03:00) | Los Angeles (-07:00) | New York (-04:00) | Brisbane (+10:00)
| 411392 | 13164544 | 1764798551 | 2025-12-03 21:49:11 | 2025-12-04 00:49:11 | 2025-12-03 13:49:11 | 2025-12-03 16:49:11 | 2025-12-04 07:49:11

## Upgrade / Incident Response team

### Client Team Coordinators
| Client Team | Primary | Backup |
|-------------|---------------------|--------------------|
| Besu | ||
| Erigon | ||
| Geth | | |
| Grandine | | |
| Lighthouse | ||
| Lodestar | | |
| Nimbus | | |
| Nethermind | | |
| Prysm | | |
| Reth | | |
| Teku | | |

### Coordinators
| Role | Primary | Backup |
|------|---------|----------------------------|
| DevOps Coordinator | Barnabas | Pari|
| Testing Coordinator | ||
| Communication Coordinator | | |
| Security Coordinator | ||

## Communication Channels
- **Primary Communication:** `#fusaka-upgrade` (Eth R&D Discord)
    - Channel to be created ~24h before the upgrade and archived once upgrade has successfully activated.
- **Status Updates:** `#announcements` (Eth R&D Discord)

## Upgrade Verification post upgrade
- [ ] All clients remained in consensus throughout the upgrade
- [ ] Chain finalized
- [ ] Validator participation and block production (monitored for at least 32 epochs)
- [ ] Verified stability of the network for 48 hours after upgrade.

## Disclaimer
The individuals and organisations named in this document have been listed solely so that other community members know whom to contact for faster coordination and incident-response during the Fusaka network upgrade.

Their inclusion does not:
- Create any fiduciary, contractual, or other legal duty towards any other party;
- Constitute any representation, warranty, or guarantee of the performance, security, or outcome of the Fusaka upgrade; or
- Give rise to any liability, whether in negligence, tort, contract, or otherwise, for any direct, indirect, or consequential damages (including any loss of funds) arising out of or in connection with the Fusaka upgrade or reliance on this document.
