## Resources

- [Pre-read](https://ethereum-magicians.org/t/eip-7938-exponential-gas-limit-increase-via-default-client-voting-behavior/23884/13) [[PDF](Slides-notes/09-Jun-ethereum-scaling-planning-preread.pdf)]

## AI-generated notes

### Summary

* **Goal of the workshop**: establish a repeatable “scaling loop” so that raising Ethereum’s L1 gas target becomes routine rather than ad‑hoc; identify bottlenecks early, classify them, and pick the right mitigation path .
* **Three mitigation paths** were defined:

  1. *Pure engineering*—client‑side optimisations that need no fork.
  2. *Containment tweaks*—quick, late‑stage fork items such as an un‑compressed block‑size cap or opcode repricing that shield the network while other work continues .
  3. *True protocol redesigns*—e.g. slot‑re‑architecture, block‑access lists, Tx‑Gas‑Cap, ePBS—needed when bandwidth/CPU limits are genuinely hit .
* **Timeline split into three stages**:

  * *Now → Glamsterdam (≈ Q4‑25)* – no more scope added to Fusaka; all scale comes from client tuning + containment.
  * *Glamsterdam → ≈ 2027* – introduce one or more protocol upgrades that attack the next blockers empirically.
  * *≥ 2027* – zkEVM‑enabled era where execution/state/data constraints are fundamentally re‑architected .
* **Parallelisation called a “missing big theme.”** Full deterministic parallel execution (block‑access lists, optimistic concurrency, long access lists) will need both protocol specs and client work .
* **Performance dashboard launched.** Each EL client has a dedicated *performance* branch; worst‑case single‑opcode benchmarks must clear **≥ 20 Mgas/s** by week’s end, else the 60 Mgas main‑net target is unsafe .
* **Benchmarking stack details**: containerised Engine‑API harness deploys a contract, replays 30‑150 invocations, normalises results, stores in Postgres, and renders live charts; “warming” mode (1 000 blocks) being added for JVM/.NET clients .
* **Devnet‑1 & main‑net shadow‑fork load‑tests** already spiked to 100 Mgas; incidents surfaced CPU and state‑tree edge‑cases, validating the toolchain’s usefulness .
* **State‑tree access identified as separate bottleneck.** Teams asked to design multi‑opcode *state* micro‑benchmarks and worst‑case main‑net traces; today’s CPU‑centric charts “optimise the non‑bottleneck” for some clients .
* **Propagation & fork‑choice stress** must be co‑analysed on the CL side; idea floated for CL to signal an upper gas bound that remains safely propagatable across the network .
* **Target‑setting debate**: at 60 Mgas, a three‑second validation window implies clients need \~20 Mgas/s; for 100 Mgas it rises to 33 Mgas/s—these numbers will steer each client’s performance goals .
* **Security‑layer to‑dos**: integrate re‑org scenarios, state+CPU combos, and RPC‑tip latency tests; agree on a worst‑case block‑processing timeout (currently 2 s in Geth/Erigon) .

### Chronological notes

* **00:00–00:03 Ansgar** – framing: L1 throughput flat for \~5 years; want a **continuous feedback loop** for safe, stepwise increases .
* **Loop breakdown**

  * *Detect* impending blockers via visibility tooling.
  * *Classify* into engineering vs containment vs redesign .
  * *Respond* quickly—small cuts (e.g. blob uncompressed cap) can merge late in a fork if needed .
* **Timeline whiteboard**

  * **Phase 1 (pre‑Glamsterdam)**: protocol frozen; only optimisation/containment possible.
  * **Phase 2 (post‑Glamsterdam)**: introduce protocol changes chosen from evidence.
  * **Phase 3 (≥ 2 yrs)**: zkEVM resets constraints but raises node‑type heterogeneity issues .
* **Parallelisation “big missing theme”** – optimistic exec already exists; deterministic parallelism needs block‑access lists, state‑diffs, gas repricing; heavy coordination between spec writers and client teams .
* **Benchmark/Perf tooling demo (Pari & Speaker 8)**

  * Containers spin up EL node, deploy contract, spam opcode N calls, normalise gas‑per‑second output.
  * Supports *warming* (1 000 mixed‑tx blocks) to stabilise JVM/C# jit effects.
  * Results shipped to Postgres; Grafana dashboard auto‑refreshes; perf‑branches run hourly CI .
* **Interpretation** – e.g. Besu 10.4 Mgas/s means a 60 Mgas block takes ≈ 6 s: “scenario we never want” .
* **Shadow‑fork load tests** – Devnet‑1 + main‑net fork pushed ↥100 Mgas; surfaced engine timeouts and state‑trie latency spikes .
* **State vs compute debate (Felix, Speaker 11)**

  * Compute‑only benchmarks miss trie‑heavy paths; need blended tests.
  * Gas schedule can shift compute‑vs‑state balance; repricing will recur .
* **Performance targets** – every client must hit ≥ 20 Mgas/s worst‑case this week; stretch goal 33 Mgas/s for 100 Mgas future; dashboard bars should rise with higher gas cap .
* **Propagation & fork‑choice coupling** – need CL metrics; suggestion: CL advertises max safe gas per block based on recent bandwidth observations .
* **Containment examples under consideration**: opcode repricing (MODEXP done), multidimensional pricing sketch, default builder logic to avoid pathological blocks .
* **Action items**

  * Client teams push optimisations to *performance* branch; dashboard auto‑confirms.
  * Research group to craft state‑heavy benchmarks & main‑net worst‑case traces.
  * Decide acceptable block‑processing timeout and integrate into perf tests .

### Relevant links

* EIP‑7825 “Transaction‑Gas‑Cap” – [eips.ethereum.org/EIPS/eip-7825](https://eips.ethereum.org/EIPS/eip-7825)
