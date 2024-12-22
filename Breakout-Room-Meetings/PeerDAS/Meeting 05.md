---
title: Meeting 05

---

# PeerDAS Breakout Room #5

Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit#heading=h.tubwqb51zcjq)

## Meeting info

Date: 2024.08.06

Agenda: https://github.com/ethereum/pm/issues/1114

YouTube Video: ​​https://www.youtube.com/watch?v=scOJSLiMFy4

## Notes

### Client updates
**Prysm**
- Fixed initial sync
- Implemented MetaDataV3 query, not yet merged
- Fixing BlobSidecar beacon API for PeerDAS

**Lighthouse**
- Fixed some networking issues and kzg library issues
- Focused on refactoring and merging PeerDAS changes to the main branch. About half way there, and will be focused on finishing it the next 1-2 weeks
- Disabled sampling by default and local network seems be a lot more stable

**Lodestar**

- Should be good to participate in devnet without sampling
- Question: are we going to include the data availability changes to fork choice?
  - not for the next (few) devnets

**Grandine**

- Made progress with some EPF participants
- Would like to hear about scope with sampling as well

**Teku**
- Implemented Lossy sampler, but difficult to test with local testnet. Currently just log results and not updating fork choice
- Implemented data column gossip validation

**Nimbus**
- Upstream c-kzg to latest
- Started Lossy sampling but not much progress recently
- Discovered some issues with spec-tests, will likely be fixed in 1.5.0-alpha-4
- 
### Devnet-2 spec

No active devnet testing

Features and dates for next devnet?
- **Gajinder**: Are we going to do sampling for the current slot? Is this how it would behave when we go live?
  - trailing fork choice was for sampling which may not be included
  - no change to fork choice if we exclude sampling

Are we excluding Sampling for next devnet or production?
- Francesco will refine and update the spec PR with regards to fork choice updates

New devnet spec: https://notes.ethereum.org/@ethpandaops/peerdas-devnet-1

### Spec test release soon

Mostly KZG updates and should not impact everyone much
**Nimbus:** would be good to include MetaDataV3 PR in the release

ACTION: Hsiao-wei to merge and include in the release

Note: Next (few) devnet will NOT have sampling changes included

### Spec PR for custody groups (decouple subnet from das-core, proposal from Pop)

client teams generally agree with it, Prysm suggests to target spec alpha-5

### Proposal to make this call weekly instead of biweekly, and moving time

Changing time makes it hard for APAC implementers to join

No one on the call feels that we should reschedule this

### Franceso's new documentation to exclude sampling

https://hackmd.io/@fradamt/no-peer-sampling

Potentially no peer sampling in devnet testing, just to help with iteration cycles, and potentially ok with no peer sampling in production

Prysm: not having sampling will simplify for more clients, but concerned that adding peer sampling may be harder later (requires a hard fork)
- It's not a last minute idea, SubnetDAS was something that's been considered for a long time
- It's mainly to help with implementation cycles, we could go live with sampling if we feel that it's easier later. This is an option to consider.
- The goal is to ship something soon, with some scalability improvements.
