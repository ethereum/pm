

# PeerDAS Breakout Room #3
Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit#heading=h.tubwqb51zcjq)
## Meeting info
**Date**: 2024.07.09
**Agenda**: https://github.com/ethereum/pm/issues/1093
**YouTube Video**: https://www.youtube.com/watch?v=kr356fArKbI
## Notes
### Client updates
- **Prysm:**
  - testing with new KZG APIs
  - working on fixing bugs in devnet-1
- **Lighthouse:**
  - Mostly working on sync, fixed an issue with rpc limits, and able to serve by range requests
  - Got sync to work a branch, but there are still some open issues that cause it to be slow
  - Tested kev's rust kzg library and it works well. Potentially merge and switch to it soon.
  - Tried to revive devnet-1 with Michael's lcli http-sync tool but no luck with Lighthouse. Best to relaunch devnet.
  - ACTION: Raise rate limit on Lighthouse supernode (instead of disabling rate limiter for safety)
- **Lodestar:**
  - Able to sync Lodestar using supernodes (without validation) 🎉
  - Will work on validation next to participate in running validators on next devnet
- **Grandine:** fixing the sync. Probably won’t participate in the next devnet

### Peerdas-devnet-1

Many forks at the moment. 6 different forks(!!!!): https://dora.peerdas-devnet-1.ethpandaops.io/forks

Should relaunch with a higher rate limit.

Bug 1: rate limiting

Bug 2: syncing

Bug 3: ENR update

- Can be improved with metadata v3 PR: https://github.com/ethereum/consensus-specs/pull/3821

Why did the LH supernode issue break the network?
- Both LH supernodes restarted, and one of them started sending excessive sampling requests to the other. Neither supernode was able to serve requests to others, potentially causing the network to split
- Teku and Prysm supernodes all died too
- Prysm: when Lighthouse died, it triggered a few bugs in Prysm. Prysm is hoping to have these fixed by end of this week.
- DevOps suspected a potential ENR issue, there were a few ENR format mismatches between clients
  - LH: using ENR to identify supernodes isn't reliable as they aren't always available. Lion raised a metadata v3 spec PR, that would help with this.
  - Prysm: may require a bit of work, and would delay relaunch devnet-2
MetaDataV3 is potentially in the next devnet after devnet-2 since it's nice to have for now.

ACTION: Relaunch with the same specs with bug fixes by the end of this week

### Specs discussion

Decouple network subnet: https://github.com/ethereum/consensus-specs/pull/3832
- already have this for attestation and would like this for data columns
- custody group instead of subnets
- Csaba: good idea, concerned that we're grouping columns just to make it efficient, but need to look into more details
- ACTION: client teams to review and potentially target devnet-3

Passing blob limit from CL: https://github.com/ethereum/consensus-specs/pull/3800
- CL clients generally support it.
- Re: do we realistically see ourselves changing the blob target to anything other than MAX // 2? if we do, then we should also have the CL send target along with max values (with the resulting extension of the EL header to have both values)
  - **Barnabas**: more flexibility if we just always send both, even we don't need it in the foreseeable future. Francesco agrees.
  - **Pop**: Is there any reason why it's divided by 2?
  - **Francesco**: no specific reason. Danrad also chimed in but I missed it. Should we include it in Pectra?
    - **Dankrad**: good to include in Pectra, so we don't need to fork the EL to increase blob limit
  - ACTION: EIP update and change engine-api interface? and raise in ACD call

### Open discussion
**Kev**: plan to gather P2P metrics?
- Barnabas posted some essential metrics on discord
- Prysm and Lighthouse have most of the metrics
- LH: We need a large-ish network to get realistic metrics, What about Grandine?
  - Grandine is currently experimenting PeerDAS development with EPF, unlikely to participate in the next devnet

**Kev**: Rust PeerDAS KZG library
  - Teku merged the PR, can we get some part of the network to run the Rust KZG library?
  - Lighthouse is likely going to switch to it soon, possibly in the next devnet.

**Jimmy**: Lighthouse working on decentralized block building (Dankrad proposed)
- WIP PR for Deneb: https://github.com/sigp/lighthouse/pull/5829
- Reth fork: https://github.com/michaelsproul/reth/pull/1
- Lion’s HackMD: https://hackmd.io/@dapplion/blob_fetch
- execution-api spec: https://github.com/ethereum/execution-apis/pull/559

**Saulius**: What are the KZG crypto bottleneck
- Kev: the Rust PeerDAS KZG lib does not currently use GPU for "MSM"
- Saulius: NVIDIA GPU should be significantly faster than utilizing cpu fully
- Kev: Be good to get some metrics once it's implemented in Grandine
- Csaba: Having nodes do faster reconstructions in the network is helpful. With more blobs, it will be time-consuming.

## Zoom chat links
https://github.com/ethereum/pm/issues/1093

https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit

https://dora.peerdas-devnet-1.ethpandaops.io/forks

https://github.com/ethereum/consensus-specs/pull/3832

https://github.com/ethereum/consensus-specs/pull/3800

https://github.com/ethereum/pm/issues/1093#issuecomment-2215630809

https://discord.com/channels/595666850260713488/1252403418941624532/1256084227926003793

https://github.com/sigp/lighthouse/pull/5829

https://github.com/michaelsproul/reth/pull/1

https://hackmd.io/@dapplion/blob_fetch

https://github.com/ethereum/execution-apis/pull/55

https://github.com/grandinetech/rust-kzg?tab=readme-ov-file#blob-to-kzg-commitment-1
