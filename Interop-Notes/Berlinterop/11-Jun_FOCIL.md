## Resources

- [Pre-read](https://hackmd.io/@oK3in1lRQ7-pt7b3j8nQxg/r1eEBJoGgg) [[PDF](Slides-notes/11-Jun_FOCIL-preread.pdf)]
- Slides - [Intro to FOCIL, Thomas](https://docs.google.com/presentation/d/1UvD2pGxWNAh5fFF-jtUVXn9lWYRw8K8xjK8n28kgaO8/edit?usp=sharing) [[PDF](Slides-notes/11-Jun_FOCIL-slides-thomas.pdf)]
- Slides - [FOCIL implementation status, Jihoon](Slides-notes/11-Jun_FOCIL-slides-jihoon.pdf.pdf)
- Slides - [FOCIL & Future of Nodes, Barnabé](https://docs.google.com/presentation/d/1DHIVUeKTvm1qWrmfVQzgRTNXn37jZljj6wSRvg6o2lw/edit?usp=sharing) [[PDF](Slides-notes/11-Jun_FOCIL-barnabe.pdf)]
- Slides - [Stateless FOCIL, Carlos](https://docs.google.com/presentation/d/1d0NSqc6OgIqyUwgjEVniE4Q16KC--ERiEVOe7l19XmA/edit?usp=sharing) [[PDF](Slides-notes/11-Jun_FOCIL-slides-carlos.pdf)]
- Slides - [zkFOCIL, Benedikt](Slides-notes/11-Jun_FOCIL-slides-benedikt.pdf)

## AI-generated notes

<sup>[prompt](Slides-notes/AI-info.md)</sup>

### Summary

* **Current status of FOCIL (Fork‑Choice‑enforced Inclusion Lists)**

  * Proposed as a headline EIP for the Glamsterdam upgrade; broad consensus on value, design largely stable for a year.
* **Implementation progress**

  * Local dev‑net now runs with 4 consensus‑layer (CL) clients (Lodestar, Prysm, Teku, Lighthouse‑in‑progress) and 2 execution‑layer (EL) clients (Geth, Reth forked by contributors). Nethermind, Erigon, Grandine are following. Spec‑test PRs and metrics draft PRs are open.
* **Outstanding work**

  * Need adversarial EL/CL tests, a clearer public narrative on scaling & UX, and agreement on deployment urgency.
* **Scaling rationale**

  * FOCIL separates censorship‑resistance (CR) from throughput, enabling L1 scaling without raising hardware requirements that would squeeze out “local builders.”
* **Synergies & conflicts with other roadmap items**

  * **Delayed Execution**: breaks the assumption that builders/execution engines know post‑state by attestation deadline; resolved by pairing with block‑level access lists carrying a state diff plus gas‑used field.
  * **ePBS**: same mitigation applies; alternative two‑step “bid list” approach exists but adds fork‑choice complexity.
  * **Account Abstraction (AA)**: FOCIL’s validity check is VM‑agnostic, but builder DoS must be avoided by recording first‑failure index; block‑level diffs again solve missing post‑state.
* **Stateless Ethereum interplay**

  * Validators running stateless or “VOPS” (Valid‑Only Partial‑Stateless) nodes can still act as includers if they store only the account tree (≈8 – 10 GiB today). Protects mempool health while avoiding user‑supplied witnesses.
  * Open design question: supporting AA when includers lack arbitrary state; options include transaction‑supplied proofs or 7702‑style upfront gas charge with refund.
* **zkFOCIL prototype**

  * Goal: hide which validator assembled an IL to deter targeted DoS. Achieved with linkable ring signatures + zkSNARK proof of key image. Prototype: 2.5 s key‑image generation (offline), 87 ms verification, 500 B proof; needs ≲16× speed‑up for production.
* **Future of nodes & “light FOCIL” vision**

  * Envisions three distinct roles: Attester (heavy), Builder (resource‑intensive), Includer (ultra‑light, possibly browser extension).
  * Proposal for permissionless includer set backed only by wallet balance (civil‑weight), with optional delegation; no slashing so service remains volunteer / reputation‑based.
* **Key open questions**

  * Incentivisation vs. complexity for includers, integrating zkFOCIL with light includers, handling validator‑set churn for key images, network‑layer anonymity, and defining end‑state CR metrics (expected inclusion time, time‑to‑CR).

---

### Chronological notes

* **Session agenda overview**: intro → implementation update → synergies with other EIPs → FOCIL × statelessness → zkFOCIL benchmarks → future‑of‑nodes discussion.

* **State of FOCIL**

  * Design unchanged “for the past year.”
  * Implementation traction required convincing EL/CL teams despite no CFI funding.
  * Weak points: adversarial testing, public narrative, timing/urgency discussion, long‑term roadmap (CR‑4‑Blob, zkFOCIL, stateless).

* **Scaling narrative**

  * Today: two sophisticated external builders + long‑tail local builders mitigate censorship.
  * Path 1: client/P2P optimisations (limited).
  * Path 2: raise hardware ↔ reduces local builders ↔ harms CR.
  * Path 3: “separate CR from throughput” via FOCIL with includers ensuring CR even if all blocks outsourced.

* **UX & metrics**

  * Need simple, empirical CR metrics: *expected inclusion time* or *time‑to‑censorship‑resistance*.

* **Urgency argument**

  * Current low censorship is “lucky.”
  * Growing regulation & vertical integration (builder ↔ searcher ↔ relay) threatens neutrality; e.g. single Build‑a‑Net outage.
  * Better to deploy before crisis; CR is Ethereum’s differentiator.

* **Implementation status (detailed)**

  * Interop dev‑net: Lodestar, Prysm, Teku, Geth; Nethermind catching up; Lighthouse bug outstanding.
  * Erigon/Grandine submitted EF‑funded FOCIL projects.
  * Draft PRs: EL & CL spec‑tests, metrics.
  * Assertion: “excellent technical readiness” → spec+fixtures and ≥6 clients within months.

* **EIP interactions**

  * *Delayed Execution* conflict: IL validity previously required post‑state; resolved by block‑level access list containing state‑diff + optimistic `gasUsed`. If incorrect, block reverts. Alternate design: builder posts “bid list” promise checked next slot.
  * *ePBS*: same solutions apply; two‑step enforcement vs. single‑step trade‑off.
  * *Account Abstraction*: FOCIL compatible because validation function is arbitrary; builder‑DoS prevented by logging first failure index + relying on transaction‑level state‑diffs to reconstruct intermediate state.

* **Statelessness & mempool health**

  * Risk: stateless includer cannot pre‑check balance/nonce → IL spam.
  * VOPS: includer stores account tree only (≈8 – 10 GiB, projected 15 – 30 GiB in 10 yrs).
  * Trade‑offs: witness‑carried proofs cause staleness & RPC reliance; alternatively charge up‑front gas (7702 model) or maintain recent block history to update proofs client‑side.
  * Networking limits: payloads >512 kB slow gossip; validator bandwidth cap 900 KB/s; need to watch additive overhead of proofs + ILs.

* **AA complication**

  * Full AA validation may need arbitrary state; stateless includer can’t guarantee.
  * Ideas: cap validation gas, restrict scheme, or use block hints for touched storage. \[UNCERTAIN] Possible correction: further work on “transaction‑supplied witnesses” plus short block‑history diffing.

* **zkFOCIL design**

  * Replace BLS signature with *linkable ring signature* + key image.
  * Key ring = all validator pubkeys; committee elected by hashing hidden key images.
  * Security: anonymity, unbiased selection, linkability prevents grinding.
  * Prototype (Reya grant):
    * Key‑image+proof generation <2.5 s (offline)
    * Verification 87 ms (needs 16× faster to check 16 ILs)
    * Proof size ≈500 B.
  * Open items: optimisation, key‑image reset cadence, validator‑set churn, network anonymity layer.

* **Future‑of‑nodes vision**

  * Three roles: Attester (heavy), Builder (resource‑intensive), Includer (light).
  * Hardware spectrum: data‑centre ↔ home server ↔ phone/browser.
  * Light FOCIL: permissionless includer registry (deposit‑less, balance‑weighted, delegate‑able, non‑slashable).
  * Need to match new node types with zkEVM proofs & DAS era; browser‑extension includer with default anonymity is aspirational.

* **Discussion points & Q\&A highlights**

  * Inclusion of invalid txs: tested block is re‑orged (current design); future designs differ under delayed‑exec/ePBS.
  * Incentives: rewarding small nodes risks capture; default is no reward, rely on altruism/reputation.
  * zkFOCIL + light FOCIL integration challenging (dynamic set, proof latency).
  * Privacy vs. storage: key‑image uniqueness ties to pubkey; validator exits/entries imply periodic regeneration.