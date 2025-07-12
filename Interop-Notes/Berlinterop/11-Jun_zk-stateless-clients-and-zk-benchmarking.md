## Resources

- [Pre-read, zk stateless clients](https://hackmd.io/@kevaundray/r1APz8c-gx) [[PDF](Slides-notes/11-Jun_zk-stateless-clients-and-zk-benchmarking-preread1.pdf)]
- [Pre-read, zk benchmarking](https://hackmd.io/@kevaundray/rkQiwS9Wex) [[PDF](Slides-notes/11-Jun_zk-stateless-clients-and-zk-benchmarking-preread2.pdf)]

## AI-generated notes

<sup>[prompt](Slides-notes/AI-info.md)</sup>

### Summary

* Reviewed the current **EL + CL** stack: proposer builds/outsources blocks (often via **MEV‑Boost**), attesters vote, and “full‑state” RPCs (e.g. Infura) answer trust‑based queries.
* Simply raising the gas limit is blocked by three coupled limits: execution time for re‑running the block, bandwidth for network propagation, and state growth/disk I/O.
* Introducing a **zk‑stateless** model replaces full re‑execution with proof verification (roughly constant time) and cuts gossip bandwidth to “block‑header + proofs”; transaction data must instead live in **blobs** for data availability.
* Stateless ≠ zk:

  * *Stateless* = block + state subset + state proof (MPT, Verkle, etc.).
  * *zk* = state proof **plus** execution proof; combined they form a **zkEVM proof**.
* New node roles foreseen:

  * **Stateless proposer** (must outsource block building).
  * **Partially‑stateless RPC** (keeps only watched keys).
  * **Proof‑serving stateless RPC** (Infura‑like but returns Merkle/Verkle proofs).
* Two reference architectures were sketched:

  1. State‑**full** EL validates block, builds witness, calls an external prover, then serves proofs to many stateless ELs over RLPx.
  2. Single‑binary CL with embedded EL verification; proof is broadcast on a new gossip topic.
* Block builders will be required to attach proofs; open questions on incentives and on negative externalities of external “prover networks”.
* **Client diversity** still matters:

  * Multiple EL state‑transition functions guard against logic bugs (“zkEVM will happily prove your bug”).
  * Multiple **zkEVM** implementations guard against proving/verification bugs; target is *N* proofs per block (exact *N* TBD, maybe one of them a raw state proof fallback).
* Debate: should specific verifiers be **enshrined** in consensus (proofs in‑block) or selected off‑chain by validators? Trade‑offs around upgrade friction versus implicit social enshrinement.
* Engineering status:

  * **Benchmarking** harness runs execution‑spec tests through each zkEVM; current single‑GPU success rates are low and some tests crash provers.
  * **ZK‑stateless client** prototype exists; likely migrating to an “embedded‑in‑CL” version first in Lighthouse/Lodestar.
  * Standardisation of APIs and security guidelines in progress.
* **Benchmarking pipeline** (Execution‑Spec → zkEVM‑bench) will quantify average and worst‑case proving times across guest programs, allocators and zkEVMs; results intended for public dashboards (e.g. ethproofs.org).
* Gas‑repricing can only be done once worst‑case provers for the chosen top‑N zkEVMs are understood; repricing should be infrequent because it breaks applications.
* Worst‑case cost shifts from validators to provers; **FCeIL/FOCIL** may be the only path for an attacker to force an expensive proof.
* Target proving latency (illustrative): ≈ 6 s, leaving time for proof gossip before the attestation deadline; protocol tweaks (e.g. level‑access lists) could help.
* Open research: interaction with data‑availability sampling, censorship risks if users must obtain witnesses from RPCs, smartphone validator feasibility, and how to de‑risk verifier upgrades.

### Chronological notes

* Intro: session renamed from “Road to zk” back to **ZK Stateless Client**; agenda covers preliminaries for zkEVM newcomers.
* Recap of current actors: proposer, block builder (local or **MEV‑Boost**), attesters, full‑state RPC.
* Question posed: “Why not just raise gas limit?” — answered with three scaling vectors (execution, propagation, state).
* Constraint accepted: decentralised nodes must meet **EIP‑7870** hardware spec; block building must retain a fallback path.
* Table comparing today vs zk‑stateless:

  * Execution → verification.
  * Full block → header + proof.
  * Still need blob DA (“put the transactions in blobs”).
* Clarification: stateless verification still needs blob bandwidth; bigger blocks mean more blobs.
* Distinction drawn between stateless and zk; tree choice only affects state proof size, not zk.
* Defined artefacts: **state proof** (e.g. MPT witness), **execution proof**, **zkEVM proof = state + execution**.
* Enumerated node flavours in zk‑stateless world; partially‑stateless node stores only watched keys, otherwise requests proofs.
* Consensus layer remains classic; zk only replaces EL execution path.
* Architectural option #1 (split EL/CL, RLPx) explained; stateless ELs request proofs from state‑full EL which in turn queries a prover.
* Architectural option #2 (single binary CL with embedded verifier) displayed; proofs gossiped on specialised pub‑sub topic.
* State‑full node should pre‑compute proofs so many stateless peers can fetch them.
* Mandatory‑proof rule proposed for block builders; economics still un‑specified.
* Risks of external “prover networks”: liveness limits and cost externalities.
* Discussion on proof sizes: minimal 128 kB; five proofs ≈ 640 kB; 1 MB proofs deemed “untenable”.
* Debate over why multiple proofs: desire for **verifier** diversity per block; fallback idea = re‑execution using a raw state proof.
* If only *k*‑of‑N proofs are required, builders might optimise for those and ignore others.
* **Enshrinement** debate: in‑block proofs make verifiers explicit but hard to retire; off‑chain selection leaves implicit enshrinement to client defaults.
* Engineering update bullets:

  * Execution‑spec test‑bench success rate currently low; many worst‑case tests crash provers.
  * Moving the zk‑stateless prototype from separate‑EL to CL‑embedded path.
  * API standardisation & security check‑lists underway.
* Benchmarking deep‑dive: dimensions = standard test‑vectors, guest program variants, zkEVM variants.
* Pipeline goal: reproducible metrics to drive gas repricing, tree‑choice questions, hash‑function changes, etc.
* Observed issues: bump allocators exhaust limited zkEVM memory; need alternative allocators.
* Publication plan: frequent automated runs, public web dashboard (likely on **ethproofs.org**).
* Gas‑repricing caveats: zkEVM performance improving rapidly; need top‑N shortlist before repricing; repricing disrupts apps.
* Shift in “worst‑case” mindset: validator cost disappears, prover cost dominates; only **Fork‑Choice‑enforced Inclusion Lists** can force a hostile prover workload.
* Open protocol questions:

  * How FOCI L gas‑caps interact with censorship‑resistance.
  * Where light clients obtain witnesses without trusting RPCs.
  * Whether always‑online requirement blocks phone‑based validators.
* Proving‑time target discussion: deduct 4 s proposal slack → aim for \~6 s proving within the 12 s slot; hardware and protocol tricks (parallel tx proofs, recursion) expected to close gap.
* Concern: contract‑size increases and shorter slots both make proving harder; need an end‑to‑end prototype to identify real bottlenecks.
* Closing remarks: future “stateless roadmap” talk will address censorship and witness‑distribution in more depth; meeting adjourned.

### Relevant links

* Execution‑spec tests (reference test‑vectors): [github.com/ethereum/execution-spec-tests](https://github.com/ethereum/execution-spec-tests)
* EthProofs: [ethproofs.org](https://ethproofs.org)
