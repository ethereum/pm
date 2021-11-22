# Ethereum 2.0 Implementers Call 54 Notes <!-- omit in toc --> 

### Meeting Date/Time: Thursday 2020/12/17 at 14:00 UTC <!-- omit in toc --> 
### Meeting Duration:  30 mins  <!-- omit in toc --> 
### [GitHub Agenda](https://github.com/ethereum/eth2.0-pm/issues/196) <!-- omit in toc --> 
### [Audio/Video of the meeting](https://youtu.be/Eo7H8fZA23E) <!-- omit in toc --> 
### Moderator:  Danny Ryan<!-- omit in toc --> 
### Notes: Avishek Kumar <!-- omit in toc --> 


-----------------------------

# Contents <!-- omit in toc --> 

- [1. Testing and Release Updates](#1-testing-and-release-updates)
- [2. Client Updates](#2-client-updates)
- [3. Research Updates](#3-research-updates)
- [4. Networking](#4-networking)
- [5. Spec discussion](#5-spec-discussion)
- [Annex](#annex)
  - [Attendees](#attendees)
  - [Zoom chat](#zoom-chat)
  - [Next Meeting Date/Time](#next-meeting-datetime)


---------------------------------------------------
# 1. Testing and Release Updates


**Danny**: All right, here is the agenda. I do expect today to be short but I guess you never know. On testing releases there is some activity on the spec repo, there are some minor features that are being worked on that we expect  are going to be there I would say let's wait until January. We can spend some time making it kind of clear what the  intentions are and we can debate and go back and forth a little
bit , I think the low-hanging fruit. Here is a little bit of accounting reform on how attestations and things are stored in state. Adding a sync committee or light client, sync committee which reuses some of the
generally similar committee functionality both on the networking leveland in the in the spec to add a um
white client first support and some other small stuff, but again I think our time will be better spent  formalizing some of that stuff writing it down. Getting people up to speed and then we can discuss it in January. Additionally there is ongoing work in the spec on him.

 **Vitalik**: I should  interrupt in just those specific issues like  there are github issues and pull
requests and that you specs that you can look at already so on the accounting reform stuff if you just go into the polls section of each use specs so the most recent and recent two from myself i forget the
numbers but one says like accounting reform and the other says quotient, reform or something like that highly recommends for client developers to look at them and at least familiarize yourself with the proposals and comments if you have things to say.

**Danny**: Right and some of that in there moves some of the state accounting to the way it is. Generally optimized on epoch transitions anyway. So I think this would be a net benefit for things like empty block transitions and stuff which are currently probably a dos vector. Cool, so ongoing work there is also to make this testing a little bit more sustainable. I want to use a little bit of a different model and I expect that to come out early next year. Did no't really want to pull the rug on you on testing infrastructure right near launch but that is right. Let's see anything else on testing and releases. Mehdi, you got anything for us.

**Mehdi Zerouali**: Not much, crashes lately which is good. I guess we had to fix our fuzzers after a few
client updates messed them up still have one small issue with HongFuzz . The mutation based fuzzing engine not the structural one. It is spitting out way too many false, positives to be useful. So we need to basically implement some timeouts to give it enough time to initialize all the clients.

**Mehdi Zerouali** :  Yeah it has been good we have been working with Parry on deploying the fuzzers to the aws infrastructure. He's got some great ansible and terraform scripts but yeah pretty quiet, I would say no crashes to report which is good.

**Danny**: good thanks. Okay anything else here

**Hsiao-wei wang**: So about the test vectors. I have a proposal about adding the bls, serialization test posting here. I think I got some feedback from the clients and the os. The battery implementers, so I think they will  continue to implement it in our test vector but the interface might change if I found something new but basically the test will focus on the three significant bytes and the verifications.

**Danny**:  Great and this is after found a couple of issues in pi cc around some of the
serialization right shall we?

**Hsiao-wei wang**:  Yes. [Unclear at 8:00].

**Danny**:  Great, okay let's move on to client updates. we can start with Teku 

# 2. Client Updates

## Teku

**Cem Ozer**: Hi everyone  from the Teku side, we have been focusing 
- On optimizing epoc processing. Creating the first block of the epoch is still slower than others, so there is potential for further improvement but it is significantly better than it was and 
we are now not seeing blocks getting orphan often on Pyrmont anymore.
- Attestation for the first slot is also now much more accurate because block import times are faster . 
- We have modified eth1 genesis block search to be more tolerant of missing historical blocks. 
- We have reduced Beacon chain backing tree heat consumption and we significantly speed up as a seed in the serialized and we fixed the bug which could echo to produce invalid attestation aggregates, that’s about it.

**Danny**:  Nice and Prysm?

## Prysm

**Terence**:  Hey guys Terence here. 
- So we have added database backups at runtime for both and validate validator clients.  We also support team um reading graffiti from file and this is for the validator side and this was a highly requested user. 
- We have peer scoring enabled by default. We update it to Golang 1.15.6 and
- with disk io for validator client and this results in safesafer tester slashing protection which is great.
- Last but not least we have added one fallback option for the eth1 node and this was also highly requested by our  user and that's it thank you.

**Danny**:  I am curious about the fallback option. Is that if the api the connection fails or does it
try to detect if maybe the main option is following the head.

**Terence**:  We are just doing the api protection fail.

**Danny**:  Cool yeah I wonder maybe if you like look at peer count or some other stuff that might
i think that it is bad. I was just setting  that up the other day and did not know exactly what was gonna happen but thank you. 

**Danny**: Lighthouse?

## Lighthouse

**Mehdi Zerouali** :  Hello first of all apologies for missing the last call, two weeks ago. 
- We’ve   been working on enhancing our slasher. 
- So, we fixed a mis proposed slashing bug and 
- we added the option for users to broadcast their slashings. 
- We fixed a couple of io failures that were causing potential database  corruptions.
- I think like a lot of people there's been some eth1 client issues so geth works seemingly and seems to work really well. 
- But everything else seems to struggle so. We also added an eth1 fallback node and a while ago and 
- we also now have a manual flag for users to purge their ethernet cache for dodgy clients.
- We simplified the beacon lock files. We are now using os locks. 
- We almost completed the Standard http api the service and events are implemented now. 
- went and corrected some light attestations .
- we have been testing and analyzing gossip cell data metrics and scoring so, we found a little  discrepancy in the expected message propagation which will be corrected very soon in the
Future PR . 
- Yeah we are currently working on reducing our block proposal time and could not get down from 500 millis to about 100 millis. 
- Paul and Benedict are working on a beacon node fallback so kind of similarto the eth1 fallback giving users the ability to specify multiple beacon notes. 
- We started experimenting with a new scoring parameter to essentially help detect censoring nodes and that's about it.

**Danny**:  Great.

## Nimbus

**Mamy**: Hi so yesterday 
- we released our version 1.0.4. We did not announce it but we will be announcing it soon . Though some users found it still though the biggest change that we had were properly handling the termination signals for example making sure that the slashing protection database is correctly flushed on disk and closed. We added also a new performance scoring so that you can check if your system can keep up with the small requirement of chain. 
- Also importantly we fixed some bugs where we did not fully aggregation. We received and we forwarded them to the network and we ended up getting a bad score and we also fixed. Issue in gossip sub which led to a slightly worse attestation, effectiveness. 
- So right now we are focusing on a couple of performance bottlenecks. one is disk io, so when we have some io when we do attestation block proposal that we would like to reduce and accelerating state transition via having something called a state diff instead of storing the wall the wall state and lastly multi-threading that we plan to have the primitives done and we plan to  refactor or verify benefits from multithreading at two different levels and for maybe three weeks from now

**Danny**:  Great and Cayman

## Lodestar

**Cayman Nava**: Hello everyone 
- so the past few weeks, it turned outthat we had not implemented the api, the standard api but  we implemented those two things to end points. 
- We finally got on implementing and integrating theBLS   batch verification which really helped us and we have just been going through profiling writing beacon nodes and fighting finding low hanging fruits. 
- Some things as simple as you know like in lib p2p getting piers in in jsp is kind of a it takes a while so just doing our batch verification  ,so we are just doing less to try to get some final things together that are really stopping us from having a responsive beacon node all the time. 
- We have decided to cut releases every two weeks. So we're just going to do like a really that kind of release schedule so that's it from us.

**Mamy**: Can people try to Lodestar on Pyrmont a pyramid?

**Cayman Nava**: Yes so it works. I will say currently
 so you could pull it down from either master build it or from npm but one thing, it will kind of pause every few minutes. But it will stay on the head but it will not be responsive at all times. So, We are working through those last things.

**Danny**:  Great, I lost my agenda page but I am pretty sure next up is research updates anybody wants to go to.

# 3. Research updates

**Vitalik**:  So on the sharding  front then I am not sure if I mentioned this in the previous call but  the data availability sampling starting is now in a PR . It is also one of them to get more recent ones in the pr list. So that includes the  beacon chain transitions and there is also a separate document that the pr links to that has been around for a while that basically talks about like how the data availability sampling works. And (?) has been doing some excellent work on optimizing proof generation and making it look like generating the inclusion proofs for or the correctness proofs for branches of a block is going to be much more practical. Possibly somewhere around eight  times faster or more than we had thought before which is potentially good news because it just reduces the headaches that we might  expect from my needing from a block proposing otherwise block proposing just a significantly simpler process.

 **Danny**:  Can you help us understand the complexity of implementing Kate commitments in terms of what type they are? How much is it built off of existing bls libraries and things versus?

**Vitalik**:  Really good question. So I think one really important thing is that you need to have a library that exposes bls operations.  So multiplication and addition being the most important ones and ideally you want this fast linear combination some aka multi-exponentiation which basically just takes a whole bunch of points and a whole bunch of coefficients. Multiplying each point by the coefficient sums them all up and gives you the output basically there is you know optimized ways of doing that are potentially up to something like 10 times faster than for large inputs than doing it the kind of naive way. so if you have
libraries that do those things saying if you do not have the fast linear combinations that you could also just code it yourself. So if you do have things it is actually not that hard and so making a Kate commitment for a piece of data just what it really means is a step. You have a kind of pre-existing set of points which would basically an ffg of the trusted setuprre-computer fairly easily and you just take the first object. You just  basically do a fast linear combination of the setup to get
to a block. So you do the first point multiplied by the first piece of data plus the second point multiplied by the second piece of data and so forth. so  Kate commitment data is easy.  verifying a proof is an inclusion proof is also easy and basically it is just a single pairing check  and now generating all inclusion proofs isthe thing that incred (?) has been working a lot on optimizing but the good news is that it is still something like 41 to 50 lines of python code or you can probably just take the python code and translate it. So my opinion is that it should not be all that difficult actually.

 **Danny**:  This is a known enough quantity that it can be worked on today?

**Vitalik**:  I think so.

**Dankrad Feist**: Once again if we have the bls library support right. I mean I think  for blst. I think you have to wait for them to expose those.

**Mamy**: I can give you some comments about the library support but just to make sure we do not need fft  because it is simple enough that we can just use a multi-scalar multiplication right?

**Vitalik**:  Correct so the fft is needed in a couple of places. So one place is to generate all inclusion proofs for a block so to generate and inclusion proofs in analog n time instead of an “n” squared time. You need the  fancy algorithm which  Dankrad & I  have created by adapting this earlier thing from Demitri and one other person and that uses ffts internally and the second thing is that the (?) trusted setup that you normally see comes in the form of a sequence of powers but in order to just commit to a blog. You want one that comes in the form of being in sequence of evaluations and converting from one to the other also requires an fft. 

**Mamy**: Okay so in terms of the state of the bls libraries that we can use. Remember that with my very first talk with Supranational back in april that was one of the things they wanted to look at the multiscalar  move but I do not think it is ready yet. However Consensys has a library called golf and gnark for snarrks and 12--381and they have the multiscalar multiplication that is also multi-threaded and that they optimized  heavily and the  Zexe Zexe project has also a library in Rust. Recently they are renamed to Artworks and they also have a heavily optimized bls 12-381including fft and multiscalar multi and I think it can
also even work on GPU.

**Vitalik**:  Oh! excellent. So I know looking at the libraries that are being used for snarks. Definitely seems like a potentially fruitful route to take. But they are one thing I want to stress is that there definitely is value from working  on the cate pieces sooner. The reason basically is that we really wants to just get the statistics on how, what  is the runtime of one of these things in practice? I mean basically adjust them like if we have that statistic. I think it significantly de-risks the whole thing.

**Dankrad Feist**: Also I am very happy to create a little intro to the fft on group stuff like the method
to create all the proofs. So if as soon as anyone is kind of saying they want to start working on this. I would create something to get them on board.

 **Danny**:  Yeah I think it maybe in  january,  it might be a good time to do some various knowledge transfer so, we can all kind of get up to speed on this and some other stuff that we are
looking to do next year. All right I need to totally derail you there.

**Vitalik**:  I think that is the main new stuff happening on the research front. No, I can not think of anything else.

 **Danny**:  okay, anyone else

**Justin Drake**: I mean related to the data availability sampling, I guess one aspect is then possibly you know. Slightly modified DHTs  with new properties like low latency and I guess **one of the things we are looking to do is hire a networking expert** who could maybe help us a different foundation investigate these issues. So if you know anyone please pass them on.

# 4. Networking 

 **Danny**:  All right  any other updates here. All right, great, are there any other updates? All right, we had a networking call one week ago. There is a to-do list that I need to get to thank you for taking notes Ben. Are there any other  networking components people want to discuss today? 

# 5. Spec Discussion

**Danny**: Okay and general spec discussion. Like I said  there is plenty of movement on the spec. I think **it makes sense to have at least one person on your team keeping up on the various developments and engaging**  and very well have plenty of good stuff to talk about maybe like a first hard fork and like I said I think it would be a good time to maybe get on some calls and make sure. We like to write down a lot of stuff to just do some knowledge transfer and get people up to speed because there is plenty of engineering, r&d tasks to begin to tackle here other than anything people want to discuss today.

**Vitalik**: Do we want to talk about fork choice things at all or is that just the kind of I keep
quietly working and figuring it out.


 **Danny**:  Let's I would say let's pick that up in the new year 

**Vitalik**: yep makes sense.

**Vitalik**: I mean for anyone listening the quick update is basically that there is some multiple small tweaks to the fork choice rule that we have been pulling over in order to  address all of the issues that  some academic people have found with the fork tourist role, basically some theoretical issues with
liveness. So yeah we will like and the ideas on exactly what to do have been around for a couple of months now but just kind of pushing them forward to something close to a ready-to-go stage and kind of underneath.

  **Danny**:  That is more of a general. Just contemplation of liveness in general because as you aware the fork choice you know is lmd ghost but then has a number of these like tweaks and fixes to make it more alive under the attacks found. Which is a game of whack-a-mole which is maybe not the like. 

**Danny**: Okay um anything else at all that people want to discuss today before we take a law at least for this. Yeah okay fair,  thank you excellent work as always happy to see main net very stable and have a great holidaystalk to you all soon

**Dankrad Feist**: Thank you bye

----------------
## Attendance

- Danny
- Leo BSC
- Vitalik
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
- Ansgar Dietrichs
- Proto Lambda
- Ben Edgington

## Next Meeting Date/Time : TBD

## Zoom Chat 

From Terence to Everyone: 02:05 PM

Accounting reform: https://github.com/ethereum/eth2.0-specs/pull/2140

From Vitalik to Everyone: 02:06 PM

And https://github.com/ethereum/eth2.0-specs/pull/2150

From Hsiao-Wei Wang to Everyone: 02:06 PM

https://github.com/ethereum/eth2.0-spec-tests/issues/24

From Terence to Everyone: 02:18 PM

https://github.com/ethereum/eth2.0-specs/pull/2146

From Mamy to Everyone: 02:26 PM

Consensys Gnarks/Goff and Zexe/arkwork-rs

the consensys work is nice because it’s quite stand alone
you just copy paste those files: 

https://github.com/ConsenSys/goff/tree/master/examples/bls381



