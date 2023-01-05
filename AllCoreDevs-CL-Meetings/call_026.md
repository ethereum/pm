# Ethereum 2.0 Implementers Call 26 Notes

### Meeting Date/Time: Thursday October 24, 2019 at [14:00 GMT](http://www.timebie.com/std/gmt.php?q=14)
### Meeting Duration: 1:15 min
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/89)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=DXGeC7cg71Y)
### Moderator: Danny Ryan
### Scribe: Brett Robertson & Benjamin Edgington

---

## Agenda

- [1. Testing and Release Updates](#1-testing-and-release-updates)
- [2. Client Updates](#2-client-updates)
- [3. Research Updates](#3-research-updates)
- [4. Network](#4-network)
- [5. Spec Discussion](#5-spec-discussion)
- [6. Open Discussion/Closing Remarks](#6-open-discussionclosing-remarks)


## 1. [Testing Updates and Release](https://youtu.be/DXGeC7cg71Y?t=346)

**Danny:**
It's been over a month since we had this call.

I released [v0.8.4](https://github.com/ethereum/eth2.0-specs/releases/tag/v0.8.4) today, it has been a long time coming. It is primarily some testing updates based off of some of the consensus issues that we found at InterOp, along with the networking updates that were also primarily driven at InterOp.
It includes chunking, listed responses for better streaming or for enabling streaming and modifying some of the message structures to better facilitate the sync.

We are staging an upcoming semi-major release. There are a number of PRs that are under review. So these things are stuff that has come out of audits for example hardening of the fork choice rule against some of the test attack vectors found by Rhea, but also some other stuff which are some substantive changes to [Phase 0](https://github.com/ethereum/eth2.0-specs/pull/1428) with respect to removing the crosslink scaffolding such that we can continue development while we iron out the actual direction will take on Phase 1.

Protolambda has an announcement.

**Protolambda:**

I shared this diagram on [Twitter](https://twitter.com/protolambda/status/1187320137092714496?s=20) about infrastructure because programs just before DevCon during DevCon and the conference just at Taipei after was too busy to launch. But not that the things are calming down and then it onboard clients on this testing infrastructure and do this performance testing of all the clients in parallel. And then in the next like week or two, I'll reach out to clients and ask them to help with the setup scripts for the official state transitions.

**Danny:**

Proto has been very actively working on this since InterOp and I'm excited about this as we move towards merged testnets.

Next up is a update from Mehdi on fuzzing.

**Mehdi:**

So as you all probably this is a follow on from the work started by Guido.
So, we now have it working for block processing,  block header processing, attestation processing and chopping.
So is all working on the latest version of the spec v0.8.3.

**Danny:** There were zero substantive changes to the state transition or some of the core stuff in v0.8.4 so you should be good to go.

**Mehdi:**

We have modified the block fuzz target last week to allow clients to essentially go to beacon state from the file. So we now have a pre-processing function that uses a stake ID reference and which actually passes the relevant state to the all the first targets. So this was a re-architecture of the way we handle the Corpus for both of the beacon state and the block.

So, so far we have guaranteed pi-spec and lighthouse on these fuzzers. Pi-spec is very slow. So we're probably going to want to remove it when deploying to production the fuzzing infrastructure.

We are also tweaking the fuzzer to ensure consistency of behavior across different implementations when returning empty bytes as opposed to an initialized pointers.

We're also working on adding epoch state transitions. So currently looking at process justification finalization, process cross links, process final updates and so on. So this should be fairly straight forward since these functions will only take a beacon state as an input.

We're also exploring creating facilitators - these are also mostly seen as lead parcel plugins to enable structware mutation based fuzzers. So this would help greatly with the coverage. And is another alternative that we could also potentially use is leveraged libprotobuf-mutator also known as LPM. It would essentially help us translate a decoded assisted object into a protobuf and back.

So first to make an informed decision, we needed accurate coverage measurement. So we decided to focus on that. That's something that we're currently working on.

So while we're doing this, this would essentially allows generate and mutate beacon states rather than sticking with known value States.

We're also adding support for more beacon state inputs by essentially adding post state into the list of known valid states that we should lead fuzzer into the input corpora. And finally we started reaching out to some of you guys to onboard additional implementations. So we're looking at onboarding Nim which we should in the very near future, this week on next and then we'll move on to Go, Java and Javascript.

## 2. [Client Updates](https://youtu.be/DXGeC7cg71Y?t=730)

### Lighthouse

**Paul Hauner:**

So we've been working with Felix to get a standard disk C5 spec without topic going. He's updated the rust code to a new spec and he's tests across compatibility with the reference go code. Ed's talking to prysm about how to test out discoveries and they've also updated to the latest go code. And Huan is working on a basic implementation of topics which is not yet merged.

From my side, I've been working on F1 linking. Mostly that. I've create a couple spec issues for some unspecified behavior when making F1 votes if things are going wrong.

Also raised and interesting attack this morning about how you can basically attain majority after 2 epochs after genesis.

Also, working to build Genesis off prysms deposit contract. I am pretty close, but still not quite there, probably tomorrow or tonight.

Scott is working on slashing protection for the validity client with a nice scheme.

Current found some solid optimizations in the rust BLS library and at the same time we're also building some basic rust bindings for Harumi to see if it's worth us switching over to.

What might affect some people trying to do InterOp is that we are going to change the way that you run Lighthouse. So we're going to present a validity client in the beacon node as separate binaries. We're going to move among the one binary code Lighthouse. So it's going to feel a lot more like parity with their subcommands. That's it from me.

### Artemis

**Joseph Delong:**

So we have made some BLS signature provements Ben has been working on that. The  noise jvm implementation is complete now. We're working on our Handel’s implementation of Handel for our client. Mostly doing code clean up and handing off to our project team were working to merge with Harmony. That's just kind of like going through HR stuff for that and we're implementing some benchmarks if we make changes to like block rusting or epoch rusting we can tell right away if there's been any kind of change in the speed of that.

**Ben Edgington:** The BLS stuff I've been working on specifically is implementing the new hash to curve standard is more or less complete so I am more or less happy issues with performance. If any teams want to take a look at it in Java, then it's on Artemis GitHub as a draft or requesting a moment. So feel free to take a look an entry back.

### Harmony

**Mikhail Kalinin:**

We’re figuring out our merging Artermis which both teams are excited about this is one of the are excited about. This is one of the priorities at the moment. We are also continuing to work on fork choice tests. It's going to be tests for our implementation of our fork choice spec. And actually it's almost done. I guess we'll be finished next week and I probably would be a good start to make some test vectors and share them with the community and have whole tests shared on the repository as well as tests as we have for the state transition part. Also we are now finished our discovery for discv5 implementation. It's already done. But now I'm working on tests discovery change. Our current goal is to get interop with the Geth implementation after that it will require some perfector. But yeah, it's It's almost done and but it doesn't contain a topic of discover part yet. Antoine is working on some GVM rapidity for our Ops and I think they are about to release a new version.

### Prysmatic

**Terence:**

Yeah, so we are just working on hardening of our testnet and finding a few bugs along the way and fixing the bugs. We also have an experimental PR working on removing a shard across our code base. I'm a big fan of such a change and also creating a test for that and try it out in the runtime. We have also started implementing the simple aggregation strategy as well. And yeah, we are another fan of that change because we think is going to help with syncing with regards to the station log. And we are also getting a Herumi BLS library to test the spec tests and then it's even faster than the previous BLS libraries we mentioned a few weeks ago. A couple of minor things were are working on equalising the new asset key library. We also implemented the process epoch optimization, which was which was inspired by the lighthouse talk during DevCon. We started working on end to end testing and then putting into our first testing strategies.

### Lodestar

**Cayman:**

We brought onto a new team member, Tuyen, and he's been contributing and finally brought him on more officially. We have a lot of small things in progress. Where the name of the game is optimization. So we're optimizing our state transition logic, refactoring, pulling it out into a separate package. We are finishing up our discv5 implementation. We are trying to fix up our networking to comply with the new the new release the spec like as of today, but you were working on before. And working on adding kind of a general caching mechanism that we can use across the board catching recent States and things like that. And in the coming weeks, we'll just be kind of trying to finish those things out and get to a kind of a stable place so we can start participating in a testnet.

### Nimbus

**Zahary:**

Then this

Before I start I will mention that Mamy has created an organization on this GitHub call Ethereum 2 clients and the idea of this organization is that would be a suitable place to store the scripts for that we developed during interop to run testnets between the multiple clients and then it would also help other useful projects such as low-level gossip subchat so we can test the libP2P implementation for conformance. So all the teams should have received an invite for this for being admins and once you are in you can add more people from your team.

So moving onto updates… We've been working on Eth 1 integration. We are pretty much wrapping this up and we are looking forward to participating in a shared testnet with a contract deployed on Gorlie. Right now we are happy implemented the latest spec 0.8.4 but I guess the consensus here will be that the cross-links simplification will be included in this shared testnet. I'll be expecting feedback from everyone. Otherwise, we'll be now so adding a lot of metrics two Nimbus and we plan to have a public refined instance once the testnet is running and we'll be running probably like 80 or 100 nodes on a server cluster and will be exposing the matrix from that. There has been significant progress in our native libP2P implementation. We are still using the daemon but we've made the first steps towards integrating the native one so it will be possible in the near future to switch between the two implementation in Nimbus. Jacek wanted to share that the ncoi tool, that he has developed during the interop, is now much more refined it and it's already sitting in the Master branch. So if anyone is curious to use it you can find it there. We've also developed fuzzing framework which allows us to use IFL, american fuzzer and lib fuzzer with programs developed in Nim. And now we are just testing the waters, but the initial focus will be on the lower level layers components such as cryptography, SSZ serialization and so on. It will be gradually moving on to the high level components. We hope to integrate without sigma prime and sigma prime differential fuzzer soon. And finally we had to spend some time integrating and switching to Nim 1.0, which was released just a few weeks ago. And actually we had to switch to the very latest version which was released yesterday. So mean was so we assume compatible with Nim 1.2 and that's it.

### Trinity

**Hsiao-Wei Wang:**

So after DevCon we have been working on making our libP2P implementation more complete and Alex has a PR about making the default protocols be set in the py P2P side and it's being merged. We also fixed the current Beacon chain syncer in Trinity. And for the python synchronized module migration, the Trinity team has been planning to migrate for a while and then we'll try to implement in 3.0 in our new modules. And while this might be the each one monitor, so it would be a new process or new components in the Trinity side query the info from the Eth 1 chain data so that we can build and listen to the Eth 1 Chain and also for the votes and also for the passive data. And as a python client we are still have the known performance issues, so Jannick has been reworking the Py SSZ data storage and the py P2P is of course is also in our radar recently.

### Parity

**Wei Tang:**

I'm fixing our two remaining issues of interop and hopefully to try to connect with some of the current other client testsnets and will also try to fix those issues in testing. I'm trying to fix some of the issues with the Casper engine it turns out there are some design issues. So I'm trying to fix that as well.

## 3. [Research Updates](https://youtu.be/DXGeC7cg71Y?t=1687)

**Danny:**

There has been a lot of discussion around the Phase 1 proposal. Vitalik discussed this at length and various workshops at DevCon and on the Blog Posts online. Essentially, it makes the trade-off to have fewer shards at least the start but the ability to cross-link in the best case every shard, every slot facilitate simple slot time inter-shard communications. I don't think we need to go super in-depth into its day. The primary primary application is that it changes some of the Phase 0 machinery that we had in place for cross-links. In retrospect obviously, we were prematurely putting that in the spec.So I have a Phase 0 spec update PR that just removes cross-links altogether from Phase 0. Funny enough cross-links and the updating of cross links and the calculation of reward cross-links was one of our biggest source of consensus errors at interop so would be nice to just remove it anyway. There is a PR up for review and it's been under review for about a week and I think we're very close merging it in 0.9. When we get to the testnet discussion we can discuss the implications on testnets which version we should be testing etc.

**Vitalik:**

I've been thinking about Phase 1 spec issues and how to optimize beacon blocks more, how to calculate the data availability roots and a couple of other things. I have a couple of open issues out but generally nothing especially hard has come out yet. Like a lot of it is basically just like problems about how do we pack bytes together. Otherwise, yeah, I don't see any super fundamental problems. Maybe the more fundamental problem, well, not even fundamental but just difficulty is there more Phase 2 related ones like how to actually do like how to actually do  guaranteed across shard movement of Eth between shards for example. Basically, there's challenges there that have to do with do we want to force every shard to communicate to every other shard with P2P in every single block. Do we want to have that as like more of a second level process and so on and so forth, but that's kind of still thinking. I guess right now, I'm still trying to come up with simplification and modifications for the existing Phase 1 design and still kind of have my eyes and ears open for any potential challenges that we haven't thought about yet. I'm expecting other people to come in with their own opinions about like how particular things to be architected eventually.

**Justin Drake:**

One update which is relevant to Phase 0 is BLS signatures. So on the standardization I'd say we're in a very good place. The spec really hasn't changed for the last several months with the exception, which is of note, of a very minor kind of security bug which should be very easy fix, like a one-line change. Riad Wahby who is one of the authors of the Wahby-Boneh hash function that we are using is doing an amazing job terms of taking ownership of the standardisation efforts. Lots of polishing. He's also addressed various patents or possible patent infringements and suggested workarounds for those. Between the 16th and the 22nd of November, there's going to be a CFRG meeting with diverse people involved in the standardization. And at that point, I guess the spec can be considered frozen.

Another update on the BLS stuff is there's this Library called [Herumi](https://github.com/herumi/bls) and it's offered and maintained by Shigeo Mutsinari who came to to DevCon and met some of the present guys and it turns out that this Library seems to be significantly faster than and other libraries like Milagro, the dizzy cache library. A recent benchmark from the Lighthouse Depot suggest that it's 2.4x faster than Milagro. So we're in touch with the author and we're considering a possible grant. One of the complaints that we have had in the past is that the integration with various languages has been not so easy. So working on simplifying the integration for Rust and Java and maybe even other languages will be a priority. He also thinks he can make the library even faster. So right now his pairings take 0.6 of a second, but he thinks he can shave off and 10-20%. It will also be good, for him to implement a really fast version of the Wahby-Boneh hash function. And you know, there's also the possibility of doing formal verification on this specific library being floated around.

One piece of good news is that Guido has come back. So he had to do a bunch of other stuff and now he's he's available again. And so he's actually currently working on fuzzy testing the Herumi library.

And final update on the BLS stuff the has been a very interesting [paper](https://eprint.iacr.org/2019/1177) recently by Mary Maller where she describes a technique to aggregate signatures in such a way that the aggregated signature is cheap to verify. So when you have n distinct messages regardless of m, you only have to pay two parents to verify the aggregated signature and kind of roughly two m exponentials so that may or may not be something that's relevant for Layer 1 but it's still very exciting and something to keep in mind for Layer 2 or for light clients. It is a very recent paper, so, I guess, we need we need a bit more time to digest it.  

In terms of quick updates for the deposit contract formal verification should end in maybe a couple weeks. So there's still one minor point regarding removing some of the safety checks and we should get the final okay on those within a couple weeks. There's also discussions about how we want to design the website to make the deposits so there is still significant work to be done before we want to deploy the deposit contract.

We want to do lots of testing to make sure that the UI is good and we also don't want to be in a situation where validators make deposits to early on and they have the funds in the deposit contract without being able to use them. So I guess there's also no significant rush to deploy, at least, until maybe we have some sort of public cross client testnet.

**Protolambda:**

SSZ is not really changing however, I am putting out some of the specs of the specs repository and drafting this new repository which covers SSZ in a more complete way and tries to implement Change Control process and it's the realization staging process. This should help standardize our shows and other experimental features going forwards. And I know since I've is working on light clients as well, and I hope to work with them, I'm trying to learn those news.

**Cayman:** Yeah, so Chainsafe is setting up a monthly light client call that the working group or a task force of sorts for light clients. The goal is to make sure that light clients don't get left behind and really I think is to coordinate bringing light client Tech from for Eth 1 and eventually Eth 2 into production. So we're going to be exploring like research and development updates, open questions and there's a lot of technical problems to work through but I think a lot of the issue is social and so having a regular meeting where we can kind of just all sync through the bigger issues and coordinate will be really helpful. And so we'll post on all the relevant channels the next few days, but then we have a solid agenda, but I think we're going to be targeting in two or three weeks for the first call. And we'll be collecting community feedback and all that.

**Danny:** I am supportive of pulling SSZ out into its own spec we have run into it a couple of times where altering SSZ spec in the context of the other spec it became more and more clear that it should be its own thing and that our own spec point to a specific version.

## 4. [Network](https://youtu.be/DXGeC7cg71Y?t=2575)

**Danny:**

I have a [PR](https://github.com/ethereum/eth2.0-specs/pull/1440) out for a Naive Attestation Aggregation proposal in which validators locally aggregate with no necessary sophisticated strategy on subnets before attestations are passed to shared more global network. The bones are in place but we need to flesh it out so if those who have been thinking of networking problems could please have a look at this PR and give me some feedback.


### Felix update

**fjl - Felix:**

We made some really good changes to the spec just this week so there is a lot more documentation about the topic in there. The Go and Rust implementations are now interoperable for the basic sort of EHT. I don’t know where the Python implementation is at right now. Too my knowledge Jannick is still working on the wire protocol. And since DevCon the Java team have been working on implementing the wire protocol into Java - I believe they are pretty far with it but I have yet to test it.

There are two open problems right now in the protocol. These need to be solved before we can think about freezing the spec. One problem is the topic radius. Estimation is not all that well defined in the spec right now and that is because we don’t have a solution for this. I expect we will find a solution to this problem when we implement it for the second time. We have a solution for the radius estimation but the quote is horrible and is actually not clear if this is a workable solution and I don’t want to document this in the spec. I do think there is a simple and good way to do topic radius estimation but we don’t really have it yet.

Another thing that came up during the audit which is almost complete. The audit was paused due to DevCon as I could not get any feedback on the initial report they created. I have however now given them the feedback and they should come back in the next few weeks with the final report and that will of course be published.

The biggest issue in the audit that LeastAuthority was trying to get through was that we should be adding some sort of Proof of Work system on node identities. It is something that I really did not want to do. I even put that in the [spec](https://github.com/ethereum/devp2p/pull/120).

The proof of work on node identities is a pretty old idea. I think by now we have two options for it. We could use equihash or cuckoo cycle. I have been playing around with cuckoo cycle and integrating it into the protocol in code. I am not super happy with this change to be honest. What I would really like to have is some more solid feedback from other people who are more knowledgeable about proof of work or just in general. We need to make a decision whether we want proof of work in this protocol or not. That is the big question, should we do this in the first place and if yes then which parameters should we use, etc. So if you have any ideas on this topic at all then please provide feedback to the PoW [issue]( https://github.com/ethereum/devp2p/issues/122).

**Jacek Sieka:**

On the proof of work topic I can briefly mention from Status’ side on of the biggest reasons we are abandoning whisper is that as a spam prevention mechanism it does not it does not quite work, simply because node power. The node doing the work honestly is almost always going to be underpowered and vulnerable to an attacker which makes it pretty much useless.

**fjl - Felix:**

So it is a bit different with this type of thing because the issue with the proof of work or discovery or more general as this is not only for discovery, is, do we want to our nodes to add proof of work on our identities? What this prevents is attackers choosing their node identity in an arbitrary way because a lot of things in discovery but more in general a lot of P2P algorithms rely just on having the node ID space uniformly distributed and attackers can actually influence the distribution by choosing their node IDs. So if you add proof of work then the attacker would have to perform PoW many, many times. Where as a node that does not care about it’s ID and just has a random ID would need to perform the Proof of Work one time. So it is a bit different from the Whisper system where you have to put PoW on every single message. So in that case you do have to spend a significant amount of mining resources just computing PoW all the time. Where as node IDs setup is a one time PoW - it runs the first time you start the node and then probably never again. I do think PoW is not that bad in that context. In terms of Node IDs it is something we really need to decide on and make a good decision about it.

**Mikhail Kalinin:** Do you have a list of scenarios for the interop process like you did with Rust?

**fjl - Felix:**

No, so basically what we did was we just ran the clients against each other and then H basically did all of the work which meant mainly checking in his code where things went wrong and that led to a couple of corrections to the spec, like a couple corrections on the go and so it was liek an interactive bugging more or less. So you could just run the implementation and send a ping message and then see if you can get a response. If you do get a response then you can see if you can encrypt it. But am pretty certain that both Rust and Go are now compliant with the spec so if you want to try either implementation and it works with yours then we are good basically.

### Whiteblock update

**Trenton van Epps:**

We have released our [repo](https://github.com/whiteblock/gossipsub-testing) for our testing methodologies for what we are doing for LibP2P. So we are laying out basically what we are going to do. The specific methods and just some metric that we hope to collect. Please join the [discussion](https://community.whiteblock.io/t/gossipsub-tests/17). We would love to have more people so if you have any thoughts or would like to see how we are doing things then please join us in the discussion.

**Antoine Toulme:**

We have some data already that we will be sharing.

Nimbus team would it be possible to get access to the organisation github and the script as well?

**Mamy:** Yes. Of course.

## 4. [Testnet Discussion](https://youtu.be/DXGeC7cg71Y?t=3229)

**Danny:**

There is a lot here especially around when the various testnets happen. One of the big things is the Phase 0 update and the pending v0.9 which will include this modification to the state transition function. It is almost entirely simplifying in that it is cutting a few things out and I think Terence has he said has gone through it. I did have some conversations with different teams and it seemed like in general consensus was to get these changes out of the spec, get them integrated into clients before we do some larger more orchestrated multiclient testnets. It also seems that whilst most teams have the Eth1 and Eth2 machinery that most teams were ironing out deposit contract following Eth1 data voting etc. and doing some more single client testnet stuff. Both larger private testnets and some teams were planning on spinning up some public testnets or semi-public testnets where most of the nodes were controlled by the client team. Although these testnets may be dominated by a single client they might do some multi-client testing. So there is still plenty of work to do with regards to single clients doing testing before moving forward to multi-client testnets while we get these Phase 0 changes integrated.

**Antoine Toulme:**

We would love to run some of that either as ourselves or in conjunction with any clients. We have an easy way to spin up a bunch of instances. What is the timeline? Do we want to use Goerli like Prysm does? Is there one deposit contract or multiple? Do we have an incerling on that?

**Greg Markou:**

I can get us lots of ETH for Goerli by the way.

**Justin Drake:**

In terms of getting ETH for the testnets. One suggestion is to make the deposit amounts 32 milli-ETH as opposed to 32 ETH and that would make it very easy to get ETH.

**Greg Markou:**

We have millions though because we are the faucet.

**Justin Drake:**

Excellent.

**Antoine Toulme:**

There were in the past some funny issues there like putting in different amounts that resulted in issues, there is enough finicky stuff in the client that can result in issues last time we ran this in June. So if we can just skip that. It is not that interesting to test the security functionality at this point as I feel it will just waste a little bit of time. If we can go straight to then I am good with that.

The Prysm contract - Terence should speak about that - has a clause in that where you can drain amounts back to the original sender. So it is not like you are losing ETH.

**Danny:**

To the question of it is one deposit contract or multiple. It is essentially one per testnet that is connected to an Eth1 chain.

There was also discussion about spinning up proof of authority testnets. I think that just connecting to Goerli is probably simpler than doing that. But it is definitely something that we could consider, especially when we move towards Public testnets or incentivized testnets so proof of authority testnets may work better because we can better allocate the ETH that can participate but that is a little bit further down the line.

**Zahary:**

One idea that I would like to share is, we are planning to do our testnets in the following way. We are going to just the validators from the mock start to kickstart the network immediately. And the very first block we will reference some current block on Goerli so the validator contract could be used to add additional validators when the network is already running - that is you don’t need to wait for everybody to leave a deposit to become a validator. We can probably publish some sort of common line parameters similar to the mock start. If the other clients are interested as well then I think this could simplify the initial cross client testing.

**Danny:**

Yes, that does sound like a good idea. If you can share your notes then we can put something together like the mock start for interop.

**Terence (Prysmatic):**

There are a few more things to discuss around the config. So for us we actually ended up increasing the injection balance just because we wanted to test when one of our validators gets ejected. And second thing we are seeing is there is that some people left the client running for too long or that people go offline for too long and then setting the threshold has half is a little too low and then it starts to hurt our finality. So that is one config that we had to change.

And the second config we had to change Eth1 follow distance. We set it from 1024 to 16 because we don’t want people to wait to long to be activated.

**Danny:**

Maybe it is worth modifying the minimal config to have in a couple of those changes or to add a new one just called minimal testnet or something? So that we can use the shared dev.

**Paiul Hauner:**

I think we should probably decide on how we are going to structure the fork for these testnets just so that we as we get closer to genesis we don’t have that situation where people use their testnet keys on mainnet and get slashed.

**Danny:**

So are you suggesting that we start with a fork version that is way out of the domain?

**Paiul Hauner:**

Yeah, it is probably very unlikely but it seemed like a good idea. So maybe we start on the right most bit for big indians and then the left most bit or something? And so get well out of the way of range of the forks we expect to use.

**Danny:**

Yeah, that is a good call.

I don’t think that value is in the config? I think we are just using the default value for Genesis?

**Paul Hauner:**  

I think so, we put it in our spec but I cannot remember if it is in the main spec of not.

**Danny:**

Yeah, I think it would be worth putting it in our config just to ensure we have it as a parameter.

**Antoine Toulme:**

There are a couple more things here. It is not really enough to just get the nodes going but we need to monitor and make sure everything is running ok. I know that Zahary mentioned that you can run for ref for testnet for the node that they run. For ourselves if we are given permission with respect to monitoring we that be enough or is there a specific tooling that we should develop to help monitor the testnets?

**Zahary:**

Our node setup is based on the Prometheus spec that was published.

**Antoine Toulme:**

Is that going to be enough or do we need to do a bit more?

**Danny:**

So that just allows you to monitor singular nodes Zahary is that correct or is that mulitple nodes to a single place?

**Antoine Toulme:**

No, you can do as many as you like.

**Zahary:**

We have some custom setup as we don’t want to expose this Prometheus for the internet so for our own environment we have a custom setup to gather and aggregate all the data in a single place.

**Antoine Toulme:**

I think this is simple enough for everyone to implement on their own.

**Danny:**

I think that is a good start. There is a push on Protocol Labs side, they are doing some more rigorous gossipsub and pubsub monitoring tools - I don’t know the timeline on that though.

**Jacek Sieka:**

In terms of general tooling one thing I would like to mention we are building a few monitoring applications, like a gossipsub sniffer and few of these things. I expect in time there will be a community that step up around block explorers and things like that. We will also have similar things but say on the web.

**Danny:**

There was some nascent interest many months ago on Block Explorers. I can knock on some doors and see that going again.

**Antoine Toulme:**

Yeah, that is what I mean.

I also know that Prysm had a good setup with Spinnaker cause they were able to do canary deployment testing and all that good stuff. So we spun up the spinnakers as well. We could organise around that as well. Is that something people would be interested in?

**Danny:**

What is a spinnaker?

**Antoine Toulme:**

Spinnaker is an SSZ pipeline integration that takes a new build, has a workflow for that build. For example you can test it in isolation in 3 or 6 nodes. Look at the stats, look at the results to see if it is good, to see if it passing the tests. It is also going to make it possible to replace the testnet nodes with the new version in an automatic failover manner without downtime.

If we had six nodes per client then spinnaker works for each of them, every time we push a new doc it would be picked up by them. Test in isolation making sure it is working, etc. Once you have the green light from programs it can transit into the testnet and then it automates the pipeline and it becomes much easier to manage it over time.

**Jacek Sieka:**

One of the concerns I would raise with these tools is that they are very centered on a very centralised approach to managing nodes and is good for cloud and software as a service. But that is not quite we are trying to do here.

**Antoine Toulme:**

Hang on, one it does not have to be the same testnet. Even if it is the same testnet it does not have to be the majority of the testnet. I could just be a client decides to do it that way. It should not be the end and all of the testnet. If you happen to be using the same contract and you are running independently you should not be at all penalised or have to interact with spinnaker at all. It may just be a way clients do choose to deploy and run their nodes. Make sense?

**Jacek Sieka:**

So long as we are aware that not all clients will use these systems. We should have that use can in mind as well.

**Antoine Toulme:**

I think you need both. I think if you want to painless approach to deploy things automatically to get updates by email then this works as it is much easier to have a continuous deployment from the perspective where you can test things all the time, you can also do crazy experiments and see if your experimental PR is working as you thought or if it is breaking the network.

By the way I am not inventing anything it is just what Prysm is using today.

**Terence (Prysmatic):**

I think for us it is just about creating the testnet quality. We don’t want PRs going in and breaking the testnet. So our workflow is more like when our PR is linked to master and then a new image is cut so then the image deploys to the cluster then we will direct 10% of the traffic to that image. Then we have 3 hours of measuring report to compare the baseline between the new image and the old image and then we will do some analysis. And then if that passes we can direct more and more traffic to that new image.

**Danny:**

So this is primarily on testnets where you control the majority of the nodes? Is that correct?

**Terence (Prysmatic):**

For us - yes.

Can we talk about aggregation strategy for multi-client testnets? I think for each individual client testnet it does not matter as each client can use their own strategy but for multi-client testnet would people be interested to implement the naive aggregation strategy mentioned in the [PR](https://github.com/ethereum/eth2.0-specs/pull/1440)?

**Danny:**

Once we have any significant load on the testnet we are going to need an aggregation strategy. If you have a single channel where everything is gossiped you don’t strictly need an explicit strategy other than aggregate locally and include in blocks. But I think the intent is to get some version of this naive strategy integrated. And when multi-client testnets come around I think we should move towards that.

And I think any of the components used should be in line with mainnet as soon as possible. This includes aggregation strategies, Secio vs Noise, etc.

So we need to get that PR merged soon and tested and onto these testnets. To that end I am seeking feedback and input to that PR.

### 5. [Spec Discussion](https://youtu.be/DXGeC7cg71Y?t=4478)

**Danny:** There is the Phase 0 changes, which will help facilitate this new Phase 1 proposal. Any questions on that or spec in general?

Great.

### 6. [Open Discussion and Closing Comments](https://youtu.be/DXGeC7cg71Y?t=4519)

None.

## Attendees:

- Alex Stokes
- Antoine Toulme
- Ben Edgington
- Brent Allsop
- Carl
- Cayman
- Chih-Cheong Lia
- Danno Ferrin
- Danny Ryan
- Dankrad
- Greg Markou
- Felix
- Hsiao-Wei Wang
- Jacek Sieka
- Jannik Luhn
- Jim Bennett
- John Adler
- Jonny Rhea
- Joseph Delong
- Justin Drake
- Kevin Mai-Hsua
- Leo BSC
- Luke Anderson
- Mamy
- Marin Petrunic
- Mehdi (Sigma Prime)
- Mikhail Kalinin
- Musab
- Nicholas Lin
- Nicolas Liochon
- Paul Hauner
- Protolambda
- Samuel Wilson
- Shahan Khatch
- Terence (Prysmatic)
- Tomasz Stanczak
- Trent Van Epps
- Vitalik Buterin
- Wei Tang
- Zahary
