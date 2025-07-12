## Resources

- [Pre-read](https://www.notion.so/efdn/History-Expiry-f23g-207d9895554180779fc4c7f9e3d95817) [[PDF](Slides-notes/10-Jun-history-expiry-preread.pdf)]

## AI-generated notes

### Summary

* **Pre‑merge history expiry is implemented across all major execution clients**, including Geth, Nethermind, Besu, Erigon, Reth (import‑only), and the consensus clients; each confirms the code path to discard blocks **up to the Merge point** is merged and can be activated.
* **Default behaviour diverges today**: some clients already prune when the operator passes a flag, but none ship with pruning *on* by default. Most plan to make “sync‑without‑pre‑merge‑history” the default once a coordinated public announcement is ready.
* Clients unanimously **support ERA files** as the canonical way to re‑add pruned history, but UX differs:

  * Geth streams blocks directly from ERA files placed in a dedicated `ancients/era` directory (no import step).
  * Others currently import the files into the DB and will add “direct‑read” later.
* **Full‑sync from ERA files** (i.e. Genesis‑to‑head without ever downloading old bodies) is not yet finished anywhere; all teams agree it is desirable.
* The meeting revisits the **portal network** after recent EF layoffs:

  * EF’s dedicated team is gone, but several client teams still intend to embed a portal implementation (e.g. Geth integrating the Go “zui” stack).
  * Consensus: portal **must not become a mandatory dependency** for running an EL node, but could be the long‑term decentralized back‑stop for history.
* **Next‑step design questions**:

  1. What *minimum* slice of history must every node keep?
  2. Should expiry be **rolling** (e.g. last N months) or **fork‑based** (drop everything before a named upgrade)?
  3. What exact file format should store *post‑merge* blocks?
* Rough convergence was reached on:

  * **Rolling window** (aligned with the CL’s 5‑month weak‑subjectivity horizon) is preferred; fork‑based checkpoint can serve as an interim step.
  * **Split ERA formats**: an “ERA‑E” file for execution payloads *with receipts* and an “ERA‑C” file for consensus data; avoid one combined file to keep tooling simple.  
* **Timeline sketch** (subject to ACD approval):

  * *June 2025*: publish blog + tooling so operators can prune pre‑merge data safely (clients may flip the default immediately after).
  * *July 2025*: finalise the ERA‑E(+receipts) spec and rolling‑window parameter; each client starts implementation.
  * *Fusaka* upgrade (\~Q4 2025): reasonable target for “history‑light” sync to be the out‑of‑box default.

### Chronological notes

* **Opening & roll‑call**

  * Interim chair (Felix Lange) confirms Matt Garnett absent; purpose is to assess status of history expiry.
  * Each client states readiness: Nethermind “has it”, Nimbus “has it”, Geth “has it”, Besu “has it”; Reth can read ERA files but cannot yet prune.
* **User‑experience survey**

  * Geth: two modes – start in `--history.expire` (skip pre‑merge) or run a one‑off prune command; headers always retained back to Genesis.
  * Nethermind: new nodes default to “no history”; existing nodes will auto‑prune in background.
  * Besu: pruning flag exists, will become default.
  * Clients agree no cross‑client guideline exists for defaults yet.
* **ERA file handling details**

  * Geth treats `.era` files as zero‑copy ancients; user drops them into a folder and the RPC layer streams bodies on demand.
  * Nethermind currently *imports* the file into the DB; wants direct‑read parity.
  * Shared pain‑point: importing duplicates data and can exceed 1 TB transient disk usage.
  * Everyone still missing: **full‑sync directly from ERA** without classic body/receipt download.
* **Receipts & file‑format debate**
  * Need a post‑merge successor to *ERA‑1* (PoW‑oriented).
  * Options tabled:
    * Re‑use ERA‑1 and *append* receipt records (backwards‑compatible).
    * Adopt CL’s *E2HS* format.
    * Define two new flavours: `ERA‑E` (EL only, incl. receipts) and `ERA‑C` (CL only, proofs, validator sets).
  * Majority lean to **ERA‑E + receipts** plus a wholly separate CL archive; avoids slot/block mismatches and heavy CL overhead in EL nodes.
* **Portal network status**

  * EF portal team (incl. Piper Merriam) was laid off; only a single dev remains, re‑assigned.
  * Rust impl *Trin* is still community‑maintained; Go impl *zui* is nearly feature‑complete and being embedded in Geth.
  * Proposal: treat portal as the “next‑gen” P2P layer inside EL clients, but keep it *optional*.
  * Concern: a vibrant portal network needs social consensus on “reasonable minimum storage” (10 GB? 50 GB? still undecided).
* **Rolling vs. fork‑based expiry**

  * CL already allows clients to prune anything older than 5 months (defined in‑spec); not all CLs enforce it, but the limit exists.
  * Rolling advantages: avoids repeated fork coordination, mirrors CL behaviour, simpler messaging (“nodes keep last N months”).
  * Fork‑based advantages: re‑uses devnet/fork tooling, matches the successful pre‑merge drop pattern.
  * Room consensus: target **rolling window**, but accept an interim “drop up to Dencun / Pectra / Fusaka” if that ships sooner.
* **API & dependency questions**

  * CLs that rely on EL block bodies for deposit‑contract proofs need a guaranteed minimum window; five‑month figure may be revisited.
  * Suggestion: expose “head pointer” in the Engine API so CL can query what the EL still stores.
  * Geth notes some CL implementations are still querying obsolete receipts; those RPC calls should be removed to avoid user confusion.
* **Distribution & discovery of files**

  * Geth has `geth eras fetch <from> <to> --server <url>`; requires users to supply a mirror.
  * Ideas:
    * Publish a curated mirror list on GitHub.
    * Embed a default EF mirror URL (concern: centralisation).
    * Longer‑term: distribute the files via portal with erasure coding.
* **Data‑volume & redundancy estimates**

  * Portal advocates quote a target of *5 % of history per node*; others deem that too high if gas limit scales.
  * Execution‑only header chain is < 10 GB, so retaining all headers indefinitely is considered acceptable.
* **Timelines proposed**

  * *June*: run cross‑client CLI tests on mainnet & Holesky; blog post instructing operators how to prune pre‑merge data.
  * *July*: lock ERA‑E spec and rolling‑window constant; small working group to finalise chunk size (epoch vs block‑count).
  * *Before Fusaka*: majority of production nodes sync without pre‑merge history by default; some may already roll off early post‑merge history.
* **Outstanding items / action points**

  * Draft ERA‑E(+receipts) spec text and reference implementation.
  * Decide on minimum rolling window (≥ 5 months?) and header retention policy.
  * Remove stale receipt queries from consensus clients.
  * Evaluate erasure‑coded distribution piggy‑backing on CL libp2p.
  * Update docs & ACD agendas for a single “flip the default” date.

### Relevant links

* EIP‑4444: *Bound Historical Data in Execution Clients* — [https://eips.ethereum.org/EIPS/eip-4444](https://eips.ethereum.org/EIPS/eip-4444)
* Trin (Rust portal network client) — [https://github.com/ethereum/trin](https://github.com/ethereum/trin)
* EIP‑4844 (blob sidecars; referenced in rolling‑window analogy) — [https://eips.ethereum.org/EIPS/eip-4844](https://eips.ethereum.org/EIPS/eip-4844)
