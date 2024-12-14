---
title: Meeting 10

---

# PeerDAS Breakout Room #10
Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit#heading=h.tubwqb51zcjq)

## Meeting info
Date: 2024.10.15
Agenda: https://github.com/ethereum/pm/issues/1179
YouTube video: https://youtu.be/o2hpnJBjSyw

## Notes
### Client updates
**Lighthouse**
- LH nodes have forked from the main fork on devnet-3, still investigating issue, seems to be related to lookup sync (DataColumnsByRoot)
- Working on getting `getBlobs` optimisation 

**Prysm**
- Had some sync issues on fullnodes
- Worked on some sync optimisation to reduce bandwidth
- Fixed a few sync issues and able to sync with other clients

**Lodestar**

- All lodestar nodes seems to be on the main fork
- Still debugging some sync issues, but restarted nodes were able to sync

**Grandine**

- Implemented reconstruction
- Had some issues with syncing to devnet-3, investigating

Most client teams seem to have some sync related issues and will continue to debug on peerdas-devnet-3

### Devnet updates

**Barnabas**: should we relaunch the devnet with supernodes only?
- Proposed by Francesco on discord as an intermediate step, as we’re having lots of issues on a small network with fullnodes
- Teams have been investigating issues and would like a week or two debug
- Teams are not sure if the issues are related to fullnodes/supernodes, but worth removing possibility of the fullnode issues
- Potentially consider more supernode validator weights in the next devnet launch

### Spec discussion

**Barnabas**: there was some Discord discussion on whether clients should verify KZG proofs on finalized epochs during sync.

- Spec PR raised https://github.com/ethereum/consensus-specs/pull/3963 
- Discussion thread: https://discord.com/channels/595666850260713488/1252403418941624532/1293879020651282442 
- This was raised because Prysm noticed that KZG verification during sync takes about 25s for 64 blocks, and wondered if we really need to verify KZG proofs for finalized blocks?
- Lighthouse also performs KZG proof verification on finalized blocks during sync 
- **George**: asked how Prysm is calling the library, is it batched?
  - Prysm currently verify block by block, could potentially batch more blocks 
- **Francesco**: node MUST verify proofs if it doesn’t have all the data to be certain that they’re valid
- Prysm: if the proof verification is batched, this could potentially cut the time down and will no longer be a problem
  - Verifying 1192 column proofs without batching => 40s
  - Verifying 1192 column proofs with batching => 3-4s
- **ACTION**: client teams to implement batching optimisation and raise if this this still an issue
 
PeerDAS Metrics (https://github.com/ethereum/beacon-metrics/pull/14)
- Katya has split the big PeerDAS metrics into parts as discussed in the last call
- She presented the PeerDAS Grafana dashboard, and can filter by node type, client, or instance
- These metrics are primarily for devs and not end users, so it would be more useful if they are implemented early
- Jimmy suggested if there are histogram metrics, we should have buckets included in the spec. Katya looked into this but ran into some issues in Teku.\
- LH has implemented some of these metrics with additional labels and found them useful (e.g. computation time labeled by blob count) , will suggest on the PR.
- Katya has another PR (https://github.com/ethereum/beacon-metrics/pull/13)  on the remaining network metrics and there are some more active discussions there.
- **ACTION**: client teams to review the DAS metrics (first PR), share comments in the next week and aim to have the 

DAS metrics PR merged soon
- Barnabas asked if any client team has started rebasing PeerDAS on Pectra
- No teams have done / tested this recently


Current state of pectra devnets?
- Pectra-3 is very stable and pectra-4 to be launched end of week
- Will wait until Pectra is stable before we rebase
- Reminder to fill out the PeerDAS contributor form: https://forms.gle/tt1L2QvSq3JnKPoW7

## Zoom chat links

https://github.com/ethereum/consensus-specs/pull/3963

https://discord.com/channels/595666850260713488/1252403418941624532/1293879020651282442

https://grafana.observability.ethpandaops.io/d/fdzvv4w0xe1hcd/peerdas-metrics-specs?orgId=1&refresh=5s&var-network=peerdas-devnet-3&var-nodes=All&var-consensus_client=All&var-instance=All&from=1728984668625&to=1728988268625

https://github.com/ethereum/beacon-metrics/pull/13

https://forms.gle/tt1L2QvSq3JnKPoW7