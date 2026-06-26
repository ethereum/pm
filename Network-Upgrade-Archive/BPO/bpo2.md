# BPO2 — Blob-Parameter-Only Upgrade #2 (Mainnet)

BPO2 is the **second** mainnet Blob-Parameter-Only (BPO) upgrade, deployed approximately one month after [BPO1](./bpo1.md). It continues the staged expansion of blob capacity under [EIP-7892](https://eips.ethereum.org/EIPS/eip-7892) following the Fusaka upgrade.

For shared BPO context (mechanism scope, source-of-truth runtime configuration, coordination notes, and timeline references), see [bpo1.md](./bpo1.md).

## BPO2-specific references

- **Meta EIP:** [EIP-8135: Hardfork Meta - BPO2](https://eips.ethereum.org/EIPS/eip-8135) — parameters, activation time, base fee update fraction.
- **Predecessor:** Builds directly on the parameter set introduced by [BPO1](./bpo1.md) / [EIP-8134](https://eips.ethereum.org/EIPS/eip-8134).

## Post-deployment analysis

Unlike BPO1, BPO2 has been the subject of dedicated empirical study because it is the first BPO to push the network into a parameter regime where blob counts can exceed the pre-Fusaka maximum:

- [Blob Analysis after Fusaka and BPO Updates](https://ethresear.ch/t/blob-analysis-after-fusaka-and-bpo-updates/23853) — MigaLabs study of blob throughput and slot stability after BPO2 activation. Findings include observed capacity underutilization and missed-slot correlation at high blob counts, with a follow-up at the 100-day mark showing the early instability had been mitigated by client-side improvements.

This analysis is the primary feedback signal informing whether additional BPO upgrades should be scheduled.

## BPO2 activation across networks

Historical record of BPO2 activation on each network. Mainnet activation parameters are also recorded in [EIP-8135](https://eips.ethereum.org/EIPS/eip-8135); per-network testnet activations are recorded in [EIP-7606](https://eips.ethereum.org/EIPS/eip-7607), added here for quick reference:
| Network Name | Activation Epoch | Activation Timestamp | Activation Time (UTC) | Fork ID      |
| ------------ | ---------------- | -------------------- | --------------------- | ------------ |
| Holešky      | 167936           | 1760389824           | 2025-10-13 21:10:24   | 0x9bc6cb31   |
| Sepolia      | 275712           | 1761607008           | 2025-10-27 23:16:48   | 0x268956b6   |
| Hoodi        | 54016            | 1762955544           | 2025-11-12 13:52:24   | 0x23aa1351   |
| Mainnet      | 419072           | 1767747671           | 2026-01-07 01:01:11   | 0x07c9462e   |
