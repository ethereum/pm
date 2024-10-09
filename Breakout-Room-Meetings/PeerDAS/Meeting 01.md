# PeerDAS Breakout Room #1

Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit#heading=h.tubwqb51zcjq)

## Meeting Info: 
**Date**: 2024.06.11

**Agenda**: https://github.com/ethereum/pm/issues/1059

**YouTube Video**: https://www.youtube.com/watch?v=P86Dr9ABGeg

## Notes

- 12:04: DappLion nowhere to be found (Fixed by 12:10)
### Client updates:
- **Lighthouse:**
  - Various custody column lookup improvements based on interop feedback (request batching, load balancing among custodial peers etc)
  - Made PeerDAS network params (custody requirement, subnet count etc) configurable 
- **Prysm**: database upgrade, more efficient in reconstructing data
  - get_custody_columns & NodeID generation issues https://hackmd.io/TSLwFcUMTkynfVtf-a9_Ag
    - Prysm, Lodestar, Nimbus generate new NodeID at each restart for anonymity 
    - Prysm PR: https://github.com/prysmaticlabs/prysm/pull/14098
  - Francesco in chat about getting a random privateKey / nodeID at each start for full node (without validator) only: “the current parameters you still won’t have any anonymity because 128 choose 4 is too high”
- **Teku**: working on the draft sampling PR
- **Nimbus**: Started after the interop.
### Specs
- Considering moving MAX_BLOBS_PER_BLOCK to configuration + removing it from the EL side with EngineAPI update
  - However, it may break optimistic sync
- PeerDAS activation
  - Consensus to leave PeerDAS activation logic same as devnet-0 for the next devnet to keep things moving 
- PeerDAS bandwidth problem: https://discord.com/channels/595666850260713488/1247156108263555185/1247156110146928640


## Actions

- Go through current preset/config.yaml and check if we should move any value into config.yaml
- Start discussion on CL set blob max limit

## Zoom chat links
- https://github.com/ethereum/pm/issues/1059
- https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit?usp=sharing
- https://hackmd.io/TSLwFcUMTkynfVtf-a9_Ag
- https://github.com/prysmaticlabs/prysm/pull/14098
- https://github.com/sigp/lighthouse/pull/5899
- https://github.com/ethereum/consensus-specs/pull/3782
- https://github.com/ethereum/consensus-specs/pull/3772
- https://github.com/ethereum/consensus-specs/pull/3717
- Discord thread here: 
	https://discord.com/channels/595666850260713488/1247156108263555185/1247156110146928640
- Full zoom chat [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit)

