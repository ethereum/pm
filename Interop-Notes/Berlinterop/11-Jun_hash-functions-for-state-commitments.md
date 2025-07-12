## Resources

- [Pre-read](https://notes.ethereum.org/m4L02cXBSzKRl9dGj-EiXQ) [[PDF](Slides-notes/11-Jun_hash-functions-for-state-commitments-preread.pdf)]

## AI-generated notes

<sup>[prompt](Slides-notes/AI-info.md)</sup>

### Summary

- The session’s purpose was to examine whether **Keccak‑256**‑based state commitments are a bottleneck for zkEVM provers and, if so, what hash‑function or tree‑layout changes might help.
- Three framing questions guided the discussion:
1. Are Keccak hashes in the state trie too costly for zkEVM provers?
2. Will upcoming proving‑system advances change that cost profile?
3. If we swap the hash, should the trie’s structure (depth, arity, code‑hashing rules, etc.) also change?
- Participants agreed current Merkle Patricia Trie (MPT) proofs are **large and uneven in depth**, and Keccak is **bit‑oriented**, making it prover‑unfriendly.
- Candidate replacement hashes were compared: **Poseidon** (fast in‑circuit, field‑based, under an EF “Poseidon Initiative” for deeper analysis), **Blake 2/3** (fast natively, but modular‑addition heavy in circuits), **SHA‑256** (hardware‑accelerated and ≈5× cheaper to prove than Keccak in several teams’ measurements), **Grøstl**, **“Tie”/matrix‑hashes**, and “binary Poseidon.”
- Multiple zkEVM teams (Polygon zkEVM, Scroll, Taiko, others) reported **SHA‑256 proving is \~5 × faster** than Keccak; some measured Keccak hashing >50 % of their total proving time.
- ECDSA verification was called out as another sizable cost (\~25 % of traces in one projection); harmonising the choice of hash for both signatures and state commitments was suggested.
- Proof‑system evolution (e.g., GKR, STARK optimisations) may **reduce non‑hash costs faster than hash costs**, potentially **raising hashing’s relative share**; therefore a 5× speed‑up today may not be enough long‑term.
- Changing only the hash leaves byte‑code hashing and trie depth issues unsolved; ideas aired include fixed‑depth tries, alternative key‑derivation, or moving to Verkle‑like layouts—each with distinct trade‑offs for DoS resistance and proof size.
- “Near‑key” depth‑extension attacks (crafting colliding prefixes to lengthen proofs) were highlighted as a ZK‑specific concern; fixed‑depth tries mitigate them but impose worst‑case hashing on every lookup.
- Field‑mismatch when using Poseidon (e.g., BabyBear vs M31) can be handled with nested proofs, but that adds overhead; some teams would rather keep SHA‑256 and avoid cross‑field gadgets.
- No final decision was taken; action items are to collect broader benchmark data (especially Blake 2/3), monitor Poseidon‑security results, and continue analysing how upcoming proof‑system changes shift the optimisation frontier.

---

### Chronological notes

* **Opening & agenda**

  * Moderator outlines three key questions: cost of Keccak in provers, effect of proving‑system progress, and whether to modify trie layout as well as hash.

* **Current trie pain points**

  * MPT proofs require heterogeneous depths and hash functions.
  * Keccak is performant on CPUs/ASICs but not in arithmetic circuits (bit‑centric, non‑field operations).

* **Change dimensions enumerated**

  * *Trie format*: balance, fixed arity, binary vs hex.
  * *Code‑hashing*: avoid full‑bytecode Keccak if possible.
  * *Hash primitive*: swap Keccak for a prover‑friendly function.
  * *Domain*: moving from bit strings to field elements introduces conversion overhead.

* **Hash candidates presented**

  * **Poseidon**: fast in SNARK/STARK, used in recursion; drawbacks—prime‑field only, not standardised, ongoing security review (“Poseidon Initiative” grants, weakened‑instance bounties, 1.5‑year timeline).
  * **Blake 2/3**: widely deployed, good native speed; prover cost high due to ADD/SUB over 64‑bit words.
  * **Grøstl**: SHA‑3 finalist, solid analysis; slow in both native and circuit contexts.
  * **Tie / matrix‑hash**: requires large input/output to match security strength; arithmetic may be awkward for provers.
  * **Rescue / Vision**: slower natively, lingering analysis questions.
  * **Binary Poseidon**: work‑in‑progress adapting Poseidon to GF(2ⁿ).

* **Floor discussion – performance data**

  * Multiple teams report **SHA‑256 ≈ 5 × faster** than Keccak inside their zkEVMs; one team cites ≈10 × on CPUs due to SHA extensions.
  * Blake benchmarks requested; StarksWare noted to have a fast implementation but no numbers shared yet.
  * Keccak proving load estimates: “>50 %” (one team), “\~⅓” (several), “<20 %” (others).

* **Field‑specific Poseidon issues**

  * Poseidon constants differ per prime; using a field different from the prover’s native field forces cross‑field proofs or field conversion gadgets → extra constraints.
  * Some teams would switch their entire proof system to M31 rather than pay that overhead; others prefer SHA‑256 to avoid it.

* **Proof‑system evolution**

  * Question: will hash constraints become cheaper in future STARK/GKR variants?
  * Response: unlikely in near term; papers show GKR doesn’t help much for hash‑like mixing; improvements elsewhere may actually **increase hashing’s percentage** of total cost.

* **ECDSA & unified hashes**

  * If Ethereum moves to hash‑based signatures for post‑quantum reasons, sharing a single hash primitive between signatures and state commitments could amortise optimisation work.
  * Today, ECDSA still expensive (\~25 % of traces in a sample projection).

* **Contract‑bytecode hashing concerns**

  * Current contract size limit (\~24 kB) keeps hash cost tolerable; lifting that limit or switching to chunked‑load (EOF / Verkle proposals) would change the calculus.
  * Verkle‑style code chunking offers selective loading but requires EOF‑style structure, which was recently deprioritised.

* **Depth‑extension (near‑key) attacks**

  * Adversary can choose keys sharing long prefixes to force deep paths and inflate proof cost.
  * Fixed‑depth tries remove variance but levy worst‑case cost on every lookup.
  * Alternative: change key‑derivation to reduce prefix predictability; no concrete scheme finalised.

* **Delayed‑state‑root / separate proof ideas**

  * Some attendees explored separating execution proof from state‑root proof and joining them off‑chain; still requires a hash link or large Merkle proofs on‑chain, so doesn’t clearly win.

* **Closing observations**

  * Short‑term: gather comprehensive performance numbers, especially for Blake 2/3 and cross‑field Poseidon tricks.
  * Medium‑term: track results of the Poseidon Initiative and proof‑system research; reassess whether a 5 × or 10 × hash‑cost reduction is mandatory before committing to a new primitive.
  * Long‑term: a joint tree‑format plus hash change (possibly Verkle‑based) may be necessary for both DoS hardening and prover efficiency.