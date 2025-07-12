## Resources

- [Pre-read](https://hackmd.io/@Nerolation/BJcGve7Mll) [[PDF](Slides-notes/10-Jun_block-level-access-lists-preread.pdf)]
- Slides - [Block-level Access Lists](https://docs.google.com/presentation/d/1kWlWez8z5lwC_oCjWUnGSOEt5_4aUDzSrshKN-5IRRk/edit?slide=id.g2fc552e0e46_1_692#slide=id.g2fc552e0e46_1_692) [[PDF](Slides-notes/10-Jun_block-level-access-lists-slides.pdf)]

## Human-generated notes

[Notes by Bosul](Slides-notes/10-Jun_block-level-access-lists-notes-bosul.pdf)

## AI-generated notes

<sup>[prompt](Slides-notes/AI-info.md)</sup>

### Summary

* **Purpose of session** – review the goals, open design space and current EIP‑7928 draft for *block‑level access lists* (BLAL), then collect client & researcher feedback.
* **Motivation** – current worst‑case execution is fully sequential; BLAL aim to unlock deterministic parallel execution (and eventually IO/execution overlap) by providing an up‑front map of all state touched in a block.
* **Specification snapshot** – EIP‑7928 adds an aggregated `block_access_list` object to the block body (hash stored in the header). The object contains:

  * a de‑duplicated set of `(address, storage‑slot)` pairs (“storage locations”), and
  * a *state diff* (writes to storage, nonces, balances, code).
    Builders must populate it; validators treat stepping outside it as an invalid block.
* **Design variants discussed** –

  * storage locations only
  * storage locations + *post‑transaction* values (current draft)
  * *pre‑transaction* values (gives IO/execution overlap)
  * full pre‑ or post‑block state.
* **Key trade‑off** – pre‑transaction values enable maximal parallelism but explode worst‑case size (≈1.5 MB @ 36 M gas); post‑values keep size below today’s worst‑case calldata (≈0.9 MB) while still enabling perfect parallel execution once IO is finished.
* **Average size today** – with the draft (storage locations + state diff) a typical main‑net block would carry \~40 kB of BLAL data.
* **Encoding & compression** – SSZ chosen over RLP for its better overhead on small lists; structure `(account → slot → txIndices)` de‑duplicates repeated touches. Further ideas: pointer‑back‑references into call‑data, excluding trivially derivable nonce diffs, etc.
* **History & networking** – worries about chain bloat led to ideas of (i) expiring BLAL after a rolling window, or (ii) moving the payload to a sidecar while keeping the hash in the header. Both remain open questions.
* **Secondary benefits** – deterministic pre‑fetch, faster state‑root computation, sync “healing” during snap sync, lighter zkEVM verification, foundations for execution sampling, and potential alignment with FOCIL & compute‑gas repricing.
* **Next steps** – prototype clients (Geth, Besu) are underway; concrete benchmarks will decide whether to keep locations‑only, keep full state diff, or adopt other optimisations before targeting the Glamsterdam upgrade.

---

### Chronological notes

* Intro: the proposal is \~6 months old; aim of the session is a 10 min refresher then 40–50 min open discussion.
* **Current execution diagram** – worst‑case “gun‑chart” is fully sequential; optimistic pre‑fetch already helps but fails in adversarial blocks.
* Vision diagrams shown:

  * ideal parallel execution of *N* transactions on unlimited cores;
  * ideal overlap of IO & execution if pre‑state is known.
* **What BLAL adds** – perfect knowledge of touched state → validator can execute Tx n before Tx n‑1 as long as accesses don’t conflict.
* **EIP‑7928 layout** – block body holds the list, header stores its hash; any deviation during execution is invalid. Builders find it trivial to emit; validators reap the gains.
* **Design space axes**:

  * *Which data?* storage locations ▸ storage values ▸ full state diff.
  * *When?* pre‑block, post‑block, pre‑tx, post‑tx.
* **Why post‑tx values were chosen (draft)** – lets validators parallel‑execute once IO done; avoids shipping all SLOAD values; size remains below calldata ceiling.
* **Pre‑tx values discussion** – would let IO and execution proceed in parallel but balloons size (SLOAD‑dominated worst case ≈1.51 MB at 36 M gas).
* Size table presented:

  * post‑values worst case ≈0.91 MB (SSTORE‑dominated).
  * pre‑values worst case ≈1.51 MB (SLOAD‑dominated).
* Question: Do repetitive touches bloat size? → de‑duplication via mapping ensures each `(address,slot)` appears once regardless of how many Txs use it.
* Concern: average history growth rises because current calldata blocks are *below* worst‑case; BLAL brings average closer to worst‑case. Could coincide with planned *history expiry* work.
* Idea: keep BLAL only for last *k* blocks or regenerate on demand; pushback that full validation needs list at sync time.
* Alternative: make BLAL a *sidecar* object (hash still in header) so it can expire independently; needs networking tweaks but attractive for bandwidth.
* **Encoding choice** – SSZ gives smaller output than RLP on many single‑value lists; keeps hash deterministic.
* **Full‑state diff merits**: allows parallel state‑root calc; lets lightweight nodes accept zkEVM proofs without re‑execution; could aid snap‑sync healing.
* Objection: must also include code writes to be truly “full state”; code size gas‑bound means worst‑case still reasonable (\~160 kB for 7 max‑size contracts).
* Suggestion: cap number of writes per block or use progressive gas multipliers to contain size; flagged as out‑of‑scope but worth research.
* **Micro‑optimisations floated** –

  * skip nonce diffs that can be inferred;
  * reference values already present in calldata via back‑indexes;
  * encode rights only, rely on optimistic read‑prefetch; risks re‑introducing worst‑case.
* **Potential new functionality** – partial execution sampling (validators attest to subsets); needs conflict‑free partitioning and stronger fork‑choice integration. Marked as speculative.
* **Implementation status** – Geth ahead, Besu in progress; Erigon interested. Benchmarks will decide whether to retain storage‑location section or slim down. Target upgrade: Glamsterdam (timeline TBD).
* Closing: consensus to gather real numbers on clients/testnets before finalising data fields, encoding or expiry strategy.

---

### Relevant links

* EIP‑7928 draft – [https://eips.ethereum.org/EIPS/eip-7928](https://eips.ethereum.org/EIPS/eip-7928)
* EthResearch thread – [https://ethresear.ch/t/block-level-access-lists-bals/22331](https://ethresear.ch/t/block-level-access-lists-bals/22331)
* Glamsterdam proposal - [https://ethereum-magicians.org/t/eip-7928-block-level-access-lists-the-case-for-glamsterdam/24343](https://ethereum-magicians.org/t/eip-7928-block-level-access-lists-the-case-for-glamsterdam/24343)
