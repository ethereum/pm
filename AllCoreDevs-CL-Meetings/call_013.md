# Ethereum 2.0 Implementers Call 13 Notes

### Meeting Date/Time: Thursday 2019/2/28 at [14:00 GMT](https://savvytime.com/converter/gmt-to-germany-berlin-united-kingdom-london-ny-new-york-city-ca-san-francisco-china-shanghai-japan-tokyo-australia-sydney/feb-14-2019/2pm)
### Meeting Duration: 2 hours
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/31) 
### [Audio/Video of the meeting](https://youtu.be/0ZWG8hMbxes)

# Agenda
1. Testing Updates [_(3:00)_](https://youtu.be/0ZWG8hMbxes?t=181)
2. Client Updates
3. Research Updates
4. Phase 0 Wire Protocol
5. Serialization
6. Spec discussion
7. Open Discussion/Closing Remarks

# 1. Testing Updates
* _Notes: [3:00](https://youtu.be/0ZWG8hMbxes?t=181)_
  * Shared simplified fork choice test, abstract, not mentioning data structures. Most people seem to think this is better to reason about. Also shared ideas on state tests.  
  * Desire to have Prysmatics chain start tests in ETH 2.0 reference tests - Terence said he could add PR  
  * Whiteblocks is opensourcing testing and simulation  
  * BLS references tests are somewhat broken - serialization format is incorrect

# 2. Client Updates
* Pegasys - Steven [_(8:25)_](https://youtu.be/0ZWG8hMbxes?t=505)  
  * Upgrading to spec 0.4 
  * Have simulated blocks from a mock network adaptor executing state transition and fork choice rule
  * BLS largely working
  * Working to integrate other tools from Pegasys  
* PyEVM/Trinity - Hsiao-Wei Wang [_(9:29)_](https://youtu.be/0ZWG8hMbxes?t=569)  
  * On spec 0.4  
  * Testnet starting with devp2p network  
  * Working on python daemon libp2p binding  
* Prysmatic - Raul [_(10:40)_](https://youtu.be/0ZWG8hMbxes?t=640)  
  * On spec 0.4 aside from small bug fixes  
  * Working on simple testnet: 8 validators and beacon node  
  * Caution on working with committees at start of epoch. Lots of weird boundary conditions  
  * Adding cache layers  
  * Finished implementing initial sync of beacon node  
  * Working towards testnet  
* Nimbus - Mamy [_(12:22)_](https://youtu.be/0ZWG8hMbxes?t=742)  
  * Working towards testnet - primary missing piece is fork-choice
  * Targeting spec 0.3 to reduce impact of changes  
  * Full sync of initial beacon chain  
  * Progress on libp2p  
  * BLS in pipeline  
  * Presentation at ETHCC on tests and simulation to highlight tools for testnets  
* Lodestar - Greg [_(15:47)_](https://youtu.be/0ZWG8hMbxes?t=947)  
  * Done porting BLS from WASM  
  * Finished state transitions  
  * Aiming for simulations in the next week  
* Harmony - Mikhail [_(17:25)_](https://youtu.be/0ZWG8hMbxes?t=1045)  
  * Added support of configuration files, passing beacon chain parameters in YAML
  * Working towards 0.4 spec  
  * Merged OS license  
  * Stabilizing validator behavior  
* Parity - Wei Tang [_(19:13)_](https://youtu.be/0ZWG8hMbxes?t=1153)  
  * Launched simple testnets for CasperFFG, using to benchmark 
  * Updating to 0.4 spec - have committee shuffling, haven't integrated into state transition function  
* Yeeth - Dean [_(21:35)_](https://youtu.be/0ZWG8hMbxes?t=1295)
  * Updated to 0.4 - working on refactoring  
  * Trying libp2p headers in Swift  
  * BLS compiling properly, might use different library  
* Lighthouse - Adrian [_(22:26)_](https://youtu.be/0ZWG8hMbxes?t=1346)  
  * Cacheing committee info for processing blocks with 16,000 validators  
  * Building fork choice test framework and core network syncing and service infrastructure  
  * PR for Rust libp2p gossip sub implementation in progress  

* _Intros:_   
  * Mike Goelzer from Protocal Labs working on libp2p - just getting a pulse on ETH 2.0 development  
  * Matt Slipper from Kyokan - wrote Phase 0 wire protocol and the "State of ETH 2.0" report  

# 3. Research Updates  
* Justin Drake - [_(25:43)_](https://youtu.be/0ZWG8hMbxes?t=1543)  
  * Created meta issue "Misc Beacon State Changes" to keep track of remaining issues to change for Phase 0  
  * Possibly working towards executable spec vs human readable (current) - Submitted 10 ETH bounty, Protolambda is working on it in Go
  * Want to return to SHA256 design decision - many projects are moving towards SHA256, but there are security concerns  
  * Need standardization on hash functions for standardization on BLS - in context SHA256 would help with this  
  * Helpful to remember whatever we choose isn't absolutely permanent, it just needs to serve us well for the next several years  
  * Looking into SHA256 security - length extension attack & academic security reductions  
  * Recently discovered ETH 2.0 light clients might be more valuable than previously thought. Potentially DOS attack on fork choice rule that light clients could navigate.  
* Felix Lange [_(31:53)_](https://youtu.be/0ZWG8hMbxes?t=1913) - Is SHA3 being considered at all since it's much more widely available in terms of implementations?  
* Vitalik - One major desideratum for hash functions is, unfortunately, easy executability within ETH 1.0 because the contract needs to be able to generate Merkle branches. Haven't considered SHA3, have considered BLAKE2 since Zcash may've used this at some point. Gas efficiences in ETH 1.0 become a hurdle with these considerations.  
* Felix - no real problem with adding a primitive for any hash function.  
* Vitalik - fair point. If we did go with a more progressive hash function, BLAKE2 might actually be our best option.  
* Felix - adding primitives doesn't decrease security of EVM at all. If any hash function needs to be added, it could be added. Agree that it may add significant development time.  
* Danny - worth considering that SHA256 is basically becoming a blockchain standared which is important to consider for interoperability. Even though SHA3 is industry standard, it's not blockchain standard.  
* Ben - offered multi-hash from Protocal Labs - is this being considered?  
* Vitalik - multi-hash just offers a choice of hash which is a problem for blockchains which require standard usage
* Discussion over the merits of multi-hash and interoperability of various hash functions between Cosmos, Polkadat, ETH 1.0, ETH 2.0  
* Danny - recap [_(45:26)_](https://youtu.be/0ZWG8hMbxes?t=2726)  
  * getting a security briefing on SHA256  
  * explore BLAKE2 in ETH 1.0, but don't count on it  
  * while potentially supporting many hash functions, we need to have ETH 1.0 compatability, ie SHA256 or keccak256  
  * continuing to consider multi-hash  
* Vitalik - [_(46:47)_](https://youtu.be/0ZWG8hMbxes?t=2807)  
  * wrote updated PR 682 for PoC game - game unchanged, moved state objects out of validator records  
  * overview of current Phase 0 and Phase 1 - see spec
  * Opened [Issue 686](https://github.com/ethereum/eth2.0-specs/issues/686) for final thoughts on Phase 1
  * Opened [Issue 702](https://github.com/ethereum/eth2.0-specs/issues/702) to explore Phase 2 thinking  
  * [Issue 701](https://github.com/ethereum/eth2.0-specs/issues/701) to illustrate some CBC thinking  
  * Experimented with writing Phase 1 in python than bullets. It seems to have worked. Will open PRs to do similar with Phase 0  
* PegaSys [_(54:55)_](https://youtu.be/0ZWG8hMbxes?t=3295)  
  * discussing how to integrate signature aggregation framework into Artemis  
  * testing quick transfer protocol
* Vitalik [_(57:05)_](https://youtu.be/0ZWG8hMbxes?t=3424)- asking for benchmark numbers from validators and shared some optimized code 
  * several teams have had slowdowns with updated validator shuffling  
  * suggestion to create issue with all benchmarks questions and individual benchmarks reached  

# 4. Phase 0 Wire Protocol  
* Matt turned Wire API into Wire Protocol
* Matt [_(1:08:51)_](https://youtu.be/0ZWG8hMbxes?t=4125) - answers previous RSA question regarding libp2p, key pairs, and node identification  
* Felix - unclear what level this is sitting at  
* Matt - I added some additional context concerning libp2p  
* Felix - understood. Perhaps these don't belong in the same spec since they're referencing different levels  
* Raul - there's some misunderstanding with how the messages are being passed - I made some comments today.  
* Felix - today we just need to agree on the high level structure of how messages are passed and can work out the specific details in later spec or libp2p multistream.  
* Frank's question - where ENRs VS Multiadders come into play?  
  * Felix - ENRs are more for discovery on our side. Maybe spec should document its assumptions? What does a node need to speak with another protocol - list these out. 
* Danny - next week we'll try to come with a 0.2 draft of ENR addressing the comments and go from there

# 5. Serialization  
* Felix [_(1:17:53)_](https://youtu.be/0ZWG8hMbxes?t=4666)  
  * Sane option seems to be consensus should be encoded using a seed. How messages are encoded may be left to individuals. It's freeform making it easier to decode.  
* SOS and SSZ does have some advantages - have specific back offsets
* Raul - Y shard is something we'd like to see. Libp2p team doesn't have capacity to integrate right now. Happy to help as he's able. 
* Danny - previous decision was made because it works for consensus. It's not optimal, but it's something simple to work with for now. 
* Further discussion on merits of SOS, SSZ, and RLP [_(1:22:25)_](https://youtu.be/0ZWG8hMbxes?t=4947) 

# 6. Spec discussion
* Felix [_(1:33:07)_](https://youtu.be/0ZWG8hMbxes?t=5577) - published a draft spec in devp2p repo. Complete spec once topic discovery spec and ENR spec are added. Working on implementation - basic structure, no code to share yet. Difficult to follow discussions because p2p discussions are held in several places. Want to move to devp2p repo to better organize discussion.  
* Danny - question on wire protocol spec regarding adding more topics vs fewer. Any performance issue on finding peers for sub-topics vs larger topics?  
* Felix - they're distinct enough topics for topic based index  

* Danny - heads up, we're planning on a gathering of breakout sessions at EDCON in Sydney with various topics
