
# Stateless Implementers Call #28
## Info
Note: This file was copied from here: https://notes.ethereum.org/@rudolf/sic-notes#Call-28-December-2-2024

Date: December 2, 2024

Recording: https://www.youtube.com/watch?v=5bxvSLvc9LA

Agenda: https://github.com/ethereum/pm/issues/1203

## Notes

## 1. Team updates

@ignaciohagopian and @gballet for @go_ethereum: started working on EIP draft for binary tries. Also working on new execution spec tests from bugs that were found in latest devnet.

@g11tech for @EFJavaScript: been playing with devnet-7, and resolving some recently found issues.

@kt2am1990 for @HyperledgerBesu: Working on implementing the blockhash gas cost modification. Also implementing the proof verification. This will unblock some other stuff like Verkle sync (snap sync equivalent), and validating proof coming from the other client. Also working on optimizing stem generation by modifying how we call the Rust Verkle library.

## 2. Execution spec tests

Update from Ignacio, sharing v0.0.8.

After we previously launched devnet-7, we found a consensus bug with Nethermind. Debugged with Tanishq and found an edge case. Created a new test case to cover this. Idea going forward is that every bug we find in any devnet should result in a new execution spec test to cover it. Any new client that joins the next devnet will also be covered by these cases.

## 3. Preimage distribution and Portal Network

Piper from Portal Network joined to share some thoughts on preimage distribution with Portal.

Regarding preimage distribution for the Verkle migration: Piper mentioned that Portal can solve this, but probably isn’t the best solution. Portal is best for clients who want to grab a subset of the data on demand. With the preimage problem for Verkle, all of the clients would need to grab the full set of preimages. But there could be a “file-based approach” that could make sense in this case.

The file-based approach: S3 buckets being able to generate the file, and potentially having pre coded S3 buckets in clients that are already distributed. Has a predistributed trust model. Distributing big files like this from S3 buckets is a pretty straightforward approach. Alternative to S3 buckets, could use torrents.

Guillaume mentioned that Lukasz from Nethermind had previously indicated a preference for using an in-protocol p2p approach. But added that it seems clear that the CDN approach is the simplest and should probably go with that.

Next steps: make a spec on a potential format for the file.

## 4. State expiry

Hadrien from OpenZeppelin joined to share some thoughts on state expiry.

One related question that was discussed in Devcon: do we want to resurrect based on reads or based on writes?

Hadrien: most of the storage accesses are as you expect related to reading and writing. And so one question is whether a read would extend the lifetime of an extension or not. There are a few slots that are being read, but never written to. For example in the case of ERC-721, when tokens are transferred the slot will often contain a zero because nobody is allowed to take the token. And anytime there is a transfer of that token, in the current implementation it will write another zero to reset, even if old value is a zero, because its cheaper than trying to read. Depending on how state expiry works, there may be different cost model depending on whether there is a zero because it was never written to the state, compared to if a zero gets explicitly written.

This is where the approach of state expiry shown in EIP-7736 comes in. Han joined to share some updates on this front.

Han is currently working on implementing 7736, and the changes needed on the Verkle part are done. Still working on the geth part. Once we get all the components complete and integrated can hopefully have a devnet to start testing out the various scenarios.

## 5. Stateless Transactions EIP

Gajinder shared some of the latest thinking around changes needed to best support stateless clients.

One of the challenges is that stateless clients which don’t maintain any execution state would not be able to do any kind of local block building. This proposal is a partial remedy to this problem.

The basic idea is that with every transaction the transaction submitter will also have to submit an execution witness, and that execution witness will have a state diff + proof of the state diff. The execution witness would also bundle the parent state root, which is what a builder would look at to see whether it can include this tx in the particular block that it’s building.

Gajinder is currently drafting the EIP. Will have something to share soon.