## Resources

- [Pre-read](https://notes.ethereum.org/@Ladislaus/ByNXBMyQlx) [[PDF](Slides-notes/10-Jun_lean-ethereum-preread.pdf)]
- Slides - [Lean ethereum, Vitalik](https://docs.google.com/document/d/1GYrv43uD030ZipLoFmTRnLoz0-EkRpA-3q9mDChHKO8/edit?tab=t.0) [[PDF](Slides-notes/10-Jun_lean-ethereum-slides-vitalik.pdf)]
- Slides - [lean ethereum, Justin Drake](https://docs.google.com/presentation/d/1WrElBUZ4duyY9SsmxWn6SeflrnUUYjejHEBxjccDnz8/edit) [[PDF](Slides-notes/10-Jun_lean-ethereum-slides-Justin.pdf)]

## Human-generated notes

- [Notes by Ladi](https://docs.google.com/document/d/1GYrv43uD030ZipLoFmTRnLoz0-EkRpA-3q9mDChHKO8/edit?tab=t.0)

## AI-generated notes

<sup>[prompt](Slides-notes/AI-info.md)</sup>

### Summary

* **“Lean Ethereum” replaces the former *Beam Chain*** name and frames a long‑term redesign of Ethereum L1 around three pillars: security, simplicity and optimality.
* The initiative splits into three parallel tracks—**Lean Consensus, Lean Data and Lean Execution (C‑D‑E)**—with an explicit goal of baking in post‑quantum security, minimal hardware requirements and formal verification throughout.
* **Security** is prioritised because L1 settles high‑value activity and underpins every L2; **simplicity** keeps the protocol auditable and lowers the chance of latent bugs; **optimality** (≈ near‑theoretical bounds) is presented as the only credible route to ossification/long‑term stability.
* Research maturity (e.g. Tendermint‑like consensus, 3‑slot finality, hash‑based signatures, ZK tooling) makes 2025 a good moment to consolidate decades‑scale designs.
* **Candidate components** already prototyped in ≤ \~400 Python LOC include 3‑slot finality (3 SF), hash‑based post‑quantum aggregate signatures, a minimal RISC‑V zkEVM, and full‑chain data‑availability sampling that reunifies blobs and calldata.
* **Lean verifiability target:** validate blocks on a \$7 Raspberry Pi Pico using only SNARK verification + DAS; staking should require “zero MEV‑sophistication” by removing proposers/relays via Attest‑Publish‑Shard (APS) and enforcing Fork‑Choice‑enforced Inclusion Lists (FOCIL).
* **Single‑hash philosophy:** Poseidon (or similar) would serve Merklization (SSZ), state root, DAS coding, post‑quantum signatures and zkEVM arithmetic—minimising cryptographic assumptions & tech‑debt.
* **Tech‑debt slated for removal**: sync committees, slot committees, deposit contract quirks, withdrawal credential variants, the entire blob sub‑system, plus large swathes of legacy EVM interpreter code.
* **Formal verification pipeline (“Lean for Lean Ethereum”)** is funded (\~\$20 M) to prove zkEVMs, 3 SF and hash‑based signature libraries; sub‑specs are intentionally tiny to ease full proofs.
* **Synergies with the near‑term (Fusaka/Pectra) roadmap:** FOCIL and APS improve L1 censorship‑resistance while enabling giga‑gas blocks; zkEVM light clients unblock shorter slots & pre‑confirmations; full‑chain DAS is prerequisite for 10–1000× data throughput.
* Community & resourcing: nine new engineering teams joined after the initial Defcon talk, giving a total of \~15 consensus‑client codebases; expectation is future consolidation and/or specialisation (e.g. networking, ZK, signatures).
* **Critiques aired during Q\&A**: claims of “optimality” may be hubristic; ossification must be balanced with adaptability; risk of simply shifting complexity into hard‑to‑audit ZK black boxes; clearer low‑level specs and open prototypes requested.
* Road‑ahead options: incremental back‑porting of Lean components into successive network upgrades **or** a coordinated “big‑bang” specification that replaces major subsystems at once.

---

### Chronological notes

* **Session opening & naming**

  * Initiative formerly called *Beam Chain*; trademark clash led to rename **Lean Ethereum**—a holistic rethink, not just a new consensus chain.
* **Core aims explained**

  * *Security*: L1 is the “world ledger”; L2 safety inherits from it.
  * *Simplicity*: more contributors grok the code; protocol layer should not centralise expertise; removal of empty accounts earlier is cited as a simplicity win that also prevented a 7702 bug.
  * *Optimality*: scaling + latency improvements without trade‑offs; getting “close to theoretical bounds” is the only rational reason to stop changing the protocol.
* **“Why now?”**

  * Consensus research space (Tendermint, optimistic availability, 3‑slot finality, ZK) seen as largely mapped; risk of missing a 10× idea is much lower than 5‑10 years ago.
* **Illustrative Lean candidates**

  * **3‑slot finality (3 SF)**: fast, provably secure (33 % async / 49 % sync attacker bounds); < 400 LOC reference implementation.
  * **Hash‑based post‑quantum ideal signature aggregation**: quantum‑resistant, single hash function, no trusted setup.
  * **zkEVM on RISC‑V**: remove interpreter overhead; devs write directly against prover ISA → ≈ 100× speed‑up.
  * **Lean Data**: trusted‑setup‑free commitments over binary fields; collapse blobs into calldata, erasing the 4844‑era split.
* **Roadmap integration strategies**

  * Piece‑by‑piece inclusion vs. fresh spec drop (e.g. new beacon chain variant replacing many sub‑systems simultaneously).
* **Justin’s expansion—C‑D‑E tracks**

  * **Lean Consensus**: post‑quantum signatures, SNARK‑based light verification, 3 SF, Attest‑Publish‑Shard (APS) to eliminate proposer centralisation.
  * **Lean Data**: **Full‑Chain Sampling (FCS)**—apply PeerDAS‑style sampling to *all* L1 data (calldata + consensus blocks) to unlock large gas increases.
  * **Lean Execution**: enshrine a ZK‑friendly ISA under the EVM; enables native roll‑ups/alliances and horizontal scaling.
* **Design principles enumerated**

  * *Lean verifiability*: \$7 Raspberry Pi or phone sufficient; home/mobile bandwidth assumed.
  * *Unsophisticated staking*: MEV games removed; APS collapses proposer & relay roles.
  * *Minimal assumptions*: migrate off BLS + KZG; single hash (Poseidon) underpins SSZ Merklization, DAS, signatures, zkEVM.
  * *Tiny sub‑specs*: prototypes show 112 LOC for 3 SF, 51 LOC for minimal RISC‑V CPU, 445 LOC for SNARK verifier.
  * *Tech‑debt purge*: eliminate sync committees, slot committees, deposit‑contract oddities, withdrawal BLS keys; treat blobs & much of EVM as debt.
  * *Longevity > ossification*: aim for “close to end‑game” so upgrades become unnecessary pragmatically, not dogmatically.
* **Formal verification commitment**

  * Lean theorem prover (Lean 4) targeted; \$20 M, 3‑year zkEVM proof effort; 3 SF formalisation begun; goal is “full proofs for everything enshrined.”
* **Issuance reform teaser**

  * “Croissant Issuance” proposal to reduce waste as validator participation approaches 80‑90 %.
* **Synergies with short‑term roadmap**

  * *FOCIL* → censorship‑resistant inclusion + enables giga‑gas without self‑builder fears.
  * *zkEVM light clients* → shorter slots, pre‑confirmations, validator hardware cut‑off.
  * *Full‑chain sampling* → prerequisite for 10 ×–1000 × gas growth because legacy calldata is unsampled today.
  * UX‑driven features (faster finality, pre‑confs) align both timelines.
* **Tomasz “five wins” narrative**

  1. Individual L2s beat Solana‑class L1s.
  2. L2s interoperate → strong network effects.
  3. Ethereum becomes liquidity “black hole” absorbing other L1s.
  4. Challenge Bitcoin as SoV.
  5. Tackle global finance / USD.

  * Lean focuses on stages 4‑5; near‑term roadmap on stages 1‑3.
* **Social‑layer effect**

  * Post‑Devcon talk attracted nine new teams; belief in long‑term vision is a “talent magnet.”
* **Q & A highlights**

  * *Optimality critique*: claiming optimal is hubris; models can change (e.g. one‑shot signatures); “ossification” should be renamed “longevity.”
  * *Call‑data vs blobs*: blobs seen as friction & packing headache; if block‑building centralisation concerns addressed differently, reverting to calldata is cleaner.
  * *Block‑builder pipeline*: APS removes proposers/relays; FOCIL adds robustness but multiple layers (e.g. size caps) still needed.
  * *State growth concern*: proposal for **partial‑state nodes** + access‑list blocks + erasure‑coded history; possible time‑based state expiry windows (1‑2 years).
  * *Client‑team sprawl*: 6 existing CLs + 9 newcomers; expectation of consolidation or modular specialisation (networking, ZK, signatures).
  * *Prototype vs complexity*: tiny Python specs valuable for discussion, but production code multiplies complexity ×100; must avoid Beacon‑chain rewrite pain.
  * *Need for deeper specs*: implementers ask for concrete aggregation/DC circuits; reply: code & calls are public, more mini‑specs will follow.
* **Session close**: agreement that overlap with ongoing upgrades is manageable; Lean components can be adopted incrementally once fully specified & proved.