# Consensus Layer Call #76 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2021/11/18 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  1 hour  <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/pm/issues/418) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=31Jxh9_xXvY) <!-- omit in toc --> 
### Moderator:  Danny Ryan<!-- omit in toc --> 
### Notes: Avishek Kumar <!-- omit in toc --> 


-----------------------------

# Contents <!-- omit in toc --> 

- [1. Kintsugi office hours](#1-Kintsugi-office-hours)
- [2. Other client updates (if any)](#2-Other-client-updates-(if-any))
- [3. Research, spec, etc](#3-Research,-spec,-etc)
- [4. Open Discussion/Closing Remarks](#4-Open-Discussion/Closing-Remarks)

  - [Attendees](#attendees)
  - [Zoom chat](#zoom-chat)
  - [Next Meeting Date/Time](#next-meeting-datetime)

----------------------------------------------
**Danny**:  Welcome to the  call stream, stream should be transferred over. Okay we have officially moved over to ethereum pm repo. Merge calls need to be made while a go and other calls are replicated and archived. Issue today is 418 consensus  call 76 making progress.

# 1. [Kintsugi](https://notes.ethereum.org/@djrtwo/kintsugi-milestones) office hours

**Danny**: Okay to start today at Kintsugi office hours thank you, other client updates and any other discussion item we close it out.

## merge-devnet-0
 
 **Danny**: So I want to start with Merge dotnet zero which I believe is actually in progress. Pari, can you give us an update here.

**Parithosh**: Hello everyone devnet was started a couple of hours ago, we have get total difficulty yet but a consess client merge is ready done by respective forks. So yeah that was the [Configs are here](https://github.com/eth-clients/testnet-configs/tree/main/merge-testnets/merge-devnet-0). Expect sister enge because that was the first merge devnet by client.There is a deposit contract, and I have  some extra validators available if you want one. There is an explorer, but it has some issues right now. I am trying to figure that out and I will link any other debugging tools against it.

**Danny**: Great I think we can probably get an update in the next update but I will presume things we have a successful transition hopefully but it is likely that optimistic sync will fail on this network, so it may be hard to join for new people. Let's get into it: client updates general progress on Kintsugi spend, how things are going, any issue state of things.

**MariusVanDerWijden**:  Hey I quickly have a question for Pari. Do you mind if I mind it during the transition.

**Parithosh**: Yeah for sure, go ahead. In my choice it should be no problem at all.

**MariusVanDerWijden**: I have  plans to mine post-merge.

**Parithosh**: Ah! Okay feel free to ask as many questions as you want. 

**MariusVanDerWijden**: I generally cause chaos.
Composition:
EL: Geth, Nethermind.
CL: Prysm, Lodestar, Lighthouse, Nimbus
Plan to stand up a new devnet in one week.

## Updates

**Danny**:  Here we go , I sync the milestones officially adopted these days, did anyone want to  give updates on these things all together. Okay I am looking at  [milestone doc](https://notes.ethereum.org/@djrtwo/kintsugi-milestones) indicates that a few clients have hit milestone M2 which means open seminar coming  this week and open ship entries this week. Anything relevant you want to share. 

## Lighthouse

**Mehdi Zerouali**: Yeah so we know that Lighthouse has finished on-merge-block consensus tests this week. Marks working on milestone M3, but slow getting everything set up and client configuration running but making quite great progress.Forks started finalising some optimistic sync this week and expected to have it really next week. 

**Danny**: so what is running now is only the lockstep sync, so someone will not be able to sync consensus post transition to  Devnet right?

**Mehdi Zerouli**: Yes that is correct..

**Danny**: Cool,good to know.

## Prysm

**Terence**: Yeah I can go next on the Prysm side, pretty  similar to the Lighthouse. Lockstep sync working with Geth and will try with Nethermind today. Mostly focussing on optimistic sync pretty non figural changes. Yeah I want to thank Paul and their team that are doing great. Yeah thank you guys.

**Danny**: Thankyou.

## Lodestar

**Lion Depplion**: For Lodestar we have integrated Geth and Nethermind in CI.so every commodity we can see that we can run M1 & M2. Optimistic sync in our case is not hardly implemented and we are ready for the  PR and it should be up soon.

## Nimbus

**Zahary Karadjov**: On Nmibus' side we had reached to  M2 with Geth and Nethermind, but behind on optimistic sync.

**Danny**: Hope you get that soon. Cool.

## Teku

**Enrico Del Fante**: On Teku we are  working in parallel on optimistic sync and also in the consensus engine API call because API changes around the merges are not much significant from our side, so we are working to make some introgression tests.

**Danny**: Got it. Any body Geth  Consensus layer

## Geth 

**MariusVanDerWijden**: I can start with Geth. I created a branch called  “beacon on top of 4399”. This is the branch to use to join the merge testnet. We are trying to get Amphora specs into the master branch, which is a delicate process. We have to be more careful like not touching or modifying the previous code but yeah that could be done this week. Changes for all are already lined up so  looking good.

**Danny**: And what is the  status of Sync?

**MariusVanDerWijden**: So the “beacon on top of 4399” that branch has normal sync until TTD, and after that no one to get signal from the Consensus layer  so it will jump in to reverse header sync, so it should be working..
 
**Danny**: Okay Great!

## Nethermind

**Tomasz**: Hey from Nethermins side we have first clients on the M2 services milestone. Lighthouse, Lodestar, Nimbus. We are started working on Prysm, hopefully that will result  soon as well. We are also looking at integrating with mergemock.
 
**MariusVanDerWijden**:  Oh Mario  has recently join the foundation to work on testing. There is a nice test tool created for execution layers by him and he wrote a lot of really nice test.one thing notice that there is disagreement about how much the EL should check the timestamp. Nice to have a bit of discussion around what resolution should we use for checking the timestamp?

**Danny**: Okay, we can talk about after. Okay light client is also working on a testing tool different from Mario testing tool yes. Would you like to tell us?

**Lightclient**: we are working on a testing tool. Allows people to write full featured tests in Python. This tool supports both engine API and transitions of blocks. Mergemock is likely to be the runner for executing the tests, but equally Mario’s test tool could do this.

**Danny**: Got it and people are most likely currently using it.

**Lightclient**: I think Nethermind is usingIt I think they are having trouble because it does not support click. I do not know if there is one else.

**Tomasz**: sorry I miss that, what was it?I missed up

**Lightclient**: Merge mock. Are you also using merge mock?

**Tomasz**: Sure we are using it at interrupted and only at the beginning with Click and what where you mean Nethermind does not support click but it does support Click later it switches to Ether. Maybe it was more about Ether. I was just talking yesterday about being 50%of Merge mock because we wanted to use it for testing. Can it be boosted and will be looking into it probably tomorrow.

**Lightclient**: Oh it's okay. Message me if you guys are looking for any issue there.

**Tomasz**: Okay fantastic thankyou.

**Danny**: Okay any other updates on client software or testing software before we switch on to TTD override issues.

## TTD override issues

**Danny**: Okay Peter said in the chat that he does not like the mechanism in which the consensus client can override the TTD in the execution client as it means very intrusive changes. Mikhail, can you discuss your options?

**Mikhail Kalinin**: Yeah sure, so the option basically are  has [a doc](https://github.com/ethereum/consensus-specs/issues/2724) outlining options:
No override for TTD on the command line. An emergency TTD change (or change to terminal block hash, TBH) would require client releases to update (for both EL and CL). This may delay any action due to time for operators to update nodes. It may be acceptable nonetheless. TBH override is more time sensitive than TTD. There is a danger that operators only upgrade one of the two clients, which would be a problem.
Set the overrides separately on the CLI for each client. This may be quicker to execute.
EL leads and CL follows - but this probably can’t be made to work.
Can do both 1 & 2 and give users the choice, but this doesn’t improve on 1 only in terms of time to execute.

**Danny**: Okay ,I will note that these were exceptional cases that we will see on devnet in  next few weeks, where there will be some for the next consensus layer that will have the same TTD for next 3 devnet so it doesn't really accept those. These logic changes we really need to work through totally the fact the standard. Opinion on override if not  we w ill continue to work on this issue and any spec changes there. Any question about this  any thing that is not clear. Okay Mikhail I could say that we can prioritise on  Updating  EIP-3675 first, and work on the UX second. Cool.

# 2. Other client updates

**Danny** : Any other client updates generally people have.

## Lighthouse

**Mehdi Zerouali**:  Yeah Just maybe I am working on Flashbots integration for post-merge Ethereum. Michael  working on the standard key manager API. Looking into an edge case in fork choice and opening a spec issue I believe.

**Danny**: Yeah thank you Ryan and Medhi for managing the key API in client repo.

# 3. Research, spec, etc

**Dany** Great , move on toResearch, spec, etc.There is Issue 2727 raises a bug in fork choice. The solution is simple and simpler than the existing approach. It will be in the next spec release.Proposer boost fix will be rebased on top of this, and some more merge transition vectors added.Getting proposer boost done prior to or at the merge is on the critical path.

**Arnetheduck**: I want to talk today for  PR 2649 which is a historical batch to be considered. There looks to be a simple way to introduce this. It’s a step towards a world in which block data can be stored off-client and verified very elegantly. It would be good to get done prior to the Merge as it would be useful for handling execution blocks.

**Danny**: It  may be better to postpone the Shanghai upgrade (the first post-Merge upgrade), which is light on the consensus layer.

**Arnetheduck**: No, I do not think it is not. Small enough but any ways if anybody else feels that it’s a good idea to do it now. 
 
**Zahoor**:  Does it even make sense at all to store execution payloads on the consensus layer?

**Arnetheduck**: It  deduplication has been discussed, e.g. just storing the hash on the consensus side. Separate issue is where we store the actual execution data long term. Geth already has some capability to insert off-line data and propagate it. The new proposals combine nicely to help with both the deduplication and out-of-band storage issues.

# 4. Open Discussion/Closing Remarks

**Danny**: Okay Open Discussion/Closing Remarks for today.	

**Saulius Grigaltis**: So this is related to any discussion around moving deposit contract logic to the execution client? 

**Danny**: Most discussion is around just shortening the following distance to make deposits quicker.

**Saulius Grigaltis**: So basically that is, to implement a native way to handle reposits rather than using the contract.

**Danny**: no, nothing around removing the contract altogether.

**Pooja Ranjan**: I have a question related to the PM repo. I see the new agenda is Etthereum/ PM and old one is archived  but unfortunately I don't find the folder where the meeting for Note 76 will go.

**Danny**: Right I have not yet created. Tim and I are going to figure out where to put these notes. I guess we will make a new folder  and also need to Migrate the past meeting notes. Or the first person can also do that.

**Pooja**: So we have to make a new folder and copy all the previous consensus layer meetings to the new folder.

**Danny**: I think that makes sense, yeah.

**Pooja Rajan**: Okay I see the message from Tim to create new folder. I will sync with him, thank you.

**Danny**: Is there anything else?

**Leo (BSC)**: Yes, just concerning the crawlers. Nodewatch is now filtering peers by client version, but this is still not sufficient: multiple networks, not only the mainnet, are continuing to show up. I have submitted a PR to suffix this issue. Thank you.

**Danny**: Nice.thank you  

**Hsiao-Wei**: How to name The Merge upgrade parts? Community vote?

**Danny**: with the Idea that  Should be named after a “B*” star.

**Hsiao-Wei**: I would vote for that.

**Danny**: and paul has mentioned the name for  Clienting  the merge, what is the actual merge, the PR to be merged. Actually it is kind of difficult to communicate and Read about. So both the execution and consensus upgrades will need names since they will not be simultaneous. Okay any else or we can close it for today. Thank you everyone.

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

## Next Meeting Date/Time : December 2, 2021 at 1400 UTC.

## Zoom Chat 

- From danny to Everyone: 02:05 PM

https://github.com/ethereum/pm/issues/418 

- https://github.com/eth-clients/testnet-configs/tree/main/merge-testnets/merge-devnet-0

https://notes.ethereum.org/@djrtwo/kintsugi-milestones 

- From parithosh to Everyone: 02:06 PM

Ah I forgot to share the composition:

EL: Geth, nethermind. CL: Prysm, Lodestar,Lighthouse,Nimbus

- From danny to Everyone: 02:18 PM

https://github.com/ethereum/consensus-specs/issues/2724 

- From parithosh to Everyone: 02:29 PM

I’d set a much higher TTD next week and release configs a day earlier, so anyone can join in and go through the merge themselves.

- From danny to Everyone: 02:30 PM

https://github.com/ethereum/keymanager-APIs/ 

- From Mehdi Zerouali to Everyone: 02:30 PM

https://hackmd.io/@paulhauner/H1XifIQ_t 

- From Hsiao-Wei Wang to Everyone: 02:31 PM

https://github.com/ethereum/consensus-specs/pull/2727

- From danny to Everyone: 02:33 PM

https://github.com/ethereum/consensus-specs/pull/2649

https://notes.ethereum.org/@djrtwo/ry_muOtEt 

- From Leo (BSC) to Everyone: 02:48 PM

https://github.com/ChainSafe/eth2-crawler/pull/123 


