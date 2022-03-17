
### Meeting Date/Time: Thursday 2022/3/10 at 14:00 GMT
### Meeting Duration:  30minutes
### [GitHub Agenda](https://github.com/ethereum/pm/issues/489) 
### [Audio/Video of the meeting](https://youtu.be/SEVY6-Zr2OM)
### Moderator:  Danny Ryan
### Notes: Alen(Santhosh)


**Danny**
* Hello, welcome to Consensus Layer Call. fixing something real quick and then we'll get started. Okay. It is fixed. This is issue 489 On PM. Repo. Sorry, I'm dealing with one tiny technical issue. 
* Sorry about that. We are now good to go. Is issues 49 shared in the chat? we will spend as much time as necessary on kill on the merge, and then go into our normal discussions. thank you for joining. Let's see, I don't have anything under the Kiln  agenda, but there's plenty to talk about the, I think most pertinent thing is the launch of the Kiln, the public, the not dev net that has not killed. I think Perry and or Mikhail probably have the most up-to-date information. Would you mind sharing that with us? 

**Pari**
* Yeah, everyone. yeah, so we have the kin conflicts that went up yesterday. the Testnet itself is about 104 hundred and 5,000 validators and a couple of client teams, are participating. So they've already been sent in the moniker and would be, validating with them if anyone else wants to join and doesn't yet have validators and we can just make deposits for you guys. all the tooling links have been posted and we are slowly working on a guide for each and every client. if you guys do make releases with the conflict built in, then please let us know. So we can update the deck. TTD is set to be like a hundred million or something like that. So based on last week's run, that should last us up till mid of next week. but it's almost impossible to know if someone from the public run Tibet, run the miner and choose through the TTD, but we're hoping that it will last for these to be 

**Danny**
* Awesome. So is the proof of work and the proof of stake Genesis had they already occurred at this point? 
* Ah, yeah. Good kind of mentioned, proof of what Genesis has occurred. Proof of stake Genesis has not happened yet, so we can change. Hasn't been launched yet. The beacon chain would go live tomorrow around this time. yeah, that's, that's the main difference and the much folk epoch has, I think, EPUB  150, so about half a day or a day. 

**Danny**
* Cool. And I believe the eat Staker folks are trying to do a party call, but now they have to feel the pain of proof of work and scheduling. so they'll probably release some details soon And I do believe, on the EF blog, we'll have a blog posts go out either today or tomorrow about details here. So keep your eyes peeled if you are listening and you want to participate in, learn more. Okay. did anybody have any questions about Kiln questions? 

**Ben**
* Quick recap on why it was put back by 10 days or so, cause this is not what we agreed at the last meeting and I'm very mindful of little delays, So  It will just alter,There are two things that we're attempting to do.

**Danny**
* One is to have the technicals ready and to vet things and to run stuff for long enough. and to understand what's going on the other is to engage with the wider community, merged Avnet five handled the former kept things moving on the former. So I didn't, there's no delay there. whereas the latter was simply not ready for public engagement. and so although the technical stream continued to move forward at the pace that was, at whatever pace developers could do, we couldn't really enter into that secondary stream, but it was decided that the secondary stream, which engages with users, this month wouldn't actually delay the release of test nets in April. the only thing that would really do that would be if you push that way back or if the technical stream was the delay. so we kind of and wanted to ensure that the public version of this was ready. that's that was the discussion at least had last week. 

**Ben**
* Got it. Okay. Thanks. Makes sense. 

**Tim**
* Yeah, I mean, and, and part of, part of that we could debate whether that actually shifts the timelines, but that was the, that was the discussion. And as of now we did not plan on delaying the public test that's in April. 
* Yeah. And I think one thing I'll add on, on, on what Danny just said, it is, you know, what's really important with Kiln is getting as much kind of real-world usage. but now it's really important to try and reach out to folks and get them to, deploy application tests and then Tulane make sure that it's not only like deploying an actual smart contract on the main net, but it's, or on killed, but it's, you know, deploying your contracts through some pipeline, you know, what your, what your, CIA tools, making sure that your front end works, making sure that things like truffle and hard hat and that stuff works, so that we don't have any kind of bad surprises when we, when we fork the actual test that 

**Danny**
* Cool other Kiln or merge related comments or discussions, 

**Mikhail Kalini**
* I have a minor update on the 2.1 release. So 2.1 it's released now. it doesn't have, any, yeah, it's a it's backwards compatible with, with two and then pretty sure that's, we're sorry, like these persistent testnet with, with two, then clients will be able to upgrade to 2.1 independently. So it has to like change that requires, changes to implementations for Swan is the quality of service on exchange, physician configuration, method. And another one is the, related to optimistic sync. yeah, basically it allows for in Berlin, any post-marriage block domestically. So any blog that is, the descendant of the transition block can be applied to the fork choice of domestically. and yeah, it's considered safe. it's just, you know, makes it simpler the code, openness. So it doesn't introduce any breaking changes. That's like short update from my side. 

**Danny**
* Thank you. And I believe, yeah, go on. 

**Marius Van Der**
* I have a small update for, for the merge, that the engine fast stuff. So I've, I've written a differential fuzzer to test different implementations of the engine API against each other, on the consensus layer. And, I, updated that to the, to the new spec and I'm currently starting to add clients to it right now. It's only doing and it immediately finds a fence, a difference between gas and diesel. And that's probably because of some, some, a reverse sink in, in diesel. but I'm planning to add another minds and if you're in JS, to it, and then as soon as Aragon is ready also, Eric one, if other folks are interested in being added to that, then they should just contact me. 

**Danny**
* Progressions is probably Mario's, high  API tests I would presume. 

**Marius Van Der**
* Yeah, exactly. And we're also trying to the other, execution layer clients who the two, the hive tests so that we can execute the tests that we already have. 

**Danny**
* Got it on that note, any other, testing updates. I know that the, METI and some others are kicking off, getting decomposed up to Bellatrix targets. so I believe by end of the month, that should be in the, in the fuzzing infrastructure. 

**Danny**
* I have like a small discussion for, do we want to fill out the Kiln milestones? So I see some clients find some dates here, but others fail, then 

**Tim**
* I would push for it just because I think there's like thousands of you. Yeah. There's like 7,000 views on that page almost. So if people want the quickly updated, I think that would be valuable. or even if, if you're too busy to update the actual table, but you have a tracking issue or something, I don't mind doing it on behalf of clients, myself. but just cause there's thousands of views on the page. I think it'd be good. 

**Danny**
* Yeah, I agree. And, I guess just to state it out loud, we're running, Maurice we're running the bad transaction or transaction fuzzer in bad blocks on Kiln. 

**Marius Van Der**
* So the transaction has a it's running intermittently, every now and then every time I have, an Exxon freeze CPU cycles and running the transaction further and, the bad block generator, I updated the bad block generator to the new V2 spec. But, I don't think we have a node running that at the moment. 

**Danny**
* Okay. I'll probably be valuable soon. 

**Marius Van Der**
* Yeah. But that also the bad block generator only generates better blocks after the merge. So it's not really useful before that. 

**Danny**
* Gotcha. Another thing that I think would be valuable for this or other kind of simulation type tests is to have, quite as, maybe quite as interesting as what's going on in the transaction world, in terms of what you can do, but probably worth sending some, some operations 
* Mid week. Good luck estimate. We'll plan on doing on the consensus layer side for a release, a, I guess semi major version bump or major version bump. I think we did a major version bump, at Altair, or not. I need to go back and look anyway, we will do a release probably at the end of March when we are making decisions about forking testsnet. So whenever we're doing that and Kiln has been running for at least a couple of weeks, we'll get some sort of more frozen, official release together. we might see some iterative tests factors come out in the meantime or doing a pass just to make sure we have the coverage that we need. Anything else on the merge before we move on? 

**Pari**
* Just one more point, it would be creative inflammable. Didn't recognize that and would not serve you any content. And while we can argue that execution punch, shouldn't be accessible by DNS and inlet setups, which use Kubernetes that is by default, what's going to happen 

**Tim
* Well, sorry. I actually have some  really quick, yeah. TJ rush, our resident difficulty valve expert and someone else on three search who handle as you'll see anyways, they put together a duende dashboard, looking at, the amount of blocks that gets produced on mainnet per week, which is basically a good indicator for when the difficulty bomb is going to suck the kick in. So it looks at like all of the theorem is history. 

## Other client updates
**Teku**
* Is updating CLI options to remove the -X experimental prefix for Merge things. The kiln network is now supported in the master branch. Release early next week.

##Fee recipient handling
**Prysm**
* Implementing fee-recipient handling.

**Lighthouse**
* Fee recipient stuff is in place, but could do with some polishing.

**Teku**
* Available from the next release.

**Marius**
* The coinbase can be specified on the Eth1 side - should we override the consensus client if it does not provide a coinbase? Note that Geth currently won’t start the miner if the coinbase is not set. [Danny] If the consensus layer is not providing a useful fee recipient then using information on the execution side to set it is reasonable. Alternative is to not allow a validator client to start without having fee recipient set - at least it ought to be noisy about it. Teku will not start if it has validators but no fee recipient, and also will refuse to propose a block. Refusing to start might be too severe, as a validator can still attest with no fee recipient set. [Marius] We’ve learned that most people don’t look at logs - better to blow up quickly rather than run a bad set-up. But the contrary view was put by [PaulH].
* Teams to consider how to handle this for their own clients.

## Research Updates

**Blob transactions**
**Proto**
* EIP 4844 consensus layer changes (blob transactions) has been moved in to consensus specs repo. Please review and comment.
* Prysm has an experimental branch with the changes.

**Proto**
* Would like some review on the sync method for the blobs. Similar to getBlocksByRange method.
* Working on some benchmarks for the KZG commitments ahead of next week’s ACD call.

**Further discussion**
* Plan is to implement this when the withdrawals fork takes place (corresponding to the Eth1 Shanghai or whatever name fork).

**Proto**
* EIP 4844 (as currently specified) does not affect the beacon state format. There is a small change to the beacon block format.

**Saulius** 
* Grandine has done some benchmarks of KZG commitments with different libraries and some parallelism that may be useful. [If ckzg is my own c-kzg library, then I am happy to see that it looks to be the quickest :rocket:]

## Spec discussion and AOB
* What’s the plan for hosting specs that span both consensus and execution layers (meta-specs)? [Tim B] There are advantages to using EIPs for this - it’s a tried and tested process. Execution specs are moving closer to looking like the consensus spec. EIPs could then contain prose explanation plus links to a PR against each of the consensus and execution specs. [Proto] Request to discuss in next ACD call.

**Micah** 
* Please bear in mind that there is already a shortage of EIP editors. [Tim B] Ideally the new process would be less work overall.
* Any updates on algorithm for calculating safe head? [Dankrad] There are some issues with the LMD part of GHOST that are making things harder than previously thought. Continuing to work on this. [Danny] Suggest continuing to stub “head” for “safe” until this is resolved and not exposing this to users via the Eth1 API. Could use “finalized” instead, but best approach is not to allow the execution layer to expose this information until it is sorted out.
* There is a call tomorrow to discuss the Eth1 fork naming for the fork previously known as Shanghai (tomorrow 1400 UTC).
* Note that daylight saving is starting in the USA, so meetings will move around - they are anchored to UTC!

----------------------------------------------------------------
## Attendance

- Danny
- MariusVanDerWijden
- Pooja Ranjan
- Mehdi Zerouali 
- Ben Edginton
- Enrico Del Fante
- Terence
- Tim Beiko
- Saulius Grigaitis
- Dankrad Feist
- Mikhail Kalinin
- Zahary Karadjov
- Tomasz
- Hsiao-wei wang
- James He
- Leo BSC
- Parithosh
- Alex Stokes
- Lion dapplion
- Zahoor
- Cayman Nava
- CarlBeek
-  Lightclient
- Ansgar Dietrichs
- Arnetheduck
- Nishant
- Aditya Asgaonkar
- Vub
- Trenton VanEpps 

----------------------------------------------------------------

## Zoom Chat 
* From lightclient to Everyone 02:01 PM: gm
* From Me to Everyone 02:01 PM: gm
* From protolambda to Everyone 02:01 PM: gm
* From terence(prysmaticlabs) to Everyone 02:01 PM: gm
* From Enrico Del Fante to Everyone 02:01 PM: gm
* From danny to Everyone 02:02 PM: https://github.com/ethereum/pm/issues/489
* From pari to Everyone 02:03 PM: https://kiln.themerge.dev/
* From Lion dapplion to Everyone 02:05 PM: What’s the initial validator count of the network?
* From pari to Everyone 02:06 PM: 104k validators General public have already made a dozen validators
* From Lion dapplion to Everyone 02:06 PM: That’s the target for the next 1-2 months? Or want to ramp up to 300k
* From pari to Everyone 02:06 PM: Currently we have no plans to scale it to that degree
* From Mikhail Kalinin to Everyone 02:09 PM: https://hackmd.io/@n0ble/kiln-spec#v21-change-set
* From Mikhail Kalinin to Everyone 02:13 PM: https://notes.ethereum.org/@timbeiko/kiln-milestones
* From pari to Everyone 02:14 PM: Nope, no node running bad block generator yet.
* From Tim Beiko to Everyone 02:18 PM: https://dune.xyz/yulesa/Blocks-per-Week, https://ethresear.ch/t/blocks-per-week-as-an-indicator-of-the-difficulty-bomb/12120/2
* From Micah Zoltu to Everyone 02:29 PM: We should assume people don’t look at logs at all. Fail hard, fail fast.
* From Micah Zoltu to Everyone 02:31 PM: How about SHOULD hard fail if there is no validator at startup? Clients can have exceptions, but barring a good reason you should fail hard and fast.
* From Lion dapplion to Everyone 02:33 PM: Do expect users to provide the fee-recipient at the validator binary or beacon node binary?
* From Enrico Del Fante to Everyone 02:35 PM: On teku side, if you run in single-process mode the param is the same. If you run in two process we actually want the param to be specified both side
* From terence(prysmaticlabs) to Everyone 02:37 PM: Prysm prototype: https://github.com/prysmaticlabs/prysm/pull/10315
* From Marius Van Der Wijden (M) to Everyone 02:37 PM: i think retrieval of individual blobs is too inefficient
* From Paul Hauner to Everyone 02:37 PM: I accidentally DMd this, but LH accepts fee recip on BN and VC but we recommend users supply to BN. The prepare_beacon_proposer endpoint suggests it should at least be on the VC.
* From terence(prysmaticlabs) to Everyone 02:41 PM: I just had a thought, in the config file, do all clients consider the case if the operator inputs an address that is pending status and which doesn’t have a validator index?
* From Saulius Grigaitis to Everyone 02:49 PM: https://github.com/sifraitech/kzg, https://github.com/sifraitech/kzg/runs/4868992790?check_suite_focus=true benchmarks
* From Tim Beiko to Everyone 03:03 PM: “Unsafe-ish”, Small nit: would people generally prefer “final” over “finalized” in the APIs, so we avoid the English vs. American spelling issues?
* From Micah Zoltu to Everyone 03:04 PM: unsafe, safe, final?
* From Tim Beiko to Everyone 03:04 PM: Very weak opinion, fine with finalized, +1 on consistency
* From Marius Van Der Wijden (M) to Everyone 03:04 PM:  finalised?
* From Mikhail Kalinin to Everyone 03:05 PM: bikeshedized!
* From Adrian Sutton to Everyone 03:05 PM: Zed everyone, not zee. 😛
* From danny to Everyone 03:05 PM: ised*
* From Marius Van Der Wijden (M) to Everyone 03:05 PM: finaliczed, finalißed
* From Tim Beiko to Everyone 03:05 PM: Whoever volunteers to maintain the JSON RPC spec gets to choose :-D
* From Micah Zoltu to Everyone 03:05 PM: How about finalized, but we require everyone who spells it pronounce it zed? Worst of all worlds.
* From Marius Van Der Wijden (M) to Everyone 03:06 PM: 🚲⛺
* From Tim Beiko to Everyone 03:07 PM: Going downhill fast: From Marius Van Der Wijden (M) to Everyone 03:07 PMcouldn’t find the shed emoji

----------------------------------------------------------------
