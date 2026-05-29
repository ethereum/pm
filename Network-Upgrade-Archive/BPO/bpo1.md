# BPO1 — Blob-Parameter-Only Upgrade #1 (Mainnet)

BPO1 is the **first** mainnet Blob-Parameter-Only (BPO) upgrade, deployed as a config-only fork following the Fusaka network upgrade. It establishes the BPO mechanism on mainnet and provides the initial incremental increase in blob capacity after PeerDAS activation.

The BPO mechanism itself is specified in [EIP-7892: Blob Parameter Only Hardforks](https://eips.ethereum.org/EIPS/eip-7892). BPO upgrades modify only blob-related parameters; no other protocol behavior is affected.

## About BPO upgrades (shared context for all BPO entries)

- **Scope:** Only blob target, blob max, and the base fee update fraction change. Nothing else.
- **Source of truth for runtime values:** [`eth-clients/mainnet/metadata/genesis.json`](https://github.com/eth-clients/mainnet/blob/main/metadata/genesis.json) (`bpoNTime` and `blobSchedule` fields).
- **Coordination notes** (activation slots, epochs, fork IDs across all testnets and mainnet; client readiness; cell-level optimization status):
  - [Fusaka & BPO timelines](https://notes.ethereum.org/@bbusa/fusaka-bpo-timeline)
  - [Blob scaling in 2026](https://notes.ethereum.org/@ethpandaops/blob-scaling-2026)
  - [Fusaka Mainnet Announcement](https://blog.ethereum.org/2025/11/06/fusaka-mainnet-announcement)

These shared references apply to every BPO entry in this archive and are not repeated in subsequent BPO files.

## BPO1-specific references

- **Meta EIP:** [EIP-8134: Hardfork Meta - BPO1](https://eips.ethereum.org/EIPS/eip-8134) — parameters, activation time, base fee update fraction.
- **Significance:** First mainnet exercise of the EIP-7892 mechanism. Establishes the precedent for config-only forks between major network upgrades and produces the first empirical data on whether the mechanism functions as designed at the coordination layer.
- **Predecessor blob schedule:** Inherits from the Prague blob configuration set at the Pectra upgrade. See [EIP-7607: Hardfork Meta - Fusaka](https://eips.ethereum.org/EIPS/eip-7607) for the immediately preceding upgrade context.
