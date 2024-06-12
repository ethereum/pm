# Light Clients Breakout Room #1

Note: This file is copied from [here](https://hackmd.io/@philknows/ryMFFQUpT)

### Meeting Info

**Agenda**: https://github.com/ethereum/pm/issues/971

**Date & Time**: [Mar 6, 2024, 14:00-15:00 UTC](https://www.timeanddate.com/worldclock/converter.html?iso=20240306T140000&p1=1440&p2=37&p3=136&p4=237&p5=923&p6=204&p7=671&p8=16&p9=41&p10=107&p11=28)

**Recording**: 


# Light Clients Breakout Room Meeting notes

Reference Issue: https://github.com/ethereum/pm/issues/971

The session was initiated to discuss a potential roadmap for Ethereum Light Clients, with a [document prepared by Etan](https://hackmd.io/@etan-status/electra-lc) serving as the foundation for the discussion. The document outlines a series of proposed changes aimed at addressing current limitations and enhancing the functionality of light clients within the Ethereum ecosystem. We start with use cases from potential builders/users of the light client protocol.

## Use Case: Portal Network

- **Decentralized Data Verification**: The Portal Network operates on a principle where all clients are equal and potentially store any data. The ability to easily prove the canonical status of light client data is crucial in this environment. Unlike traditional P2P networks with distinct client-server roles, the Portal Network requires mechanisms to ensure data integrity and canonical status without centralized authority.
- **Storing Historical Light Client Data**: Portal Network aims to store historical light client data and updates, necessitating proofs that these updates are both valid (canonical) and optimal (the best update available). This requirement stems from the network's decentralized nature, where data must be verifiable independently by any node.
- **Initial Use Case** - Chain Synchronization: The primary use case is enabling clients to follow the head of the chain by obtaining data from the Portal Network, similar to what is possible with the libp2p version. However, due to the lack of a centralized server, clients must be able to prove parts of the data independently. This capability is especially important for syncing data from before the client's initial sync timestamp.
- **Beyond Synchronization**: While chain synchronization is the initial focus, the ability to verify historical data independently has broader applications, such as in scenarios requiring token distributions or other proofs based on historical states.


## Use Case: IoT and Mobile Devices
Community builder Mihir aims to develop a client capable of syncing with the beacon chain through P2P, specifically for verifying sync aggregate updates. The ultimate goal is to enable consensus verification on resource-constrained devices like IoT devices and mobile phones without relying on centralized servers.

- **Limited libp2p Support**: The current ecosystem has limited support for serving light-client data via libP2P, with only Nimbus and Lodestar actively supporting it. There's a need for broader implementation across major clients like Lighthouse and Prysm to enhance discovery time and overall network efficiency. Note: Lighthouse is in-progress of implementing.
- **Network Dynamics and Light Client Status**: The discussion touches on the network dynamics concerning light clients, particularly their status and ability to maintain long-lived connections. The concern is that without being full peers, light clients may face disconnection issues, leading to outdated sync checkpoints upon reconnection.
- **Advocating for Backfill Protocol**: A reliable backfill protocol is proposed as a solution, especially for devices that aren't always online. This protocol would allow devices to efficiently resync with the network after being offline for extended periods without overburdening full nodes.
- **Syncing After Offline Periods**: The conversation explored whether a forward fill approach could offer the same security and ease as backfill for devices returning online after breaks.
- **Reliance on Checkpoints**: A critical point of discussion is the reliance on checkpoints for syncing and the inherent trust assumptions. The push for backfill is partly to mitigate blind trust in provided checkpoints.
- **Future Protocol Changes**: The dialogue also covers potential future changes to the protocol, such as the removal of sync committees in favor of single-slot finality. This raises questions about the adaptability of applications currently relying on sync committees and the need for clear upgrade paths.

## Use Case: Decentralized Staking Pools
Decentralized staking pools, like Rocket Pool, require the ability to detect when a validator is slashed. This involves creating proofs from the beacon state to verify such events. However, the current process is not straightforward due to the lack of a precompile and the dynamic nature of the beacon state's structure, which can change and necessitate updates to the verifiers.

## Protocol Concerns
### Centralization Concerns and Current Limitations

- A primary concern highlighted is the significant reliance on centralized servers for Ethereum interactions, such as querying balances or submitting transactions through services like MetaMask. This centralization poses risks and limitations, as it requires trust in these servers to provide accurate and honest responses

  - Currently, you need to download all the transactions in the block and process them and then all the receipts makes it quite tedious and it's not just for wallets it's also for say smart contracts
  - There is not even a transaction ID on the chain right now
  - There is no commitment to these on chain
 
- Etan emphasized the importance of distinguishing between execution and consensus layers. Execution APIs, often accessed via JSON RPC by users, have different considerations compared to consensus, which is more relevant to node operators.

- **Decentralized JSON RPC**: Highlighting efforts like HOPR (https://hoprnet.org) to create a decentralized JSON RPC, Etan pointed out the privacy and security benefits of such an approach. Currently, using services like MetaMask involves sending user addresses to a central server, potentially compromising privacy. The proposed changes would allow for correctness proofs in all responses, enabling users to query any server in a decentralized network without having to trust a specific server. This would enhance privacy by preventing correlation of requests and ensuring servers cannot provide false information about balances or transactions.
  - Decentralization might introduce higher latency compared to dedicated servers, but it's deemed crucial for those valuing decentralization to have the option to operate in a decentralized manner.
- **SnapSync Justification**: The necessity of SnapSync for the beacon state was questioned, given the current size of the beacon state (about 100-200 MB). Etan clarified that despite the small data size, the current process requires relying on centralized servers for checkpoint states and trusted state roots. For consensus, the goal is to remove the centralized server for the state. **We should strive to sync a beacon node without relying on a centralized checkpoint.**
  - SnapSync for execution, allows for requesting specific data ranges from peers, enabling the construction of a partial tree with the necessary proofs for verification. This method is seen as a potential way to currently access and verify only the portions of the state that are relevant to the user, even within the current Merkle tree structure.
- **Need for Historical Accumulators**: The discussion highlights the absence of a mechanism to indicate which sync aggregate was the best at a given period. The proposal includes adding a historical accumulator for light client data to address this gap, enabling proofs of canonical history without requiring the entire history of sync aggregates and associated proofs.

### Security Concerns

- The security of execution is tied to the engine_forkchoiceUpdated (FCU) verification and the validation of snap data against a specific root. The question raised is whether the proposed changes genuinely enhance security beyond the current capabilities.
- Consensus bootstrapping problem: Syncing new node requires you to go to a random website and just download the finalized state from there, hoping it's it's actually canonical.
  - It's possible to verify manually, but most people don't do it. Bad UX. We should aim for something like Snap sync on execution, but for the beacon state.

### Challenges in Proving LC Data Validity

- Proving that a piece of data is part of the canonical chain, especially for historical data, is identified as a complex process. It involves providing all sync aggregates from all blocks, proofs of their inclusion, and evidence that these blocks are part of the canonical history. Additionally, proving historical checkpoints requires knowing the exact time a block within a period was finalized, which affects the immutability of the subsequent sync committee.
- **Exploration for Simplicity**: The participants acknowledge the complexity involved in constructing proofs for the best update in a past period. There's an open invitation for anyone to propose simpler methods for achieving this goal. The complexity arises from the need to not only prove the canonical status of data but also to identify the most relevant or "best" update within a specific period.
- **Exploration of Practical Applications**: The discussion ends with a request for clarification on how proving the best update in a past period could be useful and what specific use cases it might enable. There's an expressed need to understand the practical applications of such proofs and how they contribute to the overall goals of decentralization, security, and efficiency within the Ethereum ecosystem.

### Execution Layer State Verification
Verifying the execution layer state, like the balance of a smart contract, is not straightforward due to misalignment between the roots of transactions, receipts, and the beacon block header. Currently, to verify transactions and receipts, one must obtain the execution block header separately, which involves interacting with a different network (DevP2P) and dealing with different encoding standards.

## Proposed Solutions Discussed
### [Light Client Backfill](https://hackmd.io/@etan-status/electra-lc#Light-client-data-backfill)

Open PR: https://github.com/ethereum/consensus-specs/pull/3614

- A significant part of the discussion focuses on the backfill capability and the inclusion of sync aggregate in the beacon state. The backfill feature would allow servers to request historical data from the network, ensuring that the data is canonical and not from a malicious chain. This is crucial for servers to serve clients on outdated checkpoints without the current period updates. See proposal to add LC endpoints to Checkpointz, already used to serve trusted checkpoints by diverse providers: https://github.com/ethpandaops/checkpointz/issues/143
- The proposal is seen as beneficial for maintaining network health by enabling clients on outdated checkpoints to sync, even if the server lacks intermediate data. This approach enhances the network's robustness and ensures continuity in data availability.


### Proposal for SSZ Stable Containers
**EIP-7495**: https://eips.ethereum.org/EIPS/eip-7495

Stable Container Concept: The proposal introduces the concept of SSZ Stable Containers to create a more stable structure for certain data within the beacon state, such as the needs discussed for decentralized staking pools. This stability would allow for the creation of verifiers (in smart contracts or on devices like hardware wallets) that do not require frequent updates, even when the beacon state evolves.

- **Consensus and Execution Changes**: Implementing SSZ Stable Containers would affect both consensus and execution layers, marking it as one of the few changes that would necessitate adjustments in these areas. The proposal is seen as apt and necessary for advancing light client use cases and improving the ecosystem's overall functionality.
- **EIP-7495 and Review Process**: The proposal is encapsulated in EIP-7495 but lacks extensive reviews. While the idea is stable and known to work, there's a possibility that further reviews could lead to breaking changes before finalizing the EIP. The need for more in-depth review by experts in SSZ is highlighted to ensure the proposal's viability and effectiveness.
- **Advocacy and Examination**: To advance the proposal, there's a suggestion to present it more broadly to garner attention and feedback from the right experts. This approach aims to champion the proposal through increased visibility and expert review, ensuring it is thoroughly vetted and considered for inclusion in future updates like Electra.

### Sync Committee Slashing
Open PR: https://github.com/ethereum/consensus-specs/issues/3321

- **Implementation Challenges**: Implementing sync committee slashing is deemed technically feasible but complex. The discussion reflects on research conducted a year ago, indicating that while possible, the utility of implementing such a mechanism remains questionable.
- **Limited Impact on Security**: The sync committee consists of 512 validators, and even perfect detection and slashing of all offending validators would result in a relatively modest total penalty (approximately 16,000 ETH, valued around $60 million at the time of discussion). This amount is considered insufficient to deter attacks on bridges that secure billions in assets, highlighting a significant security threshold issue for certain applications.
- **Bribery and Conspiracy**: A theoretical attack scenario is outlined where an adversary could potentially bribe a majority of the sync committee members to compromise a bridge. The sheer effort required to coordinate and compromise a supermajority of the sync committee makes this scenario highly theoretical and unlikely, even if the potential profit is much greater than the cost of attack.
- **Additional Stake and Operator Restrictions**: To enhance security, it's suggested that bridges or similar applications should not rely solely on light client sync for protection. Instead, requiring operators to put additional stake and restricting update submissions to those operators could provide a more robust security model without the need for slashing.
- **Future LC Protocol Dev Impacts via Single-Slot Finality and Max Effective Balance**: The discussion acknowledges that single-slot finality, which could potentially obviate the need for a sync committee, is not imminent. Additionally, the concept of Max Effective Balance (MaxEB) and its potential to impose restrictions on sync committee composition based on validators' stakes is mentioned as an area that hadn't been fully considered at the time of the initial research. However, we could improve on MaxEB with sync committee slashing by weighing in the security from the bundled security there.

### Roots Alignment
EIPs for Alignment: Adoption of specific Ethereum Improvement Proposals:

- [EIP-6493: SSZ Transaction Signature Scheme](https://eips.ethereum.org/EIPS/eip-6493)
- [EIP-6404: SSZ Transactions Root](https://eips.ethereum.org/EIPS/eip-6404)
- [EIP-6465: SSZ Withdrawals Root](https://eips.ethereum.org/EIPS/eip-6465)
- [EIP-6466: SSZ Receipts Root](https://eips.ethereum.org/EIPS/eip-6466)

could align the roots, eliminating the need to download the execution block header separately. This alignment would simplify the verification process by ensuring the consensus data matches the execution data.

## Next Steps
At a minimum, protocol devs who participated on the Light Client breakout call are advocating for some coordinated protocol changes needed to make the light client protocol viable for identified use cases. At a minimum, it would be good to consider:

- Backfill extension for the BeaconState
- Implementing SSZ StableContainer

