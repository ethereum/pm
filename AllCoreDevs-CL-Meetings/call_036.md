#  Eth2.0 Call #36
##  Meeting Date/Time: Thursday 26 March at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/135)
### [Audio/Video of the meeting](https://www.youtube.com/watch?v=Vn1oHH55yPk)
### Moderator: Danny Ryan
### Notes: Brent Allsop, Jim Bennett

----

## ACTION ITEMS
* Get the PRs mentioned in yesterday’s [Networking meeting](https://hackmd.io/@benjaminion/rkEn7C_88) into a release today.
* Danny is going to consider doing a “Virtual Interop” in the near future where at least a few people from each team get together, rather than working in silos.  He will come up with possible dates.

## Links
* Ben Edington's Quick contemporaneous [notes of the networking meeting](https://hackmd.io/@benjaminion/BkdbG45II#Eth2-Implementers%E2%80%99-Call-36---2020-03-26).

## Summary
Clients reviewed their testing and research updates in preparation for Eth 2.0, with a focus on cretion of multiclient testnets and the possibility of spec freezes. 



## AGENDA

# 1. Testing and Release Updates

**danny**
So we have a release in the queue. I anticipate that it will go out today. This has some continue networking updates that we've been working through the past about 10 days. It also has fix for two critical bugs, one in testing and one in the rewards calculations. Both of them highlight that it's likely valuable to split the attestation deltas function into some sub functions for more granular testing, because it's very difficult to capture much other than whether the values are going up or down. But if you mess up a calculation in the middle with respect to testing, it's easy to throw off the whole function and not really realize it. So that's coming. This release, because of the critical bugs in the previous one, we can go ahead and say, "use this as your target." Especially with respect to state transition, that's very minor.

I hope you're having a good time working through 2.0.11. I'm sure you'll let us know in a minute. Other updates on testing and release?

[**Mehdi - Sigma Prime**](https://youtu.be/Vn1oHH55yPk?t=373)            
Yep. I've got a Beacon Fuzz update. So we've been working on the Java integration, which is pretty much done. We got the shuffling up and running. We just need a way to disable signature verification on Teku. I'm sure they'll come out very, very soon.

We're revamping the architecture completely. We're actually considering rewriting the differential fuzzer in Rust. So we want to have the ability to swap between different fuzzing engines. We currently only use libFuzzer, but we want to be able to have a CLI that allows us to swap to AFL, honggfuzz, and potentially others. It'll be good to experiment with all of them. We're building out our coverage recording to better measure the efficiency of the structural fuzzing, which is coming together. We're prototyping new fuzzers using Lighthouse first, and we're hoping to have a lot more progress to show you folks in two weeks.

And I'm very excited to announce we're on-boarding a new person to the project: Patrick, who was a security fuzzing expert who started working with us. He'll have a look into Eth2 and all the different implementations. He started on on Monday.

We also found a minor-type error in [unclear](https://youtu.be/Vn1oHH55yPk?t=454) which is not exploitable, at least not directly exploitable, but we wanted to make sure to report it. That's it.

**danny**
Great. Thanks, Mehdi. Proto, anything on your end?

[**protolambda**](https://youtu.be/Vn1oHH55yPk?t=468)       
Slow but steady progress on network testing.

[Section unclear here]

As a proof of concept, we have synced the first 10,000 blocks of Lighthouse testnets.  

**danny**               
Great. Thanks, Proto.

# 2. [Client Updates](https://youtu.be/Vn1oHH55yPk?t=523)

**danny**
Okay, let's move on to client updates. Let's start with Teku.

[**Cem Ozer**](https://youtu.be/Vn1oHH55yPk?t=536)

So we have optimized the [unclear] so that the fork transition is now four times as fast as what we had before. We're now sitting at about 300 milliseconds per fork transition where 32,000 validators with the mainnet coupling. We added a mode where [unclear] finalize state as a quick fix to keep storage from growing like crazy while we've been syncing. We started but not completed work to replace MapDB with RocksDB. RocksDB is out of the box a bit faster than MapDB so we're expecting a speed-up there.

Our [unclear - discrete 5?] implementation seems to be working well on Lighthouse testnet 5. We're working on splitting out a separate validator client. The Rust APIs continue to improve, and we're hearing that standardization of APIs would be really useful, so we're hoping to find someone with the time and effort to coordinate that. And lastly, we're working on a standalone signing service with support for low-end keys from a hardware-supported model. That's about it.

**danny**
Nice. Are you all able to stand up a local test right now with just Teku? Not a public testnet. Have you reached that milestone?

**Cem Ozer**
Yeah, we should be able to do that.

**danny**
Good. Thank you. Prysm?

[**terence(prysmatic)**](https://youtu.be/Vn1oHH55yPk?t=636)
We're basically just working on version 11 and then with the biggest speed share, which is the dynamic at the station subnet. The feature is complete right now, so we just need extensive testing that irons out a few flaws here and there. So I'm told we have a Slasher running in production, catching slashable offenses. We caught our first [unclear] last Friday and verified the external validator was slashed, so that was pretty exciting.

We added continuous cross-testing as part of our CI pipeline. We have seven [unclear] Argus right now, which are tested with [unclear]-based random inputs. We also made a lot of radical improvements on the advanced DB configuration. So now we have a reference service on top of our state DB to maintain both hot and cold access for state, and we will start extensive testing on that later this week.

We'd separated out of initial sync block faction from block processing. We factor initial sync service and then introduce a concurrent model of syncing, so blocks are processed as they are being factioned. And that's it from me.

**danny**
Great. Thanks, Terrence, and congrats on catching the slashing in production.

Nimbus?

**Zahary Karadjov**(https://youtu.be/Vn1oHH55yPk?t=736)
We continued our work on the Discoveryv5 implementation, and we're currently interacting well with the GO implementation and the Lighthouse testnet. We were able to discover 113 nodes there. We've completely dropped the [unclear] daemon from our development branches, and we've launched finalizing a testnet based on libp2p. But the stabilization [unclear] are still underway [unclear] so we're seeing in this testnet.

We've synced with the latest spec, but we still have some pending work on the networking changes.

[unclear, with background noise interference](https://youtu.be/Vn1oHH55yPk?t=790)... from our Ethereum 1 client and integrated in the beacon node, so it now supports RPC endpoints. They're both supported by Lighthouse, for example. We're currently looking I'm trying to fix the description of the multinet repo so we can do local testing with all the clients. Hopefully, maybe some of the other teams will be interested in this as well and we can bring the scripts up to date.

We've done some work on syncing, and currently syncing is working in the libp2p testnet, but there will be more ongoing work in making the algorithm smarter and balancing the requests in a more appropriate way. And finally, we've been upgrading our compiler to Nim1.2, which will be out in the next few days.

**danny**                
Great!

Lodestar?

[**cayman**](https://youtu.be/Vn1oHH55yPk?t=871)            
So we're just finishing up the C5 implementation. We need integrate it and do a few more tests, but it's looking good. We've been spiffing up our two-node local testnet, just fixing some various things. We noticed we had a bug in our gossip validation, and we've been fixing up our API for that. And we've been working now on spec updates. We got a new contributor recently who is helping us out with our web apps. He's gonna be updating simpleserialize.com, and he recently is working on an Eth2 validator key generator web app, and that's nearing completion, too.

**danny**                 
Cool. Thank you, Cayman.

Lighthouse?

[**Paul Hauner**](https://youtu.be/Vn1oHH55yPk?t=946)            
Hello. [unclear] spec version 11, so the majority of the work has been around on getting the attestation aggregation scheme working, mainly from a networking side. So Adrian has being working on that a lot, along with Juan and Diva. Those people have put some new search routines [unclear] to assist with peer discovery and sped up [unclear] queries by adding timeouts and been thinking a lot about handling forks in the networking stack.

Michael has been working on implementing the state transition side of things. We've fiddling with the API a fair bit, trying between the validator client and the beacon node as we implement and figure out better ways we can do things.  We've been working with [Afri?], who has been playing with some of our testnet deployment tools, just kind of the first time that we've had anyone using them except for the authors. That's been really helpful, and we've been submitting lots of really good issues. We did some more optimization stuff around batch verification of blocks. That's about it from us.

**danny**                
Great. Thanks, Paul.

Trinity?

[**Alex Stokes**](https://youtu.be/Vn1oHH55yPk?t=1035)           
Nothing too crazy, other than the kind of stuff everyone else has been working on. We've been working to pull out a separate validator client, so that work is pretty much gone to completion, which is exciting to see. Otherwise, just work on node stability and the v11 spec updates, along with some infrastructure work for single client testnets.

**danny**             
Great. Thanks, Alex.

Nethermind? Do we have anyone from Nethermind today? I don't think so. Okay. Cool.

Something else that I meant to announce earlier is that with this next spec update, we're gonna be re-launching a Phase 0 pre-launch bug bounty program, so we'll get some details on that out soon. Okay, I got everyone, right? Great.

# 3. [Research Updates](https://youtu.be/Vn1oHH55yPk?t=1106)
**danny**  
Any research updates?

[**Musab AlTurki**](https://youtu.be/Vn1oHH55yPk?t=1116)           
Hi, everyone. We have been working on generalizing the Casper model to support dynamic validators. And we have done that. So what we have right now is a model of Casper as given in the [unclear - Gasper vapo?] ...K finalization and dynamic validators. And what we are working on right now is on showing the bone given by the theorem. This is also in addition to the second model in K.

So the K model is an abstraction of the beacon chain transition function, state transition function. And that K model does actually both fixed validator sets and dynamic validator sets. And it also includes partial refinement proofs showing that essentially linking the two models together, showing that the K Mobil satisfies the assumptions that are made in the top level model, the CoC model, in addition to some properties relating to the state transition function.

There are still some other properties that I think still need to be approved, but we are working on those as well. So the point of this effort is to show that the beacon change state transition function satisfies accountable safety and plausible likeness at that level. And then the ultimate goal is to be able to eventually show that the implementation itself satisfies these properties. So that's it.

**danny**                
Thanks, Musab. That's really exciting work. Seems like we're getting close.

Other research updates?

[**Joseph DeLong**](https://youtu.be/Vn1oHH55yPk?t=1289)             
For TXRX, we just had a kind of realignment on some research. I think the general direction now is to move away from EEs as a design for Ethereum 2. It's not set in stone yet, but I think Johnny Ray's gonna move into doing some sort of network monitor, and this would be helpful for Phase 0, being able to monitor the activity of the network and better understanding what's going on there.  And Mikhail just published some research about and Eth1/Eth2 bridge finality gadget. And I think his conclusions are coming closer to the conclusion that I think that the Foundation is already at that a bridge or a finality gadget makes it kind of like an infeasibility. And so I think we're gonna shift into working on the Ethe1/Eth2 merge, more likely.

**danny**                 
Cool. Thanks, Joe. Any other research updates?

[**vub**](https://youtu.be/Vn1oHH55yPk?t=1395)               
I've talked about this on other calls before regarding polynomial commitments, and obviously that Eth3 research that I published a couple of weeks ago, and the thing that I presented yesterday at the Eth study club was basically some improvements to the version that I came up with that removed the need for a sorting argument until the number of constraints goes way down and the entire scheme becomes quite a bit more viable.

**danny**               
Cool. Rapid progress. Thank you. No other research updates? Ok.

# 4. [Multi-client testnet discussion](https://github.com/ethereum/eth2.0-pm/issues/135#issuecomment-601090545)

**danny**
The next item is multi-client testnet discussion. Largely, there are two efforts, the first of which is getting a multi-client testnet up, which we might see a few give birth and die and rebirth.  Our focus today will be on that first effort. Afri, you want to talk about what you've been looking into?

**Afri**            
Yes, thank you for having me. This is my first Ethereum 2.0 call. Historically, I've been following Etehereum 2.0 since early implementations through Casper, Proof odf Work, Proof of Stake, through Trinity, Harmony, and Parity. We've come a long way, and now that the Ethereum 2.0 spec is stabilizing more and more, I still see the need for coordination. I stepped up to volunteer to set up some multi-client testnets, and here I am now, and I want to learn more about how we can assist the client teams. We have resources available. I have plenty of time. I can help coordinating things.

I used the last two weeks to our investigate client capabilities, tooling around, creating testnets and what it involves to create a testnet, and so on. I mainly work with Lighthouse, but I also want to learn how all the other clients are capable of interoperability. I know there was an interoperability multi-client testnet a couple of months ago. But we are now in a phase where we should work toward a more persistent version of multi-client testnets. So I want to learn more about which version of the specs implemented with which client, and what's the start of networking consensus,  validating, what's the status of tooling around creating testnets for each of the clients and what else I am not aware of.

I can spin this out into having separate calls on any of this. I'm happy to learn more about what can be done, and what we can contribute.

**danny**  
Cool. I was thinking you and I could maybe go back force on some of the core requirements and things that were going to be standardized and then share that more broadly. We've done surveys in the past to get a handle on where everyone is at, especially with respect to the core items. So we might do some sort of limited survey again.

As for organization beyond this call, that's likely warranted. I think we're probably at least a couple of weeks out, because I think the version that would like to target is pretty much the head spec today. And people are looking to get there. As discussed on the networking call yesterday, you were working through some of the complexities in this aggregation scheme. Prior to very recently, we were kind of cutting corners there, but we expect to be fully up to the spec very soon.

**Afri**               
Yeah, I believe we might want to have some joint strategy to freeze a certain version, but I don't know what you have done previously. Happy to learn more about that.  

**danny**  
Yeah, long ago, prior to DevCon before we shook up the spec to make some deeper breaking changes based on some conversations there, we did have a spec freeze. I'd like to, with this spec update, freeze the state transition logic. Unfortunately, also fortunately, we at least in the past two weeks, we've seen a lot of conversation around networking, primarily because some people are working through it for the first time and also hitting some of the pain points for the first time.

So we've seen more iteration on that component of the spec, and some of these iterations have been breaking. So it would be hard to, unless we were versioning protocols within the same protocol, it would be hard to freeze that today. I think, likely in the next two weeks, we're still going to see some some bumps on that. So state transition freeze and targeting soon a networking freeze, I don't have a good intuition on how many more changes we might see there, because a lot of it's just been led by the kind of networking experts on each team finding some of the issues. But I know we're getting to a better place there.

**Carl Beekhuizen**
One other point which we may end up changing and which I would like to see a possible change before we start doing testnets is the new BLS specs and v6.

**danny**          
Did that v6 draft get released?

**Carl Beekhuizen**            
Yes. I'm opening the second PR for that as we speak.  The changes are minor from v5.  So I don't see any reason why we shouldn't do that before multiplying testnets.  It's

**danny**                    
The interfaces are all the same for the clients, but the underlying logic is, what, a day of work? Three days of work?

**Carl Beekhuizen**             
A day of work. Nothing has changed in the BLS specs v2. Basically, the old one's expired, so the update was just a version bump.

**danny**                
So what we'll do is this version releasing today - freeze state transition, have it be the tangible target. Maybe release a version 12 when we have this braking signature scehem come in, knowing that the rest of the items are stable. And as clients get up to speed, you can shift the effort towards that.

**Carl Beekhuizen**   
That seems reasonable.

**danny**    
Good that they got the v6 out and those contributors are saying stability, or did anything else come up in the pipeline?

**Carl Beekhuizen**               
Nothing new expected down the pipeline. The only thing I'd like to have seen is test vectors, but otherwise that should be stable.  

**danny**    
We talked a little bit about this recent blog post, and in some of the chats, the intention here is to not allow the ITF standard to be the blocker on the mainnet. And so we will try to implement whatever the latest draft is and ultimately probably try to shake hands with a couple of other Blockchain projects that are also trying to move quickly and conform upon one of the drafts if they have not fully stabilized.

So I think a lot of this conversation is probably gonna be had on some different docs we'll be sharing, things that will try to standardize on and increasingly spinning up testnets, testing sync across clients and things like that.

Afri, is there anything else you want to talk about today? Or there any questions people have about this process or thoughts or comments before we move on?

**Afri**              
I have a lot of questions, but I will be going from client to client and talk to teams, so please bear with me if I have a lot of questions. I just need to learn more about where each of the clients is, and what the tooling status is, and how testnets can be spun up with each of the clients. I will take this offline, mainly, but if anyone has a comment now, just go ahead.

**danny**                
Thanks, Afri. I think it has been valuable to have Afri poking around, so help him out and he'll be likely to help you. Afri, are you flying solo right now or are others in the Gorli Initiative helping you?

**Afri**              
I'm solo right now. The Gorli Initiative is just three people. We have some funding, and maybe the future, we can even have stuff bountied if necessary. We can see where some incentives are required.

# 5. [Networking](https://www.youtube.com/watch?v=Vn1oHH55yPk&t=2140)

Danny just mentioned the Networking meeting the day before and that Ben has some great [notes](https://hackmd.io/@benjaminion/rkEn7C_88).  There are some PRs under review based off of that, and that they would like to get those into a release, today.  (Action Item #1)

# 6. [Spec discussion](https://www.youtube.com/watch?v=Vn1oHH55yPk&t=2189)

We've touched on probably the most pressing items.  I’m sure that there are a couple of political  bug fixes that are coming out. Just keep your eye out on that. And I recommend just immediately bumping to that version instead of finishing out on 0.11.  You won’t be able to pass the tests on 0.11 because the test generation is broken.

Beyond that, on the phase one stuff, Xiaowei has been doing a deep review. There's also been a number of additional test vectors added. So once that deep review is done, hopefully we’ll have phase one test vectors on the get one or two people prototyping.   Some of this work is going to be pivotal for doing some of the Eth 1 Eth 2 integration prototyping work in the coming months. So I'd say once the Xiaowei fixes air integrated, if you have some spare time to some reading and just kind of interested in getting caught up, that would be a good time to check it out. Certainly. I think that's most of the specks on our end. Do other people have any spec related items that they would like to discuss?  From general open discussions  I've been super pleased with the integration of unification of direction, road maps on research and expertise. Super cool to see. Anything else people want to talk about today?

[Vitalik](https://www.youtube.com/watch?v=Vn1oHH55yPk&t=2326)
Nothing for me.

**danny**
Maybe we should do a virtual interop.  Meaning at least a few people from each team one week in the near future. We spend a lot of our time hacking together on things rather than in our own little silos. Does that make sense? Is anybody interested in coordinating that? I know our efforts. When we all got together in person, we were extremely fruitful. Obviously, there is a degree of separation when we’re hanging out on the Internet.

**Alex Stokes**
I think it makes sense.

**Danny**
Cool, I’ll chew on that and maybe propose some dates.

End of meeting

# Attendees

##Attendees:

* Alex Beregszaszi
* Alex Stokes
* Ansgar Dietrichs
* Afri
* Ben Edginton
* Brent Allsop
* Carl Beekhuizen
* Cayman
* Cem Ozer
* Chih-Cheng Liang
* Danny Ryan
* Edson Alcala
* Guillaume
* Herman Junge
* Hsiao-Wei Wang
* Ivan M (Prysmatic)
* Joseph Delong
* Jim Bennett
* john
* Lakshman
* Leo BSC
* Marin Petrunic
* Mehdi Zerouali (SigmaPrime.io)
* Musab A. Alturki
* Paul Hauner
* Protolambda
* Sam Wilson
* Shay Zluf
* Svante Jorgensen
* Terence Tsao (Prysmatic)
* Trenton Van Epps
* Vitalik Buterin (vub)
* Will
* Zahary Karadjov


# Date for Next Meeting: undetermined, perhaps two to three weeks.
