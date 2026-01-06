# Championing an EIP

## Preamble

This document is focused on the process for [Core EIPs](https://eips.ethereum.org/core), i.e., those that require a hard fork to be included in a network upgrade. Out-of-scope for this document are [ERC](https://eips.ethereum.org/erc)s and other non-Core EIPs (Networking, Interface, Meta, Informational) that do not require a hard fork.

When championing a Core EIP, the amount of social consensus-building required is often proportional to the scale and impact of the change. Minor technical fixes with clear benefits may need little coordination, while proposals affecting core economic mechanisms — like staking rewards — may require extensive debate and advocacy. Taking an EIP from rough draft to mainnet requires broad stakeholder agreement and can be a multi-year process.

## Socialize Your Idea

First, look for prior art. Are there related [past EIPs](https://eips.ethereum.org/core#draft)? Does it make sense to extend or revive them?

If you're ready to move forward, consider the following channels when soliciting feedback on your idea:

- [Ethereum Magicians: Primordial Soup](https://ethereum-magicians.org/c/magicians/primordial-soup/9)
- [ethresear.ch](https://ethresear.ch/)
- [Core: Eth R&D Discord](https://discord.gg/EVTQ9crVgQ)
- [AllCoreDevs](https://github.com/ethereum/pm?tab=readme-ov-file#allcoredevs-meetings-overview) or Breakout Room meetings
- [Wallets: AllWalletDevs](https://t.me/AllWalletDevs)
- [NFTs: NFT Standards WG Telegram](https://t.me/nftstandards)
- IRL events, e.g., a working group at [Devcon](https://devcon.org/) or [Devconnect](https://devconnect.org/)

## Write the EIP

Once you’re satisfied with the momentum your idea has generated, formally specify the network changes within an EIP using the [template](https://github.com/ethereum/EIPs/blob/master/eip-template.md?plain=1). [EIP-1](https://eips.ethereum.org/EIPS/eip-1#eip-header-preamble) provides more context on the template and the EIP process more broadly.

<details>   
<summary>Reference examples</summary>

Here are some strong reference examples, each with a note on what makes them well-written. Keep in mind that the EIP template has evolved over time, so while these were exemplary when published, some may not align with today's format.

- [EIP-1153](https://eips.ethereum.org/EIPS/eip-1153) - a once-stagnant EIP that was revived and shipped to mainnet
- [EIP-1884](https://eips.ethereum.org/EIPS/eip-1884) - great rationale
- [EIP-3855](https://eips.ethereum.org/EIPS/eip-3855) - simple feature
- [EIP-4399](https://eips.ethereum.org/EIPS/eip-4399) - great rationale
- [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844) - huge feature, cross-layer EIP
- [EIP-6780](https://eips.ethereum.org/EIPS/eip-6780) - only deprecated feature in Ethereum's history, well spec'ed

</details>

## Implement Spec Changes & Generate Tests

Once the EIP is published, you can make it much easier for the community to evaluate your idea by writing a reference implementation and generating test cases. Cross-layer EIPs will require both Execution Layer (EL) and Consensus Layer (CL) implementations.

<details>
<summary>If your EIP impacts the Execution Layer:</summary>

- Implement your changes in the [execution-specs](https://github.com/ethereum/execution-specs) (EELS)
  - EIP authors are encouraged to attempt the implementation on their own. Once a PR is created, EELS maintainers regularly step in to provide feedback or polish the implementation.
  - Reference the [EIP Author's Manual](https://github.com/ethereum/execution-specs/blob/master/EIP_AUTHORS_MANUAL.md).
- Generate client tests via the [execution-spec-tests](https://github.com/ethereum/execution-spec-tests) (EEST)
  - This step is frequently performed or augmented by EEST maintainers, but EIP authors are encouraged to make an attempt.
  - Reference the [EEST docs](https://ethereum.github.io/execution-spec-tests/getting_started/quick_start/).
- Reach out for help in the [ETH R&D Discord](https://discord.gg/EVTQ9crVgQ), `#el-testing` channel.

</details>

<details>
<summary>If your EIP impacts the Consensus Layer:</summary>

- Implement the feature in the [consensus-specs](https://github.com/ethereum/consensus-specs) repo. Once a PR is created, repo maintainers will provide feedback and guide next steps.
- Update [generators](https://github.com/ethereum/consensus-specs/tree/dev/tests/generators) and generate client tests.  
- Reference the feature addition [docs](https://github.com/ethereum/consensus-specs/blob/dev/docs/docs/new-feature.md)
- Reach out for help in the [ETH R&D Discord](https://discord.gg/EVTQ9crVgQ), `#cl-testing` channel.

</details>

## Local Interop

Once your EIP has been implemented in at least one production client, network testing can begin. Depending on the nature of your change, several [ethPandaOps](https://ethpandaops.io/projects/) tools may be appropriate to leverage here.

You will be guided by the testing teams and/or the ethPandaOps team on how to proceed, but the general expectation is that your EIP will have reached the Considered for Inclusion (CFI) stage before the ethPandaOps team can commit resources to network testing.

Your EIP may require testing with various tools, including but not limited to the following:

- [Kurtosis](https://github.com/ethpandaops/ethereum-package) - private, modular multi-client devnets
- [assertoor](https://github.com/ethpandaops/assertoor) - a robust network testing framework
- [Hive](https://github.com/ethereum/hive) - an integration testing framework for clients

---

# EIP Status & Inclusion Stage

As defined in [EIP-1](https://eips.ethereum.org/EIPS/eip-1), each EIP has a status that reflects the state of its specification: `Draft`, `Review`, `Last Call`, `Final`, `Stagnant`, `Withdrawn`, and `Living`.

Separate from the EIP specification status, [EIP-7723](https://eips.ethereum.org/EIPS/eip-7723) introduced network upgrade inclusion stages for each EIP. At any point, an EIP can be in one of the following stages: `Proposed for Inclusion`, `Considered for Inclusion`, `Declined for Inclusion`, `Scheduled for Inclusion`, or `Included` within a specific network upgrade. If not included in one network upgrade, an EIP can be proposed for inclusion again in subsequent upgrades.

## Proposed for Inclusion (PFI)

Anyone can open a PR against a fork [Meta EIP](https://eips.ethereum.org/meta) to propose an EIP for inclusion in the next network upgrade. When doing so, please add a rationale for your proposal, such as in [this example](https://github.com/ethereum/EIPs/pull/9163). 

## Considered for Inclusion (CFI)

In order for an EIP to be `Considered for Inclusion` in a network upgrade, an open spec implementation PR is encouraged. Prior to being `Scheduled for Inclusion`, the implementation is required.

If client teams support including the EIP in a network upgrade, it will be moved to `Considered for Inclusion`. At this point, the EIP is expected to be included in the upgrade's devnet cycle.

## Declined for Inclusion (DFI)

A PFI or CFI'd EIP may be designated `Declined for Inclusion` if it is out of scope for the upgrade or if the EIP is not ready for inclusion. This does not prohibit the EIP from being Proposed for Inclusion again in a future network upgrade.

## Scheduled for Inclusion (SFI)

When client and testing teams agree that an EIP is thoroughly tested and is a priority for the upcoming release, it earns the `Scheduled for Inclusion` designation. By convention, EIPs need to be at least in `Review` to be SFI'd. When a network upgrade goes live on Ethereum testnets, all SFI'd EIPs will be moved to `Last Call`. 

## Included

After the network upgrade goes live on Ethereum mainnet, all EIPs included in it have their inclusion stage set to `Included` and their status moved to `Final`.
