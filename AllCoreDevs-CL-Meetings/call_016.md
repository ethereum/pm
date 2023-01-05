# Ethereum 2.0 Implementers Call 16 Notes

### Meeting Date/Time: Thursday 2019/4/18 at [14:00 GMT](https://savvytime.com/converter/gmt-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/mar-28-2019/2pm)
### Meeting Duration: 1.25 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/37)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=eN_O8bSaS5Q)

----

# 1. Testing Updates [_(8:40)_](https://youtu.be/eN_O8bSaS5Q?t=517)
* Diederik - working in integrating tests in specs repo to trigger CI. Several tests including state transition.

# 2. Client Updates [_(10:26)_](https://youtu.be/eN_O8bSaS5Q?t=626)
* Pegasys - Jonny Rhea
  * almost at 0.5.1 spec - lots of network debugging
  * planning a workship during Blockchain Week
  * generating test data for contracts
* Parity - Wei Tang
  * Merkle database implementation for storing in local database
* Lodestar - Greg Markou
  * Branch tracking V6
  * Everything wired up - ready to test single node processing empty blocks
  * libp2p well on its way
  * close to syncing with Artemis
  * PoC / MVP of validator client (currently stateless)
* Nimbus - Mamy
  * Testnet launch - good feedback from community so far
  * Optimized state transition due to memory leaks
  * 2 testnets. Public - "Testnet0"  &  one for development
  * Improved sync efficiency
  * Testnet issues with net traversal - wrapped the mini UPnP
  * Some work on Whisper
  * Eagerly waiting for SSZ tests since cacheing is needed to pass state tests
* Harmony - Anton
  * Updated to 0.5.1 spec
  * Passing all tests minus a couple state transistion tests
  * Implmented incremental tree hashing - currently benchmarking
  * Started WIRE implementation
* Trinity - Hsiao-Wei Wang
  * most of team in EDCON
  * testnet under construction - testing blocks between validators
  * integrating 0.5.1 tests
* Lighthouse - Adrian
  * passing 0.5.1 state transition tests
  * Paul implemented tree hash caching - should be implemented in runtime next week
  * assisting BLS standardization by benchmarking a new hash curve method
  * lots of bug fixes,
  * started peer management
  * started building tools for large scale network tests
* Prysmatic - Terence
  * primarily working on runtime bugs
  * able to run 128 validators - trying to increase
  * optimizing LMD forkchoice & add caching to shufflings
  * implemented single validator acting as multiple validators with many public and private keys
* Geth - Felix
  * mostly working on discovery - not quite at spec yet

# 3. Briefings from workshop [_(22:32)_](https://youtu.be/eN_O8bSaS5Q?t=1348)
* Paul - client architecture
  * Trying to define a minimal interface between a beacon node and validator client
  * Chatted about JSON vs gRPC
  * Openly discuss caching and optimizing
* Matt - Networking/libp2p
  * things we might like to change with libp2p
  * problems with serialization - will write up something for specs changes and discussing with SSZ team
  * resurrecting Whiteblock tests for gossipsub under load - biggest hurdle to wider gossipsub adoption
  * need to discuss needed changes to peer discovery for ETH 2.0
* EWASM
  * reinforced primary goals of EWASM
  * main challenges are metering and bounding execution
  * ease of formal verification with KEVM
  * interoperability with other chains
* Vitalik - Light clients
* Testnets & Roapmap
  * conditions for long standing multi-client testnets
  * building out network testing and monitoring tools
  * standardization efforts
* Vitalik - Phase 2
  * primarily whiteboarding
  * WASM
  * cross shard communication
  * Rent, State, and Merkle
  * general form feels largely figured out

# 4. Research Updates [_(32:36)_](https://youtu.be/eN_O8bSaS5Q?t=1946)
* Justin
  * team has consensus on spec freeze come end of Q2
  * lots of simplifications done and coming for depositis, incentivization, crosslinks, serialization, abstraction, SSZ...
  * BLS standarization is moving forward - having fortnightly calls (Algorand, EF, Chia, Ledger)
  * looking at constant time hash functions
  * consensus on moving transfers to Phase 1 - aiming for slower and steady approach and signals that it's still under major testing
  * working on invariance in state environments - running tests
  * looking at transaction abstraction - everything could be a contract (still an idea)
* Vitalik
  * thinking about fast cross shard transactions - largely in layer 2 - lot of issues to still work through
    * general approach: have state objects in one shard that store dependecies, so potentially mulitiple copies of state object. Some data structure that determines state object most likely to be correct. The rest are there in case first doesn't work. Challenge is elegancy and ease of working with. One contract called a "hypervisor" and transactions might end up being calls to "hypervisor". "Hypervisor" manages different state objects and which contracts to modify. Seems likely this can all be done at layer 2.
* Danny
  * on tranfers - intention is to launch with max tranfers per block constant at 0. In favor of forking to implement and practice hard-forking mechanism.
* Leo (BSC)
  * bit of academic disemination - gave a couple classes on blockchains and presented sharding

# 5. Network Updates [_(42:04)_](https://youtu.be/eN_O8bSaS5Q?t=2524)
* Discovery - Felix
  * [Discovery v5 spec](https://github.com/ethereum/devp2p/blob/master/discv5/discv5.md) about 95% done
  * Go implementation almost at parity with spec
  * Aiming to test in 1-2 weeks
  * Changed encryption, messages simplified, spec is in 3 parts (wire protocol, theory doc, rationale doc)
* Libp2p - Raul
  * abstractions and core types are being consolidated into a single repo `go-libp2p-core`
* Phase 0 Networking Protocols - Matt
  * Bag of updates to be ready soon - hopefully Tuesday (serialization, block propogation APIs)
* Network Serialization SSZ - Matt
  * limitations of using SSZ - need a predefine schema which doesn't work for RPC Request/Response wrappers - [Issue 861](https://github.com/ethereum/eth2.0-specs/issues/861)
  * also spawned conversation around potentially changing SSZ spec to make it work - [Issue 871](https://github.com/ethereum/eth2.0-specs/issues/871)
    * introduce a null & union type - doesn't completely solve problem. Still adds some helpful functionality
  * not using SSZ for Request/Respone payloads, easier expresses data simply enough
* [Gossipsub tests](https://github.com/Whiteblock/gossipsub-tests) - Zac
  * Whiteblock is reopening performance tests

# 6. Spec Discussion [_(55:22)_](https://youtu.be/eN_O8bSaS5Q?t=3322)
* Danny - want to get 0.6 spec out tomorrow or very soon for testing. Almost entirely bug fixes and simplification. Testing is also simplified.
*Discussion
  * Terence - 3 different scenarios - 1. receive bad block 2. receive block from forked chain 3. receive block from canonical chain - would like to drop bad block, save from forked chain, process normal block
  * Danny - seems sane, still do standard processing
  * Terence - if we ignore block from different proposer and there's a reshuffling and that turns out to be valid proposer
  * Danny - if it's in your tree you can still tell if it's valid so you can process it. If it looks 'not canonical', you might put it in a queue and deal with it later

# 7. Open Discussion [_(1:04:12)_](https://youtu.be/eN_O8bSaS5Q?t=3849)
* Workshop May 16th in New York in between Consensys and ETHNY - primary theme is interoperability
* CI soon and need testing on it

# Attendees
* Danny Ryan (EF/Research)
* Adrian Manning (Lighthouse/Sigma Prime)
* Alex Stokes (Lighthouse/Sigma Prime)
* Ameen Soleimani (Spankchain)
* Antoine Toulme (ConsenSys)
* Anton Nashatyrev (Harmony)
* Ben Edgington (PegaSys)
* Carl Beekhuizen (EF/Research)
* Chih-Cheng Liang (EF/Research)
* Dankrad Feist (HiDoc Technologies)
* Daniel Ellison (ConsenSys)
* Felix Lange (fjl) (EF/geth)
* Greg Markou (ChainSafe)
* Hsiao-Wei Wang (EF/Research)
* Jarrad Hope (Status)
* John Adler (ConsenSys)
* Jonny Rhea (Pegasys)
* Joseph Delong (PegaSys)
* Justin Drake (EF/Research)
* Kevin Mai-Hsuan (EF/Research)
* Leo (BSC)
* Mamy Ratsimbazafy (Nimbus/Status)
* Matthew Slipper (Kyokan)
* Mikerah (ChainSafe)
* Nishant Das (Prysmatic)
* Paul Hauner (Lighthouse/Sigma Prime)
* Raúl Kripalani (Libp2p)
* Terence Tsao (Prymatic)
* Wei Tang (Parity)
* Vitalik Buterin (EF/Research)
* Zak Cole (Whiteblock)
* Meeting notes: Mike LaCroix
