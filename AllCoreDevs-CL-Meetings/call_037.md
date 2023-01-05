# Ethereum 2.0 Implementers Call 37 Notes

### Meeting Date/Time: Thursday 2020/4/09 at 14:00 GMT

### Meeting Duration: 1 hr.

### [GitHub Agenda Page](https://github.com/ethereum/eth2.0-pm/issues/141)

### [Audio/Video of the meeting](https://www.youtube.com/watch?v=aEJ9Pw7yFYM)

#### Moderator: Danny Ryan
#### Notes: Pooja Ranjan
 ----------

## Action items
 
Mike Goldin to create an [issue](https://github.com/ethereum/eth2.0-APIs/issues/24) for the discussion of APIs based conversation: 

* to hash out a proper unified format
* to discuss thing like APIs that are in the Prysmatic repo and any that might lie on other clients to find a set that works well 
* to discuss what migrating from Protobuffs to open APIs look like and also what generating Protobuffs from Open APIs looks like and 
* whether there are some set of tooling things everyone wants to integrate into CI. 
 

 ----------

 **Danny**: Welcome everyone! 

 # 1. Testing and Release Updates
 
**Danny**: We found a small issue in a couple of tests. These actually manifest like it's going to be fine on your own because the test failed and it failed for the wrong reason and that is opened up flip another can of worms discussing whether we should handle this in de-attestation case. This kind of an exceptional signature case. There's an issue and where it's listening to feedback from the client on the spec repo. We could introduce it will be a breaking change the specs state transition when we bump to the IETF standard if people want to do that but we could also handle this exceptional case as it currently is an aspect. So, please take a look at that issue and let us know thoughts on it. On that, there are a couple of clarifications and tightened gossip conditions in the dev spec for networking and I do expect on this is breaking with respect to  v0.11.1 I think sometime in the next week if we accumulate a couple more of these minor networking changes. Non-breaking networking changes are v0.11.2. If you’re interested. Go take a look, There are a couple of PRs. 

Cool, that's going on my end any other updates on testing? 

**Proto**: 
* Tooling for testing has been improving. 
* The Python spec is optimised and running reasonably fast. That’s about 40 slots/sec on Lighthouse testnet.
* ZRNT also has been forked and together if the Rumor tooling and the Network tooling, it’s doing 49 slots/sec with BLS, and 217 slots/sec without BLS. 
* For induced network testing, you can get the introduction and share programs of network testing.

**Lakshman**: Hi guys so I'm working on basically creating a **network testing suite using Rumor**. The ideas that just like simple like feature and like RPC tests can exists in CI as well as a couple of multiclient tests to check as that propagation works. Still the basic infrastructure exists all I'll show you the [repo](https://github.com/lsankar4033/stethoscope) in the chat but still plenty of things together. I'll probably show up in people's discords asking questions about setting up clients. 

**Danny**: Cool, thanks, Lakshman.
Other testing updates? I did see in the chat that Alex has reopened that we’ve been working on and update them 10.1 but I need to dig into the issue. So, take a look there.  

Okay, any other testing updates? 
Great!

 # 2. Client Updates
 
**Danny**: In the interest of clients, as you may have seen the chat, we’re interested in just getting a simple list, what the last things you need to get in place to be able to stand up a single client. These are 11 test net in this if you can just get me a list of those things by tomorrow , will be really helpful with planning in the next couple of weeks in terms of targeting testnets and multiclient things. In addition to that today if you just have an intuition by when you might be able to have these v.0.11 testnets, just let us know. But now proceeding with regular client updates.
 ## Prysmatic 
 
 **Raul**: Hey guys, Raul here from Prysmatic.
 
 * Running v0.11 with real deposit flow. Pending any critical bugs, we likely announce some Genesis time and do the restart within the next few days. Nothing blocking in that direction. 
 * Better slashing detection all the way from Genesis. We now have proposer slashing detection giving the proposer index and blocks.
 * Fully revamped and optimized initial sycn.
 * integrated Beacon fuzz from Sigma Prime 
 * looking for a security audit 
 * We put a RFP, last Friday to know support from Sigma Prime.

We're getting ready to launch things hopefully within 2-3 days, everything will be up. 

**Danny**: Great, thanks Raul.

## Lodestar

**Cayman**: We're 
* still working through the 0.11 changes, 
* we just merged 0.10 branch in the master a few days ago. 
* And we are about to merge in our disc V5 integration so that'll unlock a lot of the ENR based issues.

I would expect that we'll finally have a bare-bones something that we can know that we can spend up and start syncing things too and probably by the next meeting.

**Danny**: Great Thanks.

## Lighthouse

**Age**: Hi everyone
* yes I from our end we've updated everything to 11.1 and 
* as far as I know everything's sorted today. so we finished off all the main net required protocol that we need, so we’re ready for that
* We’re doing some internal testing for any bugs 
* Would also be doing public multiclient testnet for 11.1 with all protocol spec that we need for the mainnet.  
* Other internal things being working on is kind of a more sophisticated peer management reputation system.
* Upgrading to Rust peer management system,  I think we've been working on for a while and 
* we're looking at testing some of the snappy compression stuff that we've done in Gossip sub 
* there are stuff we’re going to try with Rumour
* but would be curous to have a look at the gossip sub as well.

That’s pretty much from us. 

**Danny**: Great!

 
 ## Teku
 
**Meridith**: Hey guys! So the big news for us is 
* we were able to sync to lighthouses testnet and catch up which is a pretty big milestone for us.
*  we made some general stability improvements in the last couple weeks which were crucial in allowing us to catch up. 
* In terms of performance, we implemented some optimization are remarkable implementation.
* we're now able to import about 7-8blocks/sec on average that's with mainnet config 32k validators 
* we also finished implementing a new RocksDB backed database, which also gives us a little bit performance boost
* We’ve done some work to improve attestation aggregation in particular we fix some issues with block creation which were causing us to fail to include a lot of attestations.
*  we're just now starting to look v11  but we should be ready for a v 11 testnet in couple weeks

That’s it from us. 

**Danny**: Thanks, Meredith. Congrats on the sync.


## Nimbus

**Mamy**: So, 
* in terms of spec, we are now at 0.11.1.
* We also checked that we are compatible with Eth1 state deposit
* Proto array based fork choice is almost ready and tested. It’s not integrated in block pool or attestation pool as Genesis.
* On benchmark front, We did BLS benchmark suits and we provide mobile benchmark on phones and on Raspberry Pi soon.
* On fuzzing, we’ve a codebase a workaround to skip Merkle proofs, so that we could fuzz the consensus fork because we had issues there. Now we don’t need to have this skip Merkle workaround. 
* On the Networking front, we worked a lot on the stability related to P2Pand
* we are still working on some edge cases in block syncing.
* In terms of features finished, largely P2P is almost done, Snappy support is live
* On the Discovery front,  we can discover and be discovered by Lighthouse and will be working on the refinement.
* In terms of testnets,  we are currently trying to connect to Lighthouse but, found a case where we’re in consensus with CLI but not with Lighthouse. This is under investigation. 
* On general codebase, we’re revamping a lot.

**Danny**: Great, thank you!
 
## Nethermind

**Tomasz**: On v0.10. Now working on synchronization on session management.

**Danny**: Cool, thank you!

## Trinity

**Alex**: Mainly working on 
* node stability of the clients and then also the v0.11 updates,
* nothing too exciting on the testnet front but 
* definitely should be ready to join the next couple weeks.

**Danny**: Great, thank you!

**Danny**: Musab from Runtime Verification, do you want to go for any update?

**Musab**: Nothing much in particular, we're still working on the modles, the Coq model showing essentially the theorem bound, what is slashable and with dynamic validator sets. And the K-model giving the  abstraction of the state transition function of the beacon chain and linking these two. The work is ongoing and we hope to be able to share this work with everyone within the coming few weeks. 

**Danny**: Great, thank you, Musab! I think I got everyone there.

## 3. Tesnets

**Danny**: Afri or anyone wants to speak about testnets and kind of interim phase were people are getting up to this testnet spec. Any update you want to share?

**Afri**: Yeah, sure, I can give some comments on what I've been doing the last two weeks.  So last time I was setting up a lighthouse based testnet and in the meantime, I was able to make Teku synchronized to it. Right now I am figuring out if I can also add Teku validators.   In the meantime, I break the testnet. Due to some network fragmentation, I discovered, first I lost finality then I lost the ability to see new blocks. So I am in the process of resetting this entire testnet. I am trying to find out what it is capable of, it’s kind of a roadblock for now. I am focusing on client testnet on v 0.10 spec in a more stable way.  Therefore I am focused for Lighthouse and Teku first but I am looking forward for stable releases for v 0.11.1 spec  in all clients so we can eventually brought this up to more client. I put my config on GitHub on [Schlesi](https://github.com/goerli/schlesi). If someone wants to join us, just hit me up.

**Danny**: Great, thanks. Any questions for Afri?
Cool!

 ## 4. Research Updates

**Danny**:  We will move on to research updates. Who wants to get started?

### Quilt

**Will**: I can chime in here. Will from Quilt. I want to give update on some **phase 2 stuff**. 
* You guys should be hearing some announcements and releases soon.  But through Stanford blockchain, Eth CC Paris, a lot of interesting discussions and developments. 
* One of the things that we have been working on just general e-logic execution environment and some of the things that we're looking at ways how do we make the state provider network works? How do we change state dynamics, so we’re looking at SSA vs DSA to make things a little bit more effective? 
* There’s a lot of interesting works that we did around that. And also keeping the core protocol layer alive which decouple some of the account logic from some of the client logic, that kind of give some of the gap periods. 
* One of the things that were trying to figure out is how we can support getting phase 1.5, a practical system as soon as possible and kind of avoid waiting for another indeterminate waiting period and so we have this full new model ready. So what we've looked at is just trying to be a little bit more practical and have a phased approach to getting ease and moving that forward. I'm starting off with one of the first chunks and so what we're looking at is that initially starting off with the case study and **introducing account abstraction into Eth1** and some of the Eth1.x efforts. That gets us a big chunk of the way towards EEs and some of the models around EEs. We are looking at that and also have migrate Eth1 into SSA as well from DSA. 
* One of the things that also like the eWASM team has been looking at is this **concept of Eth1.x 64** and this is where you have Eth 1 and you continue to upgrade the functionality of Eth 1 running on the 64 shards and running on a determinate number of shards. So, we have been supporting some of that research, working on some data find works so that we can access some data and see how functions of some of that is? 
* So, one of the questions would be, in this phased approach, do we have Eth 1.x 64 or do we create a new execution model from the ground up? If it’s a little bit too difficult to make new upgrades that we want to apply Eth 1 and so that is in progress. That decision would need to be made. So yeah that's where at. So some of this work around account abstraction could answer some of these questions. So just **trying to get us to the most functional Eth 2, phase 1.5 as soon as possible**. Otherwise we’ve also been working on the Eth2, so that’s been moving along and that’s become main as well and trying to get feedback on that. That’s been going through the Moloch DAO soon, and will also have Gitcoin grants.

**Danny**: Cool, thanks Will.
I posted a write-up on how the [relationship between Eth 2 and Eth 1 client](https://ethresear.ch/t/eth1-eth2-client-relationship/7248) and such a merger, single-chain merger. If you're interested in that ongoing work and getting involved in prototye and spec, take a look at that. 
Other research update.

### TXRX

**Joseph**:  Hey, this is Joe from TXRX.

* Working on **Eth1–Eth2 merge requirements and constraints documents** and that should be coming shortly but we’re still in progress right now. 
* We've updated our Mothra which is like this libP2P in a wrapper. So that you can kind of like control it, the latest spec version and that’s part of our work to build this network monitor called PRKL. 
* So to that end we're also updating our stimulator for disc V5 and as we mentioned before our fork Choice tests.

**Danny**: Cool, thanks Joe.
Other research updates?
  
**Vitalik**: Do we want to talk about **hashes in polynomials commitments** at all?  
* I guess the main updates there has basically been that all we've been pushing forward on both the front of  figuring out what the benefits would be of completely replacing Merkle Tree with polynomial commitments? And we've also worked out that with some of the more recent techniques, we can basically verify hash functions inside of us Snark or Starks in a number of constraints. And so both of those paths are potentially played by quite viable alternatives to the Merkle trees.
* Potentially even in a fairly short-term, it will make sense to re-architect phase 1 with soem of these ideas in mind, a couple of months or whatever the work on that on. Those kinds of other parts of phase 1 starts are in need to kick off. 
* The benefits basically are that you get much smaller witnesses, you get a (?) codes for free. We’re also considering mechanism where you can have a self verifying **proofs of custody** so you don’t need to have a (?) reveal or challenge games.
So that's all been moving forward.
 
**Danny**: Cool, thanks Vitalik. 
Felix anything on your ends with discovery or otherwise, you’d like to fill us in?

**Felix**: Yeah, I just came out of a call with the research group that I've been talking to and they’ve started working on creating a simulation as well. Although the goal there is mostly like to figure out the algorithm for the topics.  So this is kind of something for a little bit later and we are pretty much done now getting the grant proposal together for this work and will be submitting I think at some point and then they can start working on the grant. 

Yeah, even right now I mean they've basically been researching little bit like what could be ways to do the topic in next sort of simple to understand way and yeah they had some good suggestions already and 
other than that we’ve merged the Go implementation into Ethereum master branch and I'll just keep working on it.

**Danny**: Cool, thanks Felix.  

**Justin**: One update from me is something I floated it a few months ago but basically **Supranational** which is the the main team working on that the VDF project. They are very much into the performance computing and basically, they proactively started implementing BLS12-321 library which is performance oriented. The key goal is to be friendly to the formal verification. And it looks like we will have a  basically another three-way collaboration to develop this library between Supranational, Ethereum Foundation and Protocol Labs. 
In terms of the performance, for what they have implemented so far. They are **faster than Herumi on every single operation** like small performance game, maybe 10-20% faster but kind of the more exciting thing is that there has been kind of new ideas in terms of batch operations.
It seems that the Herumi is mostly interested in performance when you do operations  one by one. That if you do operations in the batch, which is better then for Eth2, then you can get even more performance.
In the absolute best case, I think **potentially this [library](https://github.com/status-im/nim-blscurve/blob/master/blscurve/bls_signature_scheme.nim#L205-L248) can be 2X faster than Herumi**. 

**Mamy**: To add to the performance parts, I have been discussing with them on the batch API. It’s actually, once you have the primitive of that pass, it's basically use init update and finish scheme , that’s what I propose to them. This is similar to SHA 256 hashing and with primitives, you can easily add any kind of batching on top, like batching checking proof of possession, maybe dealing with public keys on messages that come as a pair or maybe as the different arrays, and this is very flexible scheme and you get final exponentiation and delayed (?) loop that you keep to get all the performance. I can share my repo, my implementation. I suppose we will go something like this, already  we have new optimisation. 

**Justin**: yeah at this point we’re trying to incorporate all these ideas and it turns out there's a lot of ideas for optimisations here because they have talked to various implementers team including Lighthouse and your team.  I think what we'll do is we'll write down in the contract something that seems reasonable as a first attempt but having to work with them on the VDF project where we’re extremely flexible and basically do what’s best for us if kind of requirements change over time.

There’s a quick **update on the VDF project**, the team now have it delivered both the academic paper, it's available publically and the implementation which is publically available on the GitHub and the Apache License. 

We're basically going to start, hopefully soon - review, Security reviews on everything they built.
In terms of performance, they have performance goals for over a 1000 participants. An order of magnitude larger  than anything that has been done before in the context of these NPCs.

**Danny**: Thanks Justin, any other follow up questions for Justin? Timeline?

**Justin**: yeah definetly, they have actually been working on it for several months and they already hired someone, basically full time to work on this even before the contract closing so yeah they're very proactive and yeah I definitely expect the code to be usable this year. Probably not in Genesis, but it will be a good hopefully, a drop in replacement for Herumi at some point.

**Danny**: Great, thank you.
Other research updates? 

 ## 5. Networking
 
**Danny**: Next up is networking, happy to discuss any items or issues run into.  I will give this mature after this call, whether we’ve an appetite for doing a networking dedicated call next week but that would certainly be one following week. But today, any networking things anyone wants to address?
Great!
 
 ## 6. APIs
 

**Danny**: Independently working on some APIs but at the same time also attempting to conform to the API repos. I think the out layer there is that Prysmatic has an independent [repo](https://api.prylabs.net) written in  protobuf that has got some traction with some integrations. I think others have also been implying with  Lighthouse  APIs up-to-date. 

Some, from Infura suggested to port the  protobuf as the canonical spec release as a starting point and generate Eth2 API based upon it. There is an ongoing conversation going on this [issue](https://github.com/ethereum/eth2.0-pm/issues/141#issuecomment-611072786) about this and we’ve also hash this out a few times before.  It seems like people would rather write in HTTP and migrate to protobuf and vice versa if the goal has to have a robust http API.

Another thing that I would like to address is the **Hex strings for byte**. I saw in some discussion on the Prysmatic repo and that was one of the sticking point for not wanting to (?) and Beacon to collaborate on the Eth 2 APIs repo. So, a few things:

(i) Does (?) of open API, HTTP APIs in this repo with CI which checks bills against migrating the protobufs, so that we can have good specs in both, does that meet our standards?

(ii) Am I correct in understanding that that was one of the main sticking point and the other sticking point for not bringing Prysmatic fully into the folder and collaborating into the single repo. 

So, the questions
* Are there issues with using open APIs and as someone suggested adding in, well one doing the due diligence on what it looks like to actually build  from protobuffs from the open APIs?
* If that is reasonable, adding that into CI and make sure that we can actually have this kind of dual conformance?
Thoughts on that?

**Age**: We just had a quick look that you could convert an open API into protobuffs, didn’t actually use it to an extent that I’d know about. 

**Danny**: One of the issues on both that we have types that aren’t well-represented necessarily on in JSON or Protobuffs and another option and the one that I have not had positive feedback on but I will throw it out there is to define everything in SSZ  and define a standard function to migrate them to either or, but that doesn’t necessarily get us all the way there and it's certainly an option format and strange decision.

**Mamy**: Maybe this is something important enough to have a call. If we don’t do the networking call next week for example, can we have call on API next week?

**Danny**:  I'm happy to do that. That would allow us to also lay out our arguments a little bit more and hash it out.

**Preston**: Hey Preston from Prysmatic here. We’ve been following the thread I haven't caught up on it this morning yet but we haven't tried to use open API to Protobuff, with that said I don't really see any issue with that just about every field in JSON is a string; so just so it would need some way to distinguish between this JSON string is unsigned 64-bit integer and this is some kind of byte array. To point of about Hex string vs Base64, I would say it's not a complete blocker. It’s possible to for us to use Hex string,  it's just that we would have to ride a little bit of conversion tooling and that would just take some time which is kind of been the hurdle that we haven't wandered across yet because if we don't need to come at that time and we don't want to. So, all things are possible here it's just a trade off.
 
**Danny**: Do you currently expose a JSON at any point or just Protobuffs right now and your bytes are in Base64?

**Preston**: Yeah, that’s the default.

**Danny**: Understood.

**Raul**: Danny, adding on to that as well, open API recommend using Base 64 binary data strings over APIs. So we've been sticking to kind of like the recommended standards under documentation.

**Danny**:  Yeah, understood. As I mentioned, that I don't really care that much about the bytes format. If we can get conformance across clients and change the byte format, I think it  was a decision made to have conformance with Eth1, but we’re not using the same fundamental structures of the APIs as well. So, we can discuss that a little bit more and discuss it. I do think that we have an opportunity to unify the efforts here and have a better experience for people that are kind interact with these clients. I think almost everyone here has this goal, so let's have a concerted effort to take his conversation to an issue and as Mamy suggested we reconvene on Wednesday to hash out any remaining items. Does that seem like a good idea?

**Mike**: I can create an issue to start that conversation.

 **Danny**: Thank you. 
 
Some conversations:
* Proper agreed upon structure, agreed upon what would be represented in the repo, how would be edited, how the CI would do?
* The other is there are existing APIs in Prysmatic APIs repo and there are a few different APIs probably hanging out with Lighthouse and other clients that users will begin to use a little bit. 
A part of conversation is to have a structured conversation about what's we’re ppulling from these APIs to bring into a common place. I know there’s a bit of stuff in the Prysmatic repo and I think there is some stuff sitting in some other repos too. They are probably doing pretty similar thing, we kind of conform a bit. 

**Mike**: I’d like to add our concerns from the INFURA side, the reason that we're approaching this with a bit of urgency is; there is good work in theEth2 APIs repo, specifying validators API in open API. There's nothing in anything specifying the broader Beacon chain API. Because Prysm already has that, so maybe that is a good starting point. But ultimately we’re happy to support any effort to unify the APIs. 

**Danny**: Agreed, I think the second part of the conversation is expanding these APIs and user APIs and probably using a lot of Prysmatic stuffs as a starting point. Thanks, Mike. 

**Jacek**: What if they want of conversion from Prysmatic to whatever Swagger, where would that land us? Would we gain any insights from that? I mean there were two things available. 

**Danny**: Certainly valuable. You know, sometimes tooling like that ends up with unreadable garbage and sometimes it’s nice. We can try that out. 

**Jacek**: That could be an action item before the meeting next week. 

**Preston**: Hey just one quick thing on that we have already generated Swagger documentation https://api.prylabs.net. So you take a look how that looks, it’s not too bad, but let me know.

**Marin**:  From Loadstar like the descriptions, comments, restrains and other stuffs. It is just as basic stuff as possible.

**Danny**: Got it. So you’re saying that  the original stuff from Prysmatic as the generator is missing?

**Marin**: Yeah. Basically we separated all the types and everything so it's easier to maintain in the Eth2 APIs and when we generate you just get one blob with all those stuff incorporated so it's hard to like separate types and reuse types. 

**Preston**: yeah and I think that it doesn't generate any validation so I think you guys have like this is a field of this link Foundation within the open API spec. The thing that we are using does not do that. 

**Marin**: Yeah but the endpoints should be pretty easy to copy and just use the existing types instead of like autogenerate one. 

**Danny**: Open up an issue to hash out a proper unified format. We're going to open up an issue we can discuss thing like APIs that are in the Prysmatic repo and any that might lie on other clients to find a set that works well. We will open an issue to discuss what migrating from Protobuffs to Open APIs look like and also what generating Protobuffs from Open APIs looks like and whether there are some set of tooling things everyone wants to integrate into CI. 

Very likely on Wednesday we will conviene for what is hopefully routes of the call 30 minutes or so, we can hash out everything that we’ve been discussing in the past few weeks, at that point. 

Thank you Mike. These are something that I think has been in the back of my mind and happy to bring it all together. 

## 7. Spec discussion

**Danny**: Anything pop up in your work on the spec recently.  I know that's a very tiny portion to work these days?

Okay, a reminder [Bug Bounty program](https://notes.ethereum.org/@djrtwo/phase0-bounty#Severity-levels-and-rewards) is out there. Find some bugs, people on the internet, bring it in. Be in touch.


## 8. Open Discussion/Closing Remarks

**Danny**: Okay anything else people want to talk about today?

**Pooja**: There is one request from the Cat Herder team. This is Pooja from the Cat Herder's team. There is this [survey](https://docs.google.com/forms/d/e/1FAIpQLSeadXscoQgrKznUOAEB_jSzNNFKHWDEFJxKH1LpDsDsC6mXpw/viewform) shared by Edson that is avilable in the comment section of the agenda to collect some basic information about liking, frustration, fear and suggestions about the current EIP process. We'd appreciate developers taking out a couple of mins to fill up the survey. It will help the EIP improvement group to prioritize and discuss issue and mitigation plans to improve the current process. I understand some of the developers in this call are also participating in the Ethereum 1.x call. So it would be super helpful for us if people take out a couple of minutes to participate in the survey. 
Thank you!


**Danny**: Yeah, absolutely, I just dropped the [link](https://docs.google.com/forms/d/e/1FAIpQLSeadXscoQgrKznUOAEB_jSzNNFKHWDEFJxKH1LpDsDsC6mXpw/viewform) in the chat. Thanks!

Okay, if you can, please send me a list of the items left to be able to have a fully conform v0.11 single client testnet and if you have any estimate on when you think you're a real stand-up that single client testnet. We’re trying to keep things moving on to the multi-client testnet front. 

Thanks everyone. We’re planning to have this meeting in two weeks. We will have a APIs discussion on Wednesday and very likely the following week we will do a Networking call, but will address that about in a week.
Thanks everyone, bye!


 # Date for Next Meeting: April 23, 2020 at 14:00 UTC

 

 ## Attendees

* Aditya
* Afri S.
* Age
* Alex Stokes (Lighthouse/Sigma Prime)
* Ansgar Dietrichs
* Ben Edgington (PegaSys)
* Cayman
* Carl Beekhuizen
* Cem Ozer
* Chih-Cheng Liang
* Danny Ryan (EF/Research)
* Hsiao-Wei Wang
* Jacek Sieka
* J (Joseph Delong)
* Justin Drake
* Lakshman Sankar
* Mamy (Nimbus/Status)
* Marin Petrunic
* Meredith Baxter
* Mike Goldin 
* Musab AlTurki
* Nishant Das
* Preston - Prysmatic Labs
* Protolambda
* Pooja Ranjan
* Raul Jordan (Prysmatic)
* Sacha saint-leger
* Tomasz Stanczak
* thezulf
* Vitalik
* Vlasov Alexandr Vladimirovich

 ## Links discussed in call:

* Danny: [Agenda](https://github.com/ethereum/eth2.0-pm/issues/141)
* Proto: issue 1713
* Mamy: https://github.com/protolambda/not-a-client 
* Lakshman Sankar: https://github.com/lsankar4033/stethoscope 
* Proto: @mamy https://github.com/protolambda/not-a-client is the zrnt lighthouse sync experiment. hope you like the name, haha
* Danny: https://github.com/goerli/schlesi
* Mamy: I think the repo would be best under the https://github.com/eth2-clients umbrella. we’ve been working to revive the starter scripts in there
https://ethresear.ch/t/eth1-eth2-client-relationship/7248 
* Preston: link to the BLS library Justin mentioned?
* Mamy: it’s not opensource yet init/update/finish scheme for batch BLS operations: https://github.com/status-im/nim-blscurve/blob/master/blscurve/bls_signature_scheme.nim#L205-L248 
* Mamy: and how to use it for various aggregation scheme is below and this can be used for keys/messages streaming from the network 
* Preston: ah ok, wanted to try it early. any way to get private access? 
* Mamy: I’m not sure, we’ve only had discussions on our needs. 
* Mike Goldin: https://api.prylabs.net
* Mamy: https://api.prylabs.network/ <— I got .network from the blog post update

