## Resources

- [Pre-read](https://hackmd.io/@alexforshtat/native_aa_forschungsingenieurtagung) [[PDF](Slides-notes/12-Jun-native-account-abstraction-preread.pdf)]
- [Slides](Slides-notes/12-Jun-native-account-abstraction-slides.pdf)

## Human-generated notes

[Notes by Souradeep](Slides-notes/12-Jun-native-account-abstraction-notes-souradeep.pdf)

## AI-generated notes

<sup>[prompt](Slides-notes/AI-info.md)</sup>

### Summary

* **ERC‑4337 adoption** proves demand for smart‑account UX, but its on‑chain bundler contract adds \~40 k‑70 k gas per transfer and incentivises private relays; native AA removes that overhead.
* **Native AA proposal (EIP‑7701)** defines three independent roles per transaction—`sender` (smart account), optional `deployer`, optional `paymaster`—each validated by its own EVM frame.
* **Separate per‑role gas limits** let nodes cap unpaid “validation gas”, preventing DoS while still allowing heavy proofs (e.g., post‑quantum, ZK) at market‑determined cost.
* **New opcodes** (`TXDATA*, TXROLE, ACCEPTROLE`) expose typed transaction fields and require the contract to explicitly accept its role, blocking accidental misuse.
* **Protocol only enforces nonce, ETH balance and paymaster balance**; all other validity conditions are deferred to contract code, preserving complete flexibility.
* **Native AA integrates with Fork‑Choice‑enforced Inclusion Lists (FOCIL)**, giving censorship‑resistance that ERC‑4337 cannot offer because it still needs an EOA bundler.
* **Interop with stateless validation**: limit validation gas, restrict state reads, and/or supply bounded witnesses so attesters can verify inclusion‑listed AA txs without full state.
* **Existing ERC‑4337 smart accounts can upgrade in place**; only minimal changes (calling `ACCEPTROLE`, using new opcodes) are required.
* **Post‑quantum migration path**: users append Falcon (or other PQ) code via EIP‑7702, then a later fork disables ECDSA; wholly new native AA accounts can skip ECDSA entirely.
* **Alternatives considered:** keep status‑quo 4337 (keeps overhead & no censorship‑resistance); teach FOCIL to parse user‑ops (violates layering); enshrine 4337 entry‑point as precompile (still opinionated, larger calldata, no PQ for bundler). Native AA judged least‑complex path with no feature regressions.
* **Future transaction types/blobs:** 7701 designed to be forward‑compatible via index‑addressable `TXDATA*` opcodes; blobs or other fields can be appended without new opcodes.
* **L2 genesis without EOAs:** chains must pre‑deploy a minimal `CREATE2` factory (or equivalent precompile) so first AA transactions can create accounts; this is out‑of‑scope for 7701 but noted for an eventual roll‑up RAP.

---

### Chronological notes

* Presenter announces focus on **“native account abstraction” (EIP‑7701)** and why ERC‑4337 is not the final stop.
* **Why AA matters**

  * Transaction validity becomes arbitrary EVM code, not hard‑coded signature/nonce/balance rules.
  * Enables passkeys, session keys, native multisig, post‑quantum signatures.
  * Gas abstraction: third‑party contracts subsidise gas.
  * Execution abstraction: a smart account can batch & pre‑inspect state within one tx.
* **ERC‑4337 experiment recap**

  * Deployed without protocol changes, massive uptake (“hundreds of millions of user‑ops, tens of millions of accounts”).
  * 85 % of user‑ops used a paymaster; gas sponsorship proved critical.
  * Gas overhead on L2 still meaningful; private relay always cheaper → centralisation pressure.
* **Requirements for native AA**

  * Must preserve AA flexibility & paymasters.
  * No factories needed after first use (support self‑deployment).
  * Hardware ceiling must stay under EIP‑7870 target specs.
  * “No unnecessary complexity, no feature regressions.”
* **Advantages versus EOAs / ERC‑4337**

  * Removes gas overhead, broadens adoption.
  * Gains censorship‑resistance through FOCIL inclusion lists.
  * Enables post‑quantum accounts without new tx types.
  * Can retrofit EOAs via 7702 to become PQ smart accounts later.
* **Gas‑overhead numbers**

  * ERC‑20 transfer via 4337 smart account (ECDSA only) ≈ +70 k gas vs legacy tx; minimum overhead ≈ 40 k gas per user‑op.
* **EIP‑7701 transaction model**

  * **Roles**:
    1. `sender` – validates tx, holds assets.
    2. `deployer` – optional factory for first‑use CREATE2.
    3. `paymaster` – optional sponsor.
  * Maximum 5 top‑level frames: deploy → sender.validate → paymaster.prepay → sender.execute → paymaster.unwind/refund.
* **DoS‑mitigation design**

  * Each role gets its own *validation gas* quota; unpaid work capped.
  * Gas is not constant; heavy ZK proofs allowed but market‑priced.
  * Separate quotas prevent sender ↔ paymaster griefing.
* **New opcodes & context**

  * `TXDATASIZE`, `TXDATALOAD`, `TXDATACOPY` (index‑based) expose calldata‑style fields (type, account data, deployer data, etc.).
  * `TXROLE` returns current frame role; contract must call `ACCEPTROLE` before returning true.
  * Prevents a benign function call from accidentally binding the contract to an AA role.
* **Validation checklist (protocol level)**

  * If `deployer` specified: its call must succeed and account must now exist.
  * `sender` frame must execute and call `ACCEPTROLE`.
  * If `paymaster` present: must accept role and hold sufficient ETH.
  * Nonce & paymaster balance enforced natively; rest left to contract.
* **Mempool policy & state access**

  * Proposed out‑of‑band rules: validation code may only read its own storage, may not emit SSTORE/SELFDESTRUCT, etc., to stop “state‑flip invalidation” DoS.
  * Nodes should trace only the validation segment (e.g., 100 k gas cap) for admission.
* **FOCIL & statelessness interplay**

  * Attesters must re‑run validation for inclusion‑listed AA txs → need low gas ceiling and compact witnesses.
  * Suggest provide storage proofs; may cap #slots or witness size; AA txs exceeding limits still valid but lose FOCIL guarantees.
* **Alternative paths evaluated**

  * **Do nothing**: leave 4337 only → no censorship‑resistance, persistent overhead, ECDSA dependency.
  * **Make FOCIL parse user‑ops**: breaks layering, keeps other drawbacks.
  * **Enshrine 4337 entry‑point as precompile**: cheaper but opinionated ABI, larger calldata (RLP vs ABI), still needs EOA bundler, blocks other AA models.
  * Older native AA drafts (EIP‑86, 2938) introduced regressions or stalled. Native 7701 deemed best trade‑off.
* **Compatibility with current 4337 wallets**

  * Most are proxy‑based; upgrading implementation to call `ACCEPTROLE` and use new opcodes is trivial.
  * ABI packaging of UserOp not required at protocol layer, keeping AA un‑opinionated.
* **Privacy discussion**

  * Example: Tornado Cash withdrawal without doxxing—paymaster validates ZKP, gets ETH from mixer, reimburses itself, user sends tx directly to P2P mempool; impossible with EOA‑funded tx.
  * Self‑relay via temporary EOA still leaks funding trace & requires off‑chain coordination.
* **Post‑quantum migration Q\&A**

  * Flow: use 7702 to attach Falcon code ➜ later fork disables ECDSA key ➜ account becomes PQ‑only.
  * Smart accounts created with 7701 can omit ECDSA from day one.
* **Blobs & future tx upgrades**

  * 7701 doesn’t include blob fields initially; retains index‑based TXDATA design so future blob‑capable AA types can reuse opcodes.
  * Idea: after AA becomes default, all *new* tx types should build on AA rather than EOAs, to avoid matrix explosion.
* **Deployment on EOA‑free L2s**

  * Need a genesis‑level CREATE2 factory (pre‑deploy or precompile) so first AA tx can create its account; an L2 RAP may specify this.
* **Closing**

  * Call for questions; discussion around ABI enshrinement, access‑list precedent, and future hard‑fork cadence. Session ends with general agreement native AA is “the future”, gas overhead and censorship‑resistance being decisive.

---

### Relevant links

* ERC‑4337 spec — [https://eips.ethereum.org/EIPS/eip-4337](https://eips.ethereum.org/EIPS/eip-4337)