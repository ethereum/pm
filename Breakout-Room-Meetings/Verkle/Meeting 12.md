# Verkle Meeting 12

## Meeting Info
Feb 12, 14:00 UTC

Recording: https://youtu.be/rwpNQ8VBDwg

Original Notes : https://twitter.com/rudolf6_/status/1757355851982241895

## Agenda

1. Client team updates
2. Testnet updates
3. EIP-2935: BLOCKHASH
4. EIP-7612: State Transition Method
5. Testing team updates
6. Deprecating Serialize Commitment


# 1. Client Team Updates

@jasoriatanishq
 for 
@nethermindeth
: joined the testnet, hit a few issues, and now working on bringing in the latest changes from Dencun.

@gajpower
 for 
@EFJavaScript
: synced with the testnet up to block 478. Currently waiting for testnet relaunch to resume stateless execution, since witnesses are missing in the current testnet. Completed blockhash implementation (EIP-2935).

@0xagnish
 for 
@ethnimbus
: optimizing the deserialization function for Banderwagon. Now the Nimbus cryptography library in Constantine is a bit faster than the Go library. Almost done with stateless primitive testing. Next up will be integrating into testnet via the Nimbus execution client.

@gagadrupal
 for 
@HyperledgerBesu
: made necessary changes to sync w/ the testnet. Found a bug in NextForkBlock in Geth. EIP-2935 has been implemented (allowing the storage of blockhash history in the state). Gas cost modifications still WIP, but managed to import more blocks with contract creations/transfers.

@gballet
 and 
@ignaciohagopian
 for 
@go_ethereum
: did a lot of spec’ing and updates for EIP-4762 and EIP-2935. Also worked on testing tooling. 
@ignaciohagopian
 has been working on reactivating the replay functionality, so that we can produce data from most recent blocks. (now able to replay 5M blocks). This will also enable more critical testing and data gathering, checking the size of proofs, etc.


# 2. Testnet Updates

@gballet
 spent a few mins to walk through the latest testnet (devnet-4), and share a spec sheet that Barnabas from DevOps has now kindly produced for the testnets. See: https://notes.ethereum.org/@ethpandaops/verkle-gen-devnet-4 for a list of all known testnet bugs, and the latest status of what has been deployed to testnet.

Barnabas added that Kurtosis is now capable of doing shadowforks out of the box. So for example you can easily test your EL/CL implementation using a state that was taken before Dencun. Encourage client teams to start using this and testing it!

For more on how to perform local shadowforks: https://x.com/parithosh_j/status/1757099658143318322


# 3. EIP-2935: BLOCKHASH

@gajpower
 shared updates to the new implementation of EIP-2935: the simplified strategy is
is that in the first block of any fork, we are persisting whatever history is needed for that block to execute. At the start of the block, you insert the parent hash into the slot. And if this is the *first* block of the fork, then you would also insert the additional 255 ancestors.

Check out the update to the EIP here for more info: https://github.com/ethereum/EIPs/pull/8166


# 4. EIP-7612: State Transition Method

@gballet
 created a new EIP for the “base” state transition method. This EIP describes the minimum set of features necessary to make the switch over and start writing all state to the new Verkle tree. Note that this EIP does *not* describe a strategy for converting *historical* state from the Merkle Patricia Tree over to Verkle. This will come in a future EIP.

Read more here: https://github.com/ethereum/EIPs/pull/8162

# 5. Testing Team Update

@elbuenmayini
 Mario from the testing team joined the call to provide the latest news on Verkle testing and walk us through the execution spec tests. First, there have been some recent updates to the execution spec test repo to better support Verkle. Starting off with the basics, which is the transition tool changes. (This is the tool that is used to fill all of the tests). Still a WIP, not yet able to generate any tests for Verkle. But getting closer. Mario also shared some interesting ideas on how we can potentially better test the actual transition from Merkle to Verkle.

To learn more: https://github.com/ethereum/execution-spec-tests/tree/main/docs/consuming_tests

# 6. Deprecating Serialize Commitment

Last up, 
@kevaundray
 gave a quick walkthrough of some changes to the WASM/typescript Verkle crypto library (related to tree key hashing and deprecating the use of .Serialize to keep things more consistent). See: https://github.com/ethereumjs/verkle-cryptography-wasm
