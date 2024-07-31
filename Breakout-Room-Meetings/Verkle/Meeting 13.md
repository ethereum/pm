# Verkle Meeting 13

## Meeting Info
Feb 26, 14:00 UTC

Recording: https://youtu.be/ekxELDRsv4Y

Original notes: https://x.com/rudolf6_/status/1763469139778167244

## Agenda:
1. Client team updates
2. Verkle shadowfork
3. Testnet updates
4. Code packaging in Verkle
5. EIP-2935: stateless BLOCKHASH


# 1. Client team updates

@gballet
 and 
@ignaciohagopian
 for 
@go_ethereum
:
Guillaume: shadowfork completed. Required some reworking of Kurtosis tooling. More details in separate agenda item on this call. Continuing to work with 
@elbuenmayini
 and the testing team on tooling and making good progress! Soon will need to complete the rebase of Verkle on top of Cancun.

Ignacio: apart from fixes for Kaustinen, working on the replay tool. Also making some progress on exploring whether there is a potential DoS vector with Verkle, if we have a branch that is deeper than expected. Motivated in part by the discussion on ring buffers + blockhash. Trying to gain more confidence on whether the potential DOS vector is actually a concern. (See https://hackmd.io/@jsign/vkt-tree-branch-attack for full writeup). Idea is to do a semi-naive attack to explore the potential DoS vector, identify the worst case depth that an attacker can realistically achieve, and then understand the performance implications on the EL side.

Daniel for 
@ethnimbus
: the Constantine library is complete and mostly on par with Geth implementation.. Now starting integration into the Nimbus client.

@kevaundray
: quick reminder that the serialized commitment method we are using in Pedersen hash is being changed, and it is a breaking change for some clients.

@gajpower
 and 
@GabRocheleau
 for 
@EFJavaScript
 and 
@lodestar_eth
: for Lodestar, planning on a rebase of Cancun alongside Guillaume. Separately, developing a preimage manager designed to handle saving of preimages on the EthJS client, which is necessary for the transition. Initially had PoC, and found issues that were fixed. Will be merged into the production EthJS client.


# 2. Verkle Shadowfork

There was a successful shadowfork of Holesky. Not running any transactions, just testing that we could perform the Merkle to Verkle transition with correct real-life data. It helped to reveal a lot of issues which is great. More testing and refining still to do. There will be more updates to the branch as we keep testing additional shadowforks!


# 3. Testnet Update (Kaustinen)

Thanks to all the teams and clients joining the testnet we've been able to uncover a good number of bugs. Can find the current specs and status of the testnet at https://notes.ethereum.org/@ethpandaops/verkle-gen-devnet-4. Going to keep this testnet up for a little while longer so teams can continue to sync and uncover more bugs. Guillaume spent a few minutes to walk through two recent bugs that were found in more detail. Also 
@Amxx
 from 
@OpenZeppelin
 has kindly deployed a bunch of test contracts around block 70,000, which will be a big help on further testing 🙏


# 4. Code packaging in Verkle

@chfast
 joined the call to walk us through an interesting design simplification he has been working on with 
@gballet
 and others for storing code in Verkle. See https://github.com/ipsilon/eof/pull/58.

This design exploration originated from thinking about what are the alternatives to the current code layout in Verkle, which is executing 31-byte code chunks (accompanied by 1 byte of metadata). And to be able to have localized jumpdest analysis. The alternative design presented by Paweł involves splitting this metadata and the code into separate sections.

Two main benefits to doing all of this: (1) the execution is more similar to what we have today, and maybe simplifies the implementation on the execution side; and (2) the metadata is only needed when you have a jump instruction. In the current Verkle design, you kind of waste this one byte of metadata if you fall through from one chunk to the next and you don’t perform any jumps. So this might allow us to charge less gas (tbd). More analysis needed to confirm exact impact on gas, using Ignacio’s handy replay tool.

@chfast
 walked through the whole proposal in detail on the call. Recommend checking out the recording for those who want a deeper dive.


# 5. EIP-2935: stateless BLOCKHASH

Last up: Gajinder shared an overview and updates on a potential Verkle implementation of EIP-2935. In short, this involves finding a solution for the blockhash opcode to play nice with Verkle and stateless clients. See https://notes.ethereum.org/@2tWvTzJhTI6SxlCGZY-dyw/HylnJWFnT#/

For context, the blockhash opcode allows for querying the hash of the past 256 blocks. But this would not be possible today with a stateless client without a new solution here, since stateless clients would not have any way to grab the most recent 256 blocks.

The current proposal is to store the previous 256 block hashes as storage slots of a system contract to allow for stateless execution (i.e. perpetual history).. See https://github.com/ethereum/EIPs/pull/8166. This is based in part on EIP-210: https://eips.ethereum.org/EIPS/eip-210.

The first part of the discussion was around whether this type of perpetual history is the right approach, or if it is better to use a ring buffer approach (see EIP-4788). Decision: folks on the call favored the ring buffer approach (size 256, to keep the behavior of blockhash). cc 
@ralexstokes


The next part of the discussion was around the implementation method, and whether it should be a "client native" approach, or a system contract. The benefits of the "client native" approach are that its possibly a simpler implementation, and a backward compatible gas schedule. The benefits of the system contract approach is less client code, but might require clients to introduce "system" contract execution capabilities. Decision: folks on the call favored the “client native” approach. Check out the recording for the full conversation.