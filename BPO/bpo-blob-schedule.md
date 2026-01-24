# Blob Schedule and BPO Upgrade Parameters (Mainnet)

This document provides a canonical reference for Ethereum mainnet blob parameter schedules and Blob-Parameter-Only (BPO) upgrades as reflected in client chain configuration.

The values documented here are sourced from execution client chain configuration and represent the authoritative activation timestamps and blob parameter values used by clients at runtime.

This file is intended to support:
- Upgrade coordination
- Tooling alignment
- Historical traceability
- Operator and ecosystem visibility

## Network

- **Chain ID:** 1 (Ethereum Mainnet)

## Upgrade Activation Times

All timestamps are Unix epoch seconds (UTC).

| Upgrade | Upgrade Category | Activation Field | Timestamp |
|---------|------------------|------------------|------------|
| **BPO2** | BPO | `bpo2Time` | 1767747671 |
| **BPO1** | BPO | `bpo1Time` | 1765290071 |
| Osaka | EL | `osakaTime` | 1764798551 |
| Prague | EL | `pragueTime` | 1746612311 |
| Cancun | EL | `cancunTime` | 1710338135 |
| Shanghai | EL | `shanghaiTime` | 1681338455 |
| Merge (Paris + Bellatrix) | Combined | `terminalTotalDifficulty` | 58,750,000,000,000,000,000,000 |
| Gray Glacier | EL | `grayGlacierBlock` | 15,050,000 |
| Arrow Glacier | EL | `arrowGlacierBlock` | 13,773,000 |
| London | EL | `londonBlock` | 12,965,000 |
| Berlin | EL | `berlinBlock` | 12,244,000 |
| Muir Glacier | EL | `muirGlacierBlock` | 9,200,000 |
| Istanbul | EL | `istanbulBlock` | 9,069,000 |
| Constantinople / Petersburg | EL | `constantinopleBlock`, `petersburgBlock` | 7,280,000 |
| Byzantium | EL | `byzantiumBlock` | 4,370,000 |
| Spurious Dragon | EL | `eip158Block` | 2,675,000 |
| Tangerine Whistle | EL | `eip150Block` | 2,463,000 |
| DAO Fork | EL | `daoForkBlock` | 1,920,000 |
| Homestead | EL | `homesteadBlock` | 1,150,000 |

#### Notes
* BPO = Blob-Parameter-Only upgrades
* EL = Execution Layer upgrades
* CL = Consensus Layer upgrades (none explicitly listed here as standalone events in this table)
* Combined = EL + CL coordinated upgrade (Merge)

## Blob Schedule Parameters

Blob parameters define the target and maximum number of blobs per block, as well as the base fee update fraction used for blob fee adjustment.

| Upgrade | Blob Target | Blob Max | BaseFeeUpdateFraction |
|---------|-------------|----------|------------------------|
| **Cancun** | 3 | 6 | 3,338,477 |
| **Prague** | 6 | 9 | 5,007,716 |
| **BPO1** | 10 | 15 | 8,346,193 |
| **BPO2** | 14 | 21 | 11,684,671 |

## Notes

- Blob-Parameter-Only (BPO) upgrades adjust only blob-related parameters and introduce no additional protocol changes.
- The BPO mechanism is specified in **[EIP-7892](https://eips.ethereum.org/EIPS/eip-7892)**.
- Parameter values listed here are taken directly from execution client chain configuration and represent production values.
- Activation timestamps reflect mainnet scheduling and may differ across test networks or devnets.

## Source (Chain Configuration Excerpt)

```json
"bpo1Time": 1765290071,
"bpo2Time": 1767747671,
"blobSchedule": {
  "cancun": {
    "target": 3,
    "max": 6,
    "baseFeeUpdateFraction": 3338477
  },
  "prague": {
    "target": 6,
    "max": 9,
    "baseFeeUpdateFraction": 5007716
  },
  "bpo1": {
    "target": 10,
    "max": 15,
    "baseFeeUpdateFraction": 8346193
  },
  "bpo2": {
    "target": 14,
    "max": 21,
    "baseFeeUpdateFraction": 11684671
  }
}
```

Please refer to [`genesis.json`](https://github.com/eth-clients/mainnet/blob/main/metadata/genesis.json#L41) for Blob-Parameter-Only (BPO) upgrade for upcoming scheduling parameter changes.
