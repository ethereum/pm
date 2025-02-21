# Champion an EIP

## Preamble

When championing an [EIP](https://eips.ethereum.org/), you should expect to spend at least as much time building social consensus as writing or testing code. Network upgrades require broad agreement from stakeholders who care about and support the change before it can be deployed. Taking an EIP from rough draft to mainnet can be a multi-year process.

<details>
<summary>What does not warrant an EIP?</summary>

- [ERCs](https://eips.ethereum.org/erc) (Ethereum Request for Comment) are not EIPs. They are application-layer or interop standards that may be adopted by the Ethereum community, but are not part of the Ethereum protocol and do not require a network upgrade.
- TODO: other out-of-scope definitions

</details>

## Socialize your idea

First, look for prior art. Are there related past EIPs? Does it make sense to extend or revive them?

If you're ready to move forward, consider the following channels when soliciting feedback on your idea:

- [Ethereum Magicians: Primordial Soup](https://ethereum-magicians.org/c/magicians/primordial-soup/9)
- [ethresear.ch](https://ethresear.ch/)
- [Core: Eth R&D Discord](https://discord.gg/EVTQ9crVgQ)
- [AllCoreDevs](https://github.com/ethereum/pm?tab=readme-ov-file#allcoredevs-meetings-overview) or Breakout Room meetings
- [Wallets: AllWalletDevs](https://t.me/AllWalletDevs)
- [NFTs: NFT Standards WG Telegram](https://t.me/nftstandards)
- IRL events, e.g., a working group at [Devcon](https://devcon.org/) or [Devconnect](https://devconnect.org/)

## Write the EIP

Once you’re satisfied with the momentum your idea has generated, formally specify the network changes within an EIP using the [template](https://github.com/ethereum/EIPs/blob/master/eip-template.md?plain=1).

<details>   
<summary>Reference examples</summary>

TODO: ~3 well-written EIPs to reference

</details>

## Implement the change in the spec and generate client tests

> **Note:** maintainers are available to help during this phase.

Once the EIP is published, you can make it much easier for the community to evaluate your idea by writing a reference implementation and generating client tests.

<details>
<summary>If your EIP impacts the Execution Layer (EL):</summary>

- Implement your changes in the [execution-specs](https://github.com/ethereum/execution-specs) (EELS)
  - EIP authors are encouraged to attempt the implementation on their own. Once a PR is created, EELS maintainers regularly step in to provide feedback or polish the implementation.
  - Reference the [EIP Author's Manual](https://github.com/ethereum/execution-specs/blob/master/EIP_AUTHORS_MANUAL.md).
- Generate client tests via the [execution-specs-tests](https://github.com/ethereum/execution-specs-tests) (EEST)
  - This step is frequently performed or augmented by EEST maintainers, but EIP authors are encouraged to make an attempt.
  - Reference the [EEST docs](https://ethereum.github.io/execution-spec-tests/getting_started/quick_start/).

</details>

<details>
<summary>If your EIP impacts the Consensus Layer (CL):</summary>

- Implement the feature in the [consensus-specs](https://github.com/ethereum/consensus-specs) repo. Once a PR is created, repo maintainers will provide feedback and guide next steps.
- Reference the feature addition [docs](https://github.com/ethereum/consensus-specs/blob/dev/docs/docs/new-feature.md).
- Update [generators](https://github.com/ethereum/consensus-specs/tree/dev/tests/generators) and generate client tests.  
</details>

## Local interop

> **Note:** maintainers are available to help during this phase.

Once at least one client team has implemented the change, network testing can begin. Depending on the nature of your change, several [ethPandaOps](https://ethpandaops.io/projects/) tools may be appropriate to leverage here. You will be guided by the testing teams and/or the ethPandaOps team on how to proceed.

Your EIP may require testing with various tools, including but not limited to the following:

- [Kurtosis](https://github.com/ethpandaops/ethereum-package) - private, modular multi-client devnets
- [assertoor](https://github.com/ethpandaops/assertoor) - a robust network testing framework
- [Hive](https://github.com/ethereum/hive) - an integration testing framework for clients

---

# EIP maturity stages

As defined in [EIP-1](https://eips.ethereum.org/EIPS/eip-1), each EIP has a lifecycle that includes the following stages: `Draft`, `Review`, `Last Call`, `Final`, `Stagnant`, `Withdrawn`, and `Living`.

Separate from the EIP lifecycle stages, [EIP-7723](https://eips.ethereum.org/EIPS/eip-7723) introduced a new status for each EIP: Network Upgrade Inclusion Stages. At any point, an EIP can be in one of the following stages: `Proposed for Inclusion`, `Considered for Inclusion`, `Declined for Inclusion`, `Scheduled for Inclusion`, or `Included` in a specific network upgrade.

## Proposed for Inclusion (PFI)

Anyone can open a PR against the fork [Meta EIP](https://eips.ethereum.org/EIPS/eip-7600) to propose an EIP for inclusion in the next network upgrade. Client teams will review each.

## Considered for Inclusion (CFI)

In order for an EIP to be `Considered for Inclusion` in a network upgrade, an open spec implementation PR is encouraged. Prior to being `Scheduled for Inclusion`, the implementation is required.

If client teams support including the EIP in a network upgrade, it will be moved to `Considered for Inclusion`. At this point, the EIP is expected to be included in the upgrade's devnet cycle.

## Declined for Inclusion (DFI)

A proposed or considered EIP may be designated `Declined for Inclusion` if client or testing teams find good reason. This does not prohibit the EIP from being considered for inclusion in a future network upgrade.

## Scheduled for Inclusion (SFI)

When client and testing teams agree that the EIP is thoroughly tested and is a priority for the upcoming release, it earns the `Scheduled for Inclusion` designation.

## Included

After the network upgrade goes live, the EIP is designated `Included`.