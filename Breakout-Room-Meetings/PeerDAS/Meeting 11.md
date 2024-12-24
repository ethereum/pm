
# PeerDAS Breakout Room #11
Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit#heading=h.tubwqb51zcjq)

## Meeting info

Date: 2024.10.29
Agenda: https://github.com/ethereum/pm/issues/1183
YouTube video: https://youtu.be/QBNPQhDYgcY

### Client updates
**Lighthouse**
- Refactoring sync logic

**Teku**

- Working on Pectra rebase
- Working on retrieving data columns from DB and validating (?)

**Nimbus**
- `csc` not populating after beacon node restart on devnet-3
- Had some issues with reconstructed columns - published columns that potentially caused some issues on the network (prysm & lodestar seem to be fine)
- Experiment on column syncing + reconstruction with supernodes 
- Planning to activate PeerDAS at Fulu
- Fulu consensus-spec PR: https://github.com/ethereum/consensus-specs/pull/3994 

**Prysm**

- Worked on optimisation on column verification
- Prysm can sync large amount of columns in seconds now 
- A lot more work for Prysm to activate PeerDAS at Fulu

**Lodestar**
- Working on getBlobs

**Grandine**
- Fixing some req/resp issues

### Devnet updates

peerdas-devnet-3 died after a 100k 🤯 slot reorg. Will shutdown today

peerdas-devnet-4 spec: https://notes.ethereum.org/@ethpandaops/peerdas-devnet-4 

Plan to launch peerdas-devnet-4 end of Nov (as Devcon is approaching), with PeerDAS activation at Fulu

Will double check again at ACDC on whether to activate PeerDAS at Fulu	

### Spec discussions

EIP-7742: discussion on how we activate this
- Discussed on Discord, will not rename the current deneb configurations (MAX_BLOBS_PER_BLOCK) and will add prefixes for future configs changes

Decoupling subnet PR (https://github.com/ethereum/consensus-specs/pull/3832)
- Callout for more comments before merging.

Pop’s PR on standardize DAS data store (https://github.com/ethereum/consensus-specs/pull/3993)
- Client teams to provide feedback and continue discussion on the PR

### Open discussions

PeerDAS Metrics (https://github.com/ethereum/beacon-metrics/pull/14)
- Discussion on metrics unit: seconds vs milliseconds	
  - Prysm prefers more granularity and suggests to use milliseconds instead
- Metric “beacon_kzg_verification_data_column_single_seconds” vs “beacon_kzg_verification_data_column_batch_seconds”
  - Nimbus only uses batch verification
  - LH only uses batch verification method too, even on single column verification, however in this case the single verification metric is used - this can be fixed
  - Single verification has been removed from the library API and no longer available, so we can safely remove the metric

Discussion on “gossipsub_topic_msg_recv_counts_unfiltered_total” (https://github.com/ethereum/beacon-metrics/pull/13)

How do clients count this filtering? 
  - Some clients may have difficulty doing some of the libp2p metrics, as they are available in the lib2p library
 
IDONTWANT implementation status (context: https://ethresear.ch/t/number-duplicate-messages-in-ethereums-gossipsub-network/19921)
- Teku will have it in place after Pectra rebase
- Lighthouse has an optimised version merged to unstable, will be released in a few weeks


## Zoom Chat Links

https://github.com/ethereum/consensus-specs/pull/3994

https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit?tab=t.0

https://notes.ethereum.org/@ethpandaops/peerdas-devnet-4

https://github.com/status-im/nimbus-eth2/pull/6677

https://github.com/ethereum/consensus-specs/issues/3952

https://github.com/ethereum/consensus-specs/commit/ded072af400c53c9cd19cc426ff004b9db100bd2

https://github.com/ethereum/consensus-specs/pull/3817

https://github.com/ethereum/consensus-specs/pull/3993

https://github.com/ethereum/beacon-metrics/pull/14

https://github.com/KatyaRyazantseva/beacon-metrics/blob/master/metrics.md#gossipsub-metrics
