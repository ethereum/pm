## Resources

- Slides - [zkday](https://docs.google.com/presentation/d/1U0w2GthAj71NcKCguqj8nQCtGqxgC8g1Y2KrkkH4prg/edit?usp=sharing) [[PDF](Slides-notes/11-Jun_zkday-kickoff-slides.pdf)]

## AI-generated Notes

<sup>[prompt](Slides-notes/AI-info.md)</sup>

### Summary

* Ethereum Foundation’s R\&D cluster has reorganised around a strong zkEVM focus; multiple sub‑teams (stateless consensus, formal verification, prototyping) now funnel effort into L1‑scale proving and integration work
* **Ambition: “Giga‑gas L1”** — raise the block‑gas target to ≈ 1 Ggas · s⁻¹ (≈ 10 k tx/s) over six years, outpacing the earlier 3×‑per‑year schedule (EIP‑7937)
* **Key enabler for latency at high gas**: Transaction Gas Cap (EIP‑7825) in Fusaka (2025) splits large blocks into parallel‑executable 30 Mgas “mini‑blocks,” yielding ≥ 100× execution concurrency at end‑state volumes
* Real‑time zk‑proving is considered “solved” for today’s 15 Mgas blocks (≈ 16 RTX 4090‑seconds); exponential prover progress and perf‑testnets showing ≥ 6 Ggas/s validate the scaling head‑room
* **Four‑phase integration path for zkEVM proofs:**
  0\. *Altruistic Mode* (2025; no fork) — validators wait for off‑chain proofs, accepting minor reward loss.

  1. *Delayed Execution* — L1 forks to insert a 1‑slot lag, masking most reward penalties.
  2. *Mandatory Proofs* — block validity requires an attached proof; builders risk loss of fees/ collateral.
  3. *Enshrined Proofs* — formally‑verified zkEVM byte‑code lives on‑chain, enabling “native validiums.”
* **“Same‑slot proofs” supersede the older *block n+1 proves block n* design, eliminating incentive mis‑alignment and “proof‑killer” blocks by having the builder publish a proof before the next proposer step**
* **FOCIL (Fork‑Choice enforced Inclusion Lists)** and ‘includer’ nodes protect censorship‑resistance while the gas grows; the forced‑include portion may keep a much smaller gas cap to avoid creating proof‑killers
* **Power budget target**: < 11.5 kW‑class “office clusters”; roadmap banks on 10–50× software plus hardware efficiency and optional distributed proving to stay inside the envelope
* **Open‑source GPU provers and permissive dual licensing** (MIT/Apache‑2) are flagged as *mandatory* for broad validator adoption; three prover stacks are already public
* **Validator‑side security model shifts to *k‑of‑n* proof diversity**: each node listens to multiple gossip channels and attests when ≥ k proofs agree, mitigating correlated zkEVM faults and LLVM/compiler monoculture risks
* **Guest‑client diversity roadmap**: migrate beyond REVM by running gEVM, EVM‑one, Nethermind‑EVM on RISC‑V/MIPS/64‑bit DSL back‑ends; avoids single‑implementation fragility
* **Database & networking “secondary bottlenecks”** now receive attention (e.g. Coinbase’s 8× LevelDB replacement, Perf‑net stress‑nets) because proving has ceased to dominate scaling limits
* **Proof‑size workstream**: prefer small “intermediate” proofs over recursion; explore ETH‑specific Halo 2 wrappers or optimised intermediate‑proof circuits to cut calldata overhead without trusted setup

---

### Chronological notes

* **Kick‑off & context**

  * ZK Day convenes researchers, client devs and zkEVM teams at Berlinterop; EF has restructured R\&D as “Protocol” with a dedicated zkEVM squad and \$20 M formal‑verification budget
* **Vision statement**

  * Goal: 1 Ggas/s L1 (\~10 k tx/s @ 100 k gas/tx) by stretching Dankrad’s 3× yearly gas cadence over six years instead of four
* **Gas‑limit scalability analysis**

  * Distinguishes *unsophisticated* actors (wallets, validators, includers) from *sophisticated* builders/RPCs
  * Real‑time zk‑proving breakthroughs relegate the unsophisticated CPU bottleneck; remaining work is “plain engineering” on DB IO and networking
* **EIP‑7825 (Tx Gas Cap) & parallel mini‑blocks**

  * 30 Mgas cap inside 60 Mgas blocks → 2× today; translates to \~100× parallelism at 1 Ggas in 3 s slots
* **Perf‑nets & DB work**

  * Coinbase 8× faster state DB (private for now); perf‑nets hitting 6–24 Ggas/s; estimate 10 Ggas/s head‑room after EVM tuning
* **Roll‑up‑centric v2 roadmap**

  * Stronger L1 acts as hub while multiple L2s also reach 1 Ggas; cumulative ≈ 1 Tgas ecosystem
* **Phase‑based zkEVM integration**

  * *Phase 0* (2025): validators optionally wait for altruistic proofs, absorb minor reward loss
  * *Phase 1* (Delayed Execution): 1‑slot lag masks latency; proof‑killer risk remains
  * *Phase 2* (Mandatory Proofs): proof absence invalidates block; builder stakes/fees at risk; addresses killers
  * *Phase 3* (Enshrined Proofs): formally‑verified zkEVM code lives on‑chain enabling native validiums
* **Same‑slot proofs mechanics**

  * Builder must publish proof < Δ≈1 s before next‑slot proposal; validators check off‑chain availability; reduces proving window to 11 s but kills mis‑alignment
  * Forced‑inclusion sub‑block (FOCIL) may keep a much lower gas cap to avoid inserting killer txs
* **Power & hardware envelope**

  * Current RISC‑V zk‑EVM ≈ 4 W executor ↔ 100 k× power in GPUs; target < 11.5 kW office cluster; expect 10–50× SW/HW gains plus distributed proving as fallback
* **Open‑source & licensing requirements**

  * GPU cluster orchestration code must be FOSS (MIT/Apache‑2); three stacks already public; EF tracker will add an OSS column
* **Proof‑size & wrapping options**

  * EthProofs urges teams to submit larger “intermediate” proofs (no recursion, no trusted setup); research open for ETH‑specific Halo2 wrapper or smaller intermediate proofs for calldata savings
* **Validator security via proof diversity**

  * Each node subscribes to *n* proof gossip topics; attests when ≥ k proofs agree; reduces correlated failure risk; “low‑resource Vouch” analogue
  * LLVM monoculture flagged; insist on multiple backend DSLs (SP‑1 Hyperplonk, Risc Zero V3) to avoid common‑mode bugs
* **Guest‑client / ISA diversity plan**

  * gEVM, EVM‑one, Nethermind‑EVM etc. compiled to RISC‑V, MIPS‑64 or custom DSLs; encourages new client teams without quadratic proof blow‑up (pairing or “multi‑EVM proofs”)
* **Database & state access future**

  * Partial‑state nodes + access‑list blocks + erasure‑coded history proposed to keep light nodes viable at 1 Ggas; state‑expiry flavours under evaluation
* **Proof‑network economics & centralisation**

  * Builders may delegate to external prover markets; diversity enforced socially (grants, libs) and by k‑of‑n validation; non‑enshrined proofs remain viable for decades if incentives suffice
* **Open discussion themes**

  * Optimality vs adaptability; leanness hides ZK complexity; block‑builder pipeline still needs robustness; how many proofs *k/n* is enough; incentives for diversity; fallback liveness if GPU fleet fails
