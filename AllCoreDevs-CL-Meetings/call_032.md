# Eth2.0 Call 32 Agenda

### Meeting Date/Time: Thursday 23 January 2020 at 14:00 UTC
### Meeting Duration: 1.5 hours scheduled, 1 hour actual
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/123)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=kt59-FEeWTI)
### Moderator: Daniel Ellison
### Notes: Jim Bennett

----

## AGENDA

## 1. [Testing and Release Updates](https://youtu.be/kt59-FEeWTI?t=178)

**Daniel Ellison**
As you know if you've been trying to work on 0.10.0, we had some issues with the BLS session writers. We didn't update them to the new APIs, and there was a failed SSZ generic test which messed up the session writers due to some import issue. There is a PR up for this. The BLS tests are being stripped down to just those of the APIs that we're using. There were a few bugs in the 0.10.0 release. We're going to release a minor bump to 0.10.1 has these bug fixes and session writers. Essentially, it's V 0 10 Um, with a couple of bug fixes - very small, not substantive stuff. That will be released by the end of tomorrow. Sorry about that. But thank you for everyone helping me get it out the door.

Proto is not here, but Proto's been doing a bunch of work getting the repo updated to 3.8. and also integrating his remercurable(?), which greatly, greatly speeds up the Pi spec. I'll let I'll let him share the members if he joins us. Very, very fast to the extent that we can start doing a little bit more interesting tests and things with Pi spec. In addition to that, been working on integrating those structurings into what's going on with Phase One stuff and phase one, at least as it stands today, will finally be gotten out of that PR into Dev. None of that will affect most of you too much except for that release.

Any other testing and release updates?

**Mehdi:Sigma Prime**

I've got a [beacon-fuzz update](https://youtu.be/kt59-FEeWTI?t=343).  Since our last update on this call, we published [a comprehensive blog post detailing our approach and current challenges with beacon-fuzz](https://blog.sigmaprime.io/beacon-fuzz-01.html).  We've confirmed that the crash identified on Nimbus is indeed a bug. We've just identified yesterday another issue the affects a slashing function and the voluntary exit function. We've opened a new issue and submitted a PR for a fix, and it was approved a couple of hours ago. It's always exciting to see beacon-fuzz finding more issues out there.

We've revamped the way we're building fuzzers. We make the build process lot more maintainable. We've deployed a few more fuzzers on Fuzzit, and we're still exploring ways to fix the namespace clash we have been dealing with. The blog post explains in detail all the possible options. We should hopefully have this resolved by next Monday. Alternatively, we might have to deploy fuzzers with production clients only.

We're currently looking at integrating the Java clients, which should be done by the next update. We will be reaching out to the Harmony Artemis team over the next couple of days.

We've identified a moderate difference in the block head processing function on Nimbus. It actually turned out to be related to the fact that BLS signature verification was enabled for Nimbus and disabled for the other implementations. So we've therefore submitted a PR to introduce a compile-time flag to keep BLS signature verification in Nimbus. We'll have a new blog post detailing out progress either at the end of next week are beginning the following week. And as soon as a couple of clients are upgraded to the latest version of the spec, we'll be updating the fuzzers accordingly. That's it for beacon-fuzz.

**Daniel Ellison**             
Awesome. That's all great. So, presumably, those two crash-inducing errors highlight paths that we're not testing in the Pi spec tests. So I'll circle back with you and see if we can add some tests to Pi spec.

**Mehdi:Sigma Prime**              
Yes, Sounds good. We have both the beacon state and the actual block objects that trigger these crashes, so it should be easy to add them to your your testing suite.

**Terence**                         
Is there any update to the [forgeries?] spec test?

**Daniel Ellison**              
Great question. There are now two independent, uh, formats floating around - one that Paul has been working on, and one that members of the Harmony team have been working on, neither of which are integrated into Pi spec, but both of which can be used to begin to work on conformance. I've had trouble Proto and I have had trouble prioritizing that in the light of just making sure that the current spec and things are ready to go for you all, so I will circle back on that today.

**Terence**                 
No problem. We actually have Paul's testing framework implemented.

**Daniel Ellison**  
If you do integrate tests that are generated off of Lighthouse. I'd love to know if you're in conformance.

**Jacek Sieka**
I just want to go back to fuzzing for a second. I'm curious how we should approach states which would not result from normal work processing - random data in the state object. That's one way an invalid validator index might happen, right? Something in the state is already wrong, but nothing in the state should ever be wrong because all the [blocks?] we applied to it limit the space of possible states.

**Mehdi:Sigma Prime**
Yeah, that makes sense. That something we had to deal with in Lighthouse as well. I think our general recommendation would be to propagate these errors the right way and checking for these assertions and not crashing when they happen, allowing your client to recover from that, which should not be too complicated. So we almost have a PR to fix that particular bug on Nimbus. The [trading?] bug is already fixed. But you're right - some of these bugs are triggered from what someone could consider invalid beacon states.

**Jacek Sieka**
When certain beacon states are invalid, is there really nothing better you can do than exit? Any stations and blocks that you produce will be weird.

**Mehdi:Sigma Prime**
Did you guys have a chance to investigate that particular input on your end?

**Jacek Sieka**
No. But we've had we've had something similar where basically we ended up rejecting all the validators, and then when you tried to find that later index you get an empty committee. There are places in this back where empty committees are not checked for.

I think that's that's kind of realistic-ish. You have really bad luck with - no, I shouldn't get that much bad luck with the something, but if you have very few validators, some of the committees might be empty and some might go on, so technically there's a chance that the chain could recover, but it's not very meaningful because there are so few validators. We've had to fix cases like that.

**Mehdi:Sigma Prime**
Yep. That makes sense. I would say generally if we can make sure that the clients can recover from these cases, I would strongly recommend implementing those fixes. Again, for Nimbus for that particular test case, I think the fix is relatively simple. Definitely for Trinity, the invalid index is caused by a [malformed?] basically a block. That's not the problem with the state itself. It's a block processing issue.

**Daniel Ellison**               
Yeah, I'd at least angle towards not crashing. And if you are in some weird state knowing it, and then going from there.

**Mehdi:Sigma Prime**  
Matt's almost got a PR for you guys. We're just not sure whether we should give you some time to investigate internally. But we can circle back and have a chat on the fuzzing channel.

**Jacek Sieka**
Yeah, let's do that. I think the best thing you can do in that case is basically dump the state and start over because somehow you got to that state and you wanna probably log some diagnostic information or whatever, but, you can't really continue to meaningfully work, right?

**Mamy**               
It's basically in programming language a question of error vs. exceptions. Should you crash now to avoid further corruption? Or should you hand over to the caller who's supposed to know better about the context?

**Mehdi:Sigma Prime**             
Yeah, it's almost a philosophy question in software engineering, right? Anyone who you ask, people tend to adopt an approach as opposed to another. I'm personally inclined to propagate the error and let the caller handle it in a hopefully safer way.

## 2. [Client Updates](https://youtu.be/kt59-FEeWTI?t=963)
Great. Client Updates. Let's go with Artemus.

**Ben Edgington**        
Right, that'll be me. We merged 0.9.4 into Master earlier this week. We've also made all the changes for 0.10.0 as well, including all the BLS changes. We would pass the reference tests if the tests were correct. We won't be merging this just yet. We're going to wait until there are some joint multi-client testnets at that level before we do that. We're hoping to join some of the existing testnets with 0.9.4 in the meanwhile.

We're continuing to implement the Eth1 data changes for 0.10.0, and we are debugging and improving discovery and sync all the time, We've also started putting some serious effort into optimization. We've sort of put it off until now, but that's properly underway. Expecting good performance improvements, low hanging fruit there.

And finally, you may have picked this up elsewhere, but we are officially changing the name. Unfortunately, NASA stole the name Artemis after their latest space programs. That's not really the reason. We have a trademark clash, unfortunately, so in future, Artemus will be known as Teku, alongside Besu, which is our Ethereum 1 client faces - Besu and Teku. At some point, we'll get around to renaming the repo and all the rest. But it's not top priority just now. That's all from us.

**Daniel Ellison**  
Long live Teku! Thanks, Ben. Lodestar?

**Cayman**          
Hey, y'all. Um, so in the past few weeks, we've merged in our initial 0.9.2 branch, and we're working through the 0.9.3. We are working on integrating our new SSZ library into lodestar, working through a few bugs and getting it up to passing all the spec tests. And we've recently got a new team member - Frankie. She'll be helping us out, and we're getting her onboarded right now. I believe that's the major highlights.

**Daniel Ellison**  
That SSZ library has some major gains, right?

**Cayman**                  
Oh, yeah, kind of underplaying that there, but yeah, the SSZ library, we've been working on it for a month or so now. It has a lot of gains across the board. So serialization, deserialization is roughly five times faster than before. It also lets us operate on immutable Merkle trees as SSZ objects and that and when we're doing that, hash re-routing is a lot faster because we have the tree there.

And we're planning on swapping out our beacon state object with a Merkle tree-backed object. And there's a certain spec PR where they've updated the Pi spec to do something similar to this, there have been really significant gains. We're planning on doing the same thing, basically. So for a preview, you guys can look at that PR, but we're planning on going in the same direction.

**Jacek Sieka**           
Is this Typescript or Wasm?

**Cayman**                
It's Typescript. We have a very experimental Wasm-based Merkle tree. But right now, the gains are so big that we don't we don't really need to go there.

**Daniel Ellison**                 
You know, the gains are on the order of 1000 X for many operations, right?

**Cayman**                   
Yeah. 1000 X, and then so when you when you have such a fast hash tree root, we can do something like 4000 hash tree roots of a beacon state per second. So when you when you have such a fast hash tree root, you can use that as the key of some kind of cache. You can basically cache a lot of these different state transition functions, even if they're naive. You cache them by the hash tree root of whatever piece of the state you're dealing on memo-ization is what you call it. You can memo-ize these different functions. Just that is enough to speed up the state transition by a lot.

Basically, for us, it's like, where right now, we're just not fast enough for mainnet to being pretty competitive for mainnet. So we're working on actually benchmarking and getting real numbers for that. So then, instead of saying "a lot," I can tell you exactly how much faster and what exactly that looks like.

**Mamy**               
Is the website simple serialized.com the with new actions?

**Cayman**              
No, it's not. So right now, I'm not passing all the spec tests, and I want to do a little polishing. So it'll probably be a week or so before I can get into that.

**Jacek Sieka**            
At some point, we had the state transition function in Wasm. It would be cool to compare it to the website.

**Cayman**               
Yeah, I'd love to see that.

**Daniel Ellison**                  
Great. Thanks, Cayman. Nethermind?

**Sly Gryphon**           
So I've been working on peer-to-peer using the Rust library for a quick solution for that. With some help from Johnny Rhea, we've got a .net example working on OSX. Slow going up on Linux and it's gonna be for Windows, and then integrate in with our main application. But because it's the same library, once it's integrated, it should just talk to the other implementations. That'll all be in the coming weeks.

**Daniel Ellison**              
Good. Trinity?

**Alex Stoke**              
A bug chunk of work has been updating our client to 0.9.3. We've landed most of that moving ahead to 0.10. We have a couple of big PRs to migrate pilot p2p to Trio, which is a Python library. That should help a lot with stability in terms of the currency of our networking layer. We have another PR for the validator clients to pull that out, and then some work on our beacon-noded PIs to support that. Probably our most exciting thing this week, Janek has been working on our Discv5 five implementation. So he's doing experiments connecting in Lighthouse, so that's pretty cool. And, yeah, that's those were the main things working towards public testnets.

**Daniel Ellison**              
Thanks, Alex. And the next three, I think you all have some version of a public testnet. I'm curious, along with your update, about the biggest hurdle, if there is one, that you're currently facing with those testnets. Let's start with Prysmatic.

**Raul Jordan Prysmatic**                
We've been running our mainnet testnet for two weeks. We're not really seeing significant issues. We have 29,000 active validators, 32,000 total. At the moment, we've been just working through rapid iteration with users on a lot of improvements to the user experience, fixing up memory and CPU conception, which is currently the biggest problem. A lot of it has to do with copying state fields due to a lack of immutability and go, so that eats up memory at an alarming rate. And also, of course, the biggest bottleneck ends up being some parts of hash tree root. So there's multiple efforts working on this to resolve.

One of the biggest optimizations that we did was offloading expensive computations. That's done many, many times to background workers that cache it. So if we have 1000 validators on one node and one validator requests some piece of data, there's a worker in the background that kind of delegates and returns that to any other future validators that may request it.

The other biggest bottleneck was fork(?) choice, but Terrence worked with Proto and Paul to get that implementation fixed and now we're basically seeing it disappear. We're working on a lot of unit testing coverage, and we added some interesting stuff, like a slashing protection to validator client.

Aside from that, we have this slasher architecture that is listening to attestations and things happening in the testnet and essentially will track slashing offenses and submit that to the beacon node. We're still working on wrapping up at that aspect of the slasher. I would say the biggest issue right now is just fixing up resource consumption of the beacon node at the moment.

**Daniel Ellison**   
Gotcha. So computation seems to be the bottleneck?

**Raul Jordan Prysmatic**                 
Yeah. So we fixed memory, so now at this point, it's just really CPU. There's so much stuff going on in the life cycle of a single slot.

**Daniel Ellison**                  
Right. Gotcha. Given an estimation on the amount of nodes on the network.

**Raul Jordan Prysmatic**
Yeah. So on average, nodes have around 80 to 100 peers. There's a new website that came out recently called [Eth2stats.io](eth2stats.io) created by Alethio where people can register their nodes. We only run on the order of seven or so. We know the community runs a lot more than that. So you can which ones people have registered on there. But, you know, aside from that, we haven't done a recent topology mapping.

**Daniel Ellison**
So given peer counts accounts more than 50?

**Raul Jordan Prysmatic**        
Yes, I think that's that's accurate.

**Daniel Ellison**               
Okay. All right. Great. Thanks, Raul. Lighthouse?

**Mehdi:Sigma Prime**               
That'll be me again. So we've been adopting for [proto array? unclear - please review](https://youtu.be/kt59-FEeWTI?t=1717) We're in the final stages of testing and running on several testnet nodes. We're seeing some great improvements there. We still need to investigate one error we've been seeing. Paul's on it. He's a big fan of the [proto array?] approach and definitely recommends it to the other teams. He's gained an appreciation for the nuances in the [fork choice roll? unclear - please review](https://youtu.be/kt59-FEeWTI?t=1740) and we're super keen to see some cross client testing in the hopefully very near future.

We're in the process of updating to 0.10.0. Our BLS implementation has been updated in the last couple of days. We're now working to pass a [test vectors? unclear - please review](https://youtu.be/kt59-FEeWTI?t=1757). A rough ETA for first working version would be late next week. We're adding HTTP API validator client to allow for the management of validators.

We're currently dealing with some locks that occurred during heavy API usage while the node is syncing. We found that we were essentially jamming our scheduler with long running block tasks which was causing chaos, so we've implemented a work around for now until we can swap over to the [unclear - please review](https://youtu.be/kt59-FEeWTI?t=1797) We've identified a fork choice bug that's actually allowed us to discover new bugs and new issues in our syncing logic. We've been addressing all reported bugs from the previous testnet and patching Lighthouse as new ones are discovered.

We built a new, dedicated thread for block processing that takes the load out of other Lighthouse processes, which was causing some unexpected issues with timeouts. We've added some more robust syncing logic to handle malicious [unclear - please review](https://youtu.be/kt59-FEeWTI?t=1828) We're now testing our syncing with some custom adversarial peers on the testnet. It's going pretty smoothly so far.

We're continuing to make progress in what we call our [DO.2? unclear - please review](https://youtu.be/kt59-FEeWTI?t=1840), which will introduce a significant network upgrade with the introduction of sharded subnets.

We're seeing a lot more community engagement in Lighthouse, which is great. We've been taking lots of feedback and implementing lots of small UX fixes. We're also seeing significant interest in our validator client UI proposals. You guys might have seen the RFP that we pushed out a few weeks ago. We're still processing the responses. The deadline to respond is the end of next week - the 31st of January, to be precise - and we'll be announcing the winning vendor shortly after. We're also making great progress on the hiring front. We're looking to hire 1 to 2 more Rust developers. Late applications are still accepted, but time's definitely running out. We're looking at moving fairly quickly on this.

And finally, we're also looking for people to help on a contracting basis with some develops work, primarily sorry around deploying and maintaining testnets. We're looking to deploy testnets with hundreds of nodes, especially thousands, most probably using AWS. So please reach out to Paul via this call or Twitter if you're interested, or if you know someone who's interested.

That's it for Lighthouse.

**Daniel Ellison**              
Biggest hurdle in those testnets?

**Mehdi:Sigma Prime**              
I think we definitely had a lot of issues when dealing with fork choice. So the work that Paul has been doing lately in these last couple of weeks outside with Proto has been quite instrumental in fixing those bugs. But apart from that, testnet's been running fine. We took some validators offline, which resulted in some skipped slots, which highlighted some bugs which we haven't actually seen before in our syncing. So that was quite interesting. But everything's going quite smoothly on the testnet front. Still about 16,000 validators. Looking hopefully at upgrading to the 0.10  perhaps late next week.

**Daniel Ellison**                 
Give an estimation on the number of nodes on that network right now.

**Mehdi:Sigma Prime**             
I think we're about 40. Don't quote me on thisI'll have to check my dashboard. Yeah. We've got about 20 peers connected.

**Daniel Ellison**                 
Yeah, I see 20 peers. I guess that implies it was somewhere in that range, if not more. Thanks.

I ask because we're all keen to see testnets with more validators, but at this point, even more keen to see testnets with more nodes. I think the 20-to-100 range is still slightly in the toy range of the amount of nodes we expect to see on mainnet. You know, somewhere on the order of 1,000, 10,000 if we're in the same range as the current Ethereum network. And so I think there's gonna be some interesting stuff that falls out from gossip and discovering things that we're not yet seeing.

**Mehdi:Sigma Prime**               
Our testnet is still semi-public. I haven't really communicated around the relaunch testnets.

**Daniel Ellison**  
I blogged about it last week. Thanks, Mehdi. Nimbus?

**Mamy**                
In Nimbus, we have the specs 0.10 implemented except crypto. The crypto BLS part should land by Monday. It's implemented using Milagro. We passed the content [test vectors? unclear - please review](https://youtu.be/kt59-FEeWTI?t=2087) On Ethereum 1, we started to implement something called EVMC, which is an API to be able to switch between Geth, Aleth as a C++ implementation on Nimbus. This is a work in progress.

We are looking into how to reuse an Ethereum 1 code for Ethereum 2 phase 2. We [forgot?] to testnet. Now we can use mixed libP2P or Go-libP2P daemon with Nimbus. I will hand over to Zahary after the other updates to explain the hurdles about a number of nodes. Otherwise, most of the team will be in Brussels for FOSDEM between February 1st on February 7th. So if you want to chat or meet us physically, you are welcome to reach out to us. We will be holding a kind off Interop-like event on a particular clone of other clients testnets and repos - Prism and Lighthouse, so we can test with everyone physically there so we can connect to both clients. We also had some weekend projects from one committee member, and he managed to build Nimbus on Android and run it on the phone.  We also know of something called [End by Gen?] that can generates bindings to Rust libraries so you can easily use Rust libraries with a name.

Now I will hand over to Zahary to explain what we have on the testnets.

**Zahary Karadjov**             
On the testnets front, we've been trying to balance between implementing needed new features, such as Discovery5, station aggregation, and so on, and the long-lasting effort of making the testnet more stable.

In Discovery5, we've merged the latest code and we've tried to integrate with [unclear- please reveiw](https://youtu.be/kt59-FEeWTI?t=2254). On the stability front, we've seen, for a few weeks already, various issues that arise in longer running testnets. For example, where nodes are restarted or joined the network later, we've seen various issues with the data structures. The database maintained by the node and the algorithms that initialize the data structures at what we call block pool and station pool. Basically, we're seeing that sometimes when the nodes are restarted, their data structures are not initialized properly and the node starts misbehaving. On the number of nodes, we haven't been advertising our network, but it's running on 10 different servers with two nodes per server. So we kept twenty nodes online at all times.

**Daniel Ellison**            
Thanks, Zahary. Sorry. Okay. I think that was everyone. Great.

Proto did join us. Proto, do you have anything to add? I went over a little bit - the fact we're bumping Python 38 and that the Eth phase 1 stuff is going to be in dev soon. Anything else on your end?

**protolambda**                
You represent it pretty well, and Cayman explains the SSZ changes as well. So having binary tree backs as a CD library, or at least using this technique for some parts of the states, it's really effective, especially if you use this to come up with the keys for your memorization of the states. So usability think all gets to be a lot easier to install and play around. All this ends in dev pretty soon.

**Daniel Ellison**                
Right?  That's something I forgot. The ability to HIP install the spec repo is going to be there and much more easy than it currently is. Thanks, Proto.

## 3. [Research Updates](https://youtu.be/kt59-FEeWTI?t=2422)

**Dankrad**   
On my end, one of things I'm currently looking into is whether we should changed their proof of custody to 256-bit blocks, which seems probably like a more elegant options with more performance, and I'm looking into whether that's doable in the MPC.

The other thing I'm currently looking at is data availability, where we just got a team to implement the binary [unclear - please review](https://youtu.be/kt59-FEeWTI?t=2480) and hopefully get some good performance numbers from that to make some decisions - for example, what the binary field size should be. Also, whether we can do that in a slot or if the block producer can immediately do all the data availability stuff, or if we have to outsource that to some sort of super nodes to provide the data availability proofs.

**Daniel Ellison**              
Gotcha. Thanks, Dankrad. I mentioned before ongoing work on the phase one specs - I'm really hoping to see something relatively clean and stable in the next couple of weeks. I want to give a couple of teams something to dig into on that some protoypes, but we're not quite there yet.

TX/RX?

**Joseph Delong**                
Hey, how's it going? So over the past few weeks, we've been working on a couple of different projects. So Mikhail has been working on this E22 bridge. And I have some notes from him about what he thinks about that if anyone's interested - reviewing the proposals and documentation that's out there right now.

Alex has been working on some decentralized time sync. I have been working on [crush r?] transactions, mainly reviewing literature and working on this Python tester for it. And then I think that's pretty much over.

Anton and Dimitri have been working on Discovery v5 testing. I think that's it for now.

**Jonny Rhea**                  
I'll jump in and say that I'm working with, um Is Johnny, by the way? I'm working with Mac Garnett on EE tooling. We basically kind of spec-ed out a plan for a truffle or an EE kind of test framework, and he's working on an initial implementation of a transaction EE, and I created like a cargo plug-in for Rust to regenerate the framework of an EE, but I'll let Mac talk more about this.

**Daniel Ellison**                 
Thanks, guys. Other research updates?

**Sam**               
Sam from Quilt. Some stuff we've been working on since last call. We hosted a Phase 2 call and discuss the Phase 1 to Phase 2 transition plan and a general phase zero to phase  1 transition plan. There's also a write-up we released to support that. Ansgar and I released a state provider write-up that goes over some of the details of push-and-pull models to block proposers. We have a road map for our simulation. It's formalized, and we're moving forward on it. We're figuring out how to attach that and simulate different state provider models.

I've been working on a small write-up that makes the case for investigating dynamic [?] access. I'll be posting that soon, so hopefully you'll be interested in reading that. We've been going through scenarios on our [crush r?] framework for managing Eth and EE balances. And I think that's pretty much everything we've been working on at Quilt. Let me know if I missed anything.

**Daniel Ellison**               
Thanks him. Other research updates before I move on?

As you're likely aware, the runtime verification audit and verification of the deposit contract bytecode has been published and is up for review. If you or anyone from your team has the technical expertise to dig in and take a look at the formal specs and provide any input, feedback, and review, please do - now's the time before this thing goes to production. I'm always here to get some more eyes on it. That's it for research updates. Thank you.

## 4. [Networking](https://youtu.be/kt59-FEeWTI?t=2807)

**Daniel Ellison**
So we do have a networking call in about six days, the core of which we will address any practical items related to the sync current specs, issues we're seeing, and then move on to more research-y items if we have time.

There's also this PR up for adding a response code. It looks like there's a lot of active discussion. I didn't have time review this morning, but if it's still up for debate on Wednesday, we'll hash it out there.

As I said, I'm very eager to see some load tests, load tests and number of validators, obviously, but more so in number of nodes. So if you do any kind of that work, talk to me. Otherwise, we can talk about it more on Wednesday.

Other networking related I did related items worth bringing up today?

**Jacek Sieka**              
I think we might announce that [unclear - please review](https://youtu.be/kt59-FEeWTI?t=2885)

**Daniel Ellison**
Yes, thank you, Jacek. And y'all have done some rudimentary work there? There's some initial work on the noise integration?

**Jacek Sieka**               
No, not really. We looked at the problem, but no, just fooling around.

**Mehdi:Sigma Prime**
Yeah, same on our end. I think Adrian's been looking at it, but we haven't gotten around to actually starting implementation.

**Daniel Ellison**                
Gotcha. And I think one of the reasons it was selected is that there's wide language support for the base protocols, but once somebody implements that, I'd be curious about the complexity of the integration actually using it.

Okay, we'll talk about that more Wednesday. Other networking related items?

**protolambda**            
Yes. So although I've been busy with lots of other things, if looks for other things there? Um, the [??] station aggregation technique is getting improved. So I want to do some careful improvements. So not directly if it's like this new aggregations strategy that completely changes things. Instead, I think we can at least get a lower upper bounds on the cost of local aggregation while still being gossip-sub compatible. And so this basically means we can change how we track what othet peers know and what you decide to drop. And doing this, you can decide to drop messages as already part of aggregates that are known by your peers. And so you can try to reduce messages that way. They'll still be able to propagate these aggregates, so you don't have full local aggregation anymore. You can propagate these aggregates that all fit nicely in the subtree. So, you know, orders that follow the same strategy will be able to merge them.

**Daniel Ellison**                
Cool. Thanks. Maybe you can tell us a bit more about it on Wednesday or if you have some time, to write up the basics of your thoughts, that would be good to see.

## 5. [Spec Discussion](https://youtu.be/kt59-FEeWTI?t=3062)

**Daniel Ellison**   
I know there's a new version in dropped very recently. There's some missing tests come up in this that they'd like to discuss.

Herman shared 1578, which was an issue posted by Justin for dual key voluntary exits which allowed either the hot key or the cold key for the voluntary exit. I think the main pushback on that is that the cold key in the long run key probably won't be a key, but instead, it's a code or a pointer to a medium or message rather than a key. I suppose the counter to that is just use it as it is today, and then add something more sophisticated in the future, but it's hard to know, depending on what the structure turns into, whether we can add that more sophisticated feature in the future.  

Specifically, it's worth highlighting the use case here - the use case likely being a custodial staking service. I have the cold key. I do not have the signing key. And the staker starts doing something wrong. If they do something slashable, they'll be kicked out, but maybe, for instance, they go off line, they go totally dark, I can't talk to them. Rather than reaching the ejection balance, I could instead, if they were offline for two days or something like that, just initiate an exit myself. It's a valid use case.

Other thoughts on this? I need to think a little bit more on the implications of the future.

**Herman Junge**                
Now, the thing is, we have the assurance that the pre-sign message is effective always. We don't need to do a major modification to the protocol - just do as Vitalik suggested.

**Daniel Ellison**                  
Right, So you can do that, right? The custodial staker could give you a signed voluntary exit that was for, say, your activation. Which is fine - you can hold that. There are some strange cases in which someone, maybe an adversary who makes some fork of the chain, could take some of these messages and make you exit early in this fork, and so there are subtle risks there that are not that detrimental. Likely in most cases, I need to think about it a little bit more, but that's probably a reasonable approach. I forgot that that was suggested there.

If I or anyone else thinks of some deeper issue with that method, then we'll share, but we'll leave the issue open for another couple of days for any more conversation. Thanks, Herman.

**Mamy**               
Not really spec discussion, but as a general comment, I've implemented the hash to curve spec as a new one for 0.10, and the crypto speck is quite nice because it's blending high level goals and the design rationales and the implementation, so you have both the implementation, which is what we have, and also why we are doing things like this. And I know that we had some feedback about the spec being kind of obscure on the intent. That's just a comment on the crypto spec.

**Daniel Ellison**                 
An implicit comments about the terseness of the spec.

**Ben Edgington**              
It may be a good time to reveal my secret weekend project to put together an annotated spec. I'm working on that with Rationale and digging through Github for all the reasons why we did all that stuff, because this has been a pain point for a long time. So that is something I'm just doing as a personal project. But there may be other efforts underway. I will publish the first fruits of that in two or three weeks.

**Daniel Ellison**                 
Great. And we're continuing to update this phase zero for humans, which is not totally complete in all the things that a spec probably needs, but using it for helping people get on board with audits and things. Maybe some combination of these multiple paths will get us where we want to be.

A good number of people will be in Denver. Maybe we'll add a channel to the discord for that number of people will be in Stanford right after.

**Joseph Delong**     
Danny, we're gonna do a workshop right after - the day after on February 22nd.

**Daniel Ellison**            
Great. Do y'all have a lot of resources around that or an invite out that we should be looking for?

**Joseph Delong**                 
Yeah, sure. I dropped it in the chat, but I'll drop it in again.

**Jacek Sieka**                 
A couple of us will be at the EthCC in Paris as well.

**Daniel Ellison**                            
Absolutely. I will not be in Paris, but some people might seem certainly will be. And I know others will be, so organize away. I'm excited to hear about y'all's individual Interop effort to mess with some multi-client testnets. Maybe when others get together at some of these events, that might be a good target as well.

**Mehdi Sigma Prime**              
Yeah, I'll be in Paris as well if we need to catch up.

**protolambda**         
Okay, maybe also just create the channel for Paris as well, then? To coordinate things?

**Daniel Ellison**              
Yeah, let's add those three channels to the discord. Just that people can easily communicate at least meet up for dinner when they're there.

**Mehdi Sigma Prime**               
I saw somewhere that there's going to be an Eth2 client summit? Is that confirmed?

**Daniel Ellison**               
I haven't heard this. If there's gonna be enough of us there, I will be there and I will do something.

**Mehdi Sigma Prime**      
I'll be there as well. I'm pretty sure I saw this somewhere on Twitter. but I may have just dreamt it. It's getting late here.

**Daniel Ellison**                
If you come across the source, let me know, because I'll collaborate with them.

**protolamda**            
So shout-out to [???} She has been pushing for Eth to be on a bigger stage at different hackathons and conferences. So I think she's organizing, at least educational parts, like the part where we can answer questions to people who go to the conference.  

**Daniel Ellison**              
 believe that we will have one of these in two weeks. I'll have to look. I'm gonna be on a plane that day at the exact time of this call. So we'll schedule around that or someone else will run the call. I'll let you know. Um, Well, that Jonah's Thanks, everyone. Good work. Talk to a lot of y'all of the networking call.

# Attendees

* Daniel Ellison (Host)
* Sly Gryphon
* Alex Stokes
* Alex Vlasov
* Ansgar Dietrichs
* Ben Edgington
* Carl Beekhuizen
* Cayman
* Cem
* Chih-Cheng Liang
* Dankrad
* Herman Junge
* Hsiao-Wei Wang
* Jacek Sieka
* Jannik Luhn
* Jim Bennett
* Jonny Rhea
* Joseph Delong
* JosephC
* kevin.mh.chia
* Mamy
* Mehdi Sigma Prime
* Nicolas Liochon
* Nishant Das
* protolambda
* Raul Jordan Prysmatic
* Sam
* Svante Jorgensen
* Terence
* Tomasz Stanczak
* trentonvanepps
* Zahary Karadjov

# Date for Next Meeting: 6th February 2020, at 1400 UTC.
