## Resources

- [Pre-read](https://hackmd.io/@raul/p2p-berlinterop-2025) [[PDF](Slides-notes/12-Jun-p2p-networking-preread.pdf)]
- Slides - [P2P networking](https://docs.google.com/presentation/d/1Ek38ZSiKMCZtBDl9RQrO28BhKwDnLfGaox3pHXG7phU/edit?usp=sharing) [[PDF](Slides-notes/12-Jun-p2p-networking-slides.pdf)]

## Human-generated notes

- [Notes by Pop](https://notes.ethereum.org/sgr6oeivSGKw9owxEjJY_A) [[PDF](Slides-notes/12-Jun-p2p-networking-notes-pop.pdf)]
- [Notes by Wonbin](https://hackmd.io/@HMU3ciGqSo2XRf4OpBV7Ng/HkpETIFmgg) [[PDF](Slides-notes/12-Jun-p2p-networking-notes-wonbin.pdf)]

## AI-generated notes

### Summary

* **Session purpose & context** – Newly‑formed EF peer‑to‑peer networking team (Raul & Marco) presented current network telemetry, outlined work‑streams (propagation, transport, benchmarking + simulation, telemetry + analysis) and invited broad discussion on reliability, security and “first‑principles” re‑design of the stack.
* **Current mainnet health** – EthPandaOps traces show beacon‐block propagation ≈ 0.5 s on average (likely seeded by hyper‑connected MEV relays) but attestation CDFs appear much slower (≈ 4 s) than some client‑local measurements; team will audit tracing queries & client logging paths.
* **Bandwidth math** – 33 k attestations/slot × 200 B ≈ 6.5 MB unique data/slot; blob sidecar duplication is high because 80 % of blobs are already in the EL mempool when gossiped; suppression and smarter metadata are needed.
* **Quick wins** – Deep CPU & hot‑spot profiling across clients; “parameter‑only” GossipSub tweaks; enabling QUIC (incl. unreliable datagrams & session resumption) everywhere; eliminating outdated muxers (mplex) and aligning implementations.
* **GossipSub roadmap** – Five duplicate‑reduction ideas discussed; strongest consensus for **choke‑extensions** (receiver‑controlled lazy‑push). Requires feature‑flag negotiation independent of protocol version to avoid hard forks.
* **Network‑coding path** – RLNC (and chunk/fountain variants) can off‑load large payloads (blobs, future ↑blob‑counts) by spraying coded chunks over large fan‑outs; effective only with new topologies and QUIC datagrams. Re‑base existing Prism RLNC PoC on libp2p‑QUIC.
* **Transport direction** – “QUIC all the way”: single RTT hand‑shake, zero‑RTT reconnection, flow control and native multiplexing make TCP + yamux/noise legacy; proposal to deprecate mplex formally.
* **Benchmarking & interop** – Shadow will host deterministic multi‑client test‑nets; new “interop‑tester” DSL lets scenarios be reused for every proposal; telemetry (gossip traces, crawlers) will feed real‑world latencies & churn into Shadow models.
* **Telemetry consolidation** – EthPandaOps ClickHouse warehouse will accept community probes; need to redact sensitive peer IDs / IPs before publishing parquet bundles.
* **Reliability themes** – Graph healing, redundancy, chaos testing and DOS‑aware back‑pressure discussed; validator anonymity remains an open research space (mix‑net prototypes, hop‑count randomisation).
* **First‑principles rethink** – Questioned whether L1 nodes must cater to browsers; maybe serve light‑client data over HTTP/WebTransport instead of full p2p; consider unifying CL & EL networking (blob mempool in CL, shared discovery) and replacing JSON‑RPC EngineAPI with binary/IPC.
* **Action items** – Finalise mplex deprecation PR; agree on feature‑flag negotiation scheme; prototype choke‑extensions; re‑run propagation traces with validated methodology; extend Shadow interop suite; map EL/CL engine‑API pain points; weekly p2p call open to contributors.

---

### Chronological notes

* **Intro & agenda (Raul)**

  * Networking session long‑planned since his EF onboarding (≈ 6 weeks).
  * Agenda: overview metrics → focus‑area deep‑dives → group discussions on reliability & first‑principles.
* **State‑of‑the‑network data**

  * Built new dashboards from EthPandaOps traces (9‑12 points of presence).
  * **Block CDF**: mean 500 ms; hypothesis: MEV relays hyper‑connected.
  * **Attestation CDF**: \~4 s to 85 %; discrepancy vs. client‑local (\~1 s) flagged; possible causes: empty‑slot attestations, logging delay, signature verification queue.
  * **Bandwidth calc**: attestation set ≈ 6.45 MB/slot unique; with 4 s window implies modest per‑subnet load.
  * **Block size observations**: avg 40 kB; recent max \~168 kB; historic stress \~2 MB (full‑gas call‑data).
  * **Blob‑sidecar**: \~1 s propagation, high duplicate due to EL mempool 80 % hit rate (drops to 60–69 % with getBlobs v1 quirks).
  * Traffic pattern is bursty: blocks early, blobs, attests, idle \~5 s/slot; suggests opportunity for smarter phase scheduling.
* **North‑star targets & roadmap pressures**

  * Upcoming changes: slot restructuring, ↓slot time, 100–300 M gas, 8× blobs, PeerDAS, PBS/ePBS, FOCIL, 3‑SEF, EIP‑7870 constraints.
* **Work‑stream structure**

  * Layers: propagation → transport → benchmarking/simulation → telemetry/analysis; cross‑cutting security & reliability; continuous “first‑principles” backlog.
* **Short‑term “quick wins”**

  * Hot‑path profiling across clients.
  * GossipSub tweaks possible once reliable datagrams allow large fan‑outs.
  * Resolve transport disparities: some clients still lack QUIC, some even lack TLS 1.3/noise‑XX.
* **Propagation layer deep‑dive (Marco)**

  * **Problem**: GossipSub rewards duplicates; bad for large messages.
  * **Taxonomy**: eager‑push (=send full msg) vs. lazy‑push (=IHAVE pointer).
  * **Five proposal families**
    1. **IAnnounce** – sender sets eager/lazy ratio.
    2. **Preamble‑IHAVE (I’m‑receiving)** – receiver pre‑declares.
    3. **Generalised GossipSub** – similar to choke‑ext but broader.
    4. **Push‑pull phase transition** – depends on hop‑count.
    5. **Choke‑extensions** – receiver tells peer to lazy‑push (“choke”) or eager‑push (“unchoke”); preferred because simple, compatible, enables others.
  * Discussion points:
    * Selective choke per sub‑stream (Csaba).
    * Wide variance among client impls (Mikhail); need shared best‑practice guide.
    * IHAVE scheduling strategies (down‑by‑one, timers) differ.
    * Requirement: new feature‑flag negotiation; version bumps brittle (Jacek).
* **Transport layer**

  * **Deprecate mplex** PR open (Teku main hold‑out).
  * **QUIC advantages**: 1‑RTT setup, no HoL blocking, flow control, unreliable datagrams, zero‑RTT resume.
  * Datagrams open UDP‑style design while preserving security.
* **Benchmarking & simulation**

  * **Shadow** selected; runs many heterogeneous clients deterministically.
  * “Interop‑tester” DSL: instructions + scenarios decouple test design from client code.
  * Need canonical scenario catalogue (e.g., TCP slow‑start interplay).
  * Telemetry‑driven parameterisation: build B0 mainnet model (latency, churn, RTT).
* **Telemetry & analysis**

  * Consolidate probes (gossip tracers, crawlers, Hermes) into EthPandaOps ClickHouse → daily Parquet dumps.
  * First finding: Xatu observers peer with each other → skewed traces; will break internal links.
  * Must redact PII; beware slot exhaustion when probes over‑peer.
* **Reliability / security brainstorming**

  * Self‑healing, redundancy, chaos testing proposed; validator anonymity via mix‑nets / hop‑count randomisation raised.
* **First‑principles stack reconsideration**

  * QUIC now ubiquitous; libp2p abstraction leaks performance (no RTT, CC stats, reliable‑reset).
  * Question multi‑transport requirement: browsers may consume via HTTP/WebTransport instead of full p2p.
  * Legacy “TCP‑yamux‑noise” could be ossified but yamux called “dead end”.
  * Discovery v5 could migrate onto QUIC datagrams; would simplify NAT hole‑punching.
  * Unify CL & EL networking:
    * Blob mempool likely belongs on CL side.
    * EngineAPI JSON‑RPC too heavy; suggest protobuf/IPC; earlier initiation already in use.
* **Discussion snippets**
  * Graph‑healing & tree topologies with coding could cut latency (Greg).
  * Attestation throttling vs. graph shape.
  * Light‑client traffic may be better served via edge HTTP.
  * Need DOS‑resistant sync (“always‑fork” pain).
* **Wrap‑up**
  * Weekly p2p call (private until structure stable); contributors invited.
  * Slogan: “QUIC all the things.”