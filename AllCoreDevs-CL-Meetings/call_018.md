# Ethereum 2.0 Implementers Call 18 Notes

### Meeting Date/Time: Thursday 2019/5/23 at [14:00 GMT](https://savvytime.com/converter/gmt-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/mar-28-2019/2pm)
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/43)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=dw2GmEuLr5k&)

----

# 1. [Testing Updates](https://youtu.be/dw2GmEuLr5k?t=417)
* Protolambda
  * Slow week with NY blockchain week, helpful to get together with implementers
  * Epoch transistions, sanity tests, want clients to create test runners and get feedback
  * Tests are currently on separate branch, soon to be released
* Mikhail
  * keccak256 still used in BLS test vectors
* Danny - this was likely a mistake,
* Protolambda
  * Loading configuration files: compile-time vs runtime
* Mamy
  * Nimbus discussed this at length - for now using compile-time constants, not through YAML
  * Reconsidering in future for users, don't want them have to recompile everytime
* Paul
  * Our approach has been to make our types generic across different size array lengths, so we're specifying sets of layouts so it's a mix
* Danny
  * Configurable constants validity condition accompanies this, currently enumerating those in a branch
  * Constants will likely live in a test repo for now

* Antoine
  * Testing jenkins instance for building docker files for Lighthouse, Prysm, Artemis for nodes on a simulated testnet
  * Working without discovery, just for connection. Next step is peer and sync
  * Format build by Whiteblock - network delays, easy to recreate real world simulations
* Danny
  * Another initial fuzzing test targeting Go and Py specs, overtime will integrate more clients

# 2. [Client Updates](https://youtu.be/dw2GmEuLr5k?t=1117)
* Parity - Wei Tang
  * Up to date with 0.6 spec
  * Basic validator implementation running - one potential issue with BLS implementation: some rare cases where library is deemed invalid
* Harmony - Mikahil
  * Finished 0.6 spec, passing all current tests, need to check out issues with BLS
  * Almost finished work on networking stack (wire proctocol, sync online mode, CLI interface for nodes)
  * Nodes falling apart after running several hours - mostly related to consensus
  * Too difficult to store public keys and compress them each time
* Pegasys - Jonny
  * Lot of planning for interop lockin
  * Implementation of watching validators register; Timing mechanism is now swappable for testing different ones
* Nimbus - Mamy
  * Slow weeks - several people on holiday
  * Networking, forward and backward sync
  * Still working on libp2p
  * Some confusion between keccak256 and SHA256
  * Shuffling and BLS mainnet tests passing
  * Update on ETH 1: new member working networking and reusable parts for ETH 2.0
  * Documentation generator for repo - should be cross language compatible
  * Also working on multi-threading and debugging Nim library
* Prysmatic - Terence
  * Finished up to 0.6 spec, working on how to use and optimize in testnet
  * Updating SSZ and trie hashing
  * Investigating BLS alternatives
  * Possible colaboration with Whiteblock for p2p
* Lodestar - Cayman
  * SSZ and BLS (switched to Milagro) tests passing for 0.6, soon state transtition tests and shuffling
  * Landed first version of gossipsub, reviewed by libp2p team - haven't integrated yet
  * Working on simulations running end to end
  * Collaborating with Yeeth team to convert Lodestar components to WASM
* Lighthouse - Luke
  * Almost up to date with 0.6
  * Implemented parses of EF tests, added some provisions for future fuzzing - passing majority of tests
  * Progress with Discovery V5, inital implementation with Rust libp2p
  * Refactored database wrapper for optimizing for state storage and will be fuzzing more components
* Trinity - Hsiao-Wei
  * Working on beach chain validator functionality, adding block sinking process on devp2p
  * Progress on Discovery V5 - implemented encryption-decryption functions from spec
  * Updating deposit contract

# 3. [Research Updates](https://youtu.be/dw2GmEuLr5k?t=2083)
* Vitalik
  * [V2 of Phase 2 proposal](https://notes.ethereum.org/w1Pn2iMmSTqCmVUTGV4T5A?viewPhase#)
  * Instead of maintaining large array of state for every shard, 32 byte hash takes that place
  * Full state can be abstracted across different execution environments
  * Despite more abstraction it's simpler based on how it lets you abstract things - ex: no need for 1 standard rent scheme - allows for
  alot more experimentation and design flexibility
  * Happens to provide a nice slot for ETH 1.0
  * Knowns and Unknowns:
    * Known - fundamentally possible to fulfill vision - complexity doesn't seem to increase with 2 layers over 1
    * Unknown - efficiency benefits from 1 type of committee over 2 types
    * Unknown - challenges in fragmentation over different environments - harder or easier to upgrade? - Censorship attacks
    * Unknown - 2 layer structure economic design for fee markets
  * Discussion of [SSZ partial for light clients](https://youtu.be/dw2GmEuLr5k?t=2883)
* Olivier (Pegasys)
  * Finishing Handle paper (scalable BFT network aggregation protocol) - discovered and corrected some attack vectors
  * Working on blog post series on PCP

# 4. [Network](https://youtu.be/dw2GmEuLr5k?t=3509)
* Zak
  * Finished intial test series on gossipsub - will share data and results shortly
  * Started Discovery V5 and writing light client
* Mike - Libp2p
  * Putting a lot more effort into specs since it's a big barrier for implementers
* Zak
  * We're going to want a more solidified spec for libp2p for future implementers and we also need numbers for message sizes (avg, max)
  for adequate pre-production testing

# 5. [interop lockin](https://youtu.be/dw2GmEuLr5k?t=3955)
**Joseph:** Ongoing discussion over interop concerning: Why not libp2p first? Why minimum wire protocol for interop?

**Jonny:** HackMD document attempting to outline with interop might look like with clients talking to eachother over libp2p. Mostly to simplify things
  and attempt to establish a baseline for node communication

**Adrian:** if strip out higher level protcols of libp2p we're mostly working with TCP transport and multistream. Why can't we use basic
  libp2p with this functionality?

**Zak:** that should work, we just need everyone to interpret messages the same way for consistent execution.

**Mikerah:** [minimal libp2p implementation doc](https://github.com/ethresearch/p2p/issues/4) available for reference

**Adrian:** libp2p should already be interoperable (Rust, Go, Javascript) off the shelf

**Felix:** spec for frame format that multistream uses?

**Adrian:** yes

**Felix:** is there a way to remove the multistream for testing purposes?

**Paul:** could they not just bind into the daemon?

**Mike:** yeah, we built the daemon version of libp2p specifically for languages without libp2p implementation would be able to interop

**Zak:** do we want to benchmark libp2p against devp2p? Right now we're testing gossipsub, floodsub, and plumbtree across both

**Kevin:** I don't think the bindings are the most complicated part. The troublesome part is additional features like peers connecting

**Zak:** another issue people have had is peers added to the routing table without any routeable IP address in libp2p. DiscoveryV5 should
  account for that

**Felix:** we should have an evolving spec for the lower protocol and not just point people to libp2p

**Mike:** we've actually been trying to specify what a libp2p 1.0 looks like implmented so perhaps we can contribute


# Attendees
* Danny Ryan (EF/Research)
* Adrian Manning (Lighthouse/Sigma Prime)
* Alex Stokes (Lighthouse/Sigma Prime)
* Antoine Toulme (ConsenSys)
* Ben Edgington (PegaSys)
* Brett Robertson (Cat Herders)
* Carl Beekhuizen (EF/Research)
* Cayman
* Chih-Cheng Liang (EF/Research)
* Daniel Ellison (ConsenSys)
* Daniel
* Felix Lange (fjl) (EF/geth)
* Greg Markou (ChainSafe)
* Hsiao-Wei Wang (EF/Research)
* Kevin Mai-Hsuan (EF/Research)
* Jacek Sieka (Status/Nimbus)
* Jannik Luhn (Brainbot/Research)
* Jonny Rhea (Pegasys)
* Joseph Delong (PegaSys)
* Leo (BSC)
* Luke Anderson (Lighthouse/Sigma Prime)
* Mamy Ratsimbazafy (Nimbus/Status)
* Matt Garnett
* Matthew Slipper (Kyokan)
* Mike Goelzer (libp2p)
* Mikerah (ChainSafe)
* Mikhail Kalinan (Harmony)
* Nicolas Gailly (PegaSys)
* Nishant Das (Prysmatic)
* Olivier Begassat (ConsenSys)
* Paul Hauner (Lighthouse/Sigma Prime)
* Preston (Prysmatic)
* Protolambda (EF)
* Steven Schroeder (PegaSys)
* Terence Tsao (Prymatic)
* Trenton Van Epps (Ethereum Cat Herders)
* Weather Cam?
* Wei Tang (Parity)
* Vitalik Buterin (EF/Research)
* Zak Cole (Whiteblock)
* Meeting notes: Michael LaCroix
