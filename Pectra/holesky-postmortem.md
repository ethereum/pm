# [Active] Holesky Pectra Incident Post-Mortem

Author: Tim Beiko 

Status: Active

Date: Feb 27, 2025, 19:00 UTC

# Current Status and Next Steps

Client teams are still trying to recover the Holesky network. 

## Holesky Coordinated Slashings

On [ACDE#206](https://github.com/ethereum/pm/issues/1306), client teams decided to try and coordinate mass Holesky slashings around slot `3737760` (Feb 28, 15:12:00 UTC). Ideally, the nework would have enough validators online to finalize an epoch on the valid chain at the same time. If successful, this will help clients sync to the minority chain. While all slashings and exits will still need to be processed, and Holesky is expected to go through other longs period of non-finality, a finalized epoch will make it easier to peer with nodes on the valid chain. 

Holesky operators should now:

1. Update their clients to the versions listed below
2. Sync their validators to the head of the chain
3. Be ready to disable slashing protection by slot `3737760` (Feb 28, 15:12:00 UTC)

Instructions to disable slashing protection for each client can be found below. A call will be hosted from 15:00-16:00 UTC for client teams and node operators to coordinate on this: https://github.com/ethereum/pm/issues/1337

### Disabling Slashing Protection 

Instructions for how to disable slashing protection per client. 

**Grandine**

TBA

**Lodestar**
1. Stop validator client
2. `rm -r <dataDir>/validator-db`
3. Start validator client

**Lighthouse**

See https://github.com/sigp/lighthouse/issues/7040

**Nimbus**

TBA

**Prysm**

Add the following CLI argument to the validator client **and NOT to the beacon node** and restart the validator client **and NOT the beacon node**: `--force-clear-db`

**Teku** 

TBA

**Web3Signer**

See https://docs.web3signer.consensys.io/concepts/slashing-protection

## Client Releases and Resources

Updates to releases listed in the original [Pectra testnet announcement](https://blog.ethereum.org/2025/02/14/pectra-testnet-announcement)

**Execution Layer Released Fixes:**
- Geth:  [v1.15.3](https://github.com/ethereum/go-ethereum/releases/tag/v1.15.3)
- Nethermind: [v1.31.1](https://github.com/NethermindEth/nethermind/releases/tag/1.31.1)
- Besu: [25.2.1](https://github.com/hyperledger/besu/releases/tag/25.2.1)
- Reth and Erigon: *No update needed (correctly handled the deposit contract)*

**Consensus Layer Fixes:**

Consensus layer teams have been putting out patches to improve peering and sync on branches and docker releases. The following information is accurate as of 19:00 UTC on Feb. 27. This [HackMD document](https://hackmd.io/@_iAz6KERTsWIHHNF-wMxAA/r1XlYyickx#CL-docker-tags) may have more recent information. 

- Lighthouse branch: [`holesky-rescue`](https://github.com/sigp/lighthouse/tree/holesky-rescue)
- Lodestar:
    - Branch: [`holesky-rescue`](https://github.com/ChainSafe/lodestar/tree/holesky-rescue)
    - Docker image: `ethpandaops/lodestar:holesky-rescue-5cb590f`
- Prysm branch: [`hackSync`](https://github.com/prysmaticlabs/prysm/tree/hackSync)
- Nimbus branch: [`splitview`](https://github.com/status-im/nimbus-eth2/tree/feat/splitview) 
- Grandine branch: [`holesky-recover`](https://github.com/grandinetech/grandine/tree/holesky-recover) 

**Useful Resources:**
- [ENR and enode list for correct chain](https://hackmd.io/@_iAz6KERTsWIHHNF-wMxAA/r1XlYyickx)
- [Block verification script](https://gist.github.com/samcm/e2da294dab77e93ad0ee0e815580294f)
- [Validator status tracking](https://hackmd.io/zu-FVVBSQr-GPdfh4UUIdQ)
- [Holesky block explorer (correct chain)](https://dora-holesky.pk910.de/)
- [Nethermind snapshot](https://nethermind.benaadams.vip/snapshot/nethermind_holesky_3420120_0x204dda_8f25ea_snapshot.tar.bz2)
- [EthPandaOps snapshots](https://ethpandaops.io/data/snapshots/)
- [Incident Debrief call notes](https://ethereum-magicians.org/t/holesky-incident-debrief-february-26-2025/22998)

# Root Cause Analysis

## Execution Layer Issue 

The root cause of the initial problem was that several execution clients (Geth, Nethermind, and Besu) had incorrect deposit contract addresses configured for the Holesky testnet. Specifically:

- Holesky's deposit contract address should be `0x4242424242424242424242424242424242424242`
- Some EL clients were using the mainnet deposit contract address or had no specific configuration for Holesky, leading them to use `0x0000...0000` 

When a block containing a deposit transaction was proposed at slot 3711006 (block 3419724), these clients processed it with an empty requests list, resulting in an incorrect requests hash. This caused a network split where:

- Erigon and Reth correctly rejected the invalid block
- Geth, Nethermind, and Besu accepted the invalid block

The deposit transaction in question can be found at: [https://holesky.etherscan.io/tx/0x48d5201b36db1122ce4d67367d03ad97d7c2e5b497c324843496230859be1bc7/advanced#eventlog](https://holesky.etherscan.io/tx/0x48d5201b36db1122ce4d67367d03ad97d7c2e5b497c324843496230859be1bc7/advanced#eventlog)

## Consensus Layer Issue

Once the network split occurred, a secondary issue emerged: consensus clients had difficulty syncing to the correct chain. This was due to:

1. The majority of nodes following the invalid chain
2. The invalid chain reaching justified status (though not finalized) in epoch 115968, making it the dominant chain
3. Consensus clients entering "syncing" mode when they couldn't find enough peers on the valid chain
4. Validators not producing blocks while their beacon nodes were in "syncing" mode
5. Slashing protection preventing validators from attesting to the correct chain after having attested to the invalid chain

The justification of the invalid chain created a particularly challenging situation. This justification meant that validators who had attested to the justified checkpoint on the invalid chain would face "surround" slashing conditions if they tried to attest to the correct chain.

This created a negative feedback loop where the valid chain had few blocks and few peers, making it increasingly difficult for nodes to sync to it. The situation was made worse because consensus clients are designed to follow the chain with the most attestation weight, which in this case was the invalid chain.

# Root Cause Remediations

_Note: this is a rough first draft, more to come later._

## User-specified Unfinalized Checkpoint Sync 

Allow CL clients to pick an arbitrary block from which to inialize checkpoint sync, even if not finalized. This would allow users to socially coordinate around a specific chain, forcing the client to sync to it. To be discussed further on March 6's ACDC call. 

## Validate EL fork parameterization 

Implement a form of validation for EL parameters introduced or changed in a network upgrade, either statically or as part of the peer-to-peer protocol. A telegram group has been created to discuss the issue: https://t.me/+d8rLI1WcaY41MmY5 

# Timeline of Events

_Note: I used an LLM to compile this based on the Discord chat transcript. I've sanity checked most of it, but there may be slight inaccuracies._

## February 24, 2025

### 22:04-23:00 UTC: Network Split Identified 
- 22:04: Multiple users report invalid block issues on the Holesky network after the Pectra upgrade
- 22:05: First reports of validation errors in Lighthouse:
  > "Invalid execution payload... validation_error: mismatched block requests hash: got 0x12e7307cb8a29c779310bea59482500fb917e433f6849de7394f9e2f5c34bf31, expected 0xe3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
- 22:07: Confirmation that Erigon is also seeing invalid blocks: "we have bad blocks on erigon too"
- 22:13: Lodestar reports similar errors with invalid blocks
- 22:19: Initial investigation reveals that some execution clients have the wrong deposit contract address
- 22:30: Teams identify that Erigon and Reth correctly rejected the invalid blocks, while Geth, Nethermind, and Besu accepted them
- 22:44: Confirmation that the issue is related to block 3419724 with hash `0x40a656c88b9ceb7d6251adc8819228a98ae26511faa246cb88004ca402a9f642`
- 22:47: somnergy (Erigon) explains: "Erigon received a header which suggests empty requests hash, but erigon found one or more requests while processing the block"

### 23:00-23:59 UTC: EL Root Cause Identification + Fix
- 23:10: Marius van der Wijden shares the parsed deposit request data from the problematic block
- 23:14: Marek (Nethermind) suggests: "to all EL clients, check your configuration for depositContractAddress"
- 23:19: Teams confirm the correct deposit contract addresses:
  - Holesky: `0x4242424242424242424242424242424242424242`
  - Sepolia: `0x7f02c3e3c98b133055b8b348b2ac625669ed295d`
- 23:23: Geth PR created: [ethereum/go-ethereum#31247](https://github.com/ethereum/go-ethereum/pull/31247)
- 23:23: Nethermind PR created: [NethermindEth/nethermind#8265](https://github.com/NethermindEth/nethermind/pull/8265)
- 23:28: Besu PR opened: [hyperledger/besu#8346](https://github.com/hyperledger/besu/pull/8346)
- 23:29: EthereumJS PR opened: [ethereumjs/ethereumjs-monorepo#3882](https://github.com/ethereumjs/ethereumjs-monorepo/pull/3882)
- 23:38: Ryan Schneider notes: "Everyone check Sepolia while we're looking 🙂"

## February 25, 2025

### 00:00-03:00 UTC: Early Sync Recovery Attempts 
- 00:26: First reports of Lighthouse nodes successfully syncing to the correct chain
- 00:31: First attempt to use `debug_setHead(0x342e4b)` (block 3419723) to reset Besu nodes:
  ```
  curl -X POST --data '{"jsonrpc":"2.0","method":"debug_setHead","params":["0x342e4b", true],"id":1}' http://127.0.0.1:8545/ -H "Content-Type: application/json"
  ```
- 00:41: Nethermind releases version 1.31.1 with the fix: [Nethermind v1.31.1](https://github.com/NethermindEth/nethermind/releases/tag/1.31.1)
  > "We changed a default sync method from snap to full sync with pruning enabled so it will catch up from genesis to a proper fork."
- 01:12: Besu releases version 25.2.1 with the fix: [Besu 25.2.1](https://github.com/hyperledger/besu/releases/tag/25.2.1)
- 01:16: First successful block production on the correct chain
- 01:22: Kamil (Nethermind) reports: "We just reorged to this block!" showing progress on the correct chain
- 02:00: Confirmation of more blocks being produced on the correct chain

### 03:00-06:00 UTC: Chain Stabilization Begins 
- 03:34: First reports of Reth validators successfully syncing to the correct chain
- 03:36: Confirmation that the latest block on the correct chain is at slot 3715626 with block root `0xe2975407c4d0a06671dfbdfd7b4eaf168d49009b78178e99a44f5d0ae104215e`
- 03:48: Discussion about the difficulty of finding peers on the correct chain
- 04:02: Checkpoint sync URL for the correct chain shared: [https://checkpoint-sync.holesky.ethpandaops.io/](https://checkpoint-sync.holesky.ethpandaops.io/)
- 04:13: ENR list for correct chain nodes created and shared at [https://hackmd.io/@_iAz6KERTsWIHHNF-wMxAA/r1XlYyickx](https://hackmd.io/@_iAz6KERTsWIHHNF-wMxAA/r1XlYyickx)
- 05:38: First Nethermind snapshot for the correct chain created
- 05:44: Ben Adams confirms successful sync: "Synced Chain Head to 3420047 (0xdd482e...08c37a) 🥳"

### 06:00-12:00 UTC: Coordination and Strategy Development 
- 06:29: Discussion begins about the long-term recovery strategy and memory usage concerns
- 06:56: Sam from EthPandaOps shares a script to verify if a node is on the correct fork: [https://gist.github.com/samcm/e2da294dab77e93ad0ee0e815580294f](https://gist.github.com/samcm/e2da294dab77e93ad0ee0e815580294f)
- 07:32: Dora block explorer begins to show the correct chain at [https://dora-holesky.pk910.de/](https://dora-holesky.pk910.de/)
- 07:50: EthPandaOps snapshots made available: [https://ethpandaops.io/data/snapshots/](https://ethpandaops.io/data/snapshots/)
- 08:17: EthPandaOps creates Docker images for patched clients:
  - Lighthouse: `ethpandaops/lighthouse:michaelsproul-disable-attesting-279afb0`
  - Prysm: `ethpandaops/prysm-beacon-chain:holesky-blacklist`
- 09:29: Confirmation that all teams are seeing the same canonical chain
- 10:22: Ben Adams shares Nethermind snapshot: [https://nethermind.benaadams.vip/snapshot/nethermind_holesky_3420120_0x204dda_8f25ea_snapshot.tar.bz2](https://nethermind.benaadams.vip/snapshot/nethermind_holesky_3420120_0x204dda_8f25ea_snapshot.tar.bz2)
- 10:40: Discussions about whether to proceed with Sepolia fork as scheduled
- 11:16: Lodestar team releases `ethpandaops/lodestar:holesky-rescue-1f257bb`

### 18:00-24:00 UTC:  Increased Validator Participation 
- 18:03: Prysm validators begin producing blocks on the correct chain
- 18:04: Dora block explorer updated to blacklist the bad chain:
  > "I've added a root blacklist to dora too, so the bad chain shouldn't be displayed as the canonical one anymore."
- 19:26: Teku team begins syncing their validator nodes:
  > "We have finally sync'd up one of our validator nodes. I am in the process of replicating its db to other nodes. We should have our 100k validators up and running in the next hour! 🚀"
- 20:04: Besu validators (20K) come online with Prysm
- 21:21: Script created to track block production by client: [https://gist.github.com/fab-10/3bf1cfc8c905b2059762aa5d5f669702](https://gist.github.com/fab-10/3bf1cfc8c905b2059762aa5d5f669702)
- 21:34: Fab_10 shares a script to see who is proposing blocks:
  ```
  ./block-graffiti.sh 100
  3717953 [Besu 🐐 Lighthouse]
  3717901 [Besu 🐐 Lighthouse]
  3717885 [¤ Frax Finance ¤]
  3717882 [🚀 xrchz 🐟 💰 ❓]
  3717867 [Besu 🐐 Lighthouse]
  3717862 [Besu 🐐 Lighthouse]
  ```
- 22:36: Nethermind produces multiple blocks in succession:
  > "Nethermind proposes blocks! ❤️"
- 23:36: Attestant validators begin getting slashed due to double voting

## February 26, 2025

### 00:00-06:00 UTC: Increased Validator Participation 
- 00:15: Jim (Attestant) shares modified Vouch client: `attestant/vouch:unsynced`
- 02:15: Jimmy Chen clarifies the purpose of Lighthouse's `disable-attesting` flag:
  > "`disable-attesting` is mainly used to avoid flooding the BN so it can sync without struggling with attestation requests."
- 02:42: Prysm team confirms their validators are online
- 03:14: Obol team brings 10K validator cluster online
- 03:48: Chainsafe confirms all 100K Lodestar keys are proposing blocks
- 04:56: EF DevOps brings all 40K validators online
- 05:42: Nimbus team shares instructions for removing slashing protection:
  > "for nimbus-eth2, it's `<dataDir>/db/slashing_protection.sqlite3`. also restart the beacon node so that it forgets about the fake-valid engine response from the broken EL versions."

### 06:00-14:30 UTC: Strategy Refinement 
- 07:46: Discussion about how to disable slashing protection for each client
- 08:24: Grandine team shares instructions: "For Grandine you need to remove slashing protection DB by running `rm ~/.grandine/holesky/validator/slashing_protection*`"
- 09:54: Confirmation that approximately 5-8 blocks per epoch are being produced (15-25% of target)
- 10:22: Nethermind snapshot shared at block 3420120
- 10:40: Besu team brings another 40K validators online
- 11:27: Confirmation that ~15K Nethermind validators have been slashed
- 11:50: Potuz emphasizes: "we need the blocks much more than the attestations, I thought we had clearly agreed to stabilize the chain before attesting. Any attestation takes out all the blocks from that validator that could support the chain"
- 12:01: Potuz provides clear recovery strategy:
  > "The summary is very simple:
  > 	1. Sync nodes
  > 	2. Enable validators
  > 	3. Do not remove slashing db
  > 	That's it."
- 12:34: Potuz provides detailed explanation for the strategy:
  > "Nodes run more smoothly when there are blocks in the chain, when a block is not there we start hitting cache misses and need to start applying heuristics because the block may have been there and we didn't see it. The chain can pack more attestations when there are more blocks in the chain and thus be less forked. Syncing nodes receive more regular updates of their status when there are more blocks in the chain..."
- 12:52: Paul Harris reports: "We've at least got one of our teku / besu nodes up with 20k keys - all will surround so no attestations, but producing blocks."
- 13:07: Kamil (Nethermind) reports: "Nethermind slashed 13337 validators so far based on Dora and seems like it is slowing down? Still 80-90% of ours slots are proposing blocks well"
- 13:16: Grandine team reports successful recovery with Nethermind
- 14:00: [Holesky Incident Debrief call takes place](https://ethereum-magicians.org/t/holesky-incident-debrief-february-26-2025/22998
- 14:29: Marek (Nethermind) creates Hackmd document to track validator status: [https://hackmd.io/zu-FVVBSQr-GPdfh4UUIdQ](https://hackmd.io/zu-FVVBSQr-GPdfh4UUIdQ)

### 14:30 UTC - cont'd: Network Health Improvement
- 15:43: Terence reports significant improvement: "I'm actually syncing really smoothly on my local node now, everything from scratch (geth - prysm). Following blocks from 6 hours ago. Having Dora alive makes this really easy. I'm impressed how much more smoother everything is today comparing to yesterday"
- 17:33: Discussion about long-term recovery plan, estimating 18 days until finalization
- 19:09: Marius estimates Holesky is getting 10% attestations participation and 30-50% of scheduled block proposals. 

