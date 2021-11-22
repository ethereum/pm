# Ethereum 2.0 Implementers Call 62 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2021/04/22 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  47 mins  <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/214) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=D9Aqr8thF9c) <!-- omit in toc --> 
### Moderator:  Danny Ryan<!-- omit in toc --> 
### Notes: Avishek Kumar <!-- omit in toc --> 


-----------------------------

# Contents <!-- omit in toc --> 

- [1. Client Updates](#1-client-updates)
- [2. Altair](#2-Altair)
- [3. Research Updates](#3-research-updates)
- [4. Spec discussion](#4-spec-discussion)
- [5. Open Discussion/Closing Remarks](#5-Open-Discussion/Closing-Remarks)

  - [Attendees](#attendees)
  - [Zoom chat](#zoom-chat)
  - [Next Meeting Date/Time](#next-meeting-datetime)

-----------------------------------------------
**Danny**: Okay, stream has been transferred over. We will discuss Altair and final spec.  and have a conversation on where we stand on engineering and Atair. Also give an update on spec repo and testing. Let's begin with a client update and we can go withTeku.

# 1. Client Updates

## Teku

**Ben Edgington**: Okay that me. Altair work is going well and I expect we’ll be done with it by the end of our current sprint in two weeks and specifically on Altair:

Reference and fork choice tests are all passing.
Gossip changes are done.
We’re working on the validator API and duties. For this, we are following the API
format proposed by Jim McDonald.
We’ve got logic to parse the Altair fork info from the configuration file and construct fork and forkSchedule objects that transition at the specified slot.
We are almost done with the blocksByRange and blocksByRoot RPC methods for Altair. So that's the main thing that will be working.

In other news, we will be migrating our default database from RocksDB to LevelDB over the next couple of releases. We’ve been running LevelDB in some of our test infrastructure for a couple of months now, and it seems altogether more pleasant than Rocks. In particular, memory consumption is much improved. We’ll make sure this is as transparent as possible for Teku users of course and we have a release coming tomorrow with a few features worth noting:
First, we have a nice community contribution for specifying multiple Eth1 endpoints and have automatic failover in between.
Second, Infura is now providing beacon chain state snapshots. On a fresh Teku install you can point to Infura’s API endpoint and be fully synced and running in under a minute. We’ve had snapshot sync for a while now if you have another running node, or a recent state file around. But being able to start up directly from Infura is super convenient.
Finally, we are now storing orphaned blocks in archive mode and providing an API to retrieve them. This was a feature requested by some of our users. That's all a goal.

**Danny**: Alright , Nimbus

## Nimbus

**Zahary Karadjov**:  well I guess I should take up. Quick update 

With release versions 1.2 and 1.2 1, they represent big  improvements in performance of Nimbus.

With the introduction of batched verification of incoming gossip  location of ink, we achieve roughly  between 30% and 50% reduction of CPU usage of the time. Right now  for example we can  process all the upstation from the bottom network on the nodes that are running 2010 validators without the maximum out the CPU.

 And other updates, new features, an implementation of the official REST API which is currently in beta.  Just like Teku we have implemented failover ETH 2 providers. anotherI like New “lazy” attestation packing algorithm, which has increased block rewards and discusses the major improvements for this week.

**Danny**: And how is Altair Development?

**Zahary Karadjov**: Altair development is making progress. Focusing more on Rayonism, and ready to participate in the first testnet.

**Danny**: Okay great. Lodestar

## Lodestar

**Cayman Nava**: Hey here we go:

As for Altair, we were  passing both fork choice and spec tests with a naive implementation of state transition.
 
We are working on networking part and validator duties. v0.20 is out, a minor release for stability updates. 

We are working on a light client for the Scaling Ethereum hackathon rather than Rayonism.

**Danny**: Nice, Prysm

## Prysm

**Terence**: hey guys it’s me. 

So on the Altair front we finish implementing a state transition.
We are working on networking and validators stuff right now. Good news is that  Spec tests are passing for state transition.
New slasher implementation that will be in a release next week. Much more performant.
Interop achieved with Catalyst for Rayonism. But there is a bug in the hash tree root for nested lists.
Last but not least welcome to new hire, Casey. I am sure we will meet him soon

**Danny**: Good. 

## Lighthouse

**Mehdi Zerouali**: Hi, we are Passing spec tests for Altair. We are planning to merge consensus changes soon.  We had lots of refactoring to handle forks. Remaining features to be done are sync committee changes and validator client updates. On networking, RPC and gossip changes have been implemented, started work on discovery. Opened two issues on the specs repo: #2314 (Participation rewards are skipped for epoch prior to Altair upgrade) and #2347 (Altair p2p MetaData should contain syncnets field). Would appreciate review from others. LH will be participating in Rayonism. We are planning a big release with doppelganger support and memory improvements. Recent release improves attestation handling and block packing. We Will start development of the user interface in May. 

**Danny**: Okay thank you Yeah 2314 Michaeal has an original comment in regards to Light house. I was seven days ago and have a few options that we are going to see. I do agree doing nothing is not a good call but I also think that during a map for increases the potential increases please do take a look.

# 2. Altair

**Danny**: On the Altair front  thanks to engineering progress.

## Engineering progress

**Danny**: Looks like a couple of weeks until we’ll be able to run testnets.

**Terence**: yeah it sounds good.

**Danny**: This enables us to make the original target by the end of June for deployment a little early. Especially with Rayonism also happening.Eth1 London fork is planned for Late July (or early August). We can plan our fork when we know the date for London.Important to do Altair “right” rather than “fast”.Review in two weeks. Clients should let the others know when they have a viable Altair implementation.

## Spec and Testing

**Danny**: Some additional tests for corner cases, and some fixes are coming. There will also be some transition tests. These will be in another pre-release next week, but there are no new features. Any other things on Altair issue that you want to discuss today.

**Jacek Sieka**: I had a question for Ben regarding snap shorts that sync in Jira. I am querious when somebody tries a separate line and things It does not get blocked right. So what  happens next when somebody needs to sync with Teku.

**Ben Edgington**: we can possibly discuss  this offline but it is just like sorting Genesis again . I mean it basically downloads the SS which the states  oh I see is the back filling Blocks . Yah we do I need to check on that. Do you think about pay scoring each other for not having the booked history?

**Jacek Sieka**: Yeah those scoring and you know once nobody has the search blocks then we do not have the minimum.

**Ben Edgington**: Yeah , we are not currently planning to Implement that. We don't see any issue if people simultaneously continue everybody on the network and drop the whole history, so we are not currently very concerned about it but definitely willing to discuss.

**Danny**: Like I said you well block filling of Genesis we are not concern about starting to put back the genesis

**Ben Edgington**: So we are happy to start for the translation to just report and we are the reserve block before that I think we do not have the block currently.

**Danny**: one more question on how validating that states. Is it generally safe or you having some checkpoint to technical issue that revives on validating issues .

**Ben Edgington**:  I think when we have all agreed on a single distributary method to check states  it looks like I think we can incorporate some safety net  but currently it is just simple trust which the table has been given which is not a long term sustainable model . we don't yet have I think understanding what a network interested check point looks like.

**Danny**: How do you currently make sure or authenticate that state is coming from the insurer.

**Ben Edgington**:  so you provide your impeier url and it is secure by the normal means.

**Danny**:  okay, anything else on Altair basically. Any thing on optimisations for Altair.

**Proto Lambda**: I have concern. I am  thinking about two optimisations for Altair. 

Reduction in hashing for tree of participation records. Currently random access - there may be some optimisations available; talk to me if you’ve done any work on this. 
Sync committee pre-computation. Note that the computation differs from that for existing committees, due to differing timescales.

**Danny**: Thankyou. Any call or question to Proto. Okay let moves on to Research Updates.

# 3.Research Updates
 
**Danny**: There are regular bi-weekly  merge calls.Proto is still managing 3 office call every week
on Rayonism but beyond those two are any research updates or updates that people like to share.

**Proto Lambda**: I am wondering about the calls tomorrow. It will be a little bit different if we have EthGlobal and merge smith on the call. So no Rayonism escapes our call or will be moved because conflicts with EthGlobal presentations and you all are welcome to watch the presentation of course.

**Danny**: Okay any other research update you would like to share.  

# 4.Spec discussion

**Danny**: Proto did some work on the latest sharding designs, so take a look.

# 5.Open Discussion/Closing Remarks

**Danny**: Sigma Prime is looking at reviving Beacon Fuzz for Altair. Also Note that there is an extra all core devs call tomorrow. Monday or Tuesday, there should be an initial Rayonism testnet, with something longer-lived by the end of the week. Thank you.
 ----------------------------------------------------------------
## Attendance

- Danny
- Leo BSC
- Vitalik
- Jacek Seika
- Patricio Worthalter
- Nishant
- Dankrad Feist
- Justin Drake
- Mamy
- Cayman Nava
- Mehdi Zerouali 
- Cem Ozer
- Terence
- Hsiao-wei wang
- Carl Beekhuizen
- Aditya Asgaonkar
- Alex Stokes
- Mikhail Kalinin
- Barnabe Monnot
- Zahary
- Pooja Ranjan
- Ansgar Dietrichs
- Proto Lambda
- Ben Edginton

## Next Meeting Date/Time : May 06, 2021 at 1400 UTC.


## Zoom Chat 

