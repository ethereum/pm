## Resources

- [Pre-read](https://ethresear.ch/t/native-rollups-superpowers-from-l1-execution/21517) [[PDF](Slides-notes/12-Jun-native-rollups-preread.pdf)]

## Human-generated notes

- [Notes from Ladislaus](https://docs.google.com/document/d/1Ln1zXUOmUFEKaemfrK8oAROYfDL_HwFQP-fYItTVfMM/edit?tab=t.0) [[PDF](Slides-notes/12-Jun-native-rollups-notes.pdf)]

## AI-generated notes

### Summary

* **Goal of proposal — “native roll‑ups”**: expose the L1 EVM state‑transition function (STF) to L2s through a new `EXECUTE` precompile so an L2 can *re‑use* Ethereum’s execution rather than re‑implementing it, thereby inheriting full Ethereum‑grade security and eliminating most Security‑Council and governance attack surface.
* **Four‑layer model**: settlement, data availability, sequencing, execution. A roll‑up that re‑uses *all four* layers becomes an “ultrasound” roll‑up; one that re‑uses only execution becomes a “native” roll‑up.
* **Security motivation**: present roll‑ups carry three vulnerabilities—implementation bugs in custom EVMs/Fraud‑/ZK‑proof circuits; emergency multisig compromise; and perpetual governance overhead to track EVM hard‑forks. Native roll‑ups remove (or sharply reduce) all three.
* **Usability motivation**: launching an EVM‑equivalent roll‑up should drop from nine‑figure engineering budgets to “a few lines of Solidity” that call the precompile; synchronous composability between L2s also improves.
* **`EXECUTE` precompile interface**: inputs = `preStateRoot`, `postStateRoot`, `transactions` (+ witnesses), optional `gasUsed`; returns `true/false` iff stateless execution of the supplied tx set over `preStateRoot` yields `postStateRoot` and (optionally) the supplied gas figure.
* **Subjective verification**: until an enshrined zkEVM lands, each validator chooses either (a) stateless re‑execution or (b) verifying off‑chain ZK proofs; strategy diversity is *inside* each operator.
* **Gas cost**: calldata/blob bytes are still paid for, but `EXECUTE` itself can be constant‑cost; with “same‑slot proving” the *execution* gas limit for native roll‑ups can be effectively unbounded while L1 execution remains bounded.
* **Horizontal vs vertical scaling**: once the L1 is zk‑proven (“Snarkify L1”) gas limit can climb toward \~1  gigagas/s (vertical); native roll‑ups add another \~1  teragas/s horizontally across \~1000 L2s.
* **Roadmap**:

  1. **Snarkify L1** → raise gas limit (60 M → 100 M → 300 M … 1 G)
  2. Expose `EXECUTE`; early adopters use subjective proof diversity
  3. Standardise derivation pipeline (possible `DERIVE` precompile)
  4. Long‑term: enshrine a single zkEVM, enable native validiums
* **Trade‑offs / exclusions**: only EVM‑equivalent roll‑ups qualify; no support for Cairo/SVM/Move, non‑EVM features like Stylus‑wasm, or validiums (until step 4). Roll‑ups that deviate only “10 %” from EVM likely migrate; truly novel VMs (>10× better) will remain separate.
* **Open concerns**: DOS considerations in the mempool, standardising blob ↔ tx conversion, proof‑diversity policy, migration path for existing roll‑ups, and whether forcing homogeneity slows minor innovation.

---

### Chronological notes

* Intro; room survey on understanding of native roll‑ups → decide to cover basics *and* advanced topics.
* **Terminology mental model**

  * Four layers per chain: settlement / data / sequencing / execution.
  * L2 vs L1 depends on settlement; roll‑up vs validium/optimium on data; “based” vs non‑based on sequencing; “native” vs custom on execution.
  * “Ultrasound” roll‑up = reuse all four.
* **Problem statement** — security weaknesses today

  * Custom zkEVM / fraud‑proof bugs inevitable.
  * Security‑council multisigs social‑engineering risk (examples of lax Telegram signing).
  * Governance required to track hard‑fork opcode changes exposes token‑holder capture.
* **Aspirations**

  * *World‑War‑III‑grade* security by inheriting mainnet EVM.
  * Lower cost/complexity of launching L2s; “few lines of Solidity.”
  * Dramatically simpler synchronous composability because L2 can “cheat” like L1 (delayed state‑root verification).
* **High‑level bifurcation prediction**

  * Bucket 1: EVM‑equivalent roll‑ups become native (no‑brainer).
  * Bucket 2: VMs with ≥10× advantage (e.g. SVM, Cairo, FHE) stay external.
  * Middle‑ground (minor tweaks) hollowed out.
* **`EXECUTE` precompile details**

  * Inputs: preRoot, postRoot, txs (+ Merkle witnesses), optional gasLimit.
  * Output: boolean success.
  * Tx bytes can reside in calldata or blobs; only *availability* required.
  * Standard tx encoding likely RLP; unpacking/compression handled by separate “`DERIVE`” precompile or host contract.
* **Witness size considerations**

  * Optimistic roll‑ups: `EXECUTE` used only in dispute → witness overhead negligible.
  * ZK roll‑ups: witnesses snark‑compressible except for leaf nodes; \~10–20 % overhead estimated.
* **Deposits / context**

  * Deposits handled either by repurposing existing beacon‑chain deposit logic or pre‑processing them in derivation pipeline before `EXECUTE`.
  * Extra context (e.g. block header, gas price) can be injected as additional trace data.
* **Implementation / enforcement**
  1. **Subjective re‑execution**
     * Validator downloads txs & witnesses; statelessly replays.
     * Limited by own gas limit (e.g. 10 M) → checkpoints needed for optimistic roll‑ups’ fraud proofs.
     * Requires storing blobs if blobs used.
  2. **Subjective proof verification**
     * Validator fetches zk proofs from chosen zkEVMs; cheap, parallelisable.
     * Enables effectively unbounded gas per L2 block and “teragas” aggregate.
* **Gas economics & incentives**

  * Data still costs (blobs / calldata).
  * `EXECUTE` call itself can be constant (\~1 k gas) independent of trace size.
  * Same‑slot proving aligns proposer & prover; proposer won’t include tx unless proof already available, eliminating griefing DOS.
* **Vertical‑then‑horizontal roadmap**

  * Snarkify L1 first; raise gas limit (target path: 60 M → 100 M → 300 M → 900 M → 2.7 G → 1 G gas/s over \~6 yrs).
  * Re‑use same tech for `EXECUTE` to reach \~1 T gas/s across L2s.
* **Migration strategy for existing roll‑ups**

  1. Decouple EVM core from derivation pipeline.
  2. Swap core for `EXECUTE`; retain custom derivation (initial security gain).
  3. Community converges on standard derivation → `DERIVE` precompile.
  4. Optionally formally verify tiny bespoke derivation if not standardised.
* **Potential simplification**: if blobs deprecated in favour of calldata, `DERIVE` may do little more than unzip RLP‑encoded L2 blocks.
* **Vertical‑scale only?** `EXECUTE` also usable to ZK‑prove *L1* blocks (Gigagas L1 vision) before being leveraged by L2s.
* **Native‑validium future**: once proofs are on‑chain (enshrined zkEVM) `transactions` argument can be dropped and only (`preRoot`, `postRoot`, `proof`) kept, enabling data‑off‑chain native validiums.
* **Shared sequencing & composability**

  * Base + native roll‑up combo + delayed execution ⇒ next‑slot real‑time proving ⇒ synchronous flash‑loan–style flows across L2s.
  * Same‑slot proving (multi‑year) would further tighten composability.
* **DOS & mempool discussion**

  * Need new tx type with upfront `EXECUTE` inputs/proof so builders can simulate cheaply.
  * Otherwise adversary could tack large trace onto a normal tx late in execution. \[UNCERTAIN] Possible correction: also solvable by mempool rules limiting `EXECUTE` without proof.
* **Proof‑diversity policy**

  * Option 1: validators locally require *k‑of‑n* proofs from curated list.
  * Option 2 (future): single enshrined verifier, simpler but waits for fully verified, stable zkEVM.
* **Inter‑VM gap (e.g. Stylus wasm)**

  * Short term: excluded.
  * Long term: expose lower‑level ISA (e.g. RISC‑V) underneath EVM so alt‑VMs can compile to it; still needs formal verification to avoid governance.
* **Innovation concerns**

  * Native roll‑ups commoditise execution; small EVM tweaks no longer worth it.
  * Experimental “canary” L2s with Security Councils may still thrive for rapid iteration.
* **Session close**: recap, invitation to continue discussion offline; next presentation starts.

