# Navigating the path to endgame stateless Ethereum

#### Pre-reads

- EIPs: [6800](https://eips.ethereum.org/EIPS/eip-6800), [4762](https://eips.ethereum.org/EIPS/eip-4762) 
- [Latest Verkle measurements](https://efdn.notion.site/Verkle-measurements-123d9895554180e6ac17eddf76c692b6?pvs=73)
- verkle.info
- [Anatomy of a Verkle Proof](https://ihagopian.com/posts/anatomy-of-a-verkle-proof)
- [Binary Tree Notes](https://hackmd.io/@jsign/binary-tree-notes)

---

### 1. 💡Reminder, the whole point of this is to get stateless clients and help solve state growth
- stateless clients can help increase gas limit
- better developer UX (remove contract code size limit)
- improve UX of running a node (reduce sync time)
- smaller DB footprint (compared to current MPT: roughly 25% savings)


### 2. ⌛️ We have to migrate away from the current MPT at some point
- why? current worst-case proof size is ~300MB
 
     > A worst case block today would consist of 12500 calls (assuming 800 gas cost of calling, including 700 gas for the call + 100 gas to setup parameters for the opcode), each to a max-sized 24 kB contract. That is, 24 MB Merkle proofs, and 300 MB code length, for a total proof size of 324 MB. 
- [See old discussion here](https://ethereum-magicians.org/t/protocol-changes-to-bound-witness-size/3885)

### 3. 🤔 Currently two main candidates to migrate to: (a) Verkle, or (b) binary w/ something like poseidon/blake/sha256
- **Verkle**: 
    - pros: it works (gives us small proofs), multiple clients are fairly far along, and is almost certainly the fastest path to shipping stateless clients
- **Binary**: 
    - pros: more friendly to current SNARK systems,  and is quantum-resistant
    - back to the future: Guillaume author on initial Binary EIP ([3102](https://eips.ethereum.org/EIPS/eip-3102)) from back in 2019
    - *note: what kind of binary tree?*
        - two options: 
            - Prefixed Merkle Tree (PMT): including extension nodes to avoid full depth.
            - Sparse Merkle Tree (SMT): a tree with a fixed (full) depth of 256-bits (assuming key length). 
            

### 4. Quantum concerns 
- We've spent time talking to top quantum experts 
    - Conclusion: impossible to predict, with experts estimating anywhere between the next 10-20 years. But momentum clearly has been accelerating. 
    - Scott Aaronson: "if you have things you want to remain secure in year 2034, then you should probably start moving"
    - Seth Lloyd: "I say 10 years plus or minus never"
    - [Notes from Scott Aaronson convo](https://docs.google.com/document/d/1yMLK5ToZ-K7BWWLSMk3R39HJodtHH_kOBzd1NxA1Mp8/edit?usp=sharing)
    - [Summary of quantum-vulnerable parts of Ethereum ](https://docs.google.com/spreadsheets/d/138bR2gRQS9dktKKsYBc2euOROdQ74g4KwPuCsHlXjX0/edit?usp=sharing)
- Quantum is clearly an important variable, but should not be *the* determining factor. Verkle was always intended as a temporary stepping stone on the path to fully SNARKifying the L1. 
- Relevant question: pros/cons of having to do 2 separate migrations. 

### 5. ZK performance is accelerating, but still little ways to go
- Need to hit ~200k hashes/second
 
    > math: worst-case block has 13,000 tree accesses. With this, binary trie will be about 250k to 500k hashes. This needs to be proved within 1-2 secs.
- Poseidon fast enough already today...but open question if secure enough to ship on L1 (cryptography team working on this question)
- [Plonky3 w/ Poseidon](https://twitter.com/dlubarov/status/1851667100542341155): over 2M hashes per second on M3 Max (16 core)
    - "2m hash/sec = 62 MB/sec of merkling is enough to fully re-hash a theoretical-maximum-sized ethereum consensus state within a single slot, now do blake3 or sha256 pls"
    - Daniel: We'll work on blake3 soon 🫡
    - [High-level timings from Daniel here](https://gist.github.com/dlubarov/0eb8490f659a5aa9970cf95cfe1b0fb5)
- Next up: need to better understand perf of Blake, sha256, and things like Binius (new proof system from [Irreducible](https://www.irreducible.com/posts/binius-hardware-optimized-snark))


### 6. Conclusion: so... how to find best path forward? 
*First step: what are the questions we need to answer?*
1) what is the relative priority of shipping stateless clients in the first place? (see above benefits)
1) how does snap sync work in each path?
    - what sync algo to use w/ SNARKs
    - how to increase gas limit without breaking sync/healing

1) what is current ZK prover performance, and how much faster do they have to get to give us real-time proving on "reasonable hardware"
    - Hard to know until we have a better idea of what the zk witness actually look like. (200k hashes/sec?) 
    - Poseidon seems clearly fast enough, but need updated numbers on Blake/sha256/keccak 
1) what is "reasonable hardware"
    - consumer laptop?
1) which hash function (and related security considerations)
    - [Poseidon vs Blake vs sha256](https://docs.google.com/presentation/d/1ThnYm75e4jqXartpv6rmwQXVg5gF8L_WNmHyND9-_kM/edit#slide=id.p)
1) what is the future of local building?
    - will people still be able to self-build blocks locally?
1) database size / format: 
    - what's the db footprint of binary trie
    - how do we store data in a way that's not a performance bottleneck

1) what do the ZK proofs actually look like, what's the max expected proof size, etc
1) Details on binary tree design
    - [see Ignacio's recent doc ](https://hackmd.io/@jsign/binary-tree-notes)


---
If time:

*Brainstorming the following questions:*
    - eip158/enabling deletions in pre-state expiry verkle
    - Using sha256/blake3 for key computation
    - Changes to the proof format: opacity, structure
    - EOF and verkle
    - 7702 and verkle