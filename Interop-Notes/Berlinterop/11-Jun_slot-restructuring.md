## Resources

- [Pre-read](https://notes.ethereum.org/@ralexstokes/berlinterop-shorter-slot-times) [[PDF](Slides-notes/11-Jun_slot-restructuring-preread.pdf)]

## Human-generated notes

- [Notes by Alex](Slides-notes/11-Jun_slot-restructuring-notes-alex.pdf)
- [Notes by Shantikiran](Slides-notes/11-Jun_slot-restructuring-notes-shantikiran.pdf)

## AI-generated notes

<sup>[prompt](Slides-notes/AI-info.md)</sup>

### Summary

* **Today’s slot anatomy:** a 12 s slot contains three critical sub‑events—block proposal (≈0 s), attestations (≈4 s) and attestation aggregation (≈8 s). Execution‑layer (EL) payload verification and gossiping happen in parallel with these windows.
* **Problem statement:** the first half of the slot is CPU‑ and bandwidth‑intensive while the back half is mostly idle, causing bursty network load, validator “stampedes” at 4 s and higher miss‑rates in slot 0 of each epoch.
* **Two incremental fixes were highlighted**

  1. *Duty‑rebalancing PR*: shift attestation deadline from 4 s → 6 s and aggregation deadline to +3 s, while strongly encouraging “attest‑on‑validation” instead of “attest‑at‑4 s” to spread traffic.
  2. *Spec refactor*: express all duty offsets as millisecond constants so slot geometry can be tuned and fuzz‑tested more easily.
* **Shortening the global slot time (e.g., 12 s → 6 s)** would lower UX latency, cut time‑to‑censorship‑resistance and tighten pre‑confirmation loops, but requires invasive changes to fork‑choice tests, epoch processing, client databases and bandwidth budgets.
* **Delayed execution (EIP‑7886)** moves EL execution and builder work *after* attestations, freeing more time for block propagation while keeping 12 s slots.
* **ePBS (EIP‑7732)** separates the beacon block from the EL payload; only the small beacon block must traverse the network before attestations, the (potentially large) encrypted payload can propagate afterwards, removing relay trust at the cost of sequential latency.
* **Slot‑layout trade‑off visualised:** four timelines were compared—current, re‑balanced, “rebalance + delayed execution”, and ePBS—with color‑coded bandwidth vs CPU windows. Opinions diverged on whether ePBS “wastes” early‑slot bandwidth and how encryption or erasure‑coding could mitigate that.
* **Builder timing reality check:** builders already game the deadlines by proposing as late as possible; any extra head‑room will be exploited unless attestation and “late‑block” rules are tightened.
* **Scaling economics:** shorter slots (even with proportionally lower gas limits) still improve DEX arbitrage spreads, pre‑conf UX and validator censorship windows; finality can be layered via “safe‑head” rules.
* **Immediate action items agreed:**

  * Merge the spec refactor/duty‑rebalancing constants PR.
  * Make “attest as soon as block is validated” a *hard* spec rule (remove optional 4 s path).
  * Draft an EIP for attestation‑deadline/aggregation‑deadline changes so it can ship independently, potentially in the Glamsterdam upgrade.
* **Long‑term coordination:** pick a slot architecture first (status‑quo with rebalancing, delayed execution, or ePBS) and *then* design a slot‑time reduction; otherwise testing complexity explodes.
* **Future research tasks:** gossip‑mesh optimisation, CL‑driven gas‑limit hints to the EL, state‑pruning at non‑critical slots, and encrypted payload techniques for ePBS.

---

### Chronological notes

* Overview of current 12 s slot and sub‑slot timings.

  * Proposal at 0 s → attest at 4 s → aggregate at 8 s.
  * Execution‑layer payload validation is on the critical path.

* **Motivations to shorten slots**

  * Smoother UX, lower latency for interop, faster censorship‑escape.
  * Major risk: the `SECONDS_PER_SLOT` constant is deeply embedded; few clients support dynamic changes.

* **Motivations to keep 12 s but *rebalance* duties**

  * Observation: last 4–8 s of slot are mostly idle; earlier half is overloaded.
  * PR (“duty‑rebalancing”) proposal:
    * Extend attestation deadline to 6 s, aggregation deadline to 9 s.
    * Require clients to broadcast attestations immediately after validation (no 4 s stampede).
    * Timings chosen heuristically; must preserve tolerance for geographically distant nodes.

* Internal client work that could free earlier‑slot CPU:

  * Move database pruning away from slot 0 (do it in later slots).
  * Reduce epoch‑transition hashing by eliminating obsolete validator keys and rethinking `max_effective_balance` touches.
  * Perform epoch processing before block processing inside the client.

* **Builder / relay timing concerns**

  * Market competition already delays block publication; extra slack will be consumed.
  * Late‑block rule (`late≥2 s`) can be tightened independently of attestation windows.

* **Four slot‑layout sketches (white‑board diagram)**

  1. **Status‑quo** – proposal/attn/agg tightly packed; execution + propagation overlap.
  2. **Adjusted sub‑division** – more purple bandwidth window, slightly more green execution window.
  3. **Adjusted + delayed execution (EIP‑7886)** – attestations first, execution after; splits slot into bandwidth‑then‑CPU.
  4. **ePBS (EIP‑7732)** – beacon block propagates first; encrypted EL payload propagates after attestation; small PTC committee checks availability.
     * Debate: early portion “wasted” for throughput unless payload is pre‑propagated with encryption/erasure coding.

* **Builder reality**

  * Many CL clients start EL block building only after slot start; empirical 1–1.5 s to build beacon block.
  * Builders receive blocks directly from proposers; attestation arrival mostly determines their “win” decision.

* **Encrypted payload discussion**

  * Simple symmetric encryption or erasure‑coded scheme could let builders ship payload chunks before attestations, avoiding ePBS latency tax.
  * Must still satisfy gossip validation and avoid unbundling risk.

* **Time‑to‑censorship‑resistance, pre‑confs, finality**

  * Three latencies matter: pre‑confirmation, censorship escape, and finality.
  * Slot‑time halving improves all three simultaneously, whereas pre‑confs alone don’t cut censorship window.
  * Shorter slots benefit DEX LPs by reducing informed‑flow losses, though the exact profit function is debated.

* **Spec‑level incremental steps**

  * Refactor constants to milliseconds; merge immediately.
  * Remove “wait‑to‑4 s” attestation path; enforce attest‑on‑validation.
  * Create an EIP to codify attestation=6 s, aggregation=9 s and ship in Glamsterdam if nothing bigger lands.

* **Implementation / testing cautions**

  * Changing slot length is a “major fault feature”: affects fork choice tests, DB layouts, epoch‑transition load.
  * Must design in tandem with 7732/7886 to avoid re‑work; roll‑outs could be phased (rebalance → architecture change → slot‑time shrink).

* **Additional open items**

  * Research erasure‑coded gossip mesh for faster propagation.
  * Investigate “CL informs EL of max propagatable gas limit” mechanism (issue previously opened).
  * Aggregate propagation currently <1 s; plenty of slack if attestation window is shifted.
  * Difficulty‑bomb‑style “single issue” forks are discouraged; bundle with broader upgrades.
  * Safe‑head rules already give near‑instant execution certainty for some L2s; wider promotion encouraged.

---

### Relevant links

* **EIP‑7732** – “Beacon‑block proposer / builder separation (ePBS)” – [eips.ethereum.org/EIPS/eip-7732](https://eips.ethereum.org/EIPS/eip-7732)
* **EIP‑7886** – “Delayed Execution” – [eips.ethereum.org/EIPS/eip-7886](https://eips.ethereum.org/EIPS/eip-7886)