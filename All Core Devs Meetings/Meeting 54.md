# Ethereum Core Devs Meeting 54 Notes
### Meeting Date/Time: Fri, February 1, 2019 14:00 UTC
### Meeting Duration: 1.5 hours
### [GitHub Agenda Page](https://github.com/ethereum/pm/issues/73)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=qBpImOhpWFg)

# Agenda
1. Roadmap
    1. Constantinople - Ropsten fork
    1. Istanbul Hardfork Roadmap
    1. Outlook: PoS finality gadget on PoW chain (Serenity)
    1. ProgPoW audit?
1. Working Group Updates
    1. Ethereum 1.x Stanford Meetings Overview
    1. State Rent
    1. EWasm
    1. Pruning/Sync
    1. Simulation
1. Testing Updates 
1. Client Updates 
    1. Geth
    1. Parity Ethereum
    1. Aleth/eth
    1. Trinity/PyEVM
    1. EthereumJS
    1. EthereumJ/Harmony
    1. Pantheon
    1. Turbo Geth
    1. Nimbus
    1. Mana/Exthereum
1. Research Updates 

# 1. Roadmap
## 1.1 Constantinople
### 1.1.1 Testnet forks
- Martin: Ropsten is 3000 Blocks away (11 hours away)

### 1.1.2 Clients
- Afri: Parity release 2.2.8/2.3.1
- Geth: Geth release 1.8.22 

ACTION 1: Hudson to send tweet from Ethereum Twitter regarding upgrading nodes for Ropsten.
    
## 1.2 Istanbul Hardfork Roadmap
- Afri: No update.
    
## 1.3 Outlook: PoS finality gadget on PoW chain (Serenity)
- Hudson: Best people to speak on this are Vitalik or Danny. As they are not online we will leave that for next time.
    
## 1.4 ProgPoW audit?
- Hudson: Audit is to check the viability of claims from ProgPoW. This is to be completed before all EIPS are submitted for Instanbul. Also looking for funding to do this audit.
- Martin: Will the auditors be hardware experts?
    - Hudson: Yes they will.
- Danno Ferrin: Any update on Specification? Would prefer Generic Specification. 
    - Hudson: Not sure. 

ACTION 2: Hudson will get them to clarify in the Gitter Chat.

- Hudson: What group should decide to implement this?
    - Martin: Just implement it and let the clients decide. Drawback - less hashes/sec with ProgPoW. Difficulty is also expected to go down. Only if ProgPoW is double the hashrate will difficulty match.
    
ACTION 3: Danno suggested we get Ethereum Cat Herders to look into this.

- Martin/Greg/Lane/Piper: Still concern around who should make the decision if ProgPoW should be implemented. Core Developers don't feel qualified about making the decision.
    - Lane: Suggest we make a decision prior to audit and then audit makes decision on go or no go.
    - Hudson: Is it possible to make a ProgPoW fork before Instanbul?
        - Martin/Lane: Yes it can
    - Hudson: Feel we need to get more community feedback before making a decision.
    - Hudson: There are still issues with ProgPoW. Not sure we can implement this quickly.
        - Danno: Agreed.
    - Lane: What is in the audit?
        - Hudson: Put the questions in the Zoom Chat.
    - Hudson: Miner signalling would favour ProgPoW.
    - Martin: An Audit will not resolve anything. It will remain controversial. But let's get it done quickly.
 
ACTION 4: Lane suggested to get the Cat Herders to facilitate the ProgPoW audit.

- Hudson: Note Audit can take months is there any concern around this. It is agreed that the implementation can still progress in the mean time. Everyone agrees that the audit is a good course of action.
    - Martin: Should we ask for Miner Signalling?
    - All: Yes, get a signal from the miners.

ACTION 5: Get signalling from Miners.

- Hudson: No Support vs Support signalling to be decided in All Core Dev Gitter Channel.
    - Lane: This does not require a Hard fork or client update?
        - Martin: No
    - Hudson: A date has not yet been decided for the Audit yet. April/May is probably about when it should be completed.
    
# 2. Working Group Updates
## 2.1 Ethereum 1.x Stanford Meetings Overview
- Hudson: 30 people attended. Not All Ethereum Core Developers.
    - Objectives:  Ensure Longevity of Ethereum 1.x network.
    - Clarify and then explain the core functions of each Working Group and their relevance to each other.
    - Establish (via presentation, discussion, and corrections) framework for designing, evaluating, and comparing the change plans. I started drafting the framework here.
    - Define initial set of changes to the Ethereum protocol that are likely to be specified by May 2019 deadline, to be implemented in Oct 2019.
    - Propose a social contract to not add any specific features into the protocol, but instead focus on the longevity of the network (essentially monopoly of Ethereum 1x over the Ethereum 1.0 roadmap).
    - Identify ways to champion Ethereum 1x project and engage the community on deliverables.

All videos for the Ethereum Stanford presentations can be found online: 
- [Ethereum 1.x Morning Day 1](https://www.youtube.com/watch?v=BpLyO8Q4ZZo)
- [Ethereum 1.x Afternoon Day 1](https://www.youtube.com/watch?v=Nky1BPwap2M)
- [Ethereum 1.x Morning Day 2](https://www.youtube.com/watch?v=P2S7OW2E1vk)
- [Ethereum 1.x Afternoon Day 2](https://www.youtube.com/watch?v=dHZiWFWCGNM)
- [Ethereum 1.x Morning Day 3](https://www.youtube.com/watch?v=CnOyVZ3HvK4)
- [Ethereum 1.x Afternoon Day 3](https://www.youtube.com/watch?v=HAK3ijgLRoM)
   
## 2.2 State Fees
- Alexy was hot available to provide update.
    
## 2.3 EWasm
- Guillaume: Ewasm is independent of the rest of the Ethereum 1.x
    - Will keep Precompiles in Geth and Parity as they are.
    - Will not lift every precompile into Ewasm.

## 2.4 Pruning/Sync
- No one was available to provide update.
    
## 2.5 Simulation
- Zak (Whiteblock): Vanessa presented on simulations on uncle rates using agredated data from the mainnet.
    - We are working on a test plan on validating the hypothesis on sync failure and increasing state size. Working on generating 240 millions users. Generate this state probably by Wednesday. Save it and use it to run multiple tests using this state. Been documenting the process and will share it in due course. Working with Alexy and Andre. Suggest it is not just bandwidth.  
    - Martin: Keen to find out how the state was generated.
        - Zak: Shared how it was being done. And provided a twitter link: https://twitter.com/0xzak/status/1091019925970251778?s=20


# 3. Testing Updates
- Martin: Dimitry generated the tests pretty quickly. Parity and Geth passed all the tests. All looks good. We are unable to do Fuzzing as Parity has a feature missing.

- Brooklyn: Nothing specific to share.
- Antoine:  Nothing specific to share.

# 4. Client Updates
## 4.1 Geth
-Martin: Patch Release 1.8.22 for the Constantinople fix and also contains some security fixes in the peer to peer protocol stack. Continuing to merge changes into the master branch stack which will eventually make it into the 1.9 release which will be potentially breaking changes but that is not yet for a while.
    
## 4.2 Parity Ethereum
- Afri: Released St Peters Fork yesterday with 2.2.8 stable and 2.3.1 beta. Everyone should update their node.
    
## 4.3 Aleth/eth
- Pawel: Merged the Constantinople changes.
    
## 4.4 Trinity/PyEVM
- Piper: Work in progress for the St Petersburg fix. Hoping to get release out by next week Tuesday.
    
## 4.5 EthereumJS
- Not here.
    
## 4.6 EthereumJ/Harmony
- Mikhail: Constantinople fix released.
    -
## 4.7 Pantheon
- Danno: Released Constantinople fix for Ropsten and Mainnet and added support for new Goerli testnet. Started working on Fast sync. 
It is the old standard but the new Ethereum 1.x is not yet ready.
    
## 4.8 Turbo Geth
-Alexy not available to provide update.
    
## 4.9 Nimbus
-No one available to provide update.
    
## 4.10 Mana/Exthereum
-No one available to provide update.

ACTION 6: Hudson will invite IOHK Ethereum Client Mantis written in Haskel to the Ethereum Core Dev Calls as they can sync to mainnet.

# 5. Research Updates
- Vitalik or Danny was not available to provide update.

# 6. Anything Else 
- Hudson: Congrats Afri on Goerlicon. 
    - Afri/Lane: It was awesome.
    
- Zak Cole: Will be opensourcing Whiteblock. Get in touch with if you want to get involved or collaborate. 

- Truffle/Ganache: ethereumjs petersburg release is a WIP. Ganache-cli/core has an experimental petersburg release published to npm.
    - David: Had a fork of EthereumJS VM.

- Lane: Ewasm update, focused on Ethereum 1.x. Looking at bench marking specifically a product called Life which is an ahead of time compiler written in Go.

- Martin: A person has been engaged via a Github grant to work on the more advanced lib fuzzer based fuzzer. Github handle cryptomental.
 There is also another person working on the fuzz testing of Solidity. It is now on the Google Opensource Plus testing framework.

- Guillaume: Will there be any notes or meeting from W3M? Please share. 
     - Afri: Not sure will check when he gets back in the office.

# Date for next meeting
- 15 February 2019.

# Attendees
- Hudson Jameson
- Brett Robertson
- Tim Beiko
- Ben Burns
- Antoine Toulme 
- Brooklyn Zelenka
- Martin Holst Swende
- Danno Ferrin
- Daniel Ellison
- Zak Cole 
- Mikhail Kalinin
- Greg Colvin
- Pawel Bylica
- Greg Colvin
- Johannes Zweng
- Afri Schoedon
- Piper Merriam 
- Meredith Baxter
- Anton Nashatyrev
- Lane Rettig
- David Murdoch
- Alex Beregszaszi
- Guillaume 
