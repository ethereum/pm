# Consensus Node Bandwidth

With PeerDAS on the horizon and our goal to increase the global blob count, bandwidth requirements for Ethereum consensus nodes is becomming an important concern. This session will discuss the current state of consensus node banwidth usage, estimated usage with PeerDAS and current and future research/plans to handle bandwidth in consensus nodes.

**Facilitator:** Adrian Manning
**Note Taker:** Jimmy Chen
**Pre-Reads:**
1. https://blog.sigmaprime.io/peerdas-distributed-blob-building.html
2. https://ethresear.ch/t/gossipsub-topic-observation-proposed-gossipsub-1-3/20907
3. https://hackmd.io/@ttsao/get-blobs-early-results
4. https://hackmd.io/@dknopik/epf-week16?utm_source=preview-mode&utm_medium=rec (and probably week 17)

**Useful Image**: 

(IDONTWANT usage in Lighthouse)
![IDONTWANT](https://hackmd.io/_uploads/B1wnE1Kbkl.png)

(Peers per protocol)
![peers_per_protocol](https://hackmd.io/_uploads/Sk8-qh3Wkl.png)

(Duplicates Filtered)
![duplicates](https://hackmd.io/_uploads/BkCwjn2WJe.png)


## Agenda

1. **Current state of bandwidth on consensus nodes:** We will discuss an overview of what current bandwidth looks like and show estimates for future upgrades to get a scope of the landscape
1. **IDONTWANT - How's it going?:** Have a look over the current state of the IDONTWANT message and whether it has helped, decide on any modifications. i.e send per-topic, per-message, with publish etc. 
1. **PeerDAS - How much more bandwidth?:** Discuss estimates for PeerDAS, what we expect on the network and if we are ok with the constants being chosen and bandwidth costs.  [[4]](https://hackmd.io/@dknopik/epf-week16?) 
1. **Fetch blobs from the EL:** Fetching blobs from the EL is an optimization strategy that appears to help. Discuss if we can improve this and expectations going forward. [[1]](https://blog.sigmaprime.io/peerdas-distributed-blob-building.html) [[3]](https://hackmd.io/@ttsao/get-blobs-early-results)
1. **Execution layer blob mempool** - This potentially could be researched and may give improved bandwidth. Worth discussing. 
3. **Gossipsub 1.3:** A proposal to improve gossipsub which additionally may help reduce bandwidth. [[2]](https://ethresear.ch/t/gossipsub-topic-observation-proposed-gossipsub-1-3/20907)
4. And Beyond - Open discussion about potential new proposals others may have and general closing remarks. 

# Notes

## Gossip 1.2 IDONTWANT messages

- LH detects 54% of nodes on mainnet today supports IDONTWANT
- `IDONTWANT` usage in Lighthouse
    - No sigificant change since `IDONTWANT` added to Lighthouse
    - A recent PR with `IDONTWANT` message cutoff was expected to improve this
        - `IDONTWANT` is only sent to peers when the message reaches a specified size
- Duplicate messages are causing excess bandwidth
    - still lots of duplicates with `IDONTWANT`
- Daniel presented simulation using Shadow
    - Uses full clients in simulated setups on a single machine
    - It works by slowing down time as long as much as you want
    - 1000 nodes with 1 hour
        - used 4 hours of real time for the simulation
        - compared bandwidth with / without IDONTWANT
            - 3/6 blob count, `IDONTWANT` only shows 3kb/s less bandiwdth consumption
            - note there's limitation in shadow it cannot correclty simulate the time taken to compute things - it's able to simulate latency and bandwidth
        - simulated a network that mirros mainnet geogrpahic and client distribution
    - Currently clients don't have ability to stop sending in-flight data, if `IDONTWANT` received from peer half way through
    - Csaba talked about Message gossip "diffusion": potentially switching from "push" to "pull" approach - could reduce bandwidth
        - e.g. If message received early (relative to time in the slot), send to more nodes
- `episub` calculates statistics based on messages received from peers
    - determines optimal mesh, and adjust mesh peers dynamically based on data
    - very complicated and hard to get right
    - Gossipsub 1.2 today: mesh peers are computed statically
- `IDONTWANT` initially showned 30% reduction in bandiwdth usage (data from Anton)
- `IDONTWANT` seems to be more effective on high latecny nodes (node in Australia received less duplicates than node in Germany)

## PeerDAS

- Increases proposer bandwidth requirement and usage
- `getBlobs` to reduce proposer bandwidth 
    - Prysm has seen great improvements with Geth
    - Lighthouse didn't see much improvements on block avaialbility time
    - EL implementation and response time will be key to effectiveness of getBlobs
- Node Crawler from ProbeLab
    - Measure upload bandwidth of each node on the network
    - Presented some metrics that showed different regions, cloud/non-cloud, RPC response size shows different bandwidth capacity
    - 20 mpbs 

## Gossipsub 1.3 Idea

- Pop presented a new approach to have "observing" behaviour in additional to the current "subscribing" behaviour.
- No simulation yet, but it has a high guarantee that the node only received one copy of the message
- Limitation is that observing node doesn't contribute to the gossip network.

## Discv5 crawler by Csaba 

- Measured response time when sending `FINDNODE` UDP packets to bootnode
    - compared time distance between UDP packets
    - collected thousands of ENRs in 10 seconds
    - 200k+ ENRs on the DHT
- Graph showing:
    - RTT latency distribution across thousands of nodes
    - bandwidth distribution (with majority below 20Mbps, and some above)
- Tested using 2Gbps bandwidth from Italy :open_mouth: 

## Open Discussion

- Latency (propagation speed) vs Bandwidth usage optimisations
    - Some improvement proposals like episub optimises for one thing but sacrifices the other

---

## Breakout #2

### Blob Count Increase & `IDONTWANT`

- 4/6 or 6/9?
- Need more test data!
    - Prysm 5.2 has `IDONTWANT`
    - Lodestar seeing degraded performance on holesky seeing (receiving) a lot of `IDONTWANT`
        - Could be Lighthouse, PR to introduce 1kb cutoff was only merged recently, so it's sending lots of messages
    - When is `IDONTWANT` sent?
        - after receiving if message size > 1kb (in spec)
        - on publish (WIP spec PR)
    - check and finetune metrics
        - it would be useful to track "client versions per mesh"
    - is 1kb cutoff a good size?
- Does Nimbus send `IDONWANT`? We see a client with unknown protocol id sending these messages

### Yannis's topics

1. Dynamic message difussion
2. Different versions of gossipsub for topics?
    - e.g. `IDONTWANT` could be configured per topic?
3. Topic observation and control messages

#### Observations

- Duplicates of messages seem to be received closer to end of slot?
    - Csaba: it makes sense to differentiate between topics, e.g. PeerDAS
    - Age: doing it based on time could be dangerous. If we add `hop_count` when forwarding messages, then we know the hop count 0 is. But if `validator custody` is going to reduce annoymonity anyway, then it migth be useful to put it in.
    - We should look into this

### Pop's Gossip v1.3 (observers)

- observing node receives IHAVE
- observing node send IWANT to the first peer that sent IHAVE
- observing node gets the message
- pros: less bandwidth and only receives one copy
- cons: downside is higher latency

Q: is it possible that one faster node would be sending more than others? 
- we can limit the number of connected observing nodes 

There are some nodes sending `IWANT` to everyone
- could be the `go` impl, but we should look at all clients

Yannis wil compile a list of things to look at in the next round of testing and publish the results later.

### Staggerred Publishing

- Sending to some peers first, and more peers later
- Age submitted a PR to rust-libp2p but wasn't accepted

### Different versions per topic

- diff mesh peers per topic would be useful for peerdas
- **ACTION:** we'll put some of these items into issues / PRs on the repos (libp2p / consensus-specs)

### PeerDAS metrics

- current process a bit adhoc, is there a good way to do it? libp2p-spec vs beacon-metrics?
    - some libp2p metrics are not ethereum-specific

