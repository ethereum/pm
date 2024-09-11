# Verkle Meeting 18

## Meeting Info
June 3, 14:00 UTC

Duration: 60 minutes

Meet link: shared in #verkle-trie-migration Eth R&D Discord right before the call

Recording: https://youtu.be/dCMbA90jh0M

Original notes, copied from here: https://x.com/rudolf6_/status/1798557660905902393

## Agenda

1. Client team updates
2. Testing updates
3. State root of parent block in the proof (PR here)
4. EIP-158 removal (due to EIP-7702)
5. Discuss whether system contracts should be warm
6. EIP-2935 updates post-Verkle
7. Gas cost spec (EIP-4762) PR open questions

# 1. Client team updates

@gballet
 for 
@go_ethereum
: worked on finalizing the updated gas schedule, the revamp of EIP-2935, test framework for the conversion, and a spec update to add the state root of the parent block to the Verkle proof. Also quick highlights on the most recent conversion test (converting all Merkle state over to Verkle): took about 16 days of blocks for it to complete (transferring 10k leaves per block). 
@ignaciohagopian
: in addition to the test vectors, also did a Go implementation of the Ipsilon proposal for code chunking.

@kt2am1990
 for 
@HyperledgerBesu
: completed some optimizations during interop, so can import blocks much faster now. Also implemented proof verification using rust-verkle. Continuing work on the migration/conversion, and also on the snap sync implementation for Verkle.

@jasoriatanishq
 for 
@nethermindeth
: now able to sync Kaustinen testnet using Verkle sync. Have improved how healing works in Nethermind, so its much faster now, but still need to test on latest testnet. Also implemented the most recent gas cost changes. And started working on moving over to rust-verkle for some operations, so now proof verification is much faster than before.

@GabRocheleau
 for 
@EFJavaScript
: have also made all the gas changes from latest EIP-4762. And have started a verkle trie implementation for EthJS.

Somnath for 
@ErigonEth
: was able to regenerate the preimage files using a slightly different approach, and the total size is now much smaller: 28gb instead of 40. Can see more info here: https://hackmd.io/@somnergy/rkeJgDO7A  (note: one of the big open questions with the conversion from Merkle to Verkle is where and how to get preimages for all the clients that don’t store them by default).


# 2. Testing updates

@elbuenmayini
 for the testing team: over past few weeks, a bunch of things have been fixed between the transition tool and the testing filling process, which is now fully working for Verkle. Also the hive instance for Verkle is now working. Another small update: we are preparing pre-releases on the execution spec tests repository. So now can tag releases with only Verkle changes. And all client teams working on a branch can go into the releases page and easily get the last Verkle release from the repo.

@gballet
 added: fixed a bug that caused issues with tests which was due to an old PR related to the conversion. Still a few tests that aren’t passing, and debugging is ongoing.

Lastly, can find latest work on test vectors from 
@ignaciohagopian
 here: https://github.com/spencer-tb/execution-spec-tests/pull/41

# 3. State root of parent block in the proof

Quick tldr on this: making a small change to help with EthJS stateless implementation: basically we need the state root of the parent block inside the proof, otherwise stateless clients would also need to get the previous block. Updating the consensus spec repository to add this field to the execution witness. Should be included in the relaunch of testnet 7.

# 4. EIP-158 interaction with EIP-7702

Next up, discussion of a potential issue caused by interaction of EIP-158 (removal of empty accounts from state) and EIP-7702. With 7702, an eoa could be empty (zero nonce/balance), but still have some storage. Pre-verkle, that can be destructed, but post-verkle it cannot.

question is: how do you delete a verkle contract? see reason why we deactivated selfdestruct.. deleting an account with storage in Verkle context is impossible. Now with 7702 there is a new corner case in which an account could be marked for deletion bc of 158, but can’t be entirely deleted if it has storage bc we don’t know where that storage is.

Two potential solutions: Either completely disable storage in 7702, or possibly just get rid of EIP-158. Or make behavior of 158 more like the new behavior of selfdestruct (EIP-6780). I.e. if an account gets created during tx and becomes empty in same tx, then rules of 158 should still apply.

@gajpower
 and 
@jasoriatanishq
 brought up a previous discussion where we decided if we set a storage value to 0, and someone is paying the trunk fill cost, then just add it to state rather than deleting it. Even if its zero at the end of the transaction.

@shemnon
 mentioned that not charging in this context is reminiscent of the Shanghai attacks, and creates a potential attack vector.. perhaps it's not a bad thing to charge for the account creation even if the account never gets persisted because they clear it out. Better than encouraging transient account uses.

Decided to continue the conversation separately and will come back to this in the near future.

# 5. Whether to warm system contracts

Recommend watching the recording to get the full discussion here, but the short version is that Guillaume brought up how it would potentially be much simpler from implementation side to not warm anything.

@shemnon
 proposed to potentially only pre-warm the initial precompiled contracts, which already have logic in and are special-cased bc never accessing the account state to run those. The contracts that are not in that reserved space (like blockhash) would be subject to the existing warming rules. (i.e. pay the cold cost and then they are considered warm).

Agreed to take some more time to think on this topic a bit, and will revisit in next 2 weeks.


6. Gas cost updates to EIP-4762

During the recent client team interop, we spent some time going over the gas cost changes and making final updates to the spec. But there are a few leftover questions remaining from that discussion. Since we were running short on time on this call, we decided to schedule a separate call to go over these questions in a bit more detail and try to fully finalize it all so we can get Guillaume’s PR merged and update EIP-4762.

We ended the call with a quick reminder on 
@GabRocheleau
’s proposal for preimage distribution using the execution witness. Decided to come back to this topic asap. See this doc for a short summary: https://notes.ethereum.org/@rudolf/r1C62ySQ0
