# Holešky Pectra Incident Post-Mortem

Author: Tim Beiko, Mario Havel

Status: Resolved

Date: Mar 20, 2025

# Current Status 

The Holešky network has been successfully recovered. After 2 weeks of running without finality, the chain finalized again on Mar 10 at 19:21 UTC at epoch `119090`.

The recovery was achieved by coordinating operators to follow the correct chain until participation reached enough validators for finality. Since then, participation has continued to slowly rise and the network appears stable. Detailed recovery efforts and original instructions for validators are described below.

After reaching finality, the consensus started processing validator events and the exit queue became full for the next ~1.5 years. Because of this, full validator lifecycle tests and other Electra testing like consolidations are not possible. Holešky long term support window was shortened and to allow for immediate testing, the network is replaced by [Hoodi](https://github.com/eth-clients/hoodi).

## Recovery Efforts

The initial strategy to coordinate slashing with operators disabling slashing protections, planned at [ACDE#206](https://github.com/ethereum/pm/issues/1306), was not successful. The outcome and new options were discussed at [ACDC#152](https://github.com/ethereum/pm/issues/1323). At that point, slashings and coordination of validators to follow the correct fork did not reach the necessary 66% threshold, and the network remained in a prolonged state of non-finalization. This scenario is one which consensus clients are not designed for and causes significant resource overhead. Client teams implemented fixes and mitigations allowing clients to run more efficiently even through extended periods of non-finalization.

After [ACDC#152](https://github.com/ethereum/pm/issues/1323), based on outlined strategies, PandaOps initiated another coordination effort to reach finality in the network, planned to take place until March 12. An [analysis](https://docs.google.com/spreadsheets/d/1nndNt-XC4JzqsjmCRuiXBGCGMFomCHx_e_DZzFqvhGM/edit?gid=373616122#gid=373616122) suggested that the network would eventually reach finality due to inactivity leak around March 28. However, this would result in losing significant time for testing Pectra, so the strategy aimed to try again before March 12. As an alternative, if this approach didn't succeed, a shadow fork of the last finalized state would be created as an alternative testing environment.

As participation slowly increased, the goal was to prompt as many validators as possible to connect to the correct network before Mar 12. This was successfully achieved on the evening of March 10. A [new finalized epoch](https://light-holesky.beaconcha.in/epoch/119090) of the correct chain was created, which could then be used by clients to sync normally again.

<details>
  <summary>Original Validator Instructions for recovery</summary>

Original instructions for Holešky validators to participate and contribute to the recovery:

- Update your clients to a version containing the fix, [list of versions below](#client-releases-and-resources)
- Disable slashing protection as [described below](#Disabling-Slashing-Protection)
- Instead of your own Beacon Node, connect to the [provided Beacon API](https://holesky-rescue.ethpandaops.io/) at https://holesky-rescue.ethpandaops.io/
    - If you have trouble finding peers or need another endpoint, check https://notes.ethereum.org/@ethpandaops/holesky-rescue-efforts-v2
- Reach out to PandaOps or your client team in R&D Discord in case of any issues following the correct chain

EL clients need to use full sync instead of snap sync. This should be the default configuration in releases containing fixes.

### Coordinated Slashings

On [ACDE#206](https://github.com/ethereum/pm/issues/1306), client teams decided to try and coordinate mass Holešky slashings around slot `3737760` (Feb 28, 15:12:00 UTC). The goal was for the network to achieve enough validators online to finalize an epoch on the valid chain at the same time.

### Disabling Slashing Protection 

Instructions for how to disable slashing protection per client:

**Grandine**

`rm ~/.grandine/holesky/validator/slashing_protection*`

**Lodestar**
1. Ensure that your configuration is NOT using doppelganger protection
2. Stop validator client
3. Remove slashing protection database by running `rm -r <dataDir>/validator-db`
4. Start validator client

**Lighthouse**

See https://github.com/sigp/lighthouse/issues/7040

**Nimbus**

`rm ~/.cache/nimbus/validators/slashing_protection.sqlite3`

Note that the exact path will depend on individual configurations. If the node has not cleanly shut down, users may also need to delete SQLite WAL files such as `slashing_protection.sqlite3-wal` and `slashing_protection.sqlite3-shm`.

**Prysm**

Add the following CLI argument to the validator client **and NOT to the beacon node** and restart the validator client **and NOT the beacon node**: `--force-clear-db`

**Teku**

1. Ensure that your configuration is not using doppelganger protection (`--doppelganger-detection-enabled`)
2. Stop Teku
3. Remove slashing protection files: `rm <teku_data_directory>/validator/slashprotection/*`
4. Start Teku

**Vouch/Dirk**

See https://github.com/attestantio/vouch/issues/304

**Web3Signer**

See https://docs.web3signer.consensys.io/concepts/slashing-protection

## Client Releases and Resources

Updates to releases listed in the original [Pectra testnet announcement](https://blog.ethereum.org/2025/02/14/pectra-testnet-announcement)

**Execution Layer Released Fixes:**
- Geth: [v1.15.3](https://github.com/ethereum/go-ethereum/releases/tag/v1.15.3) and subsequent releases
- Nethermind: [v1.31.1](https://github.com/NethermindEth/nethermind/releases/tag/1.31.1) and subsequent releases
- Besu: [25.2.1](https://github.com/hyperledger/besu/releases/tag/25.2.1) and subsequent releases
- Reth and Erigon: *No update needed (correctly handled the deposit contract)*

**Consensus Layer Fixes:**

Consensus layer teams have been releasing patches to improve peering and sync on branches and docker releases. The following information is accurate as of 19:00 UTC on Mar. 10. This [HackMD document](https://hackmd.io/@_iAz6KERTsWIHHNF-wMxAA/r1XlYyickx#CL-docker-tags) may have more recent information.

- Lighthouse
  - Branch: [`holesky-rescue`](https://github.com/sigp/lighthouse/tree/holesky-rescue)
  - Release: [Frankenstein's Monster](https://github.com/sigp/lighthouse/releases/tag/v7.0.0-beta.2)
  - Docker image: `sigmaprime/lighthouse:sigp-holesky-rescue-6399ad4`
- Lodestar:
    - Branch: [`holesky-rescue`](https://github.com/ChainSafe/lodestar/tree/holesky-rescue)
    - Release: [v1.27.1](https://github.com/ChainSafe/lodestar/releases/tag/v1.27.1)
    - Docker image: `ethpandaops/lodestar:holesky-rescue-43b5b91` 
- Prysm:
    - Branch: [`hackSync`](https://github.com/prysmaticlabs/prysm/tree/hackSync)
    - Docker image: `ethpandaops/prysm-beacon-chain:hackSync-a9dc6a1` 
- Nimbus
    - Branch: [`splitview`](https://github.com/status-im/nimbus-eth2/tree/feat/splitview) 
    - Docker image: `ethpandaops/nimbus-eth2/splitview-49a5263`
- Grandine 
     - Branch: [`holesky-recover`](https://github.com/grandinetech/grandine/tree/holesky-recover)
- Teku:
    - Branch: [`master`](https://github.com/Consensys/teku)
    - Docker image: `consensys/teku:develop`

**Useful Resources:**
- [ENR and enode list for correct chain](https://hackmd.io/@_iAz6KERTsWIHHNF-wMxAA/r1XlYyickx)
- [Block verification script](https://gist.github.com/samcm/e2da294dab77e93ad0ee0e815580294f)
- [Validator status tracking](https://hackmd.io/zu-FVVBSQr-GPdfh4UUIdQ)
- [Holesky block explorer (correct chain)](https://dora-holesky.pk910.de/)
- [Nethermind snapshot](https://nethermind.benaadams.vip/snapshot/nethermind_holesky_3420120_0x204dda_8f25ea_snapshot.tar.bz2)
- [EthPandaOps snapshots](https://ethpandaops.io/data/snapshots/)

</details>

## Postmortems from client teams
  - [Lodestar Holesky Rescue Retrospective](https://blog.chainsafe.io/lodestar-holesky-rescue-retrospective) 
  - [Besu Deposit Contract Address Postmortem](https://hackmd.io/@siladu/H1qydmWhyx)
  - [Prysm Postmortem](https://github.com/prysmaticlabs/documentation/pull/1028)
  - [Who Moved My Testnet? - Reflection on testnet situation by Lucas Saldanha](https://hackmd.io/@lucassaldanha/rJd-9rAikg)
  - [Original Incident Debrief call notes](https://ethereum-magicians.org/t/holesky-incident-debrief-february-26-2025/22998)

# Root Cause Analysis

## Execution Layer Issue 

The root cause of the initial problem was that several execution clients (Geth, Nethermind, and Besu) had incorrect deposit contract addresses configured for the Holešky testnet. Specifically:

- Holesky's deposit contract address should be `0x4242424242424242424242424242424242424242`
- Some EL clients were using the mainnet deposit contract address or had no specific configuration for Holesky, leading them to use `0x0000...0000` 

When a block containing a deposit transaction was proposed at slot 3711006 (block 3419724), these clients processed it with an empty requests list, resulting in an incorrect requests hash. This caused a network split where:

- Erigon and Reth correctly rejected the invalid block
- Geth, Nethermind, and Besu accepted the invalid block

The deposit transaction in question can be found at: [https://holesky.etherscan.io/tx/0x48d5201b36db1122ce4d67367d03ad97d7c2e5b497c324843496230859be1bc7/advanced#eventlog](https://holesky.etherscan.io/tx/0x48d5201b36db1122ce4d67367d03ad97d7c2e5b497c324843496230859be1bc7/advanced#eventlog)

Previous Pectra activations on devnets and Ephemery did not trigger this issue because those networks operate with manually initialized genesis.

## Consensus Layer Issue

Once the network split occurred, a secondary issue emerged: consensus clients had difficulty syncing to the correct chain. This was due to:

1. The majority of nodes following the invalid chain
2. The invalid chain reaching justified status (though not finalized) in epoch 115968, making it the dominant chain
3. Consensus clients entering "syncing" mode when they couldn't find enough peers on the valid chain
4. Validators not producing blocks while their beacon nodes were in "syncing" mode
5. Slashing protection preventing validators from attesting to the correct chain after having attested to the invalid chain

The justification of the invalid chain created a particularly challenging situation. This justification meant that validators who had attested to the justified checkpoint on the invalid chain would face "surround" slashing conditions if they tried to attest to the correct chain.

This created a negative feedback loop where the valid chain had few blocks and few peers, making it increasingly difficult for nodes to sync to it. The situation was exacerbated because consensus clients are designed to follow the chain with the most attestation weight, which in this case was the invalid chain.

# Root Cause Remediations

## Validating Configuration and Fork Parameterization 

Better validation of config and fork paramaters is necessary, also genesis configuration is being standardized across clients. EL clients are implementing a new RPC method enabling to retrieve and validate the correct configuration. [eth_config](https://hackmd.io/@shemnon/eth_config). Incompatible configuration results in an early error. 

## User-specified Unfinalized Checkpoint Sync 

Clients will enable custom checkpoint sync block and improve capabilities to sync even from an arbitrary non-finalized checkpoints. This would enable users to socially coordinate around a specific chain, forcing the client to sync to it.
Further improvement could be a leader-based coordination systems for correct chain identification and fix invalid chain pruning capabilities. 

> e.g. Prysm added "sync from head" feature ([PR #15000](https://github.com/prysmaticlabs/prysm/pull/15000), more planned [#14988](https://github.com/prysmaticlabs/prysm/issues/14988)), geth is working on similar featre [#31375](https://github.com/ethereum/go-ethereum/issues/31375), Teku consideres it but it's codebase heavily relies on a finalized source to start the sync

## Further issues and mitigations

Apart from the original root issue, the incident uncovered a number of other problems caused by the extreme case of a long non-finality, especially for CL clients. Clients implemented more fixes and improvements.

### Issues across consensus clients

#### High resource usage 

Most clients ended up with excessive memory usage and performance degradation as non-finality duration extended (for example Prysm/Geth machine with 300GB+ RAM usage). Without finalized checkpoint to write to the database, clients had to store a lot of data in memory.

#### Fork Choice issues

An incorrect chain with an invalid block being justified caused issues for fork choice. Clients had to handle many competing forks with correct one being a minority without justification.

#### Peer discovery and connection issues

All clients struggled to find peers on the correct chain, even with manual ENR sharing and coordination. Peer scoring and many concurrent forks made it difficult to find a good peer.

#### Slashing protection issues

Every client team needed custom procedures for managing slashing protection. Surround slashing conditions were a problem for validators that attested to the invalid chain.

### Client specific improvements

  - Lighthouse
    - Developing "hot tree-states" feature to store data in hot DB more efficiently during non-finality. Allows to store data in the hot DB in a disk similarly to the cold DB, without consuming an inordinate amount of disk space.
    - Added `lighthouse/add_peer` endpoint to help nodes find canonical chain peers, especially useful with `--disable-discovery`
    - Optimized `BlocksByRange` to load from fork choice when possible
    - Added `--invalid-block-roots` flag to automatically invalidate problematic blocks (like 2db899...)
    - Improved cache management and other optimizations
  - Prysm
    - Added a new flag to allow syncing from a custom checkpoint, [sync from head](https://github.com/prysmaticlabs/prysm/pull/15000)
    - Fixed bugs with attestation aggregation and attester slashing bug introduced in Electra [#15027](https://github.com/prysmaticlabs/prysm/pull/15027), [#15028](https://github.com/prysmaticlabs/prysm/pull/15028)
    - Fixed REST API performance issues with `GetDuties` endpoint [#14990](https://github.com/prysmaticlabs/prysm/pull/14990)
    - Plans more features for custom sync: [marking invalid blocks](https://github.com/prysmaticlabs/prysm/issues/14989), [optimistic sync option](https://github.com/prysmaticlabs/prysm/issues/14987), [adding blocks manually](https://github.com/prysmaticlabs/prysm/issues/14986), [follow chain by leader's ENR](https://github.com/prysmaticlabs/prysm/issues/14994)

  - Lodestar
    - Added feature to [check for blacklisted blocks](https://github.com/ChainSafe/lodestar/pull/7498) and introduced a [new endpoint](https://github.com/ChainSafe/lodestar/pull/7580) to return them
    - Fixed checkpoint state pruning to prevent OOM crashes [#7497](https://github.com/ChainSafe/lodestar/pull/7497), [#7505](https://github.com/ChainSafe/lodestar/pull/7505)
    - Added pruning of persisted checkpoint states [#7510](https://github.com/ChainSafe/lodestar/pull/7510), [#7495](https://github.com/ChainSafe/lodestar/issues/7495)
    - Added feature to use local state source as checkpoint [#7509](https://github.com/ChainSafe/lodestar/pull/7509)
    - Addded new endpoint `eth/v1/lodestar/persisted_checkpoint_state` to return a state based on an optional `rootHex:epoch` parameter [#7541](https://github.com/ChainSafe/lodestar/pull/7541)
    - Improved peer management during sync stalls, adding check whether peer is `starved` [#7508](https://github.com/ChainSafe/lodestar/pull/7508)
    - Fixed bug in attestationgossip validation introduced in Electra [#7543](https://github.com/ChainSafe/lodestar/pull/7543)
    - Considered adding pessimistic sync but might cause problems with snap synced EL and doesn't seem that useful [#7511](https://github.com/ChainSafe/lodestar/pull/7511)
    - Added state persistence for invalid blocks to allow their analysis [#7482](https://github.com/ChainSafe/lodestar/pull/7482)
    - Exploring binary diff states and era files to import state [#7535](https://github.com/ChainSafe/lodestar/pull/7535), [#7048](https://github.com/ChainSafe/lodestar/issues/7048)

  - Teku
    - Fixed fork choice bug related to equivocating votes [#9234](https://github.com/Consensys/teku/pull/9234)
    - Fixed sync issues during long non-finality, sync process to restarting from an old block because `protoArray` initialised with 0 weights and canonical head became a random chain tip in the past
    - Fixed node restarting sync from last finalized state
    - Fixed slow block production due to too many single attestations 
    - Added sorting for better attestation selection during aggregation
    - Identified and working on various smaller issues https://github.com/Consensys/teku/issues?q=%5BHOLESKY%20PECTRA%5D
    - To deal with huge performance overhead, team created a "superbeacon" node on a new machine with substantial CPU/RAM resources to handle the load

  - Nimbus
    - Didn't experience major issues with performance
    - Created branch `feat/splitview branch that keeps better track of forks
    - Even when block was was `INVALID`, it was added to fork choice and justified, creating a hard situation to recover from, due to the fundamentally optimistic nature of how the engine API works
    - While the `feat/splitview` branch was able to effectively find/explore lots of forks on from different nodes, it was unable to get ELs to often respond with anything but `SYNCING`, so couldn't rule out actually-`INVALID` forks
    - After the networking finalized, Nimbus took a while to finish some on-finalization processing it did and disrupted slot and block processing for a while. Once it got past that, it was fine, and `feat/splitview` wasn't necessary anymore

  - Grandine
    - Fixed increased memory usage that led to OOM errors

  - Besu
    - Fixed deposit contract address misconfiguration [#8346](https://github.com/hyperledger/besu/pull/8346)
    - Besu is using a 3rd party web3 library to process the deposit contract, team will review usage of external libraries in critical consensus paths [#8391](https://github.com/hyperledger/besu/issues/8391)
    - Fixed snap sync stalling [#8393](https://github.com/hyperledger/besu/issues/8393)
  
  - Geth
    - Fixed deposit contract address configuration [#31247](https://github.com/ethereum/go-ethereum/pull/31247)
    - Working on `--synctarget` flag to force client follow a specific chain [#31375](https://github.com/ethereum/go-ethereum/issues/31375)
    - Identified crashes when trying to add invalid block after syncing good branch [#31320](https://github.com/ethereum/go-ethereum/issues/31320)

### Testing and process improvements

#### More non-finality testing
Clients have not been tested under such long non-finality conditions before. Some period of non-finality should become a standard testing procedure.

#### Testnet and fork management**

Testnets and hardforks require more careful handling, Holesky/Sepolia/Hoodi should be considered a proper staging environments. Testnets setup should be close to mainnet as possible and hardfork activation should be handled similarly to mainnet with proper procedures. Some more insights on this topic can be found here: https://hackmd.io/@lucassaldanha/rJd-9rAikg

#### Incident response coordination

The process for incident response needs to be clear and executed across client teams. Especially during hardforks, whether testnet or mainnet,developers and devops need be on-call and actively monitoring the situation. Communication needs to be clear between clients, without teams working in isolation. A proper standard procedure for incident response needs to be established with clear guidelines and responsibilities.

#### Validator client separation

Modularity by using separate validator clients proved valuable, allowing teams to connect their validators to connect to healthy beacon nodes providers. Moving validator keys between clients can be challenging and time-consuming.

# Timeline of Events

_Note: I used an LLM to compile this based on the Discord chat transcript. I've sanity checked most of it, but there may be slight inaccuracies._

## February 24, 2025

### 22:04-23:00 UTC: Network Split Identified 
- 22:04: Multiple users report invalid block issues on the Holešky network after the Pectra upgrade
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

### 18:00-24:00 UTC: Increased Validator Participation 
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
- 15:43: Terence reports significant improvement: "I'm actually syncing really smoothly on my local node now, everything from scratch (geth - prysm). Following blocks from 6 hours ago. Having Dora alive makes this really easy. I'm impressed how much smoother everything is today compared to yesterday"
- 17:33: Discussion about long-term recovery plan, estimating 18 days until finalization
- 19:09: Marius estimates Holesky is getting 10% attestation participation and 30-50% of scheduled block proposals.

