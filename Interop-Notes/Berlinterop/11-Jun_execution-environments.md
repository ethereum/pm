## Resources

- [Pre-read](https://notes.ethereum.org/@gballet/Sypeq0Vbxl) [[PDF](Slides-notes/11-Jun_execution-environments-preread.pdf)]

## AI-generated notes

<sup>[prompt](Slides-notes/AI-info.md)</sup>

### Summary

* Attendees explored **how to let execution‑layer client code run inside zkEVMs without re‑writing it**, focusing on Rust today but ultimately aiming for *any* language that existing clients use.
* **Key blocker is the “target triple” problem**: architecture (e.g., `riscv64`), extension set, system‑call ABI (Linux / bare‑metal / WASM/WASI) and calling convention must all match what the guest binary expects and what the zkEVM circuit implements.
* Consensus client developers asked zkEVM teams whether they can **expose a RISC‑V Linux system‑call ABI inside the circuit**; at least one team already does this by adding an internal kernel that services `ecall`s from user‑space.
* Several zkEVMs can already compile to or emulate Linux‑RISC‑V; others could add it, but some currently rely on bespoke bare‑metal stubs or WASM imports.
* Participants tentatively agreed to **standardise on the Linux syscall numbers for 0‑511**, then carve out disjoint numeric ranges for (i) cryptographic precompiles and (ii) project‑specific extensions, avoiding collisions.
* A working list of **“must‑have” precompiles** emerged: Poseidon, SHA‑256, ECRecover and “almost every cryptographic operation”. Automatic‑circuit generation (e.g., Powdr) can still add optional extras.
* The group wants a **uniform host/guest I/O contract** (reading inputs, writing outputs, `commit`)—ideally mapped to ordinary Linux file descriptors (stdin/stdout/stderr) so that existing language runtimes just work.
* Debate on **ISA standardisation**: some propose mandating RISC‑V for guest programs; others argue this would foreclose future ZK‑friendly ISAs or higher‑level formats like WASM. No decision—door stays open.
* Concerns surfaced about hardware centralisation, long‑term maintenance burden of multiple ISAs, and proving correctness of ahead‑of‑time translations.
* Action items:

  * Spin up a **repo to collect precise specs** (syscall ranges, precompile list, host/guest interface).
  * Use the existing Telegram channel for discussion.
  * Reconvene at **Devconnect Argentina** to review progress.

---

### Chronological notes

* Opening goal‑setting: standardise execution environments; support more languages than Rust; identify unresolved questions.
* **“Target triple” overview** – problems arise at four layers:

  * Architecture (`riscv64`, `mips`, etc.).
  * ISA extension subset (e.g., `gc`, `imac`).
  * OS / syscall interface (Linux, bare‑metal, WASM/WASI).
  * Calling convention (usually GNU).
* OS/Syscall compatibility matrix (Linux, bare‑metal, WASM):

  * Besu, Erigon, Geth, Nethermind can compile for Linux.
  * Rust can target Linux *and* bare‑metal if a runtime is provided; zkEVMs can supply that runtime.
  * Some clients (Go in particular) *only* emit Linux binaries, limiting options.
* **Question posed to all zkEVM builders**: can you support `riscv64‑linux` ABI?

  * One team already does by adding a kernel inside the circuit; Linux syscalls jump to kernel code, which then calls precompiles.
  * Others say it is feasible but requires engineering time; some currently trap `ecall` directly to the prover for efficiency.
* Idea: make the in‑circuit kernel *re‑usable* across projects so every zkEVM does not re‑implement Linux semantics from scratch.
* Discussion of **WASM route**: certain clients (Kotlin, Go with hacks, Optimism’s fault‑proof VM) can target WASM; adding full WASI support inside zkEVMs would be extra work.
* Teams confirm WASM is low priority compared to RISC‑V; some use WASM only for tooling, not main execution.
* **Precompile inventory**:

  * Baseline set: Poseidon hash, SHA‑256, ECRecover.
  * Suggestion: reserve numeric ranges—0‑511 Linux syscalls, 1 000‑9 999 common precompiles, 10 000+ project‑specific.
  * Need to publish an exact table so guest binaries know what exists everywhere.
* Automatic precompile discovery (Powdr): uses profiling to lift hot basic blocks into dedicated circuits; behaves like normal precompiles at link time.
* **Host–guest I/O**:

  * Proposals: map host `read`/`write` to standard Linux file descriptors or dedicate specific syscall numbers.
  * Must agree on how `commit` (state root/output) is exposed.
  * Decision deferred to spec repo.
* Alternative linkage idea: instead of syscalls, allow ELF static linkage to named functions that the zkEVM loader patches—could avoid Go’s dependency on timers and other OS services. Mixed reception.
* **ISA catalogue presented**: RISC‑V, MIPS, WASM, Cairo, Valida, Petra, Thumb (ARM16), EVM bytecode.
* Discussion on Thumb: attractive 16‑bit density but ARM licensing risks; shelved unless legal clarity.
* Powdr explains its production path: prove blocks directly from EVM traces via Besu plugin—no separate guest ISA needed.
* **RISC‑V‑only proposal debated**:

  * *Pros*: open spec, rich tooling, reuse of existing compilers, easier code‑size analysis.
  * *Cons*: locks out future ZK‑optimised ISAs; forces translation of existing bytecode; may not improve proving speed; hardware centralisation worries.
  * No consensus reached; group leans toward keeping multiple ISA options.
* WASM advocates highlight structured control‑flow that eases ahead‑of‑time analysis and potential static gas bounds; sceptics note 20‑40× interpreter overhead unless translated, which itself must be proved correct.
* Observation: EVM’s coarse 256‑bit ops make interpreter overhead modest; WASM’s fine‑grained ops magnify it.
* Parallel drawn to ML world: LLVM’s MLIR dialect approach may be a better long‑term model—have a family of IRs tuned for ZK rather than one fixed ISA.
* Maintenance concern: execution clients would need to verify proofs for every supported ISA; library modularity mitigates but does not eliminate cost.
* Closing logistics:

  * Use the existing Telegram channel.
  * Create a public repo with Markdown spec drafts for syscalls, precompile ranges, I/O contract.
  * Next in‑person session pencilled for Devconnect Argentina.