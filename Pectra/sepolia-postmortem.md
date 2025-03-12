# Sepolia Pectra Incident Post-Mortem

Author: Mario Havel

Status: Resolved

Date: Mar 12, 2025, 18:00 UTC

## Current Status 

The Sepolia testnet has fully recovered from the incident that occurred during the Pectra upgrade on March 5, 2025. Following quick identification of the issue, client teams coordinated a response, first mitigating continuous efforts of the attacker while developing and deploying fixes. Within hours of the incident, later the same day, the network was again operating normally, processing transactions, building blocks and finalizing. 

## Incident overview

On March 5, 2025, at 7:29 UTC (epoch 222464), the Pectra network upgrade was activated on the Sepolia testnet. Shortly after activation, validators began experiencing issues with transaction inclusion, resulting in the production of empty blocks. The issue was specifically related to Sepolia's permissioned deposit contract and its interaction with EIP-6110, which changes how validator deposits are handled. Sepolia runs a permissioned validator set gated by a custom ERC-20 token for deposits, instead of regular ETH. EL clients processing events from the deposit contract ran into issues when the contract emitted unexpected ERC-20 related logs. While fixing the problem, an attacker was actively pushing transactions triggering the issue. Core teams prepared the fix and coordinated release while replacing malicious transactions causing empty blocks. The coordinated rollout happened at 14:00 UTC and successfully mitigated any further issues.

> Note that this issue was specific to Sepolia's testnet configuration and could not occur on the Ethereum mainnet.

Despite the incident, the network:
- Never lost finality
- Continued to produce blocks (though empty)
- Was fully restored within approximately 6.5 hours after the issue occurred

## Incident response and fixes

A high-level overview timeline of the incident, a detailed timeline based on developer chat logs is available below.

### Issue identified after Pectra fork (7:30 - 10:30 UTC)

Pectra was activated on epoch 222464, 7:29 UTC. Shortly after, developers and PandaOps noticed empty blocks. Client logs and block tracing revealed issues with processing the custom deposit contract. Teams joined an emergency call, discussed fixes and determined that an uncoordinated rollout would cause a chain split, so they scheduled an update together for 14:00 UTC.

### Fix preparation and attack mitigation (10:30 - 14:00 UTC)

Client teams started to implement fixes in their client. Felix from the go-ethereum team developed a simple fix that ignored erroneous logs coming from the deposit contract. However, during this time, the attacker sending malicious transactions and triggering the issue was still active. Meanwhile, PandaOps actively replaced the triggering transactions with higher-paying ones to allow full block production. However, it's assumed the attacker actually read the public developer channel so some fixes were discussed in private. The attacker could still send transactions to the deposit contract and constantly trigger issues because ERC-20 allows a zero token transfer. The temporary fix was developed in private and deployed to EF DevOps nodes (~10% of network). This allowed at least those nodes to propose full blocks until the coordinated deployment of the fix. 

### Coordinated Deployment (14:00 UTC)

At 14:00 UTC, developers joined another coordination call and all nodes were updated with new client releases containing the proper fix. This was confirmed successful, the chain continued to be stable with regular blocks and previously problematic transactions were included without further issues. 

## Client Releases

Client teams released versions containing hot fixes for the Sepolia issue. All node operators must upgrade their execution layer clients to follow Sepolia:

- Besu: [v25.2.2](https://github.com/hyperledger/besu/releases/tag/25.2.2)
- Erigon: [v3.0.0-rc3](https://github.com/ledgerwatch/erigon/releases/tag/v3.0.0-rc3), [v2.61.3](https://github.com/erigontech/erigon/releases/tag/v2.61.3)
- Geth: [v1.15.5](https://github.com/ethereum/go-ethereum/releases/tag/v1.15.5)
- Nethermind: [v1.31.4](https://github.com/NethermindEth/nethermind/releases/tag/1.31.4)
- Reth: [v1.2.2](https://github.com/paradigmxyz/reth/releases/tag/v1.2.2)

## Root Cause Analysis

### Execution Layer Issue

The issue occurred in the execution layer because of the incompatibility between EIP-6110 implementation and Sepolia's custom deposit contract. Unlike mainnet or Holešky, Sepolia validation is permissioned which is achieved by using a token-gated deposit contract based on ERC-20 tokens instead of ETH.

When a deposit was sent to test the execution-triggered withdrawal functionality, execution clients encountered an error: "unable to parse deposit data: deposit wrong length: want 576, have 32". This is because the deposit contract emitted ERC-20 transfer events that are not part of a regular contract and were not expected by the EIP-6110 implementation logic. The failed events parsing invalidated blocks containing transactions to deposit, forcing validators to produce empty blocks.

An important obstacle of the fixing process was the ongoing attack triggering the issue. Because ERC-20 allows zero token transfers, which can be initiated by anyone, even without owning the token, the attacker could still send malicious transactions that emit incorrect events in the contract. 

### Root Cause Remediations

- Execution clients implemented a fix for parsing deposit contract logs but further discussion is needed to make it more robust, improve ABI decoding
- EIP-6110 is updated to add events filtering
- The testnet configuration needs to more closely mirror mainnet, reducing testnet specific edge cases
- Blockchain tests are updated to cover related scenarios

## More Resources:
- [Initial EF blog post](https://blog.ethereum.org/2025/03/05/sepolia-pectra-incident)
- [Analysis by Marius from Geth](https://mariusvanderwijden.github.io/blog/2025/03/08/Sepolia/)

## Timeline of Events

_Note: LLM was used to compile this based on the Discord chat transcript. I've sanity checked most of it, but there may be slight inaccuracies._

Because of mitigating an active attacker, some fixes were not discussed publicly and only happened in private chat between developers. 

### March 5, 2025: Sepolia Testnet Issue Timeline

Some developers and PandaOps had been meeting in person, identified the issue, shortly after the public chat starts:

### ~9:43 AM: Identifying the Issue
- 9:44: Tim Beiko reports: "There's an issue on Sepolia caused by some EL clients having issues processing transactions due to the deposit contract being different on Sepolia. PandaOps + Geth are IRL investigating."
- 9:51: Ahmad Bitar warns: "The fix for this might lead to a disagreement in consensus, so maybe, any fix to be deployed must be a scheduled fork."
- 10:01-10:02: Ahmad Bitar and lightclient urge: "please do not deploy this fix" / "yes please dont deploy any fixes right now" to prevent further chain split

### 10:07-10:29 AM: Emergency Coordination
- 10:07: Zoom meeting link shared, client teams are joining
- 10:21: fjl asks: "regarding fixes, are we in agreement about matching on the log topic?"
- 10:27: lightclient reports: "looks like geth, nethermind, and erigon are in agreement?"
- 10:28: parithosh confirms: "transactions are flowing again and we will discuss and co-ordinate proper fixes"
- 10:29: kamil_chodola notes: "Seems like erigon validators are still down"

### 10:45-11:37 AM: Fix Development & Testing
- 10:45: Mario Vega shares blockchain test for the issue
- 10:45: parithosh updates: "Clients agreed on a fix and can deploy them, ideally with some co-ordination just to be careful"
- 11:05: danceratopz shares hive command for testing incorrect behavior
- 11:10: fjl confirms: "fix is in Geth master branch now"
- 11:23-11:37: Discussion about deposit contract differences between Sepolia and other networks
- 11:37: M.Kalinin starts working on update to EIP-6110, update PR: "PTAL, https://github.com/ethereum/EIPs/pull/9453"
- 11:42: proto asks: "Will there be client releases for the L1 sepolia deposit-log selection fix?"
- 11:43: ralexstokes confirms: "yes, l1 client teams working on releases"
- 11:50: PSA shared: "Deposit log topic 0x649BBC62D0E31342AFEA4E5CD82D4049E7E1EE912FC0889AA790803BE39038C5"
- 11:57-12:08: Discussion about ABI decoding approach for the logs
- 1:17: Mario Vega shares updated test for ABI decoding
- 1:19-1:20: Som and danceratopz confirm the fix passes with Erigon's main and Nethermind

### 1:42-1:59 PM: Client Releases & Validation
- 1:42: spencer confirms: "Geth/Reth passes. Ethjs/Besu draft PRs also pass."
- 1:44: danceratopz lists versions tested
- 1:45: Nethermind 1.31.4 released
- 1:49: parithosh shares updated status and list of released clients
- 1:51: Reth v1.2.2 and Erigon-3 fix releases announced

### 2:00-3:25 PM: Coordinated Deployment 
- 2:12: Andrew Ashikhmin announces Erigon v2.61.3 release
- 2:27: spencer confirms: "All these releases pass on my end!"
- 2:52: ralexstokes shares Sepolia rollout call link
- 2:57: parithosh asks CL teams to confirm availability
- 3:01: parithosh instructs: "Please proceed with updating your nodes"
- 3:04: jakubgs reports: "done"
- 3:07: skylenet reports orphaned blocks and asks to verify node updates
- 3:08: jakubgs confirms all nodes are updated to Geth v1.15.5
- 3:12-3:18: Discussion identifies that Nimbus nodes are still missing blocks
- 3:21: jakubgs reports: "BN sync distance is growing" with screenshots showing sync issues
- 3:24-3:25: tersec investigates and notes Nimbus might be on a fork
- 3:25: Barnabas suggests: "might be a nimbus bug?"

### 3:25-4:09 PM: Nimbus Issues Investigation
- 3:26: Barnabas reports: "we also have our nimbus node on a diff fork" (with thread discussion)
- 4:09: parithosh posts update: "The update worked as expected. Network is finalizing with transactions being processed as expected. We tested a deposit and it works as expected now."

### 4:09-4:56 PM: Post-Incident Follow-up
- 4:09: parithosh announces EF blogpost at https://blog.ethereum.org/2025/03/05/sepolia-pectra-incident
- 4:09: parithosh outlines next steps: "Updates on tests, A detailed incident report over the next days, Deeper discussion on fix"
- 4:44: agnish reports Nimbus-Erigon issues on Pectra-devnet-7
- 4:48-4:56: Andrew Ashikhmin and Som investigate Erigon issues, noting "state root mismatch from a certain block"
- 4:53: Justin Florentine asks about L2s running on Sepolia

### 5:38-10:57 PM: Retrospective Discussion
- 5:38: Justin Florentine recalls suggesting shadowforking testnets before forking
- 9:35: Barnabas explains that shadowforking wouldn't have caught these bugs: "as generally we always re-deploy a mainnet like deposit contract"
- 10:44-10:57: Discussion about whether shadowforking could have caught the bug
- 10:57: parithosh provides detailed explanation: "Current process uses a mainnet deposit contract for shadowforks" and acknowledges "It's clear the diffs with mainnet on our testnets has become unwieldy and we will mod things to be as close to mainnet as possible in the future"