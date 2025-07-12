## Resources

- [Pre-read](https://hackmd.io/xe5e3ubsQNOuKv3I9YTwyA) [[PDF](Slides-notes/10-Jun-future-of-PeerDAS-preread.pdf)]
- Slides - [Scaling the L2: EL mempool short-term future](https://drive.google.com/file/d/1B0DfGcerj7HCOCWXN3frN_Rn2w1JDpi9/view) [[PDF](Slides-notes/10-Jun-future-of-PeerDAS-slides-el-mempool.pdf)]
- Slides - [Scaling the L2: cell level "gossip"](https://drive.google.com/file/d/1ijtiyVodnvrozeEkLjsrjVuFXc1WpYAw/view) [[PDF](Slides-notes/10-Jun-future-of-PeerDAS-slides-cell-gossip.pdf)]

## AI-generated notes

<sup>[prompt](Slides-notes/AI-info.md)</sup>

### Summary

* **Session scope** – reviewed the *current* PeerDAS design, enumerated its weaknesses, and brainstormed two forward paths: **(a) mempool handling of blobs** and **(b) propagation / reconstruction efficiency**.
* **Four principal shortcomings identified**

  1. **`getBlobs` dependency on full columns** – a node must already hold *every* blob in the column to reconstruct; private blobs or mild mempool loss break the shortcut.
  2. **Back‑bone (“super”) node reliance** – only nodes willing to download ≥ ½ of all columns can help reconstruction; smaller participants become passive.
  3. **Inefficient gossip‑sub flooding** – each column is pushed to the node’s full mesh (≈ 8 peers), causing needless replication as blob size/throughput grows.
  4. **“All blobs in the mempool”** – today every EL propagates every blob; as throughput rises this shifts the bottleneck from CL to EL and cannot scale.
* **Empirical data (Geth, 500‑peer test)** – public blobs reached ≈ 80 % of peers within \~1 s; overall blob traffic ≈ 11 kB/s; \~20 % of main‑net blocks contain at least one private blob, disabling `getBlobs` for that block.
* **Implicit sharding path** – if bandwidth limits stay unchanged, diffusion will naturally drop below 100 %; mempool becomes an *emergent* shard network, but `getBlobs` then needs smarter selective fetch.
* **Explicit horizontal sharding proposal** – hash last *n* bits of the **transaction hash** against the node‑ID; each node fetches/serves only its shard (e.g., 16 shards → \~500 nodes per shard). Real‑network snapshot shows nearly uniform distribution of both type‑3 txs and blobs. Prototype patches for Geth & Reth are in flight.
* **Vertical / column sharding sketch** – have nodes fetch column fragments; safer for DoS only with extra fraud proofs (“mantickets”); considered longer‑term.
* **Probabilistic fetch + “predictive self‑staging”** – broadcast type‑3 *headers* network‑wide; only \~15 % of peers randomly download each blob payload via a new `get_blob_payload` devp2p RPC. Peers advertise availability flags; poor responders are scored down. Keeps bandwidth flat while maintaining high (> 99 %) availability probability.
* **DoS & builder considerations** – bursty “all‑at‑once” downloads by upcoming proposers could leak their role; stochastic fetch and stable bandwidth smooth such spikes. Builders can and should run full‑blob mempools; ordinary validators should not be required to.
* **Roll‑up constraints** – sharding by *sender address* was examined but rejected: roll‑ups rely on single‑address sequential nonces, and splitting traffic across many addresses is impractical. Hash‑based sharding avoids this pitfall.
* **Timeline signals** – Fusaka can ship with present mempool logic at modest throughput; serious mempool/propagation changes are expected only *after* Fusaka (target upgrades: Glamsterdam +).
* **Long‑range ideas** – cell‑level messaging, row‑based subnets, side‑car blobs (hash pinned in the header) and smarter encoding were parked for the second sub‑session.

---

### Chronological notes

* **Agenda outline** – 5–10 min recap of PeerDAS design → 40 min mempool discussion → 40 min propagation; aim is to map the design space rather than choose a single solution now.
* **Current design recap**

  * Blobs enter the EL mempool already KZG‑encoded with proofs.
  * CL propagates *columns* via dedicated subnets; a validator samples column‑wise.
  * Reconstruction today requires half the columns and is typically performed by a small “backbone” subset of nodes.
* **Problem 1 – weakened `getBlobs`**

  * Needs *all* blobs in a column; fails for private blobs and for any EL that missed ≥ 1 blob.
  * Ties usefulness to perfect mempool propagation, which is unrealistic at higher throughput.
* **Problem 2 – backbone‑node dependency**

  * Non‑backbone nodes cannot contribute to availability because they never hold enough columns to reconstruct a row.
  * Reconstruction workload (CPU + reseed bandwidth) concentrates on a minority.
* **Problem 3 – gossip‑sub inefficiency**

  * Each column (\~tens of kB) is multicasted to all mesh peers; replication factor too high.
  * As blob size / target gas increases this becomes prohibitive.
* **Problem 4 – full‑blob mempool**

  * All blobs currently travel through EL; CL improvements therefore just shift scaling pain leftwards.
  * Eventually EL bandwidth becomes the throttling constraint.
* **Measurement study (Csaba)**

  * Geth node with 500 peers recorded who announced and who delivered blobs/txs.
  * 80 % of public blobs reached the node; propagation median < 1 s.
  * Private blobs make ≈ 20 % of blocks “`getBlobs`‑unfriendly”.
  * Bandwidth today: \~11 kB/s per node for blob pushes; manageable but linear in throughput.
* **Short‑term outlook**

  * **Implicit sharding**: as bandwidth saturates, diffusion < 100 % becomes inevitable; `getBlobs` must adapt (smarter selective fetch, relaxed success criteria).
  * Could likely double current blob count before hitting the wall.
* **Explicit horizontal sharding design (Raúl & team)**

  * Hash(last *n* bits(txHash)) == last *n* bits(nodeID) → node subscribes to that shard.
  * With 16 shards and ≈ 8 k main‑net nodes → \~500 replicas per shard.
  * Real‑data simulation shows near‑uniform blob distribution; hash‑of‑sender performs poorly (one shard dominates).
  * Early code exists for Geth & Reth.
* **Vertical / column sharding concept** (Csaba)

  * Nodes fetch cells in their custodial columns only; needs extra validity checks (man‑tickets) to block spam.
  * Left for “longer‑term” subsystem after mempool work.
* **Probabilistic fetch protocol (“15 % dice‑roll”)**

  * Announce type‑3 tx hash + “have‑payload” flag to peers.
  * Each node randomly elects to fetch \~15 % of blobs; expect ≥ 4 serving peers with 95 % confidence in 1 000‑node network.
  * New devp2p RPC `get_blob_payload`; peers failing to serve are down‑scored.
  * Keeps type‑3 txs global (needed for predictive cell staging) while capping bulk data traffic.
* **Predictive self‑staging**

  * CL watches EL mempool look‑ahead window; nodes holding data pre‑stage cells during idle slot time.
  * Requires that every node has the tx header to authenticate incoming cells.
* **DoS & peer‑selection notes**

  * Adaptive disconnects could penalise slow peers but risk amplifying transient link loss; tuning needed.
  * Random selection of fetchers reduces targeted attack surface compared with deterministic shards.
* **Roll‑ups & nonce ordering**

  * Sharding by sender breaks roll‑ups that require sequential nonces; they cannot easily split traffic across addresses.
  * Hash‑based sharding leaves roll‑ups untouched.
* **Implementation and timeline**

  * No mempool overhaul planned for Fusaka; could ship with lower throughput.
  * Expect prototypes, benchmarks and consensus on shard spec before Glamsterdam upgrade cycle.
* **Future‑work parking lot**

  * Cell‑level messaging and row subnets to make reconstruction fine‑grained.
  * Blob sidecars hashed in block header (decouples history size from consensus object).
  * Alternative encodings (pointer back‑references, erasure‑encoding tweaks).