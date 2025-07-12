## AI-generated notes

### Summary

* **Wallet UX fragmentation**: today’s multi‑roll‑up ecosystem forces users to juggle network switching, bridging, gas management and chain lists, leading to phishing risks and poor adoption.
* **On‑chain discoverability vision**: wallets should resolve *chain‑specific addresses* like `alice@arbitrum.eth`, automatically fetch canonical RPC endpoints from an **L1 registry**, and execute seamless cross‑chain transfers without manual network selection.
* **ERC‑7828 — Chain‑Specific Addresses**: extends the 20‑byte address with a chain context (`bob@base.eth`) so that both users and wallet code become chain‑agnostic.
* **ERC‑7785 — On‑chain Config “phone book”**: stores chain metadata (chain ID, RPC(s), canonical bridge wrapper, light‑client address, etc.) on Ethereum L1, providing an immutable, auditable source that removes reliance on hard‑coded JSON files.
* **Namespace & squatting concerns**: ENS selected as the default namespace; sub‑domain reservation plus cost (or proof‑of‑personhood gates) expected to deter squatters. Debate remains open but no viable alternative gained traction.
* **Required config fields (v1)**: chain ID, RPC list, standardized bridge wrapper, light‑client contract, chain‑type/tx‑types; L2s asked to propose additions and commit to a **testnet deployment within six months**.
* **Standardized L1→L2 bridge wrapper**: thin contract sitting in front of each canonical bridge normalises `depositGasToken()` and `depositToken()` (ERC‑20). Wallets interact with one ABI while underlying implementations vary. Wrapper MUST stay trust‑minimal and reside in the on‑chain registry.
* **Open design questions**: handling custom gas‑tokens, failed deposits/recovery, attribute encoding (ERC‑7786), permissionless asset‑ID↔token‑address mapping across chains. A separate Telegram working group was formed to draft the ABI.
* **Standardised light‑client contracts**: each L2 publishes an L1 contract that verifies L2 proofs (`verifyFinalizedState`, `verifyRecentState`). Wallets fetch proofs via RPC, then use `eth_call` on L1 for verification—eliminating blind trust in RPC responses. Helios (OP chains) cited as proof‑of‑concept.
* **Further RPC spec work**: proposal for an `eth_callWithProof` endpoint so wallets can request execution results plus merkle/other proofs in a single response, regardless of underlying VM (EVM, Stylus/Wasm, etc.).
* **Action items**:

  * Join two Telegram groups (On‑chain‑Config & Bridge Wrapper / Light‑client).
  * Submit mandatory field list for config contract.
  * Contribute ABI drafts and surveys of existing bridge contracts.
  * Add Helios engineers to the light‑client thread.

---

### Chronological notes

* *Meeting opens & agenda*: account‑abstraction/interop team introduces four topics—wallet struggles, on‑chain config + chain‑specific addresses, standardised L1→L2 bridge wrapper, standardised light‑client contract.

* *Current UX pain points*

  * 2020: single‑chain simplicity → 2024: >100 new EVM chains (Chainlist).
  * Wallets hard‑code chain lists; users paste RPC URLs, creating phishing surface and brittle configs when URLs rotate.
  * Fragmented liquidity & stuck assets when gas token absent.

* *Vision mock‑up*: send USDC from Arbitrum using aggregated balances; success receipt shows `alice@arbitrum.eth`. Chains become “invisible”; wallet discovers route automatically.

* *Phone‑number analogy*: users shouldn’t know country codes or carriers; similarly they shouldn’t manage chain IDs or RPCs. Chain‑specific addresses aim to hide that complexity.

* *Chain‑Specific Address standard (ERC‑7828)*

  * Adds chain component to 20‑byte EOA/contract address.
  * Eliminates manual network switching for both users and wallet logic.

* *On‑chain Config registry (ERC‑7785 concept)*

  * Stores canonical RPC URLs, bridge wrapper, light‑client address, metadata.
  * Rationale: immutable audit trail, no firmware‑style surprises (Ledger Recover cited).
  * Open question: exactly which fields are day‑one mandatory.

* *Namespace / ENS discussion*

  * Concern: name squatting (e.g., `nike.eth`).
  * Proposed mitigations: ENS cost model, proof‑of‑humanity gating for sub‑names, sub‑domain reservations for official L2s.
  * Decision: stick with ENS for v1; revisit multi‑namespace in later version.

* *Additional config‑contract fields proposed*

  * Chain‑type flag to expose supported tx‑types/features.
  * Standard bridge & light‑client pointers.
  * Potential inclusion of gas‑limit, blob parameters, etc. \[UNCERTAIN]
    * Possible correction: suggestion was limited to “whatever appears in chain‑list JSON today plus L2‑specific extras”.

* *Commitment timeline*

  * Working group formed; goal: v1 registry contract on testnet within six months; several L2 teams signaled willingness.

* *Standardised L1→L2 bridge wrapper*

  * Motivation: dozen canonical bridge ABIs diverge; wallet maintainers forced to track each.
  * Wrapper normalises `depositGasToken()` and `depositToken(address token, uint256 amount, …)`; internal logic may call canonical bridge or 7786 message router.
  * Must remain trustless (only canonical bridge), exclude third‑party bridges (CCTP, LayerZero) for baseline.

* *Discussion threads*

  * **Retriable calls & failure recovery**: need optional `refundFailedDeposit()` interface, but scope kept minimal for v1.
  * **Custom gas‑token chains**: rename ETH‑specific function to `depositGasToken`; wrapper converts ETH to native token where required.
  * **Asset‑ID ↔ token‑address mapping**: idea of permissionless registry maintained via cross‑chain calls; could live outside bridge wrapper standard; volunteer asked to draft proposal.
  * **Survey request**: collect existing bridge ABIs to quantify divergence.

* *Light‑client standard discussion*

  * Goal: allow wallets to verify L2 storage/code without trusting centralized RPC.
  * API sketch:
    * `verifyFinalizedState(bytes proof, bytes32 slot, …) returns (bool)`
    * `verifyRecentState(bytes proof, bytes32 slot, …) returns (bool)`
  * For zk roll‑ups both map to same logic; optimistic roll‑ups distinguish finalized vs recent.
  * Each L2 deploys its own contract; address published in config registry.

* *Wallet flow outline*

  * Wallet fetches proof via RPC (`eth_getProof` or new `eth_callWithProof`).
  * Calls light‑client contract on L1 using `eth_call`; verifies result via its existing L1 light‑client.
  * Execution of ERC‑20 `balanceOf` etc. may require fetching contract bytecode; debate over handling Wasm (Stylus) or precompiles.

* *RPC spec extension*

  * Proposal: standard endpoint returning **execution result + proof** so wallets can remain VM‑agnostic.
  * To be added to light‑client working‑group charter.

* *Meeting close & next steps*

  * Two Telegram groups created (On‑chain Config; Bridge/Light‑client).
  * Participants asked to:
    * Post required field lists, ABI suggestions.
    * Survey canonical bridge ABIs.
    * Bring Helios contributors into light‑client thread.
  * Agreement to iterate publicly and publish reference contracts.

---

### Relevant links

* [https://eips.ethereum.org/EIPS/eip-7828](https://eips.ethereum.org/EIPS/eip-7828)
* [https://eips.ethereum.org/EIPS/eip-7785](https://eips.ethereum.org/EIPS/eip-7785)
* [https://eips.ethereum.org/EIPS/eip-7786](https://eips.ethereum.org/EIPS/eip-7786)
* [https://github.com/a16z/helios](https://github.com/a16z/helios)