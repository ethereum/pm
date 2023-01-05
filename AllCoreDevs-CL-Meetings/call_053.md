# Ethereum 2.0 Implementers Call 53 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2020/12/2 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  1 hr <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/193) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://youtu.be/8mE--yxMZtk) <!-- omit in toc --> 
### Moderator: Danny Ryan <!-- omit in toc --> 
### Notes: Edson Ayllon <!-- omit in toc --> 


-----------------------------

# Contents <!-- omit in toc --> 

- [1. Testing and Release Updates](#1-testing-and-release-updates)
- [2. Testnet/Mainnet](#2-testnetmainnet)
- [3. Client Updates](#3-client-updates)
  - [Nimbus](#nimbus)
  - [Lodestar](#lodestar)
  - [Prysm](#prysm)
  - [Teku](#teku)
  - [Lighthouse](#lighthouse)
  - [Nethermind](#nethermind)
- [4. Research Updates](#4-research-updates)
  - [Weak Subjectivity](#weak-subjectivity)
  - [Vitalik](#vitalik)
  - [TXRX](#txrx)
  - [Justin Drake](#justin-drake)
  - [Leo (BSC)](#leo-bsc)
- [5. Networking](#5-networking)
- [6. Spec discussion](#6-spec-discussion)
- [7. Open Discussion/Closing Remarks](#7-open-discussionclosing-remarks)
- [Annex](#annex)
  - [Attendees](#attendees)
  - [Next Meeting Date/Time](#next-meeting-datetime)

-----------------------------


# 1. Testing and Release Updates

Video | [0:26](https://youtu.be/8mE--yxMZtk?t=26)
-|-

Mainnet launched. It is running stable. 

Nothing new for testing releases. We do have testing reforms we want to do. And fork-choice things we want to get in. In progress.

Some specification work related to upgrades we want to see early on. One is adding lightclient sync committee. Might release test vectors for that in January.

Proto has been working on API bindings and surface vectors. Reach out to protolambda if you want to talk about API tests.

Very close to a release on those APIs. If you are actively using the APIs, and see some open issues you'd like included, please reach out.




# 2. Testnet/Mainnet

Video | [5:41](https://youtu.be/8mE--yxMZtk?t=341)
-|-

Testnet looks good. Mainnet looks good.

Terence asks if there exists a testnet with finality disabled. This is to design more optimizations around finality. 

The group thinks this is high priority. When there is forking an non-finality, clients don't prune. Non-finality without forking doesn't produce the same issue. Target is for early January.

Another case may be testing when there are no block at all. Testing for an entire epoch, for stability.

Pyrmont work, at least until the end of January, there's no need to disrupt it. Over time, it may degrade. We could tune some parameters so under certain loads, it stabilizes quickly. Pyrmont is good enough for the next 2-3 months, but we may consider our options and do a restart in the next year. 

We may consider adding weak subjectivity sync to Pyrmont. 



# 3. Client Updates

Video | [14:35](https://youtu.be/8mE--yxMZtk?t=875)
-|-

## Nimbus

- Still have work to do in documentation
- Hotfix scheduled today
- Want to thank supporters, will have something for Gitcoin supporters soon
- Still using import and export of slashing databases v3. Plan on v5 soon
- On networking, raised number of peer requestion for 79 to 160. Have much better attestation aggregation relay
- Concerned with drop of Lighthouse clients on P2P connection, while Teku and Prysm are stable
- Team at BLST released signficant improvements to the describer function. Translates to roughly 15% improvement to all clients using BLST
  
## Lodestar

- Released BLST integration
- Working on getting BLST to compile to WASM, waiting to see performance results
- Made a release day before mainnet. Lodestar is at experimental level robustness
- Have nodes (no validators) on mainnet, with some performance issues, however, staying on the network

## Prysm

- Working on documentations before mainnet, and fixing user reported bugs.
- Post mainnet, working on import and export validator client exchange format.
- Working on weak subjectivity link
- And implementing Eth2 API

## Teku

- Released weak subjectivity checkpoint link feature. Can get a node running in under a minute
- Implmented historical sync
- Fixed an issue where attestation sometimes failed on the first slot of an epoch on Pyrmont
- Remaining issue on delayed block production
- Fixed issue where we failed to gossip voluntary exits
- Main work post mainnet launch was to pull data more reliably from mainnet nodes, which proved different from Georli

## Lighthouse

- Launched on mainnet, will post updates later.

## Nethermind

Nodes that can serve Eth2 can go to 100 GB. Only need reciepts following the deployment of the deposit contract.

Beam-sync client can serve requests with a smaller footprint. If deposit contract receipts could be bundled and verified, which could work with LES protocol.

# 4. Research Updates

Video | [28:56](https://youtu.be/8mE--yxMZtk?t=1736)
-|-

## Weak Subjectivity

There's a new weak subjectivity calculation where the period also depends on the average validator balance. Will look to get merged next release.

Have been working on slashing protection rebuild. Clients don't support v5 of the slashing interchange format yet. Also uses the Eth2 API. 


## Vitalik

A couple of PRs in progress. Including the light client, and the incentive accounting reforms. Takes simplifications to rewards introduced in the large Phase 1 candidate and moves them to a separate cache which could be included more quickly. 

There's a couple of wishlist items:
- Redesign the spec so empty epochs and long strings of empty epochs don't have O(N) processing time
- Reforming how the inactivity leaks work
- Using polynomial commitments to remove most of the merkeling overhead from epoch transitions

These exist as scattered issues, but will publish a more coherent document that covers these. 

Most clients are already optimizing the epoch transition in a way that's similar. 

## TXRX

Executable beacon chain proposal has been published. 

There are some pain point to address, such as what hash issue. In the meantime, the prototype is already in progress. The goal is to imlement and validate the core proposal.

## Justin Drake

Regarding BLST. An optimization was found for doing square roots over the extension field. This results in hash to g2 will be 40% faster. Translates to 15% speed upgrade in signature verfication.


## Leo (BSC)

With respect to the figures from last meeting, written a document which shows things found. Shared this with a few, and recieved feedback. 


# 5. Networking

Video | [37:05](https://youtu.be/8mE--yxMZtk?t=2225)
-|-

Have been discussing having a call next week, tentatively Wednesday morning. There is still an outstanding PR regarding weak subjectivity sync, and what is a good and bad node in this respect.

**Jacek:** It's good to not have very low peer settings. It makes it harder to find clients, and degrades the network performance in general.

**ProtoLambda:** There was a recent issue on improvements that can be made on connecting onboarding. 

**Danny:** So essentially, allowing for elasticity on the upper end, and on some interval pruning down to a target number, rather than having a hard limit on a target number.


# 6. Spec discussion

Video | [40:25](https://youtu.be/8mE--yxMZtk?t=2425)
-|-

Vitalik will publish a document on incentive accounting, empty slot optimizations, and other optimizations. It's better to start these discussions sooner than later to get it into a fork in a reasonable amount of time.

Big things in R&D are data availability, sharding, and merge spec. Over the next few weeks, these will go into implementation and testing to form more complete specs. Will be leveraging some new cryptography called Kate committments. 

A question on BLS is how to define the API to make best use of the library. 

Another thing to think about is we'll need specific BLS tools optimized for Kate based availability sampling. 

In terms of low hanging fruit, light clients are easy to implement. The PR is up on the specs repo.

# 7. Open Discussion/Closing Remarks

Video | [40:25](https://youtu.be/8mE--yxMZtk?t=2961)
-|-

No discussion.

------

# Annex 


## Attendees 

- Aditya Asgaonkar
- Alex Stokes
- Ansgar Dietrichs
- Barnabe Monnot
- Ben Edgington
- Carl Beekhuizen
- Cayman Nava
- Dankrad Feist
- Danny Ryan
- Hsiao-Wei Wang
- Jacek Sieka
- Justin Drake
- Lakshman Sankar
- Leo (BSC)
- Mamy
- Mikhail Kalinin
- Nishant
- Pooja Ranjan
- Protolambda
- Raul Jordan
- Sacha Saint-Leger
- Terence (Prysmatic)
- Vitalik Buterin



## Next Meeting Date/Time

Thursday, December 17, 2020.
