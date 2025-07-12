## AI-generated notes

### Summary

* The original “roll‑up‑centric roadmap” assumed that Layer‑2s (L2s) would quickly diverge from Layer‑1 (L1) by adopting new EVM features, but the ecosystem is instead converging on **strong EVM equivalence** across layers.
* Exotic features first expected on L2s (e.g. the *R1 precompile*, generic curve precompiles, native account‑abstraction) gained little traction because of security, competitive and isolation risks; L1 is now leading on feature adoption.
* The meeting focused on how **upcoming L1 execution‑layer changes** can be designed so they:

  1. are *immediately useful* to L2s or
  2. are *easily adaptable* by L2s with minimal diff.
* Three collaboration areas were defined:

  1. **Passive consumption** – ship L1 features in a form that L2s can reuse (separate data pricing, opcode/precompile repricing, transaction‑type extensibility).
  2. **Active co‑design for scalability** – share L2 experience running at hundreds of millions of gas, align on state/history expiry, database layouts, block‑level access lists and large‑block performance.
  3. **Small but inevitable L2‑only gaps** – standardise necessities such as `L1_SLOAD` while minimising bespoke opcodes and precompile address clashes.
* Gas‑cost hard‑coding by dApps is a blocker; proposals included **frequent repricing** on L1 and even *per‑block variable schedules* or runtime‑configurable gas tables to force best‑practice.
* Geth maintainers previewed a **rolling‑window History Expiry** implementation (configurable “N most‑recent blocks”) and a forthcoming *new archive‑mode*; they urged L2s to stop relying on legacy full‑history modes.
* L2 operators highlighted urgent pain‑points: data‑blob costs, SSTORE/SLOAD gas mis‑pricing, database bottlenecks (LMDB vs. Pebble vs. LevelDB), 40‑TB+ chain storage growth, and need for parallel execution hints (block‑level access lists).
* Consensus emerged to restructure cross‑layer communication: retire the broad “Roll‑Call” meetings, replace with **single‑topic, feature‑oriented calls** and a clearer AllCoreDevs (ACD) reform that lists champions, stakeholders and decision timelines.
* EF’s new *Application & Protocol Support* team will institutionalise early application feedback and publish predictable upgrade roadmaps; L2s committed resources to co‑developing scaling features.
* Agreement: L1 innovation cadence will remain slow (≥ 1 year per feature) but must be *predictable*; L2s can ship interim precompiles provided an address‑allocation scheme and eventual L1 alignment exist.

---

### Chronological notes

* **Roll‑up‑centric roadmap recap**

  * Vitalik’s post initiated expectation that L2 EVMs would diverge while L1 ossified.
  * Companies built roll‑ups, but few adopted new crypto primitives; R1 precompile uptake limited.
  * Security and competitive risks made solo innovation unattractive; equivalence prevailed.

* **Shift in strategy**

  * Community now pushes L1 scaling (compute, data, state), reducing need for exotic L2‑only EVMs.
  * Goal: land “cool features” on mainnet first, then have them propagate automatically to L2s.

* **Session objectives (three tracks)**

  * *Track 1*: ensure new L1 features are either directly useful to L2s or trivially adjustable.
  * *Track 2*: leverage L2 operational experience (gigagas, 40 TB state) to inform L1 throughput work.
  * *Track 3*: decide whether thin but persistent L2‑specific deltas should be standardised.

* **Topic 1 – Data & gas‑cost design**

  * L1 will price compute, data and state separately; L2s need compatible data‑pricing hooks for calldata/blobs.
  * Frequent opcode & precompile repricing planned; needs zk‑EVM awareness and L2‑specific schedules.
  * Proposal: make the gas‑table a runtime configuration file; performance impact of cache look‑ups under study.
  * Idea floated: per‑block randomised gas prices to discourage hard‑coding.

* **Engineering pain‑point: gas‑equivalence**

  * \~60 % of some L2 engineering effort spent mirroring L1 gas; repricing could relieve that.
  * Smooth transition required; ecosystem must identify which contracts would break if costs change.

* **Additional L2 asks**

  * Independent fee fields for L2‑specific costs (data, proof) within the L1 tx format; leave an extensible “misc” field.
  * New tx type without sig‑verification for system submissions.
  * Block‑level access lists to parallelise state access.

* **History & state management**

  * Geth team:
    * Basic *history‑pruning* code done; rolling‑window expiry planned for end‑2025 with configurable depth.
    * Need client‑wide consensus on parameters; sub‑chains/L2s free to choose different windows.
    * Legacy archive‑mode is unsustainable; new mode shrinks disk but drops historical proof ability.
  * Need alternative fetch layer (EIP‑4444 style) for resurrecting pruned data.
  * Clarify terminology: “history expiry” vs. “state expiry” vs. “deleting cold accounts”.

* **Database layout discussion**

  * Each EL client currently wedded to bespoke DB (Geth/LevelDB, Nethermind/RocksDB, Erigon/BadgerDB, Reth/Pe bble); performance diverges at high TPS.
  * Desire for a **purpose‑built DB** tuned to future Verkle/Binary tries or QM‑D proposals; suggestion to convene design sessions.

* **State‑size & stateless research**

  * Future L1 scaling (≥ 100 M gas) will force stateless or partially‑stateful nodes plus zk‑proof‑friendly state structures.
  * L2s facing these limits now; collaboration could “pull‑forward” lessons to L1 research.

* **Process & governance improvements**

  * L2s need proactive notice of candidate EIPs (EOF, R1, block AXL, etc.) to allocate resources.
  * EF to pilot *feature‑oriented stakeholder calls* and publish explicit inclusion/rejection decisions per fork.
  * New ACD reform post seeks feedback; EF “App & Protocol Support” team launched to formalise engagement.

* **Standardising L2‑only features**

  * Example: `L1_SLOAD` (needed only on roll‑ups) – decide whether to standardise in a shared EIP bucket.
  * Consensus: avoid custom opcodes; favour precompiles (address space above mainnet range, block allocations per chain).
  * If L2s must ship early, involve L1 devs to avoid divergent “v1/v2” versions (lesson from R1 precompile).

* **Closing points**

  * L1 feature velocity will remain measured (≥ 12 months from spec to fork), but predictability and clear milestones are paramount.
  * Engineering solutions (better node modes, pruning, DB tuning) can mitigate near‑term L2 pressures while protocol‑level work matures.
  * Parties will continue discussions at subsequent single‑topic sessions and via the new stakeholder process.

---

### Relevant links

* History expiry (sectioned sync) proposal — [https://eips.ethereum.org/EIPS/eip-4444](https://eips.ethereum.org/EIPS/eip-4444)