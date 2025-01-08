# Ethereum 2.0 Implementers Call 38 Notes

 ### Meeting Date/Time: Thursday 2020/4/23 at 14:00 GMT

 ### Meeting Duration: 1 hr.
 ### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/145)
 ### [Video of the meeting](https://www.youtube.com/watch?v=avRcGzfjeIw&feature=youtu.be)

 #### Moderator: Danny Ryan
 #### Notes: Sachin Mittal
 ----------

 # 1. Testing and Release Updates
 


**Danny**: So,from now, we will have our versions more meaningful. So, 
* anything under V0.11. except for that v.0.11.0 which had a bug and we fix very quickly will be backwards compatible. 
* We have v0.11.2 under final review right now to be released today. 

This is not conditions to be on a new epock basis and instead of a slot basis. If two clients were on kind of these disparate cases those are still interopable. So check it out, its PR is under review that will be released today. if anything else, any minor thing come through, that are backwards compatible, they can continue to be released under v0.11.

* v0.12 is coming, v0.12 is slotted, slotted for the ITF and BLS standard, being updated to the next draft. 
 
There's a draft if the hashed curve, that is supposedly eminent along with that there is a couple of type fixes which i think it would ultimately be non substitute and are just fix things not all enter and it looks like there is a additional validation addition being added to fork choice based on some of the old conversations and issues that were picked up. 

v0.12 is primarily the swap of an undelying library. 

* v0.11 tests nets and v0.12 tests nets will not be interoperable. 

these v0.11 tests nets are still very important for testing for potentially getting some users on them like the topaz but ultimately whatever ends up being a long term persisted multi-client test net. Not some of the test nets that we're spending up today will have to target this new ITF standard.

**Question**: will v0.12 come with fork choice tests?

**Danny**: Great question. Andsgar dietrichs is looking into that a little bit and alex is looking into that as well but default is maybe i obviously incredibly difficult time prioritizing us  but its something we have opened up again the past couple days. 
* v0.12 might come with fork choice test  and this is the next point, some modified rewards and penalties tests so debugging lighthouse and prison. 
 
There was another rewards penalties bug found, its currently on the topaz test nets, this is a surprise, 
* There are like 90% of our bugs showed up when we try to get clients to pair.

So, in light of that, that's something we've talked about a little bit  internally but it's a super clear signal that this thing is that massive function is air pump and is probably going to be a source of consensus bugs. 

* Proto and i are working on a proposal to reformat that function into two sub functions to be able to test things a lot more granularly. 

Right now it's difficult for us to write tests because there's a lot of moving parts within that single function. so its difficult to even make sure that you're testing and triggering the right things. Honestly, the bug that we saw, i was a little surprised because i thought that we had it tested so that is something probably the next 24 hours, i'm gonna have a new proposal up to format that function, a new format for tests of that function those are coming, 

* as for the Topaz net there's a bug deployed so you know we're also figuring things, how to restart fork etc

**Question**: we think we're gonna run topaz least for firm for now to consist out some of these issues. We have memory usage and kind of profiling with a lot of activity on v0.11 and we know already that that we have to restart for v0.12 right now because there's like a BLS change, so yeah, that would be our plan tp restart for topaz with this bug fix and in terms of interrupts, we can do some smaller like local test nets or a little coordinated test nets with other clients and then we can maintain a brand

**Danny**: You're right, it is useful to have a bunch of people on there for memory issues. 

* In v0.12 modified functions, it would be a non substantial change and would totally be backwards compatible and you actually wouldn't have to necessarily change any of your client other than the testing harness. i did mention that it would certainly be out by v0.12 but this might be something we might have a testing update to come. actually just next week on the v0.11 to update that testing harness 

So that's the general very long-winded update on releases and testing. Proto, anything else on your end?

**Proto**: I just wanted to note that although it's a critical book, it doesn't really affects users directly. i mean so what's happening here is that if in the attestation belt you can get slightly three different words. right now there's this mistake where monthly faults gets the context of another type of faults and so unless we starts look really deep into the finishing this. We should fix this and it's better to have this fixed and run on the test nets.

**Danny**: Yeah, it's not critical in the context of a single client. It's critical if there are multiple clients. Okay but again, given all of the bugs that we can devote in canada last year, not terribly surprising and this is something that i think we really need to harden against if there's a lot of moving parts in there and getting any balance wrong is gonna cause troubles.

**unknown1**: just to know, the high spec is correct for the i think serenity PI spec lighthouse and do test against nimbus, all of those are the same.

**Proto**: i could get the shorter plans so along with the spec changes. so if recognised along with the spec changes. 

* it's rumored to include these new functionalities as the new RPC types and what not. 
* so client can start testing using that functionality right now but for network tests , we change the direction there a little bit, 

i've seen actively instrumenting and six seven eight different clients is not going to work short term. we definitely try and look at clients and maybe instrument sometimes but to enable network for each of the client, we decided to approach closer and inspect where we have these configuration files reached by all files. define the test and have a client, 

* started the client instruments, the client, if variety in read private key for the network identity, the right features sets at once and then the network, the script, so when the actual test, so those two big fighting tests and looking at all this network behaviour enough that we try and manage these responsibilities between clients and testing infrastructure better.  

**Mehdi**: hi everyone, so the latest fuzzing efforts were pretty prolific, 
* we found 5 bugs on nimbus including they're pretty cool stack overflow, 
* we also found two minor bugs on zrnt (proto has already fixed). 
* we also found the very interesting and critical bug in our SSZ as a visualisation on Lighthouse by the way we published a blog post 
* we've been using honk fuzz, which is a pretty cool google fuzzing engine that allows us to generate interesting samples. 

so basically we are keeping the ones that triggering a more code parks on my house and we are treating them to all the other implementations. i just want to talk about the fact that 

* a lot of implementations out there are treating beacon states, there's trusted structures. This is quite risky if we are potentially moving to a version of warp sync for each two, 

so sinking by B states and not just block patches. so, yeah, there's a lot of we've had conversation around overflow and underflow, so the spec has been clarified which is good. now state transiting, multiple fuzzing engines including honk fuzz will be leveraging our structural fuzzing effort. We currently have a PR in the works to do this a lighthouse and we'll be using the generated samples in the differential processor. so we're going to 

* document all this in a nice design book that will be shared with everyone hopefully sometime next week. 

and we're looking forward to community feedback and that's it.
 
# 2. Client Updates
 
**Danny**: Moving on to clients, lets start with lodestar.
 
## Lodestar

**Cayman**: Hey, so past few weeks 

* we've been mainly working on getting to spec compliance so * we were mostly uptodate with v0.11, 
* the two notable gaps are snappy compression request response and a few ENR thing. 

i think we dont have the eth to ENR flag yet, so we're are working through that and we're also gonna be 

* fixing up out CLI to make it a little easier to run.


**Danny**: Cool,Thanks Cayman and did i see that you all had the state transition merchants be zero alone.

**Cayman**: Yeah,we current master is on the v0.11 .

**Danny**: Cool, that means it's at least some of the core components are useful to developers and things that might want to use it.

**Cayman**: Yeah, for Sure.

**Danny**: Great, Thanks Cayman.

**Prysm**: Hey guys,Prysm from Chris Mathew Labs, so we

* launched our Topaz testnet that has 21,000 validators 
with 3000 and right now 

* we are about 41,000 slots since Genesis 

which was last friday. We had to skip one penality yet except for one incident and the cause has been identified and fixed.And like what was announced earlier 

* we were able to sync Lighthouse until first epoch . 

You'll find a consensus part of our imitation due to number of overflow , so today we'll fix that part and then likely we'll start a new dev testnet for  working Topaz . So far just the amounts  of great feedback on Topaz so 

* we did all our process improvement micro optimizations and making our UX better.

**Danny**: Thanks Terrence.

**Teku**: So, 

* our JVM libp2p Noise implementation is now interoperating with Lighthouse. From what I understand, the Go implementation needs some upstream fixes but then we should be fully interoperate with Prysm using Noise.

* We’ve implemented batch optimizations so one batch verification of signatures within blocks, this gives a modest but worthwhile speedup.

* The protoarray forkchoice algorithm has been implemented and tested using Alex Vlasov’s fork choice tests. 

* We've also reworked our hot-state management in order to keep all the hot state completely in memory. So on restarts we regenerate it by replaying blocks onto the last finalised state. The has improved sync speed by a factor of 3 or so. 

* Our current focus in the current sprint is finishing up all the network changes for v0.11.1. State transition is up to date.

**Danny**: Sounds great and do we have an update on the Go libp2p Noise bug.

**Raul**: Not yet, 

* libp2p requires some fixing  

on the p2p side the peroblem has do with simultaneous handshakes and basically litigated peters doesn't really handle who should be the initatore of the handshake so that's still pending resolution .we're just sopporting (sekai) o ideally, once it's fixed, we will just update to noise and allow the fallback to happen correctly.

**Danny**: Cool

**Trinity**:Hey Everyone, 

* Steady progress on v0.11 testnet. 

There is a lot of internal changes going on with the client right now as this whichever judgement concurrency framework and python but still some progress towards testnets, 

* internal changes to the forkchoice. 

* Some Ops work we've been doing on our team for running Trinity testnets.And we also got an updated BLS (binding)  with Milagro BLS.

**Danny**: Nice, doing some speed.

**Nimbus**: Hi, so on the core part, 

* we switched Testnet 1 to use mainnet configuration. 
* We have some performance improvements to do in particular and performance is dominated by hash tree root.
* We know that we have a lot of repeated hash tree root that we can skip so some focus is on that and also some stack overflows.
* currently we use update and rewind states to apply new blocks to rules, but we are concerned now that this could be a potential DoS vector

if some blocks or attestation are crafted to make us spend a lots of time processing.

* On networking site, we have improved sync algorithm 

and now we've more reliable thinking and 

* we have spents the past weeks also debugging discovery and libp2p and in particular we had memory leaks, some solved and we have at least another one to track down.
* To Preparing for audit, we are removing stale  code and we are improving the handling of errors in all of our four libraries.

On the interrupt side , 

* we fixed the bug that leads to the different genesis between Nimbus and lighthouse 

something that we've talked about two weeks ago. We've discovery between lighthouse and Nimbus  working but we cannot talk yet and we also try to run prysm locally and this part is still work in progress.

**Danny**:Great.

## LightHouse
okay, just regarding Mehdy talking about the database thing, 
* we do call it sparse storage so you store, it's kind of configurable you know, 

you store a full state on say every epoch boundary and then you replay epoch to get the ones in the middle. something we've done is that we 

* the assumption that any block in you database has signatures verified so when we are replaying epoch, we need to verify signaturesso that saves a little bit of time. 

* we also flattened out the state roots  in finalised section.

so its another point is we only do it in the cold section, so we only do it in the finalised area and in the hot section, we keep all of the states there. in finalized, we flatten out all the state routes into their own kind of key, so when we are replaying epoch onto there where we're not actually doing state routes, we already know what the state return to.

Getting into update, 

* we've launched 2 test nets in the last week. 
* 4000 validates test net and 1600 validator test net. 
* There are not quite to be latest spec yet, 

we are still kind of stress testing and testing out deployment infrastructure and agains bugs. 

* we are hoping that we can launch a long lasting 16K test net next week 

but we dont want to do that prematurely. we've motion this long running v0.2.0 branch, so we had, people are getting frustated with ourselves and other people. so thats not in master. 

* so master is now version 11.1 state stansition. 

Full compact for version 0.1.1, 

* we've raised several PRS and the network expects over the last couple of weeksto kind of address things in caches and stuff like this. 

i've spent a fair bit of time learning and 

* using ansible to automate out test net, 

it's pretty cool so i think its kust like SSH automation. there is software to install for its just SSH boxed and you define what you want to do in yanil so we can go three commands from nothing to deploy AWS infra with deposit contract and then you know like root nodes distributed and F distributed validates deposited and the test that started so we've been enjoying that and we're hoping that we can use that, it works quite well for managing multiple disparate test net and so 

* we are looking forward to starting some tests nets with short slot times 

and other challenging kind of thing, so that thing is fully open except for hopefully authentication secrets. 

* Adrian decided to sync with prism, 

i managed to get the RPC working in block side downloading, then we hit the state route thing, we've spoken about that. 

* we made some progress on switching rust latest async programming feature called stable features which gives us an updated execute async executers so we can avoid some blocks we've been having.

* we went and implemented safe arithmetic through the state transition logic 

so we can files with arbitary states. so that goal is to so that their implementation is panic free across any arbitrary state. thinking we're getting close, we're pausing it but hopefully we'll get that soon, haven't found anything yet since that. and to do that michael 

* wrote a rust linter that goes and find unchecked arithmetic, 

we ran it across the code base, already found some interesting mod by zero and stuff like this. we're doing some research on suicide events to see if it's conceivable with our http library so it's looking good so far. 

* we're looking forward to jumping on that standard HTTP API when it's defined 

and finally michael 

* revisiting out slashing production database 

and we're doing some thinking about exporting out so like JSON or some format so that we can transfer validators between my house instances and hopefully between other clients so we'll present that if when we come up with something interesting for that. 

**Paul**: I think paul is managing his another set of ansible scripts who generically deploy across different clients but maybe you can share about some of that in couple weeks. 

## Testnets

**Danny:** I think people gave their individual tests net updates. there's a public test net sent out in prism. i was working on with some test net stuffs. Nimbus has their regular weekly restart test nets and some base interopability stuff going on after you have anything else to update us on. 

**afri**: I have some comments, so two weeks ago I dropped a .10 test net spec in favor of .11 

because most of the clients are working towards .11, i started backward this time 

* tried to bootstrap in network based on teku. 

My main goal was finding out what yet unfortunately i didn't managed to get this test net bootstrap. later i added a lighthouse node to validate its configuration and that brought but eventually i braked it and then i didn't have the time to investigate and was little bit distracted by the Topaz launch and also curious about adding a lighthouse node to topaz but i think most observe things being covered was already experiencing pampy networking.

* we would probably have this single test nets for why because thay saw a good purpose, was according client teams, for interoparability, i would encourage that we have more short-lived test nets so we can pass evaluate any issues that occur at the networking and synchronization consensus or whatever comes up.

so possibly if we could start setting up very fast definites in the future, that would be nice but i believe from the colonizations on disclosure as well, everyone is going to, that's my update. 

**Paul**: I think one thing might be we've the f2 test nets repo is using a config.yml file that describe 

* the test net, it was modeled of the config directory in the spec but that's kind of now full of phase 1 stuff,

that's not particularly really interesting to phase 0 client so i think we're probably gonna see clients, like we're missing a few things from there because its not obvious anymore what is and isn't in it. so there's kind of like 

* no longer a firm reference for what that config.Yaml will should be. 

So, i guess an action for that might be that we're defining that structure would be useful, 

* i don't know whether you want to split it into two parts in the spec repo or we just define another structure for it because we've had abit of trouble like.

**Danny**: I think it's gonna be saying to keep them separate  or to keep them as sub components of one or the other, yeah beacause it's a mess right now.

**Paul**: There is something in prysm that i want to consider too, is publishing one of those because we're having a bit of trouble figuring out, i mean exactly what constants there we know there may not but just we're kind of doubting ourselves when we had the state issue.

**Danny**: Great, we're gonna move on a research.

## Research Updates

**TXRX**: We held our steering panel which is kind of like getting researchers to and that was kind of like focused better and with that 

* we have Mikhail working on Eth1–Eth2 merger doc 

that i think publishing of that doc is imminent and crush our transactions, we are still working throught and put analysis, you have some interesting results when we're sweeping the probability of a cross-shard transaction and that should be released soon .  

* Joe working on cross-shard transaction modelling.

* Jonny working on a network monitoring tool called prkl and he is connected to Topaz and is able to monitors peer and walk the DHT of Topaz network. 

* Alex is continuing on clock sync and he is working on some things around v verifiable pre-compiles for to overcome the earlier Jit problems with execution environments and as well as his PI spec breweries working on fork choice tests 

for based on PI specs so he is wanting to make a essentially a transpiler that will take the high spec and compile it into the languages you know tested to the languages of the clients rather than having to manually modify them and 

* Dimitry is continuing on discv5 simulation and he has got it so you can compare about 14 different metrics.

**Danny**: Cool, other research updates.

**Aditya**: I can talk about my peer right, so paul opened an issue about FFG and Lnd vote in attestation is not being consistent , so i wont describe what the issue is but the fix to it is that when you receive at a stations outside a block
you 
* should check that the beacon block route and the target for attestation are in the same chain.

So this introduces like some new stuff in the fork choice spec, no removals, so it's still not backwards compatible but 

* it should be hopefully minor change to the clients and i put the chat request in the chat if anyone wants to check out what it looks like .

**Danny**: Yeah, cool. Some testing in there and to get it staged for give you 0.12 right .

**Aditya**: The full choice stuff so for trace testing try to get on it as soon as possible , it should be in the next major update in the spec , 

* fuzzy testing seems fine for now but somewhere down the line we also want to test for orchestrated attacks. 

So let's see we can get it in the next major update .

**Danny**: Yeah, cool. There is some ongoing work with Alex from six arts so let's make sure to follow up with him to make sure we're coalescing on one thing , other research items for us.

**Quilt**: Nothing new from the last announcements , we are 

* continuing to work towards account abstraction in the eth1x endeavor and also thinking about eth1x64 

and have been working on just generally getting data so we can start evaluating how we might partition properly current eth1 transactions if we were to expand it across multiple shards.

**Danny**: Perfect timing (Will) for joining us , do you have any update from girls work that you'd like to share .

**Will**: i would like to share the eth1x right up but we haven't shared it yet, i think we did share a version with you Danny just for review but we planned you to really get it out this week .Apart from that 

* there was just a small post regarding the block hash on a tree search which was triggered by the atomic 64 work and could hav esome implementations regarding stateless deuterium buti think it may have more implications regarding the eth1x to merge and i think these are the only visible updates from our side .

**Danny**: They're cool and thankyou, any other research updates, questions or comments before we move on.

**Unknown**: I can talk about the face one recent work so i'm working on two rakat and outdated face one xiaochan issues and try to make the current spec to be updated and i think we've organized to-do list and we will try to finish them in the cup next couple weeks and maybe so we had a kind of the  face one Friesen date last year and now i think it's a good time to make the face aspect to be able as possible.

**Hsiao**: i think especially probably i know some of you began to look at the spec we are working on refining some state transaction cleaning things up testing we're adding the validator guide adding network spec and certainly at the beginning of may 
* if you haven't had a look at it and want to start digesting it would be good time.

Okay other reasearch updates great we did have API call on Monday there is some decision made there was some discussion kind of this extra man proposed a little bit put together for a beacon API and the formation of a small working group 

* to refine that make it as restful as possible and get an updated proposal out there is been some work done there

i'm not sure if there's an update there is do you have anything for us or we're gonna wait watch our next week.

**Danny**: I'll started with small changes i don't know people can see the other tab googlesheet

* there is small changes like we combined a lot of API's into single one because there's lot of naming and other stuff and the different hopefully you can take a look soon and probably pitching some more endpoints.

**Marin:** yeah cool goal is to have as we components of beacon an API  push them out more for public review itertively so definitely get some stuff out show by next week thanks man.

## Networking

**Marin:** Okay we have haven't had a networking call in a bit we had that API call this week instead are they any i know my house has brought a number of small networking changes primarlily around these gossips validation conditions trying to reduce the overhead stuff is there anything else that's come up that you all want to discuss the glaring issues and problem we found the 10 cents with respect to networking.

**Danny:** One thing i have notice that my just view worth meaning there's some issues for this but the block that you could propagate and there's like really 

* lots of different verification conditon but at the station now like the box that can publish on the network

like not necessarily able to be like included aggregation or the communicative language but they can't necessarily be put into fork choice so i just wanted to point out there's lot of different things and we have had to really pay attention to like before we have returning an error on the HS state if someone said it's noted station in it we've got an error adding it to fork choice would be declaring that to be invalid but it is actually valid for an extension you get on the eve gossips to not actually get it your fortress which is something to keep in mind.

**Paul**: Right yeah the condition are first and formost does resistant condition in the gossips and then like for example the black ones very obivious like we don't actually run the state-transition you know we see if the signature checks because that's signal a pretty strong signal that a proposal wouldn't if we see there proposal kind of like someone doing the group work and so there is certainly a difference between fully verifying these messages and just verifying the task resistance stuff so yes there are some disparties there so they are networking things.

## Spec discussion

**Danny:** Yeah great now spec items obviously we talk about,

* proto and i are working on a modified proposal to break up the mega rewards function into better testable components 

so that we can try to some of these rewards problem in the bud but we'll have an update on that soon any other spec things .

**Danny:** Great then open discussion anything anyone has talked about

**Vitalik:** speaking of spec stuff actually, there are a couple of changes,

* we think it's look late to do it for phase 0, they seem like potentially good ideas for phase one 

so one of those was justin's proposal to 

* unify uniqueness slashing for beacon blocks and shared blocks 

and potentially anything else that has uniqueness and the other one was the proposal that i have suggested,

* we tried to maintain an invariant that the maximum possible amount of money the amount of rewards ever everyone gets actually had the base reward divided by the divided by the square root of the balance 

so there's nice and simple formula straight from the protocol for a calculating what the maximum rewards are

**Danny:** so on yours that is true other than i guess slashings in phase zero.

**Vitalik:** i mean fee in phase zero - its slightly untrue the reason its proposer awards right. So right now i think each of the rewards is divided by 5 either of a direct are like five section of rewards that all add up to be its rewards divided by this root of the balance and then there's also the total rewards that are one like the other rewards divided by eight so the proposer reward is actually a portion of the base reward. Okay so i think it's true right now other than this slash a visor being than that changrd the last time.

**Vitalik:** Let me check for grey right now.

**Danny:** yeah so inclusion delay you take the issue work you gave  a portion to the proposer and then you give the rest of it.

**Vitalik:** To good rewards per log is for who write the proposer award as right okay so base rewards for a park is four and then yet base rewardis divided by a four and then they get base reward is added for once for matching source once for matching target once for matching head abd then there's the inclusion delay reward and then let see where does it.

**Danny:** So in inclusion the rewards its first give something to propose it.

**Vitalik:** Yeah okay so again and the reaminder maximally the maximum the remainder can be given by than is scale for the tester right okay and then 

* there aren't any fancy objects and pay zero except for slash but in swash hangs like more in gets destroyed anyway so we don't care right.

**Danny:** Okay so i ain't an immune barriers i think would be valuable for reasoning in phase one.

**Vitalik:** Yeah okay it's good to have in phase one then

**danny:** As for the equivocationsi think there's a little bit of a mixed response my inclination would be if we want it to defeacte proposal slashing in phase one and repalce it at that message.

**Vitalik:** Yeah it seem reasonable and i think justin was under the impression that there was three.

**Danny:** There'd be three uniqueness coming phase one i would one points to but there's no shared of data stations so there's like twoknown objects right now.

**Vitalik:** Right the beacon block yeah

**Danny:** Any other spec things oh sorry knobs back what I've always faster opening session anything else anybody has.

## Open Discussion

**Preston:** Hey Danny just wondering if you could giveus the time lines in the nextupcoming releases are the spec changes  

**Danny:** Yeah so 

* we have two 0.11.2 that is the queue right now that is backwards no to 0 of 1 
* we have V.0.12 which is dependent upon the release of the next draft ITF standard we are in communication with 

the spec maintainer x and they say its imminent but said that weak ago so we're gonna continue knock on their door that would i mean ideally first week in may we can cut this release but i there's little bit of this variable out of our control 

* as for the modified testing of the dispoit and of the reward function that in something that will probably release to be 0.11 which would be totally non substances

we've changed some of the test harmesses as soon as possible so essentially next week.

**Preston:** Ok that's sound great ok thanks 

* 0.12 we think that's version we want to create a bayonet or do we expect any other paint.

**Danny:** Following that the only thing that the only breaking changes through that anybody would be critical security fixes i'm not confident to say that we wouldn't necessarily find any of those there ongoing audits of clients which might uncover things and there's the potential that 
* we run into some bugs on the assessments interoperability testing but barring critical bug fixes the plan is to realese is to be bring that the V-0 12 to make that.

**Preston:** Okay thank you

**David:** As for the 

* we're going to be able to release that IETF goodies near 12 as soon as they release that but there's also gonna be some lag time i'm going these libraries updated
* we'll signal to all the library maintain to once that's out to try get that as soon as possible. 

Oh anything else great then keep up the good work i'm really excited to see all these test set. All right thank you everyone i'll talk to you all very soon.
 

 ## Attendees

* Alex Stokes (Lighthouse/Sigma Prime)
* Aditya
* Ansgar Dietrichs
* Age
* Alex
* Afr Schoe
* Ben Edginton (PegaSys)
* Cayman
* Carl Beekhuizen
* Cem Ozer
* Chih-Cheng Liang
* Danny
* Hsiao-Wei Wang
* Jonny Rhea 
* JosephC
* Joseph Delong
* Leo BSC
* Mamy
* Marin Petrunic
* Mehdi (Sigma Prime)
* Matt Garnett
* Nicolas 
* Nishant Das
* Protolambda
* Pooja Ranjan
* Paul Hauner
* Preston-Prysmatic
* Rauljordan
* S
* Terence 
* Vitalik
* Will Villanueva


 
