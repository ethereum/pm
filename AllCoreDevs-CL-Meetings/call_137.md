# Consensus Layer Call 137

### Meeting Date/Time: Thursday 2024/7/11 at 14:00 UTC
### Meeting Duration: 1 hour
### [GitHub Agenda](https://github.com/ethereum/pm/issues/1096) 
### [Audio/Video of the meeting](https://youtu.be/IXgfhk_bFwA) 
### Moderator: Stokes
### Notes: Alen (Santhosh)

## Summary <!-- omit in toc -->
Summary | Description
-|-
137.1  |**Pectra Devnet 1** CL and execution layer (EL) clients are ready for the launch of Pectra Devnet 1. Developers expect to launch the next testnet next week. A developer by the screen name “pk910” said that his team, presumably the EF Developer Operations (DevOps) team, is testing client combinations between Nethermind, Geth, Teku, Nimbus, Lodestar, and Grandine. EthereumJS and Lodestar developer Gajinder Singh noted that the EthereumJS client is already for testing on Pectra Devnet 1.
137.2  |**PeerDAS Devnet 1** EF DevOps Engineer Barnabas Busa shared that CL client teams are working on fixing bugs from PeerDAS Devnet 1. Once all client fixes are in, Busa said developers plan on relaunching PeerDAS Devnet 1 hopefully by the end of the week. Stokes shared an update on his pull request (PR) to change the hard coded blob gas limit on the EL and CL. He said he is working on delineating the impacts of this PR on the CL vs EL and formalizing the changes into an Ethereum Improvement Proposal (EIP) for potential inclusion in the Pectra upgrade.
137.3  |**Fork Choice Testing Update** The TxRX research team at Consensys has implemented an initial version of their fork choice test generator. The test generator is intended to identify bugs in client software that may result in a chain split and any areas where client software may deviate from CL specifications in a non-trivial way. This is research supported by a grant from the EF. The team, represented on the call by Alexander Vlasov and Mikhail Kalinin, requested feedback on their work as they seek to refine test suites and enable more flexible test generation. 

**Stokes**
* Okay. I think we're good there. And here's the agenda Okay, great. So, everyone, this is, consensus layer call 137. It is issue 1096 in the PM repo. 
And yeah, let's go ahead and get started. 
* The agenda is pretty light today, so hopefully, yeah, we can get through everything. So first off, I want to start with Elektra, in particular Devnet 1. I think most CL clients are ready for Devnet one. does that sound correct, everyone? 
* Getting some thumbs up. Okay. I'll assume your thumbs up. Mean means your client is ready to go so then. 
* Otherwise, I think last time we were waiting on some L clients to be ready. that being said, I think there are a couple that are ready for Devnet one, so I would suggest we go ahead and launch the Devnet as soon as we can I think, Paul and Barnabas are out this week, so they are usually the ones doing that. But that being said, I think we can, launch it as soon as we're ready. Does anyone oppose that? I think even if there are other EL clients who aren't quite ready, they can just join when they are. Okay, there's a ball pit. We can't hear you. Oh. There's Barnabas. 

**Barnabas**
* Hey. Maybe I can quickly join in. we are currently testing with, Teku Nimbus, Lodestar as the consensus layer clients, and Nevermind and Geth as the execution layer clients. And when looking at the, interop chat, I've just found an small issue with, Nimbus that should be looked at. But if any other client is ready, please share your client image that we can add that to the testing. Apart from that, all other clients are fine so far. 

**Stokes**
* Sounds good. cool then. Yeah. I mean, I would suggest we start Devnet one next week if Yeah, that's not possible, then I think definitely by the also, it would be the next ACDE next week. Yeah. I think as soon as possible. And, yeah, we'll keep picture moving along. Well, one second. okay. Yeah. Anything else? on Pectra or devnet one that we should need to discuss right now.

# PeerDAS [6:20](https://youtu.be/IXgfhk_bFwA?t=380)
**Stokes**
* In that case, we will turn to PeerDAS, so I don't know if anyone here is on the breakout call the other day. but it sounds like things are moving along. I think there are some issues with the devnet that they had. but the plan is to move into the next devnet. anyone have any updates they would like to discuss? 
* Yeah. So we have Devnet one running now, and it's currently forking away from every every client, from every other client. So we really don't have a good. Uh devnet one, we were thinking about relaunch and on Tuesday we discussed that we are going to be planning for a relaunch, by the end of the week. So hopefully by tomorrow we should have, client fixes for all the different issues that have arise on Devnet one. 

**Stokes**
* Okay, great. Cool so otherwise, I have a small update. I had a PR to start to uncouple having the accounts set on the CL and EL after some discussion there, what we landed on was that essentially the check, even right now for the maximum in the EL redundant. Just given the way the engine API works and the checks CL already does. 
* So the plan there is to actually keep the maximum check just with the CL that does not need to be sent across the EL, because it kind of already happens indirectly with the version hashes. 
* There's in the question of the target, the target. If we want to have the CL sort of derive, this value will need to be sent across the engine API in the same way, and also be included in the block header.
* So that will look like an EIP that presumably we would include in Pectra or sometime in the future. And yeah, I have had not I have not had time to get that together. But yeah, just a quick update there. That's where things are at 

**Mikhail**
* I have a question on that topic. related to this and, this, PR could you please give us a quick summary on why can't we, compute the Bob gas price on the CL and do the validation and send this value to the EL, right. Because, yeah. Because in this case, we would not need to add another field to, to the block header. As far as I believe, we would just we could just repurpose the excess, field  to keep this, price. I don't know if it would work,

**Stokes**
* Yeah. No, that that sounds right. I mean, the main pushback with so there is this PR that we dropped, it's specs issue or PR 3800. So this one is just basically handling like these max and target values, leaving all of the fee accounting and calculations with the EL itself. There was another PR from Denkard to basically even go one step further and pull the fee calculations into the CL as well. 
* We can do this I think it violates the sort of, you know, separation of concerns across the EL and CL that we have and generally is nice. So from what I heard is that, implementors with Pc-dos kind of preferred the max and target routes rather than hoisting everything into the CL 
* But it's an option. 

**Mikhail**
* I'm just trying to understand the where is the separation of concerns would be broken in this case, because it's more like the you know, 

**Stokes**
* Just seems to make more sense to have like fees and accounting and all of this within the L, because that's like like the CL doesn't really care about like the blob base fee, for example. Whereas the there's quite a bit. 

**Mikhail**
* Yeah. But I would argue that actually CL cares because CL handles the networking for blobs and blob propagation. So from that perspectiveCL care about this target. And this is why actually, we are our intention is to, have these mocks and target, given by the CL rather than defined on the CL and also, yeah. But from the transaction propagation perspective here is just. 
* Yeah, just one could be one problem, but I don't know how how much, this price is used for in the, blob transaction. Though probably it is important to have, this, this value at hand and to build a block and propagate transactions. In this case, yes. It must be on the EL as well known in advance. 

**Stokes**
* Right. I mean, so the EL definitely needs the target so it can compute the base fee. The base fee is helpful. And the Nimbu and block validation, all these different places. I would say the CL actually doesn't care about the target. It only cares about the max. again, just even more for like, dos concern reasons. 

**Mikhail**
* Yeah I see okay, cool. Thank you. 

**Stokes**
* That's how I'm thinking about it so I'll keep working on the consensus specs, PR, and also any EIP, and, yeah, we will keep those moving along if other people feel strongly about, you know, this other option of having the the base fee calculation pulled all the way into the CL. Like we can explore that as well. generally, from what I've heard again, we want to leave that with the EL. Okay. Anything else on PeerDAS

# Fork choice testing update [13:30](https://youtu.be/IXgfhk_bFwA)
**Stokes**
* The next up we had an update on fork choice testing. let's see, is Alexandr? That's the GitHub handle. Are they on the call? I don't yeah. 

**Alexandr**
* Alex. Yes I am on the call. Okay. Perfect. 

**Stokes**
* You had a presentation? 

**Alexandr**
* Yes. I put the link in. In the chat. Or can you see my screen? Yep. Okay, great. so we have been working on for Fork compliance testing. it's a works supported by a Ethereum Foundation grant. Actually And, okay, so we have implemented a test generator and generated test suites. There is a link to more detailed report on ETH research. 
* And I quickly go over overview of what have been done. So actually there is more work, but we have implemented and implemented initial phase, the generator and the compliance test suites. 
* And our focus was on ease of adoption, minimize surprise to client teams And in particular we keep the same for choice test format without actually there is only one small changes. 
* We added new check which can be ignored initially and next step will be to, work on implementation specific coverage guided fuzzing and using this test suites as seed corpus. And eventually we expect up to 1 billion of test vectors. 
* But it's probably upper bound. Okay So test generator is implemented. Now we have a draft consensus packs or requests to to put it into the wrapper. okay. As I said, it outputs test cases using standard test format. we have also simple Python test runner which can execute the tests using the official fork choice spec. 
* The test generation is parameterized, so there are several parameters, and we can adjust them and generate more tests depending on your needs it's currently one problem is that test generation currently is slow about 10s per test. We know the problem. It's basically a consequence of consequence of compatibility. So we are relying on the existing for choice testing infrastructure And because of that, one aspect is that it's kind of slow. However, it can be run in a multiprocessing mode. okay. I hand over to Mikhail to talk about. 

**Mikhail**
* thanks, Alex. So this slide elaborates on the ease part that Alex has mentioned. So we have added just one more, check or the into the fork choice test format. So the the test generator produces the fork choice test in the usual format. And, yeah, with just one additional property, which is called viable for had roots and weights. 
* And yeah, it can be ignored at the beginning. So, it just can be skipped. this check can be skipped. Yeah. so that's, that's the extension of the format. So it should be pretty easy to integrate this one, next slide please. Yeah. So, now let's a bit circle back and yeah, a bit described how this test generation suite works. 
* So we have three actually three, models, written in Minisink, which is the constraint, solvable solver language. this is one of the models. It gives us an idea of, why do we use it and how it works? I mean, the constraint solver in this particular case 
* So, this block cover model, covers the various, sets of predicates, that are in the filter block tree to define whether the, block is viable for head. So on the right we see the excerpt from the spec. So the predicates are, kind of flags, which indicates whether the, voting source epoch is equal to the justified checkpoint epoch. whether it is, whether this value plus two, is greater than the current epoch, greater or equal to the current epoch. 
* So we we actually give a bunch of, a different set of those predicates one can be false, the other true, and all this kind of stuff. so we give this vector of predicates, to this model as the user input to this model. 
* And this model produces the solution which is written on the bottom. So this is just numbers, and some, you know, yeah some information that will be used by test instantiator, if downstream, which will produce the test, the focus test out of this. yeah. Data and, and some other, Yeah.
* So here what you see is just one solution, but we can ask constraint solver to give us all potential solution, all possible solutions, with the certain constraints on the next slide, yeah, we have a couple of, other models which, used to produce similar information for supermajority link trees and for block trees. yeah. 
* And in the next slide, please. So the test suite config looks like this. there are instances. Instances are those solutions from the model from the given by the constraint solver that we have already seen. there is also the randomness seed that is passed  on the test instance input and the number of variations and number of mutations, number of variations is the number of variations with different with different, randomness seeds.
* And this is just the initial one. So the first one will be derived from, from this one yeah. 
* And next slide please. So how the randomness uh seed is used. so this kind of like the block tree instantiator that, consumes the supermajority and block tree, model outputs and some randomness seed. And for instance, in this instance here, we take this data and we use the, we leverage on the existing fork choice test helpers from the PySpark test suite and produce the, fully functioning a fully featured fork choice test. 
* And, just wanted to mention how this, just want to show how this randomness seed used, here. so this particular instantiator works in two, steps. First step is to create the tree of supermajority links given some certain, model constraints. 
* And, the second step would be to create, to, to build a block tree, based on the most recent justified checkpoint so and on every on these two steps we use randomness to actually partition validator sets, and subsample while data sets that will be built in the blockchain, during the certain period of time. 
* For instance, during step one, we create partitions, validator partitions, to be active during one, to be active during a certain  epoch. So we just yeah, use randomness to sample one or more validator subsets. 
* So it can be two, as you can see in the third epoch, we used two other subset because we need to build to, parallel, to two forks. To parallel forks. And yeah, the next on the next step, this same randomness used to attest to different, block tips and also used to flip the we also flip the coin when we need to, whether this slot will be empty or not.
* And for other aspects of the test as well. But yeah, this gives some, intuition behind how randomness used. And so the with the given supermajority link and block three, outputs from the model, we can apply different seeds and, and actually get get different test cases with different, fork choice, with different weights for each, viable hat and yeah, different and some other properties like empty slots and invalid messages and so forth. * next slide please Now to the test seeds. Alex, do you want to give. 

**Alexandr**
* Yes yes I just switching on microphone okay. So  again more details can be found in the link. we currently implemented  three test suites like tiny small and standard tiny is like for demonstration purposes and small is for initial adoption and probably for small testing. And so and standard is like for main testing and yeah, okay. Standard is 13,000 and small is ten times less. 
* And so on. We also planned to generate extended test suites. However currently since test generation is slow and there is no kind of demand for it, we did not generate it. But we can do that in future if needed. there are also links to tests, in tar format links to the generated tests and yeah 
* Okay, so a couple of thoughts about test groups. we split our tests in a six groups, block tree. It does main testing, kind of, focus on trees, block trees of varying shapes 
* and block weight, is more focused on producing block trees with, variation in weights to kind of to cover, get weight functionality and also have a shuffling group, which focus on shuffling mutation operators and on shuffling basically means that we, shift, events kind of delay block or make it appear later or earlier or drop and duplicate. 
* You can also duplicate messages also have a tester thrashing, group of tests and invalid messages. Yeah. And block cover which covers various combination of predicates from filter block tree method. Yeah. I hand over to Mikhail again. 

**Mikhail**
* Yeah. So we also did, with this test suite. We also did, integrate it in Teku. So yeah, there were there was a question about how fast it is to run those tests. So it's like the standard suite with the 13,000 tests. Takes about 20 minutes on my old Mac, to run, which is, yeah, quite fast. so we have found several issues of different kind. like, there were two edge case bags in the test session. 
* The station processing in Teku. so. Yeah, but they are super edgy and. Yeah, unlikely to happen ever, but still. 
* Yeah. What, what's interesting, is the next one is that, there were a couple of issues, a couple of failed tests that are related to to, attestation processing optimizations. So the spec does not nothing about optimizing attestation processing, but clients do those optimization to prevent spam on the main net, we had the incident, a few months ago, several months ago. 
* So, and yeah, so actually some of those attestations were not processed by attacker, which is fair. Those optimizations are pretty legit. But this is, this caused the divergence, from the test result. From what? What's given by the spec and what what happened in tech also, in Teku fork choice test executor deferred, attestations from the future that is coming from the future for later processing and applies them later on. It's kind of happened implicitly, but it does not differ blocks. And to say that on the mainnet run it would defer blocks and process them as well. 
* But the fork choice test executor, triggers, some those parts of the functionality Teku that would not defer blocks. So we have this kind of to deal with this somehow. Also we, we ran those that test suite with the coverage which just standard coverage, metric. 
* And, yeah, the following functionality appeared to be not covered by the suit. So obviously with that was expected, that execution payload, invalid status and all that is related to it, kind of like remains uncovered because we do not model this in our test, suite. And also there were protera pruning. threshold is quite large, to be hit by our test because we run we produce those tests with minimal configuration. So it would require like mainnet configuration to, to hit these, these yeah. Functionality. And. 
* Yeah, on the next slide, we kind of like, summarize an open questions, to, to all client developers based on our experience with Teku. So how to deal with the first question is how to deal with the messages from the future. 
* So we have several options here and ideally we would like to yeah. If all clients, defer those messages for later processing. then probably this is the way to go. So the suite can do this, and expect that the client will implicitly apply, the corresponding message, when the store time allows to do this, so that that would be the best option, I guess, but there are others to think about, and I believe it's pretty much dependent on, the fork choice test runner implementation in each client and on the fork choice implementation at all. 
* So the other one is how to deal with legit optimization and client implementations. so option there are two options here. So the the first one is to just ignore those tests by each client implementation separately. 
* The other one is just exclude them from the suit somehow. But I, honestly, we don't like the second one because different clients may have different optimizations and some will work. some will not work. So excluding them all would be kind of like, meaning that we do not test some functionality in some client because the other client does not process this attestation for. 
* Yeah, legit reasons. So those are open questions to think about, when you will. Yeah. When this simple, test suite will be being adopted. And next slide please Yeah. So basically that's, that's all we have so far and happy to address questions. 

**Stokes**
* Super cool. I have a quick question like how hard is it or easy is it to, write these constraint models. Like did you find that part was like pretty straightforward? 

**Alexandr**
* It's probably writing models not very difficult, but making them useful to generate tests can be tricky. Like, actually, we originally thought about using some kind of test generator, which just give us a kind of best coverage of state using standard coverage metrics like branch or statement coverage. 
* But in in case of our choice, it's not very interesting actually. I mean, it's easy to get. And so we come up with this solution to use model based coverage. So for example, we have several predicates in filter block tree. 
* And we want to cover various possible assignments of true and false values to these predicates. And of course some of them are not probably possible. They can be excluded by some checks in code, but we want basically to have a test case for each combination of predicate which is possible to instantiate.
* And similarly for blocks, and for trees, we can say restrict us to have like say a tree of 8 blocks and just enumerate all possible combinations of such trees, probably with additional restrictions like maximum child count and so on. And so this models we use these models basically to instantiate models. 
* Okay. Instantiate this enumerate all possible combinations, various solutions to this model. And basically when we generate a test case for each instance this will give us coverage that we want. And writing I mean, it's not difficult just to need to have some experience with constraint programming. Constraint satisfaction programming. It's actually quite convenient I would say. 

**Stokes**
* Gotcha. Thanks. Ansgar and Potuz. 

**Ansgar**
* Not not Ansgar here. Or Ansgar with a different German accent. So regarding the, letting people, or forcing people to, forcing the tests to leave out tests that people cannot pass. So we kind of have a similar problem with the execution, layer tests where we have some tests that we cannot pass anymore because we, for example, we removed the fork choices, that was needed, for pre-merge. So all of the tests that kind of require you to pick between different proof of work chains stuff that we cannot pass anymore, and we just, ignore them
* So I would also go the route of, telling clients like, this is the test suit. And if you if there are tests in it that you cannot pass because of your optimizations, you should just ignore them locally. for your client, but not remove them from the test suit. 

**Alexandr**
* Yeah, it's definitely there will be some, kind of cases where clients do not pass tests, but that does not mean that this is dangerous because, for example, if some message is early delayed and but there are multiple copies of blocks and attestations arriving in practice. So I think many failures won't be real problems and we need somehow exclude them. 

**Potuz**
* I'm just wondering, how hard is it to change the test generator for other versions of fork choice? I particularly have in mind, 7732, but also for PeerDAS, if they eventually go to block slot voting, how hard would it be to adapt it? 

**Alexandr**
* Okay. We can generate basically we can. We are currently generating  and but we also try generating to Altair and Capella and using mainnet and okay we're generating using minimal profile but generating mainnet is possible just very slow. And for other forks basically it should be working. Hopefully it will work. Just need to. 

**Potuz**
* So this these are forks that changed the way that we that change the fork choice logic actually which is not it's not about mainnet or minimal or not the form of the blocks, but actually the way we count attestations and the way we weight the nodes. 

**Alexandr**
* Yeah I mean, it's still probably work because we just generate these blocks and trees and just run the same actions. So I kind of don't know details. Maybe it will require some adaptation, but in a good if you're happy, if you're lucky, it just works. It will just work. Yeah. 

**Mikhail**
* I can add more on this. probably. We'll try. so yeah, as Alex said, it might need to even, yeah, some fork choice changes, some fractures. Surgery might require, adjusting those models, those constraint solver models that we were mentioning in the beginning. But for this, block slot particular case, the empty slots are kind of the product of the randomness seed that is given to the generator. So it probably will be enough just, you know, to to do nothing. And this will probably be enough, having the empty slots. Yeah. 

**Potuz**
* But Mikhail, that's that's very hard to believe. Right. So on the on the block slot, the weight would be assigned to a different to a different node. Right. That's when when you're asking for weights and one of these optional tests, I mean the result would be very different from one model or the other model. Yeah. It shouldn't be a matter of like changing. 

**Mikhail**
* It's not going to be a matter of changing a test generator because test generator uses this back. Actually so it directly calls to this back end if, if this spec has this change, if this spec has the uh block slot, fork choice in it, then the generator will just use it and produce the outputs. Correct compliant with the spec. 

**Potuz**
* very nice, I think I got it. Thanks. 

**Mikhail**
* If there is some change that requires to remove some of the predicates or add new predicates, then we would need to yeah, that's just an example. Then we would need to adjust the model that yeah works with those and probably to improve coverage. 

**Alexandr**
* Probably to improve coverag you also uh may want to introduce changes. 

**Mikhail**
* Are there any other questions 

**Alexandr**
* Okay. If there will be questions you can write us. 

**Mikhail**
* Yeah. Just ask us directly in discord whenever. And also we're keen to see these adopted by, client, different client implementations. we have a PR and Teku. The PR is listed in the references slide to this presentation. So also those test suites are public and we have this PR to the consensus spec repo. So please yeah find a time to try it out to run it. So the presentation slides are. Yeah. Thanks everyone for that for your attention. 

**Alexandr**
* Yeah. Thank you 

**Stokes**
* Yeah. Thank you both. 

---- 


### Attendees
* Stokes
* Tim
* Arnetheduck
* Marek
* Lance
* Micah
* Paul Hauner
* Ben Edgington
* Loin Dapplion
* Terence
* Enrico Del Fante
* Pooja Ranjan
* Hsiao-Wei Wang
* Saulius Grigaitis 
* Roberto B
* Olegjakushkin
* Chris Hager
* Stokes
* Dankrad Feist
* Caspar Schwarz
* Seananderson
* Andrew
* Crypdough.eth
* Zahary
* Matt Nelson
* George Avsetsin
* James HE
* Marius
* Ansgar Dietrichs
* Lightclient
* Stefan Bratanov
* Afri 
* Ahmad Bitar
* Lightclient
* Nishant
* Gabi
* Pari
* Jimmy Chen
* Gajinder
* Ruben
* Mikhail
* Zahary
* Daniel Lehrner
* Andrew
* Daniel Lehrner
* Fredrik
* Kasey Kirkham
* Protolambda
* Cayman Nava
* Stefan Bratanov
* Ziad Ghali
* Barnabas Busa
* Potuz
* Trent
* Jesse Pollak

  
### Next meeting Thursday 2024/7/25 at 14:00 UTC

* Carlbeek
