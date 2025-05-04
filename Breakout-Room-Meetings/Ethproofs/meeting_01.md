# Ethproofs Community Call #1: zkVM team introductions

**Prev Call:** Initial Call

**Meeting Date/Time:** Friday 2025/4/25 at 15:00 UTC

**Meeting Duration:** 2 hours

[GitHub Agenda & Presentations](https://github.com/ethereum/pm/issues/1449)

[Audio/Video of the meeting](https://youtu.be/4E-yaX-F7Qw)

Moderator: Justin Drake

Facilitators: Will Corcoran
- Facilitator email: will@ethereum.org
- Facilitator telegram: @corcoranwill


# Ethproofs Team Introduction & Platform Overview

| Topic | Subtopic | Details |
|-------|----------|---------|
| Introduction | Overview | - First Ethproofs call with ~150 attendees<br>- Focus on zkVMs<br>- 90-minute session with 21 zkVM teams presenting|
| | Ethproofs Purpose | - "L2beat but for zkVMs" that can prove EVM blocks<br>- Mission: Accelerate Ethereum snarkification<br>- Key primitive: Real-time proving |
| Real-time Proving Benefits | Consensus Layer | - Post-quantum security for beam chain<br>- Recursive aggregation of hash-based signatures (PQ)<br>- Validators on weak devices (phones, watches)<br>- Fully validating wallets |
| | Execution Layer | - Massive gas limit increase (1000x)<br>- Native rollups with direct L1 gas access<br>- Security benefits |
| | Application Layer | - Synchronous composability between rollups<br>- Enables flash loans, atomic arbitrage, liquidations across rollups |
| Future Calls | Schedule | - Call #2: Provers<br>- Call #3: Bringing L1 to gigas frontier (1 gigas/second)<br>- Calls #4-5: ISA considerations for EVM replacement<br>- Call #6: Formal verification |
| Ethproofs Updates | Team Recognition | - Built by Nuno, Pablo, Paul, and Joshua<br>- Same team behind ethereum.org<br>- Currently building V2 |
| | V2 Features: Multi-machine | - Current version limited to single CPU/GPU<br>- V2 will support multiple CPUs/GPUs<br>- Transparent hardware specs |
| | V2 Features: Pizza Metrics | - Visual representation of zkVM properties<br>- Performance metrics: verification time, proof size<br>- Security metrics: auditing, formal verification, security bits, post-quantum readiness, bounty programs |
| | V2 Features: In-browser Verification | - One-click proof verification in browser<br>- Demo showed 43ms verification time on single thread<br>- Using micro-zk-proofs library supporting Groth16 and Plonk |
| | V2 Features: Prover Killers | - Specially crafted EVM blocks to test worst-case scenarios<br>- 2x2 matrix showing provers vs. machine clusters<br>- Green notification for under 12-second proving<br>- Designed to exploit asymmetry between EVM gas and ZK prover cycles |
| Prover Killers | Implementation | - Developed by Connor (independent researcher)<br>- Targets ZK-unfriendly EVM operations: SHA-256, Keccak, ModExp, EC recover, elliptic curve pairings<br>- Will be distributed via Ethereum test repository<br>- Given catchy names like "SHA-256 Slayer" and "ModExp Murderer" |
| Data Fetching | Optimization | - Current issue: Large delta between total time and prover time<br>- Better approach: Use debug_executeWitness RPC endpoint on Reth<br>- Gets multi-proof for all state accesses in one call<br>- Reduces multiple RPC calls to a single call |
| Real-time Proving Grants | Program | - Three $100,000 grants planned<br>- Launch on Call #2<br>- Requirements include open-source prover, performance thresholds<br>- Aims to support real-time proving over extended period (1 year) |
| Support | Contact | - Will Cororan serving as primary coordinator<br>- Assistance with API keys, introductions, bug reports, grant applications |




# zkVM Showcase
| Topic | Subtopic | Details |
|-------|----------|---------|
| Newly Revealed zkVMs | Ix (Argument) | - Functional reduction zkVM<br>- Proves execution of Lean 4 kernel (dependently typed lambda calculus)<br>- Plugs into EVM-lean formal model<br>- Uses graph reduction instead of modeling CPU state<br>- Prioritizes safety and formal verification |
| | StarkV (StarkWare) | - RISC-V implementation for STU prover<br>- Based on Cairo knowledge<br>- Collaboration with Nexus<br>- Expected to be slower than Cairo but wider adoption<br>- Cairo M31 expected to have 50x optimization |
| | ZCray (Irreducible) | - Binius-native verifiable VM<br>- Custom ISA optimized for binius arithmetization<br>- Goals: low overhead, Rust/WASM compilation, interoperability<br>- Uses non-deterministic ROM and no general-purpose registers<br>- Collaboration with Polygon, open sourcing soon |
| Previously Announced zkVMs | Boojum 2.0 (MatterLabs) | - Multi-interpreter execution environment<br>- Compiles to RISC-V for proving<br>- Stark prover with M31 field<br>- Fully GPU accelerated<br>- 2-3 minutes for mainnet block on L4 GPU<br>- 35-50 seconds on RTX5090 |
| | Ceno (Scroll) | - "Sumcheck is all you need" design philosophy<br>- Multi-ari sum check with GKR layer circuit<br>- Pay-as-you-go prover (no padding)<br>- 1 minute block proving without GPU<br>- 1.5-2x faster than state-of-the-art on benchmarks |
| | Euclid (Scroll) | Euclid is not a zkVM but Scroll's recent upgrade that replaced Halo 2-based zkEVM circuits with OpenVM<br>Key benefits include:<br>- Better compatibility (replaced Poseidon hash-based ZK tree with ML Patricia tree)<br>- Simplified codebase (more readable Rust code vs complex Halo 2 circuits)<br>- Faster EIP support (added EIP7702 and RIP7212 in less than a week)<br>- Performance improvements (3x faster proof generation)<br>- Lower costs (1.2-2 cents per mega gas for L2 blocks)<br>- Removed limitations (deprecated circuit capacity checker<br>- The implementation is open source and can prove Ethereum mainnet blocks |
| | Jolt (a16z) | - Relies on sum protocol and lookup arguments (batch evaluation)<br>- Three core components: memory checking, read-write memory/registers/RAM, minimal constraint system<br>- Transitioning to "twist and shout" memory checking<br>- Working on bounded prover memory without recursion |
| | Keth (Kakarot) | - ZK-native EVM in Cairo targeting Starkware prover<br>- Alternative stack with no RISC-V/Plonky3 dependency<br>- Four engineers built stateless ZK L1 client in four months<br>- Facing challenges with trace length (1B) for Cairo prover |
| | Linea | - Type 2 zkVM based on MIMC hash function<br>- Directly arithmetizing London EVM<br>- In production with mainnet<br>- Upgrading to Prague EVM and type 1 architecture<br>- Transitioning to smaller field and targeting sub-10 second latency |
| | Nexus zkVM 3.0 | - RISC-V instruction set<br>- Switched from elliptic curves to arithmetization and small fields<br>- Collaboration with Starkware using PST2 backend<br>- Formally specified circuits<br>- Working on recursion and large execution support |
| | o1vm | - Supports MIPS32 and RISC-V 32 IM<br>- Based on pasta curve cycles<br>- Moving from Bellman to Promish for backend<br>- Working on Nova-based folding scheme called Arabata<br>- Currently paused to focus on Mina protocol |
| | OpenVM (Axiom) | - Modular zkVM framework with "no CPU" architecture<br>- Allows custom ISAs by mixing and matching opcodes<br>- Accelerated pre-compiles for all Ethereum operations<br>- Used by Scroll, can prove mainnet blocks<br>- Under 10 minutes on single CPU, ~1 minute on multi-machine |
| | Pico (Brevis) | - RISC-V compatible zkVM<br>- Modular back-end (swap proving systems with one line change)<br>- Application-level co-processor architecture<br>- Claimed fastest on CPU for various workloads<br>- GPU version coming next month for ETH proofs |
| | powdrVM (powdr)| - Multi-front-end (RISC-V, redacted ISA) and multi-backend (Plonky3, Halo2)<br>- Auto pre-compiles: automatically synthesized accelerators<br>- 3.5x faster end-to-end proof times<br>- Targeting 10x for complex benchmarks |
| | R0VM (RISC Zero) | - First RISC-V zkVM and first to prove Ethereum block<br>- Open source, including GPU acceleration<br>- Currently under 30 seconds per block<br>- Targeting real-time proving by mid-year<br>- Working on formal verification |
| | SP1 (Succinct) | - RISC-V 32 IM zkVM<br>- Extensive pre-compiles for Ethereum<br>- Integrated on ETH proofs via multiple providers<br>- Currently fastest on ETH proofs<br>- Binary-only GPU prover with multi-node capability<br>- Real-time proving within 2-3x (23s for 15M gas) |
| | Valida (LITA) | - Custom ISA with Plonky3 prover<br>- Supports C, Rust, and WASM languages<br>- Paper releasing on IAC formally specifying ISA<br>- Full compiler toolchain<br>- Exploring GPU acceleration with NIM-based code generator |
| | zk-Engine (NovaNet) | - NIVC folding-based prover network<br>- Works with WASM, supports parallelization<br>- Reliable liveness through folding<br>- Privacy by default<br>- Pay-per-opcode proving with specialized provers |
| | ZisK (Hermes/Polygon) | - RISC-V architecture optimized for latency<br>- Distributed and parallel prover system<br>- Open source including GPU proving<br>- Based on proven Polygon zkEVM toolset<br>- 0.15 second aggregation time for 2:1 recursion |
| | zkMIPS (ZKM) | - First industry MIPS32 zkVM<br>- Consistent instruction set with composite operations<br>- Version 1.0 coming in May with 6-20x performance increase<br>- GPU acceleration in two weeks<br>- Targeting 20 second end-to-end time |
| | zkWASM (Delphinus) | - Web assembly support<br>- Reference implementation in Halo2<br>- CPU prover at 7 seconds per million instructions<br>- Batch continuation at 3 seconds<br>- Complex ISA with 140 instructions and 64-bit memory |
| Real-time Proving Status | Close Contenders | - SP1: 23s for 15M gas block<br>- Seno VM: <1 minute without GPU<br>- Bonsai/RiscZero: <30 seconds, targeting real-time by mid-year<br>- ZisK: Built for latency from day one<br>- OpenVM: ~1 minute on multi-machine<br>- Pico: GPU version next month |
| | Technical Innovations | - Memory checking improvements<br>- GPU acceleration<br>- Multi-machine distribution<br>- Custom ISAs<br>- Fast recursion (ZisK: 0.15s, RiscZero: 0.21s for 2:1) |
