# Consensus Layer Call #79 Notes
### Meeting Date/Time: Thursday 2022/01/13 at 14:00 UTC
### Meeting Duration: 1 hour
### [Agenda](https://github.com/ethereum/pm/issues/443)
### [Recording](https://www.youtube.com/watch?v=izyYW9-HbNk)
### Moderator: danny
### Notes: Stefan Wüst

***Summaries and highlights were curated and slightly modified from [Quick Notes](https://hackmd.io/@benjaminion/ryBR2ip3Y) by Ben Edington and some inspiration on how to write these notes was taken from the [Consensus Layer Call #77 Notes](https://github.com/ethereum/pm/blob/master/Consensus-Layer-Meetings/call_077.md) by George Hervey. Kudos to both of them!***

## Intro

danny:
OK. The stream should be transferred over. Here is the agenda. If you are in Youtube chat and you can hear me, let me know. People might still be trickling in.
So, first half we will discuss anything related to Kintsugi and the merge. Then we'll go into any other client update happening. Then some general discussion time about spec and other things beyond the merge.
THank you Alex and Tim for handling a couple of calls in my absence. I was off a lot of last month and in fact I'm still wating through everything and catching up.
Let us begin.

## Kintsugi office hours

### Kintsugi finalizing

danny:
We can start with general Kintsugi Updates. Is Pari here or Raphael? Hey Pari. People are trickling in.
The first thing on the agenda is just general Kintsugi testnet update. I see that we're finalizing. Do you want to give us a quick on that?

Pari:
Quite a few bugs this week. The chain wasn't finalising from last friday morning until about yesterday evening. Have now pruned a couple of forks. There was one mayor fork and we have I think almost every client combination working. I think that was Nethermind Nimbus and Nethermind? that Marek said he would look into. Otherwise we seem to be good to go.
And as a sidenote: I have a bunch of databases from the non finalising period. I will upload them and just share a drive link. There's also a dump of the array, a couple of log files and quite a lot of debugging information in case some people want to dig in the stuff.

danny:
Great. And I know, I'm always beating this drum. I know we captured some test cases from this. I think some more should be captured and make their way into Hive or some sort of environment that actually uses the engine API. Are we cataloging these anywhere?

Pari:
Not yet but I'll start a document to do that. I also work on a proper indcident report. This is a nice candidate for that

Marius:
Marius is already adding them to his PR for Hive.

Mikhail:
I d' like to add that the blockhash issue occurred due to some unclarity in the spec that the blockhash must be verified against the block constructed from received payload. Pending an update to address this.

danny:
Any time there is an inserted execution payload there should be a “well-formedness check” before proceeding any further.

Mikhail:
Any block header verification including this blockhash verification should be performed if possible.

Marius:
Should we already have to check finality? Or should we have this somewhere else?

danny:
Consensus layer client shouln't revert finality but if it were on a branch that you decided it should never execute, it seems prudent to say "I'm not going to do that" in some way.

Some discussion around how to handle blocks older than the execution layer’s finality checkpoint. This could happen if the consensus layer were to resync from genesis, say. Seems to be straightforward to handle. Also can probably ignore forkChoiceUpdated() calls that go backwards.

danny:
TL/DR here is that this is not the case for all execution clients (aragon handles things a bit differently). The default is that the execution client executes a branch in proof of work once the fork choice has signaled this is canonical so only when the difficulty of a branch overtakes the canonical branch would it actually execute such a branch and whereas the semantics of execute payload and fork choice updated applying a bit differently to the execution layer. they're pretty much saying "I'm giving you a payload. It might be from any branch, it might not even end up being the fork choice or canonical but you should execute it".

### Update on testing
Peter s:
Do we have any environment for testing these scenarios - e.g. spin up a non-finalising chain?

danny:
Hive is approaching being able to handle this kind of scenario, and partitions. Let Lightclient know if you have any specific configurations that would be useful.

There is also some third-party simulation work going on.

### EL/engine-api handling of branching tips/reorgs
Further topic. This may not be true for all execution clients, but default is for client to only execute a branch once its PoW difficulty is greater than the previous head. There is a mismatch in this expectation with the way that the consensus layer drives the execution client, which led to high load on the very forked testnet. [Peter S] In PoW mode, when a block does not build on our current chain, if we have the state for the parent we execute it, if not we store the block for later. [Danny] We may need to modify the semantics of the engine API calls to allow for this kind of behaviour: allow for mandatory or optional execution in forkChoiceUpdated() and executePayload()respectively (maybe?). Geth stores 128 past states which makes the change in the semantics much more of an edge case. Erigon does not store multiple states, and big reorgs are relatively heavy - it uses reverse state diffs. Note that Geth is moving in the same direction (with reverse diffs), though it will still maintain 128 past states. Action: document any required changes to the engine API and get review. Could be useful to add VALID and INVALID returns for forkChoiceUpdated().

### Other topics
Peter S:
There are some ordering dependencies of calls in the Engine API. What is the desired behaviour in the case of protocol violation that breaks this ordering?

Mikhail:
forkChoiceUpdate() will just return SYNCING if it’s called out of order. The current API should handle all edge cases gracefully. Need to double check that all cases are covered in practice.

Lightclient:
Which consensus clients support starting from a Merge (pre transition) checkpoint?

danny:
It is specified that it should be possible for all clients now (not sure about amphora)

### Planning

danny:
Spec updates coming, main thing being the call semantics. Other minor things (PR on ELCO, communication, authentification). Until then, keep Kintsugi will remain up. Probably one more testnet like Kintsugi, then Merge-fork public testnets.

Aim to freeze spec/near frozen state asap.

Pari:
Do all clients support the Bellatric naming? (See chat)

danny:
Ready in my opinion. To be coordinated outside of this call.

Saulius:
What changes needed to be made to clients as a result of testnet incidents? Would be good to have a list. Also, should we think about making the fork choice more like PoW since fork handling in PoW has proven very robust? On PoS forking is cheap, not so under PoW.

Marius:
There was some discussion in Greece about whether proposing bad blocks would be penalised, things that would be difficult for the execution layer to handle, such as not building on the current head.

danny:
Likely this is possible since we have a block roots accumulator. Haven’t thought deeply about it. Action: Saulius invites further discussion

## Other client updates

Lodestar
Introducing a new team member. New release v0.33.0

Grandine
Finally joined Kintsugi (just before the crash). Back today with 1000 validators, performing well. Currently testing only with Geth. Looks good right now.

Prysm
We've been working on optimistic sync. Fork choice proposer boost and new spec tests to be done by end of Jan. Switching beacon state to native Go structures to save memory. Implementing Web3Signer API, by end of Jan. Work on Key Managwement API.

Nimbus
Preparing new release today or tomorrow. Mostly performance, but also ships key manager API. Optimised used of Nim garbage collector, we were able to significantly reduce our network usage by ~1GB on mainnet.

Want to work on light client. Have a server compatible with Lodestar, and will put a light client mode into Nimbus. Have plans to contribute to the spec.

REST API cache now speeds up calls significantly.

Teku
v22.1.0 release has network config --kintsugi. Also a bunch of Optimisations. Lots of work on optimistic sync. Starting to find lots of great corner cases in optimistic sync. More confident that it will work out well now.

Working on key manager API - can be enabled in the release build. You can enable it in the release build and play with it. Just need to add authentication and SSL. Should be fully supported in next release.

Lighthouse
Release candidate in next day, release next week. Big update! Performance work, moving slasher DB to new platform. Optimistic sync close to mergeable. Flashbots PoC. Client diversity analysis. Proposer boost and Bellatrix rename ready to go.

Marius:
LH database grew 7GB a day during non-finalisation, but were not pruned when finalisation occurred - is this expected? [Paul H] This ought to work; will look into it. [Adrian S] Teku’s default for finalised states is tree-mode which deduplicates automatically.

Jacek:
Nimbus does deduplication for validator states as well.

(Discussion of Teku’s state tree storage mode ensues…

Jacek:
Nimbus has been playing with daily “era files”, which are effectively complete checkpoints.)


## Research, spec, etc

Dankrad:
I published a draft for simplified sharding that should greatly simplify the design. Please take a look at the draft PR. It would be interesting to get feedback. Should be much faster to implement.

danny:
If you want to do some R&D work on DHTs, get in touch with us!

Also George posted pretty comprehensive new Single Secret Leader Election post on Ethresear.ch today.

If there's nothing else we close.
Thank you!

## Chat highlights
- **From pari to Everyone 02:40 PM:**
Does everyone support the bellatrix config renaming?
- **From Adrian Sutton to Everyone 02:41 PM:**
Teku has a PR ready to merge with the bellatrix renaming - just waiting on the Kintsugi spec rename happening.
- **From terence(prysmaticlabs) to Everyone 02:42 PM:**
Prysm is ready
- **From Marius to Everyone 02:44 PM:**
Agree, there should be penalties for proposing a bad block
- **From stokes to Everyone 02:44 PM:**
define “bad”
- **From Adrian Sutton to Everyone 02:44 PM:**
It would wind up being a penalty for missing your block proposal essentially.
- **From danny to Everyone 02:44 PM:**
define bad though?
right
- **From Marius to Everyone 02:45 PM:**
Not following the consensus rules (bad blockhash, etc)
I remember I backed off from this discussion after some good arguments last time (but I don’t remember them anymore)
- **From Adrian Sutton to Everyone 02:48 PM:**
You do wind up missing out on block rewards and any tx fees and MEV. So missing your block proposal is pretty costly even without penalties just in terms of the opportunity cost. You have a strong incentive to get it right.
- **From danny to Everyone 02:50 PM:**
but once you are at a depth of multiple epochs, proposers no longer map to the head’s shuffling so there is not an opportunity cost
- **From Marius to Everyone 02:54 PM:**
Reposting this from discord here: My lighthouse node is 26GB right now (due to the time of non-finalization).
It grew roughly with 7GB per day in the time of non-finalization.
If we aim for 2 weeks of non-finalization max, that would be 98GB of additional space needed.
I suspected the node to prune these states once we reached finalization.
Is that something that clients do?
Otherwise two or three periods of non-finalization would blow up most nodes
- **From terence(prysmaticlabs) to Everyone 02:54 PM:**
@zahary: you may be interested at this: https://github.com/ethereum/consensus-specs/pull/2802
- **From Marius to Everyone 02:56 PM:**
Been really helpful for us too, getting dos’d by teku did find a couple of weird races
- **From James He to Everyone 02:57 PM:**
keymanager-api standards providing a native way to onboard and offboard from a vc through API, prysm implementation of the 3 api endpoints in production, teku and lighthouse will have them in prod soon.
Joaquim Vergès an android tech lead @twitch has been helping with the implementation on the 3 keymanager-apis on web3signer / developing a generic ui for these api endpoints providing a much needed community implementation of a gui for clients who implement these 3 endpoints.
3 more keymanager-api endpoints were proposed for managing remote signer public keys.
prysm currently developing web3signer support for end of january
- **From protolambda to Everyone 03:05 PM:**
the balances tree and participation flags tree cause the state diff to blow up more than desired
the validator tree indeed doesn’t change much
When will infura be serving light-client requests with merkle proof?
- **From arnetheduck to Everyone 03:06 PM:**
validator db is a bit more half of the state - it’s also the part that keeps growing, the rest stays constant-size more or less
- **From protolambda to Everyone 03:07 PM:**
constant-size for latest state, but not if you store every historical state. Then validators tree is one of the better parts (infrequent changes) afaik
- **From Adrian Sutton to Everyone 03:08 PM:**
Would be good to get light-client requests available soon - there’s just quite a bit going on with merge and key manager APIs. Do we have a standard API for the light client requests yet? I know Lodestar did some apis but not sure if they’ve been written up as a standard API yet.
- **From protolambda to Everyone 03:09 PM:**
Probably better to ask lodestar directly after call. Maybe with nimbus if they’re interested in consuming those proofs as well
- **From arnetheduck to Everyone 03:10 PM:**
linear history of blocks + one full state a day = 30gb
- **From Trenton Van Epps to Everyone 03:12 PM:**
https://ethresear.ch/t/whisk-a-practical-shuffle-based-ssle-protocol-for-ethereum/11763


## Attendees
- Trenton Van Epps
- danny
- Enrico Del Fante
- Pooja Ranjan
- Paul Hauner
- lightclient
- Saulius Grigaitis
- Tim Beiko
- Marius Van Der Wijden
- ?
- Ben Edgington
- carlbeek
- terence(prysmaticlabs)
- Mikhail Kalinin
- ?
- Marek Moraczynski
- ?
- Cayman Nava
- Rafael (skylenet)