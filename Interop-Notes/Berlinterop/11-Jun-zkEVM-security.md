## Resources

- [Pre-read](https://notes.ethereum.org/3-V-mUFUSliephNFkhaVyA) [[PDF](Slides-notes/11-Jun-zkEVM-security-preread.pdf)]

## AI-generated notes

<sup>[prompt](Slides-notes/AI-info.md)</sup>

### Summary

* Core‑devs presented a **three‑phase roadmap for integrating zkEVM proofs into Ethereum**:

  1. *Stateless‑client / early‑adopter phase* (target ≈ Q4 2025) – proofs optional.
  2. *Mandatory‑proofs / delayed‑execution phase* (≈ Q2 2026) – attestations withheld if a block lacks a proof.
  3. *Enshrinement* (≈ 2027‑28, date flexible) – one or more provers/verifiers become part of L1 consensus.
* **Minimum cryptographic strength**: >100 bits now; 128 bits expected post‑enshrinement.
* **No recursive Groth16 wrapping** is strongly preferred; goal is raw STARK or a universal‑setup SNARK directly acceptable to L1.
* **Proof‑size guideline**: ≤ 300 kB today (ideal ≤ 128 kB) to keep stateless‑client bandwidth manageable.
* Teams should publish an **“executable spec”** that sits between the academic paper and hand‑optimised code, capturing every optimisation and edge‑case.
* Establish a **verifier‑upgrade path**: a new verifier may ship only after it is at least as formally verified and audited as the previous one.
* **Formal‑verification plan**: begin partial FV of circuits+verifier during the optional‑proof phase; full FV required before enshrinement.
* **Security conjectures**: move away from unproven “8‑STARK” assumptions; medium‑term target is provable security or at least weaker, well‑studied conjectures (e.g. list‑decoding bounds).
* **Wrapping trade‑offs** debated:\*\* larger proofs + no trusted setup\*\* vs **small Groth16 proofs w/ setup & post‑quantum risk**. Consensus leans to eliminating wrapping and accepting slightly larger proofs.
* Multiple projects reported current raw STARK sizes (≈ 270 kB to 1 MB); all believe sub‑300 kB is feasible with parameter tuning.
* **Grinding** for extra security bits is rarely implemented; some teams plan to add it once wrapping is removed.
* Completeness / availability DoS and hardware‑cost constraints acknowledged but treated as orthogonal tracks (handled in Justin’s “prover‑killer” workstream).
* Bug‑bounty levels today are low (≈ 150 k USD); amounts will rise once proofs affect consensus and EF bounties apply.
* Power‑consumption limits, slot‑time halving, and future gas bumps noted but deferred to other discussions.

---

### Chronological notes

* **Session opens**: purpose is to align on zkEVM security expectations and iterate with project teams.
* **Roadmap sketch**

  * Present → Future timeline drawn.
  * *Milestone 1*: “Stateless client” (\~Q4 2025) – zkEVM proof accepted by an opt‑in client, not required for attestations.
  * *Milestone 2*: “Mandatory proofs” (\~Q2 2026) – clients refuse to attest blocks lacking a proof.
  * *Milestone 3*: “Enshrined proofs” (farther future) – prover(s) live inside the core protocol, maximum security required.
* **Short‑term security guidelines (for Milestone 1)**

  * Proof system ≥ 100‑bit security.
  * **No recursive Groth16 wrapping** (avoid trusted‑setup complexity & post‑quantum fragility).
    * Acceptable: raw STARK, or universal‑setup PLONK.
  * **Target proof size** made‑up but “plausible”: ≤ 300 kB; *ideal* ≤ 128 kB to ease stateless‑client download load.
  * Need a **spec document**: pseudo‑code / executable spec bridging paper ↔ implementation; prevents optimisation‑induced bugs (e.g. recent Clonk‑ThreeFry omission).
  * Define **verifier‑upgradeability**: upgrades only after equal‑or‑better formal guarantees; hard requirement once proofs mandatory.
* **Open floor on wrapping**

  * General agreement: no wrapping “makes everything better”.
  * Pros/cons aired: Groth16 gives 2 kB proofs but needs large trusted setup & is non‑PQ; universal PLONK slower to prove; STARKs incur larger size.
  * Some teams already at \~270 kB raw (RiskZero); SP‑1 ≈ 1 MB but can tune parameters to shrink 3×.
  * If wrapping banned, protocol must tolerate bigger proofs; reconsider blob limits / gas cost.
* **Proof‑size details from teams**

  * RiskZero: 270 kB raw, no wrapping, two‑second recursion including final wrap if needed.
  * Gnosis HyperNova team (Porter): aiming sub‑300 kB raw; wrapping only for on‑chain posting.
  * Scroll: raw STARK huge, shrink via Groth16 to \~3 kB; could optimise raw proof if wrapping removed.
  * Lambda / Provenance: halo2‑KZG wrapper yields ≈ 1 kB; universal setup only.
  * SP‑1: \~1.5 MB raw due to conservative parameters; confident 300 kB achievable.
* **Spec discussion**

  * Spec must let two independent teams implement a verifier that agrees on transcripts.
  * Document all *protocol‑level* optimisations (affecting transcript) separately from *engineering* tweaks (parallel kernels, cache tricks).
  * Ideal workflow: write spec first, then code; reality: many will back‑write spec from optimised code—acceptable if result matches.
  * Example bug (double linear‑combination with coeff = 1) shows why explicit specs matter.
  * Debate on where spec lives: separate doc vs richly‑commented code; consensus: format flexible, but must exist and be maintained.
* **Circuits vs. proof‑system spec**

  * Verifier code abstracts circuit via VK; yet circuit logic itself must be specified to enable FV linking “function ↔ circuit”.
  * Compiler pipelines (e.g. DSL → IR → constraints) also need documentation for audit/FV.
* **Medium‑term goals (between Milestone 1 & 2)**

  * **Ditch heavy conjectures** (e.g. 8‑STARK) → provable security or weaker, scrutinised conjectures (list‑decoding bounds).
  * Accept 2‑3× proof‑size increase if needed; raise size ceiling accordingly.
  * Begin **partial formal verification** of circuits & verifiers; budget 6‑12 person‑months per prover.
  * Establish notice period for verifier changes; avoid “surprise” proofs.
* **Completeness / availability / DoS**

  * Recognised as separate track (“prover‑killer” work); not addressed by current size/security levers.
* **Gas limits & slot time**

  * Future half‑slot‑time and gas‑bump proposals will keep performance pressure high; proofs must stay fast despite larger size/FV.
* **Bug bounties**

  * Today \~150 k USD/project; will scale with criticality and EF umbrella once proofs enshrined.
* **Long‑term (enshrinement) expectations**

  * Provable security, 128‑bit target.
  * Fully‑verified specs & circuits; every verifier change follows EIP/ACD process.
  * Raw proof accepted directly by consensus, no wrappers, no un‑audited optimisations.
* **Open questions / future work**

  * Exact proof‑size limit to be finalised; communication channel TBD.
  * How to codify FV tooling so teams can iterate without months‑long external engagements.
  * Whether grinding suffices to restore lost bits when conjectures are relaxed.
  * Power‑budget targets and hardware standardisation (out of scope for this session).
* **Session closes** with agreement to share guideline doc, solicit feedback, and refine milestones ahead of Devcon‑next.