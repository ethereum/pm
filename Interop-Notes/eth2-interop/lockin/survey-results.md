|   | **Harmony** | **Prysm** | **Lighthouse** | **Artemis** | **Trinity** | **Lodestar** | **Nimbus** | **Shasper** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  **0.1 Link to raw answers** | [Link](https://hackmd.io/DGT-VV7xTBeJzCJPtu24_g) | [Link](https://gist.github.com/rauljordan/286ba48755a826af58df3183fc67140f) | [Link](https://gist.github.com/protolambda/183210168cc9e34398e2337083270729) | [Link](https://hackmd.io/SDWkvHAeTZCFtZ1Np-C0aQ?view) | [Link](https://notes.ethereum.org/BRRs2i7CSvKb7zkW5C5WHg?view) | [Link](https://hackmd.io/-JcbLcoERg-f9c154ODoCw?both) | [Link](https://hackmd.io/CHgplHlVTxOSvgnPurfXFQ?both) | [Link](https://gist.github.com/sorpaas/7f5843a16fb9cff8b0e99d34be6ef394) |
|  **0.2 Link to raw followup answers** | [Link](https://notes.ethereum.org/4WimtbcYSbmEJ8ByJUS6Nw) | [Link](https://gist.github.com/terencechain/75cd618598db06af66dbe55e9616c573) | [Link](https://notes.ethereum.org/7ZVjYG1aTmmXTZFPDXL60Q) | [Link](https://notes.ethereum.org/bLv4lFPOTrWVb8-BnDO26A) | [Link](https://notes.ethereum.org/MCRM-jb9R7SCYK1n4g8_LA) | [Link](https://notes.ethereum.org/UNEIAeRgTj-aqLKCHYgGVg) | [Link](https://notes.ethereum.org/e_qm3HAoSmGtK3TDoPVgXQ) |  |
|  **1. General** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  1.1 What is the latest version of the specification which your client currently supports? | v0.8.2 | v0.8.2 | v0.8.2 | v0.8.2| v0.8.2 | v0.8.1 | v0.8.2 | v0.8.1 |
|  1.2 Is v0.8.2+ targeted as interop version? If not, which version do you suggest? | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
|  1.3 Are any features or components particularly difficult to update, and on what versions are these currently? | test suite update | test suite update | merklization. | SSZ 8.1 update | No | No | No | No |
|  1.4 In terms of interop, do you have any suggestions? | time/place to work on code | - | network conformance | multi-client integration test network</br>SEE DOC for full answer | Start small | A best-effort for Lodestar, see if latest speed improvements make interop possible | Start with libp2p and work our way up the stack all the way to application layer / consensus | N/A |
|  1.5 What has been your primary bottleneck in development? | network stack and attestation pool | runtime bugs, libp2p breaking or poor design | Spec updates -- re-doing work or coding defensively in expectation of a spec update. | SSZ and (more recently) test format changes | Optimizing python, and taking on libp2p in python | resource allocation | Dependencies whose code needs writing | Networking |
|  1.6 What do you anticipate to be the primary bottleneck in the future? | sync process and consensus | runtime bugs, and following design changes | Perhaps spec updates during future phases, or friction trying to collaborate with other teams. | Keeping 9 clients interoperable. | Performant state transition function. Attestations workload | resource allocation | Testing / polish while community is pushing for release | Haven't been doing much |
|   |  |  |  |  |  |  |  |  |
|  **2. Networking Essentials** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  2.1 Does your client currently implement libp2p? If not, what subset is working? | Anton has finished libp2p API and started to integrate it into the client. It will take a time but we hope that it will be done this week. | Yes | Yes | Yes, Mothra is handling our libp2p side. | Yes | Yes | Yes, libp2p Go deamon | Yes |
|  2.2 Do you make use of a libp2p daemon approach? | No | No | No | No, we have native bindings to rust libp2p. No gRPC required | No | No | Yes | No |
|  2.3 How does your client become aware of its peers? Static node list, DHT/discv5, etc. | Static node list | Static peering via `--peer` flag. discv5 in master, but waiting on some updates from felix | Static peering and Discv5 - Although we can support libp2p kademlia if needed. | We use discv5 and static nodes (via mothra) | Static node list and discv5 is ready for some initial inerop tests (talk to jannik) | Static node list | Static node list | mDNS discovery and Kademlia |
|  2.4 By which process does your client establish a handshake with its peers? | unencrypted TCP | libp2p spec | discv5 session handshake, libp2p secio* | Network spec | Networking spec | req/resp hello messages | static nodes, networking spec | status message starts sync |
|  2.5 Which wire-level encryption methods does your client implement or support? Secio? TLS? Other? If your client supports multiple encryption methods, please indicate which ones. | none now. secio and noise in future. | SecIO supported, could add TLS | Secio (although we could upgrade to noise relatively easily). | Secio currently | Secio | Secio | Everything supported by the Go daemon | tcp-ws-secio-mplex-yamux |
|  2.6 Does your client conform to the specified wire protocol? If not, please provide a link to the appropriate code snippet or repo which defines these message types. | Yes, except for libp2p | Yes | Yes | Yes, GOSSIP as defined in the network spec. Working on RPC | Yes | WIP, PR in progress | Yes | simple status sync |
|  2.7 Can you run a stable testnet with multiple nodes of your single client? | Yes | Yes* | Yes | Yes* | Not yet | No | Yes | Yes |
|   |  |  |  |  |  |  |  |  |
|  **3. Syncing** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  3.1 Do you use the /eth2/beacon_chain/req/beacon_blocks/1/ proposed in the Network Spec for syncing? | We're able to sync by requesting historic data via RPC requests identical to the spec but over a custom transport protocol. Moving to spec'd RPC is a part of (2.1) libp2p integration. | Yes | Yes | Not yet | Yes | WIP | Yes, Old and new requests supported. Currently using old for sync | No |
|  3.2 Do you support a full sync from genesis after the network is running for a longer period of time? | Yes | Yes | Yes | Not yet | Not yet | No | Yes | Yes |
|  3.3 Can you bootstrap syncing with a copy of sync data? | There is a work in progress on that. Should be done it two days. | No | No | No | No | No | Yes | No |
|  3.4 Do you make use of batch-requests for blocks? If so, what does your batched block request look like? | Yes, 128 chunks. | Yes | Yes, it's based on the BeaconBlocks req. We batch lookup with fixed count parameters. | Not yet | Not yet | No | Not yet, we plan to use batch requests for both | No |
|  3.5 Do you have any particular sync strategy? (Full sequential, skip-ahead, or some hybrid approach?) | Randomly requesting peers* | Full sequential sync from genesis with multiple peers | Primarily full sequential if needed, with optimizations | No | No | No | full sequential sync* | simple full sequential |
|  3.6 Do you implement any pruning mechanism? (not necessary for initial interop) | No | For attestations | Not in master, but we are prototyping in a PR (its a part of the hot/cold DB we're working on). | No | No | No | Not yet | No |
|   |  |  |  |  |  |  |  |  |
|  **4. State Storage** |  |  |  |  |  |  |  |  |
|  (Out of interest, no hard requirements) |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  4.1 Do you minimize storage? Are you supporting any of the following approaches? | No |  | WIP, should be ready in 1-2 weeks. | No minimization. Currently store all blocks and states for all slots |  | No | No | No |
|  Immutable state data structure | No | No | No | No | Yes | No | No | No |
|  Segmented/chunkfied state | No | No | No | No | No | No | No | No |
|  Full copies | Yes | No | No | Yes | Yes | Yes | Yes | Yes |
|  Other | No | Yes | No | No | No | No | No | No |
|  4.2 What is your storage approach like? |  |  |  |  |  |  |  |  |
|  Store on X interval | No | No | No | No | No | No | No | No |
|  Store every slot | No | No | No | Yes | Yes | No | No | No |
|  Store every block | No | Yes | Yes, but to be replaced | Yes | No | Yes | No | Yes |
|  Other | write-buffer that is flushed when its reaches pre-defined threshold (64Mb for now) | No | WIP, hot/cold database where hot is space-inefficient but fast & cold uses a highly optimized layout which assumes no forking (relies upon finality). | No | WIP, Epoch boundaries | No | Yes, Epoch boundaries | No |
|   |  |  |  |  |  |  |  |  |
|  **5. Attestation Aggregation** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  5.1 Do you follow the current basic interop aggregate strategy? (parse anything, but publish just minimal what you have to aggregate later). | The pool is 70% ready. I am going to release it this week either. Gossiping attestations is a part of libp2p integration as well. We're aggregating locally for block production. | Yes | Yes | Yes* | Yes | No | Yes* | No |
|  5.2 Do you support alternative (more advanced) aggregation strategies? | No | No | We can support strategies but none are built/employed. | No | No | No | No | No |
|   |  |  |  |  |  |  |  |  |
|  **6. Fork Choice** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  6.1 Do you test fork choice? In what kind of context(s) do you test it? | No | Yes | No | Yes | No | No | No |
|  6.2 What is your implementation type like: |  |  |  |  |  |  |  |  |
|  Unoptimized spec | Yes | Yes | Yes | Yes | Yes | No | Yes | Yes |
|  Cached spec-like | No | WIP | Yes | No | No | No | No | No |
|  Reduced form (shortcut 1-child nodes) | No | Yes | Yes | No | No | No | No | No |
|  Stateful structure | No | No | No | No | No | Yes | No | No |
|  Other | No | No | No | No | No | No | No | No |
|   |  |  |  |  |  |  |  |  |
|  **7. Spec-Tests / Transition Consensus** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  7.1 Do you pass the following spec tests? If not, in which configuration and what tests?: |  |  |  |  |  |  |  |  |
|  Block operations | Yes | Yes | Yes | Close | Yes | Yes | WIP | Yes |
|  Epoch processing | Yes | Yes | Yes | Close | Yes | Yes | WIP | Yes |
|  Sanity tests | Yes | Yes | Yes | Close | Yes | Yes | WIP | Yes |
|  BLS integration | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
|  SSZ_static | Yes | Yes | Yes | Yes | Not yet | Yes | Yes | Yes |
|  Shuffling | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
|  7.2 What spec version are you currently targetting for tests? | v0.8.2 | v0.8.2 | v0.8.2 | v0.8.2 | v0.8.3 | v0.8.1 | v0.8.3 | v0.8.1 |
|   |  |  |  |  |  |  |  |  |
|  **8. Block Propagation (Strategy)** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  8.1 Do you follow the network spec: verify the proposer signature before relaying a block? | Not yet. | Yes | No, Currently no gossipsub validation - it's on the TODO list | No | Yes | WIP | No | No, import block first |
|  8.2 And if so, do you transition state completely, or just enough to know the proposer index? | N/A | Just enough to know proposer and verify signature | Full state transition | Just enough to know proposer and verify signature | Just enough to know proposer and verify signature | Transition state completely | Our block propagation is immediate and fully naive | Transition state completely |
|  8.3 Do you use any different approaches, like: |  |  |  |  |  |  |  | N/A |
|  8.3.1 Do you at any time randomly (or always) relay blocks without verification of the signature? | always rely on unverified blocks | No | Relay all blocks currently - planned to change | We receive the block and propogate before checking it. | No | Yes | Yes | N/A |
|  8.3.2 Which blocks do you process first (i.e. what gets priority)? | No priority | No | We request needed blocks during syncing and they are processed sequentially. We process each block from gossip prioritised by time of arrival | FIFO | No priority | FIFO | FIFO | N/A |
|  8.3.3 Do you detect spam? (i.e. drop peers with high amounts of invalid blocks) | No | No | We detect this, but do not drop peers | No | Not yet | Save block root of invalid blocks and skip them if they are received repeatedly. | No | N/A |
|  8.3.4 Is there any security check for double voting on the same block height before propagation? | No | No | No | No | No | No | No | N/A |
|   |  |  |  |  |  |  |  |  |
|  **9. Attestation Propagation (strategy)** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  9.1 Do you follow the network spec: verify a voted-for block fully before relaying an attestation? (option 1), or do you take another approach, such as relaying first, or with certain peers only? | queued until block is known | Like spec | blindly relay | blindly relay | Verify attestation, but not if block root is known | blindly relay | blindly relay | No |
|   |  |  |  |  |  |  |  |  |
|  **10. Block Proposals** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  10.1 Do you fill grafitti with any debug data? - What do you think of thus grafitti debug format proposal, described here? | No, lgtm | No, lgtm | Yes, but only tag the client version. | No, lgtm | No, lgtm | No, lgtm | No, lgtm | No, lgtm |
|  10.2 Do you implement the latest Validator API? | Yes | Yes, but JSON only with b64 | WIP | No, we have our own gRPC communication with our Validators | Not yet | Yes | No | Yes |
|  10.3 What is your clock syncing approach? | local machine time NTP | roughtime servers/sytem time | NTP | system clock | system clock | system clock | system clock | system clock |
|   |  |  |  |  |  |  |  |  |
|  **11. Monitoring** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  11.1 Do you implement the proposed Metrics | No | Yes | Yes | Yes | No | Yes | Maybe, WIP but not priority | No |
|  11.2 Do you provide a API endpoint for:<br/>- Sync status<br/>- Current chain head (from node perspective)<br/>- A series of blocks | No | Yes | Yes | No | No | Yes | No* | No |
|  11.3 What do you use for logging? (e.g. custom JSON, library XYZ) | log4j2 library | Logrus, JSON | JSON | Log4J, JSON/CSV | Python native | custom text, winston logger | JSON | No |
|  11.4 Provide links to any misc. API implemented by the beacon node. | N/A | [Link](https://github.com/prysmaticlabs/ethereumapis) | N/A | N/A | N/A | N/A | N/A | N/A |
|   |  |  |  |  |  |  |  |  |
|  **12. Keystore** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  12.1 Do you use anything like the Eth1 keystore format? | Yes | Yes | No, currently store raw keys. | Yes | Not yet | Yes | Not yet. | No |
|  12.2 Do you see any problems with the latest proposed keystore format, for interop purposes specifically? | No | No | No | No | No | No | Yes* | No |
|   |  |  |  |  |  |  |  |  |
|  **13. SSZ** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  13.1 Do you have SSZ v0.8 (hash-tree-roots with stable depth, bitlists/vectors) implemented currently? | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
|  13.2 Do you experience any particular delays with hash-tree-root? (If not already for the minimal configuration, does it apply to mainnet state sizes for your ssz implementation?) | No | No | No | No | Fine at low validator count (< 100) | No | No | No |
|   |  |  |  |  |  |  |  |  |
|  **14. BLS** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  14.1 Do tests pass for version v0.8.2+ (little endian domain bytes) | Yes | Yes | Yes | Yes | Yes | TBD | Yes | Passed for v0.8.1, haven't upgraded yet |
|  14.2 What BLS library do you use? (provide link) | [Milagro](https://github.com/apache/incubator-milagro-java) | [BLS12-381](https://github.com/phoreproject/bls) | Apache Milagro | [Milagro](https://repo1.maven.org/maven2/) | [Milagro](https://github.com/sigp/milagro_bls) | [Milagro](https://github.com/ChainSafe/incubator-milagro-crypto-js) | [BLS12-381](https://github.com/status-im/nim-blscurve) | [Milagro](https://github.com/sigp/milagro_bls) |
|  14.3 Do you implement a BLS wrapper? (provide link) | Milagro | [Custom](https://github.com/prysmaticlabs/prysm/tree/master/shared/bls) |[Milagro](https://github.com/sigp/milagro_bls) | [Mikuli](https://github.com/PegaSysEng/artemis/tree/master/util/src/main/java/tech/pegasys/artemis/util/mikuli) | [Milagro](https://github.com/ChihChengLiang/milagro_bls_binding) | [Custom](https://github.com/ChainSafe/lodestar/tree/master/packages/bls) | [Milagro](https://github.com/apache/incubator-milagro-crypto-c) | N/A |
|  14.4 Do you have a benchmark of verify-aggregate bench speed of 128 participants, same message being signed. Called from client. | Yes | Yes, ~25ms | Yes, ~7ms | No | Yes | Yes, ~400ms | No | No |
|   |  |  |  |  |  |  |  |  |
|  **15. Chain Start (reference doc)** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  15.1 Do you support loading: |  |  |  |  |  |  |  | only support loading genesis spec |
|  A kickstart ((genesis_time, validator_count) tuple) | Yes | Soon | Yes* | Yes | Yes | Yes | yes | No |
|  A list of deposits, with incremental proofs (genesis spec) | No | No | WIP | Yes | No | No | No, (?) | No |
|  A list of deposits, with proofs all to the same deposit root. | Yes | No | WIP | No | No | No | No, (?) | No |
|  A series of deposit contract logs from an Eth 1.0 oracle, from a mock/test service | Yes | Yes | WIP | Yes | No | Yes | No | No |
|  A series of deposit contract logs from a real Eth 1.0 node? | Yes | Yes | WIP | No | No | Yes | No | No |
|  A genesis constructed from a (slow and long) stream of deposit log events? | No | Yes | Not yet | Yes | No | No | No | No |
|  A plain prepared genesis BeaconState object from SSZ? | Soon | No | Yes | Yes | Yes, yaml. SSZ soon | Yes | Yes | No |
|  15.2 For testing genesis, do you generate keys in advance? And/or in a predictable reproducible manner for debugging? | Advance | Advance | Reproducible | Reproducible | Both | Reproducible | Reproducible | Advance |
|   |  |  |  |  |  |  |  |  |
|  **16. Configuration & Performance** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  16.1 Do you meet minimal configuration in respect to processing performance; 6 seconds with 8-slot epochs? | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
|  16.2 Are there alternative variations / easier parameters that work particularly well for your testnet(s)? | No | No | 1s slot times | Not sure | Yes, 4 slots/epoch, 4 shards | No | 3 seconds slots in 16 shards, 1000 validators network | No |
|  16.3 Do you load configuration on compile-time or run-time? | Both | Comile time presets, switch on runtime | Compile time presets, switch on runtime. Some TOML configurables | Both | Compile-time | Runtime | Compile-time | Compile-time |
|   |  |  |  |  |  |  |  |  |
|  **17. Building & deploying** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  17.1 Do you provide a build script for the client? | Gradle | Bazel | Cargo | Yes | No | Yes | Yes | No |
|  17.2 Do you use a form of containerization? E.g. Docker? | No | Yes | Yes | Yes | No | Yes | Yes | No |
|  17.3 Have you automated testnet deployments? | No | Yes | Yes | No | No | No | Yes | No |
|  17.4 What platforms/architectures are supported? | x86_64 | x86_64 & ARM | OSX, Linux | OSX, Linux | OSX | Linux | OSX, Linux, Windows | Linux |
|   |  |  |  |  |  |  |  |  |
|  **18. Conclusion** |  |  |  |  |  |  |  |  |
|   |  |  |  |  |  |  |  |  |
|  18.1 Is there anything that this questionnaire did not cover? | No | No | No | No | No | No | No | No |
|  18.2 Any miscellaneous suggestions? | No | No | No | No | No | No | No | No |
|  18.3 Are there any bottlenecks into which we may not currently have visibility? | No | Libp2p design causing problems | No | No | Phase 1 to phase 2, BLS standard | Naive implementation, slow code, brittle cli | No | No |
|  18.4 What can we do to provide you with adequate support? In other words, how can we make your life easier? | No test format changes | No test format changes | - | - | - | list optimizations, create “slow network” configuration | - | - |
|  18.5 In terms of tooling, what are we currently lacking? | Network/chain monitors | - | Interop network tests, large scale testing, differential fuzzing | Decode encrypted payloads with wireshark or tcpdump | Network monitor/stats, hive for eth2. A stable eth1 light client | No | Network monitoring tools (libp2p, Eth2) | No |
|  18.6 Notes shared in followup questions | Hopefully, we will have a discovery v5 client working this week. We don't have a detailed guide on how to use our client for interop. But I don't think it's necessary since one of us will be on site. |  | We have made Lighthouse interop documentation [here](https://sigp.github.io/lighthouse-interop-docs/interop.html). Hopefully this is helpful, keen for feedback. |  |  |  |  |  |
