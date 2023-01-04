# Ethereum 2.0 Implementers Call 28 Notes

### Meeting Date/Time: Thursday 2019/11/21 at 14:00 GMT
### Meeting Duration: ~ 1 hr 20 mins
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/101)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=DzLrxuN55VA)
### Moderator: Danny Ryan
### Notes: Pooja Ranjan

----------

 **Danny**: Welcome everyone!

 ## 1. Testing and Release Updates

 **Danny**: Testing generally stable, Mehdi will add more.
 As for release, I do have a pending release on GitHub with some minor clarifications in changes, specifically clarify some things. It might change one test vector, will let you know. Other than that everything is good.

**Mehdi** : Hi everyone!
* Some of you may have seen danny's update. Sigma Prime has been awarded grant from the Ethereum Foundation to do work on Beacon fuzzer and differential fuzzer.
* Will be ramping up our efforts on Beacon fuzz from next week, allocating more time and resources.
* Since the last update, we've managed to cleaned up the fuzzing targets. Weeding out functional and the fuzzing targets that are no longer needed in the specs.
* Added couple of block state transition to our fuzzers.
* The good news is all the block state transitions are now included in the beacon fuzz.
* also added two epoch state transition functions, they are up and running. Looking at process, process rewards and penalties and that kind of things.
* We've been working on integrating other implementations as well. We reached out to couple of you folks. As a reminder, currently beacon fuzz works fully supports PySpec, zrnt, and Lighthouse.
* We reached out to Prysm. The process is not very straight forward, but we will get there at the end. Prysm is now integrated but we are facing issues.
* we are facing name space clashes, reached out to Proto, who is providing bunch of options that we can explore.
* Reached out to Nimbus as well. Trying to see how we could prosthetic C-library that we can simply link to our differential fuzzers.
* We started integrating Trinity, which should be very straight forward.
* We started working on Prysm thinking that having zrnt up and running will be trivial, but turned out quite the opposite. It is not as simple as expected.

**Next steps:**
 * finalize all the epoch state transition, should be done next week
 * will also bump all the current fuzzers to the latest version of the spec
 * continue to integrate trinity
 * hoping to have Prysm, Trinity and Nimbus up and running on the Beacon fuzz by the next update.

**Danny**: Thanks, any other testing updates?
I know there is a desire and even a need for **fork choice tests**, that's been on a back runner for us for a while and we need to prioritize it. I'll try to get some notes for review up on that within the next week.
The good thing is some of these corner cases and things we've integrated into the spec recently are those, and not expected to be seen especially on those test nests and even primarily not even seen on mainnet.


 ## 2. Client Updates

 ### Prysm

**Terence**:

*  Relaunched testnet with v0.9 last week. There has been lot of public interest.
*  55 peers right now , only 10 are of ours
*  with that comes a lot of questions, support and great feedback on the community
*  We've been improving upon those feedback and testnet stability
*  lot of bug fixes on RPC back-end
* On the side, working on aggregator, because previously every validator aggregate and then broadcast the attestation. So,we are switching to these aggregators.
*  making SSD performance improvement
*  ramping the Eth1 data implementation logic
*  resume finishing fully end to end test from depositing a deposit contract, submitting the deposit transaction and finalizing epoch.

**Danny**: Thank you Terence!
The current testnet does not use aggregation, is that what you said?

**Terence**: It does aggregation but right now every validator is an aggregator.

**Danny**: Okay. Have you put the configuration of the testnet into the test repo with any notes about it?

**Terence**: Not yet, it should be the same as minimum config. with an exception.

**Danny**: Okay. When you get chance, just drop in there. Just us getting in the habit of documenting these nets. so that we can begin to small experimentation, will be good.

**Terence**: Sure.

### Lighthouse

**Paul**

* v 0.9.1 merged, pretty good.
* working on a hot/cold database
* implemented validator on-boarding flow
* we have a test not running running in the cloud with  orchestration and monitoring. We're just not quite ready to push it to the public yet because we want to change the documentation and aim to get hot/col database in there before we make it public. Just so we're not filling up people's machine.
* working on refactoring the validator clients. We're putting in some new slashing protection stuff
* doing aggregation in the validator clients. It should make it your beacon node to handle large numbers.
* Working with Herumi on fast BLS implementation, but will still maintain our owns. Herumi is fast and extremly impressive.
* On the networking side, we've stated working on noise handshaking on P2P. We've added sybil resistance to the DHT
* focusing on testing efforts to test all networks components which is not trivial.

**FJL**: for Adrian - how did you add sybil resistance to the DHT?

**Adrain**: On the disc v 5, there was a few suggestions, essentially we limit IP addresses in /24 subnets.  In a particular bucket, I think we only allow two /24 subnet on the entire /24 subnet. In entire DHT limit the number of IPs on a /24 subnet.

**FJL**: Oh okay, thank you.

**Danny**: Thank you Paul.

### Loadstar

**Marin**

* we implemented Carls apes in JavaScript and we are currently testing it across the environments and we'll release it soon.
* made huge progress in disc v 5 in  JavaScript and
* our 0.9 spec is pretty much done. We're just waiting on the next release of JS Lib P2P

### Nimbus

**Mamy**

* weekly testnet setup in place. We reboot the testnet set up every Tuesday morning and it's stable for a week
* We've a separate developer branch and we merge everything on Monday. You can use that as a stable branch in comparison to Nimbus.
* spec- now compatible with 0.9.1 and waiting for 0.9.2 and verified that we've the same Genesis as 0.9.1 and so that would be deployed on the testnet next Tuesday
* complex sync issue being debug,
* working on data logs. Going through all the logs are quite stressing for set up and even for us
* crypto and BLS - I did some benchmark on the new BLS on the Raspberry pi, it was 21 ms for pairing.

**Next to do**
* working with Sigma Prime on Beacon fuzz
* on networking front on disc v 5

Side note on Eth1 - At Nimbus Eth 1, we finished Istanbul hardfork implementation.

**Danny**: Are those testnet that you're rebooting is something that public can join?

**Mamy**: Yes, that's the idea.

**Danny**: 0.9.1, are you all using the aggregation strategy specified?

**Mamy**: No, we don't have the aggregation strategy yet.
One mor thing, while we pass the minimal test, we still have some issue with version.


**Danny**: Thank you!

### Parity

**Wei**

* doing some optimization work for the Beacon chain state transition implementation
* the current purpose is to try to revive the Substrate runtime, which was previously removed.
* goal is to helpfully, to first make a breach and build using a Substrate runtime module.


**Danny**: Great, thank you!

### Trinity

**Alex**

* working on spec update and performance
* ver 0.9.0 and 0.9.1 updates are mostly altogether
* some refactoring we have to do on the fork choice that's blocking being fully up-to-date there. We're passing all of the fixture the spec test that
* updates to pilot Pylibp2p stability
* we merged in our Eth 1 monitor
* some great performance work on PySSZ, which had been bottleneck for us
* will start work on attestation and aggregation.

**Danny**: Cool, thanks Alex!

### Artemis

**Joseph**

* split in 2 teams -
    (a) **Advanced Research** which combining with Harmony and would be working on the Shard clients
    (b) **Artemis production readiness** team are making changes and implementing sync right now. Shahan will give update on that.

**Shahan**
* finished 0.9.0
* finalizing the naive aggregation stuff the will take a look at 0.9.1 right after
* done all the request response methods done to at least basic functionality
* we are finalizing a review  
* starting a round of interop testing with other clients
* starting to investigate block sync approach, specially Prysmatic
* also working on disc v 5 focused on the interop side of that

**Danny**: Great, thanks!
Meredith, I saw your question in the chat on it is a function of the size of the validator  that I don't know if that is explicitly written down anywhere, but we can.
This is **Weak subjectivity period** and it's dynamic. Foe many use cases of the weak subjectivity period, we would instead just rely upon some sort of upper bound rather than using even if it drops lower for the safety and health of network. It's just much simpler to err on the side of conservative on it but I will drop some more notes on that after this call.

**Meridth**: Awesome, thanks.

### Harmony

**Mikhail**

* There is a little progress being done on the gossip sub simulation. This simulator now being able to handle 100,000 of nodes and disseminate a message within there in the same amount of time.
* Further steps are to add the mesh topology and add metrics like bandwidth and so forth to this piece of software
* next we did a partial update of all the spec of 0.9.0 and this is within our work on the fork choice tests. we are about to finish this fork choice test for our code base
*  We probably can use our code to generate some basic test vectors.
*  also there is a work near to be finished with disc v 5. It's now been testing with the Geth .
* Some reach interop stuff, Dimitri is working on. It's going to be finished this week.
* I also made a write-up about the special condition detection. It's compiled from the ideas that previously been posted by Proto and Danny and some other stuff that  also contains some estimation of sizes, so the indexes could be useful for those who are designing this part of the client. I'll post it tomorrow.
* next couple of week will be productive

**Danny**: Great, thanks!

 ## 3. Research Updates


**Vitalik**:

*  **On protocol side** phase 1, we've done some edits phase 1 spec. Proto has been doing some work on kind of plugging into all of the testing machinery.
* Not too many changes, fairly small tweaks
* One thing that we talked about is blocks containing multiple chunks vs the ability to have created multiple blocks
* The idea is to just collapse the two dimensional array into one. That is simpler in some ways but it's also more complex and less  efficient  in other ways.
* I feel like there might be an opportunity to conceptually simplify things quite a bit otherwise the main thing that could be added on is one fraud proofs  and the other group of incorrect groups of custody bits which aren't too difficult because it's only a single round game. But there's still wants of economic insight and incentive nuances there to think about.
* I've been getting the feeling from the conversations with other people in these two groups that make people believe more and more that data availability of proofs actually or something important and are not just a kind of optional extras to throw on and to throw on at some point.People are actually afraid of the possibility that committees will break them. May be the skin break can cause the entire chain to finalize something invalid.
* Phase 1 has been designed from the start with phase 2 and or with the data availability proofs in mind. The main reason why blocks have multiple chunks instead of one root is so that it'd makes it easier to and if combined all of those pieces together into a single big root. But then after that there's the question of what specific date availability scheme do we use? The two realistic alternatives either
* something fraud proof based or
* something STARK based

There was a version of something fraud proof based that I coded up like almost a year ago and it would need to be updated.

The STARK based one is protocol wise conceptually simpler except there's this one kind of  very self-contained much more complex piece which is actually proving and verifying the STARK. But the main challenge there is we need to just make sure we have a decent Stark friendly hash function.

*  On the **hash function side**, there's also one other nuance which is basically, do we go with a binary field based hash or prime field hash and if we go with a binary field-based hash then there's no problems but on the other hand and STARK people have been mostly focusing on prime field rather than buying a binary field. So we risk being left out of infrastructure.
*  On the **prime field base side**, the challenge is basically that the 256 sides of a chunk. It doesn't perfectly match up with any particular prime modulus. The one trick I came up with, to try to alleviate that is that blocks would basically come with a tag that just says like what number you should offset everything by.  If you do that with high probabilities you will be able to  always find the tag that works. The high probability the first tag you randomly choose will be a tag that works. So the idea there would be just kind of rotate every week so that none of the waves fall into the tiny small range that's not covered by whatever prime, slightly blow to little futures. So,  that would needs to be kind of put into SSZ in some form.

**Next steps**:

* prototype this STARK based stuff and see how viable it is in bps sense.
* Otherwise there is this option of just figuring out how to swats things.

Those are the protocol level things from my side. My own time, I've been spending on some application layer questions.

**Danny**: Thank you Vitalik!
Those STARK friendly hash functions have not yet been vetted by the community of cryptographers.

**Vitalik**: This is basically the entire reason why use. However, STARK friendly hash function and our grant of STARK where and all of these other kind of things that have been in motion for over a year exist and they've provided some where, I know candidates that we can use with medium confidence right now. In general, there is a desire to be conservative and wait until those functions get properly vetted.

**Chat question**: Any news from the IETF forum on BLS standardization?

**Carl**:

**Hash-to-curve** idea was [presented](https://youtu.be/dMFgaeRdsfU?t=1009) at IETF meeting, yesterday. It was mostly update or for those people explaining the changes that have gone in the last meetings, then some questions around where to go from here. All looks very good, no one raised any issue which was precondition on making this a blockchain standard.

In terms of the hash to curve, the next thing happening is the proof of concept which is to be the master for most implementation that's being used to generate the test vectors which were removed, making sure all the canonical implementation of hash to curve are good. It should happen in the next two week or so. It will be moved to last call from the status on the an IETF standpoint. It would be submitted for input on the cryptography.  

**Danny**: How long is the last call?

**Carl**: That is much longer, in my view, it is six months or something.

With the reservation that nothing being said we haven't had proper discussions about this since the IETF meeting. We don't have a formal written agreement surface is a standard. I'm reasonably happy to declare those to be the BLS standards going forward and don't really expect anything to change there.

I think for most cases it's fair to say that BLS thing is not really holding us back. Only after next internal meeting which is happening in two weeks from now. For now basically think of it as a standard.

**Danny**: Great! Is there a PR up for review in spec repo?

**Carl**: There is a PR for review. I think it looks pretty good it needs some of the definition, RFC specifications I am not sure weather we want to take those off and then again in pseudo code or Python in the spec or not. But what is there, is good.  I'm going to squash all the EIPs and hopefully get those merge in.

**Danny**: Those EIPs are the Peter evasion standards?

**Carl**: Yes.

**Danny**: Cool, thank you very much. Any other research update?


**Justin Drake**: I've few updates -

**Relevant for phase 0**.

* The EF is looking for someone to manage the validators  that we're going to run. We are looking for someone with Dev Ops skill, operational skills, security skills to help set up the high uptime, high security set up, potentially multi-client, multi-cloud. Essentially, been using the threshold BLS signature and provide all this infrastructure as open source.  Potentially being complimentary to institutional, great infrastructure that Coinbase might provide. If you know anyone who might fit the bill, please send me a message.

**FJL**: We actually have a Dev Ops team, right?

**Justin Drake**: Yes, we could use the DevOps team, if they have a strong bandwidth and if appropriate, we can also look outside, its not mutually exclusive.

**Relevant for phase 1**

Spending time on zero knowledge proof.  one of the cool things that Dan Boneh came up with a  really neat, a secretly election mechanism and he wrote a paper and his paper got accepted, so it will be published very soon. It turns out that the circuit is very simple. You could do it either with ZK proof or fault proof. It is very similar to data availability situation. Of course if we can do it with zk proof, it's cleaner and it turns out in this specific instance, its potentially very doable.


**Relevant to Phase 2**

Getting more details on STARK friendly. There's been one of the candidate hash function in the competition that was broken the GMC.There's two of more experimental ones that remain rescued and facade on. The committee that reviewed this, still think that it will take years for these hash functions to be very far away vetted and for us to have very high confidence.

One of the hash function available is The Pederson hash which is provably secure under trust assumptions. It would be worthwhile looking at the performance in the plain text because it is significantly slower.

**Vitalik**: Another alternative to hashing backstops by the way it is going to bring back template multi hashing. At least for shard block they would provide both regular hash root and MMC hash root or whatever hash function we have. then you would have a fraud proof to show that one doesn't actually lead to the other. That way we can benefit from the data availability checking, conditional on that hash working and we also have the hash chains backed by whatever we have.

**Justin**: Right, I am not totally convinced that this is necessarily strict security upgrade. I guess, we can have this discussion offline.

**Vitalik**: What is the argument?

**Justin**: I think he is saying that if the hash function is broken, then you can trick the light client.

**Vitalik**: You won't be able to trick light clients because light clients would  ask for branches that go through the roots to go through the traditional hash. If the hash function is broken the only thing you'd be able to do what I think is get away with I'm unavailable data and if you get the committee to sign off on it.

**Justin**: If the committee is compromised  then it's hash function is compromised.

**Vitalik**: Yeah.

**Danny**: lets keep moving.

**Will**:
* Starting [Eth2.0 community call](https://github.com/ethereum/eth2.0-pm/issues/103)  Dec 03, 2019 - Issue in PM repo
* recently released an [update](https://medium.com/@william.j.villanueva/ethereum-2-0-phase-2-progress-7673b57eabff) on everything up until this point. So you guys are all interested in progress what's been going on definitely recommend you read through the article.
*  We had an implementation this this last week between Runtime API so this is the sandboxing API for calling new WASM runtime and those functions support this and run them in a protective manner.
* So now we're smart contract execution environment and we'll go ahead and get some basic smart contracts running for that we've been expecting scouts to test across multiple Shards.
* we're continuing to optimize token EEs and update token EEs implementations that are going on in parallel.
* Also working on some of the accumulator implementations more performance as well.


**Mamy**: What language do you use for the smart contract?
**Will**: Smart contracts that will be called will be in WASAM. Is that what you're talking about?

**Mamy**: It's because we also we've a POC in WASM to write smart contract. We are looking for new targets like what VM we can use it for, if we can use it for Ethereum 2.
**Will**: That'll be cool will play with that. I think for the most part the contacts will write, will be put together an assembly script and Rust. Those what we are playing with initially and then having compiled that in WASM.

**Mamy**: If we can find the contract, the original one in assembly script, we can just replicate it in name, see that we generate something executable that is almost the same. This way it would be like Vyper in terms of interface that we can use for Phase 2 for testing.

**Will**: Awesome! Lets do that. I'll share with you as we get this working and then we should try to write one as well.

**Mamy**: Cool!

**Danny**: Thanks, Will! Other research update.

**Danny**: I want to announce, let's shall be aware of there are some new **domain specific calls**. I think the particular cadence of these calls is still TBD. Likely, once a month to start but depending on progress and things might swap to be quicker.

There's Eth1.x, there is **research call**, they are primarily organizing on Eth research forum. It is to push forward some of the research on the existing chain with a focus on getting one improving theorem today and also staging Ethereum for future upgrade of moving Ethereum to Eth 2, more towards stateless model and other things. So check that out. Like I said, they are organizing a lot on Eth research forum.

In addition to that we are going to start at least monthly **networking call** where a member or two from each team I hope that as been focused primarily on networking, we're going to get together to enumerate the problem more explicitly and work on driving that effort a little bit to sleep. I'm going to lead that call to start but certainly I'm open to not leading that call depending upon who steps up and is available.

I will drop an agenda item on Eth 2 PM repo, an issue that we'll set up this call. It might be next week, if not it will certainly be the following.

Any questions or thought on that particular item? Don't want to introduce an incredible amount of coordination overhead for adding all these calls. They are experiments and if they are valuable, will continue doing.


**Danny**: One more call **[Light Client task force](https://github.com/ChainSafe/lodestar/issues/555)**. Another call coming up, first week December, Wednesday.

As Eth 2 progresses, these two covers an increasingly large domain. Hopefully these domain specific calls, we can rally the effort.


 ## 4. Networking

 **FJL**: No much updates.
* One thing that might be of interest to the historic team that we just Just converted Geth code base to use Go-modules. I am looking to include Disc v 5 code on Geth master branch asap. I think that's going to be a big help to anyone using Go.
* Not directly related to Eth2 but might be interesting to Eth 2 in future. Since the Istanbul HF is coming up in the Eth 1 chain. Everyone is upgrading their nodes which means that all of a sudden have a lot more  capable Eth 1 nodes around.  And we want to leverage that by running a DHT crawler that collects all of these. We've this infrastructure to base your break so you can actually set up. Then we will have something to announce there right after the fork process. I think this is going to be a pretty good test run of DNS infrastructure. I think it's probably going to be really nice for Eth 2  as well once it launches.

**Danny**: On Disc v 5, I know there was talk about integration of proof of work or looking into other techniques for adding some resistance. Is there any update?

**FJL**: No, I haven't received any update, any feedback on the spec in the last two week.
* happy to hear, its being implementing
* it seems like working without my involvement but would be nice to have more involvement
* at the same time, there are research challenges left for this protocol and I will be happy to have get more help on that.
* happy to have calls about it

 **Danny**: Thank you, Felix. Networking experts, provide feedback and input and like I said, we've a networking call coming up and we more explicitly rally around some of these problems. other networking updates?

 On Harmony simulations, when you all are expecting to publish some results on that?

 **Mikhail**: I think the basic results should be published by the end of next week. We're just going to publish these basic simulator stuff, get feedback. Proto is willing to the creation simulation.

**Danny**: Cool!


 ## 5. Spec discussion

 **Danny**: Proto dropped [issues with and options for signing root](https://github.com/ethereum/eth2.0-specs/issues/1487), discussing pain points in disparity between hash tree root and signing root.

**Proto**:
*  signing root is kind of pain, outlined this in detail in the [issue](https://github.com/ethereum/eth2.0-specs/issues/1487). Collect more feedback on the proposal to remove signing roots. Alternatively there are other workaround but they aren't pretty and don't cover all issues.
*  With more feedback, I'll put together a PR describing the changes and by the next call, I'll like to make a decision as a group of implementers.

**Raul**: Signing root can be a little bit confusing to someone not familiar. I agree that it's worth revisiting. There's a lot that can be done to explore alternatives. I like Proto's alternative of having a sign block container and regular block container.

**Mamy**: Actually there is something that we wanted to do in Nimbus.  one suspect stabilizes because  we have issues on the test suit. We need some kind of workaround on that. I guess having a sign type and something separate will be much easier.

**Mikhail , Shahan**: +1 for signed block container

**Proto**: There is something to n/w as well. There are considerations for how you deal with typing structure. Take a look and we will discuss more in next call.

**Danny**: other spec related item?


 ## 6. Testnet Discussion

 **Danny**: Status is similar to two weeks ago. Prime focus in most clients is getting a public version of the testnet out or joining other public testnets.

Some really good movement on that. Prysmatic relaunched testnet, couple of other clients really near to that. Nimbus doing their weekly builds.

It seems like there's still work to do before orchestrate a large scale multi-client public network. Are there any other thoughts, comments, discussion, questions about this?



 ## 7. Open Discussion/Closing Remarks

**Mikhail**: I have a question about weak subjectivity period. It's period size comes from Casper FFG paper. I am wondering if we are tightly coupled with the size calculation that we've so far and does it prevent long range attacks only or if there are some other implications here?

**Vitalik** - **[weak subjectivity period](https://ethresear.ch/t/weak-subjectivity-under-the-exit-queue-model/5187)**, yes there are calculation. I made an Eth Research post about that. How long the week subjectivity period is based on the rate at which people can withdraw. The withdrawal period is maximum is 8 months in the worst case. In the normal case, the one who is withdrawing, get out after about two days. In the case, where there is small amount of Ether, the maximum also drops and of compromise and encourage more people to join in.

In terms of why that exists and based, one part of it is because it determines how often people needs to come online to get the security guarantee.

Another aspect is that are predetermined like basically if the weak subjectivity period gets two short that people who did that things might end up at not getting slashed. So both of those things put together.

**Danny**: Do you usually define the period as the time which it takes?

**Vitalik**: I think mathematically speaking it would have to be period that it takes for a third to exit.

**Mikhail**: Thanks Vitalik, I'll take a look at this. I was just wondering if we can cut it down by half for example and weather it just breaks the long-range attacks or breaks something else?

**Vitalik**: to break what down By half the maximum or the amounts?

**Danny**: The effective weak subjectivity period is the period in which the network is actually policing, right? Which could be up to the maximum theoretical or below.

**Vitalik**: I guess the maximum withdrawal period is theoretically 8 months but that would only happen if literally everyone tries to exit at the same time. Then the amount that you would need to log on once every eight months that divided by 3. Eight month is the worse case.

**Mikhail**: Okay cool!

**Danny**: Other questions regarding this for just anything?
Okay I know y'all are all pretty heads down working on these things.  I think we're also entering into a period where it's very important to Communicate with community. I started doing those quick update but updates on individual teams on how to better understand your clients, involve the testnets are  always extremely appreciated by the community, so don't forget to write. Thank you. keep your eyes peeled on the Eth 2.0 pm repo. Thank you everyone !!

 # Date for Next Meeting: December 05, 2019 at 1400 UTC

 ## Attendees

* Alex Stokes (Lighthouse/Sigma Prime)
* Adrian Manning
* Ben Edgington (PegaSys)
* Cayman
* Carl Beekhuizen
* Cem Ozer
* Chih-Cheng Liang
* Daniel Ellison (Consensys)
* Danny Ryan (EF/Research)
* FJL
* Hsiao-Wei Wang
* Jacek Sieka
* JosephC
* Justin Drake
* Kevin Mai-Hsuan Chia
* Mamy
* Marin Petrunic
* Martin Lundfall
* Mbaxter
* Mehdi | Sigma Prime
* Mikerah Quintyne-Collins
* Mikhail Kalinin
* Nicholas (Hsiu-Ping) Lin
* Nicolas Liochon
* Nishant Das
* Paul Hauner
* Protolambda
* Pooja Ranjan
* Raul Jordan
* Sam
* Shahan K.
* Steven Schroeder
* Terence Tsao (Prysmatic Labs)
* Tomasz Stanczak
* Trent (Whiteblock)
* Vitalik B.
* Wei Tang
* William Shatswell Villanueva


 ## Links discussed in call:

*  https://github.com/ethereum/eth2.0-pm/issues/101
* Presentation: https://youtu.be/dMFgaeRdsfU?t=1009
* Slides: https://datatracker.ietf.org/meeting/106/materials/slides-106-cfrg-update-on-draft-irtf-cfrg-hash-to-curve
*  https://github.com/ethereum/eth2.0-pm/issues/103
*  https://medium.com/@william.j.villanueva/ethereum-2-0-phase-2-progress-7673b57eabff
*  https://github.com/ChainSafe/lodestar/issues/555
*  https://github.com/ethereum/eth2.0-specs/issues/1487 
*  https://ethresear.ch/t/weak-subjectivity-under-the-exit-queue-model/5187
