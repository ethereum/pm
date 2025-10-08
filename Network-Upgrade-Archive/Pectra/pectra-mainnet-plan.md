# Mainnet Upgrade & Incident Response Team Plan

## Upgrade Information

| Epoch | Start Slot | Unix | UTC (+00:00) | Moscow (+03:00) | Los Angeles (-07:00) | New York (-04:00) | Brisbane (+10:00)
 | -- | -- | -- | -- | -- | -- | -- | --
|  364032 | 11649024 | 1746612311 | 2025-05-07 10:05:11 | 2025-05-07 13:05:11 | 2025-05-07 03:05:11 | 2025-05-07 06:05:11 | 2025-05-07 20:05:11 | 2025-05-07 20:05:11

## Upgrade / Incident Response team

### Client Team Coordinators
| Client Team | Primary | Backup |
|-------------|---------------------|--------------------|
| Besu | Daniel Lehrner | Gabriel Trintinalia or Simon Dudley|
| Erigon | Somnath Banerjee | Andrew Ashikhmin |
| Geth | Felix Lange | Marius van der Wijden |
| Grandine | Saulius Grigaitis | Povilas Liubauskas or Tumas |
| Lighthouse | Sean Anderson | Michael Sproul |
| Lodestar | Phil Ngo | Nico Flaig |
| Nimbus | Dustin | Advaita Saha |
| Nethermind | Marek Moraczyński | Łukasz Rozmej <br> Kamil Chodoła <br> Ahmad Bitar |
| Prysm | Ping @prysmatic in the Eth R&D Discord | prysm@offchainlabs.com |
| Reth | Roman Krasiuk | Matthias Seitz |
| Teku | Enrico Del Fante | Paul Harris |

### Coordinators
| Role | Primary | Backup |
|------|---------|----------------------------|
| DevOps Coordinator | Parithosh | Barnabas |
| Testing Coordinator | Mario Vega (@marioevz) | Dan (@danceratopz) <br> Spencer (@spencer-tb) |
| Communication Coordinator | Tim Beiko | Alex Stokes |
| Security Coordinator | Fredrik Svantes | Justin Traglia |

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

## Disclaimer
The individuals and organisations named in this document have been listed solely so that other community members know whom to contact for faster coordination and incident-response during the Pectra network upgrade.

Their inclusion does not:
- Create any fiduciary, contractual, or other legal duty towards any other party;
- Constitute any representation, warranty, or guarantee of the performance, security, or outcome of the Pectra upgrade; or
- Give rise to any liability, whether in negligence, tort, contract, or otherwise, for any direct, indirect, or consequential damages (including any loss of funds) arising out of or in connection with the Pectra upgrade or reliance on this document.
