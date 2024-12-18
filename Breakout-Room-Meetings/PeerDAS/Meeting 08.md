---
title: Meeting 08

---

# PeerDAS Breakout Room #8

Note: This file is copied from [here](https://docs.google.com/document/d/1Ng2IrCe28kTt1BnIsjtMlKHq2MHgaja24LhFXSvqfJQ/edit#heading=h.tubwqb51zcjq)


## Meeting info
Date: 2024.09.17
Agenda: https://github.com/ethereum/pm/issues/1145 
YouTube video: https://youtu.be/UYUJCbDf6po

### Client updates

**Lighthouse**

- Been doing local interop testing & debugging with other clients, observed network forking after 700 slots, when a client missed a block with 6 blobs (suspect due to slow proof computation on testing machine). Need to investigate why clients aren't recovering from these.
- Made max blobs per block configurable.
- Gathered some metrics with decentralized blob building with 16 blobs, working on a blog post to share the metrics 📉.

**Prysm**

- Fixed an issue with high CPU usage.
- Switched to subnet sampling only and removed peer sampling.
- Been investigating an issue with Prysm not being able to recover after a re-org. 🍴

**Teku**

- Worked on some DB refactor.
- Implemented Parallelisation of proof computation during block. proposal (5x faster) and KZG verification.
- Made debug log less noisy 🤫

**Grandine**

- Had some issue with LH downscoring the node, but almost ready to join devnet 🔥 will provide DevOps team with a branch.


### Devnet Updates

Local testing

Found a bug with Lodestar endianness in ENR.

Network still forks after some slots, will look into metrics

Potentially try testing with no blobs, and gradually increase blob count and observe behaviour

Barnabas is back 🎉

Katya raised a new metrics Spec change
- Katya will create a PR for this: https://github.com/KatyaRyazantseva/beacon-metrics/blob/master/metrics.md#peerdas-metrics

**Lion**: we should distinguish between interesting metrics and metrics that should be standardized, It’s historically difficult to standardize metrics:

**Saulius**: suggest to implement the required functionality all in clients and open PR. Using the same Dashboard will make debugging issues much easier, people agreed.

### P2P Debug Tool

Jimmy investigated the possibility of interpreting and visualizing P2P traffic to help with debugging, however this is very hard due to encryption with noise protocol.

Pari suggested implementing debug events on the Beacon API, and was interested to hear clients' thoughts.

Pari thinks this would be very useful, current tooling uses traces but it is still very difficult to debug p2p traffic. Having visibility in traffic will also allow us to see messages that didn’t pass validation.

- Will draft a Beacon API PR and continue the discussion from there
If devs are having issues with local testing due to resources, devops team can offer some temporary help.

Will continue with local testing and iron out issues before we launch devnet-2.

### Spec Discussion

Sampling without Peer Sampling (https://github.com/ethereum/consensus-specs/pull/3870)

- This is still targeted for devnet-2.
- Prysm has implemented this and it was an easy change
- Q: Do we need to keep the samples from the extra subnets?
  - **Francesco**: easiest to keep them in case people ask.
  - However most clients only query peers that advertise the columns, so maybe it’s not necessary to store those.
  - Francesco to clarify this with a spec PR.

### Open Questions

George asked if client teams are happy with the direction with proof computation
- There’s a distributed block building breakout call scheduled later today to discuss.
- In general, teams support the pre-computation and distributed block building strategy.
- Lighthouse has performed some testing with 16 blobs and computation metrics is looking good (more to share later)

**Pari**: team's thoughts on splitting Pectra into 2 forks?
- **Lion**: Fusaka Q1 2026, is it too late?
- **Francesco**: feel uneasy bundled with EOF, should ship as soon as we can
- Some suggestions on a CL only fork after Pectra-1
- **Jimmy**: in favour of split because it seems unlikely that we’d be ready by Q1 2025, still have validator custody and custody groups to implement.

Jimmy: What’s the must-have features before we can ship PeerDAS
- Outstanding spec changes we haven’t implemented: validator custody and custody groups, is there any more?
- Francesco feels more strongly about validator custody, custody groups is nice to have
- What about sharded mem pools?
  - Francesco: should not consider it on the critical path
  - Jimmy: from testing 16 blobs, the EL bandwidth usage doesn’t seem too crazy, we can probably live without this until 64 blobs
- Should optimizations like distributed block building be part of the requirements to ship PeerDAS?
- **Francesco**: We're not talking about crazy high blob counts, we don't really need to include full distributed block building, as long as we have a viable infrastructure to make it work.
- Home stakers could include less blobs, from the network perspective it’s fine.

## Zoom chat links

https://github.com/KatyaRyazantseva/beacon-metrics/blob/master/metrics.md#peerdas-metrics

https://grafana.observability.ethpandaops.io/public-dashboards/f5ea5e0b0d3a4cbcbb2c6a93a014112c?orgId=1